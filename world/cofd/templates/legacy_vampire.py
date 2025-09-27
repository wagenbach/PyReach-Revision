"""
Legacy Vampire Template Definition for Chronicles/World of Darkness 1st Edition.
Vampire: The Requiem template adapted for 1st edition mechanics.
"""

from . import register_template

# Valid clans for Legacy Vampire characters (1st edition)
LEGACY_VAMPIRE_CLANS = [
    "daeva", "gangrel", "mekhet", "nosferatu", "ventrue"
]

# Valid covenants for Legacy Vampire characters (1st edition)
LEGACY_VAMPIRE_COVENANTS = [
    "carthian movement", "circle of the crone", "invictus", 
    "lancea sanctum", "ordo dracul", "unaligned"
]

# Valid vampire disciplines for 1st edition (simplified list)
LEGACY_VAMPIRE_DISCIPLINES = [
    # Core Disciplines
    "animalism", "auspex", "celerity", "dominate", "majesty", 
    "nightmare", "obfuscate", "protean", "resilience", "vigor",
    # Covenant Disciplines
    "coils_of_the_dragon",  # Ordo Dracul
    "cruac",                # Circle of the Crone
    "theban_sorcery"        # Lancea Sanctum
]

# Legacy Vampire template definition
LEGACY_VAMPIRE_TEMPLATE = {
    "name": "legacy_vampire",
    "display_name": "Vampire (Legacy)",
    "description": ("Legacy Vampire template for World of Darkness 1st Edition. "
                   "Vampires are the undead, cursed beings that feed on the blood of mortals. "
                   "Uses traditional virtue/vice system and 1st edition mechanics."),
    "bio_fields": ["clan", "covenant", "sire", "embrace_date"],
    "integrity_name": "Humanity",
    "starting_integrity": 7,
    "supernatural_power_stat": "blood_potency",
    "starting_power_stat": 1,
    "resource_pool": "vitae",  # 1st edition used "vitae" instead of "blood"
    "power_systems": LEGACY_VAMPIRE_DISCIPLINES,
    "anchors": ["virtue", "vice"],  # Legacy uses virtue/vice only
    "merit_categories": ["physical", "social", "mental", "supernatural", "fighting", "style", "vampire"],
    "field_validations": {
        "clan": {
            "valid_values": LEGACY_VAMPIRE_CLANS
        },
        "covenant": {
            "valid_values": LEGACY_VAMPIRE_COVENANTS
        }
    },
    "legacy_mode": True,  # Flag to indicate this is a legacy template
    "version": "1.0",
    "author": "Chronicles of Darkness Legacy",
    "game_line": "Vampire: The Requiem (1st Edition)",
    "notes": "Legacy Vampire template for World of Darkness 1st Edition mechanics with virtue/vice anchors"
}

# Register the template
register_template(LEGACY_VAMPIRE_TEMPLATE)
