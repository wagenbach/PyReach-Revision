# Migration Notes - Modular Template System (Python-Based)

## Database Setup

Since new models were added, you'll need to create and run Django migrations:

```bash
# Create migrations for the new template models
python manage.py makemigrations

# Apply migrations to create the database tables
python manage.py migrate
```

## Initial Template Setup

After the database migration, install the built-in templates:

```python
# Option 1: Using Django shell
python manage.py shell
>>> from world.cofd.template_setup import setup_template_system
>>> setup_template_system()

# Option 2: Using the management command
python manage.py setup_templates

# Option 3: Using in-game command (after server is running)
+template/install builtin
```

## Character Migration

Existing characters with legacy stats can be migrated using the existing `+migrate` command:

```
# In-game command to migrate your own character
+migrate

# Staff command to migrate another character
+migrate <character_name>

# Note: There's also a mass migration function in the code for all characters
```

## Verification

After setup, verify the system is working:

```
# List available built-in templates
+template/builtin

# List installed templates
+template/list

# Check a specific template
+template/info vampire

# Test creating a new template
+template/create test_template
```

## File Structure Created

```
exordium/
├── world/
│   ├── cofd/
│   │   ├── template_models.py      # Database models
│   │   ├── template_registry.py    # Registry system
│   │   ├── template_setup.py       # Setup utilities
│   │   └── templates/              # Template Python modules
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
└── TEMPLATE_SYSTEM_SUMMARY.md     # Documentation
```

## Python Template System Benefits

### ✅ **No External Files**
- All templates are Python modules within the codebase
- No JSON files to manage or parse
- Better integration with Django and Evennia

### ✅ **Developer-Friendly**
- Full IDE support with syntax highlighting
- Error checking at import time
- Can use Python variables and constants
- Comments and documentation support

### ✅ **Performance**
- No JSON parsing overhead
- Python import caching
- Direct object access

## Creating Custom Templates

### Method 1: Copy Existing Template
```bash
# Copy an existing template file
cp world/cofd/templates/vampire.py world/cofd/templates/my_template.py

# Edit the new file with your template definition
# Add import to world/cofd/templates/__init__.py:
# from . import my_template

# Install the updated templates
+template/install builtin
```

### Method 2: Export and Modify
```bash
# Export existing template as Python code
+template/export vampire

# Copy the output to a new .py file
# Modify as needed
# Import and install
```

### Method 3: Interactive Creation
```bash
# Create basic template
+template/create my_custom_template

# Export to get Python code
+template/export my_custom_template

# Save the code and enhance as needed
```

## Troubleshooting

### Database Issues
- Make sure `makemigrations` and `migrate` complete successfully
- Check for any foreign key constraint errors
- Verify all models are properly imported

### Template Loading Issues
- Check Python syntax in template files
- Verify templates are imported in `__init__.py`
- Use `+template/reload` to clear cache
- Check Django logs for import errors

### Command Issues
- Verify commands are added to default_cmdsets.py
- Check import statements are correct
- Restart server if commands don't appear

### Character Integration Issues
- Run character migration commands
- Check that template registry is properly imported
- Verify backward compatibility with existing characters

### Python Import Issues
- Ensure all template modules have valid Python syntax
- Check that `register_template()` is called in each module
- Verify imports in `world/cofd/templates/__init__.py`

## Template Development Workflow

1. **Development**:
   - Create Python module in `world/cofd/templates/`
   - Define template dictionary
   - Add `register_template()` call

2. **Testing**:
   - Import module in `__init__.py`
   - Use `+template/builtin` to see available templates
   - Install with `+template/install builtin`

3. **Deployment**:
   - Templates are part of codebase
   - Deploy like any other Python code
   - Run migration commands on production

## Backup Recommendations

Before applying this system to production:

1. **Backup Database**: Full database backup before migrations
2. **Export Characters**: Use existing export systems if available
3. **Test Migration**: Run migration on copy of production data first
4. **Code Backup**: Templates are now part of source code

## Rollback Plan

If issues occur:

1. **Database Rollback**: Restore from pre-migration backup
2. **Code Rollback**: Revert to previous character class version
3. **Template Export**: Use `+template/export` to preserve custom templates

## Performance Notes

- Template registry uses caching for performance
- Python import caching provides additional performance
- No JSON parsing overhead
- Direct Python object access is faster

## Advantages Over JSON System

### ✅ **Maintainability**
- Templates are part of source code
- Version control treats them like any Python file
- Better diffs and merge conflict resolution
- IDE refactoring support

### ✅ **Safety**
- Python syntax checking catches errors early
- No JSON parsing exceptions
- Import-time validation
- Type safety through Python

### ✅ **Features**
- Can use Python variables for shared constants
- Comments and documentation
- Ability to compute values dynamically
- Import shared utilities between templates

## Support

If you encounter issues:

1. Check the TEMPLATE_SYSTEM_SUMMARY.md for detailed documentation
2. Review existing template Python files for examples
3. Use `+template/builtin` to see available templates
4. Use `+template/export` to see template structure
5. Check Django logs for Python import errors
6. Use `+migrate` to fix character stat issues 