"""
ANSI utility functions for text formatting and wrapping.
"""

from evennia.utils.ansi import ANSIString


def wrap_ansi(text, width=78, left_padding=0):
    """
    Wrap text while preserving ANSI codes.
    
    Args:
        text (str): The text to wrap (may contain ANSI codes)
        width (int): The maximum width for wrapping
        left_padding (int): Amount of left padding to apply
        
    Returns:
        str: The wrapped text with ANSI codes preserved
    """
    # Convert to ANSIString to handle ANSI codes properly
    ansi_text = ANSIString(text)
    
    # Simple wrapping - split by spaces and reassemble
    words = str(ansi_text).split()
    lines = []
    current_line = ""
    padding = " " * left_padding
    
    for word in words:
        # Check length without ANSI codes
        test_line = current_line + (" " if current_line else "") + word
        test_length = len(ANSIString(test_line).clean())
        
        if test_length <= width - left_padding:
            current_line = test_line
        else:
            if current_line:
                lines.append(padding + current_line)
            current_line = word
    
    if current_line:
        lines.append(padding + current_line)
    
    return "\n".join(lines) if lines else text
