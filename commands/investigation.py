from evennia.commands.default.muxcommand import MuxCommand
from evennia.utils import create, evtable
from evennia.utils.ansi import ANSIString
from world.experience import ExperienceHandler
from typeclasses.mysteries import MysteryManager
import random

class CmdInvestigation(MuxCommand):
    """
    Manage investigations and clues.
    
    Personal Clues:
        +investigation/clue <name> = <description> - Create a personal clue
        +investigation/element <clue> = <description> - Add an element to a personal clue
        +investigation/tag <clue> <tag> - Add a tag to a personal clue
        +investigation/list - List your personal clues
        +investigation/view <clue> - View a personal clue's details
        +investigation/spend <clue> <element> - Spend a clue element
        +investigation/truth <clue1> <clue2> [clue3...] - Attempt to uncover truth
        
    Mystery System:
        +investigation/mysteries - List active mysteries you can participate in
        +investigation/mystery <mystery_id> - View mystery details and your progress
        +investigation/investigate <area|object|person> - Attempt to discover clues
        +investigation/share <character> = <clue> - Share a clue with another character
        +investigation/collaborate <character> - Combine investigation efforts
        +investigation/progress [mystery_id] - Show your investigation progress
        
    Discovery Methods:
        +investigation/examine <object> - Carefully examine an object for clues
        +investigation/search <area> - Search an area for hidden clues
        +investigation/interview <character> - Interview someone for information
        +investigation/research <topic> - Research a topic (requires library/resources)
        
    Tags:
        incomplete - Clue needs more investigation
        tainted - Clue may be misleading
        critical - Important clue for solving mystery
        shared - Clue shared with other investigators
    """
    key = "+investigation"
    aliases = ["+inv"]
    help_category = "Roleplaying Tools"
    def parse(self):
        """Parse the command arguments."""
        super().parse()  # Initialize switches and other MuxCommand attributes
        
        args = self.args.strip()
        self.switches = []
    
    def func(self):
        """Execute the command"""
        if not self.switches:
            self.caller.msg("Use +investigation with a switch. See 'help +investigation' for all options.")
            return
            
        switch = self.switches[0].lower()
        
        # Personal clue management (original functionality)
        if switch == "clue":
            self.create_clue()
        elif switch == "element":
            self.add_element()
        elif switch == "tag":
            self.add_tag()
        elif switch == "list":
            self.list_clues()
        elif switch == "view":
            self.view_clue()
        elif switch == "spend":
            self.spend_element()
        elif switch == "truth":
            self.uncover_truth()
        # New mystery system functionality
        elif switch == "mysteries":
            self.list_mysteries()
        elif switch == "mystery":
            self.view_mystery()
        elif switch == "investigate":
            self.investigate()
        elif switch == "share":
            self.share_clue()
        elif switch == "collaborate":
            self.collaborate()
        elif switch == "progress":
            self.show_progress()
        elif switch == "examine":
            self.examine_for_clues()
        elif switch == "search":
            self.search_for_clues()
        elif switch == "interview":
            self.interview()
        elif switch == "research":
            self.research()
        else:
            self.caller.msg("Invalid switch. See 'help +investigation' for usage.")
    
    def create_clue(self):
        """Create a new clue"""
        if "=" not in self.args:
            self.caller.msg("Usage: +investigation/clue <name> = <description>")
            return
            
        name, description = [part.strip() for part in self.args.split("=", 1)]
        
        # Initialize clues if not exists
        if not self.caller.db.clues:
            self.caller.db.clues = {}
            
        if name in self.caller.db.clues:
            self.caller.msg(f"A clue named '{name}' already exists")
            return
            
        self.caller.db.clues[name] = {
            "description": description,
            "elements": [],
            "tags": [],
            "spent_elements": []
        }
        
        self.caller.msg(f"Created new clue: {name}")
        self.caller.msg(f"Description: {description}")
    
    def add_element(self):
        """Add an element to a clue"""
        if "=" not in self.args:
            self.caller.msg("Usage: +investigation/element <clue> = <description>")
            return
            
        clue_name, element_desc = [part.strip() for part in self.args.split("=", 1)]
        
        if not self.caller.db.clues or clue_name not in self.caller.db.clues:
            self.caller.msg(f"No clue named '{clue_name}' found")
            return
            
        self.caller.db.clues[clue_name]["elements"].append(element_desc)
        self.caller.msg(f"Added element to {clue_name}: {element_desc}")
    
    def add_tag(self):
        """Add a tag to a clue"""
        try:
            clue_name, tag = self.args.split()
        except ValueError:
            self.caller.msg("Usage: +investigation/tag <clue> <tag>")
            return
            
        if not self.caller.db.clues or clue_name not in self.caller.db.clues:
            self.caller.msg(f"No clue named '{clue_name}' found")
            return
            
        if tag not in ["incomplete", "tainted"]:
            self.caller.msg("Invalid tag. Use: incomplete or tainted")
            return
            
        if tag in self.caller.db.clues[clue_name]["tags"]:
            self.caller.msg(f"Clue already has tag '{tag}'")
            return
            
        self.caller.db.clues[clue_name]["tags"].append(tag)
        self.caller.msg(f"Added tag '{tag}' to {clue_name}")
    
    def list_clues(self):
        """List all clues"""
        if not self.caller.db.clues:
            self.caller.msg("You have no clues")
            return
            
        output = ["Your clues:"]
        for name, clue in self.caller.db.clues.items():
            tags = " ".join(f"[{tag}]" for tag in clue["tags"])
            output.append(f"{name} {tags}")
            output.append(f"  {clue['description']}")
            output.append(f"  Elements: {len(clue['elements'])} available, {len(clue['spent_elements'])} spent")
            
        self.caller.msg("\n".join(output))
    
    def view_clue(self):
        """View a clue's details"""
        clue_name = self.args.strip()
        
        if not self.caller.db.clues or clue_name not in self.caller.db.clues:
            self.caller.msg(f"No clue named '{clue_name}' found")
            return
            
        clue = self.caller.db.clues[clue_name]
        
        output = [
            f"Clue: {clue_name}",
            f"Description: {clue['description']}",
            f"Tags: {', '.join(clue['tags']) if clue['tags'] else 'None'}"
        ]
        
        if clue["elements"]:
            output.append("\nAvailable Elements:")
            for i, element in enumerate(clue["elements"], 1):
                output.append(f"{i}. {element}")
                
        if clue["spent_elements"]:
            output.append("\nSpent Elements:")
            for i, element in enumerate(clue["spent_elements"], 1):
                output.append(f"{i}. {element}")
                
        self.caller.msg("\n".join(output))
    
    def spend_element(self):
        """Spend a clue element"""
        try:
            clue_name, element_num = self.args.split()
            element_num = int(element_num)
        except ValueError:
            self.caller.msg("Usage: +investigation/spend <clue> <element_number>")
            return
            
        if not self.caller.db.clues or clue_name not in self.caller.db.clues:
            self.caller.msg(f"No clue named '{clue_name}' found")
            return
            
        clue = self.caller.db.clues[clue_name]
        
        if not 1 <= element_num <= len(clue["elements"]):
            self.caller.msg(f"Invalid element number. Choose 1-{len(clue['elements'])}")
            return
            
        # Move element from available to spent
        element = clue["elements"].pop(element_num - 1)
        clue["spent_elements"].append(element)
        
        self.caller.msg(f"Spent element from {clue_name}: {element}")
    
    def uncover_truth(self):
        """Attempt to uncover truth by combining clues"""
        clue_names = self.args.split()
        
        if len(clue_names) < 2:
            self.caller.msg("Usage: +investigation/truth <clue1> <clue2> [clue3...]")
            return
            
        # Check if all clues exist
        if not self.caller.db.clues:
            self.caller.msg("You have no clues")
            return
            
        for name in clue_names:
            if name not in self.caller.db.clues:
                self.caller.msg(f"No clue named '{name}' found")
                return
                
        # Check if clues have required elements
        for name in clue_names:
            clue = self.caller.db.clues[name]
            if not clue["elements"]:
                self.caller.msg(f"Clue '{name}' has no available elements")
                return
                
        # Calculate dice pool
        # Base pool is intelligence + investigation
        intelligence = self.caller.db.attributes["mental"]["intelligence"]
        investigation = self.caller.db.skills["mental"].get("investigation", 0)
        dice_pool = intelligence + investigation
        
        # Add bonus for number of clues
        dice_pool += len(clue_names)
        
        # Make the roll
        self.caller.msg(f"Attempting to uncover truth with {len(clue_names)} clues")
        self.caller.msg(f"Dice pool: {dice_pool}")
        
        # Use the existing roll command
        self.caller.execute_cmd(f"+roll {dice_pool}")
    
    # Mystery System Methods
    def list_mysteries(self):
        """List active mysteries the character can participate in."""
        mysteries = MysteryManager.get_active_mysteries()
        
        if not mysteries:
            self.caller.msg("No active mysteries are available.")
            return
        
        # Filter mysteries this character can access
        accessible_mysteries = []
        for mystery in mysteries:
            # Check template restrictions
            if mystery.db.allowed_templates:
                char_template = getattr(self.caller.db, 'template', None)
                if char_template not in mystery.db.allowed_templates:
                    continue
            
            # Check character restrictions
            if mystery.db.allowed_characters and self.caller.id not in mystery.db.allowed_characters:
                continue
                
            accessible_mysteries.append(mystery)
        
        if not accessible_mysteries:
            self.caller.msg("No mysteries are available for your character.")
            return
        
        table = evtable.EvTable(
            "|cID|n", "|cTitle|n", "|cCategory|n", "|cDifficulty|n", "|cYour Progress|n",
            border="table", align="l"
        )
        
        for mystery in accessible_mysteries:
            discovered_clues = mystery.get_discovered_clues(self.caller)
            total_clues = len(mystery.db.clues)
            progress = f"{len(discovered_clues)}/{total_clues}"
            
            table.add_row(
                mystery.id,
                mystery.db.title[:25],
                mystery.db.category,
                f"{mystery.db.difficulty}/5",
                progress
            )
        
        self.caller.msg(f"|cActive Mysteries:|n\n{table}")
    
    def view_mystery(self):
        """View details of a specific mystery and the character's progress."""
        if not self.args:
            self.caller.msg("Usage: +investigation/mystery <mystery_id>")
            return
        
        try:
            mystery_id = int(self.args.strip())
        except ValueError:
            self.caller.msg("Mystery ID must be a number.")
            return
        
        from evennia.utils import search
        mystery = search.search_object(f"#{mystery_id}")
        if not mystery:
            self.caller.msg(f"Mystery {mystery_id} not found.")
            return
        
        mystery = mystery[0]
        
        # Check if character can access this mystery
        can_access, reason = mystery.can_discover_clue(self.caller, list(mystery.db.clues.keys())[0] if mystery.db.clues else "dummy")
        if not can_access and "Template not allowed" in reason:
            self.caller.msg("You cannot access this mystery.")
            return
        
        discovered_clues = mystery.get_discovered_clues(self.caller)
        available_clues = mystery.get_available_clues(self.caller)
        
        output = [
            f"|c=== {mystery.db.title} ===|n",
            f"|yDescription:|n {mystery.db.description}",
            f"|yCategory:|n {mystery.db.category}",
            f"|yDifficulty:|n {mystery.db.difficulty}/5",
            f"|yYour Progress:|n {len(discovered_clues)}/{len(mystery.db.clues)} clues discovered",
            ""
        ]
        
        if discovered_clues:
            output.append("|yDiscovered Clues:|n")
            for clue_id in discovered_clues:
                clue = mystery.db.clues.get(clue_id, {})
                output.append(f"  |w{clue.get('name', 'Unknown')}|n - {clue.get('description', '')[:50]}...")
            output.append("")
        
        if available_clues:
            output.append(f"|yAvailable to Discover:|n {len(available_clues)} clue(s)")
            output.append("|yHint:|n Try using +investigation/investigate, /examine, or /search to find clues.")
        else:
            if len(discovered_clues) < len(mystery.db.clues):
                output.append("|yNext Steps:|n You may need to discover more clues before new ones become available.")
        
        self.caller.msg("\n".join(output))
    
    def investigate(self):
        """General investigation attempt in current location."""
        target = self.args.strip() if self.args else "area"
        
        if not self.caller.location:
            self.caller.msg("You need to be somewhere to investigate.")
            return
        
        # Get mysteries that have clues available in this location
        mysteries = MysteryManager.get_active_mysteries()
        location_clues = []
        
        for mystery in mysteries:
            available_clues = mystery.get_available_clues(self.caller)
            for clue_id in available_clues:
                clue = mystery.db.clues[clue_id]
                # Check if clue has location hints for current area
                location_hints = clue.get('location_hints', [])
                if not location_hints or self.caller.location.key in location_hints:
                    location_clues.append((mystery, clue_id, clue))
        
        if not location_clues:
            self.caller.msg("Your investigation of the area reveals nothing of interest.")
            return
        
        # Make an investigation roll
        intelligence = self.caller.db.attributes["mental"]["intelligence"]
        investigation_skill = self.caller.db.skills["mental"].get("investigation", 0)
        dice_pool = intelligence + investigation_skill
        
        self.caller.msg(f"|yYou begin investigating {target}...|n")
        self.caller.msg(f"Rolling Intelligence + Investigation: {dice_pool} dice")
        
        # Simulate a roll (you'd integrate with your actual dice system)
        successes = sum(1 for _ in range(dice_pool) if random.randint(1, 10) >= 8)
        
        if successes == 0:
            self.caller.msg("|rYour investigation reveals nothing useful.|n")
            return
        elif successes >= 3:
            # Exceptional success - might discover multiple clues or get bonus info
            self.caller.msg(f"|gExceptional Success! ({successes} successes)|n")
            clues_to_discover = min(2, len(location_clues))
        else:
            # Regular success
            self.caller.msg(f"|gSuccess! ({successes} successes)|n")
            clues_to_discover = 1
        
        # Discover clue(s)
        discovered = []
        for i in range(min(clues_to_discover, len(location_clues))):
            mystery, clue_id, clue = location_clues[i]
            success, msg = mystery.discover_clue(self.caller, clue_id, "investigation")
            if success:
                discovered.append(clue['name'])
        
        if discovered:
            self.caller.msg(f"|yYour investigation uncovered:|n {', '.join(discovered)}")
        else:
            self.caller.msg("Despite your efforts, you don't find anything new.")
    
    def share_clue(self):
        """Share a clue with another character."""
        if "=" not in self.args:
            self.caller.msg("Usage: +investigation/share <character> = <clue_name>")
            return
        
        char_name, clue_name = [x.strip() for x in self.args.split("=", 1)]
        
        target = self.caller.search(char_name)
        if not target:
            return
        target = target[0]
        
        # Check if caller has this clue
        personal_clues = self.caller.db.clues or {}
        if clue_name in personal_clues:
            # Share personal clue
            if not target.db.clues:
                target.db.clues = {}
            
            shared_clue = personal_clues[clue_name].copy()
            shared_clue['tags'] = shared_clue.get('tags', [])
            if 'shared' not in shared_clue['tags']:
                shared_clue['tags'].append('shared')
            
            target.db.clues[f"shared_{clue_name}"] = shared_clue
            
            self.caller.msg(f"|gYou shared the clue '{clue_name}' with {target.name}.|n")
            target.msg(f"|y{self.caller.name} shared a clue with you: {clue_name}|n")
            target.msg(f"|yDescription:|n {shared_clue['description']}")
        else:
            # Check mystery clues
            mystery_clues = getattr(self.caller.db, 'mystery_clues', {})
            found_clue = None
            
            for mystery_id, clue_ids in mystery_clues.items():
                from evennia.utils import search
                mystery = search.search_object(f"#{mystery_id}")
                if mystery:
                    mystery = mystery[0]
                    for clue_id in clue_ids:
                        clue = mystery.db.clues.get(clue_id, {})
                        if clue.get('name', '').lower() == clue_name.lower():
                            found_clue = (mystery, clue_id, clue)
                            break
                if found_clue:
                    break
            
            if found_clue:
                mystery, clue_id, clue = found_clue
                # Grant the clue to the target character
                success, msg = mystery.discover_clue(target, clue_id, "shared")
                if success:
                    self.caller.msg(f"|gYou shared the mystery clue '{clue['name']}' with {target.name}.|n")
                    target.msg(f"|y{self.caller.name} shared a mystery clue with you:|n {msg}")
                else:
                    self.caller.msg(f"|rCouldn't share clue:|n {msg}")
            else:
                self.caller.msg(f"You don't have a clue named '{clue_name}'.")
    
    def collaborate(self):
        """Start a collaboration with another investigator."""
        if not self.args:
            self.caller.msg("Usage: +investigation/collaborate <character>")
            return
        
        target = self.caller.search(self.args.strip())
        if not target:
            return
        target = target[0]
        
        if target == self.caller:
            self.caller.msg("You can't collaborate with yourself.")
            return
        
        # Initialize collaboration tracking
        if not hasattr(self.caller.db, 'collaborations'):
            self.caller.db.collaborations = []
        if not hasattr(target.db, 'collaborations'):
            target.db.collaborations = []
        
        collab_id = f"{self.caller.id}_{target.id}"
        
        if target.id not in self.caller.db.collaborations:
            self.caller.db.collaborations.append(target.id)
            target.db.collaborations.append(self.caller.id)
            
            self.caller.msg(f"|gYou begin collaborating with {target.name} on investigations.|n")
            target.msg(f"|y{self.caller.name} wants to collaborate with you on investigations.|n")
            target.msg(f"|yYou can now share clues more easily and get bonuses when investigating together.|n")
        else:
            self.caller.msg(f"You're already collaborating with {target.name}.")
    
    def show_progress(self):
        """Show investigation progress across all mysteries."""
        mystery_clues = getattr(self.caller.db, 'mystery_clues', {})
        
        if not mystery_clues:
            self.caller.msg("You haven't discovered any mystery clues yet.")
            return
        
        output = ["|cYour Investigation Progress:|n"]
        
        for mystery_id, clue_ids in mystery_clues.items():
            from evennia.utils import search
            mystery = search.search_object(f"#{mystery_id}")
            if mystery:
                mystery = mystery[0]
                total_clues = len(mystery.db.clues)
                discovered_count = len(clue_ids)
                percentage = int((discovered_count / total_clues) * 100) if total_clues > 0 else 0
                
                output.append(f"|w{mystery.db.title}|n")
                output.append(f"  Progress: {discovered_count}/{total_clues} clues ({percentage}%)")
                output.append(f"  Category: {mystery.db.category}")
                output.append("")
        
        self.caller.msg("\n".join(output))
    
    def examine_for_clues(self):
        """Examine an object for clues."""
        if not self.args:
            self.caller.msg("Usage: +investigation/examine <object>")
            return
        
        target = self.caller.search(self.args.strip())
        if not target:
            return
        target = target[0]
        
        # Check if this is a clue object
        from typeclasses.mysteries import ClueObject
        if isinstance(target, ClueObject):
            # Let the clue object handle the examination
            target.at_examine(self.caller)
        else:
            # Regular examination with investigation bonus
            self.caller.msg(f"|yYou carefully examine {target.name} for clues...|n")
            
            # Check if any mysteries have clues related to this object
            mysteries = MysteryManager.get_active_mysteries()
            found_clue = False
            
            for mystery in mysteries:
                available_clues = mystery.get_available_clues(self.caller)
                for clue_id in available_clues:
                    clue = mystery.db.clues[clue_id]
                    # Check if this object is mentioned in clue hints
                    skill_hints = clue.get('skill_hints', [])
                    if 'examination' in skill_hints or target.key.lower() in clue.get('description', '').lower():
                        # Attempt discovery
                        success, msg = mystery.discover_clue(self.caller, clue_id, "examination")
                        if success:
                            self.caller.msg(f"|gYour careful examination reveals something:|n {msg}")
                            found_clue = True
                            break
                if found_clue:
                    break
            
            if not found_clue:
                self.caller.msg(f"Your examination of {target.name} reveals nothing unusual.")
    
    def search_for_clues(self):
        """Search an area for hidden clues."""
        area = self.args.strip() if self.args else "here"
        
        if not self.caller.location:
            self.caller.msg("You need to be somewhere to search.")
            return
        
        self.caller.msg(f"|yYou begin searching {area} for hidden clues...|n")
        
        # This would be similar to investigate but with different skill emphasis
        # Could use Wits + Investigation or Dexterity + Larceny for hidden things
        wits = self.caller.db.attributes["mental"]["wits"]
        investigation = self.caller.db.skills["mental"].get("investigation", 0)
        dice_pool = wits + investigation
        
        self.caller.msg(f"Rolling Wits + Investigation: {dice_pool} dice")
        
        # Simulate roll
        successes = sum(1 for _ in range(dice_pool) if random.randint(1, 10) >= 8)
        
        if successes >= 2:
            # Search might find different types of clues than general investigation
            self.investigate()  # Reuse investigation logic for now
        else:
            self.caller.msg("|rYour search reveals nothing hidden.|n")
    
    def interview(self):
        """Interview a character for information."""
        if not self.args:
            self.caller.msg("Usage: +investigation/interview <character>")
            return
        
        target = self.caller.search(self.args.strip())
        if not target:
            return
        target = target[0]
        
        if target == self.caller:
            self.caller.msg("You can't interview yourself.")
            return
        
        # Check if target is an NPC with mystery information
        npc_clues = getattr(target.db, 'npc_clues', {})
        
        if npc_clues:
            self.caller.msg(f"|yYou begin interviewing {target.name}...|n")
            
            # Social roll - Manipulation + Persuasion or similar
            manipulation = self.caller.db.attributes["social"]["manipulation"]
            persuasion = self.caller.db.skills["social"].get("persuasion", 0)
            dice_pool = manipulation + persuasion
            
            self.caller.msg(f"Rolling Manipulation + Persuasion: {dice_pool} dice")
            
            successes = sum(1 for _ in range(dice_pool) if random.randint(1, 10) >= 8)
            
            if successes >= 2:
                # Success - might reveal clues
                available_clues = [clue_id for clue_id, requirements in npc_clues.items() 
                                 if requirements.get('social_success', 0) <= successes]
                
                if available_clues:
                    clue_id = available_clues[0]  # Give first available clue
                    mystery_id = npc_clues[clue_id].get('mystery_id')
                    
                    if mystery_id:
                        from evennia.utils import search
                        mystery = search.search_object(f"#{mystery_id}")
                        if mystery:
                            mystery = mystery[0]
                            success, msg = mystery.discover_clue(self.caller, clue_id, "interview")
                            if success:
                                self.caller.msg(f"|g{target.name} reveals something interesting:|n {msg}")
                                target.msg(f"|yYou shared information with {self.caller.name}.|n")
                            else:
                                self.caller.msg(f"{target.name} doesn't seem to know anything useful.")
                        else:
                            self.caller.msg(f"{target.name} doesn't seem to know anything useful.")
                    else:
                        self.caller.msg(f"{target.name} doesn't seem to know anything useful.")
                else:
                    self.caller.msg(f"{target.name} doesn't have any new information to share.")
            else:
                self.caller.msg(f"|r{target.name} doesn't seem willing to share information with you.|n")
        else:
            # Regular PC - could initiate social RP
            self.caller.msg(f"|yYou approach {target.name} for an interview.|n")
            target.msg(f"|y{self.caller.name} wants to interview you about ongoing investigations.|n")
    
    def research(self):
        """Research a topic for clues."""
        if not self.args:
            self.caller.msg("Usage: +investigation/research <topic>")
            return
        
        topic = self.args.strip()
        
        # Check if character is in a location with research capabilities
        location = self.caller.location
        can_research = False
        
        if location:
            # Check for library, computer, or other research tools
            research_tags = getattr(location.db, 'tags', [])
            if 'library' in research_tags or 'computer' in research_tags or 'research' in research_tags:
                can_research = True
        
        if not can_research:
            self.caller.msg("You need to be in a library, have access to a computer, or be in another location with research capabilities.")
            return
        
        self.caller.msg(f"|yYou begin researching '{topic}'...|n")
        
        # Research roll - Intelligence + Academics or Investigation
        intelligence = self.caller.db.attributes["mental"]["intelligence"]
        academics = self.caller.db.skills["mental"].get("academics", 0)
        dice_pool = intelligence + academics
        
        self.caller.msg(f"Rolling Intelligence + Academics: {dice_pool} dice")
        
        successes = sum(1 for _ in range(dice_pool) if random.randint(1, 10) >= 8)
        
        if successes >= 2:
            # Research might reveal background clues or context
            mysteries = MysteryManager.get_active_mysteries()
            
            for mystery in mysteries:
                available_clues = mystery.get_available_clues(self.caller)
                for clue_id in available_clues:
                    clue = mystery.db.clues[clue_id]
                    # Check if research topic matches clue keywords
                    if topic.lower() in clue.get('description', '').lower() or topic.lower() in clue.get('name', '').lower():
                        success, msg = mystery.discover_clue(self.caller, clue_id, "research")
                        if success:
                            self.caller.msg(f"|gYour research on '{topic}' uncovers:|n {msg}")
                            return
            
            self.caller.msg(f"|yYour research on '{topic}' provides some general background but no specific clues.|n")
        else:
            self.caller.msg(f"|rYour research on '{topic}' doesn't turn up anything useful.|n")