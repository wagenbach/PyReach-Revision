# Chronicles of Darkness Combat System

This document describes the comprehensive combat system implemented for the Chronicles of Darkness MUSH. The system follows the rules from the Chronicles of Darkness 2nd Edition core book and provides automated combat mechanics while maintaining narrative flexibility.

## Quick Start

1. **Join Combat**: `+combat/join [team]`
2. **Roll Initiative**: `+combat/init`
3. **Check Status**: `+combat/status`
4. **Take Actions**: `+combat/attack <target>`, `+combat/dodge`, etc.
5. **Advance Turns**: `+combat/next`
6. **Surrender or Leave**: `+combat/surrender` or `+combat/leave`

## Core Commands

### Combat Management
- `+combat/join [team]` - Join combat (optionally specify team number)
- `+combat/leave` - Leave combat
- `+combat/init [modifier]` - Roll initiative
- `+combat/status` - Show combat status and turn order
- `+combat/next` - Advance to next turn (staff/participants only)
- `+combat/end` - End combat (staff only)

### Team Management
- `+combat/team <number>` - Join specific team number
- `+combat/teams` - Show team composition

### Surrender System
- `+combat/surrender` - Offer surrender for your team
- `+combat/accept <team>` - Accept surrender from specified team
- `+combat/decline <team>` - Decline surrender from specified team

### Attack Actions (Instant)
- `+combat/attack <target> [weapon]` - Basic attack
- `+combat/attack/allout <target> [weapon]` - All-out attack (+2 attack, lose Defense)
- `+combat/attack/charge <target> [weapon]` - Charge attack (+1 damage, requires movement)
- `+combat/attack/specify <target>=<location> [weapon]` - Targeted attack (head, vitals, limb, etc.)
- `+combat/attack/multiple <target1>,<target2>... [weapon]` - Multiple attacks with penalties

### Defensive Actions
- `+combat/dodge` - Dodge (double Defense, lose next action)
- `+combat/dodge/full` - Full dodge for turn (Instant action)
- `+combat/block <attacker>` - Block (+2 Defense vs one attacker)
- `+combat/cover <rating>` - Take cover (1-4 rating)

### Movement Actions
- `+combat/move <distance>` - Move up to Speed (Reflexive)
- `+combat/sprint` - Sprint (roll Strength + Athletics for extra movement)

### Miscellaneous Actions
- `+combat/aim <target>` - Aim at target (+1 per turn, max +3)
- `+combat/grapple <target>` - Attempt to grapple target
- `+combat/reload [weapon]` - Reload weapon
- `+combat/ready <weapon>` - Ready/change weapon
- `+combat/delay <initiative>` - Delay action to lower initiative

### Health and Damage
- `+combat/health [target]` - Check health status
- `+combat/damage <target>=<amount>/<type>` - Apply damage (staff only)
- `+combat/heal <target>=<amount>/<type>` - Heal damage (staff only)

### Environmental (Staff Only)
- `+combat/environment <condition> <value>` - Set environmental modifiers

## Weapon System

### Weapon Commands
- `+weapons` - List all available weapons
- `+weapons <category>` - List weapons by category (unarmed, melee, ranged, firearms)
- `+weapons/info <weapon>` - Get detailed weapon information

### Weapon Categories

#### Unarmed Combat
- **Unarmed**: No damage bonus, bashing damage
- **Brass Knuckles**: No damage bonus, bashing damage, Size 1

#### Melee Weapons - Bludgeoning
- **Club**: +2 damage, bashing, Size 2
- **Baseball Bat**: +2 damage, bashing, Size 3
- **Crowbar**: +2 damage, bashing, Size 2
- **Mace**: +3 damage, bashing, Size 2

#### Melee Weapons - Bladed
- **Knife/Dagger**: +1 damage, lethal, Size 1
- **Sword**: +3 damage, lethal, Size 2
- **Machete**: +2 damage, lethal, Size 2
- **Axe**: +3 damage, lethal, Size 2

#### Ranged Weapons
- **Bow**: +2 damage, lethal, 50 yard range
- **Crossbow**: +3 damage, lethal, 80 yard range
- **Throwing Knife**: +1 damage, lethal, Str+Dex range

#### Firearms
- **Light Pistol**: +1 damage, lethal, 20 yard range, 7 round capacity
- **Heavy Pistol**: +2 damage, lethal, 30 yard range, 8 round capacity
- **Hunting Rifle**: +4 damage, lethal, 200 yard range, 5 round capacity
- **Assault Rifle**: +3 damage, lethal, 150 yard range, 30 round capacity, autofire
- **Shotgun**: +3 damage, lethal, 20 yard range, 6 round capacity

## Team System

### Team Management
The combat system supports organized team-based combat with automatic friendly fire prevention.

#### Team Assignment
- **Auto-Assignment**: Players are automatically assigned to balance teams (default: 2 teams)
- **Manual Assignment**: Use `+combat/join <team>` to specify team when joining
- **Team Changes**: Use `+combat/team <number>` to change teams during combat
- **Team Display**: Teams are shown in `+combat/status` and `+combat/teams`

#### Team Rules
- **Friendly Fire Prevention**: Allies (same team) cannot attack each other
- **Attack Blocking**: All attack commands check for team affiliation
- **Grapple Prevention**: Team members cannot grapple each other
- **Visual Identification**: Team numbers are color-coded in status displays

#### Team Commands
```
+combat/join 1          # Join combat on team 1
+combat/team 2          # Switch to team 2
+combat/teams           # Show all team compositions
+combat/status          # Shows teams in combat display
```

## Surrender System

### Surrender Mechanics
The surrender system allows teams to end combat diplomatically, giving losing sides an honorable way out.

#### How Surrender Works
1. **Offer Surrender**: Any team member can offer surrender for their entire team
2. **Team Consensus**: The entire team must agree to surrender (all members must use `+combat/surrender`)
3. **Enemy Response**: Opposing teams can accept or decline the surrender
4. **Combat Resolution**: Accepted surrender immediately ends combat

#### Surrender Commands
- `+combat/surrender` - Offer surrender for your team
- `+combat/accept <team>` - Accept surrender from specified team number
- `+combat/decline <team>` - Decline surrender from specified team number

#### Surrender Rules
- **Team Requirement**: Only complete teams can surrender (all members must agree)
- **Opposition Only**: Only opposing teams can accept/decline surrender
- **Immediate Effect**: Accepted surrender ends combat instantly
- **Declined Offers**: Declined surrender clears the offer and combat continues
- **Status Display**: Active surrender offers are shown in `+combat/status`

#### Strategic Considerations
- **Tactical Retreat**: Allows graceful exit from losing battles
- **Narrative Control**: Enables story-driven combat resolution
- **Training Scenarios**: Useful for sparring and practice sessions
- **Roleplay Opportunities**: Creates dramatic moments and character development

### Example Surrender Sequence
```
# Team 2 realizes they're losing
Alice (Team 2): +combat/surrender
Bob (Team 2): +combat/surrender

# Now Team 1 can respond
Charlie (Team 1): +combat/accept 2
# Combat ends with Team 2 surrendering

# Alternative: declining surrender
Charlie (Team 1): +combat/decline 2
# Combat continues, surrender offer cleared
```

## Combat Mechanics

### Initiative System
- **Calculation**: Initiative Attribute (Dex + Composure) + 1d10 + modifiers
- **Order**: Highest initiative acts first each turn
- **Re-rolling**: New initiative each scene (optional: once per scene)

### Action Types
- **Instant Actions**: Standard actions that take one turn (most combat actions)
- **Reflexive Actions**: Quick actions that don't consume your turn (movement up to Speed)
- **Extended Actions**: Complex actions requiring multiple turns

### Multiple Actions
- Each additional action after the first has a cumulative penalty
- 1st action: No penalty
- 2nd action: -1 penalty  
- 3rd action: -2 penalty, etc.

### Attack Resolution
1. **Calculate Attack Pool**: Attribute + Skill (varies by weapon type)
2. **Apply Modifiers**: Multiple action penalties, situational modifiers
3. **Subtract Defense**: Target's Defense rating (min 1 die remains)
4. **Roll Dice**: Count successes (8+ on d10, 10s count as 2)
5. **Calculate Damage**: Successes + weapon damage rating
6. **Apply Armor**: Subtract armor rating from damage
7. **Apply to Health**: Use existing health system for damage tracking

### Defense Calculation
- **Formula**: min(Wits, Dexterity) + Athletics
- **Modifiers**: Status effects, cover, prone, etc.
- **Application**: Subtracted from attack dice pools

### Damage Types
- **Bashing (/)**: Non-lethal damage (fists, clubs, falls)
- **Lethal (X)**: Serious wounds (knives, bullets, claws)
- **Aggravated (*)**: Supernatural/severe damage (fire, acid, supernatural attacks)

### Special Attack Types

#### All-Out Attack
- **Effect**: +2 to attack roll, lose all Defense for the turn
- **Use**: High-risk, high-reward attacks

#### Charge
- **Requirements**: Move at least 5 yards toward target
- **Effect**: +1 damage, +1 Defense against ranged attacks that turn

#### Specified Target Attacks
- **Head/Vitals**: -3 penalty, +1 damage if successful
- **Limbs**: -2 penalty
- **Hands/Feet**: -4 penalty

#### Multiple Attacks
- Attack multiple targets with increasing penalties (-1, -2, -3, etc.)
- Each attack is resolved separately

### Defensive Options

#### Dodge
- **Basic Dodge**: Double Defense for one attack, lose next action
- **Full Dodge**: Double Defense for entire turn, uses Instant action

#### Block
- **Effect**: +2 Defense against one specific attacker
- **Requirements**: Weapon or shield capable of blocking

#### Cover
- **Light Cover (1)**: -1 to ranged attacks
- **Partial Cover (2)**: -2 to ranged attacks  
- **Substantial Cover (3)**: -3 to ranged attacks
- **Full Cover (4)**: -4 to ranged attacks

### Environmental Modifiers
- **Darkness**: -1 to -3 penalty to actions
- **Weather**: Variable penalties based on conditions
- **Range**: Firearms have range penalties (Medium -1, Long -2, Extreme -3)

## Help System

### Quick Help Commands
- `+chelp` - General combat overview
- `+chelp actions` - List all combat actions
- `+chelp teams` - Team system and surrender mechanics
- `+chelp initiative` - Initiative system details
- `+chelp damage` - Damage and health system
- `+chelp modifiers` - Combat modifiers and penalties

## Integration with Existing Systems

### Health System
The combat system integrates seamlessly with the existing `+health` command system:
- Damage is automatically applied using the health tracking system
- Visual health display shows bashing (/), lethal (X), and aggravated (*) damage
- Wound penalties are automatically calculated

### Character Stats
Combat uses the existing character statistics system:
- **Attributes**: Strength, Dexterity, Stamina, Wits, Composure
- **Skills**: Weaponry, Brawl, Firearms, Athletics
- **Advantages**: Health, Defense, Speed, Initiative (derived stats)

### Equipment System
Weapons can be tracked using the existing equipment system with additional combat data.

## Staff Commands

### Combat Management
- `+combat/end` - Force end combat
- `+combat/damage <target>=<amount>/<type>` - Directly apply damage
- `+combat/heal <target>=<amount>/<type>` - Directly heal damage
- `+combat/environment <condition> <value>` - Set environmental conditions

## Examples

### Basic Combat Sequence
```
Alice: +combat/join 1
Alice: +combat/init
Bob: +combat/join 2  
Bob: +combat/init
Alice: +combat/status
Alice: +combat/attack Bob sword
Bob: +combat/dodge/full
Alice: +combat/next
Bob: +combat/attack Alice
Alice: +combat/next
```

### Team-Based Combat
```
# Setting up teams
Alice: +combat/join 1
Bob: +combat/join 1
Charlie: +combat/join 2
Diana: +combat/join 2

# Everyone rolls initiative
Alice: +combat/init
Bob: +combat/init
Charlie: +combat/init
Diana: +combat/init

# Check team composition
Alice: +combat/teams
Alice: +combat/status

# Combat with friendly fire prevention
Alice: +combat/attack Charlie sword    # Valid - different teams
Bob: +combat/attack Alice             # Error - same team!
Charlie: +combat/attack/allout Alice  # Valid - different teams
```

### Surrender Scenario
```
# Team 2 is losing and wants to surrender
Charlie: +combat/surrender
Diana: +combat/surrender

# Team 1 sees the surrender offer
Alice: +combat/status                 # Shows surrender offers
Bob: +combat/accept 2                 # Accepts surrender
# Combat ends immediately

# Alternative: declining surrender
Alice: +combat/decline 2              # Declines surrender
# Combat continues, offers cleared
```

### Advanced Combat Actions
```
Alice: +combat/attack/specify Bob=head knife
Bob: +combat/block Alice
Alice: +combat/attack/multiple Charlie,Diana crowbar
Charlie: +combat/grapple Alice
Diana: +combat/aim Alice
Bob: +combat/cover 2
```

## Best Practices

1. **Join Combat Early**: Use `+combat/join [team]` when conflict seems likely
2. **Organize Teams**: Use `+combat/teams` to verify team composition before combat
3. **Check Status Regularly**: Use `+combat/status` to track turn order, teams, and surrender offers
4. **Plan Actions**: Consider multiple action penalties when planning your turn
5. **Use Defense**: Don't forget defensive options like dodge and cover
6. **Consider Surrender**: Use surrender system for narrative resolution and training
7. **Coordinate Turns**: Use `+combat/next` to keep combat flowing smoothly
8. **Respect Allies**: Remember that friendly fire is prevented - coordinate with teammates

## System Features

### Automated Features
- Automatic initiative tracking and turn order
- Multiple action penalty calculation
- Defense application to attack rolls
- Damage calculation with weapon ratings and armor
- Integration with existing health tracking
- Status effect tracking (prone, cover, grappling, etc.)
- Team assignment and friendly fire prevention
- Surrender offer tracking and resolution

### Tactical Depth
- Various attack types with different risk/reward profiles
- Defensive options beyond basic Defense
- Environmental considerations
- Range and weapon type considerations
- Grappling system for close combat
- Team-based strategic combat
- Diplomatic resolution through surrender

### Narrative Support
- Clear action descriptions and feedback
- Room-wide announcements for dramatic moments
- Integration with experience system (beats for damage)
- Flexible weapon system supporting various combat styles
- Team-based storytelling opportunities
- Surrender system for character development and narrative resolution

### Future Support
- Create a method for allowing random combats for MUSHes that have MUD-like capabilities or "solo play"
- Allow for integration of rewards for certain combats

A lot of this needs to have continued development to be effective on a MUSH environment. Additionally, it might be better to work using the EvMenu rather than relying on players to type their input into their client. That said, it is functional for what it is, and could be used to provide combat scenarios between players and player/staff-created NPCs.
