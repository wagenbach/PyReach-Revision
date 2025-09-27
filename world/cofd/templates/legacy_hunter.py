"""
Legacy Hunter Template Definition for Chronicles/World of Darkness 1st Edition.
Hunter: The Vigil template adapted for 1st edition mechanics.
"""

from . import register_template

# Valid organizations for Legacy Hunter characters (1st edition)
LEGACY_HUNTER_ORGANIZATIONS = [
    # Tier 1 Compacts
    "the long night", "loyalists of thule", "network zero", "null mysteriis", "union",
    # Tier 2 Conspiracies  
    "aegis kai doru", "ascending ones", "cheiron group", "lucifuge", "malleus maleficarum",
    # Tier 3 Conspiracies
    "task force: valkyrie",
    # Independent
    "independent"
]

# Valid professions for Legacy Hunter characters (1st edition)
LEGACY_HUNTER_PROFESSIONS = [
    "academic", "criminal", "detective", "drifter", "hacker", "journalist", 
    "military", "occultist", "police", "scientist", "socialite", "zealot"
]

# Valid tactics for 1st edition hunters (simplified list)
LEGACY_HUNTER_TACTICS = [
    # Professional Training
    "professional_training",
    # Endowments (organization-specific powers)
    "benediction", "castigation", "advanced_armory", "relic", 
    "thaumatechnology", "elixir", "implant"
]

# Legacy Hunter template definition
LEGACY_HUNTER_TEMPLATE = {
    "name": "legacy_hunter",
    "display_name": "Hunter (Legacy)",
    "description": ("Legacy Hunter template for World of Darkness 1st Edition. "
                   "Hunters are ordinary humans who have seen the supernatural and chosen to fight it. "
                   "Uses traditional virtue/vice system and 1st edition mechanics."),
    "bio_fields": ["profession", "organization", "creed", "cell"],
    "integrity_name": "Integrity",
    "starting_integrity": 7,
    "supernatural_power_stat": None,  # Hunters don't have a supernatural power stat
    "starting_power_stat": None,
    "resource_pool": None,  # Hunters don't have a supernatural resource pool
    "power_systems": LEGACY_HUNTER_TACTICS,
    "anchors": ["virtue", "vice"],  # Legacy uses virtue/vice only
    "merit_categories": ["physical", "social", "mental", "supernatural", "fighting", "style", "hunter"],
    "field_validations": {
        "organization": {
            "valid_values": LEGACY_HUNTER_ORGANIZATIONS
        },
        "profession": {
            "valid_values": LEGACY_HUNTER_PROFESSIONS
        }
    },
    "legacy_mode": True,  # Flag to indicate this is a legacy template
    "version": "1.0",
    "author": "Chronicles of Darkness Legacy",
    "game_line": "Hunter: The Vigil (1st Edition)",
    "notes": "Legacy Hunter template for World of Darkness 1st Edition mechanics with virtue/vice anchors"
}

# Register the template
register_template(LEGACY_HUNTER_TEMPLATE)
