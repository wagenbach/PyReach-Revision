# Werewolf Shapeshifting System

## Quick Overview

The shapeshifting system allows Werewolf characters to transform between their five distinct forms, applying temporary stat modifiers and enforcing game balance restrictions.

## Commands

- **+shift <form>** - Transform into a specific form
- **+shift/list** - View all available forms
- **+shift/info <form>** - Detailed form information
- **+form** - Check your current form

## The Five Forms

1. **Hishu** (Human) - Base form, no modifiers
2. **Dalu** (Near-Man) - Str +1, Sta +1, Man -1, Size +1
3. **Gauru** (War Form) - Str +3, Dex +1, Sta +2, Size +2 [LIMITED DURATION]
4. **Urshul** (Near-Wolf) - Str +2, Dex +2, Sta +2, Man -1, Size +1
5. **Urhan** (Wolf) - Dex +2, Sta +1, Man -1, Size -1

## Key Features

### Stat Tracking
- Stores base attributes when first shifting from Hishu
- Applies temporary modifiers based on current form
- Restores base values when returning to Hishu
- Auto-recalculates derived stats (Health, Speed, Defense, Initiative)

### Restrictions
- **Can only spend XP or use +stat in Hishu form**
- Prevents accidental permanent stat changes while shifted
- Staff can override but get informed warnings

### Integration
- Works with existing character stat system
- Integrates with +xp/spend and +xp/buy commands
- Respects existing permission checks (approved status, staff access)

## Implementation Details

**File:** `PyReach/commands/shapeshifting.py`

**Classes:**
- `CmdShift` - Main shapeshifting command
- `CmdForm` - Quick form reference
- `can_modify_stats_while_shifted()` - Helper function for other commands

**Data Storage:**
- `character.db.current_form` - Current form name (defaults to "hishu")
- `character.db.base_attributes` - Stored permanent attribute values
- `character.db.base_size` - Stored permanent size value

**Integration Points:**
- `commands/stats.py` - Prevents +stat use while shifted
- `commands/experience.py` - Prevents +xp/spend and +xp/buy while shifted
- `commands/default_cmdsets.py` - Registers commands

## Documentation

For complete details, see:
- **[SHAPESHIFTING_GUIDE.md](SHAPESHIFTING_GUIDE.md)** - Comprehensive guide with lore, tactics, and mechanics
- **[COMMANDS.md](../docs/COMMANDS.md)** - Command reference with examples

## Source Material

Based on **Werewolf: The Forsaken 2nd Edition** from Chronicles of Darkness.

## Testing

To verify the system works correctly:

1. Create or log in as a Werewolf character
2. Check current form: `+form`
3. List available forms: `+shift/list`
4. Transform: `+shift dalu`
5. Check stats updated: `+sheet`
6. Try to use +stat (should be blocked)
7. Return to human form: `+shift hishu`
8. Verify stats restored: `+sheet`

## Future Enhancements

Potential additions:
- Essence cost for shifting (Harmony-based)
- Gauru duration tracking with automatic countdown
- Lunacy system for witnesses
- Equipment handling (destruction/preservation)
- First Tongue communication in wolf forms
- Death Rage (Kuruth) mechanics

## Troubleshooting

**Problem:** Can't use +stat or +xp
**Solution:** Use `+form` to check current form, then `+shift hishu` to return to human form

**Problem:** Stats seem incorrect after shifting
**Solution:** Shift to Hishu (`+shift hishu`) and use `+recalc` to recalculate derived stats

**Problem:** Error when shifting
**Solution:** Make sure you're a Werewolf template character. Use `+sheet` to verify.

## Contact

For issues or feature requests related to shapeshifting, contact development staff or create a +jobs ticket.

