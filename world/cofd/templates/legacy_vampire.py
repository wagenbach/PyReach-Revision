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

# Clan-specific discipline mappings (new rating x 5 XP for clan disciplines)
LEGACY_VAMPIRE_CLAN_DISCIPLINES = {
    "daeva": ["celerity", "majesty", "vigor"],
    "gangrel": ["animalism", "protean", "resilience"], 
    "mekhet": ["auspex", "celerity", "obfuscate"],
    "nosferatu": ["nightmare", "obfuscate", "vigor"],
    "ventrue": ["animalism", "dominate", "resilience"]
}

# All core disciplines (can be learned by any clan, but cost varies)
LEGACY_VAMPIRE_CORE_DISCIPLINES = [
    "animalism", "auspex", "celerity", "dominate", "majesty", 
    "nightmare", "obfuscate", "protean", "resilience", "vigor"
]

# Covenant disciplines (always "other" - new rating x 7 XP)
LEGACY_VAMPIRE_COVENANT_DISCIPLINES = [
    "coils_of_the_dragon",  # Ordo Dracul
    "cruac",                # Circle of the Crone (blood sorcery)
    "theban_sorcery"        # Lancea Sanctum (blood sorcery)
]

# All vampire disciplines combined for validation
LEGACY_VAMPIRE_DISCIPLINES = LEGACY_VAMPIRE_CORE_DISCIPLINES + LEGACY_VAMPIRE_COVENANT_DISCIPLINES

def is_clan_discipline(clan, discipline):
    """Check if a discipline is in-clan for a specific clan"""
    clan = clan.lower() if clan else ""
    discipline = discipline.lower() if discipline else ""
    
    clan_discs = LEGACY_VAMPIRE_CLAN_DISCIPLINES.get(clan, [])
    return discipline in clan_discs

def get_vampire_discipline_cost(clan, discipline, target_level):
    """Get the cost for a vampire discipline based on clan"""
    if is_clan_discipline(clan, discipline):
        return target_level * 5  # Clan discipline cost
    else:
        return target_level * 7  # Other discipline cost

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
