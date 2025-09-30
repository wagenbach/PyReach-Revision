"""
Chronicles of Darkness Combat Commands - Refactored Version
"""

from evennia.commands.default.muxcommand import MuxCommand
from evennia.utils import evtable
# from .combat_core import CombatTracker, WeaponData  # Disabled - module doesn't exist
from .base import BaseExordiumCommand, BuilderMixin
from world.utils.permission_utils import check_builder_permission

# Combat system implementation
from world.utils.dice_utils import roll_dice, RollType
import secrets

class WeaponData:
    """Data class for weapon statistics"""
    
    def __init__(self, name, damage=0, initiative_mod=0, weapon_type="melee", 
                 skill="weaponry", attribute="strength", range_short=0, 
                 range_medium=0, range_long=0, armor_piercing=0):
        self.name = name
        self.damage = damage  # Damage modifier
        self.initiative_mod = initiative_mod  # Initiative modifier
        self.weapon_type = weapon_type  # "melee", "ranged", "thrown"
        self.skill = skill  # Required skill
        self.attribute = attribute  # Primary attribute
        self.range_short = range_short  # Short range (yards)
        self.range_medium = range_medium  # Medium range (yards) 
        self.range_long = range_long  # Long range (yards)
        self.armor_piercing = armor_piercing  # Armor piercing rating
        
    def get_attack_pool(self, character):
        """Calculate attack dice pool for this weapon"""
        attr_value = character.db.stats.get("attributes", {}).get(self.attribute, 1)
        skill_value = character.db.stats.get("skills", {}).get(self.skill, 0)
        return attr_value + skill_value
        
    def get_damage_rating(self):
        """Get weapon damage rating"""
        return self.damage
        
    def is_ranged(self):
        """Check if weapon is ranged"""
        return self.weapon_type in ["ranged", "thrown"]

# Common weapon definitions
WEAPON_DATA = {
    "unarmed": WeaponData("Unarmed", damage=0, skill="brawl", attribute="strength"),
    "knife": WeaponData("Knife", damage=1, initiative_mod=-1, skill="weaponry"),
    "sword": WeaponData("Sword", damage=3, initiative_mod=-2, skill="weaponry"),
    "gun": WeaponData("Pistol", damage=2, weapon_type="ranged", skill="firearms", 
                     attribute="dexterity", range_short=20, range_medium=40, range_long=80),
}

class CombatTracker:
    """Full combat tracker implementation for Chronicles of Darkness"""
    
    def __init__(self, location):
        self.location = location
        self.participants = {}  # character: {data}
        self.initiative_order = []
        self.current_actor = None
        self.round_number = 1
        self.turn_number = 1
        self.teams = {}  # team_number: [characters]
        self.next_team = 1
        
    def add_participant(self, character, team=None):
        """Add a character to combat"""
        if character in self.participants:
            return  # Already in combat
            
        # Auto-assign team if not specified
        if team is None:
            team = self.next_team
            self.next_team += 1
            
        # Initialize team if needed
        if team not in self.teams:
            self.teams[team] = []
            
        # Add to team
        self.teams[team].append(character)
        
        # Initialize participant data
        self.participants[character] = {
            'team': team,
            'initiative': 0,
            'has_acted': False,
            'defense_applied': 0,
            'conditions': [],
            'prone': False,
            'in_cover': False,
            'cover_rating': 0,
            'all_out_attack': False,
            'dodge_applied': False,
            'actions_taken': 0
        }
        
        # Announce to location
        self.location.msg_contents(f"{character.name} joins combat on team {team}!")
        
    def remove_participant(self, character):
        """Remove a character from combat"""
        if character not in self.participants:
            return
            
        # Remove from team
        team = self.participants[character]['team']
        if team in self.teams and character in self.teams[team]:
            self.teams[team].remove(character)
            
        # Remove from participants
        del self.participants[character]
        
        # Remove from initiative order
        if character in self.initiative_order:
            self.initiative_order.remove(character)
            
        # Update current actor if needed
        if self.current_actor == character:
            self.advance_turn()
            
        # Announce to location
        self.location.msg_contents(f"{character.name} leaves combat.")
        
    def get_team(self, character):
        """Get character's team number"""
        if character in self.participants:
            return self.participants[character]['team']
        return None
        
    def roll_initiative(self, character):
        """Roll initiative for a character"""
        if character not in self.participants:
            return None, None
            
        # Get initiative attribute (Dexterity + Composure)
        dex = character.db.stats.get("attributes", {}).get("dexterity", 1)
        composure = character.db.stats.get("attributes", {}).get("composure", 1)
        init_attr = dex + composure
        
        # Roll 1d10 + initiative
        roll = secrets.randbelow(10) + 1
        total_initiative = roll + init_attr
        
        # Store initiative
        self.participants[character]['initiative'] = total_initiative
        
        # Update initiative order
        self.update_initiative_order()
        
        return roll, init_attr
        
    def update_initiative_order(self):
        """Update the initiative order based on current initiatives"""
        # Sort by initiative (highest first)
        self.initiative_order = sorted(
            self.participants.keys(),
            key=lambda char: self.participants[char]['initiative'],
            reverse=True
        )
        
        # Set current actor to first in order if not set
        if not self.current_actor and self.initiative_order:
            self.current_actor = self.initiative_order[0]
            
    def advance_turn(self):
        """Advance to the next character's turn"""
        if not self.initiative_order:
            return
            
        # Find current actor index
        if self.current_actor in self.initiative_order:
            current_index = self.initiative_order.index(self.current_actor)
            next_index = (current_index + 1) % len(self.initiative_order)
        else:
            next_index = 0
            
        # If we've cycled through everyone, advance round
        if next_index == 0:
            self.advance_round()
        else:
            self.turn_number += 1
            
        # Set next actor
        self.current_actor = self.initiative_order[next_index]
        
        # Reset per-turn flags for new actor
        self.reset_turn_flags(self.current_actor)
        
        # Announce turn
        self.location.msg_contents(
            f"Round {self.round_number}, Turn {self.turn_number}: "
            f"{self.current_actor.name}'s turn!"
        )
        
    def advance_round(self):
        """Advance to the next round"""
        self.round_number += 1
        self.turn_number = 1
        
        # Reset per-round flags for all participants
        for character in self.participants:
            self.participants[character]['has_acted'] = False
            self.participants[character]['actions_taken'] = 0
            self.participants[character]['all_out_attack'] = False
            self.participants[character]['dodge_applied'] = False
            
        self.location.msg_contents(f"Beginning Round {self.round_number}")
        
    def reset_turn_flags(self, character):
        """Reset per-turn flags for a character"""
        if character in self.participants:
            self.participants[character]['has_acted'] = False
            
    def get_defense(self, character):
        """Calculate character's current Defense rating"""
        if character not in self.participants:
            return 0
            
        # Base Defense = min(Wits, Dexterity) + Athletics
        wits = character.db.stats.get("attributes", {}).get("wits", 1)
        dex = character.db.stats.get("attributes", {}).get("dexterity", 1)
        athletics = character.db.stats.get("skills", {}).get("athletics", 0)
        
        base_defense = min(wits, dex) + athletics
        
        # Apply modifiers
        data = self.participants[character]
        
        # Prone reduces Defense
        if data.get('prone'):
            base_defense = max(0, base_defense - 2)
            
        # Cover provides Defense bonus against ranged attacks
        if data.get('in_cover'):
            base_defense += data.get('cover_rating', 0)
            
        # All-out attack removes Defense
        if data.get('all_out_attack'):
            base_defense = 0
            
        # Dodge doubles Defense (applied once per turn)
        if data.get('dodge_applied'):
            base_defense *= 2
            
        return max(0, base_defense)
        
    def end_combat(self):
        """End combat and clean up"""
        self.location.msg_contents("Combat has ended!")
        
        # Clear combat tracker from location
        if hasattr(self.location, 'combat_tracker'):
            del self.location.combat_tracker
            
        # Reset participant flags
        for character in self.participants:
            # Clear combat-specific attributes
            if hasattr(character.db, 'in_combat'):
                del character.db.in_combat

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
            self.caller.msg("Use +combat/help for combat commands. Common: /init, /status, /join")
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
        elif switch == "next":
            self.advance_turn()
        elif switch == "end":
            self.end_combat()
        elif switch == "help":
            self.show_help()
        else:
            self.caller.msg("Invalid combat command. Use +combat/help for available commands.")
    
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
        
    def advance_turn(self):
        """Advance to next turn (staff or participants only)"""
        # Check if caller is in combat or is staff
        if self.caller not in self.combat.participants:
            if not self.check_builder_access():
                self.caller.msg("You must be in combat or have builder access to advance turns.")
                return
        
        self.combat.advance_turn()
        
    def end_combat(self):
        """End combat"""
        if not self.check_builder_access():
            return
            
        self.combat.end_combat()
        
    def show_help(self):
        """Show combat help"""
        output = [
            "|cChronicles of Darkness Combat Commands|n",
            "",
            "|yBasic Commands:|n",
            "+combat/join [team] - Join combat (optionally specify team)",
            "+combat/init [modifier] - Roll initiative", 
            "+combat/status - Show combat status and turn order",
            "+combat/next - Advance to next turn",
            "+combat/leave - Leave combat",
            "+combat/end - End combat (staff only)",
            "",
            "|yExample Usage:|n",
            "+combat/join 1 - Join team 1",
            "+combat/init 2 - Roll initiative with +2 modifier",
            "+combat/status - Check who's turn it is",
        ]
        
        self.caller.msg("\n".join(output))

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
