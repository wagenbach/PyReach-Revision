"""
Hunter: The Vigil Template Definition for Chronicles of Darkness.
Hunters are ordinary people who have seen the supernatural and chosen to fight back.
"""

from . import register_template

# Valid hunter conspiracies
HUNTER_CONSPIRACIES = [
    "aegis kai doru", "ascending ones", "cheiron group", "lucifuge", "malleus maleficarum", 
    "network zero", "null mysteriis", "task force: valkyrie", "union"
]

# Valid hunter compacts
HUNTER_COMPACTS = [
    "ashwood abbey", "barrett commission", "bear lodge", "cainite heresy", "division six",
    "faithful of shulpae", "habibti ma", "hunt club", "knights of saint adrian",
    "long night", "loyalists of thule", "night watch", "operation blackbook", 
    "otodo", "promethean brotherhood", "utopia now", "yuri's group"
]

# Valid hunter tactics
HUNTER_TACTICS = [
    "advanced armory", "benedictions", "elixirs", "reliquary", "thaumatechnology"
]

# Valid hunter endowments
HUNTER_ENDOWMENTS = [
    "aegis talisman", "ascending flame", "cheiron implant", "lucifuge blessing", 
    "malleus ritual", "network equipment", "null mystic", "task force gear", "union device"
]

# Hunter template definition
HUNTER_TEMPLATE = {
    "name": "hunter",
    "display_name": "Hunter",
    "description": "Hunters are ordinary people who have witnessed the supernatural and chosen to take up arms against the darkness.",
    "bio_fields": ["virtue", "vice", "organization", "profession", "safe_place", "vigil"],
    "integrity_name": "Integrity",
    "starting_integrity": 7,
    "supernatural_power_stat": None,
    "starting_power_stat": None,
    "resource_pool": "willpower",
    "power_systems": HUNTER_TACTICS + HUNTER_ENDOWMENTS,
    "anchors": ["virtue", "vice"],
    "merit_categories": ["physical", "social", "mental", "supernatural", "fighting", "style", "hunter"],
    "field_validations": {
        "organization": {
            "valid_values": HUNTER_CONSPIRACIES + HUNTER_COMPACTS + ["independent"]
        }
    },
    "version": "2.0",
    "author": "Chronicles of Darkness",
    "game_line": "Hunter: The Vigil",
    "notes": "Enhanced Hunter template with Tactics, Endowments, and organizational structure"
}

# Register the template
register_template(HUNTER_TEMPLATE) 