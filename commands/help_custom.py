"""
Custom help command that escapes ANSI codes in help text.
"""

from evennia.commands.default.help import CmdHelp as DefaultCmdHelp
from evennia.utils import evtable
from textwrap import dedent


class CmdHelp(DefaultCmdHelp):
    """
    Custom help command that escapes ANSI codes in help text.
    
    Usage:
        help [topic or command]
        help list
        help all
    """
    
    def format_help_entry(
        self,
        topic="",
        help_text="",
        aliases=None,
        suggested=None,
        subtopics=None,
        click_topics=True,
    ):
        """
        Override format_help_entry to escape ANSI codes in the help text content only.
        This preserves the header/footer formatting while preventing docstring ANSI interpretation.
        """
        # Escape ANSI codes in the help text content only
        if help_text:
            # Escape pipe characters to prevent ANSI interpretation
            escaped_help_text = help_text.replace('|', '||')
        else:
            escaped_help_text = help_text
        
        # Call the parent's format_help_entry with escaped help text
        return super().format_help_entry(
            topic=topic,
            help_text=escaped_help_text,
            aliases=aliases,
            suggested=suggested,
            subtopics=subtopics,
            click_topics=click_topics,
        )


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