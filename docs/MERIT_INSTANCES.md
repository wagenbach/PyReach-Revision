# Merit Instances System

## Overview

The merit instances system allows characters to take the same merit multiple times with different specifications or instances. This is useful for merits like "Unseen Sense" where a character might want to sense different types of supernatural beings, or "Contacts" where they have contacts in different fields.

## Usage

### Setting Merit Instances

Use the colon (`:`) notation to specify an instance when setting a merit:

```
+stat <merit_name>:<instance>=<dots>
```

**Examples:**
```
+stat unseen_sense:ghosts=2
+stat unseen_sense:spirits=2
+stat unseen_sense:faeries=2
+stat contacts:police=3
+stat contacts:occult_scholars=2
+stat allies:vampire_prince=4
```

### For Other Characters (Staff Only)

Staff can set merit instances for other characters:

```
+stat <character>/<merit_name>:<instance>=<dots>
```

**Example:**
```
+stat John/unseen_sense:ghosts=2
```

## Removing Merit Instances

### Universal Removal Syntax

You can now remove ANY stat by using the equals sign with no value:

```
+stat <stat>=
+stat <merit_name>:<instance>=
```

**Examples:**
```
+stat unseen_sense:ghosts=
+stat resources=
+stat strength=
+stat specialty/athletics=
```

### For Other Characters (Staff Only)

```
+stat <character>/<merit_name>:<instance>=
```

**Example:**
```
+stat John/unseen_sense:ghosts=
```

### Legacy Removal Method

The old `/remove` switch still works:

```
+stat/remove <stat>
+stat/remove <merit_name>:<instance>
```

## How It Works

### Storage

Merit instances are stored with the full key including the instance name:

```python
# In the database:
merits = {
    "unseen_sense:ghosts": {
        "dots": 2,
        "max_dots": 5,
        "merit_type": "supernatural",
        "description": "...",
        "base_merit": "unseen_sense",
        "instance": "ghosts"
    },
    "unseen_sense:spirits": {
        "dots": 2,
        "max_dots": 5,
        "merit_type": "supernatural",
        "description": "...",
        "base_merit": "unseen_sense",
        "instance": "spirits"
    }
}
```

### Display

Merit instances are displayed with parentheses in both `+stat/list` and `+sheet`:

```
Merits:
  Supernatural: Unseen Sense (Ghosts) (2/5 dots), Unseen Sense (Spirits) (2/5 dots)
  Social: Contacts (Police) (3/5 dots), Contacts (Occult Scholars) (2/5 dots)
```

### Experience Costs

Each instance of a merit costs the full merit value:
- Unseen Sense (Ghosts) at 2 dots = 4 XP
- Unseen Sense (Spirits) at 2 dots = 4 XP  
- Unseen Sense (Faeries) at 2 dots = 4 XP
- **Total**: 12 XP for three separate 2-dot instances

This is by design - each instance is treated as a separate purchase of the same merit.

## Approved Characters

For approved characters:
- Merit instances can only be purchased through the XP system: `+xp/buy unseen_sense:ghosts=2`
- Direct setting with `+stat` is blocked (except for staff)
- Removal requires XP refund: `+xp/refund unseen_sense:ghosts` (staff only)

## Unapproved Characters

During character generation:
- Merit instances can be set freely with `+stat`
- No XP cost during character creation
- Can be removed freely with `+stat <merit>:instance=` or `+stat/remove <merit>:instance`

## Which Merits Support Instances?

Technically, any merit can be taken with instances using this syntax. However, it's most appropriate for merits where multiple instances make narrative sense:

**Good Candidates:**
- **Unseen Sense**: Different types of supernatural beings (ghosts, spirits, vampires, etc.)
- **Contacts**: Different fields or organizations
- **Allies**: Different individuals or groups
- **Alternate Identity**: Multiple identities
- **Safe Place**: Multiple safe locations
- **Striking Looks**: Different contexts or personas
- **Language**: Different languages (though this could also use the language system)

**Poor Candidates:**
- **Resources**: Wealth is fungible, doesn't make sense to have multiple instances
- **Fast Reflexes**: Physical traits don't have instances
- **Iron Stamina**: Same as above
- **Fighting Style**: Each style is its own merit

## Technical Details

### Code Changes

The merit instance system required changes to:

1. **stats.py**:
   - Updated `parse_target_stat()` to detect empty values as removal requests
   - Updated `set_stat()` to handle colon notation for instances
   - Added `remove_stat_direct()` to handle universal stat removal
   - Updated merit display in `list_stats()` to show instances properly

2. **CmdSheet.py**:
   - Updated merit display to format instances with parentheses
   - Adjusted column widths to accommodate longer merit names with instances

3. **characters.py**:
   - No changes needed - storage is compatible with existing structure

### Backwards Compatibility

The system is fully backwards compatible:
- Existing merits without instances continue to work
- Old data is not affected
- The `/remove` switch still works alongside the new `=` syntax
- Regular merit syntax still works: `+stat resources=3`

## Examples Session

```
> +stat unseen_sense:ghosts=2
Set YourCharacter's Unseen Sense (Ghosts) merit to 2 dots.
(Merit set during character generation - after approval, use +xp/buy to purchase merits)

> +stat unseen_sense:spirits=2
Set YourCharacter's Unseen Sense (Spirits) merit to 2 dots.
(Merit set during character generation - after approval, use +xp/buy to purchase merits)

> +stat contacts:police=3
Set YourCharacter's Contacts (Police) merit to 3 dots.
(Merit set during character generation - after approval, use +xp/buy to purchase merits)

> +sheet
================================================================================
                              YourCharacter
                             NOT APPROVED
================================================================================
<-------------------------- BIO -------------------------->
Full Name     : John Doe             Template      : Mortal
...

<------------ MERITS ------------->  <--------- ADVANTAGES ----------->
Contacts (Police)        ●●●○○       Defense         : 3
Unseen Sense (Ghosts)    ●●○○○       Speed           : 11
Unseen Sense (Spirits)   ●●○○○       Initiative      : 5
...

> +stat unseen_sense:ghosts=
Removed Unseen Sense (Ghosts) from YourCharacter.

> +stat contacts:police=
Removed Contacts (Police) from YourCharacter.
```

## Future Enhancements

Potential future improvements:
- XP system integration for purchasing instanced merits
- Merit templates that define which merits should commonly use instances
- Auto-suggestions when setting certain merits to consider using instances
- Grouped display of related instances on the character sheet

