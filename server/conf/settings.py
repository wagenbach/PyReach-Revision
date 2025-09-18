r"""
Evennia settings file.

The available options are found in the default settings file found
here:

https://www.evennia.com/docs/latest/Setup/Settings-Default.html

Remember:

Don't copy more from the default file than you actually intend to
change; this will make sure that you don't overload upstream updates
unnecessarily.

When changing a setting requiring a file system path (like
path/to/actual/file.py), use GAME_DIR and EVENNIA_DIR to reference
your game folder and the Evennia library folders respectively. Python
paths (path.to.module) should be given relative to the game's root
folder (typeclasses.foo) whereas paths within the Evennia library
needs to be given explicitly (evennia.foo).

If you want to share your game dir, including its settings, you can
put secret game- or server-specific settings in secret_settings.py.

"""

# Use the defaults from Evennia unless explicitly overridden
from evennia.settings_default import *
from evennia.contrib.base_systems import color_markups

######################################################################
# Evennia base server config
######################################################################

# This is the name of your game. Make it catchy!
SERVERNAME = "exordium"

# Force 80-character width for help files and formatted output
CLIENT_DEFAULT_WIDTH = 80

# Text formatting settings
# Enable special character substitutions (%r for newlines, %t for tabs)
ENABLE_SPECIAL_CHAR_SUBSTITUTIONS = True

# Define custom substitutions (can be extended by admins)
SPECIAL_CHAR_SUBSTITUTIONS = {
    '%r%r': '\n\n',  # Paragraph break (must be processed first)
    '%r': '\n',      # Newline/carriage return
    '%t': '     ',   # Tab (5 spaces)
}

# Add your custom apps to the existing INSTALLED_APPS
INSTALLED_APPS += [
    'world.cofd',
    'world.jobs',
]
"""
BASE ANSI MARKUP CONFIGURATION
See below for more specific color markup configurations.

Note that this is not the only place to set %r/%t replacements, as that needs to also be done
within each file that uses the MUX carriage return or tab style.
"""
# Disable default pipe-based color system to prevent conflicts with help files
COLOR_NO_DEFAULT = True

COLOR_ANSI_EXTRA_MAP = color_markups.MUX_COLOR_ANSI_EXTRA_MAP
COLOR_XTERM256_EXTRA_FG = color_markups.MUX_COLOR_XTERM256_EXTRA_FG
COLOR_XTERM256_EXTRA_BG = color_markups.MUX_COLOR_XTERM256_EXTRA_BG
COLOR_XTERM256_EXTRA_GFG = color_markups.MUX_COLOR_XTERM256_EXTRA_GFG
COLOR_XTERM256_EXTRA_GBG = color_markups.MUX_COLOR_XTERM256_EXTRA_GBG
COLOR_ANSI_XTERM256_BRIGHT_BG_EXTRA_MAP = color_markups.MUX_COLOR_ANSI_XTERM256_BRIGHT_BG_EXTRA_MAP

# ANSI constants (copied from evennia.utils.ansi to avoid import)

_ANSI_BEEP = "\07"
_ANSI_ESCAPE = "\033"
_ANSI_NORMAL = "\033[0m"

_ANSI_UNDERLINE = "\033[4m"
_ANSI_HILITE = "\033[1m"
_ANSI_UNHILITE = "\033[22m"
_ANSI_BLINK = "\033[5m"
_ANSI_INVERSE = "\033[7m"
_ANSI_INV_HILITE = "\033[1;7m"
_ANSI_INV_BLINK = "\033[7;5m"
_ANSI_BLINK_HILITE = "\033[1;5m"
_ANSI_INV_BLINK_HILITE = "\033[1;5;7m"

# Foreground colors
_ANSI_BLACK = "\033[30m"
_ANSI_RED = "\033[31m"
_ANSI_GREEN = "\033[32m"
_ANSI_YELLOW = "\033[33m"
_ANSI_BLUE = "\033[34m"
_ANSI_MAGENTA = "\033[35m"
_ANSI_CYAN = "\033[36m"
_ANSI_WHITE = "\033[37m"

# Background colors
_ANSI_BACK_BLACK = "\033[40m"
_ANSI_BACK_RED = "\033[41m"
_ANSI_BACK_GREEN = "\033[42m"
_ANSI_BACK_YELLOW = "\033[43m"
_ANSI_BACK_BLUE = "\033[44m"
_ANSI_BACK_MAGENTA = "\033[45m"
_ANSI_BACK_CYAN = "\033[46m"
_ANSI_BACK_WHITE = "\033[47m"

# Formatting Characters
_ANSI_RETURN = "\r\n"
_ANSI_TAB = "\t"
_ANSI_SPACE = " "

MUX_COLOR_ANSI_EXTRA_MAP = [
    (r"%cn", _ANSI_NORMAL),  # reset
    (r"%ch", _ANSI_HILITE),  # highlight
    (r"%r", _ANSI_RETURN),  # line break
    (r"%R", _ANSI_RETURN),  #
    (r"%t", _ANSI_TAB),  # tab
    (r"%T", _ANSI_TAB),  #
    (r"%b", _ANSI_SPACE),  # space
    (r"%B", _ANSI_SPACE),
    (r"%cf", _ANSI_BLINK),  # annoying and not supported by all clients
    (r"%ci", _ANSI_INVERSE),  # invert
    (r"%cr", _ANSI_RED),
    (r"%cg", _ANSI_GREEN),
    (r"%cy", _ANSI_YELLOW),
    (r"%cb", _ANSI_BLUE),
    (r"%cm", _ANSI_MAGENTA),
    (r"%cc", _ANSI_CYAN),
    (r"%cw", _ANSI_WHITE),
    (r"%cx", _ANSI_BLACK),
    (r"%cR", _ANSI_BACK_RED),
    (r"%cG", _ANSI_BACK_GREEN),
    (r"%cY", _ANSI_BACK_YELLOW),
    (r"%cB", _ANSI_BACK_BLUE),
    (r"%cM", _ANSI_BACK_MAGENTA),
    (r"%cC", _ANSI_BACK_CYAN),
    (r"%cW", _ANSI_BACK_WHITE),
    (r"%cX", _ANSI_BACK_BLACK),
]

MUX_COLOR_XTERM256_EXTRA_FG = [r"%c([0-5])([0-5])([0-5])"]  # %c123 - foreground colour
MUX_COLOR_XTERM256_EXTRA_BG = [r"%c\[([0-5])([0-5])([0-5])"]  # %c[123 - background colour
MUX_COLOR_XTERM256_EXTRA_GFG = [r"%c=([a-z])"]  # %c=a - greyscale foreground
MUX_COLOR_XTERM256_EXTRA_GBG = [r"%c\[=([a-z])"]  # %c[=a - greyscale background

MUX_COLOR_ANSI_XTERM256_BRIGHT_BG_EXTRA_MAP = [
    (r"%ch%cR", r"%c[500"),
    (r"%ch%cG", r"%c[050"),
    (r"%ch%cY", r"%c[550"),
    (r"%ch%cB", r"%c[005"),
    (r"%ch%cM", r"%c[505"),
    (r"%ch%cC", r"%c[055"),
    (r"%ch%cW", r"%c[555"),  # white background
    (r"%ch%cX", r"%c[222"),  # dark grey background
]

######################################################################
# Settings given in secret_settings.py override those in this file.
######################################################################
try:
    from server.conf.secret_settings import *
except ImportError:
    print("secret_settings.py file not found or failed to import.")
