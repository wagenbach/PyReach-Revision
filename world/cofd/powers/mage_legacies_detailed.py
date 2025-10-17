"""
Mage: The Awakening Legacies
Detailed legacy information for Chronicles of Darkness 2nd Edition.
Based on Mage: The Awakening 2nd Edition and supplements.
"""

# ============================================================================
# LEGACIES
# ============================================================================

ALL_LEGACIES = {
    "chronologue": {
        "name": "Chronologue",
        "description": "Rejectors of Free Will",
        "primary_arcanum": "Time",
        "conjunctional_arcanum": "Fate",
        "optional_arcanum": None,
        "path": "Acanthus",
        "order": "Silver Ladder",
        "book": "NH-NA p39"
    },
    "eleventh_question": {
        "name": "Eleventh Question",
        "description": "Investigators",
        "primary_arcanum": "Time",
        "conjunctional_arcanum": None,
        "optional_arcanum": "Matter",
        "path": "Moros",
        "order": "Guardians of the Veil, Mysterium",
        "book": "MtA 2e p200"
    },
    "engineers_of_the_system": {
        "name": "Engineers of the System",
        "description": "Societal manipulators",
        "primary_arcanum": "Space",
        "conjunctional_arcanum": None,
        "optional_arcanum": "Life",
        "path": "Thyrsus",
        "order": "Silver Ladder",
        "book": "TotP p157"
    },
    "house_of_ariadne": {
        "name": "House of Ariadne",
        "description": "Urban destiny weavers",
        "primary_arcanum": "Time",
        "conjunctional_arcanum": "Fate",
        "optional_arcanum": "Space, Fate",
        "path": "Acanthus",
        "order": "Guardians of the Veil, Silver Ladder",
        "book": "NH-NA p23 / TotP p152"
    },
    "illumined_path": {
        "name": "Illumined Path",
        "description": "Guides to enlightenment",
        "primary_arcanum": "Prime",
        "conjunctional_arcanum": None,
        "optional_arcanum": "Forces",
        "path": "Obrimos",
        "order": "Mysterium",
        "book": "NH-NA p116"
    },
    "intendants_of_the_building": {
        "name": "Intendants of the Building",
        "description": "Caretakers of a hyperdimensional residential complex",
        "primary_arcanum": "Prime",
        "conjunctional_arcanum": None,
        "optional_arcanum": "Space, Mind",
        "path": "Mastigos",
        "order": None,
        "book": "TotP p163"
    },
    "keepers_of_the_covenant": {
        "name": "Keepers of the Covenant",
        "description": "Intermediaries between the material and the Shadow",
        "primary_arcanum": "Fate",
        "conjunctional_arcanum": "Spirit",
        "optional_arcanum": None,
        "path": "Thyrsus",
        "order": "Mysterium",
        "book": "DE2 p299"
    },
    "kitchen_alchemists": {
        "name": "Kitchen Alchemists",
        "description": "Alchemists of cooking",
        "primary_arcanum": "Fate",
        "conjunctional_arcanum": "Matter",
        "optional_arcanum": "Matter",
        "path": "Moros",
        "order": None,
        "book": "DE2 p372"
    },
    "logophages": {
        "name": "Logophages",
        "description": "Consumers of secrets",
        "primary_arcanum": "Prime",
        "conjunctional_arcanum": "Mind",
        "optional_arcanum": None,
        "path": "Mastigos",
        "order": "Guardians of the Veil, Mysterium",
        "book": "NH-NA p61"
    },
    "nagaraja": {
        "name": "Nagaraja",
        "description": "Transcendent revelers (*or Mantra Sadhaki)",
        "primary_arcanum": "Death",
        "conjunctional_arcanum": None,
        "optional_arcanum": "Mind",
        "path": "Mastigos",
        "order": None,
        "book": "DE p99"
    },
    "nighthawks": {
        "name": "Nighthawks",
        "description": "Thieves of magical treasures and items",
        "primary_arcanum": "Prime",
        "conjunctional_arcanum": "Matter",
        "optional_arcanum": "Death",
        "path": "Moros",
        "order": "Mysterium",
        "book": "NH-NA p29"
    },
    "perfected_adepts": {
        "name": "Perfected Adepts",
        "description": "Ascetics focused on unification of mind, body, and soul",
        "primary_arcanum": "Life",
        "conjunctional_arcanum": "Prime",
        "optional_arcanum": "Forces",
        "path": "Obrimos",
        "order": "Adamantine Arrow",
        "book": "NH-NA p26 / TotP p159"
    },
    "reality_stalkers": {
        "name": "Reality Stalkers",
        "description": "Seekers of secret places",
        "primary_arcanum": "Space",
        "conjunctional_arcanum": None,
        "optional_arcanum": "Death, Spirit",
        "path": "Mastigos",
        "order": "Mysterium",
        "book": "NH-NA p77"
    },
    "shapers_of_the_invisible": {
        "name": "Shapers of the Invisible",
        "description": "Seekers of perfection of Awakening",
        "primary_arcanum": "Spirit",
        "conjunctional_arcanum": None,
        "optional_arcanum": "Forces",
        "path": "Obrimos",
        "order": None,
        "book": "NH-NA p47"
    },
    "stone_scribes": {
        "name": "Stone Scribes",
        "description": "Recorders and psychopomps",
        "primary_arcanum": "Time",
        "conjunctional_arcanum": "Death",
        "optional_arcanum": None,
        "path": "Moros",
        "order": "Mysterium",
        "book": "NH-NA p81"
    },
    "tyrian_archons": {
        "name": "Tyrian Archons",
        "description": "Rulers by Divine Mandate",
        "primary_arcanum": "Prime",
        "conjunctional_arcanum": None,
        "optional_arcanum": None,
        "path": "Obrimos",
        "order": "Silver Ladder",
        "book": "NH-NA p35"
    },
    
    # Tremere Houses
    "house_nagaraja": {
        "name": "House Nagaraja",
        "description": "Ascetic destroyers of attachment (Tremere)",
        "primary_arcanum": "Death",
        "conjunctional_arcanum": None,
        "optional_arcanum": "Mind",
        "path": None,
        "order": "Tremere",
        "book": "NH-NA p138"
    },
    "house_seo_hel": {
        "name": "House Seo Hel",
        "description": "Norse bringers of rot (Tremere)",
        "primary_arcanum": "Matter",
        "conjunctional_arcanum": None,
        "optional_arcanum": "Death",
        "path": None,
        "order": "Tremere",
        "book": "NH-NA p140"
    },
    "house_thrax": {
        "name": "House Thrax",
        "description": "Militaristic conquerors (Tremere)",
        "primary_arcanum": "Life",
        "conjunctional_arcanum": None,
        "optional_arcanum": "Death",
        "path": None,
        "order": "Tremere",
        "book": "NH-NA p142"
    },
    "house_vedmak": {
        "name": "House Vedmak",
        "description": "Ghost and spirit hunters (Tremere)",
        "primary_arcanum": "Space",
        "conjunctional_arcanum": None,
        "optional_arcanum": "Death/Spirit",
        "path": None,
        "order": "Tremere",
        "book": "NH-NA p144"
    },
    
    # Abyssal Legacies
    "hand_of_destiny": {
        "name": "Hand of Destiny",
        "description": "Manipulative life coaches (Abyssal)",
        "primary_arcanum": "Mind",
        "conjunctional_arcanum": "Fate",
        "optional_arcanum": None,
        "path": None,
        "order": "Abyssal",
        "book": "NH-NA p119"
    },
    "keepers_of_the_chrysalis": {
        "name": "Keepers of the Chrysalis",
        "description": "Bringers of an alchemical Abyssal god (Abyssal)",
        "primary_arcanum": "Space",
        "conjunctional_arcanum": None,
        "optional_arcanum": "Matter, Mind",
        "path": None,
        "order": "Abyssal",
        "book": "NH-NA p112"
    },
    
    # Additional Legacies (mentioned but less detailed)
    "awakening_gambit": {
        "name": "Awakening Gambit",
        "description": "Encouragers of Awakenings",
        "primary_arcanum": "Mind",
        "conjunctional_arcanum": None,
        "optional_arcanum": None,
        "path": "Acanthus, Thyrsus",
        "order": None,
        "book": "SoS p134"
    },
    "bearers_of_the_eternal_voice": {
        "name": "Bearers of the Eternal Voice",
        "description": "Persuasive wordsmiths",
        "primary_arcanum": "Mind",
        "conjunctional_arcanum": None,
        "optional_arcanum": None,
        "path": "Mastigos",
        "order": "Mysterium",
        "book": "MTA 2e p202"
    },
    "bene_ashmedai": {
        "name": "Bene Ashmedai",
        "description": "Embracers of their vices",
        "primary_arcanum": "Spirit",
        "conjunctional_arcanum": None,
        "optional_arcanum": None,
        "path": "Mastigos",
        "order": "Guardians of the Veil, Mysterium",
        "book": "MTA 2e p202"
    },
    "blank_badge": {
        "name": "Blank Badge",
        "description": "Masters of collective anonymity",
        "primary_arcanum": "Mind",
        "conjunctional_arcanum": None,
        "optional_arcanum": None,
        "path": "Acanthus, Guardians of the Veil",
        "order": None,
        "book": "MTA 2e p202"
    },
    "bokor": {
        "name": "Bokor",
        "description": "Reanimators of corpses",
        "primary_arcanum": "Death",
        "conjunctional_arcanum": None,
        "optional_arcanum": None,
        "path": "Moros",
        "order": None,
        "book": "MTA 2e p203"
    },
    "brotherhood_of_the_demon_wind": {
        "name": "Brotherhood of the Demon Wind",
        "description": "Master swordsmen",
        "primary_arcanum": "Time",
        "conjunctional_arcanum": None,
        "optional_arcanum": "Space",
        "path": "Mastigos, Obrimos",
        "order": None,
        "book": "MTA 2e p202"
    },
    "carnival_melancholy": {
        "name": "Carnival Melancholy",
        "description": "Harvesters of souls for luck",
        "primary_arcanum": "Death",
        "conjunctional_arcanum": None,
        "optional_arcanum": None,
        "path": "Acanthus, Mysterium",
        "order": None,
        "book": "MTA 2e p202"
    },
    "chrysalides": {
        "name": "Chrysalides",
        "description": "Embracers of the ideal self",
        "primary_arcanum": "Life",
        "conjunctional_arcanum": None,
        "optional_arcanum": None,
        "path": "Thyrsus",
        "order": "Mysterium",
        "book": "MTA 2e p203"
    },
    "clavicularius": {
        "name": "Clavicularius",
        "description": "Masters of their vices",
        "primary_arcanum": "Spirit",
        "conjunctional_arcanum": None,
        "optional_arcanum": None,
        "path": "Mastigos",
        "order": "Guardians of the Veil, Mysterium",
        "book": "MTA 2e p202"
    },
    "cryptologos": {
        "name": "Cryptologos",
        "description": "Researchers of language and High Speech",
        "primary_arcanum": "Prime",
        "conjunctional_arcanum": None,
        "optional_arcanum": None,
        "path": "Mastigos, Guardians of the Veil, Mysterium, Silver Ladder",
        "order": None,
        "book": "MTA 2e p202"
    },
    "daksha": {
        "name": "Daksha",
        "description": "Seekers of evolutionary perfection",
        "primary_arcanum": "Life",
        "conjunctional_arcanum": None,
        "optional_arcanum": None,
        "path": "Obrimos, Adamantine Arrow",
        "order": None,
        "book": "MTA 2e p203"
    },
    "dreamspeakers": {
        "name": "Dreamspeakers",
        "description": "Explorers of the Anima Mundi",
        "primary_arcanum": "Mind",
        "conjunctional_arcanum": None,
        "optional_arcanum": None,
        "path": "Thyrsus, Adamantine Arrow",
        "order": None,
        "book": "MTA 2e p203"
    },
    "echo_walkers": {
        "name": "Echo Walkers",
        "description": "Soul-damaging seekers of perfection",
        "primary_arcanum": "Life",
        "conjunctional_arcanum": None,
        "optional_arcanum": None,
        "path": "Obrimos",
        "order": None,
        "book": "MTA 2e p203"
    },
    "forge_masters": {
        "name": "Forge Masters",
        "description": "Crafters of magical items",
        "primary_arcanum": "Prime",
        "conjunctional_arcanum": None,
        "optional_arcanum": None,
        "path": "Moros",
        "order": None,
        "book": "MTA 2e p203"
    },
    "orphans_of_proteus": {
        "name": "Orphans of Proteus",
        "description": "Master shapeshifters",
        "primary_arcanum": "Life",
        "conjunctional_arcanum": None,
        "optional_arcanum": None,
        "path": "Thyrsus",
        "order": None,
        "book": "MTA 2e p203"
    },
    "parliament_of_the_needle": {
        "name": "Parliament of the Needle",
        "description": "Communal Oneiros-mergers",
        "primary_arcanum": "Mind",
        "conjunctional_arcanum": None,
        "optional_arcanum": None,
        "path": "Mastigos, Mysterium",
        "order": None,
        "book": "TotP p35"
    },
    "pygmalion_society": {
        "name": "Pygmalion Society",
        "description": "Artists and sponsors of art",
        "primary_arcanum": "Mind",
        "conjunctional_arcanum": None,
        "optional_arcanum": None,
        "path": "Acanthus",
        "order": None,
        "book": "MTA 2e p202"
    },
    "sisterhood_of_the_blessed": {
        "name": "Sisterhood of the Blessed",
        "description": "Subtle political manipulators",
        "primary_arcanum": "Fate",
        "conjunctional_arcanum": None,
        "optional_arcanum": None,
        "path": "Acanthus, Mysterium",
        "order": None,
        "book": "MTA 2e p202"
    },
    "tamers_of_blood": {
        "name": "Tamers of Blood",
        "description": "Masters of sympathy and blood",
        "primary_arcanum": "Space",
        "conjunctional_arcanum": None,
        "optional_arcanum": None,
        "path": "Thyrsus",
        "order": None,
        "book": "MTA 2e p203"
    },
    "tamers_of_fire": {
        "name": "Tamers of Fire",
        "description": "Masters and embodiments of fire",
        "primary_arcanum": "Mind",
        "conjunctional_arcanum": None,
        "optional_arcanum": None,
        "path": "Obrimos",
        "order": None,
        "book": "MTA 2e p203"
    },
    "thrice_great": {
        "name": "Thrice-Great",
        "description": "Hermetic binders of planetary spirits",
        "primary_arcanum": "Spirit",
        "conjunctional_arcanum": None,
        "optional_arcanum": None,
        "path": "Obrimos, Mysterium",
        "order": None,
        "book": "MTA 2e p203"
    },
    "transhuman_engineers": {
        "name": "Transhuman Engineers",
        "description": "Seekers of technological singularity",
        "primary_arcanum": "Matter",
        "conjunctional_arcanum": None,
        "optional_arcanum": "Forces",
        "path": "Obrimos, Free Council",
        "order": None,
        "book": "MTA 2e p203"
    },
    "uncrowned_kings": {
        "name": "Uncrowned Kings",
        "description": "Alchemists of the self",
        "primary_arcanum": "Mind",
        "conjunctional_arcanum": None,
        "optional_arcanum": None,
        "path": "Moros",
        "order": None,
        "book": "MTA 2e p202"
    },
    "votaries_of_the_ordained": {
        "name": "Votaries of the Ordained",
        "description": "Guardians of artifacts and people of interest",
        "primary_arcanum": "Fate",
        "conjunctional_arcanum": None,
        "optional_arcanum": None,
        "path": "Moros, Guardians of the Veil",
        "order": None,
        "book": "MTA 2e p203"
    },
    "walkers_in_mists": {
        "name": "Walkers in Mists",
        "description": "Travelers and seers",
        "primary_arcanum": "Space",
        "conjunctional_arcanum": None,
        "optional_arcanum": None,
        "path": "Acanthus, Guardians of the Veil",
        "order": None,
        "book": "MTA 2e p202 / SoS p111"
    },
    "legion": {
        "name": "(Legion)",
        "description": "Soul-stealing identity thieves",
        "primary_arcanum": "Death",
        "conjunctional_arcanum": None,
        "optional_arcanum": None,
        "path": "Mastigos, Mysterium",
        "order": None,
        "book": "MTA 2e p202"
    },
}

# ============================================================================
# HELPER FUNCTIONS
# ============================================================================

def get_legacy(legacy_name):
    """Get a specific legacy by name."""
    legacy_key = legacy_name.lower().replace(" ", "_").replace("(", "").replace(")", "").replace("-", "_")
    return ALL_LEGACIES.get(legacy_key)

def get_all_legacies():
    """Get all legacy data."""
    return ALL_LEGACIES.copy()

def get_legacies_by_path(path_name):
    """Get all legacies associated with a specific path."""
    path_key = path_name.lower().capitalize()
    matching = {}
    
    for legacy_key, legacy_data in ALL_LEGACIES.items():
        if legacy_data.get('path') and path_key in str(legacy_data['path']):
            matching[legacy_key] = legacy_data
    
    return matching

def get_legacies_by_order(order_name):
    """Get all legacies associated with a specific order."""
    order_key = order_name.lower().replace("_", " ").title()
    matching = {}
    
    for legacy_key, legacy_data in ALL_LEGACIES.items():
        if legacy_data.get('order') and order_key in str(legacy_data['order']):
            matching[legacy_key] = legacy_data
    
    return matching

def get_legacies_by_arcanum(arcanum_name):
    """Get all legacies with a specific primary arcanum."""
    arcanum_key = arcanum_name.lower().capitalize()
    matching = {}
    
    for legacy_key, legacy_data in ALL_LEGACIES.items():
        if legacy_data.get('primary_arcanum') and arcanum_key == legacy_data['primary_arcanum']:
            matching[legacy_key] = legacy_data
    
    return matching

