"""
Mage Template Definition for Chronicles of Darkness.
Mage: The Awakening template with Path and Order validations.
"""

from . import register_template

# Valid paths for Mage characters
MAGE_PATHS = [
    "acanthus", "mastigos", "moros", "obrimos", "thyrsus"
]

# Valid orders for Mage characters
MAGE_ORDERS = [
    "adamantine arrow", "guardians of the veil", "mysterium", 
    "silver ladder", "free council", "seers of the throne", "tremere", "abyssal", "unaligned"
]

# Valid arcana for Mage characters (prefix conflicting names only)
MAGE_ARCANA = [
    "arcanum_death", "fate", "forces", "life", "matter", "mind", "prime", "space", "spirit", "time"
]

# Legacy mappings - legacies accessible by Path
LEGACIES_BY_PATH = {
    "acanthus": [
        "chronologue", "house of ariadne", "awakening gambit", "blank badge", 
        "carnival melancholy", "pygmalion society", "sisterhood of the blessed", 
        "storm keepers", "walkers in mists"
    ],
    "mastigos": [
        "intendants of the building", "logophages", "nagaraja", "reality stalkers",
        "bearers of the eternal voice", "bene ashmedai", "brotherhood of the demon wind",
        "clavicularius", "cryptologos", "parliament of the needle", "subtle ones"
    ],
    "moros": [
        "eleventh question", "kitchen alchemists", "nighthawks", "stone scribes",
        "bokor", "forge masters", "uncrowned kings", "votaries of the ordained", "legion"
    ],
    "obrimos": [
        "illumined path", "perfected adepts", "shapers of the invisible", "tyrian archons",
        "daksha", "echowalkers", "tamers of fire", "thrice-great", "transhuman engineers"
    ],
    "thyrsus": [
        "engineers of the system", "keepers of the covenant", "chrysalides", "dreamspeakers",
        "gilgamesh's lions", "orphans of proteus", "tamers of blood"
    ]
}

# Legacy mappings - legacies accessible by Order
LEGACIES_BY_ORDER = {
    "adamantine arrow": [
        "perfected adepts", "awakening gambit", "brotherhood of the demon wind",
        "devourers of the flesh", "hunters of the golden wing", "votaries of the ordained"
    ],
    "free council": [
        "blank badge", "cryptologos", "dreamspeakers", "parliament of the needle",
        "transhuman engineers"
    ],
    "guardians of the veil": [
        "eleventh question", "house of ariadne", "bearers of the eternal voice",
        "subtle ones", "votaries of the ordained", "legion"
    ],
    "mysterium": [
        "eleventh question", "logophages", "reality stalkers", "stone scribes",
        "cryptologos", "daksha", "walkers in mists"
    ],
    "silver ladder": [
        "illumined path", "keepers of the covenant", "logophages", "nighthawks",
        "bene ashmedai", "carnival melancholy", "clavicularius", "sisterhood of the blessed",
        "thrice-great"
    ],
    "seers of the throne": [
        "chronologue", "engineers of the system", "house of ariadne", "tyrian archons",
        "architects of the future", "bene ashmedai", "chrysalides", "clavicularius",
        "cryptologos", "secret order of the gate"
    ],
    "tremere": [
        "house nagaraja", "house seo hel", "house thrax", "house vedmak"
    ],
    "abyssal": [
        "hand of destiny", "keepers of the chrysalis"
    ]
}

# Unlinked legacies - accessible to anyone
UNLINKED_LEGACIES = [
    "archimandrite", "aurora auricalcinae", "bull's children", "celestial masters",
    "emergent", "fallen pillar", "filiae philosopharum", "hollow keepers",
    "lords of mars", "singers in silence", "skalds", "sphinxes", "tamers of the cave",
    "tamers of the winds", "tephra", "thread-cutters", "timori", "torches of artemis",
    "wind-singers"
]

# All valid legacies (for validation)
ALL_LEGACIES = list(set(
    [legacy for legacies in LEGACIES_BY_PATH.values() for legacy in legacies] +
    [legacy for legacies in LEGACIES_BY_ORDER.values() for legacy in legacies] +
    UNLINKED_LEGACIES
))

# Mage template definition
MAGE_TEMPLATE = {
    "name": "mage",
    "display_name": "Mage",
    "description": ("Mages are awakened humans who can perceive and manipulate the underlying "
                   "structure of reality through magic. They are organized into Paths based on "
                   "their approach to magic and Orders based on their philosophical beliefs."),
    "bio_fields": ["virtue", "vice", "path", "order", "shadow_name", "cabal", "legacy"],
    "integrity_name": "Wisdom",
    "starting_integrity": 7,
    "supernatural_power_stat": "gnosis",
    "starting_power_stat": 1,
    "resource_pool": "mana",
    "power_systems": MAGE_ARCANA,
    "anchors": ["virtue", "vice"],
    "merit_categories": ["physical", "social", "mental", "supernatural", "fighting", "style", "mage"],
    "field_validations": {
        "path": {
            "valid_values": MAGE_PATHS
        },
        "order": {
            "valid_values": MAGE_ORDERS
        },
        "legacy": {
            "valid_values": ALL_LEGACIES,
            "custom_validation": "legacy"  # Flag for custom validation logic
        }
    },
    "version": "2.0",
    "author": "Chronicles of Darkness",
    "game_line": "Mage: The Awakening",
    "notes": "Enhanced Mage template with Gnosis, Arcana, Mana pool, and Legacy system"
}

# Register the template
register_template(MAGE_TEMPLATE)


# Power list helper functions
def get_primary_powers():
    """Get list of primary mage powers (arcana rated 1-5)."""
    return MAGE_ARCANA.copy()


def get_secondary_powers():
    """Get list of secondary mage powers (none - mages only have arcana)."""
    return []


def get_all_powers():
    """Get all mage powers for validation."""
    return MAGE_ARCANA.copy() 