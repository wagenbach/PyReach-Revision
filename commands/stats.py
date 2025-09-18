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
        else:
            self.caller.msg("Invalid switch. See help for usage.")
    
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
                # Convert spaces to underscores in stat names
                stat = stat.strip().lower().replace(" ", "_")
                return None, stat, value.strip()
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
        
        # Check advantages
        elif stat in ["health", "willpower", "speed", "defense", "initiative"]:
            if isinstance(value, int) and value >= 0:
                target.db.stats["advantages"][stat] = value
                stat_set = True
            else:
                self.caller.msg("Advantages must be positive numbers.")
                return
        
        # Check bio fields
        elif stat in ["fullname", "full_name", "birthdate", "concept", "virtue", "vice"]:
            # Map alternate names and handle space conversions
            bio_field = stat
            if stat in ["full_name", "fullname"]:
                bio_field = "full_name"  # Store as full_name internally
            
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
                     "auspice", "tribe", "seeming", "court", "kith", "burden", "archetype", 
                     "krewe", "lineage", "refinement", "profession", "organization", "creed", 
                     "incarnation", "agenda", "agency", "hunger", "family", "inheritance", 
                     "origin", "clade", "divergence", "needle", "thread", "legend", "life"]:
            
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
        
        # Check template (staff only)
        elif stat == "template":
            if not self.caller.check_permstring("Builder"):
                self.caller.msg("Only staff can set template.")
                return
            
            # Use character's set_template method
            success, message = target.set_template(value, self.caller)
            if success:
                self.caller.msg(message)
                stat_set = True
            else:
                self.caller.msg(message)
                return
        
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
            
            # Store as integrity regardless of alias used
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
        
        # Check merits (allow setting for unapproved characters, redirect approved to XP system)
        elif stat in ["crafts", "investigation", "medicine", "occult", "politics", "science",
                     "athletics", "brawl", "drive", "firearms", "larceny", "stealth", 
                     "survival", "weaponry", "animal_ken", "empathy", "expression", 
                     "intimidation", "persuasion", "socialize", "streetwise", "subterfuge"]:
            pass  # This will be handled by the skills section above
        else:
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
        
        for category in ["attributes", "skills", "advantages", "bio", "anchors", "merits", "other"]:
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
        
        # Validate template
        valid_templates = [
            "changeling", "vampire", "werewolf", "mage", "geist", 
            "beast", "deviant", "demon", "hunter", "promethean", 
            "mortal+", "mortal plus", "mortal"
        ]
        
        if template.lower() not in valid_templates:
            self.caller.msg("Invalid template. Valid templates: Changeling, Vampire, Werewolf, Mage, Geist, Beast, Deviant, Demon, Hunter, Promethean, Mortal+, Mortal")
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