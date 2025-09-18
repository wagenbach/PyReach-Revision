"""
Chronicles of Darkness Combat Commands - Refactored Version
"""

from evennia.commands.default.muxcommand import MuxCommand
from evennia.utils import evtable
from .combat_core import CombatTracker, WeaponData
from .base import BaseExordiumCommand, BuilderMixin
from world.utils.permission_utils import check_builder_permission

class CmdCombat(BaseExordiumCommand, BuilderMixin):
    """
    Chronicles of Darkness Combat System
    
    Usage:
        +combat/init [modifier] - Roll initiative
        +combat/status - Show combat status
        +combat/next - Advance to next turn (staff/participants)
        +combat/join [team] - Join combat (optionally specify team number)
        +combat/leave - Leave combat
        +combat/end - End combat (staff only)
    """
    
    key = "+combat"
    aliases = ["+fight", "+init"]
    help_category = "Automated Combat System"
    
    def func(self):
        """Execute the command"""
        # Get or create combat tracker for this location
        if not hasattr(self.caller.location, 'combat_tracker'):
            self.caller.location.combat_tracker = CombatTracker(self.caller.location)
            
        self.combat = self.caller.location.combat_tracker
        
        if not self.switches:
            self.caller.msg("Use +combat/help for combat commands. Common: /init, /status")
            return
            
        switch = self.switches[0].lower()
        
        if switch == "init":
            self.roll_initiative()
        elif switch == "status":
            self.show_combat_status()
        elif switch == "join":
            self.join_combat()
        elif switch == "leave":
            self.leave_combat()
        elif switch == "end":
            self.end_combat()
        else:
            self.caller.msg("Invalid combat command.")
    
    def roll_initiative(self):
        """Roll initiative for combat"""
        modifier = 0
        if self.args:
            try:
                modifier = int(self.args)
            except ValueError:
                self.caller.msg("Initiative modifier must be a number.")
                return
                
        roll, init_attr = self.combat.roll_initiative(self.caller)
        total_mod = init_attr + modifier
        
        self.caller.msg(f"Initiative: {roll} (1d10 + {total_mod})")
        
    def show_combat_status(self):
        """Show current combat status"""
        if not self.combat.participants:
            self.caller.msg("No active combat in this location.")
            return
            
        table = evtable.EvTable("Character", "Team", "Initiative", "Status")
        
        for char in self.combat.initiative_order:
            data = self.combat.participants[char]
            status_parts = []
            
            if data.get('prone'):
                status_parts.append("Prone")
            if data.get('in_cover'):
                status_parts.append(f"Cover {data['cover_rating']}")
                
            status = ", ".join(status_parts) if status_parts else "Normal"
            
            name = char.name
            if char == self.combat.current_actor:
                name = f"|y{name}*|n"
                
            team = data['team']
            team_display = f"|c{team}|n" if team else "None"
                
            table.add_row(name, team_display, data['initiative'], status)
            
        output = [f"Combat Status - Round {self.combat.round_number}, Turn {self.combat.turn_number}"]
        output.append(str(table))
        
        self.caller.msg("\n".join(output))
        
    def join_combat(self):
        """Join combat"""
        team = None
        if self.args:
            try:
                team = int(self.args)
            except ValueError:
                self.caller.msg("Team number must be a number.")
                return
                
        self.combat.add_participant(self.caller, team)
        assigned_team = self.combat.get_team(self.caller)
        self.caller.msg(f"You join combat on team {assigned_team}!")
        
    def leave_combat(self):
        """Leave combat"""
        self.combat.remove_participant(self.caller)
        self.caller.msg("You leave combat.")
        
    def end_combat(self):
        """End combat"""
        if not self.check_builder_access():
            return
            
        self.combat.end_combat()
        self.caller.location.msg_contents("Combat has ended.")

class CmdCombatHelp(BaseExordiumCommand):
    """
    Get quick combat help and action reference.
    """
    
    key = "+chelp"
    aliases = ["+combathelp"]
    help_category = "Automated Combat System"
    
    def func(self):
        """Execute the command"""
        output = [
            "|cChronicles of Darkness Combat Quick Reference|n",
            "",
            "|yBasic Combat Flow:|n",
            "1. Join combat: +combat/join [team]",
            "2. Roll initiative: +combat/init",
            "3. Take actions on your turn",
            "",
            "|yCommon Commands:|n",
            "+combat/status - Show combat status",
            "+combat/join - Join combat",
            "+combat/leave - Leave combat",
            "+combat/end - End combat (staff only)"
        ]
        
        self.caller.msg("\n".join(output))

class CmdEquippedGear(BaseExordiumCommand):
    """
    View your currently equipped weapons and armor.
    """
    
    key = "+gear"
    aliases = ["+equipped"]
    help_category = "Automated Combat System"
    
    def func(self):
        """Execute the command"""
        target = self.caller
        if self.args:
            target = self.caller.search(self.args)
            if not target:
                return
            
        output = [f"Equipped gear for {target.name}:"]
        
        # Show wielded weapon
        wielded_weapon = target.db.wielded_weapon
        if wielded_weapon:
            output.append(f"Wielded: {wielded_weapon}")
        else:
            output.append("Wielded: None (unarmed)")
            
        # Show worn armor
        worn_armor = target.db.worn_armor
        if worn_armor:
            output.append(f"Armor: {worn_armor}")
        else:
            output.append("Armor: None")
            
        self.caller.msg("\n".join(output))
