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

# Renown types for werewolves (used for gift acquisition)
WEREWOLF_RENOWN = ["cunning", "glory", "honor", "purity", "wisdom"]

# Note: Werewolf gifts (facets) are managed via the werewolf_gifts.py module
# This uses the semantic syntax: +stat gift=shadow_gaze
# Gifts are individual abilities learned based on renown

# Valid werewolf rites (individual rites by rank)
# Rites use semantic syntax: +stat rite=sacred_hunt
WEREWOLF_RITES = [
    # Rank 1 Rites
    "chain_rage", "messenger", "banish", "harness_the_cycle", "totemic_empowerment",
    # Rank 2 Rites
    "bottle_spirit", "infest_locus", "rite_of_the_shroud", "sacred_hunt", "hunting_ground", "moons_mad_love",
    "shackled_lightning", "sigrblot", "wellspring",
    # Rank 3 Rites
    "carrion_feast", "flay_auspice", "kindle_fury", "rite_of_absolution", "shadowbind", "the_thorn_pursuit",
    "banshee_howl", "raiment_of_the_storm", "shadowcall", "supplication",
    # Rank 4 Rites
    "between_worlds", "fetish", "shadow_bridge", "twilight_purge", "hidden_path", "expel", "heal_old_wounds",
    "lupus_venandi",
    # Rank 5 Rites
    "devour", "forge_alliance", "urfarahs_bane", "veil", "great_hunt", "shadow_distortion", "unleash_shadow"
]

# For template validation, we include rites but gifts are validated via werewolf_gifts.py
WEREWOLF_POWERS = WEREWOLF_RITES  # Rites only for backward compatibility

WEREWOLF_LODGES = [
    "Cull", "Cherufe", "Dream Eaters", "Dreaming", "Eaters of the Dead", "Hollow Rivers",
    "Jaw Hags", "Arms", "Blue Moon", "Cage", "Chronicle", "Clocktower", "Crows", "Death",
    "Einherjar", "Embers", "Field", "Firefly", "Gargoyles", "Garm", "Harbingers", "Harmony",
    "Hook Hand", "Hundred Days", "Irkalla", "Lightning", "Muspell", "Prophecy", "Roman Ritual",
    "Screaming Moon", "Seasons", "Seven Venoms", "Shield", "Sleepless Earth", "Swords",
    "Throne", "Thunder", "Unmasked", "Voices", "Wires", "Wrath", "Matagot",
    "Prince Bishop's Wolves", "Temple of Apollo", "Tenders of the Fang",
    "Thousand Steel Teeth", "Tindalosi", "Wendigo", "Wily Crows"
]

# Werewolf template definition
WEREWOLF_TEMPLATE = {
    "name": "werewolf",
    "display_name": "Werewolf",
    "description": "Werewolves are spirit-touched shapeshifters who hunt in the border between flesh and spirit, driven by Rage and bound by ancient codes.",
    "bio_fields": ["bone", "blood", "tribe", "auspice", "pack", "totem", "deed_name", "lodge"],
    "integrity_name": "Harmony",
    "starting_integrity": 7,
    "supernatural_power_stat": "primal_urge",
    "starting_power_stat": 1,
    "resource_pool": "essence",
    "power_systems": WEREWOLF_POWERS,
    "anchors": ["bone", "blood"],
    "merit_categories": ["physical", "social", "mental", "supernatural", "fighting", "style", "werewolf"],
    "field_validations": {
        "tribe": {
            "valid_values": WEREWOLF_TRIBES
        },
        "auspice": {
            "valid_values": WEREWOLF_AUSPICES
        },
        "lodge": {
            "valid_values": WEREWOLF_LODGES
        }
    },
    "version": "2.0",
    "author": "Chronicles of Darkness",
    "game_line": "Werewolf: The Forsaken",
    "notes": "Werewolf the Forsaken template from Chronicles of Darkness 2nd edition"
}

# Register the template
register_template(WEREWOLF_TEMPLATE)


# Power list helper functions
def get_primary_powers():
    """Get list of primary werewolf powers (renown for gift acquisition)."""
    return WEREWOLF_RENOWN.copy()


def get_secondary_powers():
    """Get list of secondary werewolf powers (rites - individual abilities)."""
    return WEREWOLF_RITES.copy()


def get_all_powers():
    """Get all werewolf powers for validation (rites only - gifts validated separately)."""
    return WEREWOLF_RITES.copy()


def get_renown_types():
    """Get list of werewolf renown types."""
    return WEREWOLF_RENOWN.copy() 