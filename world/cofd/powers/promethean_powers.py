"""
Promethean: The Created - Power Data
Transmutations, Alembics, and Bestowments for Prometheans.
This file contains all the detailed information about Promethean powers.
"""

# Valid promethean lineages
PROMETHEAN_LINEAGES = [
    "frankenstein", "galatea", "osiris", "tammuz", "ulgan", "extempore", "unfleshed", "zeka",
    "amirani", "faceless", "hollow", "xibalbans"
]

PROMETHEAN_BESTOWMENTS = [
    "Spare Parts", "Titan's Strength", "Symbiotic Muse", "Unearthly Mien", "Corpse Tongue", "Revivification",
    "Heart of Clay", "Inscription", "Ephemeral Flesh", "Twilight Fluidity", "Heart of Steel",
    "Soul is in the Software", "Big Brother", "The Void", "Half-Life", "Crucible of Anguish",
    "Chem-Shell", "Living Wall", "Bloody Feast", "Vice Eater", "Blood Offering"
]

# Valid promethean refinements
PROMETHEAN_REFINEMENTS = [
    "aurum", "cuprum", "ferrum", "plumbum", "stannum", "aes", "argentum", "cobalus", "mercurius", "phosphorum"
]

# Transmutations (categories) - these are not purchased with dots
PROMETHEAN_TRANSMUTATIONS = [
    "alchemicus", "benefice", "contamination", "corporeum", "deception",
    "disquietism", "electrification", "flux", "luciferus", "metamorphosis",
    "mesmerism", "saturninus", "sensorium", "spiritus", "vitality", "vulcanus"
]

# Individual Alembics by Transmutation - these are purchased individually (like Changeling contracts)
PROMETHEAN_ALEMBICS = {
    "alchemicus": [
        # Stone Distillation
        "stone", "purification", "fortification", "transformation",
        # Aqua Regia Distillation
        "aqua_regia", "decay", "degradation", "dissolution",
        # Spagyria Distillation
        "spagyria", "temperature_modification", "alteration", "resize",
        # Elixir Distillation
        "elixir", "apprentices_brooms", "spark_of_life", "flesh_to_stone"
    ],
    "benefice": [
        # Command Distillation
        "command", "many_hands_make_light_work", "able_worker", "the_community_of_power",
        # Consortium Distillation
        "consortium", "the_fortified_compact", "common_perception", "unspoken_words",
        # Control Distillation
        "control", "protective_boon", "inviolable_unity", "bulwark",
        # Community Distillation
        "community", "communal_font", "we_are_as_one", "whats_mine_is_yours"
    ],
    "contamination": [
        # Indulgence Distillation
        "indulgence", "encourage_impulse", "remove_inhibitions", "plague_of_desire",
        # Leverage Distillation
        "leverage", "confession", "guilt_trip", "scandal",
        # Madness Distillation
        "madness", "psychotic_flash", "onset_of_madness", "catharsis",
        # Suffering Distillation
        "suffering", "purge", "affliction", "pain"
    ],
    "corporeum": [
        # Charites Distillation
        "charites", "athletic_grace", "uncanny_dexterity", "rarified_grace",
        # Zephyrus Distillation
        "zephyrus", "swift_feet", "serpent_strike", "perfected_reflexes",
        # Hygeius Distillation
        "hygeius", "human_flesh", "impossible_flesh", "resilient_flesh",
        # Motus Distillation
        "motus", "uncanny_athleticism", "mighty_bound", "exemplary_athleticism"
    ],
    "deception": [
        # Anonymity Distillation
        "anonymity", "nameless", "traceless", "forgotten",
        # Assimilation Distillation
        "assimilation", "conformity", "tongues", "hive_mind",
        # Doppelganger Distillation
        "doppelganger", "incriminate", "impersonate", "deep_cover",
        # Stalker Distillation
        "stalker", "shadow", "lurker", "phantom"
    ],
    "disquietism": [
        # Externalize Distillation
        "externalize", "safe_sojourn", "maelstrom", "assault",
        # Internalize Distillation
        "internalize", "temper", "soothe", "quell",
        # Redirect Distillation
        "redirect", "scapegoat", "rabid_rage", "iagos_whisper",
        # Weaponize Distillation
        "weaponize", "tension", "vanquish", "rampage"
    ],
    "electrification": [
        # Machinus Distillation
        "machinus", "jolt", "generator", "ghost_in_the_machine",
        # Arc Distillation
        "arc", "spark", "shock", "divine_lightning",
        # Oscillitus Distillation
        "oscillitus", "insulation", "blackout", "azothic_detonation",
        # Imperatus Distillation
        "imperatus", "lightning_therapy", "remote_absorption", "power_sink"
    ],
    "flux": [
        # Blight Distillation
        "blight", "invoke_disquiet", "aggravate_wasteland", "summon_firestorm",
        # Cannibalize Distillation
        "cannibalize", "aptitude", "acumen", "endowment",
        # Lordship Distillation
        "lordship",
        # Mutation Distillation
        "mutation", "dread_power",
        # Solvent Distillation
        "solvent", "disruption", "disaster", "detonation",
        # Unleash Distillation
        "unleash", "invigorate", "infuse", "azothic_mantle"
    ],
    "luciferus": [
        # Solar Flare Distillation
        "solar_flare", "dazzling_corona", "searing_corona", "volatile_corona",
        # Morning Star Distillation
        "morning_star", "ignus_fatuus", "beckon", "ringleader",
        # Blaze of Glory Distillation
        "blaze_of_glory", "outshining_the_sun", "roman_candle", "all_or_nothing",
        # Beacon of Helios Distillation
        "beacon_of_helios", "daybreak", "guidepost", "lighthouse_for_the_dead"
    ],
    "metamorphosis": [
        # Aptare Distillation
        "aptare", "blessing_of_tethys", "scuttling_spider", "procrustean_shape",
        # Bestiae Facies Distillation
        "bestiae_facies", "natural_weaponry", "form_of_the_barghest", "chimera",
        # Tegere Distillation
        "tegere", "impermeable_shell", "retributive_protection", "quill_assault",
        # Verto Distillation
        "verto", "medusas_visage", "everyman", "body_like_clay"
    ],
    "mesmerism": [
        # Phobos Distillation
        "phobos", "rattle", "terrify", "swoon",
        # Eros Distillation
        "eros", "lure", "seduce", "inflame",
        # Eris Distillation
        "eris", "misdirect", "baffle", "fog",
        # Penthos Distillation
        "penthos", "undermine", "defeat", "depress"
    ],
    "saturninus": [
        # Heed the Call Distillation
        "heed_the_call", "inscribed_in_flame", "controlled_burn", "sublimation_by_fire",
        # Plumb the Fathoms Distillation
        "plumb_the_fathoms", "pilgrims_landmarks", "wisdom_of_ages", "glimpsing_the_crasis",
        # Stoke the Furnace Distillation
        "stoke_the_furnace", "catalytic_affirmation", "chasing_hope", "transhuman_adaptation",
        # Prime the Vessel Distillation
        "prime_the_vessel", "shielding_pod", "humour_electrolysis", "pyros_branding"
    ],
    "sensorium": [
        # Vitreous Humour Distillation
        "vitreous_humour", "fire_sight", "piercing_sight", "ephemeral_sight",
        # Receptive Humour Distillation
        "receptive_humour", "translators_memory", "rarified_senses", "circle_of_perception",
        # Stereo Humour Distillation
        "stereo_humour", "aura_sight", "hearing_the_inner_voice", "clairvoyance",
        # Somatic Humour Distillation
        "somatic_humour", "bloodhounds_nose", "discriminating_tongue", "sensitive_ears"
    ],
    "spiritus": [
        # Clades Distillation
        "clades", "strike_the_heart", "biting_aura", "burning_strike",
        # Clupeum Distillation
        "clupeum", "personal_shield", "interposing_shield", "mystic_fortress",
        # Veritas Distillation
        "veritas", "finding_the_wellspring", "walking_the_path_of_memory", "disrupting_the_vital_humours",
        # Laruae Distillation
        "laruae", "plumb_azothic_memory", "one_of_the_tribe", "pyros_decoy"
    ],
    "vitality": [
        # Unbowed Distillation
        "unbowed", "resolution_of_steel", "crucible_of_will", "roar_of_the_defiant",
        # Unbroken Distillation
        "unbroken", "armor_of_will", "drive_on", "rebuke_the_shroud",
        # Unconquered Distillation
        "unconquered", "cyclopean_might", "titans_throw", "wrath_of_the_gods",
        # Unfettered Distillation
        "unfettered", "close_combat_defense", "shattered_chains", "no_walls_may_hold_me"
    ],
    "vulcanus": [
        # Cauterio Distillation
        "cauterio", "alter_firetouched", "animate_firetouched", "evolve_firetouched",
        # Ignus Aspiratus Distillation
        "ignus_aspiratus", "direct_fire", "fire_grasp", "divine_guidance",
        # Mutatus Aspiratus Distillation
        "mutatus_aspiratus", "contain_flux", "drawing_flux", "expel_pyros",
        # Sanctus Aspiratus Distillation
        "sanctus_aspiratus", "refine_pyros", "steal_pyros", "drain_pyros",
        # The Tsar's Gift Distillation (Zeka-specific)
        "the_tsars_gift", "the_first_stone", "the_hand_that_feeds", "sevenfold"
    ]
}

# Flatten all alembics for validation
ALL_ALEMBICS = [alembic for alembics in PROMETHEAN_ALEMBICS.values() for alembic in alembics]

# Valid promethean distillations (roles in the Pilgrimage)
PROMETHEAN_DISTILLATIONS = [
    "alpha", "beta", "gamma", "delta", "epsilon"
]

# ==================== DETAILED ALEMBIC DATA ====================
# Import detailed alembic information from separate file
try:
    from .promethean_alembics_detailed import ALL_ALEMBICS_DETAILED, get_alembic_info
    ALEMBICS_DETAILED = ALL_ALEMBICS_DETAILED
except ImportError:
    # Fallback if detailed file not found
    ALEMBICS_DETAILED = {}
    def get_alembic_info(alembic_name):
        return None

def get_alembic_details(alembic_name):
    """
    Get detailed information about a specific alembic.
    
    Args:
        alembic_name (str): The alembic key name
        
    Returns:
        dict or None: Detailed alembic data if available
    """
    return get_alembic_info(alembic_name)

def get_alembics_by_transmutation(transmutation_name):
    """
    Get all alembics for a specific transmutation.
    
    Args:
        transmutation_name (str): The transmutation name
        
    Returns:
        list: List of alembic names for that transmutation
    """
    return PROMETHEAN_ALEMBICS.get(transmutation_name.lower(), [])

def get_transmutation_for_alembic(alembic_name):
    """
    Find which transmutation an alembic belongs to.
    
    Args:
        alembic_name (str): The alembic name
        
    Returns:
        str or None: Transmutation name if found
    """
    alembic_lower = alembic_name.lower().replace(" ", "_")
    for trans_name, alembics in PROMETHEAN_ALEMBICS.items():
        if alembic_lower in alembics:
            return trans_name
    return None

