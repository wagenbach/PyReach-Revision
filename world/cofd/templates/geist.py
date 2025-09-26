"""
Geist: The Sin-Eaters Template Definition for Chronicles of Darkness.
Sin-Eaters are those who have died and returned, bound to powerful ghosts called geists.
"""

from . import register_template


# Valid geist burdens (how they died)
GEIST_BURDENS = [
    "abiding", "bereaved", "hungry", "kindly", "vengeful"
]

# Valid krewe types
GEIST_KREWE_TYPES = [
    "family", "industrial", "network", "military", "academic"
]

# Valid geist manifestations
GEIST_HAUNTS = [
    "boneyard", "caul", "curse", "dirge", "marionette", "memoria", "oracle", "rage", "shroud", "tomb"
]

# Valid geist keys
GEIST_KEYS = [
    "beasts", "blood", "chance", "cold wind", "deep waters", "disease", "grave dirt", "pyre flame", "stillness"
]

# Valid geist ceremonies
GEIST_CEREMONIES = [
    # Level 1 Ceremonies
    "dead man's camera", "death watch", "diviner's jawbone", "lovers' telephone", "ishtar's perfume",
    # Level 2 Ceremonies
    "crow girl kiss", "gifts of persephone", "ghost trap", "skeleton key",
    # Level 3 Ceremonies
    "bestow regalia", "krewe binding", "speaker for the dead", "black cat's crossing", "bloody codex", "dumb supper",
    # Level 4 Ceremonies
    "forge anchor", "maggot homonculus",
    # Level 5 Ceremonies
    "pass on", "ghost binding", "persephone's return"
    ]

# Valid crisis point triggers for geists
GEIST_CRISIS_TRIGGERS = [
    "betrayal", "abandonment", "mortality", "innocence", "loss", "helplessness", "failure", "isolation"
]

# Valid remembrance trait types (skills or merits ≤3 dots)
GEIST_REMEMBRANCE_SKILLS = [
    "athletics", "brawl", "drive", "firearms", "larceny", "stealth", "survival", "weaponry",
    "animal_ken", "empathy", "expression", "intimidation", "persuasion", "socialize", "streetwise", "subterfuge",
    "crafts", "investigation", "medicine", "occult", "politics", "science"
]

GEIST_REMEMBRANCE_MERITS = [
    "contacts", "allies", "resources", "safe_place", "library", "mentor", "retainer", "status"
]

# Key descriptions with unlock attributes and mechanics
GEIST_KEY_DETAILS = {
    "beasts": {
        "full_name": "The Key of Beasts",
        "alternate_names": "The Primeval Key, the Key of Tooth and Claw, the Key of Verdant Savagery",
        "unlock_attribute": "Wits",
        "resonance": "Resonant in places where humanity is no longer dominant (abandoned buildings, wilderness, city parks after dark) or when targeting animals.",
        "doom": "Automatically fail an action targeting an animal, or any action an animal could plausibly hinder."
    },
    "blood": {
        "full_name": "The Key of Blood", 
        "alternate_names": "The Stigmatic Key, the Key of Veils and Shades, the Key of Crimson Agony",
        "unlock_attribute": "Presence",
        "resonance": "Resonant when situations spiral out of control, especially in unpremeditated violent situations.",
        "doom": "Next attempt to avoid violent confrontation results in automatic dramatic failure."
    },
    "chance": {
        "full_name": "The Key of Chance",
        "alternate_names": "The Bastard's Key, the Key of Jinx and Hex, the Key of Black Humor", 
        "unlock_attribute": "Dexterity",
        "resonance": "Resonant when risking something important on a single action, or targeting machines with moving parts capable of lethal damage.",
        "doom": "Next roll with +3 or greater bonus becomes a chance die instead."
    },
    "cold wind": {
        "full_name": "The Key of Cold Wind",
        "alternate_names": "The Breathless Key, the Key of Gale and Garrote, the Key of Ivory Sorrow",
        "unlock_attribute": "Resolve", 
        "resonance": "Resonant in Environmental Tilts (Blizzard, Extreme Cold, Heavy Winds) or where ambient noise prevents conversation.",
        "doom": "Gain Extreme Cold Tilt for (10-Synergy) hours or until revealing a damaging personal secret."
    },
    "deep waters": {
        "full_name": "The Key of Deep Waters",
        "alternate_names": "The Tear-Stained Key, the Key of Wave and Whirlpool, the Key of Azure Futility",
        "unlock_attribute": "Manipulation",
        "resonance": "Resonant when breathing is impaired or target is at least half submerged in water.",
        "doom": "Next full Willpower replenishment only grants 1 Willpower instead."
    },
    "disease": {
        "full_name": "The Key of Disease",
        "alternate_names": "The Wasting Key, The Key of Plague and Pestilence, The Key of Bilious Despair",
        "unlock_attribute": "Stamina",
        "resonance": "Resonant in places of illness/poison (hospitals, swamps) or on targets with the Sick Tilt.",
        "doom": "Suffer the Sick Tilt until the end of the next scene."
    },
    "grave dirt": {
        "full_name": "The Key of Grave Dirt", 
        "alternate_names": "The Crushing Key, the Key of Stone and Barrow, the Key of Slate Bereavement",
        "unlock_attribute": "Strength",
        "resonance": "Resonant in places dedicated to the past (graveyards, memorials, abandoned buildings) or when underground.",
        "doom": "Must spend 1 Willpower for any extended action for rest of story (resolved by sacrificing a living being)."
    },
    "pyre flame": {
        "full_name": "The Key of Pyre Flame",
        "alternate_names": "The Burning Key, the Key of Ash and Brand, the Lover's Key, the Key of Golden Annihilation", 
        "unlock_attribute": "Intelligence",
        "resonance": "Resonant when used on targets that are on fire or subject to Extreme Heat Tilt.",
        "doom": "Gain Extreme Heat Tilt for (10-Synergy) hours or until deliberately destroying a valued possession."
    },
    "stillness": {
        "full_name": "The Key of Stillness",
        "alternate_names": "The Silent Key, the Key of Shroud and Shadow, the Key of Jet Uncertainty",
        "unlock_attribute": "Composure", 
        "resonance": "Resonant when target is unaware of Bound's presence, helpless, or only Bound and target are present.",
        "doom": "Next spoken word resolves Doom and Haunt Condition, or gain Mute Condition until end of chapter."
    }
}

# Geist template definition
GEIST_TEMPLATE = {
    "name": "geist",
    "display_name": "Geist",
    "description": "Sin-Eaters are those who have died and returned to life, bound to powerful ghosts called geists who saved them from true death.",
    "bio_fields": ["root", "bloom",  "burden", "geist_name", "krewe"],
    "integrity_name": "Synergy",
    "starting_integrity": 7,
    "supernatural_power_stat": "psyche",
    "starting_power_stat": 1,
    "resource_pool": "plasm",
    "power_systems": GEIST_HAUNTS + GEIST_KEYS + GEIST_CEREMONIES,
    "anchors": ["root", "bloom"],
    "merit_categories": ["physical", "social", "mental", "supernatural", "fighting", "style", "geist"],
    "field_validations": {
        "burden": {
            "valid_values": GEIST_BURDENS
        },
        "krewe": {
            "valid_values": GEIST_KREWE_TYPES
        }
    },
    "version": "2.0",
    "author": "Chronicles of Darkness",
    "game_line": "Geist: The Sin-Eaters",
    "notes": "Enhanced Geist template with Psyche, Manifestations, Keys, and Plasm pool",
    
    # Geist-specific secondary character sheet configuration
    "geist_config": {
        "rank": 3,
        "size": 5,
        "base_attributes": {
            "power": 1,
            "finesse": 1, 
            "resistance": 1
        },
        "attribute_dots_to_assign": 12,
        "max_attribute": 9,
        "crisis_triggers": GEIST_CRISIS_TRIGGERS,
        "remembrance_skills": GEIST_REMEMBRANCE_SKILLS,
        "remembrance_merits": GEIST_REMEMBRANCE_MERITS,
        "remembrance_max_dots": 3,
        "innate_keys": GEIST_KEYS,
        "bio_fields": ["concept", "remembrance_description", "virtue", "vice", "crisis_trigger", "ban", "bane", "innate_key"]
    }
}

# Register the template
register_template(GEIST_TEMPLATE) 