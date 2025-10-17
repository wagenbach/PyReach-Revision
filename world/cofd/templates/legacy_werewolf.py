"""
Legacy Werewolf Template Definition for Chronicles/World of Darkness 1st Edition.
Werewolf: The Forsaken template adapted for 1st edition mechanics.
"""

from . import register_template

# Valid auspices for Legacy Werewolf characters (1st edition)
LEGACY_WEREWOLF_AUSPICES = [
    "cahalith", "elodoth", "irraka", "ithaeur", "rahu"
]

# Valid tribes for Legacy Werewolf characters (1st edition)
LEGACY_WEREWOLF_TRIBES = [
    "blood talons", "bone shadows", "hunters in darkness", 
    "iron masters", "storm lords", "ghost wolves"
]

# Valid werewolf gifts for 1st edition (simplified list)
LEGACY_WEREWOLF_GIFTS = [
    # Renown Gifts
    "cunning", "glory", "honor", "purity", "wisdom",
    # Moon Gifts
    "crescent_moon", "full_moon", "gibbous_moon", "half_moon", "new_moon",
    # Shadow Gifts
    "death", "elementals", "nature", "spirits",
    # Wolf Gifts
    "hunting", "pack", "strength", "warding"
]

# Legacy Werewolf template definition
LEGACY_WEREWOLF_TEMPLATE = {
    "name": "legacy_werewolf",
    "display_name": "Werewolf (Legacy)",
    "description": ("Legacy Werewolf template for World of Darkness 1st Edition. "
                   "Werewolves are the chosen of Luna, protectors of the boundary between "
                   "the physical and spirit worlds. Uses traditional virtue/vice system."),
    "bio_fields": ["auspice", "tribe", "pack"],
    "integrity_name": "Harmony",
    "starting_integrity": 7,
    "supernatural_power_stat": "primal_urge",
    "starting_power_stat": 1,
    "resource_pool": "essence",
    "power_systems": LEGACY_WEREWOLF_GIFTS,
    "anchors": ["virtue", "vice"],  # Legacy uses virtue/vice only
    "merit_categories": ["physical", "social", "mental", "supernatural", "fighting", "style", "werewolf"],
    "field_validations": {
        "auspice": {
            "valid_values": LEGACY_WEREWOLF_AUSPICES
        },
        "tribe": {
            "valid_values": LEGACY_WEREWOLF_TRIBES
        }
    },
    "legacy_mode": True,  # Flag to indicate this is a legacy template
    "version": "1.0",
    "author": "Chronicles of Darkness Legacy",
    "game_line": "Werewolf: The Forsaken (1st Edition)",
    "notes": "Legacy Werewolf template for World of Darkness 1st Edition mechanics with virtue/vice anchors"
}

# Register the template
register_template(LEGACY_WEREWOLF_TEMPLATE)
