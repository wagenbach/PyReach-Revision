from evennia.commands.default.muxcommand import MuxCommand
from evennia.utils import evtable
from world.utils.health_utils import get_health_track, set_health_track, compact_track

class CmdSheet(MuxCommand):
    """
    Display your character sheet.
    
    Usage:
        +sheet [character] - Display character sheet
        +sheet/ascii [character] - Force ASCII display (no Unicode dots)
        
    Shows all character statistics in an organized format.
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
        """Get valid bio fields for a specific template"""
        template = template.lower() if template else "mortal"
        
        template_fields = {
            "mortal": ["virtue", "vice"],
            "mage": ["virtue", "vice", "path", "order"],
            "vampire": ["mask", "dirge", "clan", "covenant"],
            "werewolf": ["bone", "blood", "auspice", "tribe"],
            "changeling": ["needle", "thread", "seeming", "court", "kith"],
            "geist": ["virtue", "vice", "burden", "archetype", "krewe"],
            "promethean": ["virtue", "vice", "lineage", "refinement"],
            "hunter": ["virtue", "vice", "profession", "organization", "creed"],
            "demon": ["vice", "incarnation", "agenda", "agency"],
            "beast": ["legend", "life", "hunger", "family", "inheritance"],
            "deviant": ["virtue", "vice", "origin", "clade", "divergence"],
            "mortal+": ["virtue", "vice"],
            "mortal plus": ["virtue", "vice"]
        }
        
        return template_fields.get(template, ["virtue", "vice"])

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

    def func(self):
        """Display the character sheet"""
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
            if field in bio and field not in ["virtue", "vice"]:  # virtue/vice already added above if valid
                bio_items.append((field.title(), bio[field]))
        
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
            
            # Display in columns
            for i in range(3):
                output.append(f"{mental[i]}  {physical[i]}  {social[i]}")
        
        # Skills
        skills = target.db.stats.get("skills", {})
        specialties = target.db.stats.get("specialties", {})
        if skills:
            output.append(self._format_section_header("|wSKILLS|n"))
            
            # Mental Skills
            mental_skills = ["crafts", "investigation", "medicine", "occult", "politics", "science"]
            mental_display = []
            for skill in mental_skills:
                val = skills.get(skill, 0)
                dots = self._format_dots(val, 5, force_ascii)
                skill_text = f"{skill.replace('_', ' ').title():<15} {dots}"
                
                # Add specialties if they exist
                if skill in specialties and specialties[skill]:
                    specialty_list = ", ".join(specialties[skill])
                    skill_text += f" ({specialty_list})"
                
                mental_display.append(skill_text)
            
            # Physical Skills
            physical_skills = ["athletics", "brawl", "drive", "firearms", "larceny", "stealth", "survival", "weaponry"]
            physical_display = []
            for skill in physical_skills:
                val = skills.get(skill, 0)
                dots = self._format_dots(val, 5, force_ascii)
                skill_text = f"{skill.replace('_', ' ').title():<15} {dots}"
                
                # Add specialties if they exist
                if skill in specialties and specialties[skill]:
                    specialty_list = ", ".join(specialties[skill])
                    skill_text += f" ({specialty_list})"
                
                physical_display.append(skill_text)
            
            # Social Skills
            social_skills = ["animal_ken", "empathy", "expression", "intimidation", "persuasion", "socialize", "streetwise", "subterfuge"]
            social_display = []
            for skill in social_skills:
                val = skills.get(skill, 0)
                dots = self._format_dots(val, 5, force_ascii)
                skill_text = f"{skill.replace('_', ' ').title():<15} {dots}"
                
                # Add specialties if they exist
                if skill in specialties and specialties[skill]:
                    specialty_list = ", ".join(specialties[skill])
                    skill_text += f" ({specialty_list})"
                
                social_display.append(skill_text)
            
            # Display skills in columns
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
        
        # Merits
        merits = target.db.stats.get("merits", {})
        if merits:
            output.append(self._format_section_header("|wMERITS|n"))
            
            # Create a list of all merits with their dot displays
            merit_list = []
            for merit_name, merit_data in sorted(merits.items()):
                dots = self._format_dots(merit_data.get("dots", 1), merit_data.get("max_dots", 5), force_ascii)
                merit_display = f"{merit_name.replace('_', ' ').title():<20} {dots}"
                merit_list.append(merit_display)
            
            # Display merits in 2 columns
            for i in range(0, len(merit_list), 2):
                left_merit = merit_list[i] if i < len(merit_list) else ""
                right_merit = merit_list[i + 1] if i + 1 < len(merit_list) else ""
                
                # Format with proper spacing (39 chars for left column)
                left_formatted = left_merit.ljust(39)
                output.append(f"{left_formatted} {right_merit}")

        # Derived Stats
        advantages = target.db.stats.get("advantages", {})
        other = target.db.stats.get("other", {})
        
        output.append(self._format_section_header("|wADVANTAGES|n"))
        
        # Get character template to determine what advantages to show
        template = other.get("template", "Mortal").lower()
        
        # Base advantages that all characters have
        base_advantages = [
            ("Defense", advantages.get("defense", 0)),
            ("Speed", advantages.get("speed", 0)),
            ("Initiative", advantages.get("initiative", 0)),
            ("Size", other.get("size", 5))
        ]
        
        # template-specific advantages
        template_advantages = []
        if template == "changeling":
            wyrd = advantages.get("wyrd", 0)
            if wyrd > 0:  # Only show if they have the stat
                template_advantages.append(("Wyrd", wyrd))
        elif template == "werewolf":
            primal_urge = advantages.get("primal_urge", 0)
            if primal_urge > 0:
                template_advantages.append(("Primal Urge", primal_urge))
        elif template == "vampire":
            blood_potency = advantages.get("blood_potency", 0)
            if blood_potency > 0:
                template_advantages.append(("Blood Potency", blood_potency))
        elif template == "mage":
            gnosis = advantages.get("gnosis", 0)
            if gnosis > 0:
                template_advantages.append(("Gnosis", gnosis))
        elif template == "geist":
            synergy = advantages.get("synergy", 0)
            if synergy > 0:
                template_advantages.append(("Synergy", synergy))
        elif template == "beast":
            satiety = advantages.get("satiety", 0)
            if satiety > 0:
                template_advantages.append(("Satiety", satiety))
        elif template == "deviant":
            deviation = advantages.get("deviation", 0)
            if deviation > 0:
                template_advantages.append(("Deviation", deviation))
        elif template == "demon":
            primum = advantages.get("primum", 0)
            if primum > 0:
                template_advantages.append(("Primum", primum))
        elif template == "hunter":
            # Hunters don't typically have a power stat, but might have special advantages
            pass
        elif template == "promethean":
            azoth = advantages.get("azoth", 0)
            if azoth > 0:
                template_advantages.append(("Azoth", azoth))
        elif template in ["mortal+", "mortal plus"]:
            # Mortal+ might have special advantages
            pass
        # Regular mortals get no special advantages
        
        # Combine base and template advantages
        adv_list = base_advantages + template_advantages
        
        # Pad to ensure we have multiples of 3 for clean column display
        while len(adv_list) % 3 != 0:
            adv_list.append(("", ""))
        
        # Display in rows of 3 columns
        for i in range(0, len(adv_list), 3):
            row_parts = []
            for j in range(3):
                if i + j < len(adv_list):
                    name, value = adv_list[i + j]
                    if name:  # Only display if there's a name
                        part = f"{name:<16} : {value}"
                        row_parts.append(part.ljust(26))
                    else:
                        row_parts.append(" " * 26)
                else:
                    row_parts.append(" " * 26)
            output.append("".join(row_parts))
        
        # Health, Willpower, Integrity
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
        
        # Display health, willpower, integrity
        output.append("")  # Empty line before health/willpower/integrity
        output.append(f"Health: {''.join(health_boxes)}")
        
        willpower_max = advantages.get("willpower", 3)
        willpower_current = target.db.willpower_current
        if willpower_current is None:
            willpower_current = willpower_max  # Default to full
        
        willpower_dots = self._format_dots(willpower_current, willpower_max, force_ascii)
        output.append(f"Willpower : {willpower_dots} ({willpower_current}/{willpower_max})")
        
        # Integrity with template-specific name
        integrity_name = target.get_integrity_name(template)
        output.append(f"{integrity_name}: {other.get('integrity', 7)}")

        # Experience
        output.append(self._format_section_header("|wEXPERIENCE|n"))
        output.append(f"Beats: {other.get('beats', 0)}")
        output.append(f"Experience: {other.get('experience', 0)}")
        
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