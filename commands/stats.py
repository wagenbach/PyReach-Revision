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
        +stat <stat>= - Remove a stat from yourself (if not approved)
        +stat <name>/<stat>=<value> - Set a stat on someone else (staff only)
        +stat <name>/<stat>= - Remove a stat from someone else (staff only)
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
        
        Merit Instances:
        Some merits can be taken multiple times with different specifications.
        Use colon notation to create instances:
            +stat Unseen Sense:Ghosts=2
            +stat Unseen Sense:Spirits=2
            +stat Unseen Sense:Faeries=2
        Each instance costs the full merit value. To remove an instance:
            +stat Unseen Sense:Ghosts=
        
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
        template Bio: path, order, legacy, shadow_name, cabal, mask, dirge, 
                   clan, covenant, bone, blood, auspice, tribe, lodge, pack, 
                   totem, deed_name, seeming, court, kith, burden, archetype, 
                   krewe, lineage, refinement, athanor, creator, pilgrimage, 
                   throng, profession, organization, creed, incarnation, 
                   agenda, agency, hunger, family, inheritance, origin, 
                   clade, divergence
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
        +stat legacy=Perfected Adepts (mage-specific, requires matching path or order)
        +stat lineage=Frankenstein (promethean-specific)
        +stat athanor=Basilisk (promethean-specific, requires matching lineage)
        
        Specialty Examples:
        +stat specialty/athletics=Running
        +stat specialty/investigation=Crime Scenes  
        +stat specialty/brawl=Dirty Fighting
        
        Merit Examples (during character generation):
        +stat contacts=3
        +stat fast_reflexes=2
        +stat resources=2
        +stat allies=1
        +stat unseen_sense:ghosts=2
        +stat unseen_sense:spirits=2
        
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
        Alembics (Promethean): +stat alembic=purification, +stat alembic=human_flesh
        Bestowments (Promethean): +stat bestowment=spare_parts, +stat bestowment=titans_strength

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
        
        # Import template power utilities
        from world.cofd.templates import get_template_all_powers
        
        # Get powers from template definition
        return get_template_all_powers(template)
    
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
                
                # Empty value means removal - return special marker
                if value == "":
                    # Convert spaces to underscores in stat names
                    stat = stat.replace(" ", "_")
                    return None, stat, None  # None value signals removal
                
                # Check for semantic power syntax: key=beasts, ceremony=pass_on, contract=hostile_takeover, alembic=purification, etc.
                semantic_prefixes = ["key", "ceremony", "rite", "ritual", "contract", "alembic", "bestowment"]
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
        
        if not stat:
            self.caller.msg("Usage: +stat <stat>=<value> or +stat <name>/<stat>=<value>")
            return
        
        # If value is None, this is a removal request
        if value is None:
            # Redirect to remove_stat
            self.remove_stat_direct(target_name, stat)
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
        elif stat in ["academics", "computer", "crafts", "investigation", "medicine", "occult", "politics", "science",
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
                      "azoth", "primum", "satiety", "deviation", "psyche"]:
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
                     "geist_name", "embrace_date", "legacy", "shadow_name", "cabal", "lodge",
                     "pack", "totem", "deed_name", "throng", "creator", "pilgrimage", "athanor"]:
            
            # Get character's template
            character_template = target.db.stats.get("other", {}).get("template", "Mortal")
            valid_fields = target.get_template_bio_fields(character_template)
            
            # Check if this field is valid for the character's template
            if stat not in valid_fields:
                self.caller.msg(f"{stat.title()} is not a valid field for {character_template} characters.")
                self.caller.msg(f"Valid fields for {character_template}: {', '.join(valid_fields).title()}")
                return
            
            # Custom validation for Mage Legacy field
            if stat == "legacy" and character_template.lower() == "mage":
                legacy_value = str(value).lower()
                
                # Import the legacy data from mage template
                from world.cofd.templates.mage import (
                    LEGACIES_BY_PATH, LEGACIES_BY_ORDER, UNLINKED_LEGACIES, ALL_LEGACIES
                )
                
                # First check if legacy is valid at all
                if legacy_value not in [l.lower() for l in ALL_LEGACIES]:
                    self.caller.msg(f"'{value}' is not a valid Legacy.")
                    self.caller.msg(f"|wUse +help legacy|n for a complete list of valid Legacies.")
                    return
                
                # Get character's path and order
                char_path = target.db.stats.get("bio", {}).get("path", "").lower()
                char_order = target.db.stats.get("bio", {}).get("order", "").lower()
                
                # Check if legacy is unlinked (available to everyone)
                if legacy_value in [l.lower() for l in UNLINKED_LEGACIES]:
                    # Unlinked legacies are always valid
                    pass
                else:
                    # Check if character qualifies through Path or Order
                    valid_by_path = False
                    valid_by_order = False
                    
                    # Check Path
                    if char_path and char_path in LEGACIES_BY_PATH:
                        path_legacies = [l.lower() for l in LEGACIES_BY_PATH[char_path]]
                        if legacy_value in path_legacies:
                            valid_by_path = True
                    
                    # Check Order
                    if char_order and char_order in LEGACIES_BY_ORDER:
                        order_legacies = [l.lower() for l in LEGACIES_BY_ORDER[char_order]]
                        if legacy_value in order_legacies:
                            valid_by_order = True
                    
                    # If not valid by either path or order, reject
                    if not valid_by_path and not valid_by_order:
                        error_parts = []
                        error_parts.append(f"|rYou cannot take the '{value.title()}' Legacy.|n")
                        
                        if not char_path and not char_order:
                            error_parts.append("You must set your Path and/or Order before setting a Legacy.")
                        else:
                            error_parts.append(f"Your Path ({char_path.title() if char_path else 'None'}) and Order ({char_order.title() if char_order else 'None'}) do not qualify for this Legacy.")
                            
                            # Show which paths/orders can access this legacy
                            qualifying_paths = []
                            qualifying_orders = []
                            
                            for path_name, legacies in LEGACIES_BY_PATH.items():
                                if legacy_value in [l.lower() for l in legacies]:
                                    qualifying_paths.append(path_name.title())
                            
                            for order_name, legacies in LEGACIES_BY_ORDER.items():
                                if legacy_value in [l.lower() for l in legacies]:
                                    qualifying_orders.append(order_name.title())
                            
                            if qualifying_paths:
                                error_parts.append(f"|wQualifying Paths:|n {', '.join(qualifying_paths)}")
                            if qualifying_orders:
                                error_parts.append(f"|wQualifying Orders:|n {', '.join(qualifying_orders)}")
                        
                        for part in error_parts:
                            self.caller.msg(part)
                        return
            
            # Custom validation for Promethean Athanor field
            if stat == "athanor" and character_template.lower() == "promethean":
                athanor_value = str(value).lower()
                
                # Import the athanor data from promethean template
                from world.cofd.templates.legacy_promethean import (
                    ATHANORS_BY_LINEAGE, ALL_ATHANORS
                )
                
                # First check if athanor is valid at all
                if athanor_value not in [a.lower() for a in ALL_ATHANORS]:
                    self.caller.msg(f"'{value}' is not a valid Athanor.")
                    self.caller.msg(f"|wUse +help athanor|n for a complete list of valid Athanors.")
                    return
                
                # Get character's lineage
                char_lineage = target.db.stats.get("bio", {}).get("lineage", "").lower()
                
                # Check if character has set their lineage
                if not char_lineage:
                    self.caller.msg("|rYou must set your Lineage before setting an Athanor.|n")
                    self.caller.msg("Use: |c+stat lineage=<lineage name>|n")
                    return
                
                # Check if lineage qualifies for this athanor
                if char_lineage in ATHANORS_BY_LINEAGE:
                    lineage_athanors = [a.lower() for a in ATHANORS_BY_LINEAGE[char_lineage]]
                    if athanor_value not in lineage_athanors:
                        error_parts = []
                        error_parts.append(f"|rYou cannot take the '{value.title()}' Athanor.|n")
                        error_parts.append(f"Your Lineage ({char_lineage.title()}) does not qualify for this Athanor.")
                        
                        # Show which lineages can access this athanor
                        qualifying_lineages = []
                        for lineage_name, athanors in ATHANORS_BY_LINEAGE.items():
                            if athanor_value in [a.lower() for a in athanors]:
                                qualifying_lineages.append(lineage_name.title())
                        
                        if qualifying_lineages:
                            error_parts.append(f"|wQualifying Lineages:|n {', '.join(qualifying_lineages)}")
                        
                        for part in error_parts:
                            self.caller.msg(part)
                        return
                else:
                    # Lineage not recognized or doesn't have athanors
                    self.caller.msg(f"|rYour Lineage ({char_lineage.title()}) does not have access to Athanors.|n")
                    self.caller.msg("|wValid Lineages with Athanors:|n Frankenstein, Galatea, Osiris, Tammuz, Ulgan, Unfleshed, Zeka")
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
            
            # Nuclear option: completely wipe stats but initialize with defaults
            target.db.stats = {
                "attributes": {
                    # Mental attributes
                    "intelligence": 1,
                    "wits": 1, 
                    "resolve": 1,
                    # Physical attributes
                    "strength": 1,
                    "dexterity": 1,
                    "stamina": 1,
                    # Social attributes
                    "presence": 1,
                    "manipulation": 1,
                    "composure": 1
                },
                "skills": {
                    # Mental skills
                    "academics": 0,
                    "computer": 0,
                    "crafts": 0,
                    "investigation": 0,
                    "medicine": 0,
                    "occult": 0,
                    "politics": 0,
                    "science": 0,
                    # Physical skills
                    "athletics": 0,
                    "brawl": 0,
                    "drive": 0,
                    "firearms": 0,
                    "larceny": 0,
                    "stealth": 0,
                    "survival": 0,
                    "weaponry": 0,
                    # Social skills
                    "animal_ken": 0,
                    "empathy": 0,
                    "expression": 0,
                    "intimidation": 0,
                    "persuasion": 0,
                    "socialize": 0,
                    "streetwise": 0,
                    "subterfuge": 0
                },
                "advantages": {
                    # Calculate derived stats from default attributes
                    "willpower": 2,  # resolve (1) + composure (1) = 2
                    "health": 6,     # size (5) + stamina (1) = 6
                    "speed": 7,      # strength (1) + dexterity (1) + 5 = 7
                    "defense": 1,    # min(wits, dexterity) + athletics = min(1,1) + 0 = 1
                    "initiative": 2  # dexterity (1) + composure (1) = 2
                },
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
        
        # Check merits FIRST (allow setting for unapproved characters, redirect approved to XP system)
        # Also handle instanced merits with colon syntax (e.g., unseen_sense:ghosts)
        # This must come before semantic power check since both use colons
        if not stat_set:
            try:
                from world.cofd.merits.general_merits import merits_dict
                from world.cofd.merit_utilities import (
                    parse_merit_instance, check_merit_approved_status, set_merit
                )
                
                # Parse base merit name and instance
                base_merit_name, instance_name = parse_merit_instance(stat)
                
                if base_merit_name in merits_dict:
                    merit = merits_dict[base_merit_name]
                    
                    # Check if character is approved
                    can_modify, error_msg = check_merit_approved_status(target, stat, self.caller)
                    if not can_modify:
                        self.caller.msg(error_msg)
                        return
                    
                    # For unapproved characters and NPCs, allow merit setting
                    if not isinstance(value, int):
                        try:
                            value = int(value)
                        except ValueError:
                            self.caller.msg("Merit dots must be a number.")
                            return
                    
                    # Set the merit using utility
                    success, message = set_merit(target, stat, merit, value, self.caller)
                    if not success:
                        self.caller.msg(message)
                        return
                    
                    # Merit was set successfully
                    stat_set = True
            except ImportError:
                # If merit system not available, fall through to custom stat
                pass
        
        # Check for semantic power syntax (key:beasts, ceremony:pass_on, etc.)
        # This comes after merit check since both use colons
        if not stat_set and ":" in stat:
            power_type, power_name = stat.split(":", 1)
            return self._handle_semantic_power(target, power_type, power_name, value)
        
        # Check powers (template-specific supernatural abilities)
        if not stat_set:
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
                # Check if this was a merit (display confirmation message was already sent by set_merit)
                try:
                    from world.cofd.merits.general_merits import merits_dict
                    from world.cofd.merit_utilities import parse_merit_instance
                    
                    base_merit_name, instance_name = parse_merit_instance(stat)
                    
                    # If it wasn't a merit, give generic confirmation
                    if base_merit_name not in merits_dict:
                        self.caller.msg(f"Set {target.name}'s {stat} to {value}.")
                except ImportError:
                    self.caller.msg(f"Set {target.name}'s {stat} to {value}.")
            
            # Auto-calculate derived stats if setting attributes
            if stat in ["strength", "dexterity", "stamina", "composure", "resolve", "wits", "size"]:
                target.calculate_derived_stats(self.caller)
            
            # Auto-calculate power pools if setting power stats
            if stat in ["blood_potency", "gnosis", "primal_urge", "wyrd", "synergy", 
                       "azoth", "primum", "deviation"]:
                if hasattr(target, 'calculate_power_pools'):
                    target.calculate_power_pools(self.caller)
                else:
                    # Fallback: manually calculate power pools if method doesn't exist yet
                    self._calculate_power_pools_fallback(target, stat, value)
            
            # Clean up misplaced stats
            target.cleanup_misplaced_stats(self.caller)
    
    def _calculate_power_pools_fallback(self, target, stat, value):
        """Fallback method to calculate power pools when the typeclass method isn't available"""
        advantages = target.db.stats.get("advantages", {})
        other = target.db.stats.get("other", {})
        template = other.get("template", "Mortal").lower()
        
        # Standard supernatural pool lookup table
        pool_lookup = {
            1: 10, 2: 11, 3: 12, 4: 13, 5: 15,
            6: 20, 7: 25, 8: 30, 9: 50, 10: 75
        }
        
        # Calculate the appropriate pool based on template and stat
        pool_updated = None
        
        if template == "vampire" and stat == "blood_potency":
            if value == 0:
                # Blood Potency 0 uses Stamina
                attrs = target.db.stats.get("attributes", {})
                stamina = attrs.get("stamina", 1)
                advantages["vitae"] = stamina
            else:
                advantages["vitae"] = pool_lookup.get(value, 10)
            pool_updated = "vitae"
            
        elif template == "changeling" and stat == "wyrd":
            advantages["glamour"] = pool_lookup.get(value, 10)
            pool_updated = "glamour"
            
        elif template == "werewolf" and stat == "primal_urge":
            advantages["essence"] = pool_lookup.get(value, 10)
            pool_updated = "essence"
            
        elif template == "mage" and stat == "gnosis":
            advantages["mana"] = pool_lookup.get(value, 10)
            pool_updated = "mana"
            
        elif template == "geist" and stat == "synergy":
            advantages["plasm"] = pool_lookup.get(value, 10)
            pool_updated = "plasm"
            
        elif template == "promethean" and stat == "azoth":
            advantages["pyros"] = pool_lookup.get(value, 10)
            pool_updated = "pyros"
            
        elif template == "demon" and stat == "primum":
            advantages["aether"] = pool_lookup.get(value, 10)
            pool_updated = "aether"
            
        elif template == "deviant" and stat == "deviation":
            advantages["instability"] = pool_lookup.get(value, 10)
            pool_updated = "instability"
        
        if pool_updated:
            self.caller.msg(f"Updated power pool: {pool_updated}")
    
    def remove_stat_direct(self, target_name, stat):
        """
        Remove a stat directly (called from set_stat when value is empty).
        
        Args:
            target_name (str): Name of target character, or None for self
            stat (str): Name of the stat to remove
        """
        # Delegate to stat utilities
        from world.cofd.stat_utilities import remove_stat_from_character, check_stat_permissions
        
        # Determine target
        if target_name:
            target = self.caller.search(target_name, global_search=True)
            if not target:
                return
        else:
            target = self.caller
        
        # Check permissions
        has_permission, error_msg = check_stat_permissions(self.caller, target, is_removal=True)
        if not has_permission:
            self.caller.msg(error_msg)
            return
        
        # Remove the stat
        success, message = remove_stat_from_character(target, stat, self.caller)
        self.caller.msg(message)
    
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
        
        # Delegate to stat utilities
        from world.cofd.stat_utilities import remove_stat_from_character
        
        success, message = remove_stat_from_character(target, stat, self.caller)
        self.caller.msg(message)
    
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
                
                # Format merit display with instance if present
                display_name = merit_name
                if ":" in merit_name:
                    base_name, instance = merit_name.split(":", 1)
                    display_name = f"{base_name.replace('_', ' ').title()} ({instance.replace('_', ' ').title()})"
                else:
                    display_name = merit_name.replace('_', ' ').title()
                
                merit_display = f"{display_name} ({dots}/{max_dots} dots)"
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
                'promethean': 'Alembics & Bestowments',
                'demon': 'Embeds & Exploits',
                'beast': 'Nightmares',
                'hunter': 'Tactics',
                'deviant': 'Variations'
            }
            power_type = power_type_names.get(template, 'Powers')
            
            # Templates that use individual powers (semantic/known style) vs dot-rated powers
            individual_power_templates = ['changeling', 'promethean']
            
            # Display powers with dots or as known abilities
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
                    
                    # Check if this template uses individual powers (no dots) or rated powers
                    if template in individual_power_templates:
                        # For Changeling/Promethean, just show the power name
                        power_display = f"{display_name.replace('_', ' ').title()}"
                    else:
                        # For others, show dots
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
        
        # Delegate to geist template utilities
        from world.cofd.templates.geist import set_geist_stat_value, calculate_geist_derived_stats
        
        success, message = set_geist_stat_value(target, stat, value, self.caller)
        self.caller.msg(message)
        
        # Auto-calculate derived stats if setting attributes
        if success and stat in ["power", "finesse", "resistance"]:
            calculate_geist_derived_stats(target, self.caller)
    
    def _handle_semantic_power(self, target, power_type, power_name, value):
        """Handle semantic power syntax like key=beasts, ceremony=pass_on, alembic=purification"""
        # Delegate to power utilities
        from world.cofd.power_utilities import handle_semantic_power
        
        success, message = handle_semantic_power(target, power_type, power_name, value, self.caller)
        
        if not success:
            self.caller.msg(message)
        else:
            self.caller.msg(message)
        
        return success

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