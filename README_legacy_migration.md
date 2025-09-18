# Legacy Stats Migration System

## Overview

Automatically detects and migrates legacy character stats from individual attribute storage to organized stats dictionary format, then cleans up old data.

## What Gets Migrated

The migration system looks for individual attributes stored directly on character objects (like `character.db.strength`) and moves them to the new organized dictionary structure (`character.db.stats["attributes"]["strength"]`).

### Legacy Data Detected:

- **Attributes**: strength, dexterity, stamina, presence, manipulation, composure, intelligence, wits, resolve
- **Skills**: All Chronicles of Darkness skills (athletics, brawl, investigation, etc.)
- **Advantages**: health, willpower, speed, defense, initiative, power stats (gnosis, blood_potency, etc.)
- **Bio Fields**: fullname/full_name, birthdate, concept, virtue, vice, template-specific fields
- **Other Stats**: integrity, size, beats, experience, template
- **Legacy Storage**: Old dictionaries like anchors, stats_dict, character_stats, etc.

### Database Cleanup

After migration, the system removes the old individual attributes to prevent:
- Database bloat from duplicate data
- Confusion between old and new storage methods
- Potential conflicts during stat operations

## How It Works

### Automatic Migration

The migration runs automatically and silently when characters:
- Use `+stat` commands to set or view stats
- Use `+sheet` to view their character sheet
- Access any stat-related functionality

### Manual Migration

Staff can trigger migration manually using:

```
+stat/migrate [character]     # Migrate specific character
+stat/massimigrate           # Migrate all characters in database
```

### Migration Process

1. **Detection**: Scans character object for legacy attributes
2. **Categorization**: Sorts legacy data into appropriate categories:
   - `stats["attributes"]` - Character attributes
   - `stats["skills"]` - Character skills  
   - `stats["advantages"]` - Derived stats and power stats
   - `stats["bio"]` - Biography and character info
   - `stats["anchors"]` - Virtue/vice anchors
   - `stats["other"]` - Miscellaneous stats
3. **Migration**: Copies data to new structure
4. **Cleanup**: Removes old individual attributes
5. **Reporting**: (Manual only) Reports what was migrated

## New Stats Structure

```python
character.db.stats = {
    "attributes": {
        "strength": 3,
        "dexterity": 4,
        # ... other attributes
    },
    "skills": {
        "athletics": 2,
        "brawl": 3,
        # ... other skills
    },
    "advantages": {
        "health": 8,
        "willpower": 6,
        "gnosis": 3,  # Power stats stored here
        # ... other advantages
    },
    "bio": {
        "full_name": "John Smith",
        "concept": "Detective",
        "virtue": "Justice",
        "clan": "Gangrel",  # template-specific
        # ... other bio fields
    },
    "anchors": {
        "virtue": "Justice",  # Backward compatibility
        "vice": "Wrath"
    },
    "other": {
        "template": "Vampire",
        "integrity": 7,
        "size": 5,
        "beats": 3,
        "experience": 15
    }
}
```

## Benefits

1. **Organized Data**: Stats are logically grouped by category
2. **No Duplication**: Eliminates duplicate storage of the same data
3. **Database Efficiency**: Reduces database size and complexity
4. **Future-Proof**: Easier to extend and maintain
5. **Automatic**: Happens transparently without user intervention

## Staff Usage

### Check Migration Status
```
+stat/list [character]    # View organized stats (triggers migration)
```

### Manual Migration
```
+stat/migrate             # Migrate your own character
+stat/migrate PlayerName  # Migrate specific character
+stat/massimigrate        # Migrate ALL characters (use carefully!)
```

### Monitor Results
The mass migration command provides detailed reporting:
- Total characters processed
- Number of characters migrated
- Number of characters with no legacy data
- Any errors encountered

## Safety Features

- **Non-Destructive**: Only migrates data that exists
- **Preserves Values**: All stat values are maintained exactly
- **Error Handling**: Gracefully handles missing or invalid data
- **Silent Operation**: Automatic migration doesn't spam users
- **Staff-Only Mass Operations**: Bulk migration requires Builder+ permissions

## Troubleshooting

### If migration fails:
1. Check if character has the `stats` attribute initialized
2. Verify character is a valid Character typeclass
3. Use `+stat/migrate CharacterName` to manually retry
4. Check server logs for detailed error messages

### If stats appear missing:
1. Use `+stat/list` to trigger migration and view current stats
2. Check if data was moved to a different category
3. Verify the character had stats set in the first place

The migration system is designed to be safe, automatic, and transparent to players while cleaning up legacy database storage efficiently. 