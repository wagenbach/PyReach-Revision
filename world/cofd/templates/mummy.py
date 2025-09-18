"""
Mummy: The Curse Template Definition for Chronicles of Darkness.
Mummies are ancient immortals bound to serve the Judges of Duat in the modern world.
"""

from . import register_template

# Valid mummy guilds
MUMMY_GUILDS = [
    "mesen-nebu", "sesha-hebsu", "su-menent", "tef-aabhi", "amenti"
]

# Valid mummy decrees
MUMMY_DECREES = [
    "balance", "fortune", "knowledge", "protection", "vengeance"
]

# Valid mummy judges
MUMMY_JUDGES = [
    "djehuty", "duamutef", "hapi", "imsety", "kebehsenuf", "nehebkau", "neith", "ptah", "sobek"
]

# Valid mummy utterances
MUMMY_UTTERANCES = [
    "afire", "bone", "elements", "flesh", "guidance", "glory", "reign", "vision", "word"
]

# Valid mummy affinities
MUMMY_AFFINITIES = [
    "ab", "ba", "ka", "khaibit", "khat", "ren", "sahu", "sekhem", "sheut"
]

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
    "power_systems": MUMMY_UTTERANCES + MUMMY_AFFINITIES,
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

