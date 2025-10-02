"""
Formatting utility functions for consistent display across the game.
"""

from evennia.utils.ansi import ANSIString


def header(text, width=78, color="|b"):
    """
    Create a centered header line.
    
    Args:
        text (str): The header text
        width (int): Total width of the header
        color (str): ANSI color code
        
    Returns:
        str: Formatted header string
    """
    # Strip existing ANSI codes for length calculation
    clean_text = ANSIString(text).clean()
    text_length = len(clean_text)
    
    # Calculate padding
    padding = (width - text_length - 4) // 2  # -4 for "< >" decorations
    
    return f"{color}{'-' * padding}< |w{text}|n {color}>{'-' * (width - padding - text_length - 4)}|n"


def footer(width=78, color="|b"):
    """
    Create a footer line.
    
    Args:
        width (int): Total width of the footer
        color (str): ANSI color code
        
    Returns:
        str: Formatted footer string
    """
    return f"{color}{'-' * width}|n"


def divider(width=78, char="-", color="|b"):
    """
    Create a divider line.
    
    Args:
        width (int): Total width of the divider
        char (str): Character to use for the divider
        color (str): ANSI color code
        
    Returns:
        str: Formatted divider string
    """
    return f"{color}{char * width}|n"


def format_stat(name, value, width=40):
    """
    Format a stat name and value for display.
    
    Args:
        name (str): Stat name
        value: Stat value
        width (int): Total width for the stat line
        
    Returns:
        str: Formatted stat string
    """
    dots = "." * (width - len(name) - len(str(value)))
    return f"{name}{dots}{value}"
