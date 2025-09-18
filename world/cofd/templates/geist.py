"""
Geist: The Sin-Eaters Template Definition for Chronicles of Darkness.
Sin-Eaters are those who have died and returned, bound to powerful ghosts called geists.
"""

from . import register_template

# Valid geist archetypes
GEIST_ARCHETYPES = [
    "mourner", "celebrant", "gatekeeper", "necromancer", "reaper"
]

# Valid geist thresholds (how they died)
GEIST_THRESHOLDS = [
    "torn", "silent", "cold", "prey", "stigmata"
]

# Valid krewe types
GEIST_KREWE_TYPES = [
    "family", "industrial", "network", "military", "academic"
]

# Valid geist manifestations
GEIST_MANIFESTATIONS = [
    "boneyard", "caul", "curse", "marionette", "oracle", "passion", "rage", "shroud"
]

# Valid geist keys
GEIST_KEYS = [
    "cold wind", "grave dirt", "industrial", "pyre-flame", "stillness", "tear-stained"
]

# Geist template definition
GEIST_TEMPLATE = {
    "name": "geist",
    "display_name": "Geist",
    "description": "Sin-Eaters are those who have died and returned to life, bound to powerful ghosts called geists who saved them from true death.",
    "bio_fields": ["virtue", "vice", "archetype", "threshold", "krewe", "burden", "geist_name"],
    "integrity_name": "Synergy",
    "starting_integrity": 7,
    "supernatural_power_stat": "psyche",
    "starting_power_stat": 1,
    "resource_pool": "plasm",
    "power_systems": GEIST_MANIFESTATIONS + GEIST_KEYS,
    "anchors": ["virtue", "vice"],
    "merit_categories": ["physical", "social", "mental", "supernatural", "fighting", "style", "geist"],
    "field_validations": {
        "archetype": {
            "valid_values": GEIST_ARCHETYPES
        },
        "threshold": {
            "valid_values": GEIST_THRESHOLDS
        },
        "krewe": {
            "valid_values": GEIST_KREWE_TYPES
        }
    },
    "version": "2.0",
    "author": "Chronicles of Darkness",
    "game_line": "Geist: The Sin-Eaters",
    "notes": "Enhanced Geist template with Psyche, Manifestations, Keys, and Plasm pool"
}

# Register the template
register_template(GEIST_TEMPLATE) 