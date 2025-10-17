"""
Vampire Template Definition for Chronicles of Darkness.
Vampire: The Requiem template with Clan and Covenant validations.
"""

from . import register_template

# Valid clans for Vampire characters
VAMPIRE_CLANS = [
    # Major Clans
    "daeva", "gangrel", "mekhet", "nosferatu", "ventrue",
    # Uncommon and Lost Clans
    "akhud", "amari", "bekaak", "dukhan", "hypatians", "jiang_shi", "julii",
    "mekhet_hollow", "mikhaili", "nhang", "pijavica", "twice_cursed"
]

# Valid bloodlines for Vampire characters
VAMPIRE_BLOODLINES = [
    # Cross-Clan Bloodlines
    "neglatu", "parliamentarians", "penumbrae", "scions_of_the_first_city",
    # Daeva Bloodlines
    "jharana", "liderc", "vilseduire",
    # Gangrel Bloodlines
    "kerberos", "nosoi",
    # Mekhet Bloodlines
    "ankou", "icelus", "khaibit", "morbus",
    # Ventrue Bloodlines
    "bron", "vardyvle"
]

# Valid covenants for Vampire characters
VAMPIRE_COVENANTS = [
    # Major Covenants
    "carthian_movement", "circle_of_the_crone", "invictus", 
    "lancea_et_sanctum", "ordo_dracul", "belials_brood", "vii", "unaligned",
    # Regional Covenants
    "esoteric_order_of_the_golden_star", "17n", "alecto", "kataraomenon", "ypochtreosi",
    "bureau_of_childer", "bureau_of_silence", "dragons_path", "way_of_the_dragon",
    "revolutionary_council", "watchful_eyes",
    "hototogisu", "maeda_group", "takahashi_family", "ume_house",
    # Historical Covenants
    "camarilla", "childrens_crusade", "gallows_post", "legion_of_the_dead", "tenth_choir",
    "ahl_al_mumit", "al_amin", "firawn", "jaliniyya",
    "circles_of_mor", "legion_of_the_green", "weihan_cynn"
]

# Primary powers (rated 1-5 dots) - Disciplines
VAMPIRE_PRIMARY_POWERS = [
    "animalism", "auspex", "bloodworking", "cachexy", "celerity", 
    "dominate", "majesty", "nightmare", "obfuscate", "praestantia", "protean", 
    "resilience", "vigor", "crochan", "dead_signal", "chary", "vitiate", "cruac", "theban_sorcery"
]

# Secondary powers (individual abilities) - Rituals, Miracles, Coils
VAMPIRE_SECONDARY_POWERS = [
    # Cruac Rituals (individual rituals by level)
    # Level 1 Cruac
    "ban_of_the_spiteful_bastard", "mantle_of_amorous_fire", "pangs_of_proserpina", 
    "pool_of_forbidden_truths", "rigor_mortis",
    # Level 2 Cruac  
    "cheval", "mantle_of_the_beasts_breath", "the_hydras_vitae", "shed_the_virulent_bowels",
    # Level 3 Cruac
    "curse_of_aphrodites_favor", "curse_of_the_beloved_toy", "deflection_of_wooden_doom", 
    "donning_the_beasts_flesh", "mantle_of_the_glorious_dervish", "touch_of_the_morrigan",
    # Level 4 Cruac
    "blood_price", "willful_vitae", "blood_blight", "feeding_the_crone", "bounty_of_the_storm",
    "gorgons_gaze", "manananggals_working", "mantle_of_the_predator_goddess", "quicken_the_withered_womb",
    "the_red_blossoms",
    # Level 5 Cruac
    "birthing_the_god", "denying_hades", "gwydions_curse", "mantle_of_the_crone", "scapegoat",
    # Theban Sorcery Miracles (individual miracles by level)
    # Level 1 Theban
    "apple_of_eden", "blandishment_of_sin", "blood_scourge", "marian_apparition", 
    "revelatory_shroud", "vitae_reliquary",
    # Level 2 Theban
    "apparition_of_the_host", "bloody_icon", "curse_of_babel", "liars_plague", "the_walls_of_jericho",
    # Level 3 Theban
    "aarons_rod", "baptism_of_damnation", "blessing_the_legion", "the_guiding_star",
    "malediction_of_despair", "miracle_of_the_dead_sun", "pledge_to_the_worthless_one", "the_rite_of_ascending_blood",
    # Level 4 Theban
    "blandishment_of_sin_advanced", "curse_of_isolation", "gift_of_lazarus", "great_prophecy", 
    "stigmata", "trials_of_job",
    # Level 5 Theban
    "apocalypse", "the_judgment_fast", "orison_of_voices", "sins_of_the_ancestors", "transubstatiation",
    # Ordo Dracul Coils
    "coil_of_the_ascendant", "coil_of_the_wyrm", "coil_of_the_voivode",
    "coil_of_zirnitra", "coil_of_ziva"
]

# All vampire powers combined (for backwards compatibility and validation)
VAMPIRE_DISCIPLINES = VAMPIRE_PRIMARY_POWERS + VAMPIRE_SECONDARY_POWERS

# Vampire template definition
VAMPIRE_TEMPLATE = {
    "name": "vampire",
    "display_name": "Vampire",
    "description": ("Vampires are the undead, cursed beings that feed on the blood of mortals. "
                   "They are organized into Clans based on their vampiric lineage and Covenants "
                   "based on their political and religious beliefs."),
    "bio_fields": ["mask", "dirge", "clan", "bloodline", "covenant", "sire", "embrace_date"],
    "integrity_name": "Humanity",
    "starting_integrity": 7,
    "supernatural_power_stat": "blood_potency",
    "starting_power_stat": 1,
    "resource_pool": "blood",
    "power_systems": VAMPIRE_DISCIPLINES,
    "anchors": ["mask", "dirge"],
    "merit_categories": ["physical", "social", "mental", "supernatural", "fighting", "style", "vampire"],
    "field_validations": {
        "clan": {
            "valid_values": VAMPIRE_CLANS
        },
        "bloodline": {
            "valid_values": VAMPIRE_BLOODLINES
        },
        "covenant": {
            "valid_values": VAMPIRE_COVENANTS
        }
    },
    "version": "2.0",
    "author": "Chronicles of Darkness",
    "game_line": "Vampire: The Requiem",
    "notes": "Enhanced Vampire template with power stats, disciplines, and resource pools"
}

# Register the template
register_template(VAMPIRE_TEMPLATE)


# Power list helper functions
def get_primary_powers():
    """Get list of primary vampire powers (disciplines rated 1-5)."""
    return VAMPIRE_PRIMARY_POWERS.copy()


def get_secondary_powers():
    """Get list of secondary vampire powers (individual rituals, miracles, coils)."""
    return VAMPIRE_SECONDARY_POWERS.copy()


def get_all_powers():
    """Get all vampire powers for validation."""
    return VAMPIRE_DISCIPLINES.copy() 