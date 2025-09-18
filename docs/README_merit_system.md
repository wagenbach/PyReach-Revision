# Chronicles of Darkness Merit System

## Overview
The merit system implements the full Chronicles of Darkness merit database with proper prerequisite validation, experience point integration, and character sheet display. Merits are character traits purchased with experience points that provide special abilities, advantages, and story hooks.

## Merit Categories

### Mental Merit examples
Cognitive advantages and intellectual capabilities:
- **Area of Expertise**: Specialized knowledge providing enhanced bonuses
- **Common Sense**: Storyteller guidance on courses of action
- **Danger Sense**: Enhanced awareness of threats
- **Eidetic Memory**: Perfect recall abilities
- **Fast Reflexes**: Initiative bonuses
- **Professional Training**: Extensive professional expertise

### Physical Merit examples
Physical advantages and capabilities:
- **Ambidextrous**: No off-hand penalties
- **Fleet of Foot**: Enhanced movement speed
- **Hardy**: Resistance to disease and poison
- **Iron Stamina**: Fatigue resistance
- **Quick Draw**: Lightning-fast weapon readiness

### Social Merit examples
Social connections and advantages:
- **Allies**: Organizational connections
- **Contacts**: Information sources
- **Fame**: Public recognition
- **Resources**: Disposable income
- **Status**: Organizational standing
- **Striking Looks**: Appearance advantages

### Fighting/Style Merit examples
Combat techniques and martial arts:
- **Defensive Combat**: Enhanced defense calculations
- **Fighting Finesse**: Dexterity-based weapon combat
- **Martial Arts**: Formal martial arts training
- **Street Fighting**: Dirty fighting techniques
- **Armed Defense**: Weapon defensive techniques

### Supernatural Merit examples
Psychic and supernatural abilities:
- **Aura Reading**: Perceive emotional auras
- **Telepathy**: Read thoughts and send messages
- **Telekinesis**: Move objects with mind
- **Medium**: Communicate with ghosts
- **Psychometry**: Read object impressions

## Commands

### Experience Management
```
+xp                              - Show current experience and beats
+xp/beat <source>               - Add a beat from valid source
+xp/spend <stat>=<dots>         - Spend experience on attributes/skills
+xp/costs                       - Show experience point costs
```

### Merit Management
```
+xp/buy <merit>=[dots]          - Purchase a merit with experience
+xp/refund <merit>              - Refund a merit (staff only)
+xp/list merits [category]      - List available merits by category
+xp/info <merit>                - Show detailed merit information
```

### Examples
```
+xp/buy contacts=3              - Buy Contacts merit at 3 dots
+xp/buy fast_reflexes 2         - Buy Fast Reflexes merit at 2 dots
+xp/list merits mental          - List all mental merits
+xp/info striking_looks         - Show Striking Looks merit details
+xp/spend strength=4            - Raise Strength attribute to 4 dots
```

## Experience Costs
- **Attributes**: 4 XP per dot
- **Skills**: 2 XP per dot  
- **Merits**: 1 XP per dot
- **Integrity**: 2 XP per dot
- **Specialties**: 1 XP each

## Beat Sources
Players can earn beats from these valid sources:
- dramatic_failure, exceptional_success, conditions, aspirations
- story, scene, session, roleplay, challenge, sacrifice
- discovery, relationship, consequence, learning, growth

Every 5 beats automatically converts to 1 experience point.

## Prerequisites System

### Format
Prerequisites use a specific format with logical operators:
- `attribute:value` - Requires specific attribute level
- `skill:value` - Requires specific skill level  
- `[option1:value,option2:value]` - OR requirement (either option)
- `requirement1,requirement2` - AND requirement (both needed)

### Examples
- `resolve:2` - Requires Resolve 2+
- `[wits:3,dexterity:3]` - Requires either Wits 3+ OR Dexterity 3+
- `strength:3,brawl:2` - Requires both Strength 3+ AND Brawl 2+
- `martial_arts:2,stamina:3` - Requires Martial Arts merit 2+ AND Stamina 3+

### Validation
- System automatically checks current character stats
- Prevents merit purchase if prerequisites not met
- Displays clear error messages with missing requirements
- Supports complex nested prerequisites with multiple options

## Character Sheet Integration

### Display Organization
Merits appear on character sheets organized by category:
```
MERITS
----------------------------------------------------------------------

Mental Merits:
  Fast Reflexes: ●●○○○
  Eidetic Memory: ●●○○○

Physical Merits:
  Fleet of Foot: ●●●○○
  Hardy: ●○○○○

Social Merits:
  Contacts: ●●●●○
  Resources: ●●○○○
```

### Dot Display
- Uses standard dot notation (●○○○○) or ASCII (*----) based on client support
- Shows current dots vs maximum possible dots
- Color-coded by category for easy identification
- Proper formatting with merit type headers

## Data Structure

### Merit Database
Located in `world/cofd/merits/general_merits.py`:
- Complete Chronicles of Darkness merit list
- Organized by category (mental, physical, social, etc.)
- Full prerequisite definitions
- Accurate dot ranges and descriptions

### Character Storage
Merits stored in character stats under `merits` category:
```python
character.db.stats["merits"] = {
    "fast_reflexes": {
        "dots": 2,
        "max_dots": 3,
        "merit_type": "mental",
        "description": "+1 Initiative per dot"
    }
}
```

### Merit Lookup
- Dictionary-based lookup by normalized names
- Case-insensitive with space-to-underscore conversion
- Fast O(1) access for validation and display

## Staff Functions

### Administrative Commands
```
+xp/refund <merit>              - Refund merit for full experience cost
```

### Merit Management
- Staff can refund merits at full experience cost
- No prerequisite checking for staff additions
- Full administrative control over character advancement

## Integration Points

### Combat System
- Fighting and style merits integrate with combat mechanics
- Defensive Combat merit affects defense calculations
- Fast Reflexes merit provides initiative bonuses
- Combat system checks for relevant merits automatically

### Equipment System
- Merits remain separate from physical equipment
- No overlap between gear and character traits
- Clear distinction between possessions and abilities

### Condition System
- Some merits interact with condition application
- Merit effects can trigger or modify conditions
- Integrated but distinct systems

## Technical Implementation

### Validation Engine
- Robust prerequisite parsing and validation
- Support for complex logical expressions
- Clear error messaging for failed requirements
- Extensible for future merit types

### Experience Integration
- Seamless XP spending and earning
- Automatic beat-to-experience conversion
- Transaction logging and validation
- Rollback support for staff corrections

### Performance Optimization
- Dictionary-based merit lookup for O(1) access
- Lazy loading of merit data
- Efficient character sheet generation
- Minimal database queries

## Usage Guidelines

### For Players
1. Check merit prerequisites with `+xp/info <merit>`
2. Ensure sufficient experience points before purchasing
3. Consider character concept and story integration
4. Consult staff for unusual merit combinations

### For Staff
1. Use `+xp/refund` judiciously for corrections
2. Validate character advancement during approval
3. Consider merit interactions in story scenes
4. Monitor experience gain rates for balance

## Future Expansion

### template-Specific Merits
- Framework supports additional merit categories
- Easy addition of supernatural template merits
- Extensible prerequisite system for complex requirements

### Custom Merits
- Database structure supports custom merit addition
- Template system for consistent merit creation
- Staff tools for merit management and approval

### Integration Enhancements
- Enhanced combat system integration
- Social maneuvering merit effects
- Investigation system merit bonuses
- Automated merit effect application
