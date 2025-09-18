"""
Promethean: The Created Template Definition for Chronicles of Darkness.
Prometheans are artificial beings seeking to become truly human through the Great Work.
"""

from . import register_template

# Valid promethean lineages
PROMETHEAN_LINEAGES = [
    "frankenstein", "galatea", "osiran", "tammuz", "ulgan", "extempore"
]

# Valid promethean refinements
PROMETHEAN_REFINEMENTS = [
    "aurum", "argentum", "cuprum", "ferrum", "plumbum", "stannum", "mercurius"
]

# Valid promethean roles
PROMETHEAN_ROLES = [
    "scientist", "soldier", "companion", "servant", "guardian", "artist"
]

# Valid promethean transmutations
PROMETHEAN_TRANSMUTATIONS = [
    "corporeum", "deception", "disquiet", "electrification", "metamorphosis", 
    "mindfulness", "pyros", "saturninus", "spiritus", "vitality"
]

# Valid promethean distillations
PROMETHEAN_DISTILLATIONS = [
    "aes", "cobalus", "cuprum", "ferrum", "plumbum", "stannum"
]

# Promethean template definition
PROMETHEAN_TEMPLATE = {
    "name": "promethean",
    "display_name": "Promethean",
    "description": "Prometheans are artificial beings created from dead matter, seeking to complete the Great Work and become truly human.",
    "bio_fields": ["virtue", "vice", "lineage", "refinement", "creator", "role", "pilgrimage"],
    "integrity_name": "Humanity",
    "starting_integrity": 3,
    "supernatural_power_stat": "azoth",
    "starting_power_stat": 1,
    "resource_pool": "pyros",
    "power_systems": PROMETHEAN_TRANSMUTATIONS + PROMETHEAN_DISTILLATIONS,
    "anchors": ["virtue", "vice"],
    "merit_categories": ["physical", "social", "mental", "supernatural", "fighting", "style", "promethean"],
    "field_validations": {
        "lineage": {
            "valid_values": PROMETHEAN_LINEAGES
        },
        "refinement": {
            "valid_values": PROMETHEAN_REFINEMENTS
        },
        "role": {
            "valid_values": PROMETHEAN_ROLES
        }
    },
    "version": "2.0",
    "author": "Chronicles of Darkness",
    "game_line": "Promethean: The Created",
    "notes": "Enhanced Promethean template with Azoth, Transmutations, Distillations, and Pyros pool"
}

# Register the template
register_template(PROMETHEAN_TEMPLATE) 