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

# Legacy experience costs (1st Edition - new rating x multiplier)
LEGACY_EXPERIENCE_COSTS = {
    # Attributes: new dots x 5xp
    'attribute': 5,  # multiplier for new rating
    
    # Skills: new dots x 3xp  
    'skill': 3,  # multiplier for new rating
    
    # Specialties: flat cost
    'skill_specialty': 3,
    
    # Merits: new dots x 2xp
    'merit': 2,  # multiplier for new rating
    
    # Morality/Integrity: new dots x 3xp
    'integrity': 3,  # multiplier for new rating
    
    # Willpower (flat cost)
    'willpower': 8,  # flat cost for willpower
    
    # Vampire-specific costs
    'clan_discipline': 5,      # new rating x 5 (clan/bloodline disciplines)
    'other_discipline': 7,     # new rating x 7 (out-of-clan disciplines)
    'blood_sorcery_ritual': 2, # ritual level x 2 (Theban/Cruac rituals)
    'blood_potency': 8,        # new rating x 8
    
    # Other template powers (using new rating system)
    'arcanum': 8,     # per new rating (Mage)
    'gift': 7,        # per new rating (Werewolf)
    'contract': 6,    # per new rating (Changeling)
    'key': 5,         # per new rating (Geist)
    'ceremony': 4,    # per new rating (Geist)
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

def get_attribute_cost(target_level):
    """Get the cost to raise an attribute to target level (new rating x 5)"""
    return target_level * LEGACY_EXPERIENCE_COSTS['attribute']

def get_skill_cost(target_level):
    """Get the cost to raise a skill to target level (new rating x 3)"""
    return target_level * LEGACY_EXPERIENCE_COSTS['skill']

def get_merit_cost(target_level):
    """Get the cost to raise a merit to target level (new rating x 2)"""
    return target_level * LEGACY_EXPERIENCE_COSTS['merit']

def get_integrity_cost(target_level):
    """Get the cost to raise integrity/morality to target level (new rating x 3)"""
    return target_level * LEGACY_EXPERIENCE_COSTS['integrity']

def get_willpower_cost():
    """Get the cost to raise willpower (flat 8 XP)"""
    return LEGACY_EXPERIENCE_COSTS['willpower']

def get_clan_discipline_cost(target_level):
    """Get the cost to raise a clan/bloodline discipline (new rating x 5)"""
    return target_level * LEGACY_EXPERIENCE_COSTS['clan_discipline']

def get_other_discipline_cost(target_level):
    """Get the cost to raise an out-of-clan discipline (new rating x 7)"""
    return target_level * LEGACY_EXPERIENCE_COSTS['other_discipline']

def get_blood_sorcery_ritual_cost(ritual_level):
    """Get the cost for a blood sorcery ritual (ritual level x 2)"""
    return ritual_level * LEGACY_EXPERIENCE_COSTS['blood_sorcery_ritual']

def get_blood_potency_cost(target_level):
    """Get the cost to raise blood potency (new rating x 8)"""
    return target_level * LEGACY_EXPERIENCE_COSTS['blood_potency']

def calculate_vampire_discipline_cost(character, discipline, target_level):
    """Calculate vampire discipline cost based on character's clan"""
    # Get character's clan
    clan = None
    if hasattr(character, 'db') and character.db.stats:
        clan = character.db.stats.get("bio", {}).get("clan", "")
    
    # Import the vampire-specific function
    try:
        from world.cofd.templates.legacy_vampire import get_vampire_discipline_cost
        return get_vampire_discipline_cost(clan, discipline, target_level)
    except ImportError:
        # Fallback to other discipline cost if import fails
        return get_other_discipline_cost(target_level)

def calculate_stat_cost(stat_type, target_level, character=None, stat_name=None):
    """Calculate cost to raise a stat to target level using 1st Edition rules"""
    if target_level <= 0:
        return 0
    
    if stat_type == 'attribute':
        return get_attribute_cost(target_level)
    elif stat_type == 'skill':
        return get_skill_cost(target_level)
    elif stat_type == 'merit':
        return get_merit_cost(target_level)
    elif stat_type == 'integrity':
        return get_integrity_cost(target_level)
    elif stat_type == 'willpower':
        return get_willpower_cost()
    elif stat_type == 'specialty':
        return LEGACY_EXPERIENCE_COSTS['skill_specialty']
    elif stat_type == 'discipline':
        # For vampire disciplines, check if character and stat_name are provided
        if character and stat_name:
            template = character.db.stats.get("other", {}).get("template", "").lower()
            if template == "legacy_vampire":
                return calculate_vampire_discipline_cost(character, stat_name, target_level)
        # Fallback to other discipline cost
        return get_other_discipline_cost(target_level)
    elif stat_type == 'blood_potency':
        return get_blood_potency_cost(target_level)
    elif stat_type == 'blood_sorcery_ritual':
        return get_blood_sorcery_ritual_cost(target_level)
    
    return 0
