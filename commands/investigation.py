import re
import random
from evennia.commands.default.muxcommand import MuxCommand
from evennia.utils import create, evtable
from evennia.utils.ansi import ANSIString
from world.experience import ExperienceHandler
from typeclasses.mysteries import MysteryManager

class CmdInvestigation(MuxCommand):
    """
    Investigation commands for the Mystery System.
    
    Mystery Discovery:
        +investigation/mysteries - List active mysteries you can participate in
        +investigation/mystery <mystery_id> - View mystery details and your progress
        +investigation/progress [mystery_id] - Show your investigation progress
        
    Discovery Methods:
        +investigation/examine <object> - Carefully examine an object for clues
        +investigation/search [area] - Search an area for hidden clues
        +investigation/interview <character> - Interview someone for information
        +investigation/research <topic> - Research a topic (requires library/resources)
        
    Collaboration:
        +investigation/share <character> = <clue_name> - Share a mystery clue with another character
        +investigation/collaborate <character> - Begin collaborating on investigations
        
    All commands work within the context of active mysteries managed by staff.
    Use +investigation/mysteries to see what investigations are available to you.
    """
    key = "+investigation"
    aliases = ["+inv"]
    help_category = "Roleplaying Tools"
    def parse(self):
        """Parse the command arguments."""
        super().parse()  # Initialize switches and other MuxCommand attributes
        
        args = self.args.strip()
        self.switches = []
    
    def flexible_search(self, search_term):
        """
        Search for an object, trying both spaces and underscores.
        
        Args:
            search_term (str): The term to search for
            
        Returns:
            Object or None: The found object, or None if not found
        """
        # Try the original search term first
        target = self.caller.search(search_term)
        
        # If not found and search term contains spaces, try with underscores
        if not target and ' ' in search_term:
            underscore_term = search_term.replace(' ', '_')
            target = self.caller.search(underscore_term)
            if target:
                # For debugging, inform user about the substitution
                # self.caller.msg(f"|y(Found '{underscore_term}' instead of '{search_term}')|n")
                pass
        
        # If still not found and search term contains underscores, try with spaces
        if not target and '_' in search_term:
            space_term = search_term.replace('_', ' ')
            target = self.caller.search(space_term)
            if target:
                # For debugging, inform user about the substitution
                # self.caller.msg(f"|y(Found '{space_term}' instead of '{search_term}')|n")
                pass
        
        return target[0] if target else None
    
    def func(self):
        """Execute the command"""
        if not self.switches:
            self.caller.msg("Use +investigation with a switch. See 'help +investigation' for all options.")
            return
            
        switch = self.switches[0].lower()
        
        # Mystery system functionality
        if switch == "mysteries":
            self.list_mysteries()
        elif switch == "mystery":
            self.view_mystery()
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
        elif switch == "share":
            self.share_clue()
        elif switch == "collaborate":
            self.collaborate()
        else:
            self.caller.msg("Invalid switch. See 'help +investigation' for usage.")
    
    # Mystery System Methods
    def _attempt_mystery_discovery(self, method_type, target_object=None, research_topic=None):
        """
        Attempt to discover mystery clues using specified method.
        
        Args:
            method_type (str): Type of discovery method ('search', 'examine', 'interview', 'research')
            target_object (Object, optional): Specific object being examined/interviewed
            research_topic (str, optional): Topic being researched
            
        Returns:
            list: Names of discovered clues
        """
        # Get mysteries that have clues available
        mysteries = MysteryManager.get_active_mysteries()
        available_clues = []
        
        for mystery in mysteries:
            mystery_available = mystery.get_available_clues(self.caller)
            for clue_id in mystery_available:
                clue = mystery.db.clues[clue_id]
                
                # Check if clue can be discovered by this method
                skill_hints = clue.get('skill_hints', [])
                location_hints = clue.get('location_hints', [])
                
                # Location filtering (not applicable for research)
                if method_type != 'research' and location_hints and self.caller.location.key not in location_hints:
                    continue
                
                # Method filtering
                if skill_hints and method_type not in skill_hints:
                    continue
                    
                # Object-specific filtering for examine/interview
                if target_object and method_type in ['examine', 'interview']:
                    if target_object.key.lower() not in clue.get('description', '').lower():
                        continue
                
                # Topic-specific filtering for research
                if research_topic and method_type == 'research':
                    clue_desc = clue.get('description', '').lower()
                    clue_name = clue.get('name', '').lower()
                    if research_topic.lower() not in clue_desc and research_topic.lower() not in clue_name:
                        continue
                
                available_clues.append((mystery, clue_id, clue))
        
        if not available_clues:
            return []
        
        # Determine skill/attribute to use
        attribute, skill, skill_category = self._get_skill_for_clues(available_clues)
        
        # Get attribute and skill values
        attr_value = self._get_attribute_value(attribute)
        skill_value = self.caller.db.skills[skill_category].get(skill, 0)
        dice_pool = attr_value + skill_value
        
        self.caller.msg(f"Rolling {attribute.title()} + {skill.title()}: {dice_pool} dice")
        
        # Make the roll
        successes = sum(1 for _ in range(dice_pool) if random.randint(1, 10) >= 8)
        
        if successes == 0:
            return []
        
        # Determine how many clues to discover
        if successes >= 3:
            self.caller.msg(f"|gExceptional Success! ({successes} successes)|n")
            clues_to_discover = min(2, len(available_clues))
        else:
            self.caller.msg(f"|gSuccess! ({successes} successes)|n")
            clues_to_discover = 1
        
        # Attempt to discover clues
        discovered = []
        for i in range(min(clues_to_discover, len(available_clues))):
            mystery, clue_id, clue = available_clues[i]
            
            # Check if specific clue's difficulty requirements are met
            discovery_conditions = clue.get('discovery_conditions', {})
            if 'skill_roll' in discovery_conditions:
                required_difficulty = discovery_conditions['skill_roll'].get('difficulty', 2)
                if successes < required_difficulty:
                    continue
            
            success, msg = mystery.discover_clue(self.caller, clue_id, method_type)
            if success:
                discovered.append(clue['name'])
        
        return discovered
    
    def _get_skill_for_clues(self, available_clues):
        """Determine the best skill/attribute combination for available clues."""
        # Default to wits + investigation
        attribute = "wits"
        skill = "investigation"
        skill_category = "mental"
        
        # Check if any clues have specific skill requirements
        for mystery, clue_id, clue in available_clues:
            discovery_conditions = clue.get('discovery_conditions', {})
            if 'skill_roll' in discovery_conditions:
                skill_req = discovery_conditions['skill_roll']
                skill = skill_req.get('skill', 'investigation')
                attribute = skill_req.get('attribute', 'wits')
                
                # Determine skill category
                if skill in ['investigation', 'academics', 'computer', 'crafts', 'medicine', 'occult', 'science']:
                    skill_category = "mental"
                elif skill in ['athletics', 'brawl', 'drive', 'firearms', 'larceny', 'stealth', 'survival', 'weaponry']:
                    skill_category = "physical"
                elif skill in ['animal_ken', 'empathy', 'expression', 'intimidation', 'persuasion', 'socialize', 'streetwise', 'subterfuge']:
                    skill_category = "social"
                break
        
        return attribute, skill, skill_category
    
    def _get_attribute_value(self, attribute):
        """Get the value of an attribute from the character."""
        if attribute in self.caller.db.attributes["mental"]:
            return self.caller.db.attributes["mental"][attribute]
        elif attribute in self.caller.db.attributes["physical"]:
            return self.caller.db.attributes["physical"][attribute]
        elif attribute in self.caller.db.attributes["social"]:
            return self.caller.db.attributes["social"][attribute]
        else:
            # Default to wits if attribute not found
            return self.caller.db.attributes["mental"]["wits"]
    
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
            output.append("|yHint:|n Try using +investigation/search, /examine, or /search to find clues.")
        else:
            if len(discovered_clues) < len(mystery.db.clues):
                output.append("|yNext Steps:|n You may need to discover more clues before new ones become available.")
        
        self.caller.msg("\n".join(output))
    
    
    def share_clue(self):
        """Share a mystery clue with another character."""
        if "=" not in self.args:
            self.caller.msg("Usage: +investigation/share <character> = <clue_name>")
            return
        
        char_name, clue_name = [x.strip() for x in self.args.split("=", 1)]
        
        target = self.flexible_search(char_name)
        
        if not target:
            return
        
        # Check mystery clues that this character has discovered
        mystery_clues = getattr(self.caller.db, 'mystery_clues', {})
        found_clue = None
        
        if not mystery_clues:
            self.caller.msg("You haven't discovered any mystery clues to share.")
            return
        
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
            self.caller.msg(f"You don't have a mystery clue named '{clue_name}'. Use +investigation/progress to see your discovered clues.")
    
    def collaborate(self):
        """Start a collaboration with another investigator."""
        if not self.args:
            self.caller.msg("Usage: +investigation/collaborate <character>")
            return
        
        search_term = self.args.strip()
        target = self.flexible_search(search_term)
        
        if not target:
            return
        
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
        
        search_term = self.args.strip()
        target = self.flexible_search(search_term)
        
        if not target:
            return
        
        # Check if this is a clue object
        from typeclasses.mysteries import ClueObject
        if isinstance(target, ClueObject):
            # Let the clue object handle the examination
            target.at_examine(self.caller)
        else:
            self.caller.msg(f"|yYou carefully examine {target.name} for clues...|n")
            
            # Use the general mystery discovery logic
            discovered_clues = self._attempt_mystery_discovery("examine", target)
            
            if discovered_clues:
                self.caller.msg(f"|gYour careful examination reveals:|n {', '.join(discovered_clues)}")
            else:
                self.caller.msg(f"Your examination of {target.name} reveals nothing unusual.")
    
    def search_for_clues(self):
        """Search an area for hidden clues."""
        area = self.args.strip() if self.args else "here"
        
        if not self.caller.location:
            self.caller.msg("You need to be somewhere to search.")
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
                    # Check if this clue has search-specific discovery conditions
                    discovery_conditions = clue.get('discovery_conditions', {})
                    skill_hints = clue.get('skill_hints', [])
                    if 'search' in skill_hints or not skill_hints:  # Include clues without specific skill hints
                        location_clues.append((mystery, clue_id, clue))
        
        if not location_clues:
            self.caller.msg(f"|yYou search {area} thoroughly but find nothing of interest.|n")
            return
        
        self.caller.msg(f"|yYou begin searching {area} for hidden clues...|n")
        
        # Determine what skill/attribute to use based on available clues
        # Default to wits + investigation, but use clue-specific requirements if available
        attribute = "wits"
        skill = "investigation"
        skill_category = "mental"
        
        # Check if any clues have specific skill requirements
        for mystery, clue_id, clue in location_clues:
            discovery_conditions = clue.get('discovery_conditions', {})
            if 'skill_roll' in discovery_conditions:
                skill_req = discovery_conditions['skill_roll']
                required_skill = skill_req.get('skill', 'investigation')
                required_attribute = skill_req.get('attribute', 'wits')
                
                # Use the first skill-specific requirement we find
                skill = required_skill
                attribute = required_attribute
                
                # Determine skill category based on common skills
                if skill in ['investigation', 'academics', 'computer', 'crafts', 'medicine', 'occult', 'science']:
                    skill_category = "mental"
                elif skill in ['athletics', 'brawl', 'drive', 'firearms', 'larceny', 'stealth', 'survival', 'weaponry']:
                    skill_category = "physical"
                elif skill in ['animal_ken', 'empathy', 'expression', 'intimidation', 'persuasion', 'socialize', 'streetwise', 'subterfuge']:
                    skill_category = "social"
                break
        
        # Get the actual attribute and skill values
        if attribute in self.caller.db.attributes["mental"]:
            attr_value = self.caller.db.attributes["mental"][attribute]
        elif attribute in self.caller.db.attributes["physical"]:
            attr_value = self.caller.db.attributes["physical"][attribute]
        elif attribute in self.caller.db.attributes["social"]:
            attr_value = self.caller.db.attributes["social"][attribute]
        else:
            # Default to wits if attribute not found
            attr_value = self.caller.db.attributes["mental"]["wits"]
            attribute = "wits"
        
        skill_value = self.caller.db.skills[skill_category].get(skill, 0)
        dice_pool = attr_value + skill_value
        
        self.caller.msg(f"Rolling {attribute.title()} + {skill.title()}: {dice_pool} dice")
        
        # Simulate roll
        successes = sum(1 for _ in range(dice_pool) if random.randint(1, 10) >= 8)
        
        if successes == 0:
            self.caller.msg("|rYour search reveals nothing hidden.|n")
            return
        elif successes >= 3:
            # Exceptional success - might discover multiple clues
            self.caller.msg(f"|gExceptional Success! ({successes} successes)|n")
            clues_to_discover = min(2, len(location_clues))
        else:
            # Regular success
            self.caller.msg(f"|gSuccess! ({successes} successes)|n")
            clues_to_discover = 1
        
        # Discover clue(s) based on success level and skill requirements
        discovered = []
        for i in range(min(clues_to_discover, len(location_clues))):
            mystery, clue_id, clue = location_clues[i]
            
            # Check if this specific clue's conditions are met
            discovery_conditions = clue.get('discovery_conditions', {})
            can_discover = True
            
            if 'skill_roll' in discovery_conditions:
                skill_req = discovery_conditions['skill_roll']
                required_difficulty = skill_req.get('difficulty', 2)
                if successes < required_difficulty:
                    can_discover = False
            
            if can_discover:
                success, msg = mystery.discover_clue(self.caller, clue_id, "search")
                if success:
                    discovered.append(clue['name'])
        
        if discovered:
            self.caller.msg(f"|yYour search uncovered:|n {', '.join(discovered)}")
        else:
            self.caller.msg("Despite your efforts, you don't find anything new.")
    
    def interview(self):
        """Interview a character for information using the mystery system."""
        if not self.args:
            self.caller.msg("Usage: +investigation/interview <character>")
            return
        
        search_term = self.args.strip()
        target = self.flexible_search(search_term)
        
        if not target:
            return
        
        if target == self.caller:
            self.caller.msg("You can't interview yourself.")
            return
        
        self.caller.msg(f"|yYou begin interviewing {target.name}...|n")
        
        # Use the general mystery discovery logic
        discovered_clues = self._attempt_mystery_discovery("interview", target)
        
        if discovered_clues:
            self.caller.msg(f"|g{target.name} reveals something interesting:|n {', '.join(discovered_clues)}")
            target.msg(f"|yYou shared information with {self.caller.name}.|n")
        else:
            # Check if this is a PC vs NPC
            if target.has_account:
                # Regular PC - initiate social RP
                self.caller.msg(f"|y{target.name} doesn't seem to know anything about your current investigations.|n")
                target.msg(f"|y{self.caller.name} wants to interview you about ongoing investigations.|n")
            else:
                # NPC with no relevant information
                self.caller.msg(f"|r{target.name} doesn't seem willing to share information with you.|n")
    
    def research(self):
        """Research a topic for clues using the mystery system."""
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
        
        # Use the general mystery discovery logic
        discovered_clues = self._attempt_mystery_discovery("research", research_topic=topic)
        
        if discovered_clues:
            self.caller.msg(f"|gYour research on '{topic}' uncovers:|n {', '.join(discovered_clues)}")
        else:
            self.caller.msg(f"|yYour research on '{topic}' provides some general background but no specific clues.|n")