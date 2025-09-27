from evennia.commands.default.muxcommand import MuxCommand
from evennia.utils import evtable
from world.cofd.stat_dictionary import (
    attribute_dictionary, skill_dictionary, 
    advantage_dictionary, anchor_dictionary
)

class CmdStat(MuxCommand):
    """
    Set and manage character statistics.
    
    Usage:
        +stat <stat>=<value> - Set a stat on yourself (if not approved)
        +stat <name>/<stat>=<value> - Set a stat on someone else (staff only)
        +stat/list [name] - List all stats for yourself or another
        +stat/remove <stat> - Remove a stat from yourself (if not approved)
        +stat/remove <name>/<stat> - Remove a stat from someone else (staff only)
        +stat/remove specialty/<skill> - Remove all specialties for a skill
        +stat/approve <name> - Lock a character's stats (staff only)
        +stat/unapprove <name> - Unlock a character's stats (staff only)
        +stat/reset <name>=<template> - Reset character to new template (staff only)
        +stat/geist <stat>=<value> - Set a geist stat (Sin-Eater characters only)
        
        The /reset switch completely wipes ALL character stats and reinitializes
        them for the new template. This is a nuclear option for fixing corrupted
        data. Use with caution as it cannot be undone!
        
    Valid stat categories:
        Attributes: strength, dexterity, stamina, presence, manipulation, 
                   composure, intelligence, wits, resolve
        Skills: All CoD skills (athletics, brawl, investigation, etc.)
        Specialties: specialty/[skill]=[specialty name] (requires dots in skill)
        Advantages: health, willpower, speed, defense, initiative
        Merits: All Chronicles of Darkness merits (see +xp/list merits)
        Powers: Template-specific supernatural abilities
                - Vampire: disciplines, cruac rituals, theban miracles (animalism, pangs_of_proserpina, etc.)
                - Mage: arcana (arcanum_death, fate, forces, etc.)
                - Werewolf: gifts & rites (gift_strength, change, sacred_hunt, etc.)
                - Changeling: individual contracts (hostile_takeover, cloak_of_night, etc.)
                Note: Powers that conflict with attribute/skill names use prefixes
        Bio: fullname, birthdate, concept, virtue, vice
        template Bio: path, order, mask, dirge, clan, covenant, bone, blood, 
                   auspice, tribe, seeming, court, kith, burden, archetype, 
                   krewe, lineage, refinement, profession, organization, 
                   creed, incarnation, agenda, agency, hunger, family, 
                   inheritance, origin, clade, divergence
        Other: integrity, size, beats, experience, template (staff only)
        
        Template-specific integrity names can also be used:
        humanity (vampire), wisdom (mage), pilgrimage (promethean), 
        clarity (changeling), cover (demon), harmony (werewolf), 
        synergy (geist), satiety (beast)
        
    Examples:
        +stat strength=3
        +stat fullname=John Smith
        +stat birthdate=March 15, 1985
        +stat concept=Detective
        +stat virtue=Justice
        +stat vice=Wrath
        +stat template=Vampire (staff only)
        +stat clan=Gangrel (vampire-specific)
        +stat path=Obrimos (mage-specific)
        
        Specialty Examples:
        +stat specialty/athletics=Running
        +stat specialty/investigation=Crime Scenes  
        +stat specialty/brawl=Dirty Fighting
        
        Merit Examples (during character generation):
        +stat contacts=3
        +stat fast_reflexes=2
        +stat resources=2
        +stat allies=1
        
        Power Examples:
        +stat animalism=3 (vampire discipline)
        +stat pangs_of_proserpina=1 (vampire cruac ritual - level 1)
        +stat blood_scourge=1 (vampire theban miracle - level 1)
        +stat coil_of_the_ascendant=1 (vampire ordo dracul coil)
        +stat arcanum_death=2 (mage arcanum - prefixed to avoid conflict)
        +stat forces=2 (mage arcanum - no conflict)
        +stat gift_strength=4 (werewolf gift - prefixed to avoid attribute conflict)
        +stat sacred_hunt=1 (werewolf rite - rank 2)
        +stat hostile_takeover=1 (changeling contract)
        
        Geist Examples (Sin-Eater secondary character sheet):
        +stat/geist concept=The Snow Queen
        +stat/geist remembrance_description=Crisp winter cold and wedding march music
        +stat/geist remembrance_trait=intimidation (must be skill or merit ≤3 dots)
        +stat/geist power=7 (geist attributes: power, finesse, resistance)
        +stat/geist finesse=3
        +stat/geist resistance=5
        +stat/geist virtue=empathetic
        +stat/geist vice=implacable
        +stat/geist crisis_trigger=betrayal
        +stat/geist ban=Fresh pine boughs
        +stat/geist bane=Yellow roses
        +stat/geist innate_key=cold wind
        +stat/geist boneyard=3 (haunts are rated 1-5)
        
        Semantic Power Setting (Individual Abilities):
        Keys (Geist): +stat key=beasts, +stat key=stillness, +stat key=cold_wind
        Ceremonies (Geist): +stat ceremony=pass_on, +stat ceremony=ghost_trap
        Rites (Werewolf): +stat rite=sacred_hunt, +stat rite=bottle_spirit
        Rituals (Vampire): +stat ritual=pangs_of_proserpina, +stat ritual=blood_scourge
        Contracts (Changeling): +stat contract=hostile_takeover, +stat contract=cloak_of_night

        Category Powers (1-5 dots):
        Haunts (Geist): +stat boneyard=3, +stat curse=2
        Disciplines (Vampire): +stat animalism=4, +stat auspex=2
        Arcana (Mage): +stat forces=3, +stat death=1
        Gifts (Werewolf): +stat strength=2, +stat dominance=3
        
        Note: Individual abilities use semantic syntax (known/unknown).
        Categories use regular numeric ratings (1-5 dots).
        
    Note: Merits can be set directly with +stat during character generation.
    Once approved, merits must be purchased using +xp/buy <merit>=[dots] command.
    Merits require prerequisite validation. Use +xp/list merits to see available merits.
    Players can only modify their own stats if they are not approved.
    Staff can modify any character's stats at any time.
    """
    
    key = "+stat"
    aliases = ["+stats"]
    help_category = "Character Sheets and Development"
    def parse(self):
        """Parse the command arguments."""
        super().parse()  # Initialize switches and other MuxCommand attributes
        
        args = self.args.strip()
        # Don't reset switches - they're already parsed by super().parse()
    
    def func(self):
        """Execute the command"""
        if not self.switches:
            # Check if setting or just viewing
            if "=" in self.args:
                self.set_stat()
            else:
                self.caller.msg("Usage: +stat <stat>=<value> or +stat/list")
            return
            
        switch = self.switches[0].lower()
        
        if switch == "list":
            self.list_stats()
        elif switch == "remove":
            self.remove_stat()
        elif switch == "approve":
            self.approve_character()
        elif switch == "unapprove":
            self.unapprove_character()
        elif switch == "reset":
            self.reset_template()
        elif switch == "geist":
            self.set_geist_stat()
        else:
            self.caller.msg("Invalid switch. See help for usage.")
    
    def _get_template_powers(self, template):
        """Get the list of available powers for a specific template (all powers for validation)."""
        if not template:
            return []
            
        template = template.lower()
        
        # Template-specific power mappings - ALL powers for stats validation
        template_power_map = {
            'vampire': [
                       # Disciplines (categories)
                       'animalism', 'auspex', 'bloodworking', 'cachexy', 'celerity', 'coils_of_the_dragon', 
                       'dominate', 'majesty', 'nightmare', 'obfuscate', 'praestantia', 'protean', 
                       'resilience', 'vigor', 'crochan', 'dead_signal', 'chary', 'vitiate',
                       # Cruac Rituals (individual rituals by level)
                       # Level 1 Cruac
                       'ban_of_the_spiteful_bastard', 'mantle_of_amorous_fire', 'pangs_of_proserpina', 
                       'pool_of_forbidden_truths', 'rigor_mortis',
                       # Level 2 Cruac  
                       'cheval', 'mantle_of_the_beasts_breath', 'the_hydras_vitae', 'shed_the_virulent_bowels',
                       # Level 3 Cruac
                       'curse_of_aphrodites_favor', 'curse_of_the_beloved_toy', 'deflection_of_wooden_doom', 
                       'donning_the_beasts_flesh', 'mantle_of_the_glorious_dervish', 'touch_of_the_morrigan',
                       # Level 4 Cruac
                       'blood_price', 'willful_vitae', 'blood_blight', 'feeding_the_crone', 'bounty_of_the_storm',
                       'gorgons_gaze', 'manananggals_working', 'mantle_of_the_predator_goddess', 'quicken_the_withered_womb',
                       'the_red_blossoms',
                       # Level 5 Cruac
                       'birthing_the_god', 'denying_hades', 'gwydions_curse', 'mantle_of_the_crone', 'scapegoat',
                       # Theban Sorcery Miracles (individual miracles by level)
                       # Level 1 Theban
                       'apple_of_eden', 'blandishment_of_sin', 'blood_scourge', 'marian_apparition', 
                       'revelatory_shroud', 'vitae_reliquary',
                       # Level 2 Theban
                       'apparition_of_the_host', 'bloody_icon', 'curse_of_babel', 'liars_plague', 'the_walls_of_jericho',
                       # Level 3 Theban
                       'aarons_rod', 'baptism_of_damnation', 'blessing_the_legion', 'the_guiding_star',
                       'malediction_of_despair', 'miracle_of_the_dead_sun', 'pledge_to_the_worthless_one', 'the_rite_of_ascending_blood',
                       # Level 4 Theban
                       'blandishment_of_sin_advanced', 'curse_of_isolation', 'gift_of_lazarus', 'great_prophecy', 
                       'stigmata', 'trials_of_job',
                       # Level 5 Theban
                       'apocalypse', 'the_judgment_fast', 'orison_of_voices', 'sins_of_the_ancestors', 'transubstatiation',
                       # Ordo Dracul Coils
                       'coil_of_the_ascendant', 'coil_of_the_wyrm', 'coil_of_the_voivode',
                       'coil_of_zirnitra', 'coil_of_ziva'
                       ],
            'legacy_vampire': [
                       # Legacy vampire disciplines (1st edition)
                       'animalism', 'auspex', 'celerity', 'dominate', 'majesty', 
                       'nightmare', 'obfuscate', 'protean', 'resilience', 'vigor',
                       'coils_of_the_dragon', 'cruac', 'theban_sorcery'
                       ],
            'mage': ['arcanum_death', 'fate', 'forces', 'life', 'matter', 'mind', 'prime', 'space', 'spirit', 'time'],
            'werewolf': [
                        # Gifts (categories)
                        'gift_death', 'dominance', 'elementals', 'insight', 'inspiration', 'knowledge',
                        'nature', 'rage', 'gift_strength', 'technology', 'weather', 'hunting', 'pack',
                        'crescent_moon', 'full_moon', 'new_moon', 'gibbous_moon', 'half_moon', 'agony', 'blood',
                        'disease', 'evasion', 'fervor', 'hunger', 'shaping', 'gift_stealth', 'warding', 'change',
                        # Wolf Rites (individual rites by level)
                        # Rank 1 Rites
                        'chain_rage', 'messenger', 'banish', 'harness_the_cycle', 'totemic_empowerment',
                        # Rank 2 Rites
                        'bottle_spirit', 'infest_locus', 'rite_of_the_shroud', 'sacred_hunt', 'hunting_ground', 'moons_mad_love',
                        'shackled_lightning', 'sigrblot', 'wellspring',
                        # Rank 3 Rites
                        'carrion_feast', 'flay_auspice', 'kindle_fury', 'rite_of_absolution', 'shadowbind', 'the_thorn_pursuit',
                        'banshee_howl', 'raiment_of_the_storm', 'shadowcall', 'supplication',
                        # Rank 4 Rites
                        'between_worlds', 'fetish', 'shadow_bridge', 'twilight_purge', 'hidden_path', 'expel', 'heal_old_wounds',
                        'lupus_venandi',
                        # Rank 5 Rites
                        'devour', 'forge_alliance', 'urfarahs_bane', 'veil', 'great_hunt', 'shadow_distortion', 'unleash_shadow'
                        ],
            'changeling': [
                          # all contracts use semantic syntax
                          # Crown Contracts
                          'hostile_takeover', 'mask_of_superiority', 'paralyzing_presence', 'summon_the_loyal_servant', 'tumult',
                          # Royal Crown Contracts
                          'discreet_summons', 'masterminds_gambit', 'pipes_of_the_beastcaller', 'the_royal_court', 'spinning_wheel',
                          # Jewels Contracts
                          'blessing_of_perfection', 'changing_fortunes', 'light_shy', 'murkblur', 'trivial_reworking',
                          # Royal Jewels Contracts
                          'changeling_hours', 'dance_of_the_toys', 'hidden_reality', 'stealing_the_solid_reflection', 'tatterdemalions_workshop',
                          # Mirror Contracts
                          'glimpse_of_a_distant_mirror', 'know_the_competition', 'portents_and_visions', 'read_lucidity', 'walls_have_ears',
                          # Royal Mirror Contracts
                          'props_and_scenery', 'reflections_of_the_past', 'riddle_kith', 'skinmask', 'unravel_the_tapestry',
                          # Shield Contracts
                          'cloak_of_night', 'fae_cunning', 'shared_burden', 'thorns_and_brambles', 'trapdoor_spiders_trick',
                          # Royal Shield Contracts
                          'fortifying_presence', 'hedgewall', 'pure_clarity', 'vow_of_no_compromise', 'whispers_of_morning',
                          # Steed Contracts
                          'boon_of_the_scuttling_spider', 'dreamsteps', 'nevertread', 'pathfinder', 'seven_league_leap',
                          # Royal Steed Contracts
                          'chrysalis', 'flickering_hours', 'leaping_toward_nightfall', 'mirror_walk', 'talon_and_wing',
                          # Sword Contracts
                          'elemental_weapon', 'might_of_the_terrible_brute', 'overpowering_dread', 'primal_glory', 'touch_of_wrath',
                          # Royal Sword Contracts
                          'elemental_fury', 'oathbreakers_punishment', 'red_revenge', 'relentless_pursuit', 'thief_of_reason',
                          # Chalice Contracts
                          'filling_the_cup', 'frail_as_the_dying_word', 'sleeps_sweet_embrace', 'curses_cure', 'dreamers_phalanx',
                          # Royal Chalice Contracts
                          'closing_deaths_door', 'feast_of_plenty', 'still_waters_run_deep', 'poison_the_well', 'shared_cup',
                          # Coin Contracts
                          'book_of_black_and_red', 'give_and_take', 'beggar_knight', 'coin_mark', 'grease_the_wheels',
                          # Royal Coin Contracts
                          'blood_debt', 'exchange_of_gilded_contracts', 'golden_promise', 'grand_revel_of_the_harvest', 'thirty_pieces',
                          # Scepter Contracts
                          'burning_ambition', 'jealous_vengeance', 'litany_of_rivals', 'knights_oath', 'unmask_the_dark_horse',
                          # Royal Scepter Contracts
                          'a_benevolent_hand', 'fake_it_til_you_make_it', 'tempters_quest', 'curse_of_hidden_strings', 'spare_not_the_rod',
                          # Stars Contracts
                          'pole_star', 'straight_on_til_morning', 'cynosure', 'shooting_star', 'retrograde',
                          # Royal Stars Contracts
                          'frozen_star', 'star_light_star_bright', 'light_of_ancient_stars', 'pinch_of_stardust',
                          # Thorn Contracts
                          'briars_herald', 'by_the_pricking_of_my_thumbs', 'thistles_rebuke', 'the_gouging_curse', 'embrace_of_nettles',
                          # Royal Thorn Contracts
                          'acanthas_fury', 'awaken_portal', 'crown_of_thorns', 'shrikes_larder', 'witchs_brambles',
                          # Spring Contracts
                          'cupids_arrow', 'dreams_of_the_earth', 'gift_of_warm_breath', 'springs_kiss', 'wyrd_faced_stranger',
                          # Royal Spring Contracts
                          'blessing_of_spring', 'gift_of_warm_blood', 'pandoras_gift', 'prince_of_ivy', 'waking_the_inner_fae',
                          # Summer Contracts
                          'baleful_sense', 'child_of_the_hearth', 'helios_light', 'high_summers_zeal', 'vigilance_of_ares',
                          # Royal Summer Contracts
                          'fiery_tongue', 'flames_of_summer', 'helios_judgment', 'solstice_revelation', 'sunburnt_heart',
                          # Autumn Contracts
                          'autumns_fury', 'last_harvest', 'tale_of_the_baba_yaga', 'twilights_harbinger', 'witches_intuition',
                          # Royal Autumn Contracts
                          'famines_bulwark', 'mien_of_the_baba_yaga', 'riding_the_falling_leaves', 'sorcerers_rebuke', 'tasting_the_harvest',
                          # Winter Contracts
                          'the_dragon_knows', 'heart_of_ice', 'ice_queens_call', 'slipknot_dreams', 'touch_of_winter',
                          # Royal Winter Contracts
                          'ermines_winter_coat', 'fallow_fields', 'field_of_regret', 'mantle_of_frost', 'winters_curse',
                          # Retaliation Contracts
                          'peacemakers_draw', 'draw_likeness',
                          # Goblin Contracts
                          'blessing_of_forgetfulness', 'distill_the_hidden', 'glib_tongue', 'goblins_eye', 'goblins_luck',
                          'huntsmans_clarion', 'lost_visage', 'mantle_mask', 'sight_of_truth_and_lies', 'uncanny', 'wayward_guide', 'wyrd_debt',
                          # Independent Arcadian Contracts
                          'coming_darkness', 'pomp_and_circumstance', 'shadow_puppet', 'steal_influence', 'earths_gentle_movements',
                          'dread_companion', 'cracked_mirror', 'listen_with_winds_ears', 'momentary_respite', 'earths_impenetrable_walls'
                          ],
            'geist': [
                            # Keys (semantic syntax)
                            "beasts", "blood", "chance", "cold wind", "deep waters", "disease", "grave dirt", "pyre flame", "stillness",
                            # Haunts (categories)
                            "boneyard", "caul", "curse", "dirge", "marionette", "memoria", "oracle", "rage", "shroud", "tomb"
                                ],
            # other templates as they're implemented
            'promethean': [],
            'demon': [],
            'beast': [],
            'hunter': [],
            'deviant': []
        }
        
        return template_power_map.get(template, [])
    
    def parse_target_stat(self, args):
        """Parse target and stat from arguments"""
        if "/" in args and "=" in args:
            # Check if this is a specialty command
            if args.startswith("specialty/") or "/specialty/" in args:
                # Handle specialty commands: specialty/skill=value or name/specialty/skill=value
                if args.count("/") == 2:  # name/specialty/skill=value
                    target_specialty_stat, value = args.split("=", 1)
                    target_name, specialty_keyword, skill = target_specialty_stat.split("/", 2)
                    return target_name.strip(), f"specialty/{skill.strip().lower().replace(' ', '_')}", value.strip()
                else:  # specialty/skill=value
                    specialty_stat, value = args.split("=", 1)
                    specialty_keyword, skill = specialty_stat.split("/", 1)
                    return None, f"specialty/{skill.strip().lower().replace(' ', '_')}", value.strip()
            else:
                # Format: name/stat=value
                target_stat, value = args.split("=", 1)
                target_name, stat = target_stat.split("/", 1)
                # Convert spaces to underscores in stat names
                stat = stat.strip().lower().replace(" ", "_")
                return target_name.strip(), stat, value.strip()
        elif "=" in args:
            # Check if this is a specialty command
            if args.startswith("specialty/"):
                # Format: specialty/skill=value
                specialty_stat, value = args.split("=", 1)
                specialty_keyword, skill = specialty_stat.split("/", 1)
                return None, f"specialty/{skill.strip().lower().replace(' ', '_')}", value.strip()
            else:
                # Format: stat=value (self)
                stat, value = args.split("=", 1)
                stat = stat.strip().lower()
                value = value.strip()
                
                # Check for semantic power syntax: key=beasts, ceremony=pass_on, contract=hostile_takeover, etc.
                semantic_prefixes = ["key", "ceremony", "rite", "ritual", "contract"]
                if stat in semantic_prefixes:
                    # this is semantic syntax like key=beasts
                    power_type = stat
                    power_name = value.lower().replace(" ", "_")
                    return None, f"{power_type}:{power_name}", "known"  # Mark as known for individual abilities
                
                # Convert spaces to underscores in stat names
                stat = stat.replace(" ", "_")
                return None, stat, value
        else:
            return None, None, None
    

    
    def set_stat(self):
        """Set a stat value"""
        target_name, stat, value = self.parse_target_stat(self.args)
        
        if not stat or value is None:
            self.caller.msg("Usage: +stat <stat>=<value> or +stat <name>/<stat>=<value>")
            return
        
        # Determine target
        if target_name:
            # Setting for someone else - requires staff or NPC control permissions
            target = self.caller.search(target_name, global_search=True)
            if not target:
                return
                
            # Check permissions for the target
            is_npc = hasattr(target, 'db') and target.db.is_npc
            
            if is_npc:
                # For NPCs, check if caller can control them
                if not target.can_control(self.caller):
                    self.caller.msg("You don't have permission to modify that NPC's stats.")
                    return
            else:
                # For player characters, requires staff
                if not self.caller.check_permstring("Builder"):
                    self.caller.msg("Only staff can set stats for other player characters.")
                    return
        else:
            # Setting for self
            target = self.caller
            
            # Check if this is a player character that's approved
            is_npc = hasattr(target, 'db') and target.db.is_npc
            if not is_npc and target.db.approved:
                self.caller.msg("Your character is approved. Only staff can modify your stats.")
                return
        
       
        # Initialize stats if needed
        if not target.db.stats:
            target.db.stats = {
                "attributes": {},
                "skills": {},
                "advantages": {},
                "anchors": {},
                "bio": {},
                "merits": {},
                "specialties": {},
                "other": {}
            }
        
        # Try to convert value to int
        try:
            value = int(value)
        except ValueError:
            # Keep as string for non-numeric stats
            pass
        
        # Determine stat category and validate
        stat_set = False
        
        # Check attributes
        if stat in ["strength", "dexterity", "stamina", "presence", "manipulation", 
                   "composure", "intelligence", "wits", "resolve"]:
            if isinstance(value, int) and 1 <= value <= 5:
                target.db.stats["attributes"][stat] = value
                stat_set = True
            else:
                self.caller.msg("Attributes must be between 1 and 5.")
                return
        
        # Check skills
        elif stat in ["crafts", "investigation", "medicine", "occult", "politics", "science",
                     "athletics", "brawl", "drive", "firearms", "larceny", "stealth", 
                     "survival", "weaponry", "animal_ken", "empathy", "expression", 
                     "intimidation", "persuasion", "socialize", "streetwise", "subterfuge"]:
            if isinstance(value, int) and 0 <= value <= 5:
                target.db.stats["skills"][stat] = value
                stat_set = True
            else:
                self.caller.msg("Skills must be between 0 and 5.")
                return
        
        # Check advantages (including supernatural power stats)
        elif stat in ["health", "willpower", "speed", "defense", "initiative", 
                      "blood_potency", "gnosis", "primal_urge", "wyrd", "synergy", 
                      "azoth", "primum", "satiety", "deviation"]:
            if isinstance(value, int) and value >= 0:
                target.db.stats["advantages"][stat] = value
                stat_set = True
            else:
                self.caller.msg("Advantages must be positive numbers.")
                return
        
        # Check bio fields
        elif stat in ["fullname", "full_name", "birthdate", "concept", "virtue", "vice", "sire"]:
            # Map alternate names and handle space conversions
            bio_field = stat
            if stat in ["full_name", "fullname"]:
                bio_field = "full_name"  # Store as full_name internally
            
            # Special validation for virtue/vice in legacy mode
            if stat in ["virtue", "vice"]:
                from commands.CmdLegacy import is_legacy_mode
                if is_legacy_mode():
                    from world.legacy_virtues_vices import is_valid_virtue, is_valid_vice, get_virtue_info, get_vice_info, get_legacy_virtue_list, get_legacy_vice_list
                    
                    value_lower = str(value).lower()
                    if stat == "virtue":
                        if not is_valid_virtue(value_lower):
                            virtue_list = ", ".join([v.title() for v in get_legacy_virtue_list()])
                            self.caller.msg(f"'{value}' is not a valid legacy virtue.")
                            self.caller.msg(f"Valid legacy virtues: {virtue_list}")
                            return
                        # Get the proper capitalized name
                        virtue_info = get_virtue_info(value_lower)
                        value = virtue_info["name"]
                    elif stat == "vice":
                        if not is_valid_vice(value_lower):
                            vice_list = ", ".join([v.title() for v in get_legacy_vice_list()])
                            self.caller.msg(f"'{value}' is not a valid legacy vice.")
                            self.caller.msg(f"Valid legacy vices: {vice_list}")
                            return
                        # Get the proper capitalized name
                        vice_info = get_vice_info(value_lower)
                        value = vice_info["name"]
            
            # Validate length for string fields
            if isinstance(value, str) and len(value) > 50:
                self.caller.msg("Bio field values cannot exceed 50 characters.")
                return
            
            # Ensure bio category exists
            if "bio" not in target.db.stats:
                target.db.stats["bio"] = {}
            
            # Store in bio category
            target.db.stats["bio"][bio_field] = str(value)
            stat_set = True
            
            # Also store virtue/vice in anchors for backward compatibility
            if stat in ["virtue", "vice"]:
                if "anchors" not in target.db.stats:
                    target.db.stats["anchors"] = {}
                target.db.stats["anchors"][stat] = str(value)
        
        # Check template-specific bio fields
        elif stat in ["path", "order", "mask", "dirge", "clan", "covenant", "bone", "blood", 
                     "auspice", "tribe", "seeming", "court", "kith", "burden", "root", "bloom", 
                     "krewe", "lineage", "refinement", "profession", "organization", "creed", 
                     "incarnation", "agenda", "agency", "hunger", "family", "inheritance", 
                     "origin", "clade", "divergence", "needle", "thread", "legend", "life",
                     "geist_name", "embrace_date"]:
            
            # Get character's template
            character_template = target.db.stats.get("other", {}).get("template", "Mortal")
            valid_fields = target.get_template_bio_fields(character_template)
            
            # Check if this field is valid for the character's template
            if stat not in valid_fields:
                self.caller.msg(f"{stat.title()} is not a valid field for {character_template} characters.")
                self.caller.msg(f"Valid fields for {character_template}: {', '.join(valid_fields).title()}")
                return
            
            # Validate field value if it has restrictions
            is_valid, error_msg = target.validate_template_field(stat, str(value))
            if not is_valid:
                self.caller.msg(error_msg)
                return
            
            # Validate length for string fields
            if isinstance(value, str) and len(value) > 50:
                self.caller.msg("Bio field values cannot exceed 50 characters.")
                return
            
            # Store in bio category
            target.db.stats["bio"][stat] = str(value).title()
            stat_set = True
        
        # Check anchors (for backward compatibility)
        elif stat in ["virtue", "vice"]:
            target.db.stats["anchors"][stat] = str(value)
            # Also store in bio for new system
            if "bio" not in target.db.stats:
                target.db.stats["bio"] = {}
            target.db.stats["bio"][stat] = str(value)
            stat_set = True
        
        # Check template (staff only, or self if not approved)
        elif stat == "template":
            # Check permissions: staff can always change templates, players can change their own if not approved
            if target != self.caller:
                # Changing someone else's template - requires staff
                if not self.caller.check_permstring("Builder"):
                    self.caller.msg("Only staff can set template for other characters.")
                    return
            else:
                # Changing own template - allowed if not approved, staff always allowed
                if target.db.approved and not self.caller.check_permstring("Builder"):
                    self.caller.msg("Your character is approved. Only staff can change your template now.")
                    self.caller.msg("Contact staff if you need a template change.")
                    return
            
            # Validate template based on legacy mode
            from commands.CmdLegacy import is_legacy_mode
            from world.cofd.template_registry import template_registry
            
            legacy_mode = is_legacy_mode()
            
            if legacy_mode:
                # In legacy mode, only allow legacy templates and exclude 2nd edition only templates
                valid_templates = [
                    "legacy_vampire", "legacy_werewolf", "legacy_mage", "legacy_changeling", 
                    "legacy_geist", "legacy_promethean", "legacy_hunter", "mortal"
                ]
                
                if value.lower() not in valid_templates:
                    self.caller.msg("Invalid template for Legacy Mode. Valid legacy templates: Legacy Vampire, Legacy Werewolf, Legacy Mage, Legacy Changeling, Legacy Geist, Legacy Promethean, Legacy Hunter, Mortal")
                    return
            else:
                # In modern mode, allow all templates except legacy ones
                valid_templates = [
                    "changeling", "vampire", "werewolf", "mage", "geist", 
                    "deviant", "demon", "hunter", "promethean", 
                    "mortal+", "mortal plus", "mortal"
                ]
                
                if value.lower() not in valid_templates:
                    self.caller.msg("Invalid template. Valid templates: Changeling, Vampire, Werewolf, Mage, Geist, Deviant, Demon, Hunter, Promethean, Mortal+, Mortal")
                    return
            
            # Completely wipe character stats for clean slate
            old_template = target.db.stats.get("other", {}).get("template", "Mortal") if target.db.stats else "Mortal"
            
            # Confirm the nuclear option
            self.caller.msg(f"|rWARNING:|n This will completely wipe all of {target.name}'s stats!")
            self.caller.msg(f"Changing template from {old_template} to {value.title()}...")
            
            # Nuclear option: completely wipe stats
            target.db.stats = {
                "attributes": {},
                "skills": {},
                "advantages": {},
                "anchors": {},
                "bio": {},
                "merits": {},
                "specialties": {},
                "powers": {},
                "other": {"template": value.title()}
            }
            
            # Also wipe any geist stats if they exist
            if hasattr(target.db, 'geist_stats'):
                target.db.geist_stats = None
            
            # Clear other character-specific data
            target.db.willpower_current = None
            target.db.aspirations = []
            target.db.approved = False  # Template changes require re-approval
            
            self.caller.msg(f"Template changed to {value.title()}. All stats have been wiped clean.")
            self.caller.msg("Character is now unapproved and ready for fresh character generation.")
            
            # Notify the target
            if target != self.caller:
                target.msg(f"Your template has been changed to {value.title()} by {self.caller.name}.")
                target.msg("All your stats have been wiped clean. Use +stat to set new stats.")
            
            stat_set = True
        
        # Other stats
        elif stat in ["integrity", "size", "beats", "experience"]:
            if stat in ["integrity", "size"] and isinstance(value, int):
                if stat == "integrity" and not 0 <= value <= 10:
                    self.caller.msg("Integrity must be between 0 and 10.")
                    return
                elif stat == "size" and not 1 <= value <= 10:
                    self.caller.msg("Size must be between 1 and 10.")
                    return
            elif stat in ["beats", "experience"] and isinstance(value, int) and value < 0:
                self.caller.msg("Beats and experience cannot be negative.")
                return
                
            target.db.stats["other"][stat] = value
            stat_set = True
        
        # Template-specific integrity names (aliases for integrity)
        elif stat.lower() in ["humanity", "wisdom", "pilgrimage", "clarity", "cover", "harmony", "synergy", "satiety"]:
            # Get character's template to validate the integrity name is appropriate
            character_template = target.db.stats.get("other", {}).get("template", "Mortal")
            expected_integrity_name = target.get_integrity_name(character_template).lower()
            
            if stat.lower() != expected_integrity_name.lower():
                self.caller.msg(f"For {character_template} characters, use '{expected_integrity_name.lower()}' instead of '{stat}'.")
                return
            
            # Validate integrity value
            if not isinstance(value, int):
                try:
                    value = int(value)
                except ValueError:
                    self.caller.msg("Integrity value must be a number.")
                    return
            
            if not 0 <= value <= 10:
                self.caller.msg(f"{expected_integrity_name} must be between 0 and 10.")
                return
            
            # Special handling for Geist characters - Synergy is an advantage, not integrity
            if character_template.lower() == "geist" and stat.lower() == "synergy":
                target.db.stats["advantages"]["synergy"] = value
            else:
                # Store as integrity for other templates
                target.db.stats["other"]["integrity"] = value
            stat_set = True
        
        # Check specialties
        elif stat.startswith("specialty/"):
            skill_name = stat[10:]  # Remove "specialty/" prefix
            
            # Validate that this is a valid skill
            valid_skills = ["crafts", "investigation", "medicine", "occult", "politics", "science",
                           "athletics", "brawl", "drive", "firearms", "larceny", "stealth", 
                           "survival", "weaponry", "animal_ken", "empathy", "expression", 
                           "intimidation", "persuasion", "socialize", "streetwise", "subterfuge"]
            
            if skill_name not in valid_skills:
                self.caller.msg(f"'{skill_name}' is not a valid skill name.")
                self.caller.msg(f"Valid skills: {', '.join(valid_skills)}")
                return
            
            # Check if character has dots in this skill
            current_skill_value = target.db.stats.get("skills", {}).get(skill_name, 0)
            if current_skill_value == 0:
                self.caller.msg(f"Cannot add specialty to {skill_name.replace('_', ' ').title()} - character has no dots in this skill.")
                self.caller.msg(f"Set dots in the skill first with: +stat {skill_name}=<dots>")
                return
            
            # Validate specialty value
            if not isinstance(value, str) or len(value.strip()) == 0:
                self.caller.msg("Specialty must be a non-empty text description.")
                return
            
            if len(value) > 30:
                self.caller.msg("Specialty descriptions cannot exceed 30 characters.")
                return
            
            # Ensure specialties category exists
            if "specialties" not in target.db.stats:
                target.db.stats["specialties"] = {}
            
            # Initialize skill specialties list if needed
            if skill_name not in target.db.stats["specialties"]:
                target.db.stats["specialties"][skill_name] = []
            
            # Check if this specialty already exists for this skill
            existing_specialties = target.db.stats["specialties"][skill_name]
            if value.strip().title() in existing_specialties:
                self.caller.msg(f"{target.name} already has '{value.strip().title()}' as a specialty for {skill_name.replace('_', ' ').title()}.")
                return
            
            # Add the specialty
            target.db.stats["specialties"][skill_name].append(value.strip().title())
            stat_set = True
        
        # Check for semantic power syntax (key:beasts, ceremony:pass_on, etc.)
        elif ":" in stat:
            power_type, power_name = stat.split(":", 1)
            return self._handle_semantic_power(target, power_type, power_name, value)
        
        # Check powers (template-specific supernatural abilities)
        else:
            # Get character's template to determine valid powers
            character_template = target.db.stats.get("other", {}).get("template", "Mortal")
            template_powers = self._get_template_powers(character_template)
            
            if stat in template_powers:
                # Validate power value
                if not isinstance(value, int):
                    try:
                        value = int(value)
                    except ValueError:
                        self.caller.msg("Power dots must be a number.")
                        return
                
                # Validate power range (0-5 dots)
                if not 0 <= value <= 5:
                    self.caller.msg("Powers must be between 0 and 5 dots.")
                    return
                
                # Ensure powers category exists
                if "powers" not in target.db.stats:
                    target.db.stats["powers"] = {}
                
                # Set the power
                target.db.stats["powers"][stat] = value
                stat_set = True
                
                # Message about power setting
                power_display = stat.replace('_', ' ').title()
                if value == 0:
                    self.caller.msg(f"Removed {power_display} from {target.name}.")
                else:
                    self.caller.msg(f"Set {target.name}'s {power_display} to {value} dots.")
        
        # Check merits (allow setting for unapproved characters, redirect approved to XP system)
        if not stat_set:
            try:
                from world.cofd.merits.general_merits import merits_dict
                if stat in merits_dict:
                    merit = merits_dict[stat]
                    
                    # Check if character is approved and not an NPC
                    is_npc = hasattr(target, 'db') and target.db.is_npc
                    if target.db.approved and not is_npc:
                        self.caller.msg(f"Character is approved. Merits must be purchased with experience points.")
                        self.caller.msg(f"Use '+xp/buy {stat}=[dots]' to purchase merits with experience points.")
                        self.caller.msg(f"Use '+xp/info {stat}' to see merit details and prerequisites.")
                        return
                    
                    # For unapproved characters and NPCs, allow merit setting
                    if not isinstance(value, int):
                        try:
                            value = int(value)
                        except ValueError:
                            self.caller.msg("Merit dots must be a number.")
                            return
                    
                    # Validate dots
                    if value < merit.min_value or value > merit.max_value:
                        self.caller.msg(f"{merit.name} must be between {merit.min_value} and {merit.max_value} dots.")
                        return
                    
                    # Check prerequisites if they exist
                    if merit.prerequisite and not target.check_merit_prerequisites(merit.prerequisite):
                        self.caller.msg(f"Prerequisites not met for {merit.name}: {merit.prerequisite}")
                        return
                    
                    # Ensure merits category exists
                    if "merits" not in target.db.stats:
                        target.db.stats["merits"] = {}
                    
                    # Store merit data
                    target.db.stats["merits"][stat] = {
                        "dots": value,
                        "max_dots": merit.max_value,
                        "merit_type": merit.merit_type,
                        "description": merit.description
                    }
                    stat_set = True
            except ImportError:
                # If merit system not available, fall through to custom stat
                pass
        
        # Custom stat handling
        if not stat_set:
            target.db.stats["other"][stat] = value
            stat_set = True
        
        if stat_set:
            if stat == "template":
                # handled by set_template method
                pass
            elif stat in ["fullname", "full_name", "birthdate", "concept", "virtue", "vice"]:
                self.caller.msg(f"Set {target.name}'s {stat} to {value}.")
                if stat == "concept":
                    self.caller.msg("Remember: Your concept should be a brief description of what your character does.")
                elif stat == "virtue":
                    self.caller.msg("Virtue represents your character's highest moral principle.")
                elif stat == "vice":
                    self.caller.msg("Vice represents your character's greatest moral failing.")
            elif stat.lower() in ["humanity", "wisdom", "pilgrimage", "clarity", "cover", "harmony", "synergy", "satiety"]:
                # Use the proper name for template-specific integrity
                character_template = target.db.stats.get("other", {}).get("template", "Mortal")
                integrity_name = target.get_integrity_name(character_template)
                self.caller.msg(f"Set {target.name}'s {integrity_name} to {value}.")
            elif stat.startswith("specialty/"):
                skill_name = stat[10:]  # Remove "specialty/" prefix
                skill_display = skill_name.replace('_', ' ').title()
                self.caller.msg(f"Added '{value}' as a specialty for {target.name}'s {skill_display}.")
            else:
                # Check if this was a merit
                try:
                    from world.cofd.merits.general_merits import merits_dict
                    if stat in merits_dict:
                        merit = merits_dict[stat]
                        self.caller.msg(f"Set {target.name}'s {merit.name} merit to {value} dots.")
                        is_npc = hasattr(target, 'db') and target.db.is_npc
                        if not target.db.approved and not is_npc:
                            self.caller.msg("(Merit set during character generation - after approval, use +xp/buy to purchase merits)")
                    else:
                        self.caller.msg(f"Set {target.name}'s {stat} to {value}.")
                except ImportError:
                    self.caller.msg(f"Set {target.name}'s {stat} to {value}.")
            
            # Auto-calculate derived stats if setting attributes
            if stat in ["strength", "dexterity", "stamina", "composure", "resolve", "wits", "size"]:
                target.calculate_derived_stats(self.caller)
            
            # Clean up misplaced stats
            target.cleanup_misplaced_stats(self.caller)
    
    def remove_stat(self):
        """Remove a stat"""
        if "/" in self.args:
            # Format: name/stat or name/specialty/skill
            args_parts = self.args.split("/")
            if len(args_parts) == 3 and args_parts[1] == "specialty":
                # Format: name/specialty/skill
                target_name = args_parts[0].strip()
                stat = f"specialty/{args_parts[2].strip().lower().replace(' ', '_')}"
            else:
                # Format: name/stat
                target_name, stat = self.args.split("/", 1)
                target_name = target_name.strip()
                # Convert spaces to underscores in stat names
                stat = stat.strip().lower().replace(" ", "_")
            
            # Check permissions for the target
            target = self.caller.search(target_name, global_search=True)
            if not target:
                return
                
            is_npc = hasattr(target, 'db') and target.db.is_npc
            
            if is_npc:
                # For NPCs, check if caller can control them
                if not target.can_control(self.caller):
                    self.caller.msg("You don't have permission to modify that NPC's stats.")
                    return
            else:
                # For player characters, requires staff
                if not self.caller.check_permstring("Builder"):
                    self.caller.msg("Only staff can remove stats from other player characters.")
                    return
        else:
            # Format: stat or specialty/skill (self)
            target = self.caller
            args = self.args.strip()
            if args.startswith("specialty/"):
                stat = args.lower().replace(" ", "_")
            else:
                # Convert spaces to underscores in stat names
                stat = args.lower().replace(" ", "_")
            
            # Check if this is a player character that's approved
            is_npc = hasattr(target, 'db') and target.db.is_npc
            if not is_npc and target.db.approved:
                self.caller.msg("Your character is approved. Only staff can modify your stats.")
                return
        
        if not target.db.stats:
            self.caller.msg(f"{target.name} has no stats set.")
            return
        
        # Find and remove the stat
        removed = False
        
        # Check if removing a specialty
        if stat.startswith("specialty/"):
            skill_name = stat[10:]  # Remove "specialty/" prefix
            specialties = target.db.stats.get("specialties", {})
            if skill_name in specialties and specialties[skill_name]:
                # Remove all specialties for this skill
                del specialties[skill_name]
                removed = True
                skill_display = skill_name.replace('_', ' ').title()
                self.caller.msg(f"Removed all specialties for {target.name}'s {skill_display}.")
            else:
                skill_display = skill_name.replace('_', ' ').title()
                self.caller.msg(f"{target.name} has no specialties for {skill_display}.")
            return
        
        # Check if trying to remove a merit
        try:
            from world.cofd.merits.general_merits import merits_dict
            if stat in merits_dict:
                # Check if character is approved and not an NPC
                is_npc = hasattr(target, 'db') and target.db.is_npc
                if target.db.approved and not is_npc:
                    self.caller.msg(f"Character is approved. Merits cannot be removed directly with +stat/remove.")
                    if self.caller.check_permstring("Builder"):
                        self.caller.msg(f"Use '+xp/refund {stat}' to refund the merit and return experience points.")
                    else:
                        self.caller.msg(f"Only staff can refund merits. Contact staff for assistance.")
                    return
                # For unapproved characters and NPCs, allow direct removal
                # (will be handled in the normal category loop below)
        except ImportError:
            # If merit system not available, continue with normal removal
            pass
        
        for category in ["attributes", "skills", "advantages", "bio", "anchors", "merits", "powers", "other"]:
            if stat in target.db.stats.get(category, {}):
                # Special handling for template (staff only)
                if stat == "template" and category == "other":
                    if not self.caller.check_permstring("Builder"):
                        self.caller.msg("Only staff can modify template.")
                        return
                
                # Special handling for template-specific bio fields
                if stat in ["path", "order", "mask", "dirge", "clan", "covenant", "bone", "blood", 
                           "auspice", "tribe", "seeming", "court", "kith", "burden", "archetype", 
                           "krewe", "lineage", "refinement", "profession", "organization", "creed", 
                           "incarnation", "agenda", "agency", "hunger", "family", "inheritance", 
                           "origin", "clade", "divergence", "needle", "thread", "legend", "life"] and category == "bio":
                    character_template = target.db.stats.get("other", {}).get("template", "Mortal")
                    valid_fields = target.get_template_bio_fields(character_template)
                    
                    if stat not in valid_fields:
                        self.caller.msg(f"{stat.title()} is not a valid field for {character_template} characters.")
                        return
                
                # Special handling for virtue/vice (remove from both bio and anchors)
                if stat in ["virtue", "vice"]:
                    target.db.stats.get("bio", {}).pop(stat, None)
                    target.db.stats.get("anchors", {}).pop(stat, None)
                    removed = True
                    break
                else:
                    del target.db.stats[category][stat]
                    removed = True
                    break
        
        if removed:
            self.caller.msg(f"Removed {stat} from {target.name}.")
        else:
            self.caller.msg(f"{target.name} doesn't have a stat called {stat}.")
    
    def list_stats(self):
        """List all stats for a character"""
        if self.args:
            # Viewing someone else
            target = self.caller.search(self.args.strip(), global_search=True)
            if not target:
                return
        else:
            # Viewing self
            target = self.caller
        
        # Note: Auto-migration has been moved to admin commands
        # self.migrate_legacy_stats(target, silent=True)
        
        if not target.db.stats:
            self.caller.msg(f"{target.name} has no stats set.")
            return
        
        # Clean up any misplaced stats before displaying
        target.cleanup_misplaced_stats(self.caller)
        
        output = [f"|y{target.name}'s Statistics|n"]
        if target.db.approved:
            output.append("|gCharacter is APPROVED|n")
        else:
            output.append("|rCharacter is NOT APPROVED|n")
        output.append("")
        
        # Bio information
        bio = target.db.stats.get("bio", {})
        other = target.db.stats.get("other", {})
        if bio or other.get("template"):
            output.append("|wBio:|n")
            
            # Basic bio info
            full_name = bio.get("full_name", bio.get("fullname", "<not set>"))
            birthdate = bio.get("birthdate", "<not set>")
            concept = bio.get("concept", "<not set>")
            template = other.get("template", "Mortal")
            
            output.append(f"  Full Name: {full_name}")
            output.append(f"  Birthdate: {birthdate}")
            output.append(f"  Concept: {concept}")
            output.append(f"  template: {template}")
            
            # Get template-specific fields
            valid_fields = target.get_template_bio_fields(template)
            
            # Display template-specific bio fields if they exist
            template_bio_data = []
            for field in valid_fields:
                if field in bio:
                    template_bio_data.append((field, bio[field]))
            
            if template_bio_data:
                output.append(f"  |w{template} Template:|n")
                for field, value in template_bio_data:
                    output.append(f"    {field.title()}: {value}")
            
            # Show missing required fields for the template
            missing_fields = [field for field in valid_fields if field not in bio]
            if missing_fields:
                output.append(f"  |yMissing {template} fields:|n {', '.join(missing_fields).title()}")
            
            output.append("")
        
        # Attributes
        attrs = target.db.stats.get("attributes", {})
        if attrs:
            output.append("|wAttributes:|n")
            output.append("  Mental: " + ", ".join(f"{k.title()}: {v}" for k, v in attrs.items() 
                                                   if k in ["intelligence", "wits", "resolve"]))
            output.append("  Physical: " + ", ".join(f"{k.title()}: {v}" for k, v in attrs.items() 
                                                    if k in ["strength", "dexterity", "stamina"]))
            output.append("  Social: " + ", ".join(f"{k.title()}: {v}" for k, v in attrs.items() 
                                                  if k in ["presence", "manipulation", "composure"]))
            output.append("")
        
        # Skills
        skills = target.db.stats.get("skills", {})
        specialties = target.db.stats.get("specialties", {})
        if skills:
            output.append("|wSkills:|n")
            mental_skills = {k: v for k, v in skills.items() 
                           if k in ["crafts", "investigation", "medicine", "occult", "politics", "science"]}
            physical_skills = {k: v for k, v in skills.items() 
                             if k in ["athletics", "brawl", "drive", "firearms", "larceny", "stealth", "survival", "weaponry"]}
            social_skills = {k: v for k, v in skills.items() 
                           if k in ["animal_ken", "empathy", "expression", "intimidation", "persuasion", "socialize", "streetwise", "subterfuge"]}
            
            if mental_skills:
                mental_display = []
                for k, v in mental_skills.items():
                    skill_text = f"{k.replace('_', ' ').title()}: {v}"
                    if k in specialties and specialties[k]:
                        specialty_list = ", ".join(specialties[k])
                        skill_text += f" ({specialty_list})"
                    mental_display.append(skill_text)
                output.append("  Mental: " + ", ".join(mental_display))
                
            if physical_skills:
                physical_display = []
                for k, v in physical_skills.items():
                    skill_text = f"{k.replace('_', ' ').title()}: {v}"
                    if k in specialties and specialties[k]:
                        specialty_list = ", ".join(specialties[k])
                        skill_text += f" ({specialty_list})"
                    physical_display.append(skill_text)
                output.append("  Physical: " + ", ".join(physical_display))
                
            if social_skills:
                social_display = []
                for k, v in social_skills.items():
                    skill_text = f"{k.replace('_', ' ').title()}: {v}"
                    if k in specialties and specialties[k]:
                        specialty_list = ", ".join(specialties[k])
                        skill_text += f" ({specialty_list})"
                    social_display.append(skill_text)
                output.append("  Social: " + ", ".join(social_display))
                
            output.append("")
        
        # Advantages
        advantages = target.db.stats.get("advantages", {})
        if advantages:
            output.append("|wDerived Stats:|n")
            for k, v in advantages.items():
                output.append(f"  {k.title()}: {v}")
            output.append("")
        
        # Merits
        merits = target.db.stats.get("merits", {})
        if merits:
            output.append("|wMerits:|n")
            
            # Group merits by type for organized display
            merit_categories = {}
            for merit_name, merit_data in merits.items():
                merit_type = merit_data.get("merit_type", "other")
                if merit_type not in merit_categories:
                    merit_categories[merit_type] = []
                
                dots = merit_data.get("dots", 1)
                max_dots = merit_data.get("max_dots", 5)
                merit_display = f"{merit_name.replace('_', ' ').title()} ({dots}/{max_dots} dots)"
                merit_categories[merit_type].append(merit_display)
            
            # Display merits by category
            category_order = ["mental", "physical", "social", "fighting", "style", "supernatural", "other"]
            
            for category in category_order:
                if category in merit_categories:
                    category_merits = sorted(merit_categories[category])
                    if category_merits:
                        output.append(f"  |c{category.title()}:|n " + ", ".join(category_merits))
            
            # Display any remaining categories not in the ordered list
            for category, category_merits in merit_categories.items():
                if category not in category_order and category_merits:
                    category_merits = sorted(category_merits)
                    output.append(f"  |c{category.title()}:|n " + ", ".join(category_merits))
            
            output.append("")
        
        # Powers
        powers = target.db.stats.get("powers", {})
        if powers:
            output.append("|wPowers:|n")
            
            # Get template to determine power type name
            template = other.get("template", "Mortal").lower()
            power_type_names = {
                'vampire': 'Disciplines',
                'mage': 'Arcana', 
                'werewolf': 'Gifts & Rites',
                'changeling': 'Contracts',
                'geist': 'Manifestations',
                'promethean': 'Transmutations',
                'demon': 'Embeds & Exploits',
                'beast': 'Nightmares',
                'hunter': 'Tactics',
                'deviant': 'Variations'
            }
            power_type = power_type_names.get(template, 'Powers')
            
            # Display powers with dots
            power_list = []
            for power_name, dots in sorted(powers.items()):
                if dots > 0:  # Only show powers with dots
                    # Clean up display name - remove prefixes and format properly
                    display_name = power_name
                    if power_name.startswith('discipline_'):
                        display_name = power_name[11:]  # Remove 'discipline_'
                    elif power_name.startswith('arcanum_'):
                        display_name = power_name[8:]   # Remove 'arcanum_'
                    elif power_name.startswith('gift_'):
                        display_name = power_name[5:]   # Remove 'gift_'
                    elif power_name.startswith('contract_'):
                        display_name = power_name[9:]   # Remove 'contract_'
                    elif power_name.startswith('rite_'):
                        display_name = power_name[5:]   # Remove 'rite_'
                    
                    power_display = f"{display_name.replace('_', ' ').title()} ({dots} dots)"
                    power_list.append(power_display)
            
            if power_list:
                output.append(f"  |c{power_type}:|n " + ", ".join(power_list))
            else:
                output.append(f"  |c{power_type}:|n None")
            
            output.append("")
        
        # Anchors
        anchors = target.db.stats.get("anchors", {})
        if anchors:
            output.append("|wAnchors:|n")
            for k, v in anchors.items():
                output.append(f"  {k.title()}: {v}")
            output.append("")
        
        # Other
        other = target.db.stats.get("other", {})
        if other:
            output.append("|wOther:|n")
            for k, v in other.items():
                output.append(f"  {k.title()}: {v}")
        
        self.caller.msg("\n".join(output))
    
    def approve_character(self):
        """Approve a character, locking their stats"""
        if not self.caller.check_permstring("Builder"):
            self.caller.msg("Only staff can approve characters.")
            return
        
        if not self.args:
            self.caller.msg("Usage: +stat/approve <name>")
            return
        
        target = self.caller.search(self.args.strip(), global_search=True)
        if not target:
            return
        
        if target.db.approved:
            self.caller.msg(f"{target.name} is already approved.")
            return
        
        target.db.approved = True
        self.caller.msg(f"{target.name} has been approved. Their stats are now locked.")
        target.msg("Your character has been approved! Your stats are now locked.")
    
    def unapprove_character(self):
        """Unapprove a character, unlocking their stats"""
        if not self.caller.check_permstring("Builder"):
            self.caller.msg("Only staff can unapprove characters.")
            return
        
        if not self.args:
            self.caller.msg("Usage: +stat/unapprove <name>")
            return
        
        target = self.caller.search(self.args.strip(), global_search=True)
        if not target:
            return
        
        if not target.db.approved:
            self.caller.msg(f"{target.name} is not approved.")
            return
        
        target.db.approved = False
        self.caller.msg(f"{target.name} has been unapproved. They can now modify their stats.")
        target.msg("Your character has been unapproved. You can now modify your stats.")

    def reset_template(self):
        """Reset a character's template and completely wipe stats"""
        if not self.caller.check_permstring("Builder"):
            self.caller.msg("Only staff can reset templates.")
            return
        
        if not self.args or "=" not in self.args:
            self.caller.msg("Usage: +stat/reset <name>=<template>")
            self.caller.msg("This will completely wipe all stats and reset to the new template.")
            return
        
        name, template = self.args.split("=", 1)
        name = name.strip()
        template = template.strip()
        
        target = self.caller.search(name, global_search=True)
        if not target:
            return
        
        # Validate template based on legacy mode
        from commands.CmdLegacy import is_legacy_mode
        
        legacy_mode = is_legacy_mode()
        
        if legacy_mode:
            # In legacy mode, only allow legacy templates
            valid_templates = [
                "legacy_vampire", "legacy_werewolf", "legacy_mage", "legacy_changeling", 
                "legacy_geist", "legacy_promethean", "legacy_hunter", "mortal"
            ]
            
            if template.lower() not in valid_templates:
                self.caller.msg("Invalid template for Legacy Mode. Valid legacy templates: Legacy Vampire, Legacy Werewolf, Legacy Mage, Legacy Changeling, Legacy Geist, Legacy Promethean, Legacy Hunter, Mortal")
                return
        else:
            # In modern mode, allow all templates except legacy ones
            valid_templates = [
                "changeling", "vampire", "werewolf", "mage", "geist", 
                "deviant", "demon", "hunter", "promethean", 
                "mortal+", "mortal plus", "mortal"
            ]
            
            if template.lower() not in valid_templates:
                self.caller.msg("Invalid template. Valid templates: Changeling, Vampire, Werewolf, Mage, Geist, Deviant, Demon, Hunter, Promethean, Mortal+, Mortal")
                return
        
        # Confirm the reset action
        self.caller.msg(f"|rWARNING:|n This will completely wipe all of {target.name}'s stats!")
        self.caller.msg(f"Resetting {target.name} to {template.title()} template...")
        
        # Use the nuclear option to reset stats
        message = target.reset_stats_for_template(template, self.caller)
        self.caller.msg(message)
        
        # Notify the target
        target.msg(f"Your character has been reset to {template.title()} template by {self.caller.name}.")
        target.msg("All your previous stats have been wiped clean. Use +stat to set new stats.")
    
    def set_geist_stat(self):
        """Set a stat on a geist (Sin-Eater secondary character sheet)"""
        if not self.args or "=" not in self.args:
            self.caller.msg("Usage: +stat/geist <stat>=<value>")
            return
        
        # Only the player can set their own geist stats (for now)
        target = self.caller
        
        # Check if character is a Sin-Eater
        character_template = target.db.stats.get("other", {}).get("template", "Mortal")
        if character_template.lower() != "geist":
            self.caller.msg("Only Sin-Eater characters can have a geist. Your template is currently: " + character_template)
            self.caller.msg("Use '+stat template=geist' (staff) to change your template first.")
            return
        
        # Check if character is approved (same restrictions as regular stats)
        is_npc = hasattr(target, 'db') and target.db.is_npc
        if not is_npc and target.db.approved:
            self.caller.msg("Your character is approved. Only staff can modify your geist stats.")
            return
        
        # Parse stat and value
        stat, value = self.args.split("=", 1)
        stat = stat.strip().lower().replace(" ", "_")
        value = value.strip()
        
        # Initialize geist_stats if needed
        if not hasattr(target.db, 'geist_stats') or not target.db.geist_stats:
            target.db.geist_stats = {
                "attributes": {"power": 1, "finesse": 1, "resistance": 1},
                "bio": {},
                "remembrance": {},
                "keys": {},
                "haunts": {},
                "advantages": {},
                "other": {"rank": 3, "size": 5}
            }
        
        # Get template config for validation
        from world.cofd.templates import get_template_definition
        template_def = get_template_definition("geist")
        geist_config = template_def.get("geist_config", {}) if template_def else {}
        
        # Validate and set the stat
        stat_set = self._set_geist_stat_value(target, stat, value, geist_config)
        
        if stat_set:
            self.caller.msg(f"Set geist's {stat.replace('_', ' ')} to {value}.")
            
            # Auto-calculate derived stats if setting attributes
            if stat in ["power", "finesse", "resistance"]:
                self._calculate_geist_derived_stats(target)
        else:
            self.caller.msg(f"Failed to set geist stat: {stat}")
    
    def _set_geist_stat_value(self, target, stat, value, geist_config):
        """Set a specific geist stat value with validation"""
        geist_stats = target.db.geist_stats
        
        # Try to convert value to int for numeric stats
        original_value = value
        try:
            value = int(value)
        except ValueError:
            # Keep as string for non-numeric stats
            pass
        
        # Handle different stat categories
        if stat in ["power", "finesse", "resistance"]:
            # Geist attributes
            if not isinstance(value, int):
                self.caller.msg("Geist attributes must be numbers.")
                return False
            
            max_attr = geist_config.get("max_attribute", 9)
            if not 1 <= value <= max_attr:
                self.caller.msg(f"Geist attributes must be between 1 and {max_attr}.")
                return False
            
            # Check total attribute dots (base 3 + 12 to assign = 15 total)
            current_total = sum(geist_stats["attributes"].values())
            current_value = geist_stats["attributes"].get(stat, 1)
            new_total = current_total - current_value + value
            max_total = 3 + geist_config.get("attribute_dots_to_assign", 12)
            
            if new_total > max_total:
                self.caller.msg(f"Cannot set {stat} to {value}. Total attribute dots would be {new_total}, maximum is {max_total}.")
                self.caller.msg(f"Current totals: Power {geist_stats['attributes']['power']}, Finesse {geist_stats['attributes']['finesse']}, Resistance {geist_stats['attributes']['resistance']}")
                return False
            
            geist_stats["attributes"][stat] = value
            return True
        
        elif stat in ["concept", "remembrance_description", "virtue", "vice", "crisis_trigger", "ban", "bane"]:
            # Bio fields (string values)
            if isinstance(value, int):
                value = original_value  # Use original string value
            
            if len(str(value)) > 100:
                self.caller.msg("Geist bio fields cannot exceed 100 characters.")
                return False
            
            # Validate specific fields
            if stat == "virtue":
                # For geists, virtue can be more flexible than standard anchors
                geist_stats["bio"][stat] = str(value).title()
                return True
            elif stat == "vice":
                # For geists, vice can be more flexible than standard anchors
                geist_stats["bio"][stat] = str(value).title()
                return True
            elif stat == "crisis_trigger":
                valid_triggers = geist_config.get("crisis_triggers", [])
                if valid_triggers and value.lower() not in valid_triggers:
                    self.caller.msg(f"Invalid crisis trigger. Valid options: {', '.join(valid_triggers)}")
                    return False
                geist_stats["bio"][stat] = str(value).lower()
                return True
            else:
                geist_stats["bio"][stat] = str(value)
                return True
        
        elif stat == "innate_key":
            # Innate key selection
            valid_keys = geist_config.get("innate_keys", [])
            if valid_keys and value.lower() not in valid_keys:
                self.caller.msg(f"Invalid innate key. Valid options: {', '.join(valid_keys)}")
                return False
            geist_stats["bio"]["innate_key"] = str(value).lower()
            return True
        
        elif stat == "remembrance_trait":
            # Remembrance trait (skill or merit)
            if not isinstance(value, str):
                self.caller.msg("Remembrance trait must be a skill or merit name.")
                return False
                
            value_lower = value.lower().replace(" ", "_")
            valid_skills = geist_config.get("remembrance_skills", [])
            valid_merits = geist_config.get("remembrance_merits", [])
            
            if value_lower not in valid_skills + valid_merits:
                self.caller.msg(f"Invalid remembrance trait. Must be a valid skill or merit (≤3 dots).")
                self.caller.msg(f"Valid skills: {', '.join(valid_skills)}")
                self.caller.msg(f"Valid merits: {', '.join(valid_merits)}")
                return False
            
            geist_stats["remembrance"]["trait"] = value_lower
            geist_stats["remembrance"]["trait_type"] = "skill" if value_lower in valid_skills else "merit"
            return True
        
        elif stat == "remembrance_dots":
            # Remembrance trait dots
            if not isinstance(value, int):
                self.caller.msg("Remembrance dots must be a number.")
                return False
                
            max_dots = geist_config.get("remembrance_max_dots", 3)
            if not 1 <= value <= max_dots:
                self.caller.msg(f"Remembrance trait dots must be between 1 and {max_dots}.")
                return False
            
            geist_stats["remembrance"]["dots"] = value
            return True
        
        
        else:
            # Unknown stat
            self.caller.msg(f"Unknown geist stat: {stat}")
            self.caller.msg("Valid geist stats:")
            self.caller.msg("  Attributes: power, finesse, resistance")
            self.caller.msg("  Bio: concept, remembrance_description, virtue, vice, crisis_trigger, ban, bane, innate_key")
            self.caller.msg("  Remembrance: remembrance_trait, remembrance_dots")
            self.caller.msg("  Note: For keys, use the semantic syntax:")
            self.caller.msg("    +stat key=beasts")
            self.caller.msg("  Note: For haunts, use regular numeric syntax:")
            self.caller.msg("    +stat boneyard=3")
            return False
    
    def _calculate_geist_derived_stats(self, target):
        """Calculate derived stats for a geist"""
        geist_stats = target.db.geist_stats
        attrs = geist_stats["attributes"]
        
        # Calculate derived stats per Geist rules
        defense = min(attrs["power"], attrs["finesse"])
        initiative = attrs["finesse"] + attrs["resistance"] 
        speed = attrs["power"] + attrs["finesse"] + 5
        size = geist_stats["other"]["size"]  # Always 5 for geists
        
        # Store derived stats
        geist_stats["advantages"] = {
            "defense": defense,
            "initiative": initiative,
            "speed": speed
        }
        
        self.caller.msg(f"Recalculated geist derived stats: Defense {defense}, Initiative {initiative}, Speed {speed}")
    
    def _handle_semantic_power(self, target, power_type, power_name, value):
        """Handle semantic power syntax like key=beasts, ceremony=pass_on"""
        character_template = target.db.stats.get("other", {}).get("template", "Mortal")
        
        # Define valid powers for each semantic type
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
            ]
        }
        
        # Validate power type
        if power_type not in valid_powers:
            self.caller.msg(f"Invalid power type: {power_type}")
            self.caller.msg("Valid types: key, ceremony, rite, ritual, contract")
            return False
        
        # Validate power name
        if power_name not in valid_powers[power_type]:
            self.caller.msg(f"Invalid {power_type}: {power_name}")
            self.caller.msg(f"Valid {power_type}s: {', '.join(valid_powers[power_type])}")
            return False
        
        # Check template compatibility
        template_requirements = {
            "key": ["geist"],
            "ceremony": ["geist"],
            "rite": ["werewolf"],
            "ritual": ["vampire"],
            "contract": ["changeling"]
        }
        
        required_templates = template_requirements.get(power_type, [])
        if required_templates and character_template.lower() not in required_templates:
            self.caller.msg(f"{power_type.title()}s are only available to {', '.join(required_templates).title()} characters.")
            self.caller.msg(f"Your template is: {character_template}")
            return False
        
        # Handle different power types
        if power_type == "key":
            # Keys go to geist stats for Sin-Eaters
            if not hasattr(target.db, 'geist_stats') or not target.db.geist_stats:
                target.db.geist_stats = {
                    "attributes": {"power": 1, "finesse": 1, "resistance": 1},
                    "bio": {},
                    "remembrance": {},
                    "keys": {},
                    "haunts": {},
                    "advantages": {},
                    "other": {"rank": 3, "size": 5}
                }
            
            # Keys are known/unknown - semantic syntax means they have the key
            target.db.geist_stats["keys"][power_name.replace("_", " ")] = True
            self.caller.msg(f"Set {target.name} to have the {power_name.replace('_', ' ').title()} key.")
        else:
            # Ceremonies, rites, rituals go to regular powers as known abilities (stored as 1)
            if "powers" not in target.db.stats:
                target.db.stats["powers"] = {}
            
            target.db.stats["powers"][power_name] = 1
            self.caller.msg(f"Set {target.name} to know {power_name.replace('_', ' ').title()} ({power_type}).")
        
        return True

class CmdRecalc(MuxCommand):
    """
    Recalculate derived statistics.
    
    Usage:
        +recalc - Recalculate your derived stats
        +recalc <name> - Recalculate someone else's derived stats (staff only)
        
    This command recalculates derived stats like health, willpower, speed, 
    defense, and initiative based on your current attributes.
    """
    
    key = "+recalc"
    aliases = ["recalc"]
    help_category = "Character"
    
    def func(self):
        """Execute the recalculation"""
        if self.args:
            # Recalculating for someone else - requires staff
            if not self.caller.check_permstring("Builder"):
                self.caller.msg("Only staff can recalculate derived stats for other characters.")
                return
            
            target = self.caller.search(self.args.strip(), global_search=True)
            if not target:
                return
        else:
            # Recalculating for self
            target = self.caller
        
        # Use character's recalculate method
        target.recalculate_derived_stats(self.caller)