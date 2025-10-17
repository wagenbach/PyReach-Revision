"""
Promethean: The Created Template Definition for Chronicles of Darkness.
Prometheans are artificial beings seeking to become truly human through the Great Work.
"""

from . import register_template
from world.cofd.powers.promethean_powers import (
    PROMETHEAN_LINEAGES, PROMETHEAN_BESTOWMENTS, PROMETHEAN_REFINEMENTS,
    PROMETHEAN_TRANSMUTATIONS, PROMETHEAN_ALEMBICS, ALL_ALEMBICS, PROMETHEAN_DISTILLATIONS
)


# Promethean template definition
PROMETHEAN_TEMPLATE = {
    "name": "promethean",
    "display_name": "Promethean",
    "description": "Prometheans are artificial beings created from dead matter, seeking to complete the Great Work and become truly human.",
    "bio_fields": ["virtue", "vice", "lineage", "refinement", "creator", "pilgrimage", "throng", "athanor"],
    "integrity_name": "Humanity",
    "starting_integrity": 3,
    "supernatural_power_stat": "azoth",
    "starting_power_stat": 1,
    "resource_pool": "pyros",
    # Individual Alembics are purchased, not dots in Transmutations
    "power_systems": ALL_ALEMBICS + PROMETHEAN_BESTOWMENTS,
    "individual_powers": True,  # Flag indicating powers are purchased individually
    "power_categories": PROMETHEAN_TRANSMUTATIONS,  # For organization/display
    "anchors": ["virtue", "vice"],
    "merit_categories": ["physical", "social", "mental", "supernatural", "fighting", "style", "promethean"],
    "field_validations": {
        "lineage": {
            "valid_values": PROMETHEAN_LINEAGES
        },
        "refinement": {
            "valid_values": PROMETHEAN_REFINEMENTS
        }
    },
    "version": "2.0",
    "author": "Chronicles of Darkness",
    "game_line": "Promethean: The Created",
    "notes": "Promethean template with Azoth, individual Alembics (Transmutations), Bestowments, Pyros pool, and Athanor system"
}

# Register the template
register_template(PROMETHEAN_TEMPLATE)

