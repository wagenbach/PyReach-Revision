"""
Custom help command with forced width control.
"""

from evennia.commands.default.help import CmdHelp as DefaultCmdHelp
from evennia.utils import evtable


class CmdHelp(DefaultCmdHelp):
    """
    Custom help command that forces 80-character width.
    
    Usage:
        help [topic or command]
        help list
        help all
    """
    
    def func(self):
        """Execute the help command with forced 80-character width."""
        # Store the original caller width detection
        original_client_width = self.caller.client_width
        
        # Force 80-character width for this command
        self.caller.client_width = lambda: 80
        
        try:
            # Call the original help command
            super().func()
        finally:
            # Restore original width detection
            self.caller.client_width = original_client_width


# Alternative: Override just the command listing part
class CmdHelpFixed(DefaultCmdHelp):
    """
    Help command with fixed-width command listings.
    """
    
    def list_all_commands(self):
        """List all available commands with forced 80-character width."""
        # Get all available commands
        all_commands = self.caller.cmdset.get_all_cmd_keys_and_aliases()
        
        # Create table with forced width
        table = evtable.EvTable(
            "|wCommand|n", "|wDescription|n",
            table=True,
            border="cells",
            width=80,  # Force 80 characters
            maxwidth=80
        )
        
        # Add commands to table
        for cmd_key in sorted(all_commands):
            cmd = self.caller.cmdset.get(cmd_key)
            if cmd:
                table.add_row(cmd.key, cmd.__doc__.split('\n')[0] if cmd.__doc__ else "No description")
        
        self.caller.msg(str(table)) 