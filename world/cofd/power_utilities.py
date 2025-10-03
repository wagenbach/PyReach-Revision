"""
Power management utilities for supernatural abilities.
Handles semantic power syntax and power validation.
"""

from world.cofd.templates.promethean import ALL_ALEMBICS, PROMETHEAN_BESTOWMENTS


def get_valid_semantic_powers(power_type):
    """
    Get list of valid powers for a semantic power type.
    
    Args:
        power_type (str): Type of power (key, ceremony, rite, ritual, contract, alembic, bestowment)
        
    Returns:
        list: List of valid power names for that type
    """
    valid_powers = {
        "key": ["beasts", "blood", "chance", "cold_wind", "deep_waters", "disease", "grave_dirt", "pyre_flame", "stillness"],
        "ceremony": [
            "dead_mans_camera", "death_watch", "diviners_jawbone", "lovers_telephone", "ishtars_perfume",
            "crow_girl_kiss", "gifts_of_persephone", "ghost_trap", "skeleton_key", "bestow_regalia", 
            "krewe_binding", "speaker_for_the_dead", "black_cats_crossing", "bloody_codex", "dumb_supper",
            "forge_anchor", "maggot_homonculus", "pass_on", "ghost_binding", "persephones_return"
        ],
        "rite": [
            "chain_rage", "messenger", "banish", "harness_the_cycle", "totemic_empowerment",
            "bottle_spirit", "infest_locus", "rite_of_the_shroud", "sacred_hunt", "hunting_ground", "moons_mad_love",
            "shackled_lightning", "sigrblot", "wellspring", "carrion_feast", "flay_auspice", "kindle_fury", 
            "rite_of_absolution", "shadowbind", "the_thorn_pursuit", "banshee_howl", "raiment_of_the_storm", 
            "shadowcall", "supplication", "between_worlds", "fetish", "shadow_bridge", "twilight_purge", 
            "hidden_path", "expel", "heal_old_wounds", "lupus_venandi", "devour", "forge_alliance", 
            "urfarahs_bane", "veil", "great_hunt", "shadow_distortion", "unleash_shadow"
        ],
        "ritual": [
            "ban_of_the_spiteful_bastard", "mantle_of_amorous_fire", "pangs_of_proserpina", 
            "pool_of_forbidden_truths", "rigor_mortis", "cheval", "mantle_of_the_beasts_breath", 
            "the_hydras_vitae", "shed_the_virulent_bowels", "curse_of_aphrodites_favor", 
            "curse_of_the_beloved_toy", "deflection_of_wooden_doom", "donning_the_beasts_flesh", 
            "mantle_of_the_glorious_dervish", "touch_of_the_morrigan", "blood_price", "willful_vitae", 
            "blood_blight", "feeding_the_crone", "bounty_of_the_storm", "gorgons_gaze", 
            "manananggals_working", "mantle_of_the_predator_goddess", "quicken_the_withered_womb", 
            "the_red_blossoms", "birthing_the_god", "denying_hades", "gwydions_curse", 
            "mantle_of_the_crone", "scapegoat", "apple_of_eden", "blandishment_of_sin", 
            "blood_scourge", "marian_apparition", "revelatory_shroud", "vitae_reliquary", 
            "apparition_of_the_host", "bloody_icon", "curse_of_babel", "liars_plague", 
            "the_walls_of_jericho", "aarons_rod", "baptism_of_damnation", "blessing_the_legion", 
            "the_guiding_star", "malediction_of_despair", "miracle_of_the_dead_sun", 
            "pledge_to_the_worthless_one", "the_rite_of_ascending_blood", "blandishment_of_sin_advanced", 
            "curse_of_isolation", "gift_of_lazarus", "great_prophecy", "stigmata", "trials_of_job", 
            "apocalypse", "the_judgment_fast", "orison_of_voices", "sins_of_the_ancestors", "transubstatiation"
        ],
        "alembic": ALL_ALEMBICS,
        "bestowment": [b.lower().replace(" ", "_") for b in PROMETHEAN_BESTOWMENTS]
    }
    
    return valid_powers.get(power_type, [])


def get_template_requirements(power_type):
    """
    Get template requirements for a power type.
    
    Args:
        power_type (str): Type of power
        
    Returns:
        list: List of templates that can use this power type
    """
    template_requirements = {
        "key": ["geist"],
        "ceremony": ["geist"],
        "rite": ["werewolf"],
        "ritual": ["vampire"],
        "contract": ["changeling"],
        "alembic": ["promethean"],
        "bestowment": ["promethean"]
    }
    
    return template_requirements.get(power_type, [])


def handle_semantic_power(character, power_type, power_name, value, caller):
    """
    Handle semantic power syntax like key=beasts, ceremony=pass_on, alembic=purification.
    
    Args:
        character: The character object
        power_type (str): Type of power (key, ceremony, rite, ritual, contract, alembic, bestowment)
        power_name (str): Name of the specific power
        value: The value to set (usually "known" or 1)
        caller: The caller object (for messages)
        
    Returns:
        tuple: (success, message)
    """
    character_template = character.db.stats.get("other", {}).get("template", "Mortal")
    
    # Get valid powers for this type
    valid_powers = get_valid_semantic_powers(power_type)
    
    # Validate power type
    if not valid_powers:
        return False, f"Invalid power type: {power_type}\nValid types: key, ceremony, rite, ritual, contract, alembic, bestowment"
    
    # Validate power name
    if power_name not in valid_powers:
        return False, f"Invalid {power_type}: {power_name}\nValid {power_type}s: {', '.join(valid_powers)}"
    
    # Check template compatibility
    required_templates = get_template_requirements(power_type)
    if required_templates and character_template.lower() not in required_templates:
        return False, f"{power_type.title()}s are only available to {', '.join(required_templates).title()} characters.\nYour template is: {character_template}"
    
    # Handle different power types
    if power_type == "key":
        # Keys go to geist stats for Sin-Eaters
        from world.cofd.templates.geist import initialize_geist_stats
        initialize_geist_stats(character)
        
        # Keys are known/unknown - semantic syntax means they have the key
        character.db.geist_stats["keys"][power_name.replace("_", " ")] = True
        return True, f"Set {character.name} to have the {power_name.replace('_', ' ').title()} key."
    else:
        # Ceremonies, rites, rituals, contracts, alembics, bestowments go to regular powers as known abilities (stored as 1)
        if "powers" not in character.db.stats:
            character.db.stats["powers"] = {}
        
        character.db.stats["powers"][power_name] = 1
        power_display_name = power_name.replace('_', ' ').title()
        return True, f"Set {character.name} to know {power_display_name} ({power_type})."

