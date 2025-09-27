"""
Legacy Experience System for Chronicles/World of Darkness 1st Edition

This system replaces the beats system with traditional experience points.
Experience is awarded directly and costs are higher than in 2nd edition.
"""

from evennia.utils import logger
from evennia.utils.utils import lazy_property

class LegacyExperienceHandler:
    """
    A handler for managing legacy experience points for characters.
    This replaces the beats system when legacy mode is active.
    """
    def __init__(self, obj):
        self.obj = obj
        self._experience = 0
        self._load_experience()
    
    def _load_experience(self):
        """Load experience data from the object's attributes"""
        # Check for modern beats/experience data first and convert
        if hasattr(self.obj, 'db') and self.obj.db.stats:
            other_stats = self.obj.db.stats.get('other', {})
            if 'beats' in other_stats or 'experience' in other_stats:
                beats = other_stats.get('beats', 0)
                experience = other_stats.get('experience', 0)
                
                # Convert beats to experience (5 beats = 1 XP in modern, but we'll be more generous)
                # Convert 3 beats = 1 XP for legacy conversion
                converted_xp = beats // 3
                total_legacy_xp = experience + converted_xp
                
                # Migrate to legacy format
                self.obj.attributes.add('legacy_experience', total_legacy_xp)
                
                # Clear modern data
                other_stats.pop('beats', None)
                other_stats.pop('experience', None)
        
        # Load from attributes (including migrated data)
        self._experience = self.obj.attributes.get('legacy_experience', default=0)
    
    def _save_experience(self):
        """Save experience data to the object's attributes"""
        self.obj.attributes.add('legacy_experience', self._experience)
    
    def add_experience(self, amount, reason=None):
        """Add experience directly to the character"""
        self._experience += amount
        self._save_experience()
        
        reason_text = f" for {reason}" if reason else ""
        self.obj.msg(f"You gained {amount} experience{reason_text}. You now have {self._experience} experience.")
        
        # Log the experience gain
        logger.log_info(f"{self.obj.name} gained {amount} XP{reason_text}. Total: {self._experience}")
    
    def spend_experience(self, amount, item=None):
        """Spend experience points"""
        if self._experience >= amount:
            self._experience -= amount
            self._save_experience()
            
            item_text = f" on {item}" if item else ""
            self.obj.msg(f"You spent {amount} experience{item_text}. You now have {self._experience} experience remaining.")
            
            # Log the experience spend
            logger.log_info(f"{self.obj.name} spent {amount} XP{item_text}. Remaining: {self._experience}")
            return True
        else:
            self.obj.msg(f"You don't have enough experience. You need {amount} but only have {self._experience}.")
            return False
    
    @property
    def experience(self):
        """Get current experience"""
        return self._experience
    
    def set_experience(self, amount):
        """Set experience to a specific amount (admin function)"""
        old_amount = self._experience
        self._experience = max(0, amount)
        self._save_experience()
        
        logger.log_info(f"Admin set {self.obj.name}'s experience from {old_amount} to {self._experience}")
        return f"Experience set to {self._experience} (was {old_amount})"

# Legacy experience costs (higher than 2nd edition)
LEGACY_EXPERIENCE_COSTS = {
    # Attributes (much more expensive)
    'attribute_1_to_2': 4,
    'attribute_2_to_3': 8,
    'attribute_3_to_4': 12,
    'attribute_4_to_5': 16,
    
    # Skills
    'skill_0_to_1': 2,
    'skill_1_to_2': 4,
    'skill_2_to_3': 6,
    'skill_3_to_4': 8,
    'skill_4_to_5': 10,
    
    # Specialties
    'skill_specialty': 2,
    
    # Advantages
    'willpower': 2,  # per dot
    'virtue_vice': 3,  # per dot
    
    # Merits (more expensive)
    'merit': 2,  # per dot
    
    # Integrity/Morality
    'integrity': 3,  # per dot
    
    # Powers (template-specific)
    'discipline': 7,  # per dot (Vampire)
    'arcanum': 8,    # per dot (Mage)
    'gift': 7,       # per dot (Werewolf)
    'contract': 6,   # per dot (Changeling)
    'key': 5,        # per key (Geist)
    'ceremony': 4,   # per ceremony (Geist)
}

# Ways to earn experience in legacy mode (no beats)
LEGACY_XP_AWARDS = {
    'automatic_weekly': 1,        # Automatic weekly XP
    'exceptional_roleplay': 1,    # For exceptional roleplay
    'story_completion': 2,        # At the end of a major story
    'character_growth': 1,        # For significant character development
    'learning_experience': 1,     # For learning from mistakes/failure
    'heroic_action': 2,          # For truly heroic or self-sacrificing acts
    'creative_solution': 1,       # For creative problem solving
    'dramatic_failure_lesson': 1, # When a dramatic failure teaches something important
    'relationship_development': 1, # For developing meaningful relationships
    'overcoming_vice': 2,        # For overcoming your vice in a significant way
    'fulfilling_virtue': 1,      # For exemplifying your virtue
    'staff_award': 3,            # Staff discretionary award
}

def get_attribute_cost(current_level):
    """Get the cost to raise an attribute from current level to next"""
    cost_map = {
        1: LEGACY_EXPERIENCE_COSTS['attribute_1_to_2'],
        2: LEGACY_EXPERIENCE_COSTS['attribute_2_to_3'], 
        3: LEGACY_EXPERIENCE_COSTS['attribute_3_to_4'],
        4: LEGACY_EXPERIENCE_COSTS['attribute_4_to_5']
    }
    return cost_map.get(current_level, 0)

def get_skill_cost(current_level):
    """Get the cost to raise a skill from current level to next"""
    cost_map = {
        0: LEGACY_EXPERIENCE_COSTS['skill_0_to_1'],
        1: LEGACY_EXPERIENCE_COSTS['skill_1_to_2'],
        2: LEGACY_EXPERIENCE_COSTS['skill_2_to_3'],
        3: LEGACY_EXPERIENCE_COSTS['skill_3_to_4'],
        4: LEGACY_EXPERIENCE_COSTS['skill_4_to_5']
    }
    return cost_map.get(current_level, 0)

def calculate_total_cost(stat_type, current_level, target_level):
    """Calculate total cost to raise a stat from current to target level"""
    if target_level <= current_level:
        return 0
    
    total_cost = 0
    for level in range(current_level, target_level):
        if stat_type == 'attribute':
            total_cost += get_attribute_cost(level)
        elif stat_type == 'skill':
            total_cost += get_skill_cost(level)
    
    return total_cost
