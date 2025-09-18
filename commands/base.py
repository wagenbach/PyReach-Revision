"""
Base command classes and mixins for shared functionality.
"""

from evennia.commands.default.muxcommand import MuxCommand
from world.utils.permission_utils import (
    check_staff_permission, check_admin_permission, check_builder_permission,
    can_modify_character_stats, format_permission_error
)

class StaffOnlyMixin:
    """Mixin for commands that require staff permissions."""
    
    def check_staff_access(self):
        """Check if caller has staff access, return error message if not."""
        if not check_staff_permission(self.caller):
            self.caller.msg(format_permission_error("Staff"))
            return False
        return True

class AdminOnlyMixin:
    """Mixin for commands that require admin permissions."""
    
    def check_admin_access(self):
        """Check if caller has admin access, return error message if not."""
        if not check_admin_permission(self.caller):
            self.caller.msg(format_permission_error("Admin"))
            return False
        return True

class BuilderMixin:
    """Mixin for commands that require builder permissions."""
    
    def check_builder_access(self):
        """Check if caller has builder access, return error message if not."""
        if not check_builder_permission(self.caller):
            self.caller.msg(format_permission_error("Builder"))
            return False
        return True

class CharacterStatsMixin:
    """Mixin for commands that modify character stats."""
    
    def can_modify_stats(self, target):
        """
        Check if caller can modify target's stats.
        
        Args:
            target: The character whose stats would be modified
            
        Returns:
            bool: True if modification is allowed
        """
        can_modify, reason = can_modify_character_stats(self.caller, target)
        if not can_modify:
            self.caller.msg(reason)
        return can_modify

class HealthMixin:
    """Mixin for commands that work with health systems."""
    
    def get_health_summary(self, character):
        """
        Get a summary of character's current health status.
        
        Args:
            character: The character to check
            
        Returns:
            dict: Health summary with current/max and damage counts
        """
        from world.utils.health_utils import get_health_track
        
        advantages = character.db.stats.get("advantages", {})
        health_max = advantages.get("health", 7)
        track = get_health_track(character)
        
        damage_counts = {"bashing": 0, "lethal": 0, "aggravated": 0}
        for damage_type in track:
            if damage_type:
                damage_counts[damage_type] += 1
        
        total_damage = sum(damage_counts.values())
        
        return {
            "current": health_max - total_damage,
            "maximum": health_max,
            "damage_counts": damage_counts,
            "total_damage": total_damage
        }

class TargetResolutionMixin:
    """Mixin for commands that need to resolve character targets."""
    
    def find_target(self, target_name, global_search=True):
        """
        Find a target character with standardized error handling.
        
        Args:
            target_name: Name to search for
            global_search: Whether to search globally
            
        Returns:
            Character object or None if not found
        """
        if not target_name:
            return self.caller
        
        target = self.caller.search(target_name, global_search=global_search)
        if not target:
            self.caller.msg(f"Could not find character '{target_name}'.")
            return None
        
        return target

class BaseExordiumCommand(MuxCommand):
    """
    Base command class for Exordium commands with common functionality.
    """
    
    def at_pre_cmd(self):
        """Called before command execution."""
        # Add any global pre-command logic here
        return super().at_pre_cmd()
    
    def at_post_cmd(self):
        """Called after command execution."""
        # Add any global post-command logic here
        return super().at_post_cmd()
    
    def format_error(self, message):
        """Format error messages consistently."""
        return f"|r{message}|n"
    
    def format_success(self, message):
        """Format success messages consistently."""
        return f"|g{message}|n"
    
    def format_info(self, message):
        """Format info messages consistently."""
        return f"|c{message}|n"
