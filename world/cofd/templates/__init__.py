"""
Template Registration System for Chronicles of Darkness.
This module automatically registers all template definitions when imported.
"""

# Registry for template definitions
_template_definitions = {}

def register_template(template_dict):
    """
    Register a template definition.
    
    Args:
        template_dict (dict): Template definition dictionary
    """
    name = template_dict.get('name')
    if name:
        _template_definitions[name] = template_dict

def get_template_definition(name):
    """Get a specific template definition by name."""
    return _template_definitions.get(name.lower())

def get_all_template_definitions():
    """Get all registered template definitions."""
    return _template_definitions.copy()

# Import all template modules to auto-register them
from . import mortal
from . import vampire
from . import mage
from . import changeling
from . import werewolf
from . import geist
# from . import beast  # Beast template disabled, incomplete
from . import deviant
from . import demon
from . import hunter
from . import promethean
from . import mummy
from . import mortal_plus

# Import legacy template modules for 1st Edition support
from . import legacy_vampire
from . import legacy_mage
from . import legacy_changeling
from . import legacy_werewolf
from . import legacy_geist
from . import legacy_promethean
from . import legacy_hunter 