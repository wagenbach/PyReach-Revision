from evennia.utils.utils import lazy_property
from evennia.typeclasses.attributes import AttributeProperty
from evennia.utils.dbserialize import dbserialize, dbunserialize
from evennia.utils import logger
from datetime import datetime, timedelta

class Condition:
    """
    A class representing a condition that can be applied to characters.
    """
    def __init__(self, name, description, duration=None, is_persistent=False, 
                 effects=None, resolution_method=None):
        self.name = name
        self.description = description
        self.duration = duration  # None for permanent, timedelta for temporary
        self.is_persistent = is_persistent
        self.effects = effects or {}  # Dictionary of effects this condition applies
        self.resolution_method = resolution_method  # How this condition can be resolved
        self.applied_at = datetime.now()
        
    def is_expired(self):
        """Check if the condition has expired"""
        if self.duration is None or self.is_persistent:
            return False
        return datetime.now() > (self.applied_at + self.duration)
    
    def to_dict(self):
        """Convert condition to a dictionary for storage"""
        return {
            'name': self.name,
            'description': self.description,
            'duration': self.duration.total_seconds() if self.duration else None,
            'is_persistent': self.is_persistent,
            'effects': self.effects,
            'resolution_method': self.resolution_method,
            'applied_at': self.applied_at.isoformat()
        }
    
    @classmethod
    def from_dict(cls, data):
        """Create a condition from a dictionary"""
        condition = cls(
            name=data['name'],
            description=data['description'],
            duration=timedelta(seconds=data['duration']) if data['duration'] else None,
            is_persistent=data['is_persistent'],
            effects=data['effects'],
            resolution_method=data['resolution_method']
        )
        condition.applied_at = datetime.fromisoformat(data['applied_at'])
        return condition

class ConditionHandler:
    """
    A handler for managing conditions on characters.
    """
    def __init__(self, obj):
        self.obj = obj
        self._conditions = {}
        self._load_conditions()
    
    def _load_conditions(self):
        """Load conditions from the object's attributes"""
        conditions_data = self.obj.attributes.get('conditions', default={})
        for name, data in conditions_data.items():
            try:
                self._conditions[name] = Condition.from_dict(data)
            except Exception as e:
                logger.error(f"Error loading condition {name}: {e}")
    
    def _save_conditions(self):
        """Save conditions to the object's attributes"""
        conditions_data = {name: condition.to_dict() 
                          for name, condition in self._conditions.items()}
        self.obj.attributes.add('conditions', conditions_data)
    
    def add(self, condition):
        """Add a condition to the object"""
        self._conditions[condition.name] = condition
        self._save_conditions()
        self.obj.msg(f"You have gained the condition: {condition.name}")
    
    def remove(self, condition_name):
        """Remove a condition from the object"""
        if condition_name in self._conditions:
            del self._conditions[condition_name]
            self._save_conditions()
            self.obj.msg(f"You have lost the condition: {condition_name}")
            return True
        return False
    
    def get(self, condition_name):
        """Get a specific condition"""
        return self._conditions.get(condition_name)
    
    def all(self):
        """Get all conditions"""
        return list(self._conditions.values())
    
    def check_expired(self):
        """Check and remove expired conditions"""
        expired = [name for name, condition in self._conditions.items() 
                  if condition.is_expired()]
        for name in expired:
            self.remove(name)
        return expired
    
    def has(self, condition_name):
        """Check if object has a specific condition"""
        return condition_name in self._conditions

# Dictionary of standard conditions
STANDARD_CONDITIONS = {
    # Temporary Conditions
    'an_eye_for_disorder': Condition(
        name="An Eye For Disorder",
        description="",
        is_persistent=False
    ),
    'angel_empathy': Condition(
        name="Angel Empathy",
        description="",
        is_persistent=False
    ),
    'atavism': Condition(
        name="Atavism",
        description="You suffer ancient, ancestral memories that rouse anger and violent urges; the cause of these memories must be destroyed.",
        is_persistent=False
    ),
    'ban': Condition(
        name="Ban",
        description="Your character suffers from a powerful spiritual compulsion that demands specific behavior.",
        is_persistent=False
    ),
    'berserk': Condition(
        name="Berserk",
        description="Your character has had a spark of berserk rage lit within her.",
        is_persistent=False
    ),
    'bestial': Condition(
        name="Bestial",
        description="",
        is_persistent=False
    ),
    'blackballed': Condition(
        name="Blackballed",
        description="Your character has been ostracized from a social group.",
        is_persistent=False
    ),
    'blind': Condition(
        name="Blind",
        description="Your character cannot see, affecting any sight-based rolls.",
        is_persistent=False
    ),
    'bonded': Condition(
        name="Bonded",
        description="Your character has bonded with an animal, granting a bonus on interactions with it.",
        is_persistent=False
    ),
    'captivated': Condition(
        name="Captivated",
        description="Your character is enthralled by something or someone.",
        is_persistent=False
    ),
    'competitive': Condition(
        name="Competitive",
        description="Your character is driven to win at all costs.",
        is_persistent=False
    ),
    'confused': Condition(
        name="Confused",
        description="Your character cannot think straight.",
        is_persistent=False
    ),
    'connected': Condition(
        name="Connected",
        description="Your character has made inroads with a group, gaining a bonus on actions related to it.",
        is_persistent=False
    ),
    'cowed': Condition(
        name="Cowed",
        description="Your character has been put in her place through the violence and dominance of another.",
        is_persistent=False
    ),
    'cunning': Condition(
        name="Cunning",
        description="Your character is Cunning. She beguiles, tricks, sneaks and charms.",
        is_persistent=False
    ),
    'delusion': Condition(
        name="Delusion",
        description="Your character cannot make sense of the world she perceives, and because of this, she avoids that which would make her question.",
        is_persistent=False
    ),
    'demoralized': Condition(
        name="Demoralized",
        description="Your character is demoralized and hesitant in the face of the enemy.",
        is_persistent=False
    ),
    'deprived': Condition(
        name="Deprived",
        description="Your character suffers from an addiction, facing penalties when deprived of it.",
        is_persistent=False
    ),
    'despondent': Condition(
        name="Despondent",
        description="Your character feels the hunter's approach in his blood and in his bones, and its only a matter of time before death claims him.",
        is_persistent=False
    ),
    'disoriented': Condition(
        name="Disoriented",
        description="Your character has lost their sense of direction and balance.",
        is_persistent=False
    ),
    'distracted': Condition(
        name="Distracted",
        description="Your character's attention is divided.",
        is_persistent=False
    ),
    'dominated': Condition(
        name="Dominated",
        description="Your character is under the control of another.",
        is_persistent=False
    ),
    'drained': Condition(
        name="Drained",
        description="Your character's energy has been sapped.",
        is_persistent=False
    ),
    'easy_prey': Condition(
        name="Easy Prey",
        description="Through carelessness or ignorance, your character leaves a clear trail for any hunter to follow.",
        is_persistent=False
    ),
    'ecstatic': Condition(
        name="Ecstatic",
        description="Your character is in a state of overwhelming joy.",
        is_persistent=False
    ),
    'embarrassing_secret': Condition(
        name="Embarrassing Secret",
        description="Your character has a secret that could come back to haunt him. If the secret is let out, this Condition becomes the Notoriety Condition.",
        is_persistent=False
    ),
    'enraptured': Condition(
        name="Enraptured",
        description="Your character has witnessed divinity and feels the madness of faith deep within his soul.",
        is_persistent=False
    ),
    'ergi': Condition(
        name="Ergi",
        description="Your character has been accused of being unmanly, or of passive homosexuality. In Viking culture, this is a grave insult. He has until the next Thing meets to kill his accuser or face him in a duel.",
        is_persistent=False
    ),
    'essence_overload': Condition(
        name="Essence Overload",
        description="Your character has attempted to channel immensely powerful forces through her Essence, and has lost control.",
        is_persistent=False
    ),
    'euphoric': Condition(
        name="Euphoric",
        description="Your character glimpsed Rabid Wolf's radiant madness and understands his role as prey in the hunt.",
        is_persistent=False
    ),
    'exhausted': Condition(
        name="Exhausted",
        description="Your character has been run ragged and desperately needs a good rest.",
        is_persistent=False
    ),
    'flagged': Condition(
        name="Flagged",
        description="Your character has been marked for special attention.",
        is_persistent=False
    ),
    'frantic': Condition(
        name="Frantic",
        description="Your character has glimpsed the passion Rabid Wolf embodies with his every moment. He will put his full effort into every action until exhausted, as Gurim-Ur demands nothing less.",
        is_persistent=False
    ),
    'frightened': Condition(
        name="Frightened",
        description="Your character is frightened and may flee or freeze.",
        is_persistent=False
    ),
    'futuristic_visionary': Condition(
        name="Futuristic Visionary",
        description="New technologies and tales of scientific marvels galvanize your character into a flurry of inventiveness.",
        is_persistent=False
    ),
    'glorious': Condition(
        name="Glorious",
        description="Your character is Glorious. She's faced down superior opponents, committed great acts of courage, and lived to tell the tale.",
        is_persistent=False
    ),
    'guilty': Condition(
        name="Guilty",
        description="Your character is struck by a deep sense of remorse, facing penalties to attempts to resist Subterfuge, Empathy, or Intimidation rolls.",
        is_persistent=False
    ),
    'honorable': Condition(
        name="Honorable",
        description="Your character is Honorable. She wields honesty the way some Uratha wield their claws.",
        is_persistent=False
    ),
    'humbled': Condition(
        name="Humbled",
        description="Your character has been brought low.",
        is_persistent=False
    ),
    'i_know_someone': Condition(
        name="I Know Someone",
        description="Your character has a useful contact.",
        is_persistent=False
    ),
    'impostor': Condition(
        name="Impostor",
        description="Your character is pretending to be someone they're not.",
        is_persistent=False
    ),
    'informed': Condition(
        name="Informed",
        description="Your character has investigated a subject thoroughly and may shed this Condition to raise by one step the result of a related roll.",
        is_persistent=False
    ),
    'isolated': Condition(
        name="Isolated",
        description="Your character has been split from his crew, drawn and called out, cornered and quartered.",
        is_persistent=False
    ),
    'inspired': Condition(
        name="Inspired",
        description="Your character is deeply inspired. He may shed this Condition to gain Willpower and reduce the exceptional success threshold.",
        is_persistent=False
    ),
    'instinctive': Condition(
        name="Instinctive",
        description="The primal nature of the hunter calls to your character.",
        is_persistent=False
    ),
    'intoxicated': Condition(
        name="Intoxicated",
        description="Your character is under the influence of drugs or alcohol.",
        is_persistent=False
    ),
    'invisible_predator': Condition(
        name="Invisible Predator",
        description="Your character has so successfully infiltrated her prey's domain that he is oblivious to her presence.",
        is_persistent=False
    ),
    'jaded': Condition(
        name="Jaded",
        description="Your character has seen too much to be easily shocked.",
        is_persistent=False
    ),
    'languid': Condition(
        name="Languid",
        description="Your character is listless and lacking energy.",
        is_persistent=False
    ),
    'lethargic': Condition(
        name="Lethargic",
        description="Your character is sluggish and slow to act.",
        is_persistent=False
    ),
    'leveraged': Condition(
        name="Leveraged",
        description="Your character has been blackmailed or tricked into doing another's bidding.",
        is_persistent=False
    ),
    'lost': Condition(
        name="Lost",
        description="Your character has no idea where he is and cannot seek his goal without first finding his way.",
        is_persistent=False
    ),
    'lost_cohesion': Condition(
        name="Lost Cohesion",
        description="The packmates just can't seem to communicate properly, or understand each other's intentions.",
        is_persistent=False
    ),
    'lost_hunters': Condition(
        name="Lost Hunters",
        description="The pack has somehow lost touch with its instincts, feeling out-of-touch with both the wolf and human aspects of its nature.",
        is_persistent=False
    ),
    'lost_tracker': Condition(
        name="Lost Tracker",
        description="Your character has lost faith in her abilities because she failed to find her prey.",
        is_persistent=False
    ),
    'mesmerized': Condition(
        name="Mesmerized",
        description="Your character is entranced by something.",
        is_persistent=False
    ),
    'monstrous_servant': Condition(
        name="Monstrous Servant",
        description="Your character is master to a Geryo.",
        is_persistent=False
    ),
    'moon_taint': Condition(
        name="Moon Taint",
        description="Your character as been infected with the warping taint of Luna.",
        is_persistent=False
    ),
    'mute': Condition(
        name="Mute",
        description="Your character cannot speak and must communicate in some other manner.",
        is_persistent=False
    ),
    'mystified': Condition(
        name="Mystified",
        description="Your character faced an Ithaeur, and now he feels the dread of the spirit wilds wherever he goes.",
        is_persistent=False
    ),
    'notoriety': Condition(
        name="Notoriety",
        description="Your character is ostracized by the public for a perceived wrong. Social rolls are made at a penalty, as is Social Maneuvering.",
        is_persistent=False
    ),
    'obsession': Condition(
        name="Obsession",
        description="Your character is obsessed with a subject, facing a penalty on actions unrelated to it.",
        is_persistent=False
    ),
    'outlaw': Condition(
        name="Outlaw",
        description="Your character has been declared an outlaw by the Thing and banished from society. Perhaps you can't pay a weregild, or refused an honorable challenge to a duel.",
        is_persistent=False
    ),
    'paranoid': Condition(
        name="Paranoid",
        description="Your character has been reduced to a state of rampant paranoia.",
        is_persistent=False
    ),
    'plugged_in': Condition(
        name="Plugged In",
        description="Your character is connected to a network or system.",
        is_persistent=False
    ),
    'punk_generation': Condition(
        name="Punk Generation",
        description="Your character has been wronged by someone more privileged than she.",
        is_persistent=False
    ),
    'prepared_for_anything': Condition(
        name="Prepared for Anything",
        description="Your character is ready for any situation.",
        is_persistent=False
    ),
    'pure': Condition(
        name="Pure",
        description="Your character is Pure. She adheres to the Oath of the Moon in all things. She's known to put her ancestral duties above everything in her life.",
        is_persistent=False
    ),
    'raptured': Condition(
        name="Raptured",
        description="Your character has been taken up into a higher state of being.",
        is_persistent=False
    ),
    'reception': Condition(
        name="Reception",
        description="Your character has opened to the spirit world, as a result of her experience with Lunacy.",
        is_persistent=False
    ),
    'resigned': Condition(
        name="Resigned",
        description="Your character faced down his hunter, and the frightening beast has shown him the essence of doom.",
        is_persistent=False
    ),
    'sated': Condition(
        name="Sated",
        description="Your character's hunger has been satisfied.",
        is_persistent=False
    ),
    'scarred': Condition(
        name="Scarred",
        description="Your character bears physical or emotional scars.",
        is_persistent=False
    ),
    'shadow_paranoia': Condition(
        name="Shadow Paranoia",
        description="Your character has been afflicted with a supernatural panic; she is jumpy and on edge, afraid that every shadow might contain sharp teeth and sudden death.",
        is_persistent=False
    ),
    'shaken': Condition(
        name="Shaken",
        description="Your character has been frightened by something. Shed the Condition by choosing, before making a roll, to fail it.",
        is_persistent=False
    ),
    'shadowlashed': Condition(
        name="Shadowlashed",
        description="Your character failed to master the laws of the Shadow and now suffers for her hubris.",
        is_persistent=False
    ),
    'spooked': Condition(
        name="Spooked",
        description="Your character has become frightened and fascinated by something supernatural. Shed the condition when this fear and fascination causes him to hinder the group in some way.",
        is_persistent=False
    ),
    'steadfast': Condition(
        name="Steadfast",
        description="Your character is resolved. Shed the Condition to treat a failed roll as though it were a single success, or to turn a chance die into a regular die.",
        is_persistent=False
    ),
    'stumbled': Condition(
        name="Stumbled",
        description="Your character has hit a complication during an extended action.",
        is_persistent=False
    ),
    'surrounded': Condition(
        name="Surrounded",
        description="Your character has no safe place to go, no ally can be trusted, all eyes are watching him.",
        is_persistent=False
    ),
    'surveilled': Condition(
        name="Surveilled",
        description="Your character is being watched.",
        is_persistent=False
    ),
    'swaggering': Condition(
        name="Swaggering",
        description="Your character faced the full bore of a Rahu's essence. He's sure that he can win in the face of the Rahu's fury.",
        is_persistent=False
    ),
    'swooning': Condition(
        name="Swooning",
        description="Your character harbors affections for another, suffering a penalty to actions that would harm the object of affection. Said individual gains a bonus on Social rolls and Maneuvering against the character.",
        is_persistent=False
    ),
    'symbolic_focus': Condition(
        name="Symbolic Focus",
        description="Your character is filled with the symbolic power of the rite that she has invoked, becoming a channel for it.",
        is_persistent=False
    ),
    'tainted': Condition(
        name="Tainted",
        description="Your character has been corrupted by something.",
        is_persistent=False
    ),
    'tasked': Condition(
        name="Tasked",
        description="Your character has been given a specific mission.",
        is_persistent=False
    ),
    'tempted': Condition(
        name="Tempted",
        description="Your character is being tempted by something.",
        is_persistent=False
    ),
    'unware': Condition(
        name="Unware",
        description="Your character has been dazed and confused, distracted and internalized.",
        is_persistent=False
    ),
    'untraceable': Condition(
        name="Untraceable",
        description="Through care and attention to detail, your character leaves little evidence of her passage for others to follow.",
        is_persistent=False
    ),
    'wanton': Condition(
        name="Wanton",
        description="Your character is unrestrained in their desires.",
        is_persistent=False
    ),
    'wise': Condition(
        name="Wise",
        description="Your character is Wise. She seeks the intelligent, reason answer in all things.",
        is_persistent=False
    ),
    'wracked': Condition(
        name="Wracked",
        description="Every part of your character hurts.",
        is_persistent=False
    ),
    
    # Persistent Conditions
    'addicted_persistent': Condition(
        name="Addicted (Persistent)",
        description="Your character is addicted to a substance or behavior.",
        is_persistent=True
    ),
    'amnesia_persistent': Condition(
        name="Amnesia (Persistent)",
        description="Your character is missing a portion of her memory.",
        is_persistent=True
    ),
    'awestruck_persistent': Condition(
        name="Awestruck (Persistent)",
        description="Your character sees before her a glorious and terrifying figure, and something in her brain kicks her to kneel and grovel.",
        is_persistent=True
    ),
    'betrayed_persistent': Condition(
        name="Betrayed (Persistent)",
        description="Your character has been betrayed by someone they trusted.",
        is_persistent=True
    ),
    'blind_persistent': Condition(
        name="Blind (Persistent)",
        description="Your character cannot see, affecting any sight-based rolls.",
        is_persistent=True
    ),
    'blown_persistent': Condition(
        name="Blown (Persistent)",
        description="Your character's cover has been compromised.",
        is_persistent=True
    ),
    'broken_persistent': Condition(
        name="Broken (Persistent)",
        description="Your character has been gravely affected by some trauma and now faces penalties to Social rolls, rolls requiring Resolve, and resistance to any Intimidation rolls.",
        is_persistent=True
    ),
    'charmed_persistent': Condition(
        name="Charmed (Persistent)",
        description="Your character is under a lasting magical charm.",
        is_persistent=True
    ),
    'connected_persistent': Condition(
        name="Connected (Persistent)",
        description="Your character has made inroads with a group, gaining a bonus on actions related to it.",
        is_persistent=True
    ),
    'crippled_persistent': Condition(
        name="Crippled (Persistent)",
        description="Your character either cannot or has difficulty walking. His Speed trait is limited and he requires a wheelchair to travel.",
        is_persistent=True
    ),
    'delusional_persistent': Condition(
        name="Delusional (Persistent)",
        description="Your character suffers from persistent delusions.",
        is_persistent=True
    ),
    'dependent_persistent': Condition(
        name="Dependent (Persistent)",
        description="Your character is dependent on something or someone.",
        is_persistent=True
    ),
    'deprived_persistent': Condition(
        name="Deprived (Persistent)",
        description="Your character suffers from an addiction, facing penalties when deprived of it.",
        is_persistent=True
    ),
    'disabled_persistent': Condition(
        name="Disabled (Persistent)",
        description="Your character has a permanent disability.",
        is_persistent=True
    ),
    'enervated_persistent': Condition(
        name="Enervated (Persistent)",
        description="Your character is permanently weakened.",
        is_persistent=True
    ),
    'enslaved_persistent': Condition(
        name="Enslaved (Persistent)",
        description="Your character is permanently bound to serve another.",
        is_persistent=True
    ),
    'enthralled_persistent': Condition(
        name="Enthralled (Persistent)",
        description="Your character is permanently under the influence of another.",
        is_persistent=True
    ),
    'false_memories_persistent': Condition(
        name="False Memories (Persistent)",
        description="Your character has false memories implanted in their mind.",
        is_persistent=True
    ),
    'fugue_persistent': Condition(
        name="Fugue (Persistent)",
        description="Your character has broken from trauma such that he faces blackouts and lost time during which he attempts to flee the triggering situation.",
        is_persistent=True
    ),
    'hunted_persistent': Condition(
        name="Hunted (Persistent)",
        description="Your character is being pursued by something dangerous.",
        is_persistent=True
    ),
    'hunting_nature_human_persistent': Condition(
        name="Hunting Nature: Human (Persistent)",
        description="The pack values preparation and practice over blind instinct.",
        is_persistent=True
    ),
    'hunting_nature_werewolf_persistent': Condition(
        name="Hunting Nature: Werewolf (Persistent)",
        description="The pack has incorporated the strengths of both wolf and human into its hunting.",
        is_persistent=True
    ),
    'hunting_nature_wolf_persistent': Condition(
        name="Hunting Nature: Wolf (Persistent)",
        description="The pack values instinct over reason, the thrill of the chase, and the freedom of acting without the constant need for thought.",
        is_persistent=True
    ),
    'lured_persistent': Condition(
        name="Lured (Persistent)",
        description="Your character has been lured into an action; she is absolutely convinced she saw or heard something over there that she needs to check out, or has seen something she wants to investigate, becoming completely focused on it.",
        is_persistent=True
    ),
    'madness_persistent': Condition(
        name="Madness (Persistent)",
        description="Your character has been jarred loose from reality by way of some supernatural experience. He occasionally faces a penalty to Social or Mental rolls.",
        is_persistent=True
    ),
    'mute_persistent': Condition(
        name="Mute (Persistent)",
        description="Your character cannot speak and must communicate in some other manner.",
        is_persistent=True
    ),
    'obsession_persistent': Condition(
        name="Obsession (Persistent)",
        description="Your character is permanently obsessed with something.",
        is_persistent=True
    ),
    'radiation_poisoning_persistent': Condition(
        name="Radiation Poisoning (Persistent)",
        description="Your character has been exposed to atomic radiation and suffers radiation poisoning. Symptoms can include nausea and vomiting, anemia, red and blistering skin, dizziness, and seizures.",
        is_persistent=True
    ),
    'siskur_dah_persistent': Condition(
        name="Siskur-Dah (Persistent)",
        description="Your character is on the Siskur-Dah, the Sacred Hunt. She gains a specific benefit depending on the ritemaster's tribe.",
        is_persistent=True
    ),
    'soulless_persistent': Condition(
        name="Soulless (Persistent)",
        description="Your character has been stripped of a soul. He cannot regain Willpower through rest, and the use of Vice and Virtue are reversed; additionally, regaining Willpower via the Vice is a breaking point at -5 until reaching Integrity 1. He cannot use abjuration, warding, or binding, and becomes more susceptible to possession.",
        is_persistent=True
    ),
    'subservient_persistent': Condition(
        name="Subservient (Persistent)",
        description="Your character is permanently subservient to another.",
        is_persistent=True
    ),
    'thrall_persistent': Condition(
        name="Thrall (Persistent)",
        description="Your character is permanently under the control of another.",
        is_persistent=True
    ),
    'uncalled_persistent': Condition(
        name="Uncalled (Persistent)",
        description="Your character has not been called to their true purpose.",
        is_persistent=True
    )
} 