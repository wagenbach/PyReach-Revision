from evennia.commands.default.muxcommand import MuxCommand
from evennia.utils import evtable
from world.cofd.lookup_data import (
    LOOKUP_DATA, 
    get_attribute_description, get_skill_description,
    get_discipline_description, get_arcanum_description,
    get_clan_description, get_covenant_description,
    get_path_info, get_order_description, get_template_description
)
import re


class CmdLookup(MuxCommand):
    """
    Look up character creation information and game statistics.
    
    Usage:
        +lookup                              - Show available lookup categories
        +lookup attributes                   - List all attributes
        +lookup skills [mental|physical|social] - List skills by category
        +lookup merits [type|template]       - List merits by type or template
        +lookup merits/vampire               - List vampire-specific merits (legacy syntax)
        +lookup disciplines                  - List vampire disciplines
        +lookup arcana                       - List mage arcana
        +lookup spells [arcana]              - List mage spells (optionally by arcana)
        +lookup endowments [type]            - List hunter endowments (optionally by type)
        +lookup clans                        - List vampire clans
        +lookup covenants                    - List vampire covenants
        +lookup paths                        - List mage paths
        +lookup orders                       - List mage orders
        +lookup templates                    - List all character templates
        +lookup <stat_name>                  - Get detailed info on specific stat
        +lookup/search <term>                - Search for stats containing term
        
        Examples:
        +lookup strength                     - Show strength attribute details
        +lookup fast_reflexes                - Show Fast Reflexes merit details
        +lookup merits mental                - List all mental merits
        +lookup merits mage                  - List all Mage-specific merits
        +lookup merits psychic               - List all Psychic merits
        +lookup/search "combat"              - Find all stats related to combat
        
    This command provides comprehensive information about character creation
    options including attributes, skills, merits, supernatural powers, and
    template-specific information like clans, covenants, paths, and orders.
    """
    
    key = "+lookup"
    aliases = ["+dict", "+dictionary", "+info", "+reference"]
    locks = "cmd:all()"
    help_category = "Character Creation"
    
    def func(self):
        if not self.args and not self.switches:
            self.show_categories()
            return
            
        if "search" in self.switches:
            self.search_stats()
            return
            
        args = self.args.strip().lower()
        
        # Handle specific lookups
        if args == "attributes":
            self.show_attributes()
        elif args.startswith("skills"):
            parts = args.split()
            category = parts[1] if len(parts) > 1 else None
            self.show_skills(category)
        elif args.startswith("merits"):
            parts = args.split()
            filter_arg = parts[1] if len(parts) > 1 else None
            self.show_merits(filter_arg)
        elif args == "disciplines":
            self.show_disciplines()
        elif args == "arcana":
            self.show_arcana()
        elif args.startswith("spells"):
            parts = args.split()
            arcana = parts[1] if len(parts) > 1 else None
            self.show_spells(arcana)
        elif args == "clans":
            self.show_clans()
        elif args == "covenants":
            self.show_covenants()
        elif args == "paths":
            self.show_paths()
        elif args == "orders":
            self.show_orders()
        elif args == "templates":
            self.show_templates()
        elif args == "auspices":
            self.show_auspices()
        elif args == "tribes":
            self.show_tribes()
        elif args == "seemings":
            self.show_seemings()
        elif args == "courts":
            self.show_courts()
        elif args == "incarnations":
            self.show_incarnations()
        elif args == "agendas":
            self.show_agendas()
        elif args == "embeds":
            self.show_embeds()
        elif args == "exploits":
            self.show_exploits()
        elif args == "transmutations":
            self.show_transmutations()
        elif args == "alembics":
            self.show_alembics()
        elif args == "bestowments":
            self.show_bestowments()
        elif args.startswith("endowments"):
            parts = args.split()
            endowment_type = parts[1] if len(parts) > 1 else None
            self.show_endowments(endowment_type)
        elif args == "lineages":
            self.show_lineages()
        elif args == "athanors":
            self.show_athanors()
        elif args == "guilds":
            self.show_guilds()
        elif args == "decrees":
            self.show_decrees()
        elif args == "judges":
            self.show_judges()
        elif args == "utterances":
            self.show_utterances()
        elif args == "affinities":
            self.show_affinities()
        elif args == "burdens":
            self.show_burdens()
        elif args == "krewe" or args == "krewes":
            self.show_krewe_types()
        elif args == "haunts":
            self.show_haunts()
        elif args == "keys":
            self.show_keys()
        elif args == "ceremonies":
            self.show_ceremonies()
        elif args == "origins":
            self.show_origins()
        elif args == "clades":
            self.show_clades()
        elif args == "deviations" or args == "variations":
            self.show_variations()
        elif args == "adaptations":
            self.show_adaptations()
        elif args == "mortal+" or args == "mortal_plus":
            self.show_mortal_plus_types()
        elif args == "psychic" or args == "psychic_powers":
            self.show_psychic_powers()
        elif args == "gutter" or args == "gutter_magic" or args == "witch":
            self.show_gutter_magic()
        elif args == "tells" or args == "wolf_blooded":
            self.show_wolf_blooded_tells()
        elif args == "specialties" or args.startswith("specialties"):
            parts = args.split()
            skill = parts[1] if len(parts) > 1 else None
            self.show_specialties(skill)
        else:
            # Try to find specific stat
            self.show_stat_details(args)
    
    def show_categories(self):
        """Show available lookup categories."""
        msg = "|wCharacter Creation Lookup System|n\n"
        msg += "|cAvailable Categories:|n\n"
        msg += "  |yattributes|n       - List all 9 core attributes\n"
        msg += "  |yskills [type]|n    - List skills (mental/physical/social)\n"
        msg += "  |ymerits [filter]|n  - List merits by type OR template\n"
        msg += "                       Examples: merits mental, merits mage, merits vampire\n"
        msg += "  |ydisciplines|n      - List vampire disciplines\n"
        msg += "  |yarcana|n           - List mage arcana\n"
        msg += "  |yspells [arcana]|n  - List mage spells (optionally by arcana)\n"
        msg += "  |yclans|n            - List vampire clans\n"
        msg += "  |ycovenants|n        - List vampire covenants\n"
        msg += "  |ypaths|n            - List mage paths\n"
        msg += "  |yorders|n           - List mage orders\n"
        msg += "  |yauspices|n         - List werewolf auspices\n"
        msg += "  |ytribes|n           - List werewolf tribes\n"
        msg += "  |yseeings|n         - List changeling seemings\n"
        msg += "  |ycourts|n           - List changeling courts\n"
        msg += "  |yincarnations|n     - List demon incarnations\n"
        msg += "  |yagendas|n          - List demon agendas\n"
        msg += "  |yembeds|n           - List demon embeds\n"
        msg += "  |yexploits|n         - List demon exploits\n"
        msg += "  |ytransmutations|n   - List promethean transmutations\n"
        msg += "  |yalembics|n         - List promethean alembics (by transmutation)\n"
        msg += "  |ybestowments|n      - List promethean bestowments\n"
        msg += "  |ylineages|n         - List promethean lineages\n"
        msg += "  |yathanors|n         - List promethean athanors (by lineage)\n"
        msg += "  |yendowments [type]|n - List hunter endowments (optionally by type)\n"
        msg += "  |yguilds|n           - List mummy guilds\n"
        msg += "  |ydecrees|n          - List mummy decrees\n"
        msg += "  |yjudges|n           - List mummy judges\n"
        msg += "  |yutterances|n       - List mummy utterances\n"
        msg += "  |yaffinities|n       - List mummy affinities\n"
        msg += "  |yburdens|n          - List geist burdens\n"
        msg += "  |ykrewe|n            - List geist krewe types\n"
        msg += "  |yhaunts|n           - List geist haunts\n"
        msg += "  |ykeys|n             - List geist keys\n"
        msg += "  |yceremonies|n       - List geist ceremonies\n"
        msg += "  |yorigins|n          - List deviant origins\n"
        msg += "  |yclades|n           - List deviant clades\n"
        msg += "  |yvariations|n       - List deviant variations\n"
        msg += "  |yadaptations|n      - List deviant adaptations\n"
        msg += "  |ymortal+|n          - List mortal+ types (2e)\n"
        msg += "  |ypsychic|n          - List psychic powers (2e)\n"
        msg += "  |ygutter|n           - List gutter magic types (2e witches)\n"
        msg += "  |ytells|n            - List wolf-blooded tells (2e)\n"
        msg += "  |yspecialties|n      - List all skill specialties\n"
        msg += "  |yspecialties <skill>|n - List specialties for a specific skill\n"
        msg += "  |ytemplates|n        - List character templates\n\n"
        msg += "|cSpecial Commands:|n\n"
        msg += "  |y+lookup <stat>|n       - Get details on specific stat\n"
        msg += "  |y+lookup/search <term>|n - Search for stats containing term\n\n"
        msg += "|cExamples:|n\n"
        msg += "  |y+lookup strength|n\n"
        msg += "  |y+lookup fast_reflexes|n\n"
        msg += "  |y+lookup merits mental|n\n"
        msg += "  |y+lookup/search combat|n"
        
        self.caller.msg(msg)
    
    def show_attributes(self):
        """Show all attributes organized by type."""
        table = evtable.EvTable("|wAttribute|n", "|wType|n", "|wRange|n", "|wDescription|n",
                               border="cells", width=78)
        
        # Organize by type
        power_attrs = []
        finesse_attrs = []
        resistance_attrs = []
        
        for name, attr in LOOKUP_DATA.attributes.items():
            if attr.att_type == "power":
                power_attrs.append((name.title(), attr))
            elif attr.att_type == "finesse":
                finesse_attrs.append((name.title(), attr))
            elif attr.att_type == "resistance":
                resistance_attrs.append((name.title(), attr))
        
        # Add to table organized by type
        for name, attr in power_attrs:
            table.add_row(f"|r{name}|n", "|rPower|n", f"{attr.min_value}-{attr.max_value}", 
                         get_attribute_description(name.lower()))
        for name, attr in finesse_attrs:
            table.add_row(f"|g{name}|n", "|gFinesse|n", f"{attr.min_value}-{attr.max_value}",
                         get_attribute_description(name.lower()))
        for name, attr in resistance_attrs:
            table.add_row(f"|b{name}|n", "|bResistance|n", f"{attr.min_value}-{attr.max_value}",
                         get_attribute_description(name.lower()))
        
        self.caller.msg(f"|wCharacter Attributes|n\n{table}")
        self.caller.msg("\n|cNote:|n All attributes start at 1 and can be raised to 5 during character creation.")
    
    def show_skills(self, category=None):
        """Show skills, optionally filtered by category."""
        if category and category not in ["mental", "physical", "social"]:
            self.caller.msg("Valid skill categories: mental, physical, social")
            return
        
        table = evtable.EvTable("|wSkill|n", "|wType|n", "|wUnskilled|n", "|wDescription|n",
                               border="cells", width=78)
        
        for name, skill in LOOKUP_DATA.skills.items():
            if category and skill.skill_type != category:
                continue
                
            # Color code by type
            if skill.skill_type == "mental":
                skill_name = f"|c{name.title().replace('_', ' ')}|n"
                skill_type = "|cMental|n"
            elif skill.skill_type == "physical":
                skill_name = f"|y{name.title().replace('_', ' ')}|n"
                skill_type = "|yPhysical|n"
            else:  # social
                skill_name = f"|m{name.title().replace('_', ' ')}|n"
                skill_type = "|mSocial|n"
            
            unskilled_penalty = f"{skill.unskilled}" if skill.unskilled else "0"
            description = get_skill_description(name)
            
            table.add_row(skill_name, skill_type, unskilled_penalty, description)
        
        title = f"|wCharacter Skills"
        if category:
            title += f" - {category.title()}"
        title += "|n"
        
        self.caller.msg(f"{title}\n{table}")
        self.caller.msg("\n|cNote:|n Skills start at 0 and can be raised to 5. Unskilled penalty applies when using a skill at 0 dots.")
    
    def show_merits(self, filter_arg=None):
        """Show merits, optionally filtered by type or template."""
        # Check if filter_arg is a merit type or template
        merit_types = ["mental", "physical", "social", "supernatural", "fighting", "style"]
        templates = ["vampire", "mage", "werewolf", "changeling", "geist", "demon", 
                    "deviant", "hunter", "mummy", "promethean", "mortal+", "mortal_plus", "general",
                    # Minor template types
                    "psychic", "ghoul", "dhampir", "atariya", "psychic_vampire", "psychic vampire"]
        
        merit_type = None
        template = None
        
        if filter_arg:
            filter_lower = filter_arg.lower()
            if filter_lower in merit_types:
                merit_type = filter_lower
            elif filter_lower in templates:
                template = filter_lower
            else:
                self.caller.msg(f"Unknown filter: {filter_arg}")
                self.caller.msg("|cValid types:|n mental, physical, social, supernatural, fighting, style")
                self.caller.msg("|cValid templates:|n vampire, mage, werewolf, changeling, geist, demon, deviant, hunter, mummy, promethean, mortal+")
                self.caller.msg("|cMinor templates:|n psychic, ghoul, dhampir, atariya, psychic_vampire")
                return
        
        table = evtable.EvTable("|wMerit|n", "|wType|n", "|wDots|n", "|wPrerequisites|n",
                               border="cells", width=78)
        
        # Get filtered merits
        filtered_merits = LOOKUP_DATA.get_merits_by_type(merit_type, template if template else 'general')
        
        for merit in filtered_merits:
            # Color code by type with accessibility symbols
            type_colors = {
                "mental": "|c", "physical": "|y", "social": "|m",
                "supernatural": "|r", "fighting": "|R", "style": "|g"
            }
            type_symbols = {
                "mental": "◆",      # Diamond for mental
                "physical": "■",    # Square for physical
                "social": "●",      # Circle for social
                "supernatural": "★", # Star for supernatural
                "fighting": "⚔",    # Swords for fighting
                "style": "◈"        # Diamond in square for style
            }
            color = type_colors.get(merit.merit_type, "|w")
            symbol = type_symbols.get(merit.merit_type, "○")
            
            merit_name = f"{color}{symbol} {merit.name}|n"
            merit_type_display = f"{color}{merit.merit_type.title()}|n"
            
            if merit.min_value == merit.max_value:
                dots = str(merit.min_value)
            else:
                dots = f"{merit.min_value}-{merit.max_value}"
            
            prereq = LOOKUP_DATA.format_prerequisites_display(merit.prerequisite)
            
            table.add_row(merit_name, merit_type_display, dots, prereq)
        
        # Format title with proper capitalization
        if template:
            template_display = template.replace('_', ' ').title()
        else:
            template_display = "General"
        
        title = f"|w{template_display} Merits"
        if merit_type:
            title += f" - {merit_type.title()}"
        title += f" ({len(filtered_merits)} total)|n"
        
        self.caller.msg(f"{title}\n{table}")
        
        # Add legend for symbols and colors
        legend = [
            "",
            "|wMerit Type Legend:|n",
            "  |c◆ Mental|n (Cyan)        |y■ Physical|n (Yellow)      |m● Social|n (Magenta)",
            "  |r★ Supernatural|n (Red)  |R⚔ Fighting|n (Bright Red)  |g◈ Style|n (Green)",
            ""
        ]
        self.caller.msg("\n".join(legend))
        
        self.caller.msg(f"|cUse:|n |y+lookup <merit_name>|n for detailed information on any merit.")
        self.caller.msg(f"|cFilters:|n +lookup merits <type> or +lookup merits <template>")
        self.caller.msg(f"  |yTypes:|n mental, physical, social, supernatural, fighting, style")
        self.caller.msg(f"  |yMajor Templates:|n vampire, mage, werewolf, changeling, geist, demon, hunter, etc.")
        self.caller.msg(f"  |yMinor Templates:|n psychic, ghoul, dhampir, atariya, psychic_vampire, mortal+")
    
    def show_vampire_merits(self):
        """Show vampire-specific merits (backward compatibility wrapper)."""
        self.show_merits("vampire")
    
    def show_disciplines(self):
        """Show vampire disciplines."""
        table = evtable.EvTable("|wDiscipline|n", "|wDescription|n", border="cells", width=78)
        
        for discipline in sorted(LOOKUP_DATA.vampire_data['disciplines']):
            desc = get_discipline_description(discipline)
            table.add_row(f"|r{discipline.title()}|n", desc)
        
        self.caller.msg(f"|wVampire Disciplines|n\n{table}")
        self.caller.msg(f"\n|cNote:|n Disciplines are supernatural powers available to vampires.")
    
    def show_arcana(self):
        """Show mage arcana."""
        table = evtable.EvTable("|wArcanum|n", "|wDescription|n", border="cells", width=78)
        
        for arcanum in sorted(LOOKUP_DATA.mage_data['arcana']):
            desc = get_arcanum_description(arcanum)
            table.add_row(f"|b{arcanum.title()}|n", desc)
        
        self.caller.msg(f"|wMage Arcana|n\n{table}")
        self.caller.msg(f"\n|cNote:|n Arcana are the spheres of magical influence available to mages.")
    
    def show_spells(self, arcana=None):
        """Show mage spells, optionally filtered by arcana."""
        from world.cofd.templates.mage_spells import ALL_MAGE_SPELLS, get_spells_by_arcana, get_spells_by_level
        
        if arcana:
            # Filter by arcana
            spells = get_spells_by_arcana(arcana)
            if not spells:
                self.caller.msg(f"No spells found for arcana: {arcana}")
                self.caller.msg("Valid arcana: death, time, fate, forces, life, matter, mind, prime, space, spirit")
                return
            
            title = f"|wMage Spells - {arcana.title()} Arcanum|n"
        else:
            spells = ALL_MAGE_SPELLS
            title = "|wAll Mage Spells|n"
        
        # Group spells by level
        spells_by_level = {1: [], 2: [], 3: [], 4: [], 5: []}
        for spell_key, spell_data in spells.items():
            spells_by_level[spell_data['level']].append((spell_key, spell_data))
        
        output = [title, ""]
        
        # Display spells organized by level
        for level in range(1, 6):
            level_spells = spells_by_level[level]
            if level_spells:
                dots = "●" * level
                output.append(f"|c{arcana.title() if arcana else 'Level'} {dots}|n")
                
                for spell_key, spell_data in sorted(level_spells, key=lambda x: x[1]['name']):
                    spell_name = spell_data['name']
                    practice = spell_data['practice']
                    
                    # Include arcana if showing all spells
                    if arcana:
                        output.append(f"  |y{spell_name}|n - {practice}")
                    else:
                        spell_arcana = spell_data['arcana'].title()
                        output.append(f"  |y{spell_name}|n ({spell_arcana}) - {practice}")
                    
                    # Add usage hint
                    output.append(f"    |gUse:|n +stat spell={spell_key}")
                
                output.append("")
        
        self.caller.msg("\n".join(output))
        
        if not arcana:
            self.caller.msg("|cFilter by arcana:|n +lookup spells death, +lookup spells forces, etc.")
        self.caller.msg("|cFor spell details:|n +lookup <spell_name> (e.g., +lookup telekinesis)")
    
    def show_spell_details(self, spell_key, spell_data):
        """Show detailed information about a specific spell."""
        msg = f"|w{spell_data['name']} (Mage Spell)|n\n"
        
        # Arcana and level
        arcana_name = spell_data['arcana'].title()
        spell_level = spell_data['level']
        dots = "●" * spell_level
        msg += f"|cArcana:|n {arcana_name} {dots}\n"
        
        # Secondary arcana if present
        if 'secondary_arcana' in spell_data and spell_data['secondary_arcana']:
            msg += f"|cSecondary Arcana:|n {spell_data['secondary_arcana']}\n"
        
        # Practice
        msg += f"|cPractice:|n {spell_data['practice']}\n"
        
        # Primary Factor
        msg += f"|cPrimary Factor:|n {spell_data['primary_factor']}\n"
        
        # Withstand
        if 'withstand' in spell_data and spell_data['withstand']:
            msg += f"|cWithstand:|n {spell_data['withstand']}\n"
        
        # Rote Skills
        if 'rote_skills' in spell_data and spell_data['rote_skills']:
            msg += f"|cRote Skills:|n {', '.join(spell_data['rote_skills'])}\n"
        
        # Description
        msg += f"|cDescription:|n {spell_data['description']}\n"
        
        # Source
        msg += f"|cSource:|n {spell_data['source']}\n"
        
        # Usage
        msg += f"\n|gTo add to character:|n +stat spell={spell_key}\n"
        
        self.caller.msg(msg)
    
    def show_endowment_details(self, endowment_key, endowment_data):
        """Show detailed information about a specific endowment."""
        msg = f"|w{endowment_data['name']} (Hunter Endowment)|n\n"
        
        # Type and Conspiracy
        endow_type = endowment_data.get('endowment_type', 'unknown').replace('_', ' ').title()
        msg += f"|cType:|n {endow_type}\n"
        
        conspiracy = endowment_data.get('conspiracy', 'Unknown')
        msg += f"|cConspiracy:|n {conspiracy}\n"
        
        # Cost
        if endowment_data.get('cost'):
            msg += f"|cCost:|n {endowment_data['cost']}\n"
        else:
            msg += f"|cCost:|n None\n"
        
        # Dice Pool
        if endowment_data.get('dice_pool'):
            msg += f"|cDice Pool:|n {endowment_data['dice_pool']}\n"
        
        # Action Type
        if endowment_data.get('action'):
            msg += f"|cAction:|n {endowment_data['action']}\n"
        
        # Duration
        if endowment_data.get('duration'):
            msg += f"|cDuration:|n {endowment_data['duration']}\n"
        
        # Loadout
        if endowment_data.get('loadout'):
            msg += f"|cLoadout:|n {endowment_data['loadout']}\n"
        
        # Target Successes
        if endowment_data.get('target_successes'):
            msg += f"|cTarget Successes:|n {endowment_data['target_successes']}\n"
        
        # Prerequisite
        if endowment_data.get('prerequisite'):
            msg += f"|cPrerequisite:|n {endowment_data['prerequisite']}\n"
        
        # Description
        msg += f"|cDescription:|n {endowment_data['description']}\n"
        
        # Tags
        if endowment_data.get('tags'):
            msg += f"|cTags:|n {', '.join(endowment_data['tags'])}\n"
        
        # Source
        msg += f"|cSource:|n {endowment_data['book']}\n"
        
        # Usage - endowments use spaces in their keys
        msg += f"\n|gTo add to character:|n +stat endowment={endowment_key}\n"
        
        self.caller.msg(msg)
    
    def show_clans(self):
        """Show vampire clans."""
        table = evtable.EvTable("|wClan|n", "|wDescription|n", border="cells", width=78)
        
        for clan in sorted(LOOKUP_DATA.vampire_data['clans']):
            desc = get_clan_description(clan)
            table.add_row(f"|r{clan.title()}|n", desc)
        
        self.caller.msg(f"|wVampire Clans|n\n{table}")
        self.caller.msg(f"\n|cNote:|n Clans determine a vampire's supernatural heritage and favored disciplines.")
    
    def show_covenants(self):
        """Show vampire covenants."""
        table = evtable.EvTable("|wCovenant|n", "|wDescription|n", border="cells", width=78)
        
        for covenant in sorted(LOOKUP_DATA.vampire_data['covenants']):
            desc = get_covenant_description(covenant)
            table.add_row(f"|r{covenant.title()}|n", desc)
        
        self.caller.msg(f"|wVampire Covenants|n\n{table}")
        self.caller.msg(f"\n|cNote:|n Covenants are political and religious organizations that vampires join.")
    
    def show_paths(self):
        """Show mage paths."""
        table = evtable.EvTable("|wPath|n", "|wRuling Arcana|n", "|wDescription|n", border="cells", width=78)
        
        for path in sorted(LOOKUP_DATA.mage_data['paths']):
            arcana, desc = get_path_info(path)
            table.add_row(f"|b{path.title()}|n", f"|c{arcana}|n", desc)
        
        self.caller.msg(f"|wMage Paths|n\n{table}")
        self.caller.msg(f"\n|cNote:|n Paths determine a mage's approach to magic and ruling arcana.")
    
    def show_orders(self):
        """Show mage orders."""
        table = evtable.EvTable("|wOrder|n", "|wDescription|n", border="cells", width=78)
        
        for order in sorted(LOOKUP_DATA.mage_data['orders']):
            desc = get_order_description(order)
            table.add_row(f"|b{order.title()}|n", desc)
        
        self.caller.msg(f"|wMage Orders|n\n{table}")
        self.caller.msg(f"\n|cNote:|n Orders are political and philosophical organizations that mages join.")
    
    def show_templates(self):
        """Show character templates."""
        table = evtable.EvTable("|wTemplate|n", "|wDescription|n", border="cells", width=78)
        
        templates = ["mortal", "mortal+", "vampire", "mage", "werewolf", "changeling", 
                    "demon", "geist", "promethean", "hunter", "mummy", "deviant"]
        
        for template in templates:
            desc = get_template_description(template)
            if template in ["mortal", "mortal+"]:
                color = "|w"
            else:
                color = "|y"
            table.add_row(f"{color}{template.title()}|n", desc)
        
        self.caller.msg(f"|wCharacter Templates|n\n{table}")
        self.caller.msg(f"\n|cNote:|n Templates determine your character's supernatural nature and abilities.")
    
    def show_stat_details(self, stat_name):
        """Show detailed information about a specific stat."""
        # First check if it's a spell
        from world.cofd.templates.mage_spells import get_spell
        
        spell_key = stat_name.lower().replace(" ", "_")
        spell_data = get_spell(spell_key)
        
        if spell_data:
            self.show_spell_details(spell_key, spell_data)
            return
        
        # Check if it's an endowment (keep spaces for endowment lookup)
        from world.cofd.templates.hunter_endowments import get_endowment
        
        endowment_key = stat_name.lower()  # Keep spaces for endowments
        endowment_data = get_endowment(endowment_key)
        
        if endowment_data:
            self.show_endowment_details(endowment_key, endowment_data)
            return
        
        result = LOOKUP_DATA.find_stat(stat_name)
        
        if not result:
            self.caller.msg(f"No stat found matching '{stat_name}'. Use |y+lookup|n to see available categories.")
            return
        
        stat_type, stat_data = result
        
        if stat_type == 'attribute':
            msg = f"|w{stat_data.name.title()} (Attribute)|n\n"
            msg += f"|cType:|n {stat_data.att_type.title()}\n"
            msg += f"|cRange:|n {stat_data.min_value}-{stat_data.max_value}\n"
            msg += f"|cDescription:|n {get_attribute_description(stat_data.name)}\n"
            
        elif stat_type == 'skill':
            msg = f"|w{stat_data.name.title().replace('_', ' ')} (Skill)|n\n"
            msg += f"|cType:|n {stat_data.skill_type.title()}\n"
            msg += f"|cRange:|n {stat_data.min_value}-{stat_data.max_value}\n"
            if stat_data.unskilled:
                msg += f"|cUnskilled Penalty:|n {stat_data.unskilled}\n"
            msg += f"|cDescription:|n {get_skill_description(stat_data.name)}\n"
            
        elif stat_type == 'merit':
            msg = f"|w{stat_data.name} (Merit)|n\n"
            msg += f"|cType:|n {stat_data.merit_type.title()}\n"
            if stat_data.min_value == stat_data.max_value:
                msg += f"|cCost:|n {stat_data.min_value} dots\n"
            else:
                msg += f"|cCost:|n {stat_data.min_value}-{stat_data.max_value} dots\n"
            msg += f"|cPrerequisites:|n {LOOKUP_DATA.format_prerequisites_display(stat_data.prerequisite)}\n"
            msg += f"|cDescription:|n {stat_data.description}\n"
            
        elif stat_type == 'advantage':
            msg = f"|w{stat_data.name.title()} (Advantage)|n\n"
            msg += f"|cRange:|n {stat_data.min_value}-{stat_data.max_value}\n"
            msg += f"|cBase Calculation:|n {stat_data.adv_base}\n"
            msg += f"|cDescription:|n Derived stat calculated from other attributes\n"
            
        elif stat_type == 'anchor':
            msg = f"|w{stat_data.name.title()} (Anchor)|n\n"
            msg += f"|cDescription:|n Core personality trait that defines the character\n"
        
        self.caller.msg(msg)
    
    def show_transmutations(self):
        """Show promethean transmutations."""
        table = evtable.EvTable("|wTransmutation|n", "|wDescription|n", border="cells", width=78)
        
        transmutation_descriptions = {
            "alchemicus": "Mastery over matter and transformation",
            "benefice": "Powers of the Throng - cooperative abilities",
            "contamination": "Powers of emotional and social corruption",
            "corporeum": "Physical enhancement and athletic prowess",
            "deception": "Powers of concealment and disguise",
            "disquietism": "Mastery over Disquiet and Flux",
            "electrification": "Control over electricity and lightning",
            "flux": "Dark powers of the Wasteland (dangerous)",
            "luciferus": "Powers of radiance and inspiration",
            "metamorphosis": "Shapeshifting and physical transformation",
            "mesmerism": "Powers of emotional manipulation",
            "saturninus": "Powers of Azothic memory and Pyros",
            "sensorium": "Enhanced senses and perception",
            "spiritus": "Powers against supernatural threats",
            "vitality": "Powers of endurance and strength",
            "vulcanus": "Powers of the Divine Fire"
        }
        
        for transmutation in sorted(LOOKUP_DATA.promethean_data['transmutations']):
            desc = transmutation_descriptions.get(transmutation, "Promethean supernatural power")
            table.add_row(f"|g{transmutation.title()}|n", desc)
        
        self.caller.msg(f"|wPromethean Transmutations|n\n{table}")
        self.caller.msg(f"\n|cNote:|n Use |y+lookup alembics|n to see individual Alembics within each Transmutation.")
    
    def show_alembics(self):
        """Show promethean alembics organized by transmutation."""
        msg = f"|wPromethean Alembics (by Transmutation)|n\n\n"
        
        alembics_dict = LOOKUP_DATA.promethean_data['alembics']
        
        for transmutation in sorted(alembics_dict.keys()):
            alembics = sorted(alembics_dict[transmutation])
            msg += f"|g{transmutation.title()}:|n\n"
            msg += "  " + ", ".join([a.replace('_', ' ').title() for a in alembics]) + "\n\n"
        
        msg += f"|cTotal:|n {sum(len(a) for a in alembics_dict.values())} individual Alembics\n"
        msg += f"\n|cNote:|n Alembics are individual powers, not rated by dots. Set with:\n"
        msg += "|y+stat alembic=<alembic_name>|n (e.g., +stat alembic=human_flesh)"
        
        self.caller.msg(msg)
    
    def show_bestowments(self):
        """Show promethean bestowments."""
        msg = f"|wPromethean Bestowments|n\n\n"
        msg += "Bestowments are unique gifts tied to a Promethean's Lineage:\n\n"
        
        bestowments = sorted([b.lower().replace(" ", "_") for b in LOOKUP_DATA.promethean_data['bestowments']])
        
        # Display in columns
        col_width = 30
        for i in range(0, len(bestowments), 3):
            row = bestowments[i:i+3]
            msg += "  " + "".join([f"|y{b.replace('_', ' ').title():<{col_width}}|n" for b in row]) + "\n"
        
        msg += f"\n|cTotal:|n {len(bestowments)} Bestowments\n"
        msg += f"\n|cNote:|n Set with: |y+stat bestowment=<name>|n (e.g., +stat bestowment=spare_parts)"
        
        self.caller.msg(msg)
    
    def show_lineages(self):
        """Show promethean lineages."""
        table = evtable.EvTable("|wLineage|n", "|wDescription|n", border="cells", width=78)
        
        lineage_descriptions = {
            "frankenstein": "Created from corpses, the Wretched, driven by loneliness",
            "galatea": "Sculpted from unblemished forms, the Muses, seekers of beauty",
            "osiris": "Assembled from disparate parts, the Redeemed, guardians of the dead",
            "tammuz": "Formed from clay or earth, the Golem, seeking purpose",
            "ulgan": "Crafted from the remains of shamans, the Pilgrims, spiritual travelers",
            "extempore": "Spontaneously created Prometheans, rare and unpredictable",
            "unfleshed": "Prometheans without physical form, ethereal and strange",
            "zeka": "Created from metal and machine parts, the Manufactured"
        }
        
        for lineage in sorted(LOOKUP_DATA.promethean_data['lineages']):
            desc = lineage_descriptions.get(lineage, "Promethean lineage")
            table.add_row(f"|g{lineage.title()}|n", desc)
        
        self.caller.msg(f"|wPromethean Lineages|n\n{table}")
        self.caller.msg(f"\n|cNote:|n Set with: |y+stat lineage=<name>|n")
    
    def show_athanors(self):
        """Show promethean athanors organized by lineage."""
        msg = f"|wPromethean Athanors (by Lineage)|n\n\n"
        msg += "Athanors are the spiritual engines that drive the Pilgrimage:\n\n"
        
        athanors_dict = LOOKUP_DATA.promethean_data['athanors']
        
        for lineage in sorted(athanors_dict.keys()):
            athanors = sorted(athanors_dict[lineage])
            msg += f"|g{lineage.title()}:|n\n"
            msg += "  " + ", ".join([a.replace('_', ' ').title() for a in athanors]) + "\n\n"
        
        msg += f"\n|cNote:|n Set with: |y+stat athanor=<name>|n (requires matching Lineage)\n"
        msg += "Example: |y+stat lineage=Frankenstein|n then |y+stat athanor=Basilisk|n"
        
        self.caller.msg(msg)

    def show_endowments(self, endowment_type=None):
        """Show hunter endowments, optionally filtered by type."""
        from world.cofd.templates.hunter_endowments import get_all_endowments, get_endowments_by_type
        
        if endowment_type:
            # Filter by type
            endowments = get_endowments_by_type(endowment_type)
            if not endowments:
                self.caller.msg(f"No endowments found for type: {endowment_type}")
                self.caller.msg("|cValid types:|n advanced_armory, animal_control_kit, benediction, castigation, dreamscape, elixir, enkoimesis, goetic_gospel, horror_within, infusion, ink, inspiration, lives_remembered, perispiritism, relic, rites_du_cheval, rites_of_denial, seitokuten, teleinformatics, thaumatechnology, xenotechnology")
                return
            
            title = f"|wHunter Endowments - {endowment_type.replace('_', ' ').title()}|n"
        else:
            endowments = get_all_endowments()
            title = "|wAll Hunter Endowments|n"
        
        # Group endowments by type if showing all
        if endowment_type:
            output = [title, ""]
            for endow_key, endow_data in sorted(endowments.items(), key=lambda x: x[1]['name']):
                endow_name = endow_data['name']
                conspiracy = endow_data.get('conspiracy', 'Unknown')
                
                output.append(f"  |y{endow_name}|n")
                output.append(f"    Conspiracy: {conspiracy}")
                output.append(f"    |gUse:|n +stat endowment={endow_key}")
                output.append("")
        else:
            # Group by endowment type
            endowments_by_type = {}
            for endow_key, endow_data in endowments.items():
                e_type = endow_data.get('endowment_type', 'other')
                if e_type not in endowments_by_type:
                    endowments_by_type[e_type] = []
                endowments_by_type[e_type].append((endow_key, endow_data['name']))
            
            output = [title, ""]
            for e_type in sorted(endowments_by_type.keys()):
                output.append(f"|c{e_type.replace('_', ' ').title()}:|n")
                endow_list = sorted(endowments_by_type[e_type], key=lambda x: x[1])
                count = len(endow_list)
                output.append(f"  {count} endowments available")
                output.append(f"  |gView all:|n +lookup endowments {e_type}")
                output.append("")
        
        self.caller.msg("\n".join(output))
        
        if not endowment_type:
            self.caller.msg("|cFilter by type:|n +lookup endowments benediction, +lookup endowments castigation, etc.")
        self.caller.msg("|cFor endowment details:|n +lookup <endowment_name> (e.g., +lookup hellfire)")
    
    def show_auspices(self):
        """Show werewolf auspices."""
        from evennia.utils import evtable
        table = evtable.EvTable("|wAuspice|n", "|wDescription|n", border="cells", width=78)
        
        auspice_descriptions = {
            "cahalith": "The Gibbous Moon, visionaries and lorekeepers",
            "elodoth": "The Half Moon, judges and mediators",
            "irraka": "The New Moon, scouts and tricksters",
            "ithaeur": "The Crescent Moon, spirit-talkers and shamans",
            "rahu": "The Full Moon, warriors and protectors"
        }
        
        for auspice in sorted(LOOKUP_DATA.werewolf_data['auspices']):
            desc = auspice_descriptions.get(auspice, "Werewolf moon-sign")
            table.add_row(f"|y{auspice.title()}|n", desc)
        
        self.caller.msg(f"|wWerewolf Auspices|n\n{table}")
        self.caller.msg(f"\n|cNote:|n Auspices determine a werewolf's role and moon-gifts.")
    
    def show_tribes(self):
        """Show werewolf tribes."""
        from evennia.utils import evtable
        table = evtable.EvTable("|wTribe|n", "|wDescription|n", border="cells", width=78)
        
        tribe_descriptions = {
            "blood talons": "Warriors who glory in battle and honor",
            "bone shadows": "Death-speakers who police the spirit world",
            "hunters in darkness": "Territorial guardians of sacred places",
            "iron masters": "Adaptable survivors who embrace civilization",
            "storm lords": "Noble leaders who command respect",
            "ghost wolves": "Tribal outcasts who follow no pack"
        }
        
        for tribe in sorted(LOOKUP_DATA.werewolf_data['tribes']):
            desc = tribe_descriptions.get(tribe, "Werewolf tribe")
            table.add_row(f"|y{tribe.title()}|n", desc)
        
        self.caller.msg(f"|wWerewolf Tribes|n\n{table}")
        self.caller.msg(f"\n|cNote:|n Tribes determine a werewolf's culture and tribal gifts.")
    
    def show_seemings(self):
        """Show changeling seemings."""
        from evennia.utils import evtable
        table = evtable.EvTable("|wSeeming|n", "|wDescription|n", border="cells", width=78)
        
        seeming_descriptions = {
            "beast": "Animal-like changelings with feral instincts",
            "darkling": "Shadow-touched changelings who lurk in darkness",
            "elemental": "Changelings infused with primal forces",
            "fairest": "Beautiful changelings of devastating presence",
            "ogre": "Brutal changelings of terrifying strength",
            "wizened": "Crafty changelings of supernatural skill"
        }
        
        for seeming in sorted(LOOKUP_DATA.changeling_data['seemings']):
            desc = seeming_descriptions.get(seeming, "Changeling seeming")
            table.add_row(f"|m{seeming.title()}|n", desc)
        
        self.caller.msg(f"|wChangeling Seemings|n\n{table}")
        self.caller.msg(f"\n|cNote:|n Seemings reflect how the Fae transformed a changeling.")
    
    def show_courts(self):
        """Show changeling courts."""
        from evennia.utils import evtable
        table = evtable.EvTable("|wCourt|n", "|wDescription|n", border="cells", width=78)
        
        court_descriptions = {
            "spring": "The Emerald Court of desire and new beginnings",
            "summer": "The Crimson Court of wrath and iron resolve",
            "autumn": "The Leaden Court of fear and sorcerous power",
            "winter": "The Onyx Court of sorrow and cold logic",
            "courtless": "Independent changelings who reject court politics"
        }
        
        for court in sorted(LOOKUP_DATA.changeling_data['courts']):
            desc = court_descriptions.get(court, "Changeling court")
            table.add_row(f"|m{court.title()}|n", desc)
        
        self.caller.msg(f"|wChangeling Courts|n\n{table}")
        self.caller.msg(f"\n|cNote:|n Courts are seasonal political factions among the Lost.")
    
    def show_incarnations(self):
        """Show demon incarnations."""
        from evennia.utils import evtable
        table = evtable.EvTable("|wIncarnation|n", "|wDescription|n", border="cells", width=78)
        
        incarnation_descriptions = {
            "destroyer": "Angels of destruction and apocalypse",
            "guardian": "Angels of protection and defense",
            "messenger": "Angels of communication and knowledge",
            "psychopomp": "Angels of death and transition"
        }
        
        for incarnation in sorted(LOOKUP_DATA.demon_data['incarnations']):
            desc = incarnation_descriptions.get(incarnation, "Demon incarnation")
            table.add_row(f"|r{incarnation.title()}|n", desc)
        
        self.caller.msg(f"|wDemon Incarnations|n\n{table}")
        self.caller.msg(f"\n|cNote:|n Incarnations reflect a demon's original angelic function.")
    
    def show_agendas(self):
        """Show demon agendas."""
        from evennia.utils import evtable
        table = evtable.EvTable("|wAgenda|n", "|wDescription|n", border="cells", width=78)
        
        agenda_descriptions = {
            "inquisitor": "Seeking to understand the God-Machine",
            "integrator": "Attempting to live among humans",
            "saboteur": "Working to destroy the God-Machine",
            "tempter": "Corrupting humans for their own ends"
        }
        
        for agenda in sorted(LOOKUP_DATA.demon_data['agendas']):
            desc = agenda_descriptions.get(agenda, "Demon agenda")
            table.add_row(f"|r{agenda.title()}|n", desc)
        
        self.caller.msg(f"|wDemon Agendas|n\n{table}")
        self.caller.msg(f"\n|cNote:|n Agendas define a demon's goals in their new existence.")
    
    def show_embeds(self):
        """Show demon embeds."""
        msg = f"|wDemon Embeds|n\n\n"
        msg += "Embeds are intrinsic demonic powers tied to their former nature:\n\n"
        
        embeds = sorted([e.lower().replace(" ", "_") for e in LOOKUP_DATA.demon_data['embeds']])
        
        # Display in columns
        col_width = 30
        for i in range(0, len(embeds), 3):
            row = embeds[i:i+3]
            msg += "  " + "".join([f"|r{e.replace('_', ' ').title():<{col_width}}|n" for e in row]) + "\n"
        
        msg += f"\n|cTotal:|n {len(embeds)} Embeds\n"
        msg += f"\n|cNote:|n Set with: |y+stat embed=<name>|n"
        
        self.caller.msg(msg)
    
    def show_exploits(self):
        """Show demon exploits."""
        msg = f"|wDemon Exploits|n\n\n"
        msg += "Exploits are learned demonic powers that manipulate reality:\n\n"
        
        exploits = sorted([e.lower().replace(" ", "_") for e in LOOKUP_DATA.demon_data['exploits']])
        
        # Display in columns
        col_width = 30
        for i in range(0, len(exploits), 3):
            row = exploits[i:i+3]
            msg += "  " + "".join([f"|r{e.replace('_', ' ').title():<{col_width}}|n" for e in row]) + "\n"
        
        msg += f"\n|cTotal:|n {len(exploits)} Exploits\n"
        msg += f"\n|cNote:|n Set with: |y+stat exploit=<name>|n"
        
        self.caller.msg(msg)

    def show_guilds(self):
        """Show mummy guilds."""
        from evennia.utils import evtable
        table = evtable.EvTable("|wGuild|n", "|wDescription|n", border="cells", width=78)
        
        guild_descriptions = {
            "mesen-nebu": "The Watchers, prophets and scholars who preserve knowledge",
            "sesha-hebsu": "The Scribes, ritualists and spellcasters who wield utterances",
            "su-menent": "The Shepherds, leaders and guides who protect the living",
            "tef-aabhi": "The Judges, warriors and executioners who enforce ma'at",
            "amenti": "Independent mummies with no guild affiliation"
        }
        
        for guild in sorted(LOOKUP_DATA.mummy_data['guilds']):
            desc = guild_descriptions.get(guild, "Mummy guild")
            table.add_row(f"|y{guild.title().replace('-', ' ')}|n", desc)
        
        self.caller.msg(f"|wMummy Guilds|n\n{table}")
        self.caller.msg(f"\n|cNote:|n Guilds determine a mummy's role and abilities.")
    
    def show_decrees(self):
        """Show mummy decrees."""
        from evennia.utils import evtable
        table = evtable.EvTable("|wDecree|n", "|wDescription|n", border="cells", width=78)
        
        decree_descriptions = {
            "balance": "Maintain ma'at and cosmic equilibrium",
            "fortune": "Bring prosperity and good fortune to the cult",
            "knowledge": "Preserve and protect ancient wisdom",
            "protection": "Shield the cult from supernatural threats",
            "vengeance": "Strike down enemies of the Judges"
        }
        
        for decree in sorted(LOOKUP_DATA.mummy_data['decrees']):
            desc = decree_descriptions.get(decree, "Mummy decree")
            table.add_row(f"|y{decree.title()}|n", desc)
        
        self.caller.msg(f"|wMummy Decrees|n\n{table}")
        self.caller.msg(f"\n|cNote:|n Decrees define a mummy's mission from the Judges.")
    
    def show_judges(self):
        """Show mummy judges."""
        from evennia.utils import evtable
        table = evtable.EvTable("|wJudge|n", "|wDescription|n", border="cells", width=78)
        
        judge_descriptions = {
            "djehuty": "The Ibis-Headed, god of wisdom and magic (Thoth)",
            "duamutef": "The Jackal-Headed, son of Horus, protector of the stomach",
            "hapi": "The Baboon-Headed, son of Horus, protector of the lungs",
            "imsety": "The Human-Headed, son of Horus, protector of the liver",
            "kebehsenuf": "The Falcon-Headed, son of Horus, protector of intestines",
            "nehebkau": "The Serpent, primordial guardian of the gates",
            "neith": "The Weaver, goddess of war and wisdom",
            "ptah": "The Craftsman, god of creation and artisans",
            "sobek": "The Crocodile, god of the Nile and military prowess"
        }
        
        for judge in sorted(LOOKUP_DATA.mummy_data['judges']):
            desc = judge_descriptions.get(judge, "Mummy judge")
            table.add_row(f"|y{judge.title()}|n", desc)
        
        self.caller.msg(f"|wMummy Judges|n\n{table}")
        self.caller.msg(f"\n|cNote:|n Judges are the gods who command mummies in Duat.")
    
    def show_utterances(self):
        """Show mummy utterances."""
        msg = f"|wMummy Utterances|n\n\n"
        msg += "Utterances are supernatural powers granted by Sekhem:\n\n"
        
        utterance_descriptions = {
            "afire": "Powers of flame and destruction",
            "bone": "Powers over death and the dead",
            "elements": "Control over the natural elements",
            "flesh": "Mastery of the body and healing",
            "guidance": "Insight and foresight",
            "glory": "Commanding presence and authority",
            "reign": "Leadership and dominion",
            "vision": "Enhanced perception and awareness",
            "word": "Power of command and compulsion"
        }
        
        for utterance in sorted(LOOKUP_DATA.mummy_data['utterances']):
            desc = utterance_descriptions.get(utterance, "Mummy utterance")
            msg += f"  |y{utterance.title():<15}|n - {desc}\n"
        
        msg += f"\n|cNote:|n Set with: |y+stat utterance=<name>|n (rated 1-5 dots)"
        self.caller.msg(msg)
    
    def show_affinities(self):
        """Show mummy affinities."""
        msg = f"|wMummy Affinities|n\n\n"
        msg += "Affinities represent the nine souls of Egyptian belief:\n\n"
        
        affinity_descriptions = {
            "ab": "The heart, seat of emotion and will",
            "ba": "The personality and individuality",
            "ka": "The life force and vital essence",
            "khaibit": "The shadow, darker aspects",
            "khat": "The physical body",
            "ren": "The secret name and identity",
            "sahu": "The spiritual body",
            "sekhem": "The power and life energy",
            "sheut": "The shadow-self in the underworld"
        }
        
        for affinity in sorted(LOOKUP_DATA.mummy_data['affinities']):
            desc = affinity_descriptions.get(affinity, "Mummy affinity")
            msg += f"  |y{affinity.title():<15}|n - {desc}\n"
        
        msg += f"\n|cNote:|n Set with: |y+stat affinity=<name>|n (rated 1-5 dots)"
        self.caller.msg(msg)
    
    def show_burdens(self):
        """Show geist burdens."""
        from evennia.utils import evtable
        table = evtable.EvTable("|wBurden|n", "|wDescription|n", border="cells", width=78)
        
        burden_descriptions = {
            "abiding": "Died lingering, unable to let go",
            "bereaved": "Died mourning, with unfinished grief",
            "hungry": "Died starving or craving",
            "kindly": "Died peacefully, accepting death",
            "vengeful": "Died angry, with unfinished business"
        }
        
        for burden in sorted(LOOKUP_DATA.geist_data['burdens']):
            desc = burden_descriptions.get(burden, "Geist burden")
            table.add_row(f"|m{burden.title()}|n", desc)
        
        self.caller.msg(f"|wGeist Burdens|n\n{table}")
        self.caller.msg(f"\n|cNote:|n Burdens define how a Sin-Eater died.")
    
    def show_krewe_types(self):
        """Show geist krewe types."""
        from evennia.utils import evtable
        table = evtable.EvTable("|wKrewe Type|n", "|wDescription|n", border="cells", width=78)
        
        krewe_descriptions = {
            "family": "Close-knit group bound by personal ties",
            "industrial": "Organized like a corporation or business",
            "network": "Loose association of independent agents",
            "military": "Hierarchical command structure",
            "academic": "Focused on research and knowledge"
        }
        
        for krewe in sorted(LOOKUP_DATA.geist_data['krewe_types']):
            desc = krewe_descriptions.get(krewe, "Krewe type")
            table.add_row(f"|m{krewe.title()}|n", desc)
        
        self.caller.msg(f"|wGeist Krewe Types|n\n{table}")
        self.caller.msg(f"\n|cNote:|n Krewes are groups of Sin-Eaters working together.")
    
    def show_haunts(self):
        """Show geist haunts (manifestations)."""
        msg = f"|wGeist Haunts (Manifestations)|n\n\n"
        msg += "Haunts are supernatural powers rated 1-5 dots:\n\n"
        
        haunt_descriptions = {
            "boneyard": "Control over death and decay",
            "caul": "Protection and defensive abilities",
            "curse": "Inflicting misfortune and harm",
            "dirge": "Manipulating emotion and perception",
            "marionette": "Controlling bodies and actions",
            "memoria": "Accessing memories and the past",
            "oracle": "Perceiving the future and hidden truths",
            "rage": "Destructive and offensive power",
            "shroud": "Concealment and stealth",
            "tomb": "Manipulating the physical world"
        }
        
        for haunt in sorted(LOOKUP_DATA.geist_data['haunts']):
            desc = haunt_descriptions.get(haunt, "Geist haunt")
            msg += f"  |m{haunt.title():<15}|n - {desc}\n"
        
        msg += f"\n|cNote:|n Set with: |y+stat <haunt>=<1-5>|n (e.g., +stat boneyard=3)"
        self.caller.msg(msg)
    
    def show_keys(self):
        """Show geist keys."""
        msg = f"|wGeist Keys|n\n\n"
        msg += "Keys unlock and enhance manifestations in specific situations:\n\n"
        
        for key in sorted(LOOKUP_DATA.geist_data['keys']):
            msg += f"  |m{key.title().replace('_', ' '):<15}|n - The Key of {key.title().replace('_', ' ')}\n"
        
        msg += f"\n|cTotal:|n {len(LOOKUP_DATA.geist_data['keys'])} Keys\n"
        msg += f"\n|cNote:|n Set with: |y+stat key=<name>|n (e.g., +stat key=cold_wind)"
        self.caller.msg(msg)
    
    def show_ceremonies(self):
        """Show geist ceremonies."""
        msg = f"|wGeist Ceremonies|n\n\n"
        msg += "Ceremonies are rituals Sin-Eaters can perform:\n\n"
        
        ceremonies = sorted([c.replace('_', ' ').title() for c in LOOKUP_DATA.geist_data['ceremonies']])
        
        # Display in columns
        col_width = 30
        for i in range(0, len(ceremonies), 2):
            row = ceremonies[i:i+2]
            msg += "  " + "".join([f"|m{c:<{col_width}}|n" for c in row]) + "\n"
        
        msg += f"\n|cTotal:|n {len(ceremonies)} Ceremonies\n"
        msg += f"\n|cNote:|n Set with: |y+stat ceremony=<name>|n"
        self.caller.msg(msg)
    
    def show_origins(self):
        """Show deviant origins."""
        from evennia.utils import evtable
        table = evtable.EvTable("|wOrigin|n", "|wDescription|n", border="cells", width=78)
        
        origin_descriptions = {
            "cephalist": "Created by mad scientists and reality hackers",
            "cheiron group": "Experimented on by the supernatural hunting corporation",
            "government": "Products of black ops and secret military programs",
            "pentex": "Created by the corrupt megacorporation",
            "seers of the throne": "Twisted by servants of the Exarchs",
            "technocracy": "Remade by reality engineers and techno-mages"
        }
        
        for origin in sorted(LOOKUP_DATA.deviant_data['origins']):
            desc = origin_descriptions.get(origin, "Deviant origin")
            table.add_row(f"|c{origin.title()}|n", desc)
        
        self.caller.msg(f"|wDeviant Origins|n\n{table}")
        self.caller.msg(f"\n|cNote:|n Origins define who created or transformed the Deviant.")
    
    def show_clades(self):
        """Show deviant clades."""
        from evennia.utils import evtable
        table = evtable.EvTable("|wClade|n", "|wDescription|n", border="cells", width=78)
        
        clade_descriptions = {
            "coactive": "Multiple beings merged into one",
            "devoted": "Transformed through sacrifice and dedication",
            "genotypal": "Genetically engineered or mutated",
            "invasive": "Invaded by foreign elements",
            "mutant": "Spontaneously evolved or changed",
            "pelagic": "Transformed by deep and alien forces",
            "remnant": "Rebuilt from death or destruction"
        }
        
        for clade in sorted(LOOKUP_DATA.deviant_data['clades']):
            desc = clade_descriptions.get(clade, "Deviant clade")
            table.add_row(f"|c{clade.title()}|n", desc)
        
        self.caller.msg(f"|wDeviant Clades|n\n{table}")
        self.caller.msg(f"\n|cNote:|n Clades define how a Deviant was transformed.")
    
    def show_variations(self):
        """Show deviant variations."""
        msg = f"|wDeviant Variations|n\n\n"
        msg += "Variations are categories of deviant powers:\n\n"
        
        variation_descriptions = {
            "biological": "Powers of flesh, bone, and organic matter",
            "cybernetic": "Technological augmentations and implants",
            "energy": "Control over various forms of energy",
            "mental": "Psychic and cognitive abilities",
            "physical": "Enhanced strength, speed, and durability",
            "sensory": "Superhuman perception and awareness",
            "temporal": "Manipulation of time and causality"
        }
        
        for variation in sorted(LOOKUP_DATA.deviant_data['variations']):
            desc = variation_descriptions.get(variation, "Deviant variation")
            msg += f"  |c{variation.title():<15}|n - {desc}\n"
        
        msg += f"\n|cNote:|n Variations determine the type of deviant powers."
        self.caller.msg(msg)
    
    def show_adaptations(self):
        """Show deviant adaptations."""
        msg = f"|wDeviant Adaptations|n\n\n"
        msg += "Adaptations are specific deviant powers:\n\n"
        
        adaptation_descriptions = {
            "defensive": "Protective abilities and resistances",
            "environmental": "Adaptation to extreme conditions",
            "locomotion": "Enhanced movement capabilities",
            "offensive": "Combat and attack powers",
            "sensory": "Enhanced or unusual senses",
            "social": "Abilities affecting interaction",
            "utility": "Versatile and practical powers"
        }
        
        for adaptation in sorted(LOOKUP_DATA.deviant_data['adaptations']):
            desc = adaptation_descriptions.get(adaptation, "Deviant adaptation")
            msg += f"  |c{adaptation.title():<15}|n - {desc}\n"
        
        msg += f"\n|cNote:|n Set with: |y+stat adaptation=<name>|n"
        self.caller.msg(msg)
    
    def show_mortal_plus_types(self):
        """Show mortal+ types."""
        msg = f"|wMortal+ Types|n\n\n"
        msg += "Mortal+ includes all minor supernatural templates:\n\n"
        
        types = sorted(LOOKUP_DATA.mortal_plus_data['types'])
        
        # Display in columns
        col_width = 26
        for i in range(0, len(types), 3):
            row = types[i:i+3]
            msg += "  " + "".join([f"|w{t:<{col_width}}|n" for t in row]) + "\n"
        
        msg += f"\n|cTotal:|n {len(types)} Mortal+ Types\n"
        msg += f"\n|cNote:|n Use |y+stat template_type=<type>|n to set your mortal+ type"
        self.caller.msg(msg)
    
    def show_psychic_powers(self):
        """Show psychic powers."""
        msg = f"|wPsychic Powers|n\n\n"
        msg += "Psychic powers available to mortal+ psychics:\n\n"
        
        powers = sorted([p.title() for p in LOOKUP_DATA.mortal_plus_data['psychic_powers']])
        
        # Display in two columns
        col_width = 26
        for i in range(0, len(powers), 3):
            row = powers[i:i+3]
            msg += "  " + "".join([f"|c{p:<{col_width}}|n" for p in row]) + "\n"
        
        msg += f"\n|cTotal:|n {len(powers)} Psychic Powers\n"
        msg += f"\n|cNote:|n Set with: |y+stat psychic=<power>|n (e.g., +stat psychic=telepathy)"
        self.caller.msg(msg)
    
    def show_gutter_magic(self):
        """Show gutter magic types for witches (2e)."""
        from evennia.utils import evtable
        table = evtable.EvTable("|wGutter Magic Type|n", "|wDescription|n", border="cells", width=78)
        
        magic_descriptions = {
            "curses": "Hexes, jinxes, and maledictions",
            "divination": "Fortune telling, scrying, and reading signs",
            "healing": "Folk remedies, herbalism, and natural cures",
            "warding": "Protective charms, wards, and abjurations",
            "brewing": "Potions, elixirs, and magical concoctions",
            "binding": "Ritual bindings and compulsions"
        }
        
        for magic_type in sorted(LOOKUP_DATA.mortal_plus_data['gutter_magic_types']):
            desc = magic_descriptions.get(magic_type, "Gutter magic type")
            table.add_row(f"|m{magic_type.title()}|n", desc)
        
        self.caller.msg(f"|wGutter Magic Types (2e Witches)|n\n{table}")
        self.caller.msg(f"\n|cNote:|n Gutter Magic replaces 1e Thaumaturgy in 2nd Edition.")
        self.caller.msg(f"Set with: |y+stat gutter_magic=<type>|n")
    
    def show_wolf_blooded_tells(self):
        """Show wolf-blooded tells (2e)."""
        from evennia.utils import evtable
        table = evtable.EvTable("|wTell Category|n", "|wDescription|n", border="cells", width=78)
        
        tell_descriptions = {
            "moon_gift": "Powers that manifest based on moon phase",
            "pack_awareness": "Sense other Wolf-Blooded and werewolves",
            "territorial": "Enhanced abilities in claimed territory",
            "spirit_sight": "Ability to perceive the Shadow Realm",
            "primal": "Enhanced physical traits and instincts"
        }
        
        for tell in sorted(LOOKUP_DATA.mortal_plus_data['wolf_blooded_tells']):
            desc = tell_descriptions.get(tell, "Wolf-Blooded tell")
            table.add_row(f"|y{tell.replace('_', ' ').title()}|n", desc)
        
        self.caller.msg(f"|wWolf-Blooded Tells (2e)|n\n{table}")
        self.caller.msg(f"\n|cNote:|n Tells are inherited traits from werewolf ancestry.")
        self.caller.msg(f"Set with: |y+stat tell=<name>|n")
    
    def show_specialties(self, skill=None):
        """Show skill specialties, optionally filtered by skill."""
        if skill:
            # Show specialties for a specific skill
            skill = skill.lower().replace(" ", "_")
            if skill not in LOOKUP_DATA.specialties:
                self.caller.msg(f"No specialties found for '{skill}'.")
                self.caller.msg(f"Use |y+lookup specialties|n to see all available skills with specialties.")
                return
            
            specialties = LOOKUP_DATA.specialties[skill]
            msg = f"|w{skill.title().replace('_', ' ')} Specialties|n\n\n"
            msg += f"|cSuggested Specialties:|n\n"
            msg += "  " + ", ".join(specialties) + "\n\n"
            msg += f"|cUsage:|n |y+stat specialty/{skill}=<specialty name>|n\n"
            msg += f"|cExample:|n |y+stat specialty/{skill}={specialties[0]}|n"
            
            self.caller.msg(msg)
        else:
            # Show all specialties organized by skill type
            msg = f"|wSkill Specialties|n\n\n"
            msg += "Specialties add depth and focus to your skills. Set them with:\n"
            msg += "|y+stat specialty/<skill>=<specialty name>|n\n\n"
            
            # Organize by skill type
            mental_skills = ['academics', 'computer', 'crafts', 'investigation', 'medicine', 'occult', 'politics', 'science']
            physical_skills = ['athletics', 'brawl', 'drive', 'firearms', 'larceny', 'stealth', 'survival', 'weaponry']
            social_skills = ['animal_ken', 'empathy', 'expression', 'intimidation', 'persuasion', 'socialize', 'streetwise', 'subterfuge']
            
            msg += "|cMental Skills:|n\n"
            for skill in mental_skills:
                if skill in LOOKUP_DATA.specialties:
                    specialties = LOOKUP_DATA.specialties[skill]
                    msg += f"  |y{skill.title().replace('_', ' ')}:|n {', '.join(specialties[:3])}"
                    if len(specialties) > 3:
                        msg += f", ... ({len(specialties)} total)"
                    msg += "\n"
            
            msg += "\n|cPhysical Skills:|n\n"
            for skill in physical_skills:
                if skill in LOOKUP_DATA.specialties:
                    specialties = LOOKUP_DATA.specialties[skill]
                    msg += f"  |y{skill.title().replace('_', ' ')}:|n {', '.join(specialties[:3])}"
                    if len(specialties) > 3:
                        msg += f", ... ({len(specialties)} total)"
                    msg += "\n"
            
            msg += "\n|cSocial Skills:|n\n"
            for skill in social_skills:
                if skill in LOOKUP_DATA.specialties:
                    specialties = LOOKUP_DATA.specialties[skill]
                    msg += f"  |y{skill.title().replace('_', ' ')}:|n {', '.join(specialties[:3])}"
                    if len(specialties) > 3:
                        msg += f", ... ({len(specialties)} total)"
                    msg += "\n"
            
            msg += f"\n|cUse:|n |y+lookup specialties <skill>|n to see all specialties for a specific skill\n"
            msg += f"|cExample:|n |y+lookup specialties athletics|n"
            
            self.caller.msg(msg)
    
    def search_stats(self):
        """Search for stats containing the given term."""
        if not self.args:
            self.caller.msg("Usage: +lookup/search <search term>")
            return
        
        search_results = LOOKUP_DATA.search_stats(self.args)
        
        if search_results:
            msg = f"|wSearch results for '{self.args}':|n\n"
            formatted_results = []
            
            for stat_type, name, data in search_results[:20]:  # Limit to 20 results
                if stat_type == 'attribute':
                    formatted_results.append(f"|wAttribute:|n {name.title()} ({data.att_type})")
                elif stat_type == 'skill':
                    formatted_results.append(f"|wSkill:|n {name.title().replace('_', ' ')} ({data.skill_type})")
                elif stat_type == 'merit':
                    formatted_results.append(f"|wMerit:|n {name} ({data.merit_type})")
                elif stat_type == 'discipline':
                    formatted_results.append(f"|wDiscipline:|n {name.title()}")
                elif stat_type == 'arcanum':
                    formatted_results.append(f"|wArcanum:|n {name.title()}")
            
            msg += "\n".join(formatted_results)
            if len(search_results) > 20:
                msg += f"\n\n|y... and {len(search_results) - 20} more results.|n"
            msg += f"\n\n|cUse:|n |y+lookup <stat_name>|n for detailed information."
        else:
            msg = f"No results found for '{self.args}'."
        
        self.caller.msg(msg)
    

