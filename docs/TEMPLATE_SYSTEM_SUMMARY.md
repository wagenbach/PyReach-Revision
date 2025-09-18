# Modular Template System for Chronicles of Darkness

## Overview

Complete modular template system for dynamic installation and management of character templates without code changes. Uses **Python dictionary-based** approach integrated with Django.

## Key Components Created

### 1. Database Models (`world/cofd/template_models.py`)
- **TemplateDefinition**: Stores template configurations (bio fields, integrity names, validations)
- **TemplatePackage**: Groups related templates together
- **TemplateUsage**: Tracks which characters use which templates

### 2. Template Registry (`world/cofd/template_registry.py`)
- **TemplateRegistry**: Central management system for templates
- Caching for performance
- Template validation and installation from Python dictionaries
- Export functionality generates Python module code
- Usage tracking

### 3. Template Definitions (`world/cofd/templates/`)
- **Python Modules**: Templates defined as dictionaries in Python files
- **Auto-Registration**: Templates automatically register when imported
- **Type Safety**: Python syntax checking catches errors
- **IDE Support**: Full syntax highlighting and autocomplete
- **Comments**: Can include documentation and comments

### 4. Updated Character Class (`typeclasses/characters.py`)
- Integrated with template registry instead of hardcoded rules
- Dynamic template field management
- Template-aware stat validation
- Backward compatibility maintained

### 5. Admin Commands (`commands/template_admin.py`)
- **+template/list**: Show all installed templates
- **+template/builtin**: List available built-in template definitions
- **+template/info <template>**: Detailed template information
- **+template/install builtin**: Install all built-in templates
- **+template/install module <module>**: Install from Python module
- **+template/uninstall <template>**: Remove templates
- **+template/export <template>**: Export as Python module code
- **+template/reload**: Clear cache
- **+template/create <template>**: Basic template creation
- **+template/usage**: Usage statistics

### 6. Setup System (`world/cofd/template_setup.py`)
- Automated installation of built-in templates
- Example template generation
- Django management command integration

## Template Definition Structure (Python)

Templates are now defined as Python dictionaries in modules:

```python
"""
Vampire Template Definition for Chronicles of Darkness.
"""

from . import register_template

# Valid clans (can use Python variables!)
VAMPIRE_CLANS = [
    "daeva", "gangrel", "mekhet", "nosferatu", "ventrue"
]

# Template definition
VAMPIRE_TEMPLATE = {
    "name": "vampire",
    "display_name": "Vampire",
    "description": "Vampires are undead creatures...",
    "bio_fields": ["mask", "dirge", "clan", "covenant"],
    "integrity_name": "Humanity",
    "starting_integrity": 7,
    "field_validations": {
        "clan": {
            "valid_values": VAMPIRE_CLANS
        }
    },
    "version": "1.0",
    "author": "Chronicles of Darkness"
}

# Auto-register the template
register_template(VAMPIRE_TEMPLATE)
```

## Benefits of Python Over JSON

### ✅ **Native Integration**
- No JSON parsing overhead
- Direct Python object manipulation
- Better performance and memory usage

### ✅ **Developer Experience**
- **IDE Support**: Full syntax highlighting, autocomplete, error checking
- **Comments**: Can document templates with Python comments
- **Variables**: Use Python variables for lists and constants
- **Imports**: Can import shared constants between templates

### ✅ **Type Safety**
- **Syntax Validation**: Python catches syntax errors immediately
- **Structure Validation**: Dict structure validated at import time
- **Runtime Safety**: No JSON parsing exceptions

### ✅ **Maintainability**
- **Version Control Friendly**: Better diffs and merges
- **Refactoring**: IDEs can help refactor template changes
- **Testing**: Can unit test template definitions
- **Documentation**: Docstrings and comments for complex templates

## How It Works

### Template Installation
1. Create Python module with template dictionary
2. Import module in `world/cofd/templates/__init__.py`
3. Use `+template/install builtin` command
4. Template is validated and stored in database
5. Available immediately for character assignment

### Template Management
- **Built-in Templates**: Automatically loaded from Python modules
- **Custom Templates**: Create new Python modules and import them
- **Auto-Registration**: Templates register themselves when imported
- **Database Storage**: Runtime templates stored in Django models
- **Export**: Generate Python module code from database templates

## Commands Quick Reference

```bash
# List installed templates
+template/list

# List available built-in templates
+template/builtin

# Install all built-in templates
+template/install builtin

# Get template info
+template/info vampire

# Export template as Python code
+template/export vampire

# Create basic template
+template/create my_template

# Show usage stats
+template/usage

# Reload cache
+template/reload

# Uninstall template
+template/uninstall custom_template

# Install from Python module
+template/install module my_custom_module
```

## Creating Custom Templates

### Method 1: Copy and Modify
1. Copy existing template file:
   ```bash
   cp world/cofd/templates/vampire.py world/cofd/templates/my_template.py
   ```

2. Edit the template dictionary in the new file

3. Import in `world/cofd/templates/__init__.py`:
   ```python
   from . import my_template
   ```

4. Install: `+template/install builtin`

### Method 2: Export and Modify
1. Export existing template: `+template/export vampire`
2. Save the generated code to a new `.py` file
3. Modify as needed
4. Import and install

### Method 3: Interactive Creation
1. Create basic template: `+template/create my_template`
2. Export to get Python code: `+template/export my_template`
3. Save and enhance the generated code

## Migration from JSON System

**If you were using the previous JSON-based system:**

1. **Automatic Migration**: The system automatically loads from Python modules
2. **No Data Loss**: Existing database templates remain intact
3. **Export Tool**: Use `+template/export` to convert database templates to Python
4. **Gradual Migration**: Can gradually move to Python-based definitions

## File Structure

```
exordium/
├── world/
│   ├── cofd/
│   │   ├── template_models.py      # Database models
│   │   ├── template_registry.py    # Registry system
│   │   ├── template_setup.py       # Setup utilities
│   │   └── templates/              # Template definitions
│   │       ├── __init__.py         # Registration system
│   │       ├── mortal.py           # Mortal template
│   │       ├── vampire.py          # Vampire template
│   │       ├── mage.py             # Mage template
│   │       ├── changeling.py       # Changeling template
│   │       ├── example_custom.py   # Example template
│   │       └── README.md           # Documentation
├── commands/
│   └── template_admin.py           # Admin commands
├── typeclasses/
│   └── characters.py               # Updated character class
└── TEMPLATE_SYSTEM_SUMMARY.md     # This document
```

## Security Features

- **Permission Checks**: Only Builder+ can manage templates
- **Validation**: All template data validated before installation
- **Safe Deletion**: Templates in use cannot be deleted
- **System Protection**: Core templates cannot be uninstalled
- **Python Safety**: No eval() or exec() - only imports and dict access

## Performance Improvements

- **No JSON Parsing**: Direct Python object access
- **Import Caching**: Python module caching system
- **Template Caching**: Registry caches active templates
- **Lazy Loading**: Templates loaded only when needed

## Future Enhancements

The Python-based system enables advanced features:

- **Template Inheritance**: Python classes for template hierarchies
- **Computed Fields**: Use Python functions for dynamic values
- **Shared Constants**: Import common data across templates
- **Validation Functions**: Custom Python validation logic
- **Template Mixins**: Composable template components

## Example Template Files

### Simple Template (`mortal.py`)
```python
from . import register_template

MORTAL_TEMPLATE = {
    "name": "mortal",
    "display_name": "Mortal",
    "bio_fields": ["virtue", "vice"],
    "integrity_name": "Integrity",
    "starting_integrity": 7
}

register_template(MORTAL_TEMPLATE)
```

### Complex Template with Variables (`vampire.py`)
```python
from . import register_template

# Reusable constants
VAMPIRE_CLANS = ["daeva", "gangrel", "mekhet", "nosferatu", "ventrue"]
VAMPIRE_COVENANTS = ["carthian movement", "circle of the crone", "invictus"]

VAMPIRE_TEMPLATE = {
    "name": "vampire",
    "display_name": "Vampire",
    "bio_fields": ["mask", "dirge", "clan", "covenant"],
    "integrity_name": "Humanity",
    "field_validations": {
        "clan": {"valid_values": VAMPIRE_CLANS},
        "covenant": {"valid_values": VAMPIRE_COVENANTS}
    }
}

register_template(VAMPIRE_TEMPLATE)
```
