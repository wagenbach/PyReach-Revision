# Character Stat Access Pattern Standardization

**Date:** October 2, 2025  
**Status:**  COMPLETED

## Overview

This document explains stat standardization to ensure all character stat access in the commands folder uses the safe `.get()` pattern for reading values.

## Standardized Pattern

### Correctly Reading Stats (Use `.get()` with defaults)
```python
# Pattern 1: Two-step safe access
attributes = character.db.stats.get("attributes", {})
strength = attributes.get("strength", 1)

# Pattern 2: Chained safe access
strength = character.db.stats.get("attributes", {}).get("strength", 1)

# Pattern 3: Variable extraction with defaults
stats = character.db.stats
attributes = stats.get("attributes", {})
skills = stats.get("skills", {})
```

### Correctly Setting Stats (Direct access is fine)
```python
# Setting values can use direct access (after validation)
target.db.stats["attributes"]["strength"] = 3
target.db.stats["skills"]["athletics"] = 2
target.db.stats["advantages"]["health"] = 7
```

### Avoid Direct Reading Without Safety
```python
# Don't use direct access when reading - can cause KeyError
strength = character.db.stats["attributes"]["strength"]  # BAD - no safety
```

## Changes Made

### 1. dice_commands.py
**Status:**  Updated  
**Lines Changed:** 244-264  
**Changes:**
- Updated `get_stat_value()` method to use `.get()` pattern
- Changed from `stats["attributes"][stat_name]` to `attributes.get(stat_name)`
- Applied to attributes, skills, and advantages

**Before:**
```python
if stat_name in self.caller.db.stats.get("attributes", {}):
    return self.caller.db.stats["attributes"][stat_name]
```

**After:**
```python
attributes = self.caller.db.stats.get("attributes", {})
if stat_name in attributes:
    return attributes.get(stat_name)
```

### 2. mystery_commands.py
**Status:**  Updated  
**Lines Changed:** 1145-1193  
**Changes:**
- Updated `_get_attribute_value()` to use `.get()` with defaults
- Updated `_get_skill_value()` to use `.get()` with defaults
- Fixed legacy attribute access patterns
- Added appropriate default values (1 for attributes, 0 for skills)

**Before:**
```python
if attributes and attribute in attributes:
    return attributes[attribute]
```

**After:**
```python
if attributes and attribute in attributes:
    return attributes.get(attribute, 1)
```

### 3. Already Standardized Files
The following files were already using the correct `.get()` pattern:
-  **combat.py** - All 17 stat accesses already use `.get()` with defaults
-  **CmdHealth.py** - Reading uses `.get()`, setting uses direct access
-  **experience.py** - All stat accesses already use `.get()` pattern
-  **stats.py** - Reading uses `.get()`, setting uses direct access (53 accesses)
-  **CmdSheet.py** - All stat accesses already properly structured
-  **base.py** - HealthMixin uses `.get()` pattern correctly

### 4. Subdirectory Files
All files in subdirectories verified:
-  **diesiraecode/** - All files use correct patterns
-  **bbs/** - All files use correct patterns
-  **jobs/** - All files use correct patterns

## Default Values by Category

When using `.get()`, these are the recommended defaults:

| Category | Default Value | Reason |
|----------|---------------|---------|
| attributes | `1` | Starting attribute value in CoD |
| skills | `0` | Starting skill value (untrained) |
| advantages | varies | `7` for health, `2` for willpower, etc. |
| merits | `0` or check if exists | Merits are optional |
| specialties | `[]` | Empty list if none exist |
