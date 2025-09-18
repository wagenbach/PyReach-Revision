"""
Mortal Template Definition for Chronicles of Darkness.
Basic human template without supernatural powers.
"""

from . import register_template

# Mortal template definition
MORTAL_TEMPLATE = {
    "name": "mortal",
    "display_name": "Mortal",
    "description": ("Basic human template for Chronicles of Darkness. Mortals are ordinary humans "
                   "without supernatural powers, but they form the foundation of the World of Darkness."),
    "bio_fields": ["virtue", "vice", "profession", "aspirations"],
    "integrity_name": "Integrity",
    "starting_integrity": 7,
    "supernatural_power_stat": None,
    "starting_power_stat": None,
    "resource_pool": "willpower",
    "power_systems": [],
    "anchors": ["virtue", "vice"],
    "merit_categories": ["physical", "social", "mental", "supernatural", "fighting", "style"],
    "field_validations": {},
    "version": "2.0",
    "author": "Chronicles of Darkness",
    "game_line": "World of Darkness",
    "notes": "Enhanced mortal template with aspirations and standardized structure"
}

# Register the template
register_template(MORTAL_TEMPLATE) 