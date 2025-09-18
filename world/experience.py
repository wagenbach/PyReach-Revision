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
        self._beats = self.obj.attributes.get('beats', default=0)
        self._experience = self.obj.attributes.get('experience', default=0)
    
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