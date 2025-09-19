"""
Mystery and Investigation System for Chronicles of Darkness

This system allows staff to create dynamic mysteries with discoverable clues
that players can find through roleplay, investigation, and interaction.
"""

from evennia import DefaultObject, DefaultScript
from evennia.utils import logger
from django.utils import timezone
import random


class Mystery(DefaultScript):
    """
    A Mystery represents an ongoing investigation or storyline with discoverable clues.
    
    Mysteries can have:
    - Multiple clues with discovery conditions
    - Progress tracking
    - Revelation mechanics
    - Access controls (who can discover what)
    - Dynamic content that changes based on discoveries
    """
    
    def at_script_creation(self):
        """Initialize the mystery."""
        self.key = "Mystery"
        self.desc = "A mystery investigation system"
        self.interval = 60  # Check every minute for time-based triggers
        self.persistent = True
        
        # Mystery metadata
        self.db.title = ""
        self.db.description = ""
        self.db.category = "general"  # general, supernatural, crime, etc.
        self.db.difficulty = 1  # 1-5 difficulty rating
        self.db.status = "active"  # active, solved, suspended
        self.db.created_by = None
        self.db.created_date = timezone.now()
        
        # Clue system
        self.db.clues = {}  # {clue_id: clue_data}
        self.db.discovered_clues = {}  # {character_id: [clue_ids]}
        self.db.clue_counter = 0
        
        # Discovery mechanics
        self.db.discovery_methods = {}  # {method: requirements}
        self.db.revelation_triggers = {}  # Automatic revelations
        
        # Access controls
        self.db.allowed_templates = []  # Template restrictions
        self.db.allowed_characters = []  # Specific character access
        self.db.restricted_areas = []  # Location-based restrictions
        
        # Progress tracking
        self.db.milestones = {}  # Key progress points
        self.db.completion_percentage = 0
        
    def add_clue(self, name, description, discovery_conditions=None, elements=None, tags=None):
        """
        Add a clue to the mystery.
        
        Args:
            name (str): Name of the clue
            description (str): Description visible to players
            discovery_conditions (dict): Conditions required to discover this clue
            elements (list): Spendable elements for this clue
            tags (list): Tags like 'incomplete', 'tainted', 'critical'
        """
        clue_id = f"clue_{self.db.clue_counter}"
        self.db.clue_counter += 1
        
        clue_data = {
            'id': clue_id,
            'name': name,
            'description': description,
            'discovery_conditions': discovery_conditions or {},
            'elements': elements or [],
            'tags': tags or [],
            'discovered_by': [],
            'discovery_date': None,
            'prerequisite_clues': [],  # Clues that must be found first
            'leads_to': [],  # Clues this one can unlock
            'location_hints': [],  # Where this clue might be found
            'skill_hints': [],  # What skills might help discover it
            'social_hints': []  # NPCs or characters who might know about it
        }
        
        self.db.clues[clue_id] = clue_data
        return clue_id
    
    def set_clue_prerequisites(self, clue_id, prerequisite_clue_ids):
        """Set prerequisite clues that must be discovered first."""
        if clue_id in self.db.clues:
            self.db.clues[clue_id]['prerequisite_clues'] = prerequisite_clue_ids
    
    def set_clue_leads(self, clue_id, leads_to_clue_ids):
        """Set what clues this one can unlock."""
        if clue_id in self.db.clues:
            self.db.clues[clue_id]['leads_to'] = leads_to_clue_ids
    
    def can_discover_clue(self, character, clue_id):
        """
        Check if a character can discover a specific clue.
        
        Args:
            character: Character object attempting discovery
            clue_id: ID of the clue to check
            
        Returns:
            tuple: (can_discover: bool, reason: str)
        """
        if clue_id not in self.db.clues:
            return False, "Clue does not exist"
            
        clue = self.db.clues[clue_id]
        
        # Check if already discovered
        char_id = character.id
        if char_id in self.db.discovered_clues and clue_id in self.db.discovered_clues[char_id]:
            return False, "Already discovered"
        
        # Check prerequisites
        if clue['prerequisite_clues']:
            discovered_by_char = self.db.discovered_clues.get(char_id, [])
            for prereq in clue['prerequisite_clues']:
                if prereq not in discovered_by_char:
                    prereq_name = self.db.clues.get(prereq, {}).get('name', 'Unknown')
                    return False, f"Must discover '{prereq_name}' first"
        
        # Check template restrictions
        if self.db.allowed_templates:
            char_template = getattr(character.db, 'template', None)
            if char_template not in self.db.allowed_templates:
                return False, "Template not allowed for this mystery"
        
        # Check character restrictions
        if self.db.allowed_characters and char_id not in self.db.allowed_characters:
            return False, "Character not allowed for this mystery"
        
        # Check location restrictions
        if self.db.restricted_areas:
            char_location = character.location
            if char_location and char_location.key not in self.db.restricted_areas:
                return False, "Must be in specific area to discover this clue"
        
        # Check discovery conditions
        conditions = clue.get('discovery_conditions', {})
        if conditions:
            return self._check_discovery_conditions(character, conditions)
        
        return True, "Can discover"
    
    def _check_discovery_conditions(self, character, conditions):
        """Check if character meets discovery conditions."""
        for condition_type, requirement in conditions.items():
            if condition_type == 'skill_roll':
                # Requires successful skill roll
                skill, difficulty = requirement['skill'], requirement['difficulty']
                # This would integrate with your existing roll system
                continue
            elif condition_type == 'attribute_minimum':
                # Requires minimum attribute
                attr, minimum = requirement['attribute'], requirement['minimum']
                char_attr = character.db.attributes.get(attr, {}).get('current', 0)
                if char_attr < minimum:
                    return False, f"Requires {attr.title()} {minimum}+"
            elif condition_type == 'merit_required':
                # Requires specific merit
                merit = requirement['merit']
                char_merits = character.db.merits or {}
                if merit not in char_merits:
                    return False, f"Requires {merit} merit"
            elif condition_type == 'social_interaction':
                # Requires interaction with specific NPC or character type
                continue  # Would need to track social interactions
        
        return True, "Conditions met"
    
    def discover_clue(self, character, clue_id, discovery_method="manual"):
        """
        Mark a clue as discovered by a character.
        
        Args:
            character: Character discovering the clue
            clue_id: ID of the clue
            discovery_method: How it was discovered (roll, social, etc.)
        """
        can_discover, reason = self.can_discover_clue(character, clue_id)
        if not can_discover:
            return False, reason
        
        char_id = character.id
        if char_id not in self.db.discovered_clues:
            self.db.discovered_clues[char_id] = []
        
        self.db.discovered_clues[char_id].append(clue_id)
        
        # Update clue discovery info
        clue = self.db.clues[clue_id]
        clue['discovered_by'].append(char_id)
        clue['discovery_date'] = timezone.now()
        
        # Add to character's personal clue list
        if not hasattr(character.db, 'mystery_clues'):
            character.db.mystery_clues = {}
        if self.id not in character.db.mystery_clues:
            character.db.mystery_clues[self.id] = []
        character.db.mystery_clues[self.id].append(clue_id)
        
        # Check for automatic revelations
        self._check_revelation_triggers(character)
        
        # Update progress
        self._update_progress()
        
        return True, f"Discovered clue: {clue['name']}"
    
    def _check_revelation_triggers(self, character):
        """Check if discovering clues triggers automatic revelations."""
        char_id = character.id
        discovered = self.db.discovered_clues.get(char_id, [])
        
        for trigger_id, trigger_data in self.db.revelation_triggers.items():
            required_clues = trigger_data.get('required_clues', [])
            if all(clue_id in discovered for clue_id in required_clues):
                # Trigger revelation
                revelation = trigger_data.get('revelation', '')
                if revelation:
                    character.msg(f"|yRevelation:|n {revelation}")
                
                # Unlock new clues
                unlock_clues = trigger_data.get('unlock_clues', [])
                for clue_id in unlock_clues:
                    if clue_id in self.db.clues:
                        self.db.clues[clue_id]['prerequisite_clues'] = []
    
    def _update_progress(self):
        """Update mystery completion percentage."""
        total_clues = len(self.db.clues)
        if total_clues == 0:
            self.db.completion_percentage = 0
            return
        
        discovered_count = len(set().union(*self.db.discovered_clues.values()))
        self.db.completion_percentage = int((discovered_count / total_clues) * 100)
        
        # Check if mystery is solved
        if self.db.completion_percentage >= 100:
            self.db.status = "solved"
    
    def get_available_clues(self, character):
        """Get list of clues this character can potentially discover."""
        available = []
        for clue_id, clue in self.db.clues.items():
            can_discover, reason = self.can_discover_clue(character, clue_id)
            if can_discover:
                available.append(clue_id)
        return available
    
    def get_discovered_clues(self, character):
        """Get list of clues this character has discovered."""
        char_id = character.id
        return self.db.discovered_clues.get(char_id, [])
    
    def add_revelation_trigger(self, trigger_id, required_clues, revelation_text, unlock_clues=None):
        """Add an automatic revelation when certain clues are discovered."""
        self.db.revelation_triggers[trigger_id] = {
            'required_clues': required_clues,
            'revelation': revelation_text,
            'unlock_clues': unlock_clues or []
        }
    
    def at_repeat(self):
        """Called every interval - check for time-based triggers."""
        # Could implement time-based clue reveals, deadline mechanics, etc.
        pass


class ClueObject(DefaultObject):
    """
    A physical clue object that can be examined or interacted with.
    
    These can be placed in rooms and discovered through examination,
    investigation rolls, or specific interactions.
    """
    
    def at_object_creation(self):
        """Set up the clue object."""
        self.db.mystery_id = None
        self.db.clue_id = None
        self.db.discovery_method = "examine"  # examine, investigate, interact
        self.db.skill_required = None  # Optional skill check
        self.db.difficulty = 0  # Difficulty of discovery
        self.db.discovered_by = []
        self.db.hidden = True  # Hidden until discovered
        self.db.discovery_message = "You notice something interesting..."
        
    def at_examine(self, looker, **kwargs):
        """Handle examination of the clue object."""
        if self.db.mystery_id and self.db.clue_id:
            mystery = self.search(self.db.mystery_id, global_search=True)
            if mystery and mystery[0]:
                mystery = mystery[0]
                
                # Check if this character can discover the clue
                can_discover, reason = mystery.can_discover_clue(looker, self.db.clue_id)
                if can_discover:
                    # Attempt discovery
                    if self.db.skill_required:
                        # Would integrate with roll system
                        success = self._attempt_skill_discovery(looker)
                    else:
                        success = True
                    
                    if success:
                        success, msg = mystery.discover_clue(looker, self.db.clue_id, "examine")
                        if success:
                            looker.msg(f"|g{self.db.discovery_message}|n")
                            looker.msg(f"|yYou discovered a clue:|n {msg}")
                            self.db.discovered_by.append(looker.id)
                        else:
                            looker.msg(msg)
                    else:
                        looker.msg("You sense there's something here, but can't quite make it out.")
        
        return super().at_examine(looker, **kwargs)
    
    def _attempt_skill_discovery(self, character):
        """Attempt skill-based discovery."""
        # This would integrate with your existing dice system
        # For now, just return True
        return True


class MysteryManager:
    """
    Utility class for managing mysteries across the game.
    """
    
    @staticmethod
    def create_mystery(title, description, created_by, category="general", difficulty=1):
        """Create a new mystery."""
        mystery, errors = Mystery.create(title)
        if errors:
            logger.log_err(f"Error creating mystery '{title}': {errors}")
            return None
        mystery.db.title = title
        mystery.db.description = description
        mystery.db.created_by = created_by
        mystery.db.category = category
        mystery.db.difficulty = difficulty
        return mystery
    
    @staticmethod
    def get_active_mysteries():
        """Get all active mysteries."""
        mysteries = Mystery.objects.filter_family()
        return [m for m in mysteries if m.db.status == "active" and m.db.title]
    
    @staticmethod
    def get_character_mysteries(character):
        """Get all mysteries a character is involved in."""
        mysteries = MysteryManager.get_active_mysteries()
        involved = []
        
        for mystery in mysteries:
            if character.id in mystery.db.discovered_clues:
                involved.append(mystery)
        
        return involved
    
    @staticmethod
    def search_mysteries(query, category=None):
        """Search for mysteries by title or description."""
        mysteries = MysteryManager.get_active_mysteries()
        results = []
        
        query = query.lower()
        for mystery in mysteries:
            title_match = query in mystery.db.title.lower()
            desc_match = query in mystery.db.description.lower()
            cat_match = not category or mystery.db.category == category
            
            if (title_match or desc_match) and cat_match:
                results.append(mystery)
        
        return results
