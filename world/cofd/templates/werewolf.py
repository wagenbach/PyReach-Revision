"""
Werewolf: The Forsaken Template Definition for Chronicles of Darkness.
Werewolves are spirit-touched shapeshifters who hunt in the border between flesh and spirit.
"""

from . import register_template

# Valid werewolf tribes
WEREWOLF_TRIBES = [
    "blood talons", "bone shadows", "hunters in darkness", 
    "iron masters", "storm lords", "ghost wolves"
]

# Valid werewolf auspices
WEREWOLF_AUSPICES = [
    "cahalith", "elodoth", "irraka", "ithaeur", "rahu"
]

# Valid renown types
WEREWOLF_RENOWN = [
    "cunning", "glory", "honor", "purity", "wisdom"
]

# Valid werewolf gifts
WEREWOLF_GIFTS = [
    "change", "death", "dominance", "elements", "insight", "inspiration", "knowledge",
    "nature", "rage", "strength", "technology", "travel", "war", "weather"
]

# Valid werewolf rites
WEREWOLF_RITES = [
    "accord", "binding", "cleansing", "dedication", "funeral", "hunting", "pack",
    "punishment", "renown", "sacred hunt", "territorial", "warding"
]

# Werewolf template definition
WEREWOLF_TEMPLATE = {
    "name": "werewolf",
    "display_name": "Werewolf",
    "description": "Werewolves are spirit-touched shapeshifters who hunt in the border between flesh and spirit, driven by Rage and bound by ancient codes.",
    "bio_fields": ["bone", "blood", "tribe", "auspice", "pack", "totem", "deed_name"],
    "integrity_name": "Harmony",
    "starting_integrity": 7,
    "supernatural_power_stat": "primal_urge",
    "starting_power_stat": 1,
    "resource_pool": "essence",
    "power_systems": WEREWOLF_GIFTS + WEREWOLF_RITES,
    "anchors": ["bone", "blood"],
    "merit_categories": ["physical", "social", "mental", "supernatural", "fighting", "style", "werewolf"],
    "field_validations": {
        "tribe": {
            "valid_values": WEREWOLF_TRIBES
        },
        "auspice": {
            "valid_values": WEREWOLF_AUSPICES
        }
    },
    "version": "2.0",
    "author": "Chronicles of Darkness",
    "game_line": "Werewolf: The Forsaken",
    "notes": "Enhanced Werewolf template with Primal Urge, Gifts, Rites, and Essence pool"
}

# Register the template
register_template(WEREWOLF_TEMPLATE) 