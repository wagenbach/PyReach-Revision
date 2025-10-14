"""
Mummy: The Curse Template Definition for Chronicles of Darkness.
Mummies are ancient immortals bound to serve the Judges of Duat in the modern world.
"""

from . import register_template
from world.cofd.mummy_powers import (
    MUMMY_AFFINITIES, MUMMY_UTTERANCES,
    ALL_AFFINITY_NAMES, ALL_UTTERANCE_NAMES,
    AFFINITIES_BY_PILLAR, UTTERANCES_BY_PILLAR, UTTERANCES_BY_TIER
)

# Valid mummy guilds
MUMMY_GUILDS = [
    "mesen-nebu", "sesha-hebsu", "su-menent", "tef-aabhi", "maa-kep",
    "akhem-urtu", "kher-minu", "maar-kherit", "wadjet-itja"
]

# Valid mummy decrees
MUMMY_DECREES = [
    "balance", "fortune", "knowledge", "protection", "vengeance"
]

# Valid mummy judges
MUMMY_JUDGES = [
    "djehuty", "duamutef", "hapi", "imsety", "kebehsenuf", "nehebkau", "neith", "ptah", "sobek"
]

# Export the imported power data for easy access
# These are now detailed dictionaries instead of simple lists
MUMMY_AFFINITIES_DATA = MUMMY_AFFINITIES
MUMMY_UTTERANCES_DATA = MUMMY_UTTERANCES

# Mummy template definition
MUMMY_TEMPLATE = {
    "name": "mummy",
    "display_name": "Mummy",
    "description": "Mummies are ancient immortals who serve as agents of the Judges of Duat, awakening in the modern world to fulfill their eternal duties.",
    "bio_fields": ["virtue", "vice", "guild", "decree", "judge", "cult", "tomb"],
    "integrity_name": "Memory",
    "starting_integrity": 5,
    "supernatural_power_stat": "sekhem",
    "starting_power_stat": 1,
    "resource_pool": "pillars",
    "power_systems": ALL_UTTERANCE_NAMES + ALL_AFFINITY_NAMES,
    "anchors": ["virtue", "vice"],
    "merit_categories": ["physical", "social", "mental", "supernatural", "fighting", "style", "mummy"],
    "field_validations": {
        "guild": {
            "valid_values": MUMMY_GUILDS
        },
        "decree": {
            "valid_values": MUMMY_DECREES
        },
        "judge": {
            "valid_values": MUMMY_JUDGES
        }
    },
    "version": "2.0",
    "author": "Chronicles of Darkness",
    "game_line": "Mummy: The Curse",
    "notes": "Mummy template with Sekhem, Utterances, Affinities, and the Pillars system"
}

# Register the template
register_template(MUMMY_TEMPLATE)


# Helper functions for power system integration
def get_primary_powers():
    """
    Get primary/rated powers for mummy (none - mummies don't have rated powers).
    Affinities and Utterances are individual semantic powers.
    
    Returns:
        list: Empty list (no rated powers)
    """
    return []


def get_secondary_powers():
    """
    Get secondary/semantic powers for mummy (affinities and utterances).
    
    Returns:
        list: All affinity and utterance keys
    """
    return ALL_AFFINITY_NAMES + ALL_UTTERANCE_NAMES


def get_all_powers():
    """
    Get all powers for mummy (for validation in +stat command).
    
    Returns:
        list: All affinity and utterance keys
    """
    return ALL_AFFINITY_NAMES + ALL_UTTERANCE_NAMES


def get_affinity(affinity_key):
    """
    Get affinity data by key.
    
    Args:
        affinity_key (str): The affinity key (e.g., 'bestial_majesty')
        
    Returns:
        dict: Affinity data or None if not found
    """
    return MUMMY_AFFINITIES_DATA.get(affinity_key.lower().replace(" ", "_"))


def get_utterance(utterance_key):
    """
    Get utterance data by key.
    
    Args:
        utterance_key (str): The utterance key (e.g., 'awaken_the_dead_ba_1')
        
    Returns:
        dict: Utterance data or None if not found
    """
    return MUMMY_UTTERANCES_DATA.get(utterance_key.lower().replace(" ", "_"))


def get_affinities_by_pillar(pillar_name):
    """
    Get all affinities for a specific pillar.
    
    Args:
        pillar_name (str): Pillar name (Ab, Ba, Ka, Ren, Sheut, or guild name)
        
    Returns:
        list: List of affinity keys for that pillar
    """
    return AFFINITIES_BY_PILLAR.get(pillar_name, [])


def get_utterances_by_pillar(pillar_name):
    """
    Get all utterances for a specific pillar.
    
    Args:
        pillar_name (str): Pillar name (Ab, Ba, Ka, Ren, Sheut, Defining)
        
    Returns:
        list: List of utterance keys for that pillar
    """
    return UTTERANCES_BY_PILLAR.get(pillar_name, [])


def get_utterances_by_tier(tier):
    """
    Get all utterances for a specific tier.
    
    Args:
        tier (int): Tier level (1-5)
        
    Returns:
        list: List of utterance keys for that tier
    """
    return UTTERANCES_BY_TIER.get(tier, [])

