"""
Legacy Geist Template Definition for Chronicles/World of Darkness 1st Edition.
Geist: The Sin-Eaters template adapted for 1st edition mechanics.
"""

from . import register_template

# Valid archetypes for Legacy Geist characters (1st edition)
LEGACY_GEIST_ARCHETYPES = [
    "bonepicker", "celebrant", "gatekeeper", "mourner", "necromancer", "oracle", "pilgrim"
]

# Valid thresholds for Legacy Geist characters (1st edition)
LEGACY_GEIST_THRESHOLDS = [
    "torn", "silent", "stigmata", "primordial", "prey"
]

# Valid keys and ceremonies for 1st edition geists (simplified list)
LEGACY_GEIST_POWERS = [
    # Keys
    "beasts", "blood", "chance", "cold_wind", "deep_waters", 
    "disease", "grave_dirt", "pyre_flame", "stillness",
    # Ceremonies
    "ceremonies"
]

# Legacy Geist template definition
LEGACY_GEIST_TEMPLATE = {
    "name": "legacy_geist",
    "display_name": "Geist (Legacy)",
    "description": ("Legacy Geist template for World of Darkness 1st Edition. "
                   "Sin-Eaters are humans who died and returned bound to a geist. "
                   "Uses traditional virtue/vice system and 1st edition mechanics."),
    "bio_fields": ["archetype", "threshold", "krewe", "geist_name"],
    "integrity_name": "Synergy",
    "starting_integrity": 7,
    "supernatural_power_stat": "psyche",  # 1st edition used "psyche" instead of "synergy"
    "starting_power_stat": 1,
    "resource_pool": "plasm",
    "power_systems": LEGACY_GEIST_POWERS,
    "anchors": ["virtue", "vice"],  # Legacy uses virtue/vice only
    "merit_categories": ["physical", "social", "mental", "supernatural", "fighting", "style", "geist"],
    "field_validations": {
        "archetype": {
            "valid_values": LEGACY_GEIST_ARCHETYPES
        },
        "threshold": {
            "valid_values": LEGACY_GEIST_THRESHOLDS
        }
    },
    "legacy_mode": True,  # Flag to indicate this is a legacy template
    "version": "1.0",
    "author": "Chronicles of Darkness Legacy",
    "game_line": "Geist: The Sin-Eaters (1st Edition)",
    "notes": "Legacy Geist template for World of Darkness 1st Edition mechanics with virtue/vice anchors"
}

# Register the template
register_template(LEGACY_GEIST_TEMPLATE)
