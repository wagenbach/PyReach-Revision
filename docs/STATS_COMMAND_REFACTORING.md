# Stats Command Refactoring Plan

## Current State

The `stats.py` file is **2121 lines** and contains:
- Main CmdStat command class
- Geist-specific stat setting (~400 lines)
- Stat removal logic (~150 lines)
- Semantic power handling (~100 lines)
- Merit validation and setting
- Power pool calculations
- Template-specific validation (legacy, athanor, etc.)
- CmdRecalc command

## Problems

1. **Single Responsibility Violation**: One file handles too many concerns
2. **Template-Specific Logic**: Geist stats should be with geist template
3. **Code Duplication**: Similar validation patterns repeated
4. **Hard to Maintain**: Finding specific logic requires scrolling through 2000+ lines
5. **Poor Separation of Concerns**: Command mixing with business logic

## Refactoring Strategy

### Phase 1: Extract Template-Specific Logic

#### 1.1 Move Geist Stats to Geist Template
**Target**: ~400 lines reduction

Move these methods to `world/cofd/templates/geist.py`:
- `set_geist_stat()` → `set_geist_stat_value(character, stat, value, caller)`
- `_set_geist_stat_value()` → Internal helper
- `_calculate_geist_derived_stats()` → `calculate_geist_derived_stats(character, caller)`

**Before** (in stats.py):
```python
def set_geist_stat(self):
    """Set a stat on a geist (Sin-Eater secondary character sheet)"""
    # 200+ lines of geist-specific logic
```

**After** (in geist.py):
```python
def set_geist_stat_value(character, stat, value, caller):
    """Set a geist stat value with validation."""
    # All geist logic here
    return success, message

def calculate_geist_derived_stats(character, caller):
    """Calculate derived stats for a geist."""
    # Calculation logic
```

**In stats.py**:
```python
def set_geist_stat(self):
    """Set a stat on a geist."""
    from world.cofd.templates.geist import set_geist_stat_value
    
    # Basic validation
    target = self.caller
    stat, value = self.parse_geist_stat(self.args)
    
    # Delegate to template
    success, message = set_geist_stat_value(target, stat, value, self.caller)
    self.caller.msg(message)
```

### Phase 2: Extract Stat Utilities

#### 2.1 Create Stat Utilities Module
**Target**: ~200 lines reduction

Create `world/cofd/stat_utilities.py`:

```python
"""
Stat management utilities for character statistics.
"""

def parse_stat_args(args):
    """Parse stat command arguments."""
    # Parsing logic
    return target_name, stat, value

def validate_stat_value(stat, value, target):
    """Validate a stat value for a character."""
    # Validation logic
    return is_valid, error_message

def check_stat_permissions(caller, target, is_removal=False):
    """Check if caller can modify target's stats."""
    # Permission checking
    return has_permission, error_message

def remove_stat(character, stat, caller):
    """Remove a stat from a character."""
    # Removal logic with validation
    return success, message
```

#### 2.2 Create Power Utilities Module
**Target**: ~150 lines reduction

Create `world/cofd/power_utilities.py`:

```python
"""
Power management utilities for supernatural abilities.
"""

def handle_semantic_power(character, power_type, power_name, value, caller):
    """Handle semantic power syntax (key=beasts, etc.)."""
    # All semantic power logic
    return success, message

def validate_power(character, power_name, template):
    """Validate if a power is valid for a character's template."""
    # Power validation
    return is_valid, error_message

def get_valid_semantic_powers(power_type):
    """Get list of valid powers for a semantic type."""
    # Return power lists
    return power_list
```

### Phase 3: Extract Merit Handling

#### 3.1 Create Merit Utilities Module
**Target**: ~100 lines reduction

Create `world/cofd/merit_utilities.py`:

```python
"""
Merit management utilities.
"""

def parse_merit_instance(stat):
    """Parse merit name and instance from stat string."""
    # Parse "unseen_sense:ghosts" → ("unseen_sense", "ghosts")
    return base_merit, instance

def validate_merit(character, merit_name, dots, template):
    """Validate merit purchase."""
    # Validation logic
    return is_valid, error_message

def set_merit(character, merit_key, dots, caller):
    """Set a merit value with validation."""
    # Merit setting logic
    return success, message
```

### Phase 4: Simplify Main Command

After extractions, the main `CmdStat` class should be ~800-1000 lines:

```python
class CmdStat(MuxCommand):
    """Set and manage character statistics."""
    
    def func(self):
        """Route to appropriate handler."""
        # Simple routing logic
        
    def set_stat(self):
        """Set a stat value."""
        # Import utilities
        from world.cofd.stat_utilities import validate_stat_value, check_stat_permissions
        from world.cofd.merit_utilities import set_merit
        from world.cofd.power_utilities import handle_semantic_power
        
        # Parse args
        target, stat, value = parse_stat_args(self.args)
        
        # Check permissions
        if not check_stat_permissions(self.caller, target):
            return
        
        # Route to appropriate handler
        if is_merit(stat):
            set_merit(target, stat, value, self.caller)
        elif is_power(stat):
            handle_semantic_power(target, ...)
        else:
            validate_and_set_stat(target, stat, value)
    
    def remove_stat(self):
        """Remove a stat."""
        from world.cofd.stat_utilities import remove_stat
        # Simple delegation
        
    def list_stats(self):
        """List character stats."""
        # Keep as is - this is display logic
```

## File Structure After Refactoring

```
PyReach/
  commands/
    stats.py                     (~800-1000 lines) ✂️ 50% reduction
    
  world/cofd/
    stat_utilities.py            (~200 lines) 🆕 NEW
    power_utilities.py           (~150 lines) 🆕 NEW
    merit_utilities.py           (~100 lines) 🆕 NEW
    
  world/cofd/templates/
    geist.py                     (+400 lines) 📦 Template-specific
```

## Benefits

1. **Single Responsibility**: Each module handles one concern
2. **Better Organization**: Related code grouped together
3. **Easier Testing**: Utility functions can be unit tested
4. **Code Reuse**: Utilities can be used by other commands
5. **Maintainability**: Find and fix issues faster
6. **Extensibility**: Easy to add new stat types

## Implementation Order

### Step 1: Extract Geist Logic (High Impact)
- Create geist stat utilities in `geist.py`
- Update `stats.py` to use them
- **Reduction: ~400 lines**

### Step 2: Extract Power Utilities (Medium Impact)
- Create `power_utilities.py`
- Move semantic power handling
- **Reduction: ~150 lines**

### Step 3: Extract Stat Utilities (Medium Impact)
- Create `stat_utilities.py`
- Move removal logic
- Move validation logic
- **Reduction: ~200 lines**

### Step 4: Extract Merit Utilities (Low Impact)
- Create `merit_utilities.py`
- Move merit-specific logic
- **Reduction: ~100 lines**

### Step 5: Clean Up and Optimize
- Review remaining code
- Extract any remaining utilities
- **Final target: ~800-1000 lines**

## Testing Strategy

After each refactoring step:
1. Run existing tests
2. Test stat setting for all templates
3. Test merit instances
4. Test geist stats
5. Test power setting
6. Test stat removal

## Migration Notes

- All existing commands continue to work
- No changes to user-facing functionality
- Only internal implementation changes
- Backwards compatible

## Example: Before vs After

### Before (stats.py - 2121 lines)
```python
class CmdStat(MuxCommand):
    # ... 200 lines of documentation ...
    
    def set_stat(self):
        # 500+ lines of setting logic
        # Merit validation inline
        # Power validation inline
        # Template validation inline
        
    def set_geist_stat(self):
        # 200+ lines of geist logic
        
    def _set_geist_stat_value(self):
        # 100+ lines more
        
    def _calculate_geist_derived_stats(self):
        # 50+ lines more
        
    def _handle_semantic_power(self):
        # 100+ lines
        
    def remove_stat_direct(self):
        # 150+ lines
        
    # ... etc ...
```

### After (stats.py - ~800 lines)
```python
class CmdStat(MuxCommand):
    # ... 200 lines of documentation ...
    
    def set_stat(self):
        # 100 lines of routing and basic logic
        # Delegates to utilities
        
    def set_geist_stat(self):
        # 20 lines - delegates to geist.py
        from world.cofd.templates.geist import set_geist_stat_value
        success, msg = set_geist_stat_value(target, stat, value, self.caller)
        self.caller.msg(msg)
        
    def remove_stat(self):
        # 20 lines - delegates to stat_utilities.py
        from world.cofd.stat_utilities import remove_stat
        success, msg = remove_stat(target, stat, self.caller)
        self.caller.msg(msg)
        
    # ... simplified methods ...
```

## Success Criteria

- ✅ stats.py under 1000 lines
- ✅ All template-specific logic in template files
- ✅ Reusable utilities extracted
- ✅ No functionality changes
- ✅ All tests pass
- ✅ Better code organization

## Timeline

- **Step 1 (Geist)**: 1-2 hours
- **Step 2 (Powers)**: 1 hour
- **Step 3 (Stats)**: 1-2 hours
- **Step 4 (Merits)**: 1 hour
- **Step 5 (Cleanup)**: 1 hour

**Total Estimated Time**: 5-7 hours
**Total Line Reduction**: ~850 lines (40% reduction)

This refactoring will make the codebase significantly more maintainable while following the same patterns we established with the template power refactoring.

