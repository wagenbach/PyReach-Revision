"""
Characters

Characters are (by default) Objects setup to be puppeted by Accounts.
They are what you "see" in game. The Character class in this module
is setup to be the "default" character type created by the default
creation commands.

The character typeclass is where we store stats, powers, pools, and so on for each character. A character's
stats are stored on their character object using a dictionary (self.db.stats), and the same for powers, pools,
and so on.

"""

from evennia import DefaultCharacter
from evennia.utils.utils import lazy_property
from world.conditions import ConditionHandler
from world.tilts import TiltHandler
from world.experience import ExperienceHandler, EXPERIENCE_COSTS
from world.cofd.template_registry import template_registry

from .objects import ObjectParent


class Character(ObjectParent, DefaultCharacter):
    """
    The Character class represents a player character in the game.
    """

    @lazy_property
    def conditions(self):
        """
        Returns the condition handler for this character.
        """
        return ConditionHandler(self)

    @lazy_property
    def tilts(self):
        """
        Returns the tilt handler for this character.
        """
        return TiltHandler(self)

    @lazy_property
    def experience(self):
        """
        Returns the experience handler for this character.
        """
        return ExperienceHandler(self)

    def at_object_creation(self):
        """
        Called when the character is first created.
        """
        super().at_object_creation()
        
        # Initialize modern stats structure, default to mortal
        self.db.stats = {
            "attributes": {},
            "skills": {},
            "advantages": {},
            "anchors": {},
            "bio": {
                "full_name": "",
                "birthdate": "",
                "concept": "",
                "virtue": "",
                "vice": ""
            },
            "merits": {},
            "specialties": {},
            "powers": {},
            "other": {
                "template": "Mortal",
                "integrity": 7,
                "size": 5,
                "beats": 0,
                "experience": 0
            }
        }
        
        # Initialize pools tracking
        self.db.willpower_current = None  # Will be set when willpower stat is set
        self.db.health_damage = {}
        
        # Character approval status
        self.db.approved = False
        
        # Initialize aspirations and equipment
        self.db.aspirations = ["", "", ""]
        self.db.equipment = {}
        
    def at_login(self):
        """
        Called when the character logs in.
        """
        super().at_login()
        # Check for expired conditions
        expired = self.conditions.check_expired()
        if expired:
            self.msg(f"The following conditions have expired: {', '.join(expired)}")

    def at_object_receive(self, moved_obj, source_location):
        """
        Called when an object is moved into this character's inventory.
        """
        super().at_object_receive(moved_obj, source_location)
        # Add any condition-related logic here

    def at_object_leave(self, moved_obj, destination):
        """
        Called when an object is moved out of this character's inventory.
        """
        super().at_object_leave(moved_obj, destination)
        # Add any condition-related logic here

    def stat_add(self, stat, value):
        """
        Add a stat to the character.
        """
        
    def get_integrity_name(self, template=None):
        """
        Get the template-specific integrity name using the template registry.
        
        Args:
            template (str): Character template (if None, uses current template)
            
        Returns:
            str: The appropriate integrity stat name for the template
        """
        if template is None:
            template = self.db.stats.get("other", {}).get("template", "Mortal")
            
        return template_registry.get_integrity_name(template)

    def get_starting_integrity(self, template=None):
        """
        Get the starting integrity value for a specific template using the template registry.
        
        Args:
            template (str): Character template (if None, uses current template)
            
        Returns:
            int: Starting integrity value for the template
        """
        if template is None:
            template = self.db.stats.get("other", {}).get("template", "Mortal")
            
        return template_registry.get_starting_integrity(template)

    def reset_stats_for_template(self, new_template, caller=None):
        """
        Completely wipe and reinitialize stats for a new template.
        This is the 'nuclear option' for cleaning up corrupted stats.
        
        Args:
            new_template (str): The new template to set
            caller: The object calling this method (for messages)
            
        Returns:
            str: Success message
        """
        # Check if template is valid using registry
        if not template_registry.is_valid_template(new_template):
            return f"Invalid template '{new_template}'. Available templates: {', '.join(template_registry.get_template_names())}"
        
        # Get template-specific starting integrity
        starting_integrity = template_registry.get_starting_integrity(new_template)
        
        # Completely wipe the stats dictionary
        self.db.stats = {
            "attributes": {},
            "skills": {},
            "advantages": {},
            "anchors": {},
            "bio": {
                "full_name": "",
                "birthdate": "",
                "concept": ""
            },
            "merits": {},
            "specialties": {},
            "other": {
                "template": str(new_template).title(),
                "integrity": starting_integrity,
                "size": 5,
                "beats": 0,
                "experience": 0
            }
        }
        
        # Add template-specific bio fields
        template_fields = template_registry.get_bio_fields(str(new_template))
        for field in template_fields:
            self.db.stats["bio"][field] = "<not set>"
            
            # Also add virtue/vice to anchors if they exist
            if field in ["virtue", "vice"]:
                if "anchors" not in self.db.stats:
                    self.db.stats["anchors"] = {}
                self.db.stats["anchors"][field] = "<not set>"
        
        # Reset pools tracking
        self.db.willpower_current = None
        self.db.health_damage = {}
        
        # Clean up any legacy attributes that might exist
        legacy_cleanup_attrs = [
            "advantages", "merits", "pools", "powers", "sphere",
            "stamina", "composure", "strength", "dexterity", "wits", "resolve",
            "intelligence", "manipulation", "presence", "brawl", "streetwise",
            "empathy", "contacts", "street_fighting", "medium", "mask", "dirge", "blood"
        ]
        
        for attr in legacy_cleanup_attrs:
            if hasattr(self.db, attr):
                try:
                    delattr(self.db, attr)
                except AttributeError:
                    pass
        
        # Assign template in registry for tracking
        template_registry.assign_template(self, new_template, caller)
        
        message = f"Completely reset {self.name}'s stats for {new_template} template."
        message += f"\nAll previous stats have been wiped clean."
        message += f"\nUse +stat <stat>=<value> to set new stats."
        message += f"\nUse +recalc to recalculate derived stats after setting attributes."
        
        return message

    def set_template(self, new_template, caller=None, reset_stats=False):
        """
        Set character template and update bio fields accordingly.
        
        Args:
            new_template (str): The new template to set
            caller: The object calling this method (for messages)
            reset_stats (bool): If True, completely wipe and reinitialize stats
            
        Returns:
            tuple: (success, message) - success boolean and message string
        """
        # Check if template is valid using registry
        if not template_registry.is_valid_template(new_template):
            available = ', '.join(template_registry.get_template_names())
            return False, f"Invalid template '{new_template}'. Available templates: {available}"
        
        # If reset_stats is True, use the nuclear option
        if reset_stats:
            message = self.reset_stats_for_template(new_template, caller)
            return True, message
        
        # Get old and new template fields for bio updates
        old_template = self.db.stats.get("other", {}).get("template", "Mortal")
        old_fields = set(template_registry.get_bio_fields(old_template))
        new_fields = set(template_registry.get_bio_fields(new_template))
        
        # Set the new template
        if "other" not in self.db.stats:
            self.db.stats["other"] = {}
        self.db.stats["other"]["template"] = str(new_template).title()
        
        # Clean up any legacy "sphere" field
        if "sphere" in self.db.stats["other"]:
            del self.db.stats["other"]["sphere"]
        
        # Update bio fields based on template change
        if "bio" not in self.db.stats:
            self.db.stats["bio"] = {}
            
        bio_changes = []
        
        # Remove fields that are not needed for the new template
        fields_to_remove = old_fields - new_fields
        for field in fields_to_remove:
            if field in self.db.stats["bio"]:
                del self.db.stats["bio"][field]
                bio_changes.append(f"Removed {field}")
                
                # Also remove from anchors if it's virtue/vice
                if field in ["virtue", "vice"] and "anchors" in self.db.stats:
                    self.db.stats["anchors"].pop(field, None)
        
        # Add placeholders for new required fields
        fields_to_add = new_fields - old_fields
        for field in fields_to_add:
            self.db.stats["bio"][field] = "<not set>"
            bio_changes.append(f"Added {field}")
                
            # Also add to anchors if it's virtue/vice
            if field in ["virtue", "vice"]:
                if "anchors" not in self.db.stats:
                    self.db.stats["anchors"] = {}
                self.db.stats["anchors"][field] = "<not set>"
        
        # Assign template in registry for tracking
        template_registry.assign_template(self, new_template, caller)
        
        # Create success message
        message = f"Set {self.name}'s template to {new_template}."
        if bio_changes:
            message += f"\nBio field changes: {', '.join(bio_changes)}"
            message += f"\nUse +stat <field>=<value> to set the new template-specific fields."
        
        return True, message

    def get_template_bio_fields(self, template=None):
        """Get valid bio fields for a specific template using the template registry"""
        if template is None:
            template = self.db.stats.get("other", {}).get("template", "Mortal")
            
        return template_registry.get_bio_fields(template)
    
    def calculate_derived_stats(self, caller=None):
        """Calculate derived stats based on attributes"""
        attrs = self.db.stats.get("attributes", {})
        skills = self.db.stats.get("skills", {})
        other = self.db.stats.get("other", {})
        
        # Initialize advantages if needed
        if "advantages" not in self.db.stats:
            self.db.stats["advantages"] = {}
        
        updated_stats = []
        
        # Health = Size + Stamina
        if "stamina" in attrs:
            size = other.get("size", 5)  # Default size is 5
            self.db.stats["advantages"]["health"] = size + attrs["stamina"]
            updated_stats.append("health")
        
        # Willpower = Resolve + Composure  
        if "resolve" in attrs and "composure" in attrs:
            self.db.stats["advantages"]["willpower"] = attrs["resolve"] + attrs["composure"]
            updated_stats.append("willpower")
        
        # Speed = Strength + Dexterity + 5
        if "strength" in attrs and "dexterity" in attrs:
            self.db.stats["advantages"]["speed"] = attrs["strength"] + attrs["dexterity"] + 5
            updated_stats.append("speed")
        
        # Defense = Lower of Wits or Dexterity 
        if "wits" in attrs and "dexterity" in attrs:
            self.db.stats["advantages"]["defense"] = min(attrs["wits"], attrs["dexterity"])
            updated_stats.append("defense")
        
        # Initiative = Dexterity + Composure
        if "dexterity" in attrs and "composure" in attrs:
            self.db.stats["advantages"]["initiative"] = attrs["dexterity"] + attrs["composure"]
            updated_stats.append("initiative")
        
        # Send message to caller if provided
        if caller:
            if updated_stats:
                caller.msg(f"Updated derived stats: {', '.join(updated_stats)}")
            else:
                caller.msg("No derived stats could be calculated with current attributes.")
        
        return updated_stats

    def recalculate_derived_stats(self, caller=None):
        """Recalculate derived stats for a character"""
        if not self.db.stats:
            if caller:
                caller.msg(f"{self.name} has no stats set.")
            return
        
        return self.calculate_derived_stats(caller)
    
    def validate_template_field(self, field, value):
        """Validate template-specific field values using the template registry"""
        template = self.db.stats.get("other", {}).get("template", "Mortal")
        return template_registry.validate_field(template, field, value)
    
    def cleanup_misplaced_stats(self, caller=None):
        """Clean up stats that were stored with spaces in wrong categories"""
        if not self.db.stats:
            return
        
        other = self.db.stats.get("other", {})
        changes_made = []
        
        # Define proper mappings for commonly misplaced stats
        stat_mappings = {
            # Bio fields that might be in 'other' with spaces
            "full name": ("bio", "full_name"),
            "animal ken": ("skills", "animal_ken"),
            # Add other common space-containing stat names as needed
        }
        
        # Check for misplaced stats and move them
        for space_name, (correct_category, underscore_name) in stat_mappings.items():
            if space_name in other:
                value = other[space_name]
                
                # Ensure correct category exists
                if correct_category not in self.db.stats:
                    self.db.stats[correct_category] = {}
                
                # Move the stat to correct location
                self.db.stats[correct_category][underscore_name] = value
                
                # Remove from wrong location
                del other[space_name]
                
                changes_made.append(f"Moved '{space_name}' to {correct_category} as '{underscore_name}'")
        
        if changes_made and caller:
            caller.msg("Fixed misplaced stats: " + ", ".join(changes_made))
    
    def check_merit_prerequisites(self, prerequisite_string):
        """Check if character meets merit prerequisites."""
        if not prerequisite_string:
            return True
            
        # Parse prerequisite string
        # Format: "attribute:value", "skill:value", "[option1,option2]", "[req1 and req2]"
        prereqs = prerequisite_string.split(",")
        
        for prereq in prereqs:
            prereq = prereq.strip()
            
            # Handle OR requirements [option1,option2]
            if prereq.startswith("[") and prereq.endswith("]"):
                or_options = prereq[1:-1].split(",")
                or_met = False
                for option in or_options:
                    if self.check_single_merit_prerequisite(option.strip()):
                        or_met = True
                        break
                if not or_met:
                    return False
            else:
                if not self.check_single_merit_prerequisite(prereq):
                    return False
                    
        return True
        
    def check_single_merit_prerequisite(self, prereq):
        """Check a single merit prerequisite requirement."""
        prereq = prereq.strip()
        stats = self.db.stats or {}
        
        # Handle template-based prerequisites (no colon)
        if ":" not in prereq:
            current_template = stats.get("other", {}).get("template", "Mortal").lower()
            
            # Handle negative prerequisites (non_template)
            if prereq.startswith("non_"):
                required_template = prereq[4:]  # Remove "non_" prefix
                return current_template != required_template
            
            # Handle template checks
            if prereq in ["mummy", "vampire", "mage", "werewolf", "changeling", "hunter", 
                         "beast", "demon", "deviant", "geist", "promethean", "mortal", "mortal+"]:
                return current_template == prereq
                
            # If not a known template prerequisite, return False
            return False
            
        # Handle stat:value prerequisites
        stat_name, required_value = prereq.split(":", 1)
        stat_name = stat_name.strip().lower()
        
        try:
            required_value = int(required_value.strip())
        except ValueError:
            return False
            
        # Check attributes
        current_value = stats.get("attributes", {}).get(stat_name, 1)
        if current_value >= required_value:
            return True
            
        # Check skills
        current_value = stats.get("skills", {}).get(stat_name, 0)
        if current_value >= required_value:
            return True
            
        # Check merits
        current_value = stats.get("merits", {}).get(stat_name, {}).get("dots", 0)
        if current_value >= required_value:
            return True
            
        return False