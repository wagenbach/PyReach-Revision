# Chronicles of Darkness Tilt System

## Overview

The Tilt system provides a unified way of applying temporary circumstances to both characters and scenes during violent encounters. Tilts are mechanically similar to Conditions but are specifically designed for combat situations.

## Key Features

### Tilt Types
- **Personal Tilts**: Affect individual characters
- **Environmental Tilts**: Affect entire combat scenes

### Core Differences from Conditions
- Tilts only apply during combat
- Tilts do not give Beats when they end
- Tilts can convert to Conditions when combat ends
- Tilts have turn-based duration tracking

## System Components

### Core Classes

#### `Tilt`
- Represents a single tilt instance
- Properties: name, description, type, duration, effects, resolution method
- Supports turn-based advancement and expiration
- Can convert to equivalent Condition outside combat

#### `TiltHandler`
- Manages personal tilts on characters
- Handles tilt persistence and storage
- Automatically converts tilts to conditions when leaving combat
- Provides tilt querying and manipulation methods

#### `EnvironmentalTiltHandler`
- Manages environmental tilts on locations
- Tracks scene-wide effects during combat
- Automatically cleared when combat ends

### Combat Integration

The tilt system is fully integrated with the combat system:

#### Automatic Turn Advancement
- Personal and environmental tilts advance each combat round
- Expired tilts are automatically removed
- Messages announce when tilts expire

#### Combat Status Display
- Personal tilts shown in character status
- Environmental tilts displayed separately
- Duration information included

#### Tilt-to-Condition Conversion
- When combat ends, tilts convert to equivalent conditions
- Only tilts with `condition_equivalent` property convert
- Conversion provides appropriate narrative messaging

## Available Tilts

### Personal Tilts

#### Physical Impairments
- **Arm Wrack**: Damaged arm, cannot use effectively (-2 arm penalty)
- **Leg Wrack**: Damaged leg, limited mobility (-50% speed, -2 Athletics)
- **Beaten Down**: On ground and stunned (prone, -2 Defense)
- **Knocked Down**: Simply prone (can stand with instant action)
- **Immobilized**: Cannot move (0 movement, -2 Defense)

#### Sensory Impairments
- **Blinded**: Cannot see (-3 vision penalty)
- **Deafened**: Cannot hear (-3 hearing penalty)

#### Mental/Physical States
- **Stunned**: Dazed, cannot act (1 turn duration)
- **Drugged**: Under influence (-2 mental, -1 physical)
- **Poisoned**: Toxins in system (-2 Stamina, 1 damage/turn, 5 turns)
- **Sick**: General illness (-1 all actions)
- **Insane**: Reality compromised (-3 mental, -2 social)

#### Situational
- **Flooded**: In flooding area (-2 movement)

### Environmental Tilts

#### Weather Effects
- **Blizzard**: Heavy snow/wind (-3 visibility, -1 movement)
- **Heavy Rain**: Torrential rain (-1 visibility, -1 Athletics)
- **Heavy Winds**: Strong winds (-2 ranged attacks, -1 movement)
- **Extreme Cold**: Freezing temperatures (-1 Dex/Stamina)
- **Extreme Heat**: Oppressive heat (-2 Stamina, fatigue risk)

#### Visibility
- **Darkness**: Limited light (-2 visibility)
- **Smoke**: Thick smoke (-2 visibility, -1 Stamina)

#### Terrain
- **Ice**: Slippery surface (-2 Athletics, fall risk)
- **Earthquake**: Shaking ground (-2 Dexterity, knockdown risk, 3 turns)

#### Hazards
- **Fire**: Area on fire (damage risk, movement restriction)
- **Flooding**: Rising water (-2 movement, drowning risk)

## Command Interface

### Basic Commands (`+tilt`)

#### Personal Tilt Management
```
+tilt/add = <tilt_name>          # Add tilt to yourself
+tilt/add <target> = <tilt_name> # Add tilt to target (staff only)
+tilt/remove = <tilt_name>       # Remove tilt from yourself
+tilt/list [target]              # List tilts on target
```

#### Environmental Tilts (Staff Only)
```
+tilt/env/add <tilt_name>        # Add environmental tilt
+tilt/env/remove <tilt_name>     # Remove environmental tilt
+tilt/env/list                   # List environmental tilts
+tilt/env/clear                  # Clear all environmental tilts
```

#### Utility Commands
```
+tilt/help [tilt_name]           # Get tilt information
+tilt/advance                    # Advance all tilts (staff/combat)
+tilt/clear [target]             # Clear all tilts (staff only)
```

### Combat Integration (`+combat`)

#### In-Combat Tilt Management
```
+combat/tilt/apply <target>=<tilt>  # Apply tilt during combat
+combat/tilt/remove <target>=<tilt> # Remove tilt during combat
+combat/tilt/list [target]          # List tilts in combat
```

## Usage Examples

### Applying Environmental Effects
```
# Staff sets up dangerous environment
+tilt/env/add darkness
+tilt/env/add ice

# During combat, these affect all participants
+combat/status  # Shows environmental tilts
```

### Personal Tilt Application
```
# Character gets blinded in combat
+combat/tilt/apply John=blinded

# Character recovers after 3 turns or treatment
+combat/tilt/remove John=blinded
```

### Automatic Progression
```
# Each combat round, tilts advance automatically
+combat/next  # At end of round, tilts advance

# Stunned (1 turn) expires automatically
# Poisoned (5 turns) counts down: 4, 3, 2, 1, expired
```

### Combat End Conversion
```
# When combat ends:
# Blinded tilt -> Blind condition
# Arm Wrack tilt -> Disabled condition
# Environmental tilts simply clear
```

## Integration Requirements

### Character Properties
Characters need a `tilts` property that creates a `TiltHandler`:
```python
@lazy_property
def tilts(self):
    return TiltHandler(self)
```

### Location Properties
Locations need environmental tilt support (handled automatically by combat tracker).

### Combat System Integration
- Turn advancement calls `_advance_tilts()`
- Combat status displays show tilts
- Combat end triggers tilt conversion

## Best Practices

### For Players
1. Use tilts for temporary combat effects
2. Remember tilts can become conditions outside combat
3. Check `+combat/status` for active environmental effects
4. Use resolution methods to overcome tilts

### For Staff
1. Apply environmental tilts for scene atmosphere
2. Use personal tilts for combat consequences
3. Monitor tilt duration and effects
4. Consider narrative impact of tilt-to-condition conversion

### For Combat
1. Environmental tilts set the scene mood
2. Personal tilts reflect combat damage/tactics
3. Tilt combinations create complex scenarios
4. Resolution provides tactical depth

## Technical Notes

### Storage
- Personal tilts stored in character attributes
- Environmental tilts stored in location attributes
- Automatic persistence and loading

### Performance
- Tilts only active during combat
- Automatic cleanup when combat ends
- Minimal overhead when not in combat

### Integration
- Works with existing condition system
- Compatible with health/damage system
- Integrates with team-based combat
