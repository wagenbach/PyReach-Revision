# Legacy Mode - Chronicles/World of Darkness 1st Edition

## Overview

Legacy Mode transforms the MUSH to operate using Chronicles/World of Darkness 1st Edition mechanics instead of the default 2nd Edition framework. This is a global setting that affects all characters and systems.

## Activation

Only administrators can toggle Legacy Mode:

```
+legacy on    - Enable Legacy Mode
+legacy off   - Disable Legacy Mode
+legacy       - Show current status
```

When Legacy Mode is activated, all connected players receive a system announcement.

## Changes in Legacy Mode

### 1. Virtue and Vice System

- **Replaces**: Modern anchor system (aspirations, threads, etc.)
- **Uses**: Only the seven traditional virtues and seven deadly sins
- **Commands**: `+virtue` and `+vice` commands become available

#### Available Virtues:
- **Charity**: Generosity and altruism
- **Faith**: Belief and conviction
- **Fortitude**: Courage and integrity
- **Hope**: Optimism and refusal to despair
- **Justice**: Protecting innocents and punishing wrongs
- **Prudence**: Wisdom and restraint
- **Temperance**: Moderation and balance

#### Available Vices:
- **Envy**: Covetousness and jealousy
- **Gluttony**: Indulgence in excesses
- **Greed**: Insatiable desire for more
- **Lust**: Uncontrolled desire (not necessarily sexual)
- **Pride**: Arrogance and ego
- **Sloth**: Laziness and apathy
- **Wrath**: Uncontrolled anger

### 2. Experience System

- **Replaces**: Beats system with direct experience points
- **Higher Costs**: More expensive advancement reflecting 1st edition
- **Direct Awards**: Experience given directly, no beat conversion

#### Legacy Experience Costs:
```
Attributes: 4/8/12/16 XP (current level × 4)
Skills: 2/4/6/8/10 XP (new level × 2)
Specialties: 2 XP each
Merits: 2 XP per dot
Integrity: 3 XP per dot
Powers: 6-8 XP per dot (template dependent)
```

#### Experience Sources:
- Automatic weekly: 1 XP
- Exceptional roleplay: 1 XP
- Story completion: 2 XP
- Character growth: 1 XP
- Heroic actions: 2 XP
- Staff discretionary: 3 XP

### 3. Disabled Systems

The following modern systems are disabled in Legacy Mode:

#### Aspirations System
- `+aspiration` commands disabled
- No aspiration tracking on character sheets
- Virtue/Vice provide character motivation instead

#### Beats System
- `+xp/beat` commands disabled
- No beat tracking or conversion
- Experience awarded directly

#### Conditions System
- `+condition` commands disabled
- No condition tracking or effects
- Traditional status effects used instead

#### Tilts System
- `+tilt` commands disabled
- No combat tilt mechanics
- Traditional combat modifiers used instead

#### Social Combat
- `+social` commands disabled
- No doors/impression mechanics
- Traditional social interaction used instead

### 4. Character Sheet Changes

Legacy Mode character sheets display:

- **Header**: Shows "LEGACY MODE (WoD 1st Edition)" indicator
- **Bio Section**: Enhanced virtue/vice display with full descriptions
- **Experience Section**: Shows experience points instead of beats
- **No Aspirations**: Aspirations section hidden
- **Virtue/Vice Details**: Full willpower regain conditions shown

## Commands Available in Legacy Mode

### Core Commands
- `+legacy` - Toggle/view legacy mode (admin only)
- `+stat` - Set character stats (includes virtue/vice validation in legacy mode)
- `+xp` - Experience management (modified for legacy)
- `+sheet` - Character sheet (legacy format)

### Setting Virtue and Vice
In legacy mode, virtue and vice are set using the standard `+stat` command with validation:

```
+stat virtue=<virtue_name>  - Set virtue (validated against legacy list)
+stat vice=<vice_name>      - Set vice (validated against legacy list)
```

Valid virtues: Charity, Faith, Fortitude, Hope, Justice, Prudence, Temperance
Valid vices: Envy, Gluttony, Greed, Lust, Pride, Sloth, Wrath

### Template Selection
In legacy mode, only legacy templates are available:

```
+stat template=<legacy_template>  - Set character template (staff only)
```

Available legacy templates:
- Legacy Vampire
- Legacy Werewolf  
- Legacy Mage
- Legacy Changeling
- Legacy Geist
- Legacy Promethean
- Legacy Hunter
- Mortal

### Experience Commands (Modified)
```
+xp                        - Show experience points
+xp/spend <stat>=<level>   - Spend experience
+xp/buy <merit>=<dots>     - Buy merits
+xp/costs                  - Show legacy costs
```

## Migration

When Legacy Mode is first enabled:

1. **Experience Conversion**: Existing beats converted to experience (3:1 ratio)
2. **Virtue/Vice**: Existing virtue/vice values preserved
3. **Aspirations**: Hidden but preserved (can be restored if legacy mode disabled)
4. **Conditions/Tilts**: Existing conditions/tilts remain but cannot be modified

## Implementation Notes

### For Staff

- Legacy mode is stored in server configuration for persistence
- All connected players notified when mode changes
- Existing character data is preserved, not deleted
- Mode can be toggled back and forth safely

### For Players

- Character sheets automatically adapt to show legacy format
- Commands gracefully inform users when disabled
- Virtue/vice commands only work in legacy mode
- Experience costs are higher, plan advancement carefully

### For Storytellers

- Traditional World of Darkness mechanics apply
- No conditions/tilts to track in combat
- Social interactions use traditional roleplay
- Experience awards should be more conservative

## Compatibility

Legacy Mode is designed to be:

- **Reversible**: Can be disabled to return to 2nd Edition
- **Safe**: No data loss when toggling modes
- **Complete**: All major systems adapted
- **Consistent**: Unified 1st Edition experience

## Troubleshooting

### Common Issues

**Q: I can't use +aspiration anymore**
A: Aspirations are disabled in Legacy Mode. Use +virtue and +vice instead.

**Q: My beats disappeared**
A: Beats are converted to experience points in Legacy Mode. Check +xp.

**Q: Why are experience costs so high?**
A: Legacy Mode uses 1st Edition costs, which are higher than 2nd Edition.

**Q: Commands say they're disabled**
A: Many 2nd Edition systems are disabled in Legacy Mode by design.

### Getting Help

- Use `+legacy` to check current mode status
- Use `+virtue/list` and `+vice/list` to see options
- Use `+xp/costs` to see experience costs
- Contact staff for mode-related issues

## Technical Details

### Files Modified
- `commands/CmdLegacy.py` - Main legacy mode command
- `commands/CmdSheet.py` - Sheet display modifications
- `commands/aspirations.py` - Disabled in legacy mode
- `commands/experience.py` - Legacy experience handling
- `commands/conditions.py` - Disabled in legacy mode
- `commands/tilts.py` - Disabled in legacy mode
- `commands/social.py` - Disabled in legacy mode

### Files Added
- `world/legacy_virtues_vices.py` - Virtue/vice definitions
- `world/legacy_experience.py` - Legacy experience system
- `world/cofd/templates/legacy_*.py` - Legacy template definitions

### Configuration
- Legacy mode status stored in `ServerConfig`
- Accessible via `is_legacy_mode()` utility function
- Persistent across server restarts
