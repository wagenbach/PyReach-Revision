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
        +lookup powers [discipline]          - List vampire discipline powers (optionally by discipline)
        +lookup coils [mystery]              - List Coils of the Dragon (optionally by mystery)
        +lookup bloodline [name]             - List bloodline disciplines (optionally by bloodline)
        +lookup devotions [type]             - List devotions (optionally by type: general/carthian/invictus/nereid)
        +lookup scales [mystery]             - List Scales of the Dragon rituals (optionally by mystery)
        +lookup theban [rank]                - List Theban Sorcery miracles (optionally by rank 1-5)
        +lookup cruac [rank]                 - List Cruac rites (optionally by rank 1-5)
        +lookup arcana                       - List mage arcana
        +lookup spells [arcana]              - List mage spells (optionally by arcana)
        +lookup endowments [type]            - List hunter endowments (optionally by type)
        +lookup clans                        - List vampire clans
        +lookup covenants                    - List vampire covenants
        +lookup paths                        - List mage paths
        +lookup orders                       - List mage orders
        +lookup auspices                     - List werewolf auspices
        +lookup tribes                       - List werewolf tribes
        +lookup gifts [category]             - List werewolf gifts (optionally by category/renown)
        +lookup keys                         - List all Geist keys
        +lookup keys <name>                  - Show specific Geist key details
        +lookup haunts                       - List all Geist haunts
        +lookup haunts <name>                - Show specific Geist haunt details
        +lookup templates                    - List all character templates
        +lookup <stat_name>                  - Get detailed info on specific stat
        +lookup <category> <stat_name>       - Get details filtered by category
        +lookup/search <term>                - Search for stats containing term
        
        Category-Specific Lookups (for name collisions):
        +lookup merits <name>                - View as merit
        +lookup spells <name>                - View as spell
        +lookup powers <name>                - View as discipline power
        +lookup endowments <name>            - View as endowment
        +lookup attributes <name>            - View as attribute
        +lookup skills <name>                - View as skill
        
        Examples:
        +lookup strength                     - Show strength attribute details
        +lookup fast_reflexes                - Show Fast Reflexes merit details
        +lookup merits mental                - List all mental merits
        +lookup merits mage                  - List all Mage-specific merits
        +lookup merits psychic               - List all Psychic merits
        +lookup powers animalism             - List all Animalism discipline powers
        +lookup mesmerize                    - Show Mesmerize discipline power details
        +lookup devotions carthian           - List Carthian Movement devotions
        +lookup scales ascendant             - List Scales of the Dragon (Ascendant Mystery)
        +lookup theban 3                     - List Rank 3 Theban Sorcery miracles
        +lookup cruac 1                      - List Rank 1 Cruac rites
        +lookup gifts agony                  - List Gift of Agony facets
        +lookup gifts cunning                - List all Cunning renown gifts
        +lookup shadow_gaze                  - Show Shadow Gaze gift details
        +lookup keys                         - List all Geist keys
        +lookup keys beasts                  - Show Key of Beasts details
        +lookup haunts                       - List all Geist haunts
        +lookup haunts boneyard              - Show The Boneyard haunt details
        +lookup merits telekinesis           - View Telekinesis merit (psychic)
        +lookup spells telekinesis           - View Telekinesis spell (Forces 3)
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
        if args.startswith("attributes"):
            parts = args.split()
            if len(parts) > 1:
                # It's a stat name lookup with category filter
                stat_name = " ".join(parts[1:])
                self.show_stat_details(stat_name, category_filter="attributes")
            else:
                self.show_attributes()
        elif args.startswith("skills"):
            parts = args.split()
            if len(parts) > 1:
                # Check if it's a filter or a stat name
                skill_filters = ["mental", "physical", "social"]
                if parts[1] in skill_filters:
                    self.show_skills(parts[1])
                else:
                    # It's a stat name lookup with category filter
                    stat_name = " ".join(parts[1:])
                    self.show_stat_details(stat_name, category_filter="skills")
            else:
                self.show_skills(None)
        elif args.startswith("merits"):
            parts = args.split()
            if len(parts) > 1:
                # Check if it's a filter or a stat name
                merit_filters = ["mental", "physical", "social", "supernatural", "fighting", "style",
                               "vampire", "mage", "werewolf", "changeling", "geist", "demon", 
                               "deviant", "hunter", "mummy", "promethean", "mortal+", "mortal_plus",
                               "psychic", "ghoul", "dhampir", "atariya", "psychic_vampire", "general",
                               "plain", "infected", "lost boy", "dreamer"]
                if parts[1] in merit_filters:
                    self.show_merits(parts[1])
                else:
                    # It's a stat name lookup with category filter
                    stat_name = " ".join(parts[1:])
                    self.show_stat_details(stat_name, category_filter="merits")
            else:
                self.show_merits(None)
        elif args == "disciplines":
            self.show_disciplines()
        elif args.startswith("discipline_powers") or args.startswith("powers"):
            parts = args.split()
            if len(parts) > 1:
                # Check if it's a discipline filter or a stat name
                discipline_names = ["animalism", "auspex", "celerity", "dominate", "majesty", "nightmare", 
                                  "obfuscate", "protean", "resilience", "vigor", "cachexy", "crochan", "dead_signal"]
                if parts[1] in discipline_names:
                    self.show_discipline_powers(parts[1])
                else:
                    # It's a stat name lookup with category filter
                    stat_name = " ".join(parts[1:])
                    self.show_stat_details(stat_name, category_filter="powers")
            else:
                self.show_discipline_powers(None)
        elif args.startswith("coils"):
            parts = args.split()
            mystery = parts[1] if len(parts) > 1 else None
            self.show_coils(mystery)
        elif args.startswith("bloodline"):
            parts = args.split()
            bloodline = parts[1] if len(parts) > 1 else None
            self.show_bloodline_disciplines(bloodline)
        elif args.startswith("devotions") or args.startswith("devotion"):
            parts = args.split()
            if len(parts) > 1:
                # Check if it's a devotion type filter or a stat name
                devotion_types = ["general", "carthian", "invictus", "nereid"]
                if parts[1] in devotion_types:
                    self.show_devotions(parts[1])
                else:
                    # It's a stat name lookup with category filter
                    stat_name = " ".join(parts[1:])
                    self.show_stat_details(stat_name, category_filter="devotions")
            else:
                self.show_devotions(None)
        elif args.startswith("scales"):
            parts = args.split()
            if len(parts) > 1:
                # Check if it's a mystery filter or a stat name
                mystery_names = ["ascendant", "quintessence", "voivode", "wyrm", "zirnitra", "ziva", "other"]
                if parts[1] in mystery_names:
                    self.show_scales(parts[1])
                else:
                    # It's a stat name lookup with category filter
                    stat_name = " ".join(parts[1:])
                    self.show_stat_details(stat_name, category_filter="scales")
            else:
                self.show_scales(None)
        elif args.startswith("theban"):
            parts = args.split()
            if len(parts) > 1:
                rank_arg = parts[1]
                if rank_arg.isdigit():
                    self.show_theban(int(rank_arg))
                else:
                    # It's a stat name lookup with category filter
                    stat_name = " ".join(parts[1:])
                    self.show_stat_details(stat_name, category_filter="theban")
            else:
                self.show_theban(None)
        elif args.startswith("cruac"):
            parts = args.split()
            if len(parts) > 1:
                rank_arg = parts[1]
                if rank_arg.isdigit():
                    self.show_cruac(int(rank_arg))
                else:
                    # It's a stat name lookup with category filter
                    stat_name = " ".join(parts[1:])
                    self.show_stat_details(stat_name, category_filter="cruac")
            else:
                self.show_cruac(None)
        elif args == "arcana":
            self.show_arcana()
        elif args.startswith("spells"):
            parts = args.split()
            if len(parts) > 1:
                # Check if it's an arcana filter or a stat name
                arcana_names = ["death", "fate", "forces", "life", "matter", "mind", "prime", "space", "spirit", "time"]
                if parts[1] in arcana_names:
                    self.show_spells(parts[1])
                else:
                    # It's a stat name lookup with category filter
                    stat_name = " ".join(parts[1:])
                    self.show_stat_details(stat_name, category_filter="spells")
            else:
                self.show_spells(None)
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
        elif args.startswith("gifts"):
            parts = args.split()
            if len(parts) > 1:
                # Check if it's a gift category filter or a stat name
                gift_categories = ["agony", "blood", "death", "disease", "dominance", "elementals",
                                 "evasion", "fervor", "hunger", "insight", "inspiration", "knowledge",
                                 "nature", "rage", "shaping", "stealth", "strength", "technology",
                                 "warding", "weather", "change", "hunting", "pack",
                                 "crescent_moon", "full_moon", "gibbous_moon", "half_moon", "new_moon",
                                 "cunning", "glory", "honor", "purity", "wisdom"]
                if parts[1] in gift_categories:
                    self.show_werewolf_gifts(parts[1])
                else:
                    # It's a stat name lookup with category filter
                    stat_name = " ".join(parts[1:])
                    self.show_stat_details(stat_name, category_filter="gifts")
            else:
                self.show_werewolf_gifts(None)
        elif args.startswith("contracts"):
            parts = args.split()
            if len(parts) > 1:
                # Check if it's a contract category filter or a stat name
                contract_categories = ["crown", "jewel", "mirror", "shield", "steed", "sword", 
                                     "chalice", "coin", "stars", "thorn", "goblin"]
                if parts[1] in contract_categories:
                    self.show_changeling_contracts(parts[1])
                else:
                    # It's a stat name lookup with category filter
                    stat_name = " ".join(parts[1:])
                    self.show_stat_details(stat_name, category_filter="contracts")
            else:
                self.show_changeling_contracts(None)
        elif args == "seemings":
            self.show_seemings()
        elif args == "courts":
            self.show_courts()
        elif args.startswith("keys"):
            parts = args.split()
            if len(parts) > 1:
                # It's a specific key lookup
                key_name = " ".join(parts[1:])
                self.show_geist_key(key_name)
            else:
                self.show_geist_keys()
        elif args.startswith("haunts"):
            parts = args.split()
            if len(parts) > 1:
                # It's a specific haunt lookup
                haunt_name = " ".join(parts[1:])
                self.show_geist_haunt(haunt_name)
            else:
                self.show_geist_haunts()
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
            if len(parts) > 1:
                # Check if it's an endowment type filter or a stat name
                endowment_types = ["advanced_armory", "animal_control_kit", "benediction", "castigation", 
                                 "dreamscape", "elixir", "enkoimesis", "goetic_gospel", "horror_within", 
                                 "infusion", "ink", "inspiration", "lives_remembered", "perispiritism", 
                                 "relic", "rites_du_cheval", "rites_of_denial", "seitokuten", 
                                 "teleinformatics", "thaumatechnology", "xenotechnology"]
                if parts[1] in endowment_types:
                    self.show_endowments(parts[1])
                else:
                    # It's a stat name lookup with category filter (keep spaces for endowments)
                    stat_name = " ".join(parts[1:])
                    self.show_stat_details(stat_name, category_filter="endowments")
            else:
                self.show_endowments(None)
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
        """Show available lookup categories in a compact 4-column format."""
        msg = "|wCharacter Creation Lookup System|n\n\n"
        
        # Helper function to format items in 2 columns
        def format_two_columns(items):
            lines = []
            for i in range(0, len(items), 2):
                left = items[i] if i < len(items) else ""
                right = items[i + 1] if i + 1 < len(items) else ""
                lines.append((left, right))
            return lines
        
        # Define sections with items
        sections = [
            # Row 1: Core Stats | Vampire (4 columns total)
            {
                "left_title": "Core Stats:",
                "left_items": ["attributes", "skills [type]", "merits [filter]", "specialties", "templates"],
                "right_title": "Vampire:",
                "right_items": ["disciplines", "powers [disc]", "devotions [type]", "coils [mystery]",
                               "scales [mystery]", "theban [rank]", "cruac [rank]", "bloodline [name]",
                               "clans", "covenants"]
            },
            # Row 2: Mage | Werewolf
            {
                "left_title": "Mage:",
                "left_items": ["arcana", "spells [arcana]", "paths", "orders"],
                "right_title": "Werewolf:",
                "right_items": ["auspices", "tribes", "gifts [category]"]
            },
            # Row 3: Changeling | Geist
            {
                "left_title": "Changeling:",
                "left_items": ["seemings", "courts", "contracts [type]"],
                "right_title": "Geist:",
                "right_items": ["burdens", "krewe", "haunts", "keys", "ceremonies"]
            },
            # Row 4: Demon | Promethean
            {
                "left_title": "Demon:",
                "left_items": ["incarnations", "agendas", "embeds", "exploits"],
                "right_title": "Promethean:",
                "right_items": ["transmutations", "alembics", "bestowments", "lineages", "athanors"]
            },
            # Row 5: Mummy | Deviant
            {
                "left_title": "Mummy:",
                "left_items": ["guilds", "decrees", "judges", "utterances", "affinities"],
                "right_title": "Deviant:",
                "right_items": ["origins", "clades", "variations", "adaptations"]
            },
            # Row 6: Hunter | Mortal+
            {
                "left_title": "Hunter:",
                "left_items": ["endowments [type]"],
                "right_title": "Mortal+:",
                "right_items": ["mortal+", "psychic", "tells"]
            }
        ]
        
        # Display each section pair side by side
        for i, section in enumerate(sections):
            # Format left and right items into 2-column layouts
            left_lines = format_two_columns(section["left_items"])
            right_lines = format_two_columns(section["right_items"])
            
            # Display section titles side by side (total width ~75 chars)
            msg += f"|c{section['left_title']:<41}|n|c{section['right_title']}|n\n"
            
            # Display items (4 columns: 2 for left section, 2 for right section)
            max_rows = max(len(left_lines), len(right_lines))
            for j in range(max_rows):
                # Left section (2 columns, 20 chars each)
                if j < len(left_lines):
                    left_col1 = f"|y{left_lines[j][0]:<20}|n" if left_lines[j][0] else " " * 20
                    left_col2 = f"|y{left_lines[j][1]:<20}|n" if left_lines[j][1] else " " * 20
                else:
                    left_col1 = " " * 20
                    left_col2 = " " * 20
                
                # Right section (2 columns, 20 chars each, but don't pad the last one)
                if j < len(right_lines):
                    right_col1 = f"|y{right_lines[j][0]:<20}|n" if right_lines[j][0] else " " * 20
                    # Last column - don't pad with trailing spaces
                    right_col2 = f"|y{right_lines[j][1]}|n" if right_lines[j][1] else ""
                else:
                    right_col1 = ""
                    right_col2 = ""
                
                # Build line - only add right columns if they have content
                line = f"  {left_col1}{left_col2}"
                if right_col1 or right_col2:
                    line += f"{right_col1}{right_col2}"
                msg += line.rstrip() + "\n"
            
            # Only add blank line if not the last section
            if i < len(sections) - 1:
                msg += "\n"
        
        msg += "\n|cSpecial Commands:|n\n"
        msg += "  |y+lookup <stat>|n                - Get details on any stat\n"
        msg += "  |y+lookup <category> <stat>|n    - Get details with category filter\n"
        msg += "  |y+lookup/search <term>|n        - Search for stats by keyword\n\n"
        
        msg += "|cExamples:|n\n"
        msg += "  |y+lookup attributes|n - List all attributes\n"
        msg += "  |y+lookup strength|n - View strength details\n"
        msg += "  |y+lookup merits vampire|n - List vampire merits\n"
        msg += "  |y+lookup merits telekinesis|n - View telekinesis merit (not spell)\n"
        msg += "  |y+lookup spells telekinesis|n - View telekinesis spell (not merit)\n"
        msg += "  |y+lookup powers animalism|n - List Animalism discipline powers\n"
        msg += "  |y+lookup/search invisible|n - Find all invisibility-related powers\n"
        
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
                    "psychic", "ghoul", "dhampir", "atariya", "psychic_vampire", "psychic vampire",
                    "plain", "infected", "lost boy", "dreamer"]
        
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
        from world.cofd.templates.vampire import VAMPIRE_PRIMARY_POWERS
        
        table = evtable.EvTable("|wDiscipline|n", "|wDescription|n", border="cells", width=78)
        
        # Only show PRIMARY_POWERS (the rated disciplines), not secondary powers (individual rituals)
        for discipline in sorted(VAMPIRE_PRIMARY_POWERS):
            desc = get_discipline_description(discipline)
            table.add_row(f"|r{discipline.title()}|n", desc)
        
        self.caller.msg(f"|wVampire Disciplines|n\n{table}")
        self.caller.msg(f"\n|cNote:|n Disciplines are rated 1-5 dots and represent core vampiric powers.")
        self.caller.msg(f"|cView powers:|n Use |y+lookup powers <discipline>|n to see individual powers (e.g., +lookup powers animalism)")
        self.caller.msg(f"|cRitual Magic:|n Use |y+lookup cruac|n, |y+lookup theban|n, |y+lookup scales|n for covenant rituals")
    
    def show_discipline_powers(self, discipline=None):
        """Show vampire discipline powers, optionally filtered by discipline."""
        from world.cofd.templates.vampire_disciplines import get_all_discipline_powers, get_powers_by_discipline
        
        if discipline:
            # Filter by discipline
            powers = get_powers_by_discipline(discipline)
            if not powers:
                self.caller.msg(f"No powers found for discipline: {discipline}")
                self.caller.msg("|cValid disciplines:|n animalism, auspex, celerity, dominate, majesty, nightmare, obfuscate, protean, resilience, vigor")
                return
            
            title = f"|wVampire Discipline Powers - {discipline.title()}|n"
        else:
            powers = get_all_discipline_powers()
            title = "|wAll Vampire Discipline Powers|n"
        
        # Group powers by level
        powers_by_level = {1: [], 2: [], 3: [], 4: [], 5: [], "rated": []}
        for power_key, power_data in powers.items():
            level = power_data['level']
            if isinstance(level, str) and '-' in level:
                powers_by_level["rated"].append((power_key, power_data))
            else:
                powers_by_level[level].append((power_key, power_data))
        
        output = [title, ""]
        
        # Display rated disciplines first (Celerity, Resilience, Vigor)
        if powers_by_level["rated"]:
            output.append("|rRated Disciplines (• to •••••)|n")
            for power_key, power_data in sorted(powers_by_level["rated"], key=lambda x: x[1]['name']):
                power_name = power_data['name']
                cost = power_data['cost']
                
                output.append(f"  |y{power_name}|n")
                output.append(f"    Cost: {cost}")
                if power_data.get('note'):
                    output.append(f"    {power_data['note']}")
                output.append(f"    |gUse:|n +stat {power_data['discipline']}=<1-5>")
            output.append("")
        
        # Display powers organized by level
        for level in range(1, 6):
            level_powers = powers_by_level[level]
            if level_powers:
                dots = "●" * level
                if discipline:
                    output.append(f"|r{discipline.title()} {dots}|n")
                else:
                    output.append(f"|rLevel {dots}|n")
                
                for power_key, power_data in sorted(level_powers, key=lambda x: x[1]['name']):
                    power_name = power_data['name']
                    cost = power_data['cost']
                    prereq = power_data.get('prerequisite', '')
                    
                    # Include discipline if showing all powers
                    if discipline:
                        output.append(f"  |y{power_name}|n - Cost: {cost}")
                    else:
                        power_discipline = power_data['discipline'].title()
                        output.append(f"  |y{power_name}|n ({power_discipline}) - Cost: {cost}")
                    
                    if prereq:
                        output.append(f"    Prerequisite: {prereq}")
                    
                    # Add usage hint
                    output.append(f"    |gUse:|n +lookup {power_key}")
                
                output.append("")
        
        self.caller.msg("\n".join(output))
        
        if not discipline:
            self.caller.msg("|cFilter by discipline:|n +lookup powers animalism, +lookup powers dominate, etc.")
        self.caller.msg("|cFor power details:|n +lookup <power_name> (e.g., +lookup mesmerize)")
    
    def show_discipline_power_details(self, power_key, power_data):
        """Show detailed information about a specific discipline power."""
        # Check type of power
        is_coil = 'mystery' in power_data
        is_bloodline = 'bloodline' in power_data and not is_coil
        is_devotion = power_data.get('type') == 'devotion'
        
        # Title
        if is_devotion:
            devotion_type = power_data.get('covenant', power_data.get('bloodline', 'General')).title()
            msg = f"|w{power_data['name']} ({devotion_type} Devotion)|n\n"
        elif is_coil:
            msg = f"|w{power_data['name']} (Coil of the Dragon)|n\n"
            mystery_name = power_data['mystery'].title()
            msg += f"|cMystery:|n {mystery_name}\n"
        elif is_bloodline:
            bloodline_name = power_data['bloodline'].title()
            msg = f"|w{power_data['name']} ({power_data['discipline'].title()} - {bloodline_name} Bloodline)|n\n"
        else:
            msg = f"|w{power_data['name']} (Vampire Discipline Power)|n\n"
        
        # For devotions, show prerequisites and XP cost
        if is_devotion:
            msg += f"|cPrerequisites:|n {power_data['prerequisites']}\n"
            xp_cost = power_data['xp_cost']
            msg += f"|cXP Cost:|n {xp_cost} XP\n"
        else:
            # Discipline and level for non-devotions
            if 'discipline' in power_data:
                discipline_name = power_data['discipline'].title()
                power_level = power_data.get('level')
                
                if not is_coil and power_level:  # Regular disciplines and bloodlines show discipline name
                    if isinstance(power_level, str) and '-' in str(power_level):
                        msg += f"|cDiscipline:|n {discipline_name} (Rated {power_level})\n"
                    else:
                        dots = "●" * power_level
                        msg += f"|cDiscipline:|n {discipline_name} {dots}\n"
            
            if is_coil:  # Coils just show level
                power_level = power_data.get('level')
                if power_level:
                    dots = "●" * power_level
                    msg += f"|cLevel:|n {dots}\n"
        
        # Cost (Vitae/Willpower)
        msg += f"|cCost:|n {power_data['cost']}\n"
        
        # Prerequisite for non-devotions
        if not is_devotion and power_data.get('prerequisite'):
            msg += f"|cPrerequisite:|n {power_data['prerequisite']}\n"
        
        # Dice Pool
        if power_data.get('dice_pool') and power_data['dice_pool'] != '-':
            msg += f"|cDice Pool:|n {power_data['dice_pool']}\n"
        
        # Description
        msg += f"|cDescription:|n {power_data['description']}\n"
        
        # Note (for rated disciplines)
        if power_data.get('note'):
            msg += f"|cNote:|n {power_data['note']}\n"
        
        # Source
        msg += f"|cSource:|n {power_data['book']}\n"
        
        # Usage
        if is_devotion:
            msg += f"\n|gTo add to character:|n +stat devotion={power_key}\n"
        elif isinstance(power_data.get('level'), str) and '-' in str(power_data.get('level', '')):
            msg += f"\n|gTo set on character:|n +stat {power_data['discipline']}=<1-5>\n"
        elif is_coil:
            msg += f"\n|gTo add to character:|n +stat coil={power_key}\n"
        else:
            msg += f"\n|gTo add to character:|n +stat discipline_power={power_key}\n"
        
        self.caller.msg(msg)
    
    def show_coils(self, mystery=None):
        """Show Coils of the Dragon, optionally filtered by mystery."""
        from world.cofd.templates.vampire_disciplines import get_all_coils, get_coils_by_mystery
        
        if mystery:
            # Filter by mystery
            coils = get_coils_by_mystery(mystery)
            if not coils:
                self.caller.msg(f"No coils found for mystery: {mystery}")
                self.caller.msg("|cValid mysteries:|n ascendant, quintessence, voivode, wyrm, zirnitra, ziva")
                return
            
            title = f"|wCoils of the Dragon - Mystery of the {mystery.title()}|n"
        else:
            coils = get_all_coils()
            title = "|wAll Coils of the Dragon|n"
        
        # Group coils by mystery if showing all
        if not mystery:
            mysteries = {}
            for coil_key, coil_data in coils.items():
                mystery_name = coil_data.get('mystery', 'unknown')
                if mystery_name not in mysteries:
                    mysteries[mystery_name] = []
                mysteries[mystery_name].append((coil_key, coil_data))
            
            output = [title, "", "|cOrdo Dracul Transcendent Powers|n", ""]
            
            for mystery_name in sorted(mysteries.keys()):
                mystery_coils = mysteries[mystery_name]
                output.append(f"|rMystery of the {mystery_name.title()}:|n")
                output.append(f"  {len(mystery_coils)} coils available")
                output.append(f"  |gView all:|n +lookup coils {mystery_name}")
                output.append("")
            
            self.caller.msg("\n".join(output))
            self.caller.msg("|cFilter by mystery:|n +lookup coils ascendant, +lookup coils wyrm, etc.")
            self.caller.msg("|cFor coil details:|n +lookup <coil_name> (e.g., +lookup conquer_the_red_fear)")
        else:
            # Show specific mystery's coils
            output = [title, ""]
            
            # Group by level
            coils_by_level = {1: [], 2: [], 3: [], 4: [], 5: []}
            for coil_key, coil_data in coils.items():
                level = coil_data['level']
                coils_by_level[level].append((coil_key, coil_data))
            
            # Display coils organized by level
            for level in range(1, 6):
                level_coils = coils_by_level[level]
                if level_coils:
                    dots = "●" * level
                    output.append(f"|r{mystery.title()} {dots}|n")
                    
                    for coil_key, coil_data in sorted(level_coils, key=lambda x: x[1]['name']):
                        coil_name = coil_data['name']
                        cost = coil_data['cost']
                        
                        output.append(f"  |y{coil_name}|n - Cost: {cost}")
                        output.append(f"    |gUse:|n +lookup {coil_key}")
                    
                    output.append("")
            
            self.caller.msg("\n".join(output))
            self.caller.msg("|cFor coil details:|n +lookup <coil_name> (e.g., +lookup peace_with_the_flame)")
    
    def show_bloodline_disciplines(self, bloodline=None):
        """Show bloodline disciplines, optionally filtered by bloodline."""
        from world.cofd.templates.vampire_disciplines import get_bloodline_discipline, ALL_BLOODLINE_DISCIPLINES
        
        if bloodline:
            # Filter by bloodline
            powers = get_bloodline_discipline(bloodline)
            if not powers:
                self.caller.msg(f"No bloodline discipline found for: {bloodline}")
                self.caller.msg("|cValid bloodlines:|n morbus (Cachexy), bron (Crochan), jharana (Dead Signal)")
                return
            
            # Get discipline name from first power
            first_power = next(iter(powers.values()))
            discipline_name = first_power['discipline'].title()
            
            title = f"|w{discipline_name} ({bloodline.title()} Bloodline)|n"
        else:
            # Show all bloodline disciplines organized by bloodline
            output = ["|wBloodline Disciplines|n", ""]
            
            bloodlines = {
                "morbus": {"discipline": "Cachexy", "description": "The disease-bearers"},
                "bron": {"discipline": "Crochan", "description": "The blood-healers"},
                "jharana": {"discipline": "Dead Signal", "description": "The God-Machine touched"}
            }
            
            for bloodline_name, info in sorted(bloodlines.items()):
                output.append(f"|r{info['discipline']}|n ({bloodline_name.title()} bloodline)")
                output.append(f"  {info['description']}")
                output.append(f"  |gView powers:|n +lookup bloodline {bloodline_name}")
                output.append("")
            
            self.caller.msg("\n".join(output))
            return
        
        # Show specific bloodline's powers
        output = [title, ""]
        
        # Group by level
        powers_by_level = {1: [], 2: [], 3: [], 4: [], 5: []}
        for power_key, power_data in powers.items():
            level = power_data['level']
            powers_by_level[level].append((power_key, power_data))
        
        # Display powers organized by level
        for level in range(1, 6):
            level_powers = powers_by_level[level]
            if level_powers:
                dots = "●" * level
                output.append(f"|r{discipline_name} {dots}|n")
                
                for power_key, power_data in sorted(level_powers, key=lambda x: x[1]['name']):
                    power_name = power_data['name']
                    cost = power_data['cost']
                    
                    output.append(f"  |y{power_name}|n - Cost: {cost}")
                    output.append(f"    |gUse:|n +lookup {power_key}")
                
                output.append("")
        
        self.caller.msg("\n".join(output))
        self.caller.msg("|cFor power details:|n +lookup <power_name> (e.g., +lookup diagnose)")
    
    def show_devotions(self, devotion_type=None):
        """Show devotions, optionally filtered by type."""
        from world.cofd.templates.vampire_disciplines import get_devotions_by_type, get_all_devotions
        
        if devotion_type:
            # Filter by type
            devotions = get_devotions_by_type(devotion_type)
            if not devotions:
                self.caller.msg(f"No devotions found for type: {devotion_type}")
                self.caller.msg("|cValid types:|n general, carthian, invictus, nereid")
                return
            
            title = f"|w{devotion_type.title()} Devotions|n"
        else:
            # Show all devotions organized by type
            output = ["|wDevotions|n", "", "|cCombination Discipline Powers|n", ""]
            
            devotion_types = {
                "general": ("General", "Available to all vampires"),
                "carthian": ("Carthian Movement", "Revolutionary covenant devotions"),
                "invictus": ("Invictus", "Aristocratic covenant devotions"),
                "nereid": ("Nereid", "Bloodline-specific devotions")
            }
            
            for type_key, (type_name, type_desc) in devotion_types.items():
                type_devotions = get_devotions_by_type(type_key)
                output.append(f"|r{type_name}|n")
                output.append(f"  {type_desc}")
                output.append(f"  {len(type_devotions)} devotions available")
                output.append(f"  |gView all:|n +lookup devotions {type_key}")
                output.append("")
            
            self.caller.msg("\n".join(output))
            self.caller.msg("|cFilter by type:|n +lookup devotions general, +lookup devotions carthian, etc.")
            self.caller.msg("|cFor devotion details:|n +lookup <devotion_name> (e.g., +lookup quicken_sight)")
            return
        
        # Show specific type's devotions
        output = [title, ""]
        
        # Sort devotions by XP cost, then alphabetically
        sorted_devotions = sorted(devotions.items(), key=lambda x: (x[1].get('xp_cost', 0), x[1]['name']))
        
        # Group by XP cost
        devotions_by_xp = {}
        for dev_key, dev_data in sorted_devotions:
            xp = dev_data.get('xp_cost', 0)
            if xp not in devotions_by_xp:
                devotions_by_xp[xp] = []
            devotions_by_xp[xp].append((dev_key, dev_data))
        
        # Display devotions organized by XP cost
        for xp_cost in sorted(devotions_by_xp.keys()):
            xp_devotions = devotions_by_xp[xp_cost]
            output.append(f"|r{xp_cost} XP|n")
            
            for dev_key, dev_data in xp_devotions:
                dev_name = dev_data['name']
                prereqs = dev_data['prerequisites']
                cost = dev_data['cost']
                
                output.append(f"  |y{dev_name}|n")
                output.append(f"    Prerequisites: {prereqs}")
                output.append(f"    Cost: {cost}")
                output.append(f"    |gUse:|n +lookup {dev_key}")
            
            output.append("")
        
        self.caller.msg("\n".join(output))
        self.caller.msg(f"|cTotal:|n {len(devotions)} devotions")
        self.caller.msg("|cFor devotion details:|n +lookup <devotion_name> (e.g., +lookup bend_space)")
    
    def show_scales(self, mystery=None):
        """Show Scales of the Dragon rituals, optionally filtered by mystery."""
        from world.cofd.templates.vampire_rituals import get_all_scales, get_scales_by_mystery
        
        if mystery:
            # Filter by mystery
            scales = get_scales_by_mystery(mystery)
            if not scales:
                self.caller.msg(f"No scales found for mystery: {mystery}")
                self.caller.msg("|cValid mysteries:|n ascendant, quintessence, voivode, wyrm, zirnitra, ziva, other")
                return
            
            title = f"|wScales of the Dragon - Mystery of the {mystery.title()}|n"
            output = [title, "", "|cOrdo Dracul Alchemical Rituals|n", ""]
            
            # Sort by rank
            sorted_scales = sorted(scales.items(), key=lambda x: (x[1].get('rank', 0) if isinstance(x[1].get('rank'), int) else 99, x[1]['name']))
            
            for scale_key, scale_data in sorted_scales:
                rank = scale_data.get('rank', '-')
                if isinstance(rank, int):
                    dots = "●" * rank
                    output.append(f"|y{scale_data['name']}|n - Rank: {dots}")
                else:
                    output.append(f"|y{scale_data['name']}|n - Rank: {rank}")
                output.append(f"  |gUse:|n +lookup {scale_key}")
            
            self.caller.msg("\n".join(output))
        else:
            # Show all mysteries
            output = ["|wScales of the Dragon|n", "", "|cOrdo Dracul Alchemical Rituals|n", ""]
            
            mysteries = {
                "ascendant": "Overcome vampiric weaknesses",
                "quintessence": "Domain-based rituals",
                "voivode": "Blood bond rituals",
                "wyrm": "Frenzy and vitae rituals",
                "zirnitra": "Supernatural merit rituals",
                "ziva": "Humanity transcendence rituals",
                "other": "Advanced spirit-walking scales"
            }
            
            for mystery_name, mystery_desc in mysteries.items():
                mystery_scales = get_scales_by_mystery(mystery_name)
                if mystery_scales:
                    output.append(f"|rMystery of the {mystery_name.title()}:|n")
                    output.append(f"  {mystery_desc}")
                    output.append(f"  {len(mystery_scales)} scales available")
                    output.append(f"  |gView all:|n +lookup scales {mystery_name}")
                    output.append("")
            
            self.caller.msg("\n".join(output))
            self.caller.msg("|cFor scale details:|n +lookup <scale_name> (e.g., +lookup flesh_graft_treatment)")
    
    def show_theban(self, rank=None):
        """Show Theban Sorcery miracles, optionally filtered by rank."""
        from world.cofd.templates.vampire_rituals import get_all_theban, get_theban_by_rank
        
        if rank:
            # Filter by rank
            miracles = get_theban_by_rank(rank)
            if not miracles:
                self.caller.msg(f"No Theban Sorcery miracles found for rank: {rank}")
                self.caller.msg("|cValid ranks:|n 1, 2, 3, 4, 5")
                return
            
            dots = "●" * rank
            title = f"|wTheban Sorcery - Rank {dots}|n"
            output = [title, "", "|cLancea et Sanctum Divine Miracles|n", ""]
            
            for miracle_key, miracle_data in sorted(miracles.items(), key=lambda x: x[1]['name']):
                output.append(f"|y{miracle_data['name']}|n")
                output.append(f"  Target Number: {miracle_data['target_number']}")
                if miracle_data.get('opposition') and miracle_data['opposition'] != '-':
                    output.append(f"  Opposition: {miracle_data['opposition']}")
                if miracle_data.get('sacrament'):
                    output.append(f"  Sacrament: {miracle_data['sacrament']}")
                output.append(f"  |gUse:|n +lookup {miracle_key}")
                output.append("")
            
            self.caller.msg("\n".join(output))
        else:
            # Show all ranks
            output = ["|wTheban Sorcery|n", "", "|cLancea et Sanctum Divine Miracles|n", ""]
            
            for rank_num in range(1, 6):
                rank_miracles = get_theban_by_rank(rank_num)
                if rank_miracles:
                    dots = "●" * rank_num
                    output.append(f"|rRank {dots}:|n")
                    output.append(f"  {len(rank_miracles)} miracles available")
                    output.append(f"  |gView all:|n +lookup theban {rank_num}")
                    output.append("")
            
            self.caller.msg("\n".join(output))
            self.caller.msg("|cFor miracle details:|n +lookup <miracle_name> (e.g., +lookup apple_of_eden)")
    
    def show_cruac(self, rank=None):
        """Show Cruac rites, optionally filtered by rank."""
        from world.cofd.templates.vampire_rituals import get_all_cruac, get_cruac_by_rank
        
        if rank:
            # Filter by rank
            rites = get_cruac_by_rank(rank)
            if not rites:
                self.caller.msg(f"No Cruac rites found for rank: {rank}")
                self.caller.msg("|cValid ranks:|n 1, 2, 3, 4, 5")
                return
            
            dots = "●" * rank
            title = f"|wCruac - Rank {dots}|n"
            output = [title, "", "|cCircle of the Crone Blood Sorcery|n", ""]
            
            for rite_key, rite_data in sorted(rites.items(), key=lambda x: x[1]['name']):
                output.append(f"|y{rite_data['name']}|n")
                output.append(f"  Target Number: {rite_data['target_number']}")
                if rite_data.get('opposition') and rite_data['opposition'] != '-':
                    output.append(f"  Opposition: {rite_data['opposition']}")
                output.append(f"  |gUse:|n +lookup {rite_key}")
                output.append("")
            
            self.caller.msg("\n".join(output))
        else:
            # Show all ranks
            output = ["|wCruac|n", "", "|cCircle of the Crone Blood Sorcery|n", ""]
            
            for rank_num in range(1, 6):
                rank_rites = get_cruac_by_rank(rank_num)
                if rank_rites:
                    dots = "●" * rank_num
                    output.append(f"|rRank {dots}:|n")
                    output.append(f"  {len(rank_rites)} rites available")
                    output.append(f"  |gView all:|n +lookup cruac {rank_num}")
                    output.append("")
            
            self.caller.msg("\n".join(output))
            self.caller.msg("|cFor rite details:|n +lookup <rite_name> (e.g., +lookup pangs_of_proserpina)")
    
    def show_ritual_power_details(self, power_key, power_data):
        """Show detailed information about a ritual power (Scale, Theban, or Cruac)."""
        ritual_type = power_data.get('type', 'ritual')
        
        # Determine title based on type
        if ritual_type == 'scale':
            mystery_name = power_data.get('mystery', 'Unknown').title()
            msg = f"|w{power_data['name']} (Scale of the Dragon - {mystery_name})|n\n"
        elif ritual_type == 'theban':
            msg = f"|w{power_data['name']} (Theban Sorcery Miracle)|n\n"
        elif ritual_type == 'cruac':
            if 'bloodline' in power_data:
                bloodline = power_data['bloodline'].title()
                msg = f"|w{power_data['name']} (Cruac - {bloodline} Bloodline)|n\n"
            else:
                msg = f"|w{power_data['name']} (Cruac Rite)|n\n"
        else:
            msg = f"|w{power_data['name']} (Ritual Power)|n\n"
        
        # Rank
        rank = power_data.get('rank', '-')
        if isinstance(rank, int):
            dots = "●" * rank
            msg += f"|cRank:|n {dots}\n"
        else:
            msg += f"|cRank:|n {rank}\n"
        
        # Target Number (for Theban and Cruac)
        if power_data.get('target_number'):
            msg += f"|cTarget Number:|n {power_data['target_number']}\n"
        
        # Opposition
        if power_data.get('opposition') and power_data['opposition'] != '-':
            msg += f"|cOpposition:|n {power_data['opposition']}\n"
        
        # Sacrament (for Theban)
        if power_data.get('sacrament'):
            msg += f"|cSacrament:|n {power_data['sacrament']}\n"
        
        # Prerequisites (for Scales)
        if power_data.get('prerequisites'):
            msg += f"|cPrerequisites:|n {power_data['prerequisites']}\n"
        
        # Description
        msg += f"|cDescription:|n {power_data['description']}\n"
        
        # Source
        msg += f"|cSource:|n {power_data['book']}\n"
        
        # Usage
        if ritual_type == 'scale':
            msg += f"\n|gTo add to character:|n +stat scale={power_key}\n"
        elif ritual_type == 'theban':
            msg += f"\n|gTo add to character:|n +stat theban={power_key}\n"
        elif ritual_type == 'cruac':
            msg += f"\n|gTo add to character:|n +stat cruac={power_key}\n"
        
        self.caller.msg(msg)
    
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
    
    def show_stat_details(self, stat_name, category_filter=None):
        """Show detailed information about a specific stat, optionally filtered by category."""
        # Collect all matches across categories
        matches = []
        
        # Check rituals (scales, theban, cruac) if not filtering or if filtering for these
        if not category_filter or category_filter in ["scales", "theban", "cruac", "rituals"]:
            from world.cofd.templates.vampire_rituals import get_ritual_power
            ritual_key = stat_name.lower().replace(" ", "_")
            ritual_data = get_ritual_power(ritual_key)
            if ritual_data:
                matches.append(("ritual", ritual_key, ritual_data))
        
        # Check discipline powers
        if not category_filter or category_filter in ["powers", "disciplines", "discipline_powers"]:
            from world.cofd.templates.vampire_disciplines import get_discipline_power
            power_key = stat_name.lower().replace(" ", "_")
            power_data = get_discipline_power(power_key)
            if power_data:
                matches.append(("discipline_power", power_key, power_data))
        
        # Check devotions
        if not category_filter or category_filter == "devotions":
            from world.cofd.templates.vampire_disciplines import ALL_DEVOTIONS
            devotion_key = stat_name.lower().replace(" ", "_")
            if devotion_key in ALL_DEVOTIONS:
                matches.append(("discipline_power", devotion_key, ALL_DEVOTIONS[devotion_key]))
        
        # Check werewolf gifts
        if not category_filter or category_filter == "gifts":
            from world.cofd.templates.werewolf_gifts import get_gift
            gift_key = stat_name.lower().replace(" ", "_")
            gift_data = get_gift(gift_key)
            if gift_data:
                matches.append(("gift", gift_key, gift_data))
        
        # Check changeling contracts
        if not category_filter or category_filter == "contracts":
            from world.cofd.templates.changeling_contracts import get_contract
            contract_key = stat_name.lower().replace(" ", "_")
            contract_data = get_contract(contract_key)
            if contract_data:
                matches.append(("contract", contract_key, contract_data))
        
        # Check geist keys
        if not category_filter or category_filter == "keys":
            key_name_normalized = stat_name.lower().replace(" ", " ")
            keys_data = LOOKUP_DATA.geist_data['keys_detailed']
            if key_name_normalized in keys_data:
                matches.append(("key", key_name_normalized, keys_data[key_name_normalized]))
        
        # Check geist haunts
        if not category_filter or category_filter == "haunts":
            haunt_name_normalized = stat_name.lower().replace(" ", "_")
            haunts_data = LOOKUP_DATA.geist_data['haunts_detailed']
            if haunt_name_normalized in haunts_data:
                matches.append(("haunt", haunt_name_normalized, haunts_data[haunt_name_normalized]))
        
        # Check spells
        if not category_filter or category_filter == "spells":
            from world.cofd.templates.mage_spells import get_spell
        spell_key = stat_name.lower().replace(" ", "_")
        spell_data = get_spell(spell_key)
        if spell_data:
                matches.append(("spell", spell_key, spell_data))
        
        # Check endowments
        if not category_filter or category_filter == "endowments":
            from world.cofd.templates.hunter_endowments import get_endowment
            endowment_key = stat_name.lower()  # Keep spaces for endowments
            endowment_data = get_endowment(endowment_key)
            if endowment_data:
                matches.append(("endowment", endowment_key, endowment_data))
        
        # Check general stats (attributes, skills, merits, etc.)
        if not category_filter or category_filter in ["attributes", "skills", "merits", "advantages", "anchors"]:
            result = LOOKUP_DATA.find_stat(stat_name)
            if result:
                stat_type, stat_data = result
                # Only include if category matches or no filter
                if not category_filter or category_filter == stat_type or category_filter == stat_type + "s":
                    matches.append((stat_type, stat_name, stat_data))
        
        # Handle results
        if len(matches) == 0:
            self.caller.msg(f"No stat found matching '{stat_name}'. Use |y+lookup|n to see available categories.")
            return
        
        elif len(matches) == 1:
            # Single match - show it
            stat_type, key, data = matches[0]
            if stat_type == "ritual":
                self.show_ritual_power_details(key, data)
            elif stat_type == "discipline_power":
                self.show_discipline_power_details(key, data)
            elif stat_type == "gift":
                self.show_gift_details(key, data)
            elif stat_type == "contract":
                self.show_contract_details(key, data)
            elif stat_type == "key":
                self.show_geist_key(key)
            elif stat_type == "haunt":
                self.show_geist_haunt(key)
            elif stat_type == "spell":
                self.show_spell_details(key, data)
            elif stat_type == "endowment":
                self.show_endowment_details(key, data)
            else:
                self._show_basic_stat_details(stat_type, data)
            return
        
        else:
            # Multiple matches - show them all with category indicators
            self.caller.msg(f"|wMultiple matches found for '{stat_name}':|n\n")
            for i, (stat_type, key, data) in enumerate(matches, 1):
                type_display = stat_type.replace("_", " ").title()
                if 'name' in data:
                    name = data['name']
                elif hasattr(data, 'name'):
                    name = data.name
                else:
                    name = stat_name.title()
                
                self.caller.msg(f"{i}. |y{name}|n ({type_display})")
            
            self.caller.msg(f"\n|cTo view a specific type:|n")
            self.caller.msg(f"  |y+lookup merits {stat_name}|n - View as merit")
            self.caller.msg(f"  |y+lookup spells {stat_name}|n - View as spell")
            self.caller.msg(f"  |y+lookup powers {stat_name}|n - View as discipline power")
            self.caller.msg(f"  |y+lookup gifts {stat_name}|n - View as werewolf gift")
            self.caller.msg(f"  |y+lookup contracts {stat_name}|n - View as changeling contract")
            self.caller.msg(f"  |y+lookup keys {stat_name}|n - View as geist key")
            self.caller.msg(f"  |y+lookup haunts {stat_name}|n - View as geist haunt")
            self.caller.msg(f"  |y+lookup endowments {stat_name}|n - View as endowment")
            return
    
    def _show_basic_stat_details(self, stat_type, stat_data):
        """Helper method to show basic stat details (attributes, skills, merits, etc.)."""
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
        else:
            msg = f"Unknown stat type: {stat_type}\n"
        
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
        
        # Display in columns (adjusted to 25 chars to fit 78-char limit: 2 indent + 25*3 = 77)
        col_width = 25
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
    
    def show_werewolf_gifts(self, filter_arg=None):
        """Show werewolf gifts, optionally filtered by category, renown, or auspice."""
        from world.cofd.templates.werewolf_gifts import (
            get_all_gifts, get_gifts_by_type, get_gifts_by_renown, GIFT_CATEGORIES
        )
        
        if not filter_arg:
            # Show all gift categories
            output = ["|wWerewolf Gifts (Facets)|n", "", "|cAvailable Gift Categories:|n", ""]
            
            # Moon Gifts
            output.append("|yMoon Gifts (Auspice-Specific):|n")
            output.append("  crescent_moon (Ithaeur), full_moon (Rahu), gibbous_moon (Cahalith)")
            output.append("  half_moon (Elodoth), new_moon (Irraka)")
            output.append("")
            
            # Shadow Gift Categories
            output.append("|yShadow Gifts (General):|n")
            shadow_cats = ["agony", "blood", "death", "disease", "dominance", "elementals",
                          "evasion", "fervor", "hunger", "insight", "inspiration", "knowledge",
                          "nature", "rage", "shaping", "stealth", "strength", "technology",
                          "warding", "weather", "change", "hunting", "pack"]
            
            # Display in 3 columns
            for i in range(0, len(shadow_cats), 3):
                row = shadow_cats[i:i+3]
                row_text = "  " + ", ".join([f"{cat}" for cat in row])
                output.append(row_text)
            
            output.append("")
            output.append("|cBy Renown:|n")
            output.append("  cunning, glory, honor, purity, wisdom")
            output.append("")
            
            self.caller.msg("\n".join(output))
            self.caller.msg("|cFilter by category:|n +lookup gifts agony, +lookup gifts crescent_moon, etc.")
            self.caller.msg("|cFilter by renown:|n +lookup gifts cunning, +lookup gifts glory, etc.")
            self.caller.msg("|cFor gift details:|n +lookup <gift_name> (e.g., +lookup shadow_gaze)")
            return
        
        # Check if it's a renown filter
        if filter_arg in ["cunning", "glory", "honor", "purity", "wisdom"]:
            gifts = get_gifts_by_renown(filter_arg)
            title = f"|wWerewolf Gifts - {filter_arg.title()} Renown|n"
        else:
            # It's a category filter
            gifts = get_gifts_by_type(filter_arg)
            if not gifts:
                self.caller.msg(f"No gifts found for category: {filter_arg}")
                self.caller.msg("|cValid categories:|n Use |y+lookup gifts|n to see all categories")
                return
            
            title = f"|wWerewolf Gifts - {filter_arg.replace('_', ' ').title()}|n"
        
        # Group by rank
        gifts_by_rank = {1: [], 2: [], 3: [], 4: [], 5: []}
        for gift_key, gift_data in gifts.items():
            rank = gift_data.get('rank', 1)
            gifts_by_rank[rank].append((gift_key, gift_data))
        
        output = [title, ""]
        
        # Display gifts by rank
        for rank in range(1, 6):
            rank_gifts = gifts_by_rank[rank]
            if rank_gifts:
                dots = "●" * rank
                output.append(f"|yRank {dots}|n")
                
                for gift_key, gift_data in sorted(rank_gifts, key=lambda x: x[1]['name']):
                    gift_name = gift_data['name']
                    renown = gift_data['renown'].title()
                    cost = gift_data['cost']
                    
                    output.append(f"  |g{gift_name}|n ({renown}) - Cost: {cost}")
                    output.append(f"    |gUse:|n +lookup {gift_key}")
                
                output.append("")
        
        self.caller.msg("\n".join(output))
        self.caller.msg(f"|cTotal:|n {len(gifts)} gifts")
        self.caller.msg("|cFor gift details:|n +lookup <gift_name> (e.g., +lookup shadow_gaze)")
    
    def show_gift_details(self, gift_key, gift_data):
        """Show detailed information about a specific werewolf gift."""
        msg = f"|w{gift_data['name']} (Werewolf Gift)|n\n"
        
        # Category and Renown
        gift_type = gift_data['gift_type'].replace('_', ' ').title()
        renown = gift_data['renown'].title()
        msg += f"|cGift Type:|n {gift_type}\n"
        msg += f"|cRenown:|n {renown}\n"
        
        # Rank
        rank = gift_data['rank']
        dots = "●" * rank if isinstance(rank, int) else rank
        msg += f"|cRank:|n {dots}\n"
        
        # Cost
        msg += f"|cCost:|n {gift_data['cost']}\n"
        
        # Dice Pool
        if gift_data.get('dice_pool') and gift_data['dice_pool'] != '-':
            msg += f"|cDice Pool:|n {gift_data['dice_pool']}\n"
        
        # Action
        msg += f"|cAction:|n {gift_data['action']}\n"
        
        # Duration
        if gift_data.get('duration') and gift_data['duration'] != '-':
            msg += f"|cDuration:|n {gift_data['duration']}\n"
        
        # Description
        msg += f"|cDescription:|n {gift_data['description']}\n"
        
        # Source
        msg += f"|cSource:|n {gift_data['book']}\n"
        
        # Usage
        msg += f"\n|gTo add to character:|n +stat gift={gift_key}\n"
        
        self.caller.msg(msg)
    
    def show_contract_details(self, contract_key, contract_data):
        """Show detailed information about a specific changeling contract."""
        msg = f"|w{contract_data['name']} (Changeling Contract)|n\n"
        
        # Contract Type
        contract_type = contract_data['contract_type'].replace('_', ' ').title()
        msg += f"|cContract Type:|n {contract_type}\n"
        
        # Cost
        msg += f"|cCost:|n {contract_data['cost']}\n"
        
        # Dice Pool
        if contract_data.get('dice_pool') and contract_data['dice_pool'] != 'None':
            msg += f"|cDice Pool:|n {contract_data['dice_pool']}\n"
        
        # Loopholes
        if contract_data.get('loopholes'):
            msg += f"|cLoopholes:|n {contract_data['loopholes']}\n"
        
        # Description
        msg += f"|cDescription:|n {contract_data['description']}\n"
        
        # Seeming Benefits
        if contract_data.get('seeming_benefits'):
            msg += f"\n|cSeeming Benefits:|n\n"
            for seeming, benefit in contract_data['seeming_benefits'].items():
                if benefit:  # Only show non-empty benefits
                    seeming_title = seeming.title()
                    msg += f"  |y{seeming_title}:|n {benefit}\n"
        
        # Source
        msg += f"\n|cSource:|n {contract_data['book']}\n"
        
        # Usage
        msg += f"\n|gTo add to character:|n +stat contract={contract_key}\n"
        
        self.caller.msg(msg)
    
    def show_changeling_contracts(self, filter_arg=None):
        """Show changeling contracts, optionally filtered by category."""
        from world.cofd.templates.changeling_contracts import (
            get_contracts_by_category, get_all_contracts
        )
        
        if not filter_arg:
            # Show all contract categories
            output = ["|wChangeling Contracts|n", "", "|cAvailable Contract Categories:|n", ""]
            
            # Main contract categories
            main_cats = ["crown", "jewel", "mirror", "shield", "steed", "sword", 
                        "chalice", "coin", "stars", "thorn"]
            
            output.append("|yMain Contracts:|n")
            # Display in 2 columns
            for i in range(0, len(main_cats), 2):
                row = main_cats[i:i+2]
                row_text = "  " + ", ".join([f"{cat}" for cat in row])
                output.append(row_text)
            
            output.append("")
            output.append("|yOther Contracts:|n")
            output.append("  goblin (Independent Contracts)")
            output.append("")
            
            self.caller.msg("\n".join(output))
            self.caller.msg("|cFilter by category:|n +lookup contracts crown, +lookup contracts goblin, etc.")
            self.caller.msg("|cFor contract details:|n +lookup <contract_name> (e.g., +lookup hostile_takeover)")
            return
        
        # Get contracts by category
        contracts = get_contracts_by_category(filter_arg)
        if not contracts:
            self.caller.msg(f"No contracts found for category: {filter_arg}")
            self.caller.msg("|cValid categories:|n Use |y+lookup contracts|n to see all categories")
            return
        
        # Display contracts
        title = f"|wChangeling Contracts - {filter_arg.title()}|n"
        self.caller.msg(title)
        self.caller.msg("=" * len(title.replace("|w", "").replace("|n", "")))
        
        for contract_key, contract_data in contracts.items():
            name = contract_data['name']
            cost = contract_data['cost']
            contract_type = contract_data['contract_type']
            
            # Format contract type for display
            type_display = contract_type.replace('_', ' ').title()
            if 'royal' in contract_type:
                type_display = type_display.replace(' Royal', ' (Royal)')
            
            msg = f"\n|y{name}|n ({type_display})\n"
            msg += f"|cCost:|n {cost}\n"
            
            # Show dice pool if present
            if contract_data.get('dice_pool') and contract_data['dice_pool'] != 'None':
                msg += f"|cDice Pool:|n {contract_data['dice_pool']}\n"
            
            # Show loopholes if present
            if contract_data.get('loopholes'):
                msg += f"|cLoopholes:|n {contract_data['loopholes']}\n"
            
            # Show description (truncated)
            description = contract_data['description']
            if len(description) > 150:
                description = description[:147] + "..."
            msg += f"|cDescription:|n {description}\n"
            
            # Show source
            msg += f"|cSource:|n {contract_data['book']}\n"
            
            self.caller.msg(msg)
        
        self.caller.msg(f"\n|cTotal:|n {len(contracts)} contracts in {filter_arg.title()} category")
        self.caller.msg(f"\n|cNote:|n Set with: |y+stat contract=<name>|n")
    
    def show_geist_keys(self):
        """Show all Geist keys."""
        from evennia.utils import evtable
        
        keys_data = LOOKUP_DATA.geist_data['keys_detailed']
        
        output = ["|wGeist Keys|n", ""]
        output.append("|cAll nine Keys unlock specific types of Haunts based on associated Attributes:|n")
        output.append("")
        
        # Show all keys with their attributes
        for key_name in sorted(keys_data.keys()):
            key_data = keys_data[key_name]
            full_name = key_data['full_name']
            attribute = key_data['attribute']
            description = key_data['description']
            
            output.append(f"|g{full_name}|n (|c{attribute}|n)")
            output.append(f"  {description}")
            output.append(f"  |gUse:|n +lookup keys {key_name}")
            output.append("")
        
        self.caller.msg("\n".join(output))
        self.caller.msg("|cFor key details:|n +lookup keys <key_name> (e.g., +lookup keys beasts)")
    
    def show_geist_key(self, key_name):
        """Show detailed information about a specific Geist key."""
        keys_data = LOOKUP_DATA.geist_data['keys_detailed']
        
        # Normalize key name
        key_name = key_name.lower().replace(" ", " ")
        
        # Try to find the key
        key_data = keys_data.get(key_name)
        
        if not key_data:
            self.caller.msg(f"Key '{key_name}' not found.")
            self.caller.msg("|cUse:|n +lookup keys - to see all available keys")
            return
        
        msg = f"|w{key_data['full_name']}|n\n"
        msg += f"|cAttribute:|n {key_data['attribute']}\n"
        
        if key_data.get('alternate_names'):
            msg += f"|cAlso Known As:|n {key_data['alternate_names']}\n"
        
        msg += f"\n|cDescription:|n {key_data['description']}\n"
        msg += f"\n|rDoom:|n {key_data['doom']}\n"
        msg += f"\n|cSource:|n {key_data['book']}\n"
        
        self.caller.msg(msg)
    
    def show_geist_haunts(self):
        """Show all Geist haunts."""
        haunts_data = LOOKUP_DATA.geist_data['haunts_detailed']
        
        output = ["|wGeist Haunts|n", ""]
        output.append("|cHaunts are the supernatural powers of the Bound, rated from 1 to 5 dots:|n")
        output.append("")
        
        # List all haunts
        for haunt_name in sorted(haunts_data.keys()):
            haunt_display = haunt_name.replace("_", " ").title()
            output.append(f"|g{haunt_display}|n")
            output.append(f"  |gUse:|n +lookup haunts {haunt_name}")
        
        output.append("")
        self.caller.msg("\n".join(output))
        self.caller.msg("|cFor haunt details:|n +lookup haunts <haunt_name> (e.g., +lookup haunts boneyard)")
    
    def show_geist_haunt(self, haunt_name):
        """Show detailed information about a specific Geist haunt."""
        haunts_data = LOOKUP_DATA.geist_data['haunts_detailed']
        
        # Normalize haunt name
        haunt_name = haunt_name.lower().replace(" ", "_")
        
        # Try to find the haunt
        haunt_powers = haunts_data.get(haunt_name)
        
        if not haunt_powers:
            self.caller.msg(f"Haunt '{haunt_name}' not found.")
            self.caller.msg("|cUse:|n +lookup haunts - to see all available haunts")
            return
        
        haunt_display = haunt_name.replace("_", " ").title()
        output = [f"|wThe {haunt_display}|n", ""]
        
        # Group powers by rank
        powers_by_rank = {1: [], 2: [], 3: [], 4: [], 5: []}
        for power_key, power_data in haunt_powers.items():
            rank = power_data.get('rank', 1)
            powers_by_rank[rank].append((power_key, power_data))
        
        # Display powers by rank
        for rank in range(1, 6):
            rank_powers = powers_by_rank[rank]
            if rank_powers:
                dots = "●" * rank
                output.append(f"|yRank {dots}|n")
                
                for power_key, power_data in rank_powers:
                    power_name = power_data['name']
                    cost = power_data['cost']
                    description = power_data['description']
                    
                    output.append(f"  |g{power_name}|n - Cost: {cost}")
                    output.append(f"    {description}")
                    
                    if power_data.get('additional'):
                        output.append(f"    |cAdditional:|n {power_data['additional']}")
                    
                    output.append(f"    |cSource:|n {power_data['book']}")
                    output.append("")
        
        self.caller.msg("\n".join(output))
        self.caller.msg(f"|cTotal:|n {len(haunt_powers)} powers in {haunt_display}")
        self.caller.msg(f"|cNote:|n Set haunt rating with: |y+stat {haunt_name}=<dots>|n")
    
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
        
        # Display in columns (adjusted to 25 chars to fit 78-char limit: 2 indent + 25*3 = 77)
        col_width = 25
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
        
        # Display in columns (adjusted to 25 chars to fit 78-char limit: 2 indent + 25*3 = 77)
        col_width = 25
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
        
        # Display in columns (adjusted to 25 chars to fit 78-char limit: 2 indent + 25*3 = 77)
        col_width = 25
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
        
        # Display in columns (adjusted to 25 chars to fit 78-char limit: 2 indent + 25*3 = 77)
        col_width = 25
        for i in range(0, len(powers), 3):
            row = powers[i:i+3]
            msg += "  " + "".join([f"|c{p:<{col_width}}|n" for p in row]) + "\n"
        
        msg += f"\n|cTotal:|n {len(powers)} Psychic Powers\n"
        msg += f"\n|cNote:|n Set with: |y+stat psychic=<power>|n (e.g., +stat psychic=telepathy)"
        self.caller.msg(msg)
    
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
                elif stat_type == 'discipline_power':
                    formatted_results.append(f"|wDiscipline Power:|n {name} ({data['discipline'].title()})")
                elif stat_type == 'gift':
                    gift_type = data.get('gift_type', 'gift').replace('_', ' ').title()
                    formatted_results.append(f"|wWerewolf Gift:|n {name} ({gift_type})")
                elif stat_type == 'ritual':
                    ritual_type = data.get('type', 'ritual').title()
                    formatted_results.append(f"|w{ritual_type.title()}:|n {name}")
                elif stat_type == 'arcanum':
                    formatted_results.append(f"|wArcanum:|n {name.title()}")
            
            msg += "\n".join(formatted_results)
            if len(search_results) > 20:
                msg += f"\n\n|y... and {len(search_results) - 20} more results.|n"
            msg += f"\n\n|cUse:|n |y+lookup <stat_name>|n for detailed information."
        else:
            msg = f"No results found for '{self.args}'."
        
        self.caller.msg(msg)
    

