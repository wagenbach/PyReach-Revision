"""
Geist: The Sin-Eaters Template Definition for Chronicles of Darkness.
Sin-Eaters are those who have died and returned, bound to powerful ghosts called geists.
"""

from . import register_template

# Valid geist archetypes
GEIST_ARCHETYPES = [
    "mourner", "celebrant", "gatekeeper", "necromancer", "reaper"
]

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

# Geist template definition
GEIST_TEMPLATE = {
    "name": "geist",
    "display_name": "Geist",
    "description": "Sin-Eaters are those who have died and returned to life, bound to powerful ghosts called geists who saved them from true death.",
    "bio_fields": ["root", "bloom", "archetype", "threshold", "krewe", "burden", "geist_name"],
    "integrity_name": "Synergy",
    "starting_integrity": 7,
    "supernatural_power_stat": "psyche",
    "starting_power_stat": 1,
    "resource_pool": "plasm",
    "power_systems": GEIST_HAUNTS + GEIST_KEYS + GEIST_CEREMONIES,
    "anchors": ["root", "bloom"],
    "merit_categories": ["physical", "social", "mental", "supernatural", "fighting", "style", "geist"],
    "field_validations": {
        "archetype": {
            "valid_values": GEIST_ARCHETYPES
        },
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