"""
Mage: The Awakening Paths
Detailed path information for Chronicles of Darkness 2nd Edition.
Based on Mage: The Awakening 2nd Edition.
"""

ALL_PATHS = {
    "acanthus": {
        "name": "Acanthus",
        "nickname": "Enchanters/Witches",
        "ruling_arcana": ["Time", "Fate"],
        "inferior_arcanum": "Forces",
        "materials": "Glass, crystal, silver, reflective materials",
        "path_tools": "Rapier, bow, precision weapons",
        "description": "The Enchanters walk the Watchtower of the Lunargent Thorn in the Realm of Arcadia, mastering Time and Fate to weave destiny",
        "book": "MtAw2 p20, p121"
    },
    "mastigos": {
        "name": "Mastigos",
        "nickname": "Warlocks/Psychonaut",
        "ruling_arcana": ["Space", "Mind"],
        "inferior_arcanum": "Matter",
        "materials": "Iron, brass, leather, worked materials",
        "path_tools": "Curved sword, whip, cruel weapons",
        "description": "The Warlocks walk the Watchtower of the Iron Gauntlet in the Realm of Pandemonium, commanding Space and Mind to reshape consciousness and reality",
        "book": "MtAw2 p23, p121"
    },
    "moros": {
        "name": "Moros",
        "nickname": "Alchemist/Necromancers",
        "ruling_arcana": ["Matter", "Death"],
        "inferior_arcanum": "Spirit",
        "materials": "Lead, bone, gems, buried materials",
        "path_tools": "Hammer, mace, crushing weapons",
        "description": "The Necromancers walk the Watchtower of the Lead Coin in the Realm of Stygia, wielding Matter and Death to command the grave",
        "book": "MtAw2 p26, p121"
    },
    "obrimos": {
        "name": "Obrimos",
        "nickname": "Thaumaturges/Theurgists",
        "ruling_arcana": ["Forces", "Prime"],
        "inferior_arcanum": "Death",
        "materials": "Steel, petrified wood, gold, perfected materials",
        "path_tools": "Double-edged sword, spear, noble weapons",
        "description": "The Theurgists walk the Watchtower of the Golden Key in the Realm of Aether, channeling Forces and Prime as divine power",
        "book": "MtAw2 p29, p121"
    },
    "thyrsus": {
        "name": "Thyrsus",
        "nickname": "Shamans/Ecstatic",
        "ruling_arcana": ["Life", "Spirit"],
        "inferior_arcanum": "Mind",
        "materials": "Wood, copper, stone, natural materials",
        "path_tools": "Axe, sling, hunting weapons",
        "description": "The Shamans walk the Watchtower of the Stone Book in the Realm of the Primal Wild, mastering Life and Spirit to commune with nature",
        "book": "MtAw2 p32, p121"
    },
}

# ============================================================================
# HELPER FUNCTIONS
# ============================================================================

def get_path(path_name):
    """Get a specific path by name."""
    path_key = path_name.lower().replace(" ", "_")
    return ALL_PATHS.get(path_key)

def get_all_paths():
    """Get all path data."""
    return ALL_PATHS.copy()

