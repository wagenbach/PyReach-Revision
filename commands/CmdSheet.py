from evennia.commands.default.muxcommand import MuxCommand
from evennia.utils import evtable
from world.utils.health_utils import get_health_track, set_health_track, compact_track
from world.cofd.templates import get_template_definition

class CmdSheet(MuxCommand):
    """
    Display your character sheet.
    
    Usage:
        +sheet [character] - Display character sheet
        +sheet/ascii [character] - Force ASCII display (no Unicode dots)
        +sheet/geist [character] - Display geist character sheet (Sin-Eater only)
        +sheet/geist/ascii [character] - Display geist sheet in ASCII mode
        
    Shows all character statistics in an organized format.
    The /geist switch displays the secondary character sheet for a Sin-Eater's bound geist.
    """
    
    key = "+sheet"
    aliases = ["sheet"]
    help_category = "Character Sheets and Development"
    
    def _get_dots_style(self, force_ascii=False):
        """
        Determine whether to use Unicode or ASCII dots based on client support.
        
        Args:
            force_ascii (bool): Force ASCII display regardless of client support
            
        Returns:
            tuple: (filled_char, empty_char, supports_utf8)
        """
        # Check if user explicitly wants ASCII
        if force_ascii or "ascii" in self.switches:
            return ("*", "-", False)
        
        # Check session UTF-8 support
        if self.session:
            # Check if the client explicitly supports UTF-8:
            utf8_support = self.session.protocol_flags.get("UTF-8", None)
            encoding = self.session.protocol_flags.get("ENCODING", "utf-8").lower()
            
            # If the client explicitly doesn't support UTF-8 or uses non-UTF-8 encoding:
            if utf8_support is False or encoding not in ["utf-8", "utf8"]:
                return ("*", "-", False)
        
        # Unicode is default if there's not a specific error, the client is unknown, or the player doesn't specify ascii
        return ("●", "○", True)
    
    def _format_dots(self, value, max_value=5, force_ascii=False):
        """
        Format a stat value as dots (Unicode or ASCII).
        
        Args:
            value (int): Current stat value
            max_value (int): Maximum possible value
            force_ascii (bool): Force ASCII display
            
        Returns:
            str: Formatted dot display
        """
        filled_char, empty_char, supports_utf8 = self._get_dots_style(force_ascii)
        filled = filled_char * value
        empty = empty_char * (max_value - value)
        return filled + empty
    
    def _show_encoding_warning(self, supports_utf8):
        """
        Show encoding warning if not using UTF-8.
        
        Args:
            supports_utf8 (bool): Whether UTF-8 is supported
        """
        if not supports_utf8:
            warning = [
                "",
                "|y" + "="*78 + "|n",
                "|rNOTE: Your client doesn't support UTF-8 encoding.|n",
                "|w- Set your MUD client to use UTF-8 encoding|n",
                "|w- Or use: option encoding=utf-8  (if you're not logged in)|n",
                "|w- Or use: +sheet/ascii for ASCII display|n",
                "|y" + "="*78 + "|n",
                ""
            ]
            self.caller.msg("\n".join(warning))

    def _get_template_bio_fields(self, template):
        """Get valid bio fields for a specific template from the template registry"""
        if not template:
            return ["virtue", "vice"]  # Default fallback for empty/None template
            
        template = template.lower()
        
        # Handle alternate naming
        if template == "mortal plus":
            template = "mortal_plus"
        
        # Try to get template definition from registry
        template_def = get_template_definition(template)
        if template_def and "bio_fields" in template_def:
            return template_def["bio_fields"]
        
        # Fallback to default mortal fields if template not found
        return ["virtue", "vice"]

    def _migrate_legacy_stats(self, target):
        """
        Migrate legacy stats from individual attributes to new stats dictionary format.
        Silent migration that only migrates if legacy data is found.
        
        Args:
            target: Character object to migrate
            
        Returns:
            bool: True if migration was performed, False if no legacy data found
        """
        legacy_attrs = [
            # Attributes
            "strength", "dexterity", "stamina", "presence", "manipulation", 
            "composure", "intelligence", "wits", "resolve",
            # Skills  
            "crafts", "investigation", "medicine", "occult", "politics", "science",
            "athletics", "brawl", "drive", "firearms", "larceny", "stealth", 
            "survival", "weaponry", "animal_ken", "empathy", "expression", 
            "intimidation", "persuasion", "socialize", "streetwise", "subterfuge",
            # Advantages
            "health", "willpower", "speed", "defense", "initiative",
            # Bio fields
            "fullname", "full_name", "birthdate", "concept", "virtue", "vice",
            # Other
            "integrity", "size", "beats", "experience", "template",
            # Power stats
            "gnosis", "blood_potency", "primal_urge", "wyrd", "synergy", "azoth", 
            "primum", "satiety", "deviation"
        ]
        
        # Check for legacy data
        migrated_data = {}
        has_legacy_data = False
        for attr_name in legacy_attrs:
            if hasattr(target.db, attr_name):
                value = getattr(target.db, attr_name)
                if value is not None:
                    migrated_data[attr_name] = value
                    has_legacy_data = True
        
        if not has_legacy_data:
            return False
        
        # Initialize modern stats structure if needed
        if not target.db.stats:
            target.db.stats = {
                "attributes": {},
                "skills": {},
                "advantages": {},
                "anchors": {},
                "bio": {},
                "other": {}
            }
        
        # Migrate data to appropriate categories
        attributes = ["strength", "dexterity", "stamina", "presence", "manipulation", 
                     "composure", "intelligence", "wits", "resolve"]
        skills = ["crafts", "investigation", "medicine", "occult", "politics", "science",
                 "athletics", "brawl", "drive", "firearms", "larceny", "stealth", 
                 "survival", "weaponry", "animal_ken", "empathy", "expression", 
                 "intimidation", "persuasion", "socialize", "streetwise", "subterfuge"]
        advantages = ["health", "willpower", "speed", "defense", "initiative",
                     "gnosis", "blood_potency", "primal_urge", "wyrd", "synergy", 
                     "azoth", "primum", "satiety", "deviation"]
        bio_fields = ["fullname", "full_name", "birthdate", "concept", "virtue", "vice"]
        other_fields = ["integrity", "size", "beats", "experience", "template"]
        
        for attr_name, value in migrated_data.items():
            if attr_name in attributes:
                target.db.stats["attributes"][attr_name] = value
            elif attr_name in skills:
                target.db.stats["skills"][attr_name] = value
            elif attr_name in advantages:
                target.db.stats["advantages"][attr_name] = value
            elif attr_name in bio_fields:
                bio_key = "full_name" if attr_name in ["fullname", "full_name"] else attr_name
                target.db.stats["bio"][bio_key] = value
                if attr_name in ["virtue", "vice"]:
                    target.db.stats["anchors"][attr_name] = value
            elif attr_name in other_fields:
                target.db.stats["other"][attr_name] = value
            else:
                target.db.stats["other"][attr_name] = value
            
            # Clean up the old attribute
            try:
                delattr(target.db, attr_name)
            except AttributeError:
                pass
        
        return True

    def _format_section_header(self, section_name):
        """
        Create an arrow-style section header that spans 78 characters.
        Format: <----------------- SECTION NAME ----------------->
        """
        total_width = 78
        name_length = len(section_name)
        # Account for < and > characters (2 total) and spaces around name (2 total)
        available_dash_space = total_width - name_length - 4
        
        # Split dashes evenly, with extra dash on the right if odd number
        left_dashes = available_dash_space // 2
        right_dashes = available_dash_space - left_dashes
        
        return f"|g<{'-' * left_dashes}|n {section_name} |g{'-' * right_dashes}>|n"

    def _get_health_track(self, character):
        """Get health track as an array where index 0 is leftmost (most severe)."""
        return get_health_track(character)
    
    def _set_health_track(self, character, track):
        """Set health track from array format back to dictionary format."""
        set_health_track(character, track)
    
    def _get_template_powers(self, template):
        """Get the list of available primary powers for a specific template."""
        if not template:
            return []
            
        template = template.lower()
        
        # Primary powers only (disciplines, arcana, gifts)
        template_power_map = {
            'vampire': [
                       # Disciplines (categories only)
                       'animalism', 'auspex', 'bloodworking', 'cachexy', 'celerity',
                       'dominate', 'majesty', 'nightmare', 'obfuscate', 'praestantia', 'protean', 
                       'resilience', 'vigor', 'crochan', 'dead_signal', 'chary', 'vitiate', 'cruac', 'theban_sorcery'
                       ],
            'mage': ['arcanum_death', 'fate', 'forces', 'life', 'matter', 'mind', 'prime', 'space', 'spirit', 'time'],
            'werewolf': [
                        # Gifts (categories)
                        'gift_death', 'dominance', 'elementals', 'insight', 'inspiration', 'knowledge',
                        'nature', 'rage', 'gift_strength', 'technology', 'weather', 'hunting', 'pack',
                        'crescent_moon', 'full_moon', 'new_moon', 'gibbous_moon', 'half_moon', 'agony', 'blood',
                        'disease', 'evasion', 'fervor', 'hunger', 'shaping', 'gift_stealth', 'warding', 'change',
                        ],
            'changeling': [
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
                      # Keys
                      "beasts", "blood", "chance", "cold wind", "deep waters", "disease", "grave dirt", "pyre flame", "stillness",
                      # Haunts
                      "boneyard", "caul", "curse", "dirge", "marionette", "memoria", "oracle", "rage", "shroud", "tomb"
                          ],
            'promethean': [],
            'demon': [],
            'beast': [],
            'hunter': [],
            'deviant': []
        }
        
        return template_power_map.get(template, [])
    
    def _get_template_secondary_powers(self, template):
        """Get the list of available secondary powers (rituals, rites) for a specific template."""
        if not template:
            return []
            
        template = template.lower()
        
        # Secondary powers (rituals, rites, individual abilities)
        template_secondary_map = {
            'vampire': [
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
            'mage': [],  # Mages don't have secondary powers like rituals
            'werewolf': [
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
            'changeling': [],  # Changelings only have contracts (all primary)
            'geist': [
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
                        ],
            'promethean': [],
            'demon': [],
            'beast': [],
            'hunter': [],
            'deviant': []
        }
        
        return template_secondary_map.get(template, [])
    
    def _format_powers_display(self, powers, template_powers, force_ascii):
        """Format the powers section for display."""
        if not template_powers:
            return ["No powers available for this template."]
        
        power_lines = []
        
        # Group powers by category if applicable
        displayed_powers = []
        for power_name in template_powers:
            power_value = powers.get(power_name, 0)
            if power_value > 0:  # Only show powers they actually have
                dots = self._format_dots(power_value, 5, force_ascii)
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
                
                power_display = f"{display_name.replace('_', ' ').title():<20} {dots}"
                displayed_powers.append(power_display)
        
        if not displayed_powers:
            return ["No powers learned yet."]
        
        # Display powers in 2 columns like merits
        for i in range(0, len(displayed_powers), 2):
            left_power = displayed_powers[i] if i < len(displayed_powers) else ""
            right_power = displayed_powers[i + 1] if i + 1 < len(displayed_powers) else ""
            
            # Format with proper spacing (39 chars for left column)
            left_formatted = left_power.ljust(39)
            power_lines.append(f"{left_formatted} {right_power}")
        
        return power_lines
    
    def _format_secondary_powers_display(self, powers, template_secondary_powers, force_ascii):
        """Format the secondary powers (rituals/rites) section for display."""
        if not template_secondary_powers:
            return ["No secondary powers available for this template."]
        
        power_lines = []
        
        # Group secondary powers by category if applicable
        displayed_powers = []
        for power_name in template_secondary_powers:
            power_value = powers.get(power_name, 0)
            if power_value > 0:  # Only show powers they actually have
                # For secondary powers, show dots
                display_marker = self._format_dots(power_value, 5, force_ascii)
                
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
                
                power_display = f"{display_name.replace('_', ' ').title():<20} {display_marker}"
                displayed_powers.append(power_display)
        
        if not displayed_powers:
            return ["No secondary powers learned yet."]
        
        # Display powers in 2 columns like merits
        for i in range(0, len(displayed_powers), 2):
            left_power = displayed_powers[i] if i < len(displayed_powers) else ""
            right_power = displayed_powers[i + 1] if i + 1 < len(displayed_powers) else ""
            
            # Format with proper spacing (39 chars for left column)
            left_formatted = left_power.ljust(39)
            power_lines.append(f"{left_formatted} {right_power}")
        
        return power_lines

    def func(self):
        """Display the character sheet"""
        # Check if this is a geist sheet request
        if "geist" in self.switches:
            self.show_geist_sheet()
            return
            
        # Determine target
        if self.args:
            target = self.caller.search(self.args.strip(), global_search=True)
            if not target:
                return
        else:
            target = self.caller
        
        # Auto-migrate legacy stats if any exist (silent)
        # Note: Migration functionality has been moved to admin commands
        # self._migrate_legacy_stats(target)
        
        if not target.db.stats:
            self.caller.msg(f"{target.name} has no character sheet set up yet.")
            self.caller.msg("Use +stat <stat>=<value> to set your stats.")
            return
        
        # Get dot style and check UTF-8 support
        force_ascii = "ascii" in self.switches
        filled_char, empty_char, supports_utf8 = self._get_dots_style(force_ascii)
        
        # Show encoding warning if needed (only for self, not when viewing others)
        if target == self.caller and not supports_utf8 and "ascii" not in self.switches:
            self._show_encoding_warning(supports_utf8)
        
        # Build the sheet display
        output = []
        output.append(f"|y{'='*78}|n")
        output.append(f"|y{target.name.center(78)}|n")
        if target.db.approved:
            output.append(f"|g{'APPROVED'.center(78)}|n")
        else:
            output.append(f"|r{'NOT APPROVED'.center(78)}|n")
        output.append(f"|y{'='*78}|n")
        
        # Bio Section
        output.append(self._format_section_header("|wBIO|n"))
        
        # Get bio information from stats
        bio = target.db.stats.get("bio", {})
        other = target.db.stats.get("other", {})
        
        # Bio data with defaults
        full_name = bio.get("full_name", bio.get("fullname", "<not set>"))
        birthdate = bio.get("birthdate", "<not set>")
        concept = bio.get("concept", "<not set>")
        template = other.get("template", "Mortal")
        
        # Get template-specific fields to determine what to show
        template_fields = self._get_template_bio_fields(template)
        
        # Only get virtue/vice if they're valid for this template
        virtue = bio.get("virtue", "<not set>") if "virtue" in template_fields else None
        vice = bio.get("vice", "<not set>") if "vice" in template_fields else None
        
        # Create a list of all bio items to display
        bio_items = [
            ("Full Name", full_name),
            ("Template", template),
            ("Birthdate", birthdate),
            ("Concept", concept)
        ]
        
        # Add virtue/vice if they're valid for this template
        if virtue is not None:
            bio_items.append(("Virtue", virtue))
        if vice is not None:
            bio_items.append(("Vice", vice))
        
        # Add template-specific bio fields
        for field in template_fields:
            if field not in ["virtue", "vice"]:  # virtue/vice already added above if valid
                field_value = bio.get(field, "<not set>")
                bio_items.append((field.replace("_", " ").title(), field_value))
        
        # Display bio items in two-column format
        for i in range(0, len(bio_items), 2):
            left_label, left_value = bio_items[i]
            left_text = f"{left_label:<12}: {left_value}"
            
            if i + 1 < len(bio_items):
                right_label, right_value = bio_items[i + 1]
                right_text = f"{right_label:<12}: {right_value}"
            else:
                right_text = ""
            
            left_formatted = left_text.ljust(39)
            output.append(f"{left_formatted} {right_text}")
        
        # Attributes
        attrs = target.db.stats.get("attributes", {})
        if attrs:
            output.append(self._format_section_header("|wATTRIBUTES|n"))
            
            # Mental
            mental = []
            for attr in ["intelligence", "wits", "resolve"]:
                val = attrs.get(attr, 0)
                dots = self._format_dots(val, 5, force_ascii)
                mental.append(f"{attr.title():<15} {dots}")
            
            # Physical
            physical = []
            for attr in ["strength", "dexterity", "stamina"]:
                val = attrs.get(attr, 0)
                dots = self._format_dots(val, 5, force_ascii)
                physical.append(f"{attr.title():<15} {dots}")
            
            # Social
            social = []
            for attr in ["presence", "manipulation", "composure"]:
                val = attrs.get(attr, 0)
                dots = self._format_dots(val, 5, force_ascii)
                social.append(f"{attr.title():<15} {dots}")
            
            # Display in columns (aligned with skills)
            for i in range(3):
                row = mental[i].ljust(26) + physical[i].ljust(26) + social[i]
                output.append(row)
        
        # Skills
        skills = target.db.stats.get("skills", {})
        specialties = target.db.stats.get("specialties", {})
        if skills:
            output.append(self._format_section_header("|wSKILLS|n"))
            
            # Mental Skills
            mental_skills = ["crafts", "investigation", "medicine", "occult", "politics", "science"]
            mental_display = []
            mental_specialties = []
            for skill in mental_skills:
                val = skills.get(skill, 0)
                dots = self._format_dots(val, 5, force_ascii)
                skill_text = f"{skill.replace('_', ' ').title():<15} {dots}"
                mental_display.append(skill_text)
                
                # Collect specialties for separate display
                if skill in specialties and specialties[skill]:
                    specialty_list = ", ".join(specialties[skill])
                    mental_specialties.append(f"  ({specialty_list})")
                else:
                    mental_specialties.append("")
            
            # Physical Skills
            physical_skills = ["athletics", "brawl", "drive", "firearms", "larceny", "stealth", "survival", "weaponry"]
            physical_display = []
            physical_specialties = []
            for skill in physical_skills:
                val = skills.get(skill, 0)
                dots = self._format_dots(val, 5, force_ascii)
                skill_text = f"{skill.replace('_', ' ').title():<15} {dots}"
                physical_display.append(skill_text)
                
                # Collect specialties for separate display
                if skill in specialties and specialties[skill]:
                    specialty_list = ", ".join(specialties[skill])
                    physical_specialties.append(f"  ({specialty_list})")
                else:
                    physical_specialties.append("")
            
            # Social Skills
            social_skills = ["animal_ken", "empathy", "expression", "intimidation", "persuasion", "socialize", "streetwise", "subterfuge"]
            social_display = []
            social_specialties = []
            for skill in social_skills:
                val = skills.get(skill, 0)
                dots = self._format_dots(val, 5, force_ascii)
                skill_text = f"{skill.replace('_', ' ').title():<15} {dots}"
                social_display.append(skill_text)
                
                # Collect specialties for separate display
                if skill in specialties and specialties[skill]:
                    specialty_list = ", ".join(specialties[skill])
                    social_specialties.append(f"  ({specialty_list})")
                else:
                    social_specialties.append("")
            
            # Display skills in clean columns (no specialties inline)
            max_rows = max(len(mental_display), len(physical_display), len(social_display))
            for i in range(max_rows):
                row = ""
                if i < len(mental_display):
                    row += mental_display[i].ljust(26)
                else:
                    row += " " * 26
                if i < len(physical_display):
                    row += physical_display[i].ljust(26)
                else:
                    row += " " * 26
                if i < len(social_display):
                    row += social_display[i]
                output.append(row)
            
            # Display all specialties at the bottom of the skills section
            specialty_groups = []
            for skill_name, specialty_list in specialties.items():
                if specialty_list:
                    skill_display = skill_name.replace('_', ' ').title()
                    specialty_text = ", ".join(specialty_list)
                    specialty_groups.append(f"{skill_display} ({specialty_text})")
            
            if specialty_groups:
                output.append("")  # Empty line before specialties
                # Join all specialty groups with commas and wrap to fit line length
                specialties_text = ", ".join(specialty_groups)
                output.append(f"|cSpecialties:|n")
                output.append(f"  {specialties_text}")
        
        # Merits and Advantages sections side by side
        merits = target.db.stats.get("merits", {})
        advantages = target.db.stats.get("advantages", {})
        other = target.db.stats.get("other", {})
        template = other.get("template", "Mortal").lower()
        
        # Create merits list
        merit_list = []
        if merits:
            for merit_name, merit_data in sorted(merits.items()):
                dots = self._format_dots(merit_data.get("dots", 1), merit_data.get("max_dots", 5), force_ascii)
                merit_display = f"{merit_name.replace('_', ' ').title():<15} {dots}"
                merit_list.append(merit_display)
        
        # Create advantages list (including integrity)
        advantage_list = [
            f"{'Defense':<15} : {advantages.get('defense', 0)}",
            f"{'Speed':<15} : {advantages.get('speed', 0)}",
            f"{'Initiative':<15} : {advantages.get('initiative', 0)}",
            f"{'Size':<15} : {other.get('size', 5)}"
        ]
        
        # Add integrity to advantages (except for Geist characters who don't use integrity)
        if template != "geist":
            integrity_name = target.get_integrity_name(template)
            advantage_list.append(f"{integrity_name:<15} : {other.get('integrity', 7)}")
        
        # Add template-specific advantages
        if template == "changeling":
            wyrd = advantages.get("wyrd", 0)
            if wyrd > 0:
                advantage_list.append(f"{'Wyrd':<15} : {wyrd}")
        elif template == "werewolf":
            primal_urge = advantages.get("primal_urge", 0)
            if primal_urge > 0:
                advantage_list.append(f"{'Primal Urge':<15} : {primal_urge}")
        elif template == "vampire":
            blood_potency = advantages.get("blood_potency", 0)
            if blood_potency > 0:
                advantage_list.append(f"{'Blood Potency':<15} : {blood_potency}")
        elif template == "mage":
            gnosis = advantages.get("gnosis", 0)
            if gnosis > 0:
                advantage_list.append(f"{'Gnosis':<15} : {gnosis}")
        elif template == "beast":
            satiety = advantages.get("satiety", 0)
            if satiety > 0:
                advantage_list.append(f"{'Satiety':<15} : {satiety}")
        elif template == "deviant":
            deviation = advantages.get("deviation", 0)
            if deviation > 0:
                advantage_list.append(f"{'Deviation':<15} : {deviation}")
        elif template == "demon":
            primum = advantages.get("primum", 0)
            if primum > 0:
                advantage_list.append(f"{'Primum':<15} : {primum}")
        elif template == "promethean":
            azoth = advantages.get("azoth", 0)
            if azoth > 0:
                advantage_list.append(f"{'Azoth':<15} : {azoth}")
        elif template == "geist":
            # Geist characters use Synergy instead of integrity
            synergy = advantages.get("synergy", 1)
            advantage_list.append(f"{'Synergy':<15} : {synergy}")
        
        # Create section headers using the same format as other sections
        merits_header = f"|g<{'-' * 12} MERITS {'-' * 13}>|n"
        advantages_header = f"|g<{'-' * 9} ADVANTAGES {'-' * 13}>|n"
        output.append(f"{merits_header.ljust(39)} {advantages_header}")
        
        # Display merits and advantages side by side
        max_rows = max(len(merit_list) if merit_list else 1, len(advantage_list))
        for i in range(max_rows):
            left_item = merit_list[i] if i < len(merit_list) else ""
            right_item = advantage_list[i] if i < len(advantage_list) else ""
            
            # Handle empty merits case
            if not merit_list and i == 0:
                left_item = "No merits yet."
            
            left_formatted = left_item.ljust(39)
            output.append(f"{left_formatted} {right_item}")

        
        # Primary Powers (disciplines, arcana, gifts)
        powers = target.db.stats.get("powers", {})
        template_powers = self._get_template_powers(template)
        template_secondary_powers = self._get_template_secondary_powers(template)
        
        # Determine section names based on template
        primary_section_names = {
            'vampire': 'DISCIPLINES',
            'mage': 'ARCANA',
            'werewolf': 'GIFTS',
            'changeling': 'CONTRACTS',
            'geist': 'KEYS',
            'promethean': 'TRANSMUTATIONS',
            'demon': 'EMBEDS',
            'beast': 'NIGHTMARES',
            'hunter': 'ENDOWMENTS',
            'deviant': 'VARIATIONS'
        }
        secondary_section_names = {
            'vampire': 'BLOOD SORCERY & COILS',
            'werewolf': 'RITES',
            'geist': 'CEREMONIES',
            'promethean': 'BESTOWMENTS',
            'demon': 'EXPLOITS',
            'beast': 'RITUALS',
            'hunter': 'TACTICS',
            'deviant': 'RITUALS'
        }
        
        primary_section = primary_section_names.get(template.lower(), 'POWERS')
        secondary_section = secondary_section_names.get(template.lower(), 'RITUALS')
        
        # Special handling for Geist characters (Keys, Haunts, Ceremonies)
        if template.lower() == "geist":
            # Keys section (from geist_stats)
            output.append(self._format_section_header("|wKEYS|n"))
            
            if hasattr(target.db, 'geist_stats') and target.db.geist_stats:
                geist_keys = target.db.geist_stats.get("keys", {})
                key_list = []
                for key_name, has_key in geist_keys.items():
                    if has_key:
                        key_list.append(key_name.replace("_", " ").title())
                
                if key_list:
                    # Display keys in 2 columns
                    for i in range(0, len(key_list), 2):
                        left_key = key_list[i] if i < len(key_list) else ""
                        right_key = key_list[i + 1] if i + 1 < len(key_list) else ""
                        
                        left_formatted = left_key.ljust(39)
                        output.append(f"{left_formatted} {right_key}")
                else:
                    output.append("No keys unlocked yet.")
            else:
                output.append("No keys unlocked yet.")
            
            output.append("")
            output.append("|gSee +sheet/geist for detailed key information and geist character sheet.|n")
            
            # Haunts section (category powers stored in regular powers)
            output.append(self._format_section_header("|wHAUNTS|n"))
            
            # Get haunts from regular powers or geist_stats
            haunts_from_powers = {}
            haunts_from_geist = {}
            
            # Check regular powers for haunts
            haunt_names = ["boneyard", "caul", "curse", "dirge", "marionette", "memoria", "oracle", "rage", "shroud", "tomb"]
            for haunt_name in haunt_names:
                if haunt_name in powers and powers[haunt_name] > 0:
                    haunts_from_powers[haunt_name] = powers[haunt_name]
            
            # Check geist_stats for haunts  
            if hasattr(target.db, 'geist_stats') and target.db.geist_stats:
                geist_haunts = target.db.geist_stats.get("haunts", {})
                for haunt_name, rating in geist_haunts.items():
                    if rating > 0:
                        haunts_from_geist[haunt_name] = rating
            
            # Combine and display haunts
            all_haunts = {**haunts_from_powers, **haunts_from_geist}
            if all_haunts:
                haunt_list = []
                for haunt_name, haunt_rating in all_haunts.items():
                    dots = self._format_dots(haunt_rating, 5, force_ascii)
                    haunt_display = f"{haunt_name.replace('_', ' ').title():<15} {dots}"
                    haunt_list.append(haunt_display)
                
                # Display haunts in 2 columns like merits
                for i in range(0, len(haunt_list), 2):
                    left_haunt = haunt_list[i] if i < len(haunt_list) else ""
                    right_haunt = haunt_list[i + 1] if i + 1 < len(haunt_list) else ""
                    
                    # Format with proper spacing (39 chars for left column)
                    left_formatted = left_haunt.ljust(39)
                    output.append(f"{left_formatted} {right_haunt}")
            else:
                output.append("No haunts learned yet.")
            
            # Ceremonies section (individual abilities stored in regular powers)
            output.append(self._format_section_header("|wCEREMONIES|n"))
            
            ceremony_names = [
                "dead_mans_camera", "death_watch", "diviners_jawbone", "lovers_telephone", "ishtars_perfume",
                "crow_girl_kiss", "gifts_of_persephone", "ghost_trap", "skeleton_key", "bestow_regalia", 
                "krewe_binding", "speaker_for_the_dead", "black_cats_crossing", "bloody_codex", "dumb_supper",
                "forge_anchor", "maggot_homonculus", "pass_on", "ghost_binding", "persephones_return"
            ]
            
            ceremony_list = []
            for ceremony_name in ceremony_names:
                if ceremony_name in powers and powers[ceremony_name] > 0:
                    ceremony_display = ceremony_name.replace('_', ' ').title()
                    ceremony_list.append(ceremony_display)
            
            if ceremony_list:
                # Display ceremonies in 2 columns
                for i in range(0, len(ceremony_list), 2):
                    left_ceremony = ceremony_list[i] if i < len(ceremony_list) else ""
                    right_ceremony = ceremony_list[i + 1] if i + 1 < len(ceremony_list) else ""
                    
                    left_formatted = left_ceremony.ljust(39)
                    output.append(f"{left_formatted} {right_ceremony}")
            else:
                output.append("No ceremonies learned yet.")
        
        else:
            # Regular template power display
            if powers or template_powers:
                output.append(self._format_section_header(f"|w{primary_section}|n"))
                
                if template_powers:
                    power_display = self._format_powers_display(powers, template_powers, force_ascii)
                    output.extend(power_display)
                else:
                    output.append("No primary powers available for this template.")
        
        # Secondary Powers (rituals, rites, blood sorcery) - skip for Geist since handled above
        if template.lower() != "geist" and (powers or template_secondary_powers):
            if template_secondary_powers:  # Only show section if template has secondary powers
                output.append(self._format_section_header(f"|w{secondary_section}|n"))
                
                secondary_power_display = self._format_secondary_powers_display(powers, template_secondary_powers, force_ascii)
                output.extend(secondary_power_display)
        
        # Pools section (horizontal layout)
        output.append(self._format_section_header("|wPOOLS|n"))
        
        # Get pools data
        health_max = advantages.get("health", 7)
        health_track = self._get_health_track(target)
        
        # Save the compacted track back to ensure consistency
        self._set_health_track(target, health_track)
        
        # Create health boxes
        health_boxes = []
        for i in range(health_max):
            damage_type = health_track[i]
            if damage_type == "bashing":
                health_boxes.append("[|c/|n]")  # Cyan for bashing
            elif damage_type == "lethal":
                health_boxes.append("[|rX|n]")  # Red for lethal
            elif damage_type == "aggravated":
                health_boxes.append("[|R*|n]")  # Bright red for aggravated
            else:
                health_boxes.append("[ ]")
        
        # Willpower
        willpower_max = advantages.get("willpower", 3)
        willpower_current = target.db.willpower_current
        if willpower_current is None:
            willpower_current = willpower_max  # Default to full
        
        willpower_dots = self._format_dots(willpower_current, willpower_max, force_ascii)
        
        # Template-specific resource pools
        resource_pools = {
            "geist": ("Plasm", "plasm"),
            "changeling": ("Glamour", "glamour"), 
            "vampire": ("Vitae", "vitae"),
            "werewolf": ("Essence", "essence"),
            "mage": ("Mana", "mana"),
            "demon": ("Aether", "aether"),
            "promethean": ("Pyros", "pyros")
        }
        
        pool_display = ""
        if template in resource_pools:
            pool_name, pool_key = resource_pools[template]
            pool_current = getattr(target.db, f"{pool_key}_current", None)
            pool_max = advantages.get(pool_key, 10)  # Default max of 10 for most pools
            
            if pool_current is None:
                pool_current = pool_max  # Default to full
            
            pool_dots = self._format_dots(pool_current, pool_max, force_ascii)
            pool_display = f"{pool_name} ({pool_current}/{pool_max})"
        
        # Create horizontal pools layout
        health_label = "Health"
        willpower_label = f"Willpower ({willpower_current}/{willpower_max})"
        
        if pool_display:
            # Three pools: Health, Resource Pool, Willpower
            output.append(f"{health_label:^26}{pool_display:^26}{willpower_label:^26}")
            health_section = f"{''.join(health_boxes):^26}"
            pool_section = f"{pool_dots if 'pool_dots' in locals() else '':^26}"
            willpower_section = f"{willpower_dots:^26}"
            output.append(f"{health_section}{pool_section}{willpower_section}")
        else:
            # Two pools: Health, Willpower
            output.append(f"{health_label:^39}{willpower_label:^39}")
            health_section = f"{''.join(health_boxes):^39}"
            willpower_section = f"{willpower_dots:^39}"
            output.append(f"{health_section}{willpower_section}")

        # Aspirations (only show if there are any)
        aspirations_list = [asp for asp in target.db.aspirations if asp] if target.db.aspirations else []
        if aspirations_list:
            output.append(self._format_section_header("|wASPIRATIONS|n"))
            for i, asp in enumerate(aspirations_list, 1):
                output.append(f"{i}. {asp}")
        
        output.append(f"|y{'='*78}|n")
        
        # Add encoding info to bottom if ASCII mode is being used
        if not supports_utf8 or force_ascii:
            if force_ascii:
                output.append("|g(ASCII mode active - use +sheet without /ascii for Unicode)|n")
            else:
                output.append("|y(ASCII mode due to encoding - see note above for UTF-8)|n")
        
        self.caller.msg("\n".join(output))
    
    def show_geist_sheet(self):
        """Display the geist character sheet for Sin-Eaters"""
        # Determine target
        if self.args:
            target = self.caller.search(self.args.strip(), global_search=True)
            if not target:
                return
        else:
            target = self.caller
        
        # Check if character is a Sin-Eater
        character_template = target.db.stats.get("other", {}).get("template", "Mortal")
        if character_template.lower() != "geist":
            self.caller.msg(f"{target.name} is not a Sin-Eater. Current template: {character_template}")
            self.caller.msg("Only Sin-Eater characters have a geist to display.")
            return
        
        # Check if geist stats exist
        if not hasattr(target.db, 'geist_stats') or not target.db.geist_stats:
            self.caller.msg(f"{target.name} has no geist character sheet set up yet.")
            self.caller.msg("Use +stat/geist <stat>=<value> to set geist stats.")
            return
        
        # Get dot style and check UTF-8 support
        force_ascii = "ascii" in self.switches
        filled_char, empty_char, supports_utf8 = self._get_dots_style(force_ascii)
        
        # Show encoding warning if needed (only for self, not when viewing others)
        if target == self.caller and not supports_utf8 and "ascii" not in self.switches:
            self._show_encoding_warning(supports_utf8)
        
        geist_stats = target.db.geist_stats
        
        # Build the geist sheet display with magenta color scheme
        output = []
        output.append(f"|m{'='*78}|n")  # Magenta border
        
        # Get geist concept or use default
        geist_concept = geist_stats.get("bio", {}).get("concept", f"{target.name}'s Geist")
        output.append(f"|m{geist_concept.center(78)}|n")  # Magenta text
        output.append(f"|M{'GEIST CHARACTER SHEET'.center(78)}|n")  # Bright magenta
        output.append(f"|m{'='*78}|n")
        
        # Bio Section
        output.append(self._format_geist_section_header("|wBIO|n"))
        
        bio = geist_stats.get("bio", {})
        other = geist_stats.get("other", {})
        
        # Bio data with defaults
        concept = bio.get("concept", "<not set>")
        virtue = bio.get("virtue", "<not set>")
        vice = bio.get("vice", "<not set>")
        crisis_trigger = bio.get("crisis_trigger", "<not set>")
        ban = bio.get("ban", "<not set>")
        bane = bio.get("bane", "<not set>")
        innate_key = bio.get("innate_key", "<not set>")
        rank = other.get("rank", 3)
        
        # Remembrance section
        remembrance = geist_stats.get("remembrance", {})
        remembrance_desc = bio.get("remembrance_description", "<not set>")
        remembrance_trait = remembrance.get("trait", "<not set>")
        remembrance_dots = remembrance.get("dots", 0)
        remembrance_type = remembrance.get("trait_type", "")
        
        if remembrance_trait != "<not set>" and remembrance_dots > 0:
            trait_display = f"{remembrance_trait.replace('_', ' ').title()} ({remembrance_type}) {self._format_dots(remembrance_dots, 3, force_ascii)}"
        else:
            trait_display = "<not set>"
        
        # Create bio items list for display
        short_bio_items = [
            ("Concept", concept),
            ("Rank", f"{rank}"),
            ("Virtue", virtue),
            ("Vice", vice),
            ("Crisis Trigger", crisis_trigger.title() if crisis_trigger != "<not set>" else crisis_trigger),
            ("Bane", bane),
            ("Innate Key", innate_key.title() if innate_key != "<not set>" else innate_key),
            ("Trait", trait_display)
        ]

        # long fields that need their own lines
        long_bio_items = [
            ("Ban", ban),
            ("Remembrance", remembrance_desc)
        ]
        
        # Display short bio items in two-column format
        for i in range(0, len(short_bio_items), 2):
            left_label, left_value = short_bio_items[i]
            left_text = f"{left_label:<16}: {left_value}"
            
            if i + 1 < len(short_bio_items):
                right_label, right_value = short_bio_items[i + 1]
                right_text = f"{right_label:<16}: {right_value}"
            else:
                right_text = ""
            
            left_formatted = left_text.ljust(39)
            output.append(f"{left_formatted} {right_text}")
        
        # Add newline before long bio items
        output.append("")
        
        # Display long bio items on their own lines
        for label, value in long_bio_items:
            if value != "<not set>":
                output.append(f"{label:<16}: {value}")

        
        # Geist Attributes (simplified - Power, Finesse, Resistance)
        attrs = geist_stats.get("attributes", {"power": 1, "finesse": 1, "resistance": 1})
        if attrs:
            output.append(self._format_geist_section_header("|wATTRIBUTES|n"))
            
            # Format geist attributes
            power_val = attrs.get("power", 1)
            finesse_val = attrs.get("finesse", 1)
            resistance_val = attrs.get("resistance", 1)
            
            power_dots = self._format_dots(power_val, 9, force_ascii)
            finesse_dots = self._format_dots(finesse_val, 9, force_ascii)
            resistance_dots = self._format_dots(resistance_val, 9, force_ascii)
            
            output.append(f"Power          {power_dots} ({power_val})")
            output.append(f"Finesse        {finesse_dots} ({finesse_val})")
            output.append(f"Resistance     {resistance_dots} ({resistance_val})")
        
        # Keys Section
        keys = geist_stats.get("keys", {})
        output.append(self._format_geist_section_header("|wKEYS|n"))
        
        # Get key details from template
        from world.cofd.templates.geist import GEIST_KEY_DETAILS
        
        if keys:
            key_list = []
            for key_name, has_key in keys.items():
                if has_key:
                    key_lookup = key_name  # Keep as stored (with spaces)
                    key_details = GEIST_KEY_DETAILS.get(key_lookup, {})
                    full_name = key_details.get("full_name", key_name.replace("_", " ").title())
                    unlock_attr = key_details.get("unlock_attribute", "")
                    
                    key_display = f"|c{full_name}|n"
                    if unlock_attr:
                        key_display += f" (Unlock: {unlock_attr})"
                    key_list.append(key_display)
            
            if key_list:
                for i, key_display in enumerate(key_list):
                    output.append(f"  {key_display}")
                    
                    clean_key_name = key_display.split(" (")[0]
                    # Remove color codes from the key name
                    clean_key_name = clean_key_name.replace("|c", "").replace("|n", "").lower()
                    for key_code, details in GEIST_KEY_DETAILS.items():
                        if details["full_name"].lower() == clean_key_name:
                            output.append(f"    |cResonance:|n {details['resonance']}")
                            output.append(f"    |rDoom:|n {details['doom']}")
                            output.append("")
                            break
            else:
                output.append("  No keys unlocked yet.")
        else:
            output.append("  No keys unlocked yet.")
        
        # Derived Stats for Geist
        advantages = geist_stats.get("advantages", {})
        output.append(self._format_geist_section_header("|wADVANTAGES|n"))
        
        # Calculate derived stats if not already calculated
        if not advantages:
            defense = min(attrs.get("power", 1), attrs.get("finesse", 1))
            initiative = attrs.get("finesse", 1) + attrs.get("resistance", 1)
            speed = attrs.get("power", 1) + attrs.get("finesse", 1) + 5
            size = other.get("size", 5)
        else:
            defense = advantages.get("defense", 0)
            initiative = advantages.get("initiative", 0) 
            speed = advantages.get("speed", 0)
            size = other.get("size", 5)
        
        geist_advantages = [
            ("Defense", defense),
            ("Size", size),
            ("Initiative", initiative),
            ("Speed", speed)
        ]
        
        # Display advantages in rows of 2 columns
        for i in range(0, len(geist_advantages), 2):
            row_parts = []
            for j in range(2):
                if i + j < len(geist_advantages):
                    name, value = geist_advantages[i + j]
                    part = f"{name:<16} : {value}"
                    row_parts.append(part.ljust(39))
                else:
                    row_parts.append(" " * 39)
            output.append("".join(row_parts))
        output.append(f"|m{'='*78}|n")
        
        # Add encoding info to bottom if ASCII mode is being used
        if not supports_utf8 or force_ascii:
            if force_ascii:
                output.append("|g(ASCII mode active - use +sheet/geist without /ascii for Unicode)|n")
            else:
                output.append("|y(ASCII mode due to encoding - see note above for UTF-8)|n")
        
        self.caller.msg("\n".join(output))
    
    def _format_geist_section_header(self, section_name):
        """
        Create an arrow-style section header for geist sheets with magenta coloring.
        Format: <----------------- SECTION NAME ----------------->
        """
        total_width = 78
        name_length = len(section_name) - 4  # Account for color codes |w and |n
        # Account for < and > characters (2 total) and spaces around name (2 total)
        available_dash_space = total_width - name_length - 4
        
        # Split dashes evenly, with extra dash on the right if odd number
        left_dashes = available_dash_space // 2
        right_dashes = available_dash_space - left_dashes
        
        return f"|m<{'-' * left_dashes}|n {section_name} |m{'-' * right_dashes}>|n" 