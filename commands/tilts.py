from evennia.commands.default.muxcommand import MuxCommand
from evennia.utils import create
from world.tilts import Tilt, STANDARD_TILTS

class CmdTilt(MuxCommand):
    """
    Manage tilts on characters and environments during combat.
    
    Usage:
        +tilt/add [character] = <tilt_name>
        +tilt/remove [character] = <tilt_name>
        +tilt/list [character]
        +tilt/help <tilt_name>
        +tilt/env/add <tilt_name>
        +tilt/env/remove <tilt_name>
        +tilt/env/list
        +tilt/advance - Advance all tilts by one turn (staff/combat)
        +tilt/clear [character] - Clear all tilts (staff only)
        +tilt/env/clear - Clear all environmental tilts (staff only)
        
    Examples:
        +tilt/add = blinded
        +tilt/add John = stunned
        +tilt/remove = knocked_down
        +tilt/list
        +tilt/env/add darkness
        +tilt/env/list
        +tilt/help blinded
        +tilt/advance
    """
    key = "+tilt"
    aliases = ["+tilts"]
    locks = "cmd:all()"
    help_category = "Automated Combat System"
    
    def parse(self):
        """Parse the command arguments."""
        super().parse()
    
    def func(self):
        """
        This is the main command function that handles the switches.
        """
        # Check if legacy mode is active
        from commands.CmdLegacy import is_legacy_mode
        if is_legacy_mode():
            self.caller.msg("|rTilts system is disabled in Legacy Mode.|n")
            self.caller.msg("Legacy Mode uses traditional World of Darkness mechanics without tilts.")
            return
        
        if not self.switches:
            # Default behavior: list tilts on character
            self.tilt_list()
            return
            
        # Handle environmental tilts
        if "env" in self.switches:
            self.handle_environmental()
            return
            
        # Handle other switches
        switch = self.switches[0].lower()
        if switch == "add":
            self.tilt_add()
        elif switch == "remove":
            self.tilt_remove()
        elif switch == "list":
            self.tilt_list()
        elif switch == "help":
            self.tilt_help()
        elif switch == "list":
            self.tilt_list_all()
        elif switch == "advance":
            self.tilt_advance()
        elif switch == "clear":
            self.tilt_clear()
        else:
            self.caller.msg("Invalid switch. Use: add, remove, list, help, env, advance, or clear")
    
    def handle_environmental(self):
        """Handle environmental tilt commands"""
        if len(self.switches) < 2:
            self.caller.msg("Usage: +tilt/env/add, +tilt/env/remove, +tilt/env/list, or +tilt/env/clear")
            return
            
        env_switch = self.switches[1].lower()
        if env_switch == "add":
            self.env_add()
        elif env_switch == "remove":
            self.env_remove()
        elif env_switch == "list":
            self.env_list()
        elif env_switch == "clear":
            self.env_clear()
        else:
            self.caller.msg("Invalid environmental switch. Use: add, remove, list, or clear")
    
    def _check_permission(self, target):
        """Check if caller has permission to modify target's tilts"""
        if target == self.caller:
            return True
        return self.caller.check_permstring("Builder")
    
    def _check_combat_permission(self):
        """Check if caller can advance tilts (in combat or staff)"""
        if self.caller.check_permstring("Builder"):
            return True
        # Check if caller is in combat
        if hasattr(self.caller.location, 'combat_tracker'):
            return self.caller in self.caller.location.combat_tracker.participants
        return False
    
    def tilt_add(self):
        """Add a tilt to a character"""
        if not self.args:
            self.caller.msg("Usage: +tilt/add <tilt_name> or +tilt/add <character> = <tilt_name>")
            return
            
        if "=" in self.args:
            parts = self.args.split("=", 1)
            target_name, tilt_name = [part.strip() for part in parts]
        else:
            # If no = sign, default to caller
            target_name = "self"
            tilt_name = self.args.strip()
        
        # Find the target
        target = self.caller.search(target_name)
        if not target:
            return
            
        # Check permissions
        if not self._check_permission(target):
            self.caller.msg("You can only add tilts to yourself. Staff can add tilts to others.")
            return
            
        # Check if tilt exists
        tilt_name = tilt_name.lower()
        if tilt_name not in STANDARD_TILTS:
            self.caller.msg(f"Unknown tilt: {tilt_name}")
            self.caller.msg("Use '+tilt/help' to see available tilts.")
            return
            
        # Check if it's a personal tilt
        tilt_template = STANDARD_TILTS[tilt_name]
        if tilt_template.tilt_type != "personal":
            self.caller.msg(f"'{tilt_name}' is an environmental tilt. Use '+tilt/env/add {tilt_name}' instead.")
            return
            
        # Create a new instance of the tilt
        tilt = Tilt(
            name=tilt_template.name,
            description=tilt_template.description,
            tilt_type=tilt_template.tilt_type,
            duration=tilt_template.duration,
            effects=tilt_template.effects.copy(),
            resolution_method=tilt_template.resolution_method,
            condition_equivalent=tilt_template.condition_equivalent
        )
        
        # Add the tilt
        target.tilts.add(tilt)
        self.caller.msg(f"Added tilt {tilt.name} to {target.name}")

    def tilt_remove(self):
        """Remove a tilt from a character"""
        if not self.args:
            self.caller.msg("Usage: +tilt/remove <tilt_name> or +tilt/remove <character> = <tilt_name>")
            return
            
        if "=" in self.args:
            parts = self.args.split("=", 1)
            target_name, tilt_name = [part.strip() for part in parts]
        else:
            # If no = sign, default to caller
            target_name = "self"
            tilt_name = self.args.strip()
        
        # Find the target
        target = self.caller.search(target_name)
        if not target:
            return
            
        # Check permissions
        if not self._check_permission(target):
            self.caller.msg("You can only remove tilts from yourself. Staff can remove tilts from others.")
            return
            
        # Remove the tilt
        if target.tilts.remove(tilt_name):
            self.caller.msg(f"Removed tilt {tilt_name} from {target.name}")
        else:
            self.caller.msg(f"{target.name} does not have the tilt {tilt_name}")

    def tilt_list(self):
        """List all tilts on a character"""
        if not self.args:
            target = self.caller
        else:
            target = self.caller.search(self.args)
            if not target:
                return
                
        tilts = target.tilts.all()
        if not tilts:
            self.caller.msg(f"{target.name} has no tilts.")
            return
            
        # Format the output
        output = [f"Tilts on {target.name}:"]
        for tilt in tilts:
            duration_info = ""
            if tilt.turns_remaining is not None:
                duration_info = f" ({tilt.turns_remaining} turns remaining)"
                
            output.append(f"  |c{tilt.name}|n{duration_info}: {tilt.description}")
            if tilt.resolution_method:
                output.append(f"    |yResolution:|n {tilt.resolution_method}")
                
        self.caller.msg("\n".join(output))

    def tilt_list_all(self):
        """List all available tilts"""
        output = ["Available Tilts:"]
        output.append("\n|cPersonal Tilts:|n")
        personal_tilts = [name for name, tilt in STANDARD_TILTS.items() if tilt.tilt_type == "personal"]
        for tilt_name in sorted(personal_tilts):
            output.append(f"  {tilt_name}")
            
        output.append("\n|cEnvironmental Tilts:|n")
        environmental_tilts = [name for name, tilt in STANDARD_TILTS.items() if tilt.tilt_type == "environmental"]
        for tilt_name in sorted(environmental_tilts):
            output.append(f"  {tilt_name}")
            
        output.append("\nUse '+tilt/help <tilt_name>' for detailed information.")
        self.caller.msg("\n".join(output))
        
    def tilt_help(self):
        """Get information about a specific tilt"""
        if not self.args:
            self.caller.msg("Usage: +tilt/help <tilt_name>")
            return
            
        tilt_name = self.args.strip().lower()
        if tilt_name not in STANDARD_TILTS:
            self.caller.msg(f"Unknown tilt: {tilt_name}")
            return
            
        tilt = STANDARD_TILTS[tilt_name]
        output = [
            f"|cTilt: {tilt.name}|n",
            f"Type: {tilt.tilt_type.title()}",
            f"Description: {tilt.description}"
        ]
        
        if tilt.duration:
            output.append(f"Duration: {tilt.duration} turns")
        else:
            output.append("Duration: Until resolved")
            
        if tilt.resolution_method:
            output.append(f"Resolution: {tilt.resolution_method}")
            
        if tilt.effects:
            output.append("Effects:")
            for effect, value in tilt.effects.items():
                output.append(f"  {effect}: {value}")
                
        if tilt.condition_equivalent:
            output.append(f"Becomes condition when out of combat: {tilt.condition_equivalent}")
                
        self.caller.msg("\n".join(output))
    
    def tilt_advance(self):
        """Advance all tilts by one turn"""
        if not self._check_combat_permission():
            self.caller.msg("Only staff or combat participants can advance tilts.")
            return
            
        # Advance personal tilts for all characters in location
        expired_personal = []
        for obj in self.caller.location.contents:
            if hasattr(obj, 'tilts'):
                expired = obj.tilts.advance_turn()
                if expired:
                    expired_personal.extend([(obj, tilt) for tilt in expired])
        
        # Advance environmental tilts
        expired_environmental = []
        if hasattr(self.caller.location, 'environmental_tilts'):
            expired_environmental = self.caller.location.environmental_tilts.advance_turn()
        
        # Report results
        output = ["Advanced all tilts by one turn."]
        
        if expired_personal:
            output.append("\nExpired personal tilts:")
            for obj, tilt_name in expired_personal:
                output.append(f"  {obj.name}: {tilt_name}")
                
        if expired_environmental:
            output.append("\nExpired environmental tilts:")
            for tilt_name in expired_environmental:
                output.append(f"  {tilt_name}")
                
        if not expired_personal and not expired_environmental:
            output.append("No tilts expired this turn.")
            
        self.caller.msg("\n".join(output))
    
    def tilt_clear(self):
        """Clear all tilts from a character (staff only)"""
        if not self.caller.check_permstring("Builder"):
            self.caller.msg("Only staff can clear all tilts.")
            return
            
        if not self.args:
            target = self.caller
        else:
            target = self.caller.search(self.args)
            if not target:
                return
                
        target.tilts.clear_all()
        self.caller.msg(f"Cleared all tilts from {target.name}")
    
    def env_add(self):
        """Add an environmental tilt"""
        if not self.caller.check_permstring("Builder"):
            self.caller.msg("Only staff can add environmental tilts.")
            return
            
        if not self.args:
            self.caller.msg("Usage: +tilt/env/add <tilt_name>")
            return
            
        tilt_name = self.args.strip().lower()
        if tilt_name not in STANDARD_TILTS:
            self.caller.msg(f"Unknown tilt: {tilt_name}")
            return
            
        # Check if it's an environmental tilt
        tilt_template = STANDARD_TILTS[tilt_name]
        if tilt_template.tilt_type != "environmental":
            self.caller.msg(f"'{tilt_name}' is a personal tilt. Use '+tilt/add {tilt_name}' instead.")
            return
            
        # Create environmental tilt handler if needed
        if not hasattr(self.caller.location, 'environmental_tilts'):
            from world.tilts import EnvironmentalTiltHandler
            self.caller.location.environmental_tilts = EnvironmentalTiltHandler(self.caller.location)
        
        # Create a new instance of the tilt
        tilt = Tilt(
            name=tilt_template.name,
            description=tilt_template.description,
            tilt_type=tilt_template.tilt_type,
            duration=tilt_template.duration,
            effects=tilt_template.effects.copy(),
            resolution_method=tilt_template.resolution_method,
            condition_equivalent=tilt_template.condition_equivalent
        )
        
        # Add the environmental tilt
        self.caller.location.environmental_tilts.add(tilt)
        self.caller.msg(f"Added environmental tilt {tilt.name} to this location")
    
    def env_remove(self):
        """Remove an environmental tilt"""
        if not self.caller.check_permstring("Builder"):
            self.caller.msg("Only staff can remove environmental tilts.")
            return
            
        if not self.args:
            self.caller.msg("Usage: +tilt/env/remove <tilt_name>")
            return
            
        if not hasattr(self.caller.location, 'environmental_tilts'):
            self.caller.msg("No environmental tilts in this location.")
            return
            
        tilt_name = self.args.strip()
        if self.caller.location.environmental_tilts.remove(tilt_name):
            self.caller.msg(f"Removed environmental tilt {tilt_name} from this location")
        else:
            self.caller.msg(f"This location does not have the environmental tilt {tilt_name}")
    
    def env_list(self):
        """List all environmental tilts in the current location"""
        if not hasattr(self.caller.location, 'environmental_tilts'):
            self.caller.msg("No environmental tilts in this location.")
            return
            
        tilts = self.caller.location.environmental_tilts.all()
        if not tilts:
            self.caller.msg("No environmental tilts in this location.")
            return
            
        # Format the output
        output = ["Environmental tilts in this location:"]
        for tilt in tilts:
            duration_info = ""
            if tilt.turns_remaining is not None:
                duration_info = f" ({tilt.turns_remaining} turns remaining)"
                
            output.append(f"  |c{tilt.name}|n{duration_info}: {tilt.description}")
            if tilt.resolution_method:
                output.append(f"    |yResolution:|n {tilt.resolution_method}")
                
        self.caller.msg("\n".join(output))
    
    def env_clear(self):
        """Clear all environmental tilts (staff only)"""
        if not self.caller.check_permstring("Builder"):
            self.caller.msg("Only staff can clear all environmental tilts.")
            return
            
        if not hasattr(self.caller.location, 'environmental_tilts'):
            self.caller.msg("No environmental tilts in this location.")
            return
            
        self.caller.location.environmental_tilts.clear_all()
        self.caller.msg("Cleared all environmental tilts from this location") 