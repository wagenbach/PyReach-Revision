"""
Mortal+ Template Definition for Chronicles of Darkness.
Mortals with supernatural abilities - comprehensive list including all minor templates.
"""

from . import register_template

# Core World of Darkness mortal+ types
CORE_MORTAL_PLUS = [
    "Atariya", "Dreamer", "Infected", "Lost Boy", "Plain", "Psychic",
    "Psychic Vampire", "Skinthieves", "Ghost"
]

# Vampire: The Requiem related
VAMPIRE_MORTAL_PLUS = [
    "Ghoul", "Dhampir"
]

# Werewolf: The Forsaken related
WEREWOLF_MORTAL_PLUS = [
    "Wolf-blooded", "Host"
]

# Mage: The Awakening related
MAGE_MORTAL_PLUS = [
    "Sleepwalker", "Proximus"
]

# Changeling: The Lost related
CHANGELING_MORTAL_PLUS = [
    "Fae-Touched"
]

# Promethean: The Created related
PROMETHEAN_MORTAL_PLUS = [
    "Alchemist"
]

# Mummy: The Curse related
MUMMY_MORTAL_PLUS = [
    "Immortal"
]

# Demon: The Descent related
DEMON_MORTAL_PLUS = [
    "Stigmatic", "Demon-Blooded"
]

# All mortal+ types combined
ALL_MORTAL_PLUS_TYPES = (CORE_MORTAL_PLUS + VAMPIRE_MORTAL_PLUS + WEREWOLF_MORTAL_PLUS + 
                        MAGE_MORTAL_PLUS + CHANGELING_MORTAL_PLUS + 
                        PROMETHEAN_MORTAL_PLUS + MUMMY_MORTAL_PLUS + 
                        DEMON_MORTAL_PLUS)

# Psychic power types (for psychics)
PSYCHIC_POWERS = [
    "aura sight", "clairvoyance", "mind reading", "psychokinesis", 
    "psychometry", "telepathy", "precognition", "medium", "biokinesis",
    "cryokinesis", "pyrokinesis", "electrokinesis", "teleportation"
]

# Thaumaturge traditions
THAUMATURGE_TRADITIONS = [
    "apostle of the dark one", "ceremonial magician", "hedge witch", 
    "shaman", "taoist alchemist", "vodoun", "wiccan", "hermetic"
]
# Demon-blooded levels
DEMON_BLOODED_LEVELS = [
    "latent", "offspring", "fractal"
]

# Immortal types
IMMORTAL_TYPES = [
    "blood bather", "body thief", "spirit immortal", "mnemonic immortal",
    "horned immortal", "purified", "arisen"
]

# Game line heritage
GAME_LINE_HERITAGE = [
    "vampire", "werewolf", "mage", "changeling", "hunter", "promethean",
    "geist", "mummy", "demon", "beast", "deviant", "core", "none"
]

# Mortal+ template definition
MORTAL_PLUS_TEMPLATE = {
    "name": "mortal_plus",
    "display_name": "Mortal+",
    "description": "Mortals with supernatural abilities - psychics, mediums, wolf-blooded, sleepwalkers, ghouls, and many other minor supernatural templates from across the Chronicles of Darkness.",
    "bio_fields": ["virtue", "vice", "template_type", "game_line", "heritage", "abilities", "organization"],
    "integrity_name": "Integrity",
    "starting_integrity": 7,
    "supernatural_power_stat": None,
    "starting_power_stat": None,
    "resource_pool": "willpower",
    "power_systems": PSYCHIC_POWERS + THAUMATURGE_TRADITIONS,
    "anchors": ["virtue", "vice"],
    "merit_categories": ["physical", "social", "mental", "supernatural", "fighting", "style", "minor_template"],
    "field_validations": {
        "template_type": {
            "valid_values": ALL_MORTAL_PLUS_TYPES
        },
        "game_line": {
            "valid_values": GAME_LINE_HERITAGE
        },
    },
    "version": "2.1",
    "author": "Chronicles of Darkness",
    "game_line": "Chronicles of Darkness Core",
    "notes": "Enhanced Mortal+ template with psychic powers and thaumaturge traditions"
}

# Register the template
register_template(MORTAL_PLUS_TEMPLATE) 