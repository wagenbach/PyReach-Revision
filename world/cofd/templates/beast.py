"""
Beast: The Primordial Template Definition for Chronicles of Darkness.
Beasts are primordial monsters who feed on fear and embody ancient nightmares.
"""

from . import register_template

# Valid beast families
BEAST_FAMILIES = [
    "anakim", "eshmaki", "makara", "namtaru", "ugallu"
]

# Valid beast hungers
BEAST_HUNGERS = [
    "collector", "competitor", "destroyer", "nemesis", "predator", "ravager", "tyrant"
]

# Valid beast horrors (nightmare themes)
BEAST_HORRORS = [
    "depths", "fire", "isolation", "labyrinth", "mirror", "storm", "wild"
]

# Valid beast nightmares
BEAST_NIGHTMARES = [
    "alien", "environmental", "isolating", "pursuing", "ravaging", "social", "technological"
]

# Valid beast atavisms by family
BEAST_ATAVISMS = {
    "anakim": [
        "cyclopean strength", "looming presence", "mimir's wisdom", "titanic blow"
    ],
    "eshmaki": [
        "dragonfire", "from the shadows", "limb from limb", "relentless hunter"
    ],
    "makara": [
        "alien allure", "heart of the ocean", "monster from the deep", "siren's treacherous song"
    ],
    "namtaru": [
        "basilisk's touch", "infestation", "shadowed soul", "unbreakable"
    ],
    "ugallu": [
        "eye of heaven", "needs must", "storm-lashed", "wings of the raptor"
    ]
}

# All atavisms as a flat list for validation
ALL_BEAST_ATAVISMS = [
    atavism for family_atavisms in BEAST_ATAVISMS.values() 
    for atavism in family_atavisms
]

# Beast template definition
BEAST_TEMPLATE = {
    "name": "beast",
    "display_name": "Beast",
    "description": "Beasts are primordial monsters who feed on fear and embody the ancient nightmares that lurk in the collective unconscious.",
    "bio_fields": ["virtue", "vice", "family", "hunger", "horror", "lair", "inheritance"],
    "integrity_name": "Satiety",
    "starting_integrity": 5,
    "supernatural_power_stat": "lair",
    "starting_power_stat": 1,
    "resource_pool": "satiety",
    "power_systems": BEAST_NIGHTMARES + ALL_BEAST_ATAVISMS,
    "family_atavisms": BEAST_ATAVISMS,
    "anchors": ["virtue", "vice"],
    "merit_categories": ["physical", "social", "mental", "supernatural", "fighting", "style", "beast"],
    "field_validations": {
        "family": {
            "valid_values": BEAST_FAMILIES
        },
        "hunger": {
            "valid_values": BEAST_HUNGERS
        },
        "horror": {
            "valid_values": BEAST_HORRORS
        }
    },
    "version": "2.0",
    "author": "Chronicles of Darkness",
    "game_line": "Beast: The Primordial",
    "notes": "Enhanced Beast template with Lair, Nightmares, Atavisms, and Satiety mechanics"
}

# Register the template
register_template(BEAST_TEMPLATE) 