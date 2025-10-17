"""
Hunter: The Vigil Template Definition for Chronicles of Darkness.
Hunters are ordinary people who have seen the supernatural and chosen to fight back.
"""

from . import register_template
from world.cofd.powers.hunter_organizations import (
    ALL_CONSPIRACIES, 
    ALL_COMPACTS,
    get_organization,
    get_organization_summary,
    get_compact_names,
    get_conspiracy_names,
    get_all_organization_names
)
from world.cofd.powers.hunter_tactics import (
    ALL_TACTICS,
    ALL_MENTAL_TACTICS,
    ALL_PHYSICAL_TACTICS,
    ALL_SOCIAL_TACTICS,
    get_tactic,
    get_tactic_summary
)

# Valid hunter conspiracies (list of names for validation)
HUNTER_CONSPIRACIES = get_conspiracy_names()

# Valid hunter compacts (list of names for validation)
HUNTER_COMPACTS = get_compact_names()

# Valid hunter tactics (mental, physical, and social)
HUNTER_TACTICS = ALL_TACTICS

# Valid hunter endowments
HUNTER_ENDOWMENTS = [
    "advanced armory", "benediction", "elixirs", "reliquary", "thaumatechnology",
    "animal control kit", "castigation", "enkoimesis", "horror within", "infusion",
    "inspiration", "lives remembered", "perispiritism", "relics", "teleinformatics",
    "xenotechnology", "dreamscape", "ink", "rites du cheval", "seitokuken", "goetic gospel",
    "rites of denial", "all-seeing eye", "anthropophagy", "bacchanal",
    "i'm doing science", "monster media", "the prayer", "rite of hecate", "setto",
    "unearthed secrets", "your friends and neighbors"
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