"""
Staff commands for managing the mystery investigation system.

These commands allow storytellers and staff to create, modify, and manage
mysteries and clues that players can discover through roleplay.
"""

from evennia.commands.default.muxcommand import MuxCommand
from evennia.utils import evtable, search
from evennia.utils.ansi import ANSIString
from world.utils.permission_utils import check_staff_permission, check_mystery_permission
from typeclasses.mysteries import Mystery, ClueObject, MysteryManager
from django.utils import timezone
import json


class CmdMysteryAdmin(MuxCommand):
    """
    Staff command for managing mysteries and investigations.
    
    Usage:
        +mystery/create <title> = <description>
        +mystery/list [category]
        +mystery/view <mystery_id>
        +mystery/edit <mystery_id>/<field> = <value>
        +mystery/delete <mystery_id>
        +mystery/status <mystery_id> = <active|solved|suspended>
        
        +mystery/addclue <mystery_id> = <name>/<description>
        +mystery/editclue <mystery_id>/<clue_id> = <field>/<value>
        +mystery/delclue <mystery_id>/<clue_id>
        +mystery/prereq <mystery_id>/<clue_id> = <prerequisite_clue_ids>
        +mystery/leads <mystery_id>/<clue_id> = <leads_to_clue_ids>
        
        +mystery/conditions <mystery_id>/<clue_id> = <conditions_json>
        +mystery/revelation <mystery_id>/<trigger_id> = <required_clues>/<revelation>
        +mystery/access <mystery_id> = <templates|characters|areas>
        
        +mystery/progress [mystery_id]
        +mystery/discovered <mystery_id> [character]
        +mystery/grant <character> = <mystery_id>/<clue_id>
        +mystery/revoke <character> = <mystery_id>/<clue_id>
        
        +mystery/templates - List available mystery templates
        +mystery/template <template_name> = [custom_title] - Create from template
        
    Examples:
        +mystery/create The Missing Heir = A wealthy family's heir has vanished
        +mystery/addclue mystery_1 = Torn Letter/A letter with half the address torn off
        +mystery/prereq mystery_1/clue_1 = clue_0
        +mystery/conditions mystery_1/clue_2 = {"skill_roll": {"skill": "investigation", "difficulty": 3}}
        +mystery/grant Alice = mystery_1/clue_1
    """
    
    key = "+mystery"
    aliases = ["+mysteries", "+mystadmin"]
    help_category = "Storytelling Commands"
    locks = "cmd:all()"
    
    def func(self):
        """Execute the command."""
        if not check_mystery_permission(self.caller):
            self.caller.msg("You don't have permission to manage mysteries. You need Staff or Storyteller permissions.")
            return
            
        if not self.switches:
            self.show_help()
            return
            
        switch = self.switches[0].lower()
        
        if switch == "create":
            self.create_mystery()
        elif switch == "list":
            self.list_mysteries()
        elif switch == "view":
            self.view_mystery()
        elif switch == "edit":
            self.edit_mystery()
        elif switch == "delete":
            self.delete_mystery()
        elif switch == "status":
            self.set_status()
        elif switch == "addclue":
            self.add_clue()
        elif switch == "editclue":
            self.edit_clue()
        elif switch == "delclue":
            self.delete_clue()
        elif switch == "prereq":
            self.set_prerequisites()
        elif switch == "leads":
            self.set_leads()
        elif switch == "conditions":
            self.set_conditions()
        elif switch == "revelation":
            self.add_revelation()
        elif switch == "access":
            self.set_access()
        elif switch == "progress":
            self.show_progress()
        elif switch == "discovered":
            self.show_discovered()
        elif switch == "grant":
            self.grant_clue()
        elif switch == "revoke":
            self.revoke_clue()
        elif switch == "templates":
            self.list_templates()
        elif switch == "template":
            self.create_from_template()
        else:
            self.caller.msg("Invalid switch. Use +mystery without arguments for help.")
    
    def show_help(self):
        """Show command help."""
        help_text = """
|c+mystery|n - Mystery Management System

|yCreation & Management:|n
  |w+mystery/create|n <title> = <description>
  |w+mystery/list|n [category] - List mysteries
  |w+mystery/view|n <mystery_id> - View mystery details
  |w+mystery/edit|n <mystery_id>/<field> = <value>
  |w+mystery/delete|n <mystery_id>
  |w+mystery/status|n <mystery_id> = <active|solved|suspended>

|yClue Management:|n
  |w+mystery/addclue|n <mystery_id> = <name>/<description>
  |w+mystery/editclue|n <mystery_id>/<clue_id> = <field>/<value>
  |w+mystery/delclue|n <mystery_id>/<clue_id>
  |w+mystery/prereq|n <mystery_id>/<clue_id> = <clue_ids>
  |w+mystery/leads|n <mystery_id>/<clue_id> = <clue_ids>

|yAdvanced Features:|n
  |w+mystery/conditions|n <mystery_id>/<clue_id> = <json>
  |w+mystery/revelation|n <mystery_id>/<trigger> = <clues>/<text>
  |w+mystery/access|n <mystery_id> = <restrictions>

|yTracking & Management:|n
  |w+mystery/progress|n [mystery_id] - Show progress
  |w+mystery/discovered|n <mystery_id> [character]
  |w+mystery/grant|n <character> = <mystery_id>/<clue_id>
  |w+mystery/revoke|n <character> = <mystery_id>/<clue_id>
        """
        self.caller.msg(help_text)
    
    def create_mystery(self):
        """Create a new mystery."""
        if "=" not in self.args:
            self.caller.msg("Usage: +mystery/create <title> = <description>")
            return
            
        title, description = [x.strip() for x in self.args.split("=", 1)]
        
        mystery = MysteryManager.create_mystery(
            title=title,
            description=description,
            created_by=self.caller.id
        )
        
        self.caller.msg(f"|gCreated mystery:|n {title} (ID: {mystery.id})")
        self.caller.msg(f"|yDescription:|n {description}")
    
    def list_mysteries(self):
        """List all mysteries."""
        category = self.args.strip() if self.args else None
        mysteries = MysteryManager.get_active_mysteries()
        
        if category:
            mysteries = [m for m in mysteries if m.db.category == category]
        
        if not mysteries:
            self.caller.msg("No mysteries found.")
            return
        
        table = evtable.EvTable(
            "|cID|n", "|cTitle|n", "|cCategory|n", "|cProgress|n", "|cStatus|n",
            border="table", align="l"
        )
        
        for mystery in mysteries:
            table.add_row(
                mystery.id,
                mystery.db.title[:30],
                mystery.db.category,
                f"{mystery.db.completion_percentage}%",
                mystery.db.status
            )
        
        self.caller.msg(f"|cActive Mysteries:|n\n{table}")
    
    def view_mystery(self):
        """View detailed mystery information."""
        if not self.args:
            self.caller.msg("Usage: +mystery/view <mystery_id>")
            return
            
        mystery_id = self.args.strip()
        mystery = self._get_mystery(mystery_id)
        if not mystery:
            return
        
        # Basic info
        output = [
            f"|c=== Mystery: {mystery.db.title} ===|n",
            f"|yID:|n {mystery.id}",
            f"|yDescription:|n {mystery.db.description}",
            f"|yCategory:|n {mystery.db.category}",
            f"|yDifficulty:|n {mystery.db.difficulty}/5",
            f"|yStatus:|n {mystery.db.status}",
            f"|yProgress:|n {mystery.db.completion_percentage}%",
            f"|yCreated:|n {mystery.db.created_date.strftime('%Y-%m-%d %H:%M')}",
            ""
        ]
        
        # Clues
        if mystery.db.clues:
            output.append("|yClues:|n")
            for clue_id, clue in mystery.db.clues.items():
                discovered_count = len(clue['discovered_by'])
                tags = ", ".join(clue['tags']) if clue['tags'] else "None"
                prereqs = ", ".join(clue['prerequisite_clues']) if clue['prerequisite_clues'] else "None"
                
                output.append(f"  |w{clue_id}:|n {clue['name']}")
                output.append(f"    Description: {clue['description'][:50]}...")
                output.append(f"    Discovered by: {discovered_count} character(s)")
                output.append(f"    Tags: {tags}")
                output.append(f"    Prerequisites: {prereqs}")
                output.append("")
        else:
            output.append("|yClues:|n None")
        
        # Access restrictions
        if mystery.db.allowed_templates:
            output.append(f"|yAllowed Templates:|n {', '.join(mystery.db.allowed_templates)}")
        if mystery.db.allowed_characters:
            output.append(f"|yAllowed Characters:|n {len(mystery.db.allowed_characters)} specific")
        if mystery.db.restricted_areas:
            output.append(f"|yRestricted Areas:|n {', '.join(mystery.db.restricted_areas)}")
        
        self.caller.msg("\n".join(output))
    
    def add_clue(self):
        """Add a clue to a mystery."""
        if "=" not in self.args:
            self.caller.msg("Usage: +mystery/addclue <mystery_id> = <name>/<description>")
            return
            
        mystery_id, clue_info = [x.strip() for x in self.args.split("=", 1)]
        
        if "/" not in clue_info:
            self.caller.msg("Usage: +mystery/addclue <mystery_id> = <name>/<description>")
            return
            
        name, description = [x.strip() for x in clue_info.split("/", 1)]
        
        mystery = self._get_mystery(mystery_id)
        if not mystery:
            return
        
        clue_id = mystery.add_clue(name, description)
        self.caller.msg(f"|gAdded clue to {mystery.db.title}:|n {name} (ID: {clue_id})")
    
    def set_prerequisites(self):
        """Set prerequisite clues for a clue."""
        if "=" not in self.args:
            self.caller.msg("Usage: +mystery/prereq <mystery_id>/<clue_id> = <prerequisite_clue_ids>")
            return
            
        clue_path, prereqs = [x.strip() for x in self.args.split("=", 1)]
        
        if "/" not in clue_path:
            self.caller.msg("Usage: +mystery/prereq <mystery_id>/<clue_id> = <prerequisite_clue_ids>")
            return
            
        mystery_id, clue_id = [x.strip() for x in clue_path.split("/", 1)]
        prereq_list = [x.strip() for x in prereqs.split(",") if x.strip()]
        
        mystery = self._get_mystery(mystery_id)
        if not mystery:
            return
            
        if clue_id not in mystery.db.clues:
            self.caller.msg(f"Clue {clue_id} not found in mystery {mystery_id}")
            return
        
        mystery.set_clue_prerequisites(clue_id, prereq_list)
        self.caller.msg(f"|gSet prerequisites for {clue_id}:|n {', '.join(prereq_list)}")
    
    def set_conditions(self):
        """Set discovery conditions for a clue."""
        if "=" not in self.args:
            self.caller.msg("Usage: +mystery/conditions <mystery_id>/<clue_id> = <conditions_json>")
            return
            
        clue_path, conditions_str = [x.strip() for x in self.args.split("=", 1)]
        
        if "/" not in clue_path:
            self.caller.msg("Usage: +mystery/conditions <mystery_id>/<clue_id> = <conditions_json>")
            return
            
        mystery_id, clue_id = [x.strip() for x in clue_path.split("/", 1)]
        
        mystery = self._get_mystery(mystery_id)
        if not mystery:
            return
            
        if clue_id not in mystery.db.clues:
            self.caller.msg(f"Clue {clue_id} not found in mystery {mystery_id}")
            return
        
        try:
            conditions = json.loads(conditions_str)
        except json.JSONDecodeError:
            self.caller.msg("Invalid JSON format for conditions.")
            return
        
        mystery.db.clues[clue_id]['discovery_conditions'] = conditions
        self.caller.msg(f"|gSet discovery conditions for {clue_id}|n")
    
    def add_revelation(self):
        """Add an automatic revelation trigger."""
        if "=" not in self.args:
            self.caller.msg("Usage: +mystery/revelation <mystery_id>/<trigger_id> = <required_clues>/<revelation>")
            return
            
        trigger_path, revelation_info = [x.strip() for x in self.args.split("=", 1)]
        
        if "/" not in trigger_path or "/" not in revelation_info:
            self.caller.msg("Usage: +mystery/revelation <mystery_id>/<trigger_id> = <required_clues>/<revelation>")
            return
            
        mystery_id, trigger_id = [x.strip() for x in trigger_path.split("/", 1)]
        required_clues, revelation_text = [x.strip() for x in revelation_info.split("/", 1)]
        
        mystery = self._get_mystery(mystery_id)
        if not mystery:
            return
        
        clue_list = [x.strip() for x in required_clues.split(",")]
        mystery.add_revelation_trigger(trigger_id, clue_list, revelation_text)
        
        self.caller.msg(f"|gAdded revelation trigger {trigger_id} to {mystery.db.title}|n")
    
    def grant_clue(self):
        """Manually grant a clue to a character."""
        if "=" not in self.args:
            self.caller.msg("Usage: +mystery/grant <character> = <mystery_id>/<clue_id>")
            return
            
        char_name, clue_path = [x.strip() for x in self.args.split("=", 1)]
        
        if "/" not in clue_path:
            self.caller.msg("Usage: +mystery/grant <character> = <mystery_id>/<clue_id>")
            return
            
        mystery_id, clue_id = [x.strip() for x in clue_path.split("/", 1)]
        
        character = self.caller.search(char_name, global_search=True)
        if not character:
            return
        character = character[0]
        
        mystery = self._get_mystery(mystery_id)
        if not mystery:
            return
        
        success, msg = mystery.discover_clue(character, clue_id, "staff_grant")
        if success:
            self.caller.msg(f"|gGranted clue to {character.name}:|n {msg}")
            character.msg(f"|yA staff member has granted you a clue:|n {msg}")
        else:
            self.caller.msg(f"|rFailed to grant clue:|n {msg}")
    
    def list_templates(self):
        """List available mystery templates."""
        from world.mystery_templates import list_templates, MYSTERY_TEMPLATES
        
        templates = list_templates()
        
        if not templates:
            self.caller.msg("No mystery templates available.")
            return
        
        output = ["|cAvailable Mystery Templates:|n"]
        
        for template_name in templates:
            template_class = MYSTERY_TEMPLATES[template_name]
            template_instance = template_class()
            
            output.append(f"|w{template_name}|n")
            output.append(f"  Title: {template_instance.title}")
            output.append(f"  Category: {template_instance.category}")
            output.append(f"  Difficulty: {template_instance.difficulty}/5")
            output.append(f"  Clues: {len(template_instance.clues)}")
            output.append(f"  Description: {template_instance.description[:60]}...")
            output.append("")
        
        output.append("|yUsage:|n +mystery/template <template_name> = [custom_title]")
        
        self.caller.msg("\n".join(output))
    
    def create_from_template(self):
        """Create a mystery from a template."""
        from world.mystery_templates import create_mystery_from_template
        
        if "=" in self.args:
            template_name, custom_title = [x.strip() for x in self.args.split("=", 1)]
        else:
            template_name = self.args.strip()
            custom_title = None
        
        if not template_name:
            self.caller.msg("Usage: +mystery/template <template_name> = [custom_title]")
            return
        
        mystery = create_mystery_from_template(
            template_name=template_name,
            created_by=self.caller.id,
            custom_title=custom_title
        )
        
        if mystery:
            title = custom_title if custom_title else mystery.db.title
            self.caller.msg(f"|gCreated mystery from template:|n {title} (ID: {mystery.id})")
            self.caller.msg(f"|yTemplate:|n {template_name}")
            self.caller.msg(f"|yClues:|n {len(mystery.db.clues)} clues ready for discovery")
            self.caller.msg(f"|yUse:|n +mystery/view {mystery.id} to see details")
        else:
            self.caller.msg(f"|rTemplate '{template_name}' not found.|n")
            self.caller.msg("Use +mystery/templates to see available templates.")
    
    def show_progress(self):
        """Show mystery progress."""
        if self.args:
            mystery_id = self.args.strip()
            mystery = self._get_mystery(mystery_id)
            if not mystery:
                return
            mysteries = [mystery]
        else:
            mysteries = MysteryManager.get_active_mysteries()
        
        for mystery in mysteries:
            total_clues = len(mystery.db.clues)
            discovered_count = len(set().union(*mystery.db.discovered_clues.values())) if mystery.db.discovered_clues else 0
            
            self.caller.msg(f"|c{mystery.db.title}|n (ID: {mystery.id})")
            self.caller.msg(f"  Progress: {mystery.db.completion_percentage}% ({discovered_count}/{total_clues} clues discovered)")
            self.caller.msg(f"  Participants: {len(mystery.db.discovered_clues)} characters")
            self.caller.msg("")
    
    def _get_mystery(self, mystery_id):
        """Get a mystery by ID."""
        try:
            mystery_id = int(mystery_id)
        except ValueError:
            self.caller.msg("Mystery ID must be a number.")
            return None
        
        mystery = search.search_object(f"#{mystery_id}")
        if not mystery or not isinstance(mystery[0], Mystery):
            self.caller.msg(f"Mystery {mystery_id} not found.")
            return None
        
        return mystery[0]


class CmdClueObject(MuxCommand):
    """
    Create discoverable clue objects in rooms.
    
    Usage:
        +clueobj/create <name> = <mystery_id>/<clue_id>
        +clueobj/edit <clue_object> = <field>/<value>
        +clueobj/list [here]
        +clueobj/delete <clue_object>
        
    Examples:
        +clueobj/create torn letter = mystery_1/clue_2
        +clueobj/edit torn letter = discovery_message/You notice a letter under the desk
        +clueobj/edit torn letter = skill_required/investigation
        +clueobj/edit torn letter = difficulty/3
    """
    
    key = "+clueobj"
    aliases = ["+clueobject"]
    help_category = "Storytelling Commands"
    locks = "cmd:all()"
    
    def func(self):
        """Execute the command."""
        if not check_mystery_permission(self.caller):
            self.caller.msg("You don't have permission to create clue objects. You need Staff or Storyteller permissions.")
            return
            
        if not self.switches:
            self.caller.msg("Usage: +clueobj/create, +clueobj/edit, +clueobj/list, or +clueobj/delete")
            return
            
        switch = self.switches[0].lower()
        
        if switch == "create":
            self.create_clue_object()
        elif switch == "edit":
            self.edit_clue_object()
        elif switch == "list":
            self.list_clue_objects()
        elif switch == "delete":
            self.delete_clue_object()
        else:
            self.caller.msg("Invalid switch.")
    
    def create_clue_object(self):
        """Create a new clue object."""
        if "=" not in self.args:
            self.caller.msg("Usage: +clueobj/create <name> = <mystery_id>/<clue_id>")
            return
            
        name, clue_path = [x.strip() for x in self.args.split("=", 1)]
        
        if "/" not in clue_path:
            self.caller.msg("Usage: +clueobj/create <name> = <mystery_id>/<clue_id>")
            return
            
        mystery_id, clue_id = [x.strip() for x in clue_path.split("/", 1)]
        
        # Create the clue object
        clue_obj = ClueObject.create(
            name,
            location=self.caller.location,
            home=self.caller.location
        )
        
        clue_obj.db.mystery_id = mystery_id
        clue_obj.db.clue_id = clue_id
        clue_obj.db.desc = f"This appears to be related to an ongoing investigation."
        
        self.caller.msg(f"|gCreated clue object:|n {name} linked to {mystery_id}/{clue_id}")
    
    def edit_clue_object(self):
        """Edit a clue object's properties."""
        if "=" not in self.args:
            self.caller.msg("Usage: +clueobj/edit <object> = <field>/<value>")
            return
            
        obj_name, edit_info = [x.strip() for x in self.args.split("=", 1)]
        
        if "/" not in edit_info:
            self.caller.msg("Usage: +clueobj/edit <object> = <field>/<value>")
            return
            
        field, value = [x.strip() for x in edit_info.split("/", 1)]
        
        clue_obj = self.caller.search(obj_name)
        if not clue_obj or not isinstance(clue_obj, ClueObject):
            self.caller.msg("Clue object not found.")
            return
        
        if field in ['discovery_message', 'skill_required', 'difficulty', 'hidden']:
            if field == 'difficulty':
                try:
                    value = int(value)
                except ValueError:
                    self.caller.msg("Difficulty must be a number.")
                    return
            elif field == 'hidden':
                value = value.lower() in ['true', '1', 'yes']
            
            setattr(clue_obj.db, field, value)
            self.caller.msg(f"|gUpdated {obj_name}.{field} to:|n {value}")
        else:
            self.caller.msg("Valid fields: discovery_message, skill_required, difficulty, hidden")
    
    def list_clue_objects(self):
        """List clue objects in the area."""
        if self.args and self.args.strip().lower() == "here":
            objects = [obj for obj in self.caller.location.contents if isinstance(obj, ClueObject)]
        else:
            objects = ClueObject.objects.all()
        
        if not objects:
            self.caller.msg("No clue objects found.")
            return
        
        table = evtable.EvTable(
            "|cName|n", "|cLocation|n", "|cMystery/Clue|n", "|cDiscovered|n",
            border="table", align="l"
        )
        
        for obj in objects:
            location_name = obj.location.name if obj.location else "None"
            mystery_clue = f"{obj.db.mystery_id}/{obj.db.clue_id}"
            discovered_count = len(obj.db.discovered_by)
            
            table.add_row(
                obj.name,
                location_name,
                mystery_clue,
                discovered_count
            )
        
        self.caller.msg(f"|cClue Objects:|n\n{table}")
