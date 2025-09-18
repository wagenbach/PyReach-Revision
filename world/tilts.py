from evennia.utils.utils import lazy_property
from evennia.typeclasses.attributes import AttributeProperty
from evennia.utils.dbserialize import dbserialize, dbunserialize
from evennia.utils import logger
from datetime import datetime, timedelta

class Tilt:
    """
    A class representing a tilt that can be applied to characters or scenes during combat.
    """
    def __init__(self, name, description, tilt_type="personal", duration=None, 
                 effects=None, resolution_method=None, condition_equivalent=None):
        self.name = name
        self.description = description
        self.tilt_type = tilt_type  # "personal" or "environmental"
        self.duration = duration  # None for until resolved, number for turns/rounds
        self.effects = effects or {}  # Dictionary of effects this tilt applies
        self.resolution_method = resolution_method  # How this tilt can be resolved
        self.condition_equivalent = condition_equivalent  # What condition this becomes outside combat
        self.applied_at = datetime.now()
        self.turns_remaining = duration  # Track remaining duration
        
    def advance_turn(self):
        """Advance the tilt by one turn, reducing duration if applicable"""
        if self.turns_remaining is not None and self.turns_remaining > 0:
            self.turns_remaining -= 1
            return self.turns_remaining <= 0
        return False
    
    def is_expired(self):
        """Check if the tilt has expired"""
        if self.turns_remaining is None:
            return False
        return self.turns_remaining <= 0
    
    def to_dict(self):
        """Convert tilt to a dictionary for storage"""
        return {
            'name': self.name,
            'description': self.description,
            'tilt_type': self.tilt_type,
            'duration': self.duration,
            'effects': self.effects,
            'resolution_method': self.resolution_method,
            'condition_equivalent': self.condition_equivalent,
            'applied_at': self.applied_at.isoformat(),
            'turns_remaining': self.turns_remaining
        }
    
    @classmethod
    def from_dict(cls, data):
        """Create a tilt from a dictionary"""
        tilt = cls(
            name=data['name'],
            description=data['description'],
            tilt_type=data['tilt_type'],
            duration=data['duration'],
            effects=data['effects'],
            resolution_method=data['resolution_method'],
            condition_equivalent=data.get('condition_equivalent')
        )
        tilt.applied_at = datetime.fromisoformat(data['applied_at'])
        tilt.turns_remaining = data.get('turns_remaining')
        return tilt

class TiltHandler:
    """
    A handler for managing tilts on characters during combat.
    """
    def __init__(self, obj):
        self.obj = obj
        self._tilts = {}
        self._load_tilts()
    
    def _load_tilts(self):
        """Load tilts from the object's attributes"""
        tilts_data = self.obj.attributes.get('combat_tilts', default={})
        for name, data in tilts_data.items():
            try:
                self._tilts[name] = Tilt.from_dict(data)
            except Exception as e:
                logger.error(f"Error loading tilt {name}: {e}")
    
    def _save_tilts(self):
        """Save tilts to the object's attributes"""
        tilts_data = {name: tilt.to_dict() 
                     for name, tilt in self._tilts.items()}
        self.obj.attributes.add('combat_tilts', tilts_data)
    
    def add(self, tilt):
        """Add a tilt to the object"""
        self._tilts[tilt.name] = tilt
        self._save_tilts()
        self.obj.msg(f"You are affected by the tilt: {tilt.name}")
    
    def remove(self, tilt_name):
        """Remove a tilt from the object"""
        if tilt_name in self._tilts:
            tilt = self._tilts[tilt_name]
            del self._tilts[tilt_name]
            self._save_tilts()
            self.obj.msg(f"You are no longer affected by the tilt: {tilt_name}")
            
            # Check if this tilt should become a condition outside combat
            if tilt.condition_equivalent and not self._is_in_combat():
                self._convert_to_condition(tilt)
            return True
        return False
    
    def get(self, tilt_name):
        """Get a specific tilt"""
        return self._tilts.get(tilt_name)
    
    def all(self):
        """Get all tilts"""
        return list(self._tilts.values())
    
    def personal_tilts(self):
        """Get all personal tilts"""
        return [tilt for tilt in self._tilts.values() if tilt.tilt_type == "personal"]
    
    def advance_turn(self):
        """Advance all tilts by one turn and remove expired ones"""
        expired = []
        for name, tilt in list(self._tilts.items()):
            if tilt.advance_turn():
                expired.append(name)
                self.remove(name)
        return expired
    
    def has(self, tilt_name):
        """Check if object has a specific tilt"""
        return tilt_name in self._tilts
    
    def clear_all(self):
        """Clear all tilts (when leaving combat)"""
        for tilt_name in list(self._tilts.keys()):
            self.remove(tilt_name)
    
    def _is_in_combat(self):
        """Check if the object is currently in combat"""
        return hasattr(self.obj.location, 'combat_tracker') and \
               self.obj in self.obj.location.combat_tracker.participants
    
    def _convert_to_condition(self, tilt):
        """Convert a tilt to its equivalent condition"""
        if tilt.condition_equivalent:
            # Import here to avoid circular imports
            from world.conditions import STANDARD_CONDITIONS
            
            if tilt.condition_equivalent in STANDARD_CONDITIONS:
                condition = STANDARD_CONDITIONS[tilt.condition_equivalent]
                self.obj.conditions.add(condition)
                self.obj.msg(f"The tilt {tilt.name} has become the condition {condition.name}")

class EnvironmentalTiltHandler:
    """
    A handler for managing environmental tilts that affect an entire combat scene.
    """
    def __init__(self, location):
        self.location = location
        self._tilts = {}
        self._load_tilts()
    
    def _load_tilts(self):
        """Load environmental tilts from the location's attributes"""
        tilts_data = self.location.attributes.get('environmental_tilts', default={})
        for name, data in tilts_data.items():
            try:
                self._tilts[name] = Tilt.from_dict(data)
            except Exception as e:
                logger.error(f"Error loading environmental tilt {name}: {e}")
    
    def _save_tilts(self):
        """Save environmental tilts to the location's attributes"""
        tilts_data = {name: tilt.to_dict() 
                     for name, tilt in self._tilts.items()}
        self.location.attributes.add('environmental_tilts', tilts_data)
    
    def add(self, tilt):
        """Add an environmental tilt to the location"""
        self._tilts[tilt.name] = tilt
        self._save_tilts()
        self.location.msg_contents(f"The area is affected by: {tilt.name}")
    
    def remove(self, tilt_name):
        """Remove an environmental tilt from the location"""
        if tilt_name in self._tilts:
            del self._tilts[tilt_name]
            self._save_tilts()
            self.location.msg_contents(f"The area is no longer affected by: {tilt_name}")
            return True
        return False
    
    def get(self, tilt_name):
        """Get a specific environmental tilt"""
        return self._tilts.get(tilt_name)
    
    def all(self):
        """Get all environmental tilts"""
        return list(self._tilts.values())
    
    def advance_turn(self):
        """Advance all environmental tilts by one turn and remove expired ones"""
        expired = []
        for name, tilt in list(self._tilts.items()):
            if tilt.advance_turn():
                expired.append(name)
                self.remove(name)
        return expired
    
    def has(self, tilt_name):
        """Check if location has a specific environmental tilt"""
        return tilt_name in self._tilts
    
    def clear_all(self):
        """Clear all environmental tilts (when combat ends)"""
        for tilt_name in list(self._tilts.keys()):
            self.remove(tilt_name)

# Dictionary of standard tilts
STANDARD_TILTS = {
    # Personal Tilts
    'arm_wrack': Tilt(
        name="Arm Wrack",
        description="One of your arms is damaged and cannot be used effectively.",
        tilt_type="personal",
        effects={"arm_penalty": -2},
        resolution_method="Heal the damage that caused this Tilt",
        condition_equivalent="disabled_persistent"
    ),
    'beaten_down': Tilt(
        name="Beaten Down", 
        description="You are on the ground and stunned from severe damage.",
        tilt_type="personal",
        effects={"prone": True, "defense_penalty": -2},
        resolution_method="Stand up (requires instant action) or heal damage",
        condition_equivalent="humbled"
    ),
    'blinded': Tilt(
        name="Blinded",
        description="You cannot see and suffer penalties to most actions.",
        tilt_type="personal", 
        effects={"vision_penalty": -3},
        resolution_method="Remove the cause of blindness or wait for effect to end",
        condition_equivalent="blind"
    ),
    'deafened': Tilt(
        name="Deafened",
        description="You cannot hear and suffer penalties to perception and social actions.",
        tilt_type="personal",
        effects={"hearing_penalty": -3},
        resolution_method="Remove the cause of deafness or wait for effect to end"
    ),
    'drugged': Tilt(
        name="Drugged",
        description="You are under the influence of drugs, affecting your coordination and judgment.",
        tilt_type="personal",
        effects={"mental_penalty": -2, "physical_penalty": -1},
        resolution_method="Wait for the drug to wear off or use appropriate medicine",
        condition_equivalent="intoxicated"
    ),
    'flooded': Tilt(
        name="Flooded",
        description="You are in an area with significant flooding that impedes movement.",
        tilt_type="personal",
        effects={"movement_penalty": -2},
        resolution_method="Get to higher ground or wait for water to recede"
    ),
    'immobilized': Tilt(
        name="Immobilized",
        description="You cannot move from your current position due to restraints or paralysis.",
        tilt_type="personal",
        effects={"movement": 0, "defense_penalty": -2},
        resolution_method="Break free with Strength + Athletics or remove restraints"
    ),
    'insane': Tilt(
        name="Insane",
        description="Your grip on reality has been severely compromised.",
        tilt_type="personal",
        effects={"mental_penalty": -3, "social_penalty": -2},
        resolution_method="Psychiatric treatment or supernatural healing",
        condition_equivalent="madness_persistent"
    ),
    'knocked_down': Tilt(
        name="Knocked Down",
        description="You have been knocked to the ground and are prone.",
        tilt_type="personal",
        effects={"prone": True},
        resolution_method="Stand up (instant action)"
    ),
    'leg_wrack': Tilt(
        name="Leg Wrack", 
        description="One of your legs is damaged, severely limiting your mobility.",
        tilt_type="personal",
        effects={"speed_penalty": -50, "athletics_penalty": -2},
        resolution_method="Heal the damage that caused this Tilt",
        condition_equivalent="crippled_persistent"
    ),
    'poisoned': Tilt(
        name="Poisoned",
        description="Toxins course through your system, weakening you.",
        tilt_type="personal",
        duration=5,  # 5 turns
        effects={"stamina_penalty": -2, "health_damage_per_turn": 1},
        resolution_method="Medical treatment or wait for poison to run its course"
    ),
    'sick': Tilt(
        name="Sick",
        description="You are suffering from illness that affects your performance.",
        tilt_type="personal",
        effects={"all_actions_penalty": -1},
        resolution_method="Rest and medical treatment",
        condition_equivalent="deprived"
    ),
    'stunned': Tilt(
        name="Stunned",
        description="You are dazed and cannot take actions effectively.",
        tilt_type="personal",
        duration=1,  # 1 turn
        effects={"no_actions": True},
        resolution_method="Wait one turn"
    ),
    
    # Environmental Tilts
    'blizzard': Tilt(
        name="Blizzard",
        description="Heavy snow and wind limit visibility and movement for everyone.",
        tilt_type="environmental",
        effects={"visibility_penalty": -3, "movement_penalty": -1},
        resolution_method="Find shelter or wait for weather to clear"
    ),
    'darkness': Tilt(
        name="Darkness",
        description="The area is shrouded in darkness, limiting visibility.",
        tilt_type="environmental", 
        effects={"visibility_penalty": -2},
        resolution_method="Provide light source"
    ),
    'earthquake': Tilt(
        name="Earthquake",
        description="The ground shakes violently, making it hard to maintain footing.",
        tilt_type="environmental",
        duration=3,  # 3 turns
        effects={"dexterity_penalty": -2, "knockdown_risk": True},
        resolution_method="Wait for earthquake to end or find stable ground"
    ),
    'extreme_cold': Tilt(
        name="Extreme Cold",
        description="Freezing temperatures affect everyone's performance.",
        tilt_type="environmental",
        effects={"dexterity_penalty": -1, "stamina_penalty": -1},
        resolution_method="Find warmth or shelter"
    ),
    'extreme_heat': Tilt(
        name="Extreme Heat", 
        description="Oppressive heat saps strength and endurance.",
        tilt_type="environmental",
        effects={"stamina_penalty": -2, "fatigue_risk": True},
        resolution_method="Find cooling or shade"
    ),
    'heavy_rain': Tilt(
        name="Heavy Rain",
        description="Torrential rain reduces visibility and makes surfaces slippery.",
        tilt_type="environmental",
        effects={"visibility_penalty": -1, "athletics_penalty": -1},
        resolution_method="Find shelter or wait for rain to stop"
    ),
    'heavy_winds': Tilt(
        name="Heavy Winds",
        description="Strong winds interfere with movement and ranged attacks.",
        tilt_type="environmental", 
        effects={"ranged_penalty": -2, "movement_penalty": -1},
        resolution_method="Find windbreak or wait for winds to die down"
    ),
    'ice': Tilt(
        name="Ice",
        description="Slippery ice covers the ground, making movement treacherous.",
        tilt_type="environmental",
        effects={"athletics_penalty": -2, "fall_risk": True},
        resolution_method="Remove ice, add traction, or move to non-icy area"
    ),
    'smoke': Tilt(
        name="Smoke",
        description="Thick smoke fills the area, obscuring vision and hindering breathing.",
        tilt_type="environmental",
        effects={"visibility_penalty": -2, "stamina_penalty": -1},
        resolution_method="Clear the smoke or leave the area"
    ),
    'fire': Tilt(
        name="Fire",
        description="The area is on fire, causing damage and limiting movement options.",
        tilt_type="environmental",
        effects={"fire_damage_risk": True, "movement_restriction": True},
        resolution_method="Extinguish the fire or evacuate the area"
    ),
    'flooding': Tilt(
        name="Flooding",
        description="Rising water makes movement difficult and poses drowning risks.", 
        tilt_type="environmental",
        effects={"movement_penalty": -2, "drowning_risk": True},
        resolution_method="Get to higher ground or wait for water to recede"
    )
} 