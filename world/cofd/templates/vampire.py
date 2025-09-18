"""
Vampire Template Definition for Chronicles of Darkness.
Vampire: The Requiem template with Clan and Covenant validations.
"""

from . import register_template

# Valid clans for Vampire characters
VAMPIRE_CLANS = [
    "daeva", "gangrel", "mekhet", "nosferatu", "ventrue"
]

# Valid covenants for Vampire characters
VAMPIRE_COVENANTS = [
    "carthian movement", "circle of the crone", "invictus", 
    "lancea et sanctum", "ordo dracul", "unaligned"
]

# Valid vampire disciplines
VAMPIRE_DISCIPLINES = [
    "animalism", "auspex", "bloodworking", "cachexy", "celerity", "coils of the dragon",
    "cruac", "dominate", "majesty", "nightmare", "obfuscate", "praestantia", "protean",
    "resilience", "theban sorcery", "vigor"
]

# Vampire template definition
VAMPIRE_TEMPLATE = {
    "name": "vampire",
    "display_name": "Vampire",
    "description": ("Vampires are the undead, cursed beings that feed on the blood of mortals. "
                   "They are organized into Clans based on their vampiric lineage and Covenants "
                   "based on their political and religious beliefs."),
    "bio_fields": ["mask", "dirge", "clan", "covenant", "sire", "embrace_date"],
    "integrity_name": "Humanity",
    "starting_integrity": 7,
    "supernatural_power_stat": "blood_potency",
    "starting_power_stat": 1,
    "resource_pool": "blood",
    "power_systems": VAMPIRE_DISCIPLINES,
    "anchors": ["mask", "dirge"],
    "merit_categories": ["physical", "social", "mental", "supernatural", "fighting", "style", "vampire"],
    "field_validations": {
        "clan": {
            "valid_values": VAMPIRE_CLANS
        },
        "covenant": {
            "valid_values": VAMPIRE_COVENANTS
        }
    },
    "version": "2.0",
    "author": "Chronicles of Darkness",
    "game_line": "Vampire: The Requiem",
    "notes": "Enhanced Vampire template with power stats, disciplines, and resource pools"
}

# Register the template
register_template(VAMPIRE_TEMPLATE) 