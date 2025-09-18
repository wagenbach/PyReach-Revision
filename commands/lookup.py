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
        +lookup merits [type]                - List merits, optionally by type
        +lookup merits/vampire               - List vampire-specific merits
        +lookup disciplines                  - List vampire disciplines
        +lookup arcana                       - List mage arcana
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
            if len(parts) > 1 and parts[1] == "vampire":
                self.show_vampire_merits()
            else:
                merit_type = parts[1] if len(parts) > 1 else None
                self.show_merits(merit_type)
        elif args == "disciplines":
            self.show_disciplines()
        elif args == "arcana":
            self.show_arcana()
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
        else:
            # Try to find specific stat
            self.show_stat_details(args)
    
    def show_categories(self):
        """Show available lookup categories."""
        msg = "|wCharacter Creation Lookup System|n\n"
        msg += "|cAvailable Categories:|n\n"
        msg += "  |yattributes|n       - List all 9 core attributes\n"
        msg += "  |yskills [type]|n    - List skills (mental/physical/social)\n"
        msg += "  |ymerits [type]|n    - List merits by type\n"
        msg += "  |ymerits/vampire|n   - List vampire-specific merits\n"
        msg += "  |ydisciplines|n      - List vampire disciplines\n"
        msg += "  |yarcana|n           - List mage arcana\n"
        msg += "  |yclans|n            - List vampire clans\n"
        msg += "  |ycovenants|n        - List vampire covenants\n"
        msg += "  |ypaths|n            - List mage paths\n"
        msg += "  |yorders|n           - List mage orders\n"
        msg += "  |yauspices|n         - List werewolf auspices\n"
        msg += "  |ytribes|n           - List werewolf tribes\n"
        msg += "  |yseeings|n          - List changeling seemings\n"
        msg += "  |ycourts|n           - List changeling courts\n"
        msg += "  |yincarnations|n     - List demon incarnations\n"
        msg += "  |yagendas|n          - List demon agendas\n"
        msg += "  |yembeds|n           - List demon embeds\n"
        msg += "  |yexploits|n         - List demon exploits\n"
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
    
    def show_merits(self, merit_type=None):
        """Show general merits, optionally filtered by type."""
        if merit_type and merit_type not in ["mental", "physical", "social", "supernatural", "fighting", "style"]:
            self.caller.msg("Valid merit types: mental, physical, social, supernatural, fighting, style")
            return
        
        table = evtable.EvTable("|wMerit|n", "|wType|n", "|wDots|n", "|wPrerequisites|n",
                               border="cells", width=78)
        
        filtered_merits = LOOKUP_DATA.get_merits_by_type(merit_type, 'general')
        
        for merit in filtered_merits:
            # Color code by type
            type_colors = {
                "mental": "|c", "physical": "|y", "social": "|m",
                "supernatural": "|r", "fighting": "|R", "style": "|g"
            }
            color = type_colors.get(merit.merit_type, "|w")
            
            merit_name = f"{color}{merit.name}|n"
            merit_type_display = f"{color}{merit.merit_type.title()}|n"
            
            if merit.min_value == merit.max_value:
                dots = str(merit.min_value)
            else:
                dots = f"{merit.min_value}-{merit.max_value}"
            
            prereq = LOOKUP_DATA.format_prerequisites_display(merit.prerequisite)
            
            table.add_row(merit_name, merit_type_display, dots, prereq)
        
        title = f"|wGeneral Merits"
        if merit_type:
            title += f" - {merit_type.title()}"
        title += f" ({len(filtered_merits)} total)|n"
        
        self.caller.msg(f"{title}\n{table}")
        self.caller.msg(f"\n|cUse:|n |y+lookup <merit_name>|n for detailed information on any merit.")
    
    def show_vampire_merits(self):
        """Show vampire-specific merits."""
        table = evtable.EvTable("|wMerit|n", "|wType|n", "|wDots|n", "|wPrerequisites|n",
                               border="cells", width=78)
        
        sorted_merits = LOOKUP_DATA.get_merits_by_type(None, 'vampire')
        
        for merit in sorted_merits:
            # Color code by type
            type_colors = {
                "mental": "|c", "physical": "|y", "social": "|m",
                "supernatural": "|r", "fighting": "|R", "style": "|g"
            }
            color = type_colors.get(merit.merit_type, "|w")
            
            merit_name = f"{color}{merit.name}|n"
            merit_type_display = f"{color}{merit.merit_type.title()}|n"
            
            if merit.min_value == merit.max_value:
                dots = str(merit.min_value)
            else:
                dots = f"{merit.min_value}-{merit.max_value}"
            
            prereq = LOOKUP_DATA.format_prerequisites_display(merit.prerequisite)
            
            table.add_row(merit_name, merit_type_display, dots, prereq)
        
        self.caller.msg(f"|wVampire Merits ({len(sorted_merits)} total)|n\n{table}")
        self.caller.msg(f"\n|cUse:|n |y+lookup <merit_name>|n for detailed information on any merit.")
    
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
                    "demon", "geist", "promethean", "hunter", "mummy", "beast", "deviant"]
        
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
    

