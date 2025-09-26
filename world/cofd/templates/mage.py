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
    "silver ladder", "free council", "seers of the throne", "unaligned"
]

# Valid arcana for Mage characters (prefix conflicting names only)
MAGE_ARCANA = [
    "arcanum_death", "fate", "forces", "life", "matter", "mind", "prime", "space", "spirit", "time"
]

# Mage template definition
MAGE_TEMPLATE = {
    "name": "mage",
    "display_name": "Mage",
    "description": ("Mages are awakened humans who can perceive and manipulate the underlying "
                   "structure of reality through magic. They are organized into Paths based on "
                   "their approach to magic and Orders based on their philosophical beliefs."),
    "bio_fields": ["virtue", "vice", "path", "order", "shadow_name", "cabal"],
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
        }
    },
    "version": "2.0",
    "author": "Chronicles of Darkness",
    "game_line": "Mage: The Awakening",
    "notes": "Enhanced Mage template with Gnosis, Arcana, and Mana pool"
}

# Register the template
register_template(MAGE_TEMPLATE) 