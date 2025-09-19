from evennia.utils.utils import lazy_property
from evennia.typeclasses.attributes import AttributeProperty
from evennia.utils import logger

class ExperienceHandler:
    """
    A handler for managing experience points and beats for characters.
    """
    def __init__(self, obj):
        self.obj = obj
        self._beats = 0
        self._experience = 0
        self._load_experience()
    
    def _load_experience(self):
        """Load experience data from the object's attributes"""
        # Check for legacy data in db.stats first
        legacy_beats = 0
        legacy_experience = 0
        
        if hasattr(self.obj, 'db') and self.obj.db.stats:
            other_stats = self.obj.db.stats.get('other', {})
            if 'beats' in other_stats or 'experience' in other_stats:
                legacy_beats = other_stats.get('beats', 0)
                legacy_experience = other_stats.get('experience', 0)
                
                # Migrate legacy data to attributes
                if legacy_beats > 0 or legacy_experience > 0:
                    self.obj.attributes.add('beats', legacy_beats)
                    self.obj.attributes.add('experience', legacy_experience)
                    
                    # Clear legacy data
                    other_stats.pop('beats', None)
                    other_stats.pop('experience', None)
        
        # Load from attributes (including migrated data)
        self._beats = self.obj.attributes.get('beats', default=legacy_beats)
        self._experience = self.obj.attributes.get('experience', default=legacy_experience)
    
    def _save_experience(self):
        """Save experience data to the object's attributes"""
        self.obj.attributes.add('beats', self._beats)
        self.obj.attributes.add('experience', self._experience)
    
    def add_beat(self, amount=1):
        """Add beats to the character"""
        self._beats += amount
        # Check if we can convert beats to experience
        while self._beats >= 5:
            self._beats -= 5
            self._experience += 1
        self._save_experience()
        self.obj.msg(f"You gained {amount} beat(s). You now have {self._beats} beats and {self._experience} experience.")
    
    def add_experience(self, amount):
        """Add experience directly to the character"""
        self._experience += amount
        self._save_experience()
        self.obj.msg(f"You gained {amount} experience. You now have {self._experience} experience.")
    
    def spend_experience(self, amount):
        """Spend experience points"""
        if self._experience >= amount:
            self._experience -= amount
            self._save_experience()
            self.obj.msg(f"You spent {amount} experience. You now have {self._experience} experience remaining.")
            return True
        else:
            self.obj.msg(f"You don't have enough experience. You need {amount} but only have {self._experience}.")
            return False
    
    @property
    def beats(self):
        """Get current beats"""
        return self._beats
    
    @property
    def experience(self):
        """Get current experience"""
        return self._experience
    
    @property
    def total_beats(self):
        """Get total beats including fractional beats"""
        fractional_beats = self.obj.attributes.get('fractional_beats', default=0.0)
        return self._beats + fractional_beats
    
    def add_fractional_beat(self, amount):
        """Add fractional beats to the character"""
        fractional_beats = self.obj.attributes.get('fractional_beats', default=0.0)
        fractional_beats += amount
        
        # Convert to whole beats when >= 1.0
        whole_beats = int(fractional_beats)
        fractional_beats = fractional_beats - whole_beats
        
        # Save fractional beats
        self.obj.attributes.add('fractional_beats', fractional_beats)
        
        # Add whole beats if any
        if whole_beats > 0:
            self.add_beat(whole_beats)
        
        return whole_beats, fractional_beats

# Experience costs for different improvements
EXPERIENCE_COSTS = {
    'attribute': 4,  # per dot
    'merit': 1,      # per dot
    'skill_specialty': 1,
    'skill': 2,      # per dot
    'integrity': 2   # per dot
}

# Ways to earn beats
BEAT_SOURCES = {
    'dramatic_failure': 1,      # When a dramatic failure occurs
    'exceptional_success': 1,   # When an exceptional success occurs
    'conditions': 1,            # When resolving a condition
    'aspirations': 1,           # When fulfilling an aspiration
    'story': 1,                 # At the end of a story
    'scene': 1,                 # At the end of a scene
    'session': 1,               # At the end of a session
    'roleplay': 1,              # For good roleplay
    'challenge': 1,             # For overcoming a significant challenge
    'sacrifice': 1,             # For making a meaningful sacrifice
    'discovery': 1,             # For making an important discovery
    'relationship': 1,          # For developing relationships
    'consequence': 1,           # For accepting consequences
    'learning': 1,              # For learning from mistakes
    'growth': 1                 # For character growth
} 