"""
Deviant: The Renegades Template Definition for Chronicles of Darkness.
Deviants are people transformed by conspiracies, escaped from laboratories and secret programs.
"""

from . import register_template

# Valid deviant origins
DEVIANT_ORIGINS = [
    "cephalist", "cheiron group", "government", "pentex", "seers of the throne", "technocracy"
]

# Valid deviant clades
DEVIANT_CLADES = [
    "coactive", "devoted", "genotypal", "invasive", "mutant", "pelagic", "remnant"
]

# Valid deviant scars
DEVIANT_SCARS = [
    "baseline", "conspicuous", "paranoid", "stubborn", "loyal", "untrustworthy"
]

# Valid deviant variations
DEVIANT_VARIATIONS = [
    "biological", "cybernetic", "energy", "mental", "physical", "sensory", "temporal"
]

# Valid deviant adaptations
DEVIANT_ADAPTATIONS = [
    "defensive", "environmental", "locomotion", "offensive", "sensory", "social", "utility"
]

# Deviant template definition
DEVIANT_TEMPLATE = {
    "name": "deviant",
    "display_name": "Deviant",
    "description": "Deviants are people who have been transformed by conspiracies and secret organizations, then escaped or been discarded.",
    "bio_fields": ["virtue", "vice", "origin", "clade", "scar", "conspiracy", "touchstone"],
    "integrity_name": "Loyalty",
    "starting_integrity": 7,
    "supernatural_power_stat": "acclimation",
    "starting_power_stat": 1,
    "resource_pool": "willpower",
    "power_systems": DEVIANT_VARIATIONS + DEVIANT_ADAPTATIONS + DEVIANT_SCARS,
    "anchors": ["virtue", "vice"],
    "merit_categories": ["physical", "social", "mental", "supernatural", "fighting", "style", "deviant"],
    "field_validations": {
        "origin": {
            "valid_values": DEVIANT_ORIGINS
        },
        "clade": {
            "valid_values": DEVIANT_CLADES
        }
    },
    "version": "2.0",
    "author": "Chronicles of Darkness",
    "game_line": "Deviant: The Renegades",
    "notes": "Enhanced Deviant template with Deviation, Variations, Adaptations, and specialized mechanics"
}

# Register the template
register_template(DEVIANT_TEMPLATE) 