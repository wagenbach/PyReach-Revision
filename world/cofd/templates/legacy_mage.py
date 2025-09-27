"""
Legacy Mage Template Definition for Chronicles/World of Darkness 1st Edition.
Mage: The Awakening template adapted for 1st edition mechanics.
"""

from . import register_template

# Valid paths for Legacy Mage characters (1st edition)
LEGACY_MAGE_PATHS = [
    "acanthus", "mastigos", "moros", "obrimos", "thyrsus"
]

# Valid orders for Legacy Mage characters (1st edition)
LEGACY_MAGE_ORDERS = [
    "adamantine arrow", "free council", "guardians of the veil", 
    "mysterium", "silver ladder", "apostates"
]

# Valid arcana for 1st edition mages
LEGACY_MAGE_ARCANA = [
    "death", "fate", "forces", "life", "matter", 
    "mind", "prime", "space", "spirit", "time"
]

# Legacy Mage template definition
LEGACY_MAGE_TEMPLATE = {
    "name": "legacy_mage",
    "display_name": "Mage (Legacy)",
    "description": ("Legacy Mage template for World of Darkness 1st Edition. "
                   "Mages are awakened humans who can manipulate reality through their will. "
                   "Uses traditional virtue/vice system and 1st edition mechanics."),
    "bio_fields": ["path", "order", "cabal", "shadow_name"],
    "integrity_name": "Wisdom",
    "starting_integrity": 7,
    "supernatural_power_stat": "gnosis",
    "starting_power_stat": 1,
    "resource_pool": "mana",
    "power_systems": LEGACY_MAGE_ARCANA,
    "anchors": ["virtue", "vice"],  # Legacy uses virtue/vice only
    "merit_categories": ["physical", "social", "mental", "supernatural", "fighting", "style", "mage"],
    "field_validations": {
        "path": {
            "valid_values": LEGACY_MAGE_PATHS
        },
        "order": {
            "valid_values": LEGACY_MAGE_ORDERS
        }
    },
    "legacy_mode": True,  # Flag to indicate this is a legacy template
    "version": "1.0",
    "author": "Chronicles of Darkness Legacy",
    "game_line": "Mage: The Awakening (1st Edition)",
    "notes": "Legacy Mage template for World of Darkness 1st Edition mechanics with virtue/vice anchors"
}

# Register the template
register_template(LEGACY_MAGE_TEMPLATE)
