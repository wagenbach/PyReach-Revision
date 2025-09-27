"""
Legacy Promethean Template Definition for Chronicles/World of Darkness 1st Edition.
Promethean: The Created template adapted for 1st edition mechanics.
"""

from . import register_template

# Valid lineages for Legacy Promethean characters (1st edition)
LEGACY_PROMETHEAN_LINEAGES = [
    "frankenstein", "galatea", "osiran", "tammuz", "ulgan"
]

# Valid refinements for Legacy Promethean characters (1st edition)
LEGACY_PROMETHEAN_REFINEMENTS = [
    "aurum", "cuprum", "ferrum", "plumbum", "stannum"
]

# Valid transmutations for 1st edition prometheans (simplified list)
LEGACY_PROMETHEAN_TRANSMUTATIONS = [
    # Alchemicus
    "alchemicus",
    # Corporeum
    "corporeum", 
    # Deception
    "deception",
    # Disquiet
    "disquiet",
    # Electrification
    "electrification",
    # Mesmerism
    "mesmerism",
    # Metamorphosis
    "metamorphosis",
    # Pyros
    "pyros",
    # Sensorium
    "sensorium",
    # Vulcanus
    "vulcanus"
]

# Legacy Promethean template definition
LEGACY_PROMETHEAN_TEMPLATE = {
    "name": "legacy_promethean",
    "display_name": "Promethean (Legacy)",
    "description": ("Legacy Promethean template for World of Darkness 1st Edition. "
                   "Prometheans are artificial beings seeking to become human through the Great Work. "
                   "Uses traditional virtue/vice system and 1st edition mechanics."),
    "bio_fields": ["lineage", "refinement", "creator", "role"],
    "integrity_name": "Humanity",  # Prometheans use Humanity in 1st edition
    "starting_integrity": 7,
    "supernatural_power_stat": "azoth",
    "starting_power_stat": 1,
    "resource_pool": "pyros",
    "power_systems": LEGACY_PROMETHEAN_TRANSMUTATIONS,
    "anchors": ["virtue", "vice"],  # Legacy uses virtue/vice only
    "merit_categories": ["physical", "social", "mental", "supernatural", "fighting", "style", "promethean"],
    "field_validations": {
        "lineage": {
            "valid_values": LEGACY_PROMETHEAN_LINEAGES
        },
        "refinement": {
            "valid_values": LEGACY_PROMETHEAN_REFINEMENTS
        }
    },
    "legacy_mode": True,  # Flag to indicate this is a legacy template
    "version": "1.0",
    "author": "Chronicles of Darkness Legacy",
    "game_line": "Promethean: The Created (1st Edition)",
    "notes": "Legacy Promethean template for World of Darkness 1st Edition mechanics with virtue/vice anchors"
}

# Register the template
register_template(LEGACY_PROMETHEAN_TEMPLATE)
