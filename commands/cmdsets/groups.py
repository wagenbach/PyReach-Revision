"""
Command set for group-related commands.
"""

from evennia import CmdSet
from commands.groups import CmdGroups, CmdRoster


class GroupsCmdSet(CmdSet):
    """
    Command set for group management and roster commands.
    """
    
    key = "groups"
    priority = 10
    
    def at_cmdset_creation(self):
        """
        Populates the cmdset
        """
        self.add(CmdGroups())
        self.add(CmdRoster())
