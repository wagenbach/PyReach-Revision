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

# Valid werewolf gifts (prefix conflicting names only)
WEREWOLF_GIFTS = [
    "change", "gift_death", "dominance", "elements", "insight", "inspiration", "knowledge",
    "nature", "rage", "gift_strength", "technology", "travel", "war", "weather"
]

# Valid werewolf rites (individual rites by rank)
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
    "power_systems": WEREWOLF_GIFTS + WEREWOLF_RITES,
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