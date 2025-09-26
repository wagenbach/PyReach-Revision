"""
Vampire Template Definition for Chronicles of Darkness.
Vampire: The Requiem template with Clan and Covenant validations.
"""

from . import register_template

# Valid clans for Vampire characters
VAMPIRE_CLANS = [
    "daeva", "gangrel", "mekhet", "nosferatu", "ventrue"
]

# Valid covenants for Vampire characters
VAMPIRE_COVENANTS = [
    "carthian movement", "circle of the crone", "invictus", 
    "lancea et sanctum", "ordo dracul", "unaligned"
]

# Valid vampire disciplines and blood sorcery powers
VAMPIRE_DISCIPLINES = [
    # Disciplines (categories)
    "animalism", "auspex", "bloodworking", "cachexy", "celerity", "coils_of_the_dragon", 
    "dominate", "majesty", "nightmare", "obfuscate", "praestantia", "protean", 
    "resilience", "vigor", "crochan", "dead_signal", "chary", "vitiate",
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

# Vampire template definition
VAMPIRE_TEMPLATE = {
    "name": "vampire",
    "display_name": "Vampire",
    "description": ("Vampires are the undead, cursed beings that feed on the blood of mortals. "
                   "They are organized into Clans based on their vampiric lineage and Covenants "
                   "based on their political and religious beliefs."),
    "bio_fields": ["mask", "dirge", "clan", "covenant", "sire", "embrace_date"],
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