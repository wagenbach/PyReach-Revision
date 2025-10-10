"""
Consolidated data structure for the character creation lookup system.
This module combines all stat types and provides enhanced lookup functionality.
"""

from world.cofd.stat_dictionary import (
    attribute_dictionary, skill_dictionary, 
    advantage_dictionary, anchor_dictionary
)
from world.cofd.merits.general_merits import all_merits as general_merits
from world.cofd.merits.vampire_merits import vampire_merits
from world.cofd.merits.mage_merits import mage_merits
from world.cofd.merits.werewolf_merits import werewolf_merits
from world.cofd.merits.changeling_merits import changeling_merits
from world.cofd.merits.geist_merits import geist_merits
from world.cofd.merits.demon_merits import demon_merits
from world.cofd.merits.deviant_merits import deviant_merits
from world.cofd.merits.hunter_merits import hunter_merits
from world.cofd.merits.mummy_merits import mummy_merits
from world.cofd.merits.promethean_merits import promethean_merits
from world.cofd.merits.minor_template_merits import (
    minor_template_merits, PSYCHIC_MERIT_NAMES,
    ghoul_merits, dhampir_merits, atariya_merits, psychic_vampire_merits,
    general_supernatural_merits
)
from world.cofd.templates.vampire import VAMPIRE_CLANS, VAMPIRE_COVENANTS, VAMPIRE_DISCIPLINES
from world.cofd.templates.mage import MAGE_PATHS, MAGE_ORDERS, MAGE_ARCANA, LEGACIES_BY_PATH, LEGACIES_BY_ORDER, UNLINKED_LEGACIES, ALL_LEGACIES
from world.cofd.templates.demon import DEMON_INCARNATIONS, DEMON_AGENDAS, DEMON_EMBEDS, DEMON_EXPLOITS
from world.cofd.templates.mortal_plus import ALL_MORTAL_PLUS_TYPES, PSYCHIC_POWERS
from world.cofd.templates.werewolf import WEREWOLF_AUSPICES, WEREWOLF_TRIBES, WEREWOLF_LODGES
from world.cofd.templates.changeling import CHANGELING_SEEMINGS, CHANGELING_COURTS, CHANGELING_KITHS, CHANGELING_ENTITLEMENTS
from world.cofd.templates.promethean import (
    PROMETHEAN_TRANSMUTATIONS, PROMETHEAN_ALEMBICS, 
    PROMETHEAN_BESTOWMENTS, PROMETHEAN_LINEAGES
)
from world.cofd.templates.legacy_promethean import ATHANORS_BY_LINEAGE
from world.cofd.templates.hunter_endowments import ADVANCED_ARMORY, ANIMAL_CONTROL_KIT, BENEDICTION, CASTIGATION, DREAMSCAPE, ELIXIR, ENKOIMESIS, GOETIC_GOSPEL, HORROR_WITHIN, INFUSION, INK, INSPIRATION, LIVES_REMEMBERED, PERISPIRITISM, RELIC, RITES_DU_CHEVAL, RITES_OF_DENIAL, SEITOKUTEN, TELEINFORMATICS, THAUMATECHNOLOGY, XENOTECHNOLOGY
from world.cofd.templates.hunter import HUNTER_CONSPIRACIES, HUNTER_COMPACTS, HUNTER_TACTICS, HUNTER_ENDOWMENTS
from world.cofd.templates.mummy import MUMMY_GUILDS, MUMMY_DECREES, MUMMY_JUDGES, MUMMY_UTTERANCES, MUMMY_AFFINITIES
from world.cofd.templates.geist import GEIST_BURDENS, GEIST_KREWE_TYPES, GEIST_HAUNTS, GEIST_KEYS, GEIST_CEREMONIES
from world.cofd.templates.deviant import DEVIANT_ORIGINS, DEVIANT_CLADES, DEVIANT_SCARS, DEVIANT_VARIATIONS, DEVIANT_ADAPTATIONS
from world.cofd.templates.mortal_plus import (
    ALL_MORTAL_PLUS_TYPES, PSYCHIC_POWERS, PROXIMUS_FAMILIES,
    DEMON_BLOODED_LEVELS, GAME_LINE_HERITAGE, WOLF_BLOODED_TELLS
)
import re


class LookupData:
    """Consolidated data structure for character creation lookups."""
    
    def __init__(self):
        self.attributes = attribute_dictionary
        self.skills = skill_dictionary
        self.advantages = advantage_dictionary
        self.anchors = anchor_dictionary
        self.general_merits = general_merits
        self.vampire_merits = vampire_merits
        self.mage_merits = mage_merits
        self.werewolf_merits = werewolf_merits
        self.changeling_merits = changeling_merits
        self.geist_merits = geist_merits
        self.demon_merits = demon_merits
        self.deviant_merits = deviant_merits
        self.hunter_merits = hunter_merits
        self.mummy_merits = mummy_merits
        self.promethean_merits = promethean_merits
        self.minor_template_merits = minor_template_merits
        self.ghoul_merits = ghoul_merits
        self.dhampir_merits = dhampir_merits
        self.atariya_merits = atariya_merits
        self.psychic_vampire_merits = psychic_vampire_merits
        self.general_supernatural_merits = general_supernatural_merits
        self.psychic_merit_names = PSYCHIC_MERIT_NAMES
        self.all_merits = (general_merits + vampire_merits + mage_merits + werewolf_merits + 
                          changeling_merits + geist_merits + demon_merits + deviant_merits +
                          hunter_merits + mummy_merits + promethean_merits + minor_template_merits)
        
        # Template-specific data
        self.vampire_data = {
            'clans': VAMPIRE_CLANS,
            'covenants': VAMPIRE_COVENANTS,
            'disciplines': VAMPIRE_DISCIPLINES
        }
        
        self.mage_data = {
            'paths': MAGE_PATHS,
            'orders': MAGE_ORDERS,
            'arcana': MAGE_ARCANA,
            'legacies_by_path': LEGACIES_BY_PATH,
            'legacies_by_order': LEGACIES_BY_ORDER,
            'unlinked_legacies': UNLINKED_LEGACIES,
            'all_legacies': ALL_LEGACIES
        }
        
        self.demon_data = {
            'incarnations': DEMON_INCARNATIONS,
            'agendas': DEMON_AGENDAS,
            'embeds': DEMON_EMBEDS,
            'exploits': DEMON_EXPLOITS
        }
        
        self.mortal_plus_data = {
            'types': ALL_MORTAL_PLUS_TYPES,
            'psychic_powers': PSYCHIC_POWERS,
            'demon_blooded_levels': DEMON_BLOODED_LEVELS,
            'game_line_heritage': GAME_LINE_HERITAGE,
            'wolf_blooded_tells': WOLF_BLOODED_TELLS,
            'proximus_families': PROXIMUS_FAMILIES,
        }
        
        # Mummy data
        self.mummy_data = {
            'guilds': MUMMY_GUILDS,
            'decrees': MUMMY_DECREES,
            'judges': MUMMY_JUDGES,
            'utterances': MUMMY_UTTERANCES,
            'affinities': MUMMY_AFFINITIES
        }
        
        # Geist data
        self.geist_data = {
            'burdens': GEIST_BURDENS,
            'krewe_types': GEIST_KREWE_TYPES,
            'haunts': GEIST_HAUNTS,
            'keys': GEIST_KEYS,
            'ceremonies': GEIST_CEREMONIES
        }
        
        # Deviant data
        self.deviant_data = {
            'origins': DEVIANT_ORIGINS,
            'clades': DEVIANT_CLADES,
            'scars': DEVIANT_SCARS,
            'variations': DEVIANT_VARIATIONS,
            'adaptations': DEVIANT_ADAPTATIONS
        }
        
        # Werewolf data
        self.werewolf_data = {
            'auspices': WEREWOLF_AUSPICES,
            'tribes': WEREWOLF_TRIBES,
            'lodges': WEREWOLF_LODGES
        }
        
        # Changeling data
        self.changeling_data = {
            'seemings': CHANGELING_SEEMINGS,
            'courts': CHANGELING_COURTS,
            'kiths': CHANGELING_KITHS,
            'entitlements': CHANGELING_ENTITLEMENTS
        }
        
        # Promethean data
        self.promethean_data = {
            'transmutations': PROMETHEAN_TRANSMUTATIONS,
            'alembics': PROMETHEAN_ALEMBICS,
            'bestowments': PROMETHEAN_BESTOWMENTS,
            'lineages': PROMETHEAN_LINEAGES,
            'athanors': ATHANORS_BY_LINEAGE
        }
        
        # Hunter data - need to build the endowments dict from imported modules
        hunter_endowments = {
            **ADVANCED_ARMORY,
            **ANIMAL_CONTROL_KIT,
            **BENEDICTION,
            **CASTIGATION,
            **DREAMSCAPE,
            **ELIXIR,
            **ENKOIMESIS,
            **GOETIC_GOSPEL,
            **HORROR_WITHIN,
            **INFUSION,
            **INK,
            **INSPIRATION,
            **LIVES_REMEMBERED,
            **PERISPIRITISM,
            **RELIC,
            **RITES_DU_CHEVAL,
            **RITES_OF_DENIAL,
            **SEITOKUTEN,
            **TELEINFORMATICS,
            **THAUMATECHNOLOGY,
            **XENOTECHNOLOGY
        }
        
        self.hunter_data = {
            'endowments': hunter_endowments,
            'conspiracies': HUNTER_CONSPIRACIES,
            'compacts': HUNTER_COMPACTS,
            'tactics': HUNTER_TACTICS
        }
        
        # Skill specialties
        self.specialties = {
            # Mental Skills
            'academics': ['Anthropology', 'Art History', 'English', 'History', 'Law', 'Literature', 'Religion', 'Research', 'Translation'],
            'computer': ['Data Retrieval', 'Graphics', 'Hacking', 'Internet', 'Programming', 'Security', 'Social Media'],
            'crafts': ['Automotive', 'Cosmetics', 'Fashion', 'Forging', 'Graffiti', 'Jury-Rigging', 'Painting', 'Perfumery', 'Repair', 'Sculpting'],
            'investigation': ['Artifacts', 'Autopsy', 'Body Language', 'Crime Scenes', 'Cryptography', 'Dreams', 'Lab Work', 'Riddles'],
            'medicine': ['First Aid', 'Pathology', 'Pharmaceuticals', 'Physical Therapy', 'Surgery'],
            'occult': ['Angels', 'Alchemy', 'Mystic Places', 'Casting Lots', 'Phrenology', 'Sorcery', 'Supernatural Being (specify)', 'Superstition', 'Witchcraft'],
            'politics': ['Bureaucracy', 'Church', 'Democratic', 'Invictus', 'Local', 'Organized Crime', 'Scandals'],
            'science': ['Physics', 'Chemistry', 'Neuroscience', 'Virology', 'Alchemy', 'Genetics', 'Hematology'],
            # Physical Skills
            'athletics': ['Acrobatics', 'Archery', 'Climbing', 'Jumping', 'Parkour', 'Swimming', 'Throwing'],
            'brawl': ['Biting', 'Boxing', 'Dirty Fighting', 'Grappling', 'Martial Arts', 'Threats', 'Throws'],
            'drive': ['Defensive Driving', 'Evasion', 'Off-Road Driving', 'Motorcycles', 'Pursuit', 'Stunts'],
            'firearms': ['Handguns', 'Rifles', 'Shotguns', 'Trick Shots'],
            'larceny': ['Breaking and Entering', 'Concealment', 'Lockpicking', 'Pickpocketing', 'Safecracking', 'Security Systems', 'Sleight of Hand'],
            'stealth': ['Camouflage', 'Crowds', 'In Plain Sight', 'Rural', 'Shadowing', 'Stakeout', 'Staying Motionless'],
            'survival': ['Foraging', 'Hunting', 'Navigation', 'Shelter', 'Weather'],
            'weaponry': ['Chains', 'Clubs', 'Improvised Weapons', 'Spears', 'Swords'],
            # Social Skills
            'animal_ken': ['Animalism', 'Canines', 'Felines', 'Reptiles', 'Threatening', 'Training'],
            'empathy': ['Calming', 'Emotion', 'Lies', 'Motives', 'Personalities'],
            'expression': ['Dance', 'Drama', 'Journalism', 'Musical Instrument', 'Performance Art', 'Singing', 'Speeches'],
            'intimidation': ['Direct Threats', 'Interrogation', 'Stare Down', 'Torture', 'Veiled Threats'],
            'persuasion': ['Confidence Scam', 'Fast Talking', 'Inspiring', 'Sales Pitch', 'Seduction', 'Sermon'],
            'socialize': ['Bar Hopping', 'Church Lock-in', 'Dress Balls', 'Formal Events', 'Frat Parties', 'Political Fundraisers', 'the Club'],
            'streetwise': ['Black Market', 'Gangs', 'Navigation', 'Rumors', 'Undercover'],
            'subterfuge': ['Detecting Lies', 'Doublespeak', 'Hiding Emotion', 'Little White Lies', 'Misdirection']
        }
    
    def find_stat(self, stat_name):
        """Find a stat by name across all categories."""
        stat_name = stat_name.lower().replace(" ", "_")
        
        # Check attributes
        if stat_name in self.attributes:
            return ('attribute', self.attributes[stat_name])
        
        # Check skills
        if stat_name in self.skills:
            return ('skill', self.skills[stat_name])
        
        # Check advantages
        if stat_name in self.advantages:
            return ('advantage', self.advantages[stat_name])
        
        # Check anchors
        if stat_name in self.anchors:
            return ('anchor', self.anchors[stat_name])
        
        # Check merits
        for merit in self.all_merits:
            if merit.name.lower().replace(" ", "_") == stat_name:
                return ('merit', merit)
        
        return None
    
    def search_stats(self, search_term):
        """Search for stats containing the given term."""
        search_term = search_term.lower()
        results = []
        
        # Search attributes
        for name, attr in self.attributes.items():
            if search_term in name.lower():
                results.append(('attribute', name, attr))
        
        # Search skills
        for name, skill in self.skills.items():
            if search_term in name.lower():
                results.append(('skill', name, skill))
        
        # Search merits
        for merit in self.all_merits:
            if (search_term in merit.name.lower() or 
                search_term in merit.description.lower()):
                results.append(('merit', merit.name, merit))
        
        # Search disciplines
        for discipline in self.vampire_data['disciplines']:
            if search_term in discipline.lower():
                results.append(('discipline', discipline, None))
        
        # Search arcana
        for arcanum in self.mage_data['arcana']:
            if search_term in arcanum.lower():
                results.append(('arcanum', arcanum, None))
        
        return results
    
    def get_merits_by_type(self, merit_type=None, template=None):
        """Get merits filtered by type and/or template."""
        merits = []
        
        # Map template names to their merit lists
        template_map = {
            'vampire': self.vampire_merits,
            'mage': self.mage_merits,
            'werewolf': self.werewolf_merits,
            'changeling': self.changeling_merits,
            'geist': self.geist_merits,
            'demon': self.demon_merits,
            'deviant': self.deviant_merits,
            'hunter': self.hunter_merits,
            'mummy': self.mummy_merits,
            'promethean': self.promethean_merits,
            'mortal+': self.minor_template_merits,
            'mortal_plus': self.minor_template_merits,
            'general': self.general_merits,
            # Minor template types
            'ghoul': self.ghoul_merits,
            'dhampir': self.dhampir_merits,
            'atariya': self.atariya_merits,
            'psychic_vampire': self.psychic_vampire_merits,
            'psychic vampire': self.psychic_vampire_merits,
        }
        
        # Special handling for psychic merits - filter from general merits by name
        if template and template.lower() == 'psychic':
            merits = [m for m in self.general_merits if m.name in self.psychic_merit_names]
        elif template and template.lower() in template_map:
            merits = template_map[template.lower()]
        elif template is None:
            merits = self.general_merits
        else:
            merits = self.all_merits
        
        if merit_type:
            merits = [m for m in merits if m.merit_type == merit_type]
        
        return sorted(merits, key=lambda m: m.name)
    
    def parse_prerequisites(self, prereq_string):
        """Parse prerequisite string into structured data."""
        if not prereq_string:
            return []
        
        prereqs = []
        # Split on commas and clean up
        parts = [p.strip() for p in prereq_string.split(',')]
        
        for part in parts:
            if not part:
                continue
                
            # Handle negation
            negated = False
            if part.startswith('!'):
                negated = True
                part = part[1:]
            
            # Handle stat:value format
            if ':' in part:
                stat, value = part.split(':', 1)
                try:
                    value = int(value)
                    prereqs.append({
                        'type': 'stat',
                        'stat': stat.replace('_', ' ').title(),
                        'value': value,
                        'negated': negated
                    })
                except ValueError:
                    # Non-numeric value, treat as requirement
                    prereqs.append({
                        'type': 'requirement',
                        'requirement': f"{stat.replace('_', ' ').title()}: {value}",
                        'negated': negated
                    })
            # Handle bracketed OR conditions like [wits:3,dexterity:3]
            elif part.startswith('[') and part.endswith(']'):
                or_conditions = part[1:-1].split(',')
                or_prereqs = []
                for condition in or_conditions:
                    if ':' in condition:
                        stat, value = condition.split(':', 1)
                        try:
                            value = int(value)
                            or_prereqs.append(f"{stat.replace('_', ' ').title()} {value}")
                        except ValueError:
                            or_prereqs.append(condition.replace('_', ' ').title())
                    else:
                        or_prereqs.append(condition.replace('_', ' ').title())
                
                prereqs.append({
                    'type': 'or_condition',
                    'conditions': or_prereqs,
                    'negated': negated
                })
            else:
                # Simple requirement
                prereqs.append({
                    'type': 'requirement',
                    'requirement': part.replace('_', ' ').title(),
                    'negated': negated
                })
        
        return prereqs
    
    def format_prerequisites_display(self, prereq_string):
        """Format prerequisites for display."""
        if not prereq_string:
            return "None"
        
        prereqs = self.parse_prerequisites(prereq_string)
        if not prereqs:
            return "None"
        
        display_parts = []
        
        for prereq in prereqs:
            if prereq['type'] == 'stat':
                stat_display = f"{prereq['stat']} {prereq['value']}"
                if prereq['negated']:
                    stat_display = f"NOT {stat_display}"
                display_parts.append(stat_display)
            
            elif prereq['type'] == 'or_condition':
                or_display = " OR ".join(prereq['conditions'])
                if prereq['negated']:
                    or_display = f"NOT ({or_display})"
                else:
                    or_display = f"({or_display})"
                display_parts.append(or_display)
            
            elif prereq['type'] == 'requirement':
                req_display = prereq['requirement']
                if prereq['negated']:
                    req_display = f"NOT {req_display}"
                display_parts.append(req_display)
        
        return ", ".join(display_parts)


# Global instance for easy access
LOOKUP_DATA = LookupData()


def get_attribute_description(attr_name):
    """Get description for an attribute."""
    # Pull directly from the attribute dictionary
    if attr_name in attribute_dictionary:
        return attribute_dictionary[attr_name].description
    return "Core character attribute"


def get_skill_description(skill_name):
    """Get description for a skill."""
    # Pull directly from the skill dictionary
    if skill_name in skill_dictionary:
        return skill_dictionary[skill_name].description
    return "Character skill"


def get_discipline_description(discipline_name):
    """Get description for a vampire discipline."""
    descriptions = {
        "animalism": "Command and communicate with animals",
        "auspex": "Supernatural senses and perception",
        "bloodworking": "Manipulate and weaponize blood",
        "cachexy": "Inflict disease and decay",
        "celerity": "Supernatural speed and reflexes",
        "coils of the dragon": "Ordo Dracul transcendence techniques",
        "cruac": "Circle of the Crone blood sorcery",
        "dominate": "Mental control and command",
        "majesty": "Supernatural presence and awe",
        "nightmare": "Inspire terror and fear",
        "obfuscate": "Concealment and stealth",
        "praestantia": "Enhanced physical capabilities",
        "protean": "Shapechanging and transformation",
        "resilience": "Supernatural toughness",
        "theban sorcery": "Lancea et Sanctum divine magic",
        "vigor": "Supernatural strength"
    }
    return descriptions.get(discipline_name, "Vampire supernatural power")


def get_arcanum_description(arcanum_name):
    """Get description for a mage arcanum."""
    descriptions = {
        "death": "Decay, ghosts, and the underworld",
        "fate": "Luck, destiny, and probability",
        "forces": "Energy, motion, and physics",
        "life": "Biology, healing, and transformation",
        "matter": "Substances, alchemy, and transmutation",
        "mind": "Thoughts, emotions, and mental control",
        "prime": "Raw magic and the Supernal Realm",
        "space": "Distance, teleportation, and scrying",
        "spirit": "The Shadow Realm and ephemeral beings",
        "time": "Temporal manipulation and prophecy"
    }
    return descriptions.get(arcanum_name, "Sphere of magical influence")


def get_clan_description(clan_name):
    """Get description for a vampire clan."""
    descriptions = {
        "daeva": "Seductive predators driven by passion and desire",
        "gangrel": "Savage survivors who embrace their Beast",
        "mekhet": "Mysterious shadows who trade in secrets",
        "nosferatu": "Hideous monsters dwelling in the underground",
        "ventrue": "Noble lords who rule from positions of power"
    }
    return descriptions.get(clan_name, "Vampire bloodline")


def get_covenant_description(covenant_name):
    """Get description for a vampire covenant."""
    descriptions = {
        "carthian movement": "Revolutionary vampires seeking political change",
        "circle of the crone": "Pagan vampires who worship the dark goddess",
        "invictus": "Aristocratic vampires maintaining feudal traditions",
        "lancea et sanctum": "Religious vampires serving as God's predators",
        "ordo dracul": "Philosophical vampires transcending their curse",
        "unaligned": "Independent vampires avoiding covenant politics"
    }
    return descriptions.get(covenant_name, "Vampire political organization")


def get_path_info(path_name):
    """Get ruling arcana and description for a mage path."""
    path_info = {
        "acanthus": ("Time, Fate", "Enchanters who walk between worlds"),
        "mastigos": ("Mind, Space", "Warlocks who command demons and souls"),
        "moros": ("Death, Matter", "Necromancers who speak with the dead"),
        "obrimos": ("Forces, Prime", "Theurges who wield divine fire"),
        "thyrsus": ("Life, Spirit", "Shamans who commune with nature")
    }
    return path_info.get(path_name, ("Unknown", "Awakened magician"))


def get_order_description(order_name):
    """Get description for a mage order."""
    descriptions = {
        "adamantine arrow": "Warrior-philosophers who protect the Awakened",
        "guardians of the veil": "Secret agents maintaining the Masquerade",
        "mysterium": "Scholar-mages preserving magical knowledge",
        "silver ladder": "Political leaders guiding human destiny",
        "free council": "Democratic rebels embracing modern methods",
        "seers of the throne": "Servants of the Exarchs opposing Awakening",
        "unaligned": "Independent mages avoiding order politics"
    }
    return descriptions.get(order_name, "Mage political organization")


def get_template_description(template_name):
    """Get description for a character template."""
    descriptions = {
        "mortal": "Ordinary humans with no supernatural abilities",
        "mortal+": "Humans with minor supernatural abilities",
        "vampire": "Undead predators who feed on blood",
        "mage": "Awakened humans who manipulate reality",
        "werewolf": "Shapeshifters who guard the boundaries",
        "changeling": "Fae-touched humans who escaped Arcadia",
        "demon": "Fallen angels who escaped the God-Machine",
        "geist": "Humans bound to death-spirits",
        "promethean": "Artificial beings seeking humanity",
        "hunter": "Humans who hunt supernatural creatures",
        "mummy": "Immortal servants of ancient judges",
        "beast": "Incarnate nightmares who feed on fear",
        "deviant": "Humans transformed by conspiracy"
    }
    return descriptions.get(template_name, "Supernatural character type")
