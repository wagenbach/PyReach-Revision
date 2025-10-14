# Mystery Cult System Guide

## Overview

The Mystery Cult system allows staff and group leaders to create customized Mystery Cults (cabals) with specific benefits granted at each initiation level. When characters are members of the cult and have the **Mystery Cult Initiation** merit on their character sheet, they automatically gain access to the benefits defined for their initiation level.

## Creating a Mystery Cult

### Step 1: Create the Group

```
+group/create The Invisible College
> Created group 'The Invisible College' with ID #1

+group/type 1=cabal
> Set group 'The Invisible College' type to Cabal
```

### Step 2: Set Up Initiation Benefits

Use `+mysterycult/set` to define what benefits are granted at each initiation level (1-5).

**Format:**
```
+mysterycult/set <group id>/<level>=<type>:<name>[:<description>]
```

**Benefit Types:**
- **specialty** - A Skill Specialty
- **merit** - A Merit (with dots)
- **skill** - A Skill dot
- **other** - Any other benefit

### Step 3: Add Members

```
+group/add 1=Marcus
> Added Marcus to group 'The Invisible College'
```

### Step 4: Set Member's Initiation Level

Members need the Mystery Cult Initiation merit on their character sheet:

```
+stat/merit Marcus/Mystery Cult Initiation=3
```

This character will now have access to all benefits from levels 1-3.

## Initiation Level Guidelines

These are the standard guidelines from Chronicles of Darkness:

| Level | Standard Benefit |
|-------|------------------|
| 1 | A Skill Specialty or one-dot Merit |
| 2 | A one-dot Merit |
| 3 | A Skill dot, or a two-dot Merit (often supernatural) |
| 4 | A three-dot Merit, often supernatural in origin |
| 5 | A three-dot Merit, or a major advantage not reflected in game traits |

## Commands

Mystery Cult commands are integrated into the `+group` command system. You can use either `+group` or the standalone `+mysterycult` command.

### View Cult Benefits

**Using +group:**
```
+group <id>
```
When viewing a cabal, automatically shows Mystery Cult benefits summary.

**Using +mysterycult:**
```
+mysterycult <group id>
```
Shows detailed benefits for the Mystery Cult.

### Set a Benefit

**Using +group:**
```
+group/set <group id>/<level>=<type>:<name>[:<description>]
```

**Using +mysterycult:**
```
+mysterycult/set <group id>/<level>=<type>:<name>[:<description>]
```

**Examples:**
```
+group/set 1/1=specialty:Politics (Bureaucracy)
+group/set 1/2=merit:Language (Aramaic) 1
+group/set 1/3=merit:Contacts 2:Mammon cultists
+group/set 1/4=merit:Thief of Fate 3
+group/set 1/5=other:Three dots Resources + monthly ••••• purchase:From cult coffers
```

### Clear a Benefit

**Using +group:**
```
+group/clear <group id>/<level>
```

**Using +mysterycult:**
```
+mysterycult/clear <group id>/<level>
```

**Example:**
```
+group/clear 1/3
> Cleared Level 3 benefit for 'The Invisible College'.
```

### Check Character Benefits

**Using +group:**
```
+group/check <group id>=<character>
```

**Using +mysterycult:**
```
+mysterycult/check <group id>=<character>
```

This shows what benefits the character is entitled to based on their Mystery Cult Initiation merit level.

**Example:**
```
+group/check 1=Marcus
> Mystery Cult Benefits for Marcus
> Cult: The Invisible College (#1)
> 
> Benefits Marcus should have:
> Level 1 (Specialty): Politics (Bureaucracy)
> Level 2 (Merit): Language (Aramaic) 1
> Level 3 (Merit): Contacts 2
>   Mammon cultists
```

### View Templates

**Using +group:**
```
+group/template <name>
```

**Using +mysterycult:**
```
+mysterycult/template <name>
```

Available templates:
- **mammon** - Chosen of Mammon (wealth and power cult)
- **sisters** - Sisters of the Machine Gun, Brothers of the Bomb (anti-God-Machine fighters)

**Example:**
```
+group/template mammon
> Example Mystery Cults:
> 
> Chosen of Mammon
> Followers of Mammon obtain material wealth and power at any cost
> 
> Initiation Benefits:
>   1: Politics Specialty in Bureaucracy
>   2: Language Merit (Aramaic)
>   3: Two dots between Contacts, Allies, Resources, or Retainers
>   4: Thief of Fate (•••) Merit
>   5: Three dots of Resources plus one Resources ••••• purchase per month from cult coffers
```

## Complete Example: Creating the Chosen of Mammon

```bash
# 1. Create the cult
+group/create Chosen of Mammon
> Created group 'Chosen of Mammon' with ID #1

+group/type 1=cabal
> Set group 'Chosen of Mammon' type to Cabal

+group/desc 1=Mammon believes in the almighty dollar, and its inherent power. Followers obtain material wealth and power at any cost.
> Set description for group 'Chosen of Mammon'.

# 2. Set up initiation benefits
+group/set 1/1=specialty:Politics (Bureaucracy)
> Set Level 1 benefit for 'Chosen of Mammon': Specialty - Politics (Bureaucracy)

+group/set 1/2=merit:Language (Aramaic) 1
> Set Level 2 benefit for 'Chosen of Mammon': Merit - Language (Aramaic) 1

+group/set 1/3=merit:Contacts 2:Mammon cultists
> Set Level 3 benefit for 'Chosen of Mammon': Merit - Contacts 2

+group/set 1/4=merit:Thief of Fate 3
> Set Level 4 benefit for 'Chosen of Mammon': Merit - Thief of Fate 3

+group/set 1/5=other:Resources 3 + one Resources ••••• purchase per month:From cult coffers
> Set Level 5 benefit for 'Chosen of Mammon': Other - Resources 3 + one Resources ••••• purchase per month

# 3. View the cult
+group 1
> Chosen of Mammon (#1)
> Type: Cabal
> ...
> 
> Mystery Cult Initiation Benefits:
>   Level 1 (Specialty): Politics (Bureaucracy)
>   Level 2 (Merit): Language (Aramaic) 1
>   Level 3 (Merit): Contacts 2
>   Level 4 (Merit): Thief of Fate 3
>   Level 5 (Other): Resources 3 + one Resources ••••• purchase per month
>   Use +mysterycult for full details

# 4. Add a member
+group/add 1=Marcus
> Added Marcus to group 'Chosen of Mammon'

# 5. Set their initiation level
+stat/merit Marcus/Mystery Cult Initiation=3
> Set Mystery Cult Initiation to 3 for Marcus

# 6. Check what benefits they should have
+group/check 1=Marcus
> Mystery Cult Benefits for Marcus
> Cult: Chosen of Mammon (#1)
> 
> Benefits Marcus should have:
> Level 1 (Specialty): Politics (Bureaucracy)
> Level 2 (Merit): Language (Aramaic) 1
> Level 3 (Merit): Contacts 2
>   Mammon cultists
```

## Viewing Mystery Cult in Group Display

When you view a cabal with `+group <id>`, it automatically shows a summary of the Mystery Cult benefits:

```
+group 1
> Chosen of Mammon (#1)
> Type: Cabal
> Leader: Marcus
> 
> Description:
> Mammon believes in the almighty dollar, and its inherent power...
> 
> Members:
>   Marcus - High Priest (Leader)
>   Luna - Acolyte
> 
> Mystery Cult Initiation Benefits:
>   Level 1 (Specialty): Politics (Bureaucracy)
>   Level 2 (Merit): Language (Aramaic) 1
>   Level 3 (Merit): Contacts 2
>   Level 4 (Merit): Thief of Fate 3
>   Level 5 (Other): Resources 3 + one Resources ••••• purchase per month
>   Use +mysterycult for full details
```

## Staff Notes

### Applying Benefits

The system **tracks** what benefits characters should have, but doesn't automatically apply them to character sheets. Staff should:

1. Use `+mysterycult/check <id>=<character>` to see what benefits they're entitled to
2. Manually apply those benefits using `+stat` commands
3. Track benefits in character notes if needed

### Why Manual Application?

- **Flexibility**: Some benefits are complex (like "major advantage not reflected in game traits")
- **Context**: Staff can interpret benefits appropriately for the game
- **Control**: Prevents automatic changes to character sheets
- **Documentation**: The cult system provides a reference, staff implements appropriately

### Specialty Application

For specialties like "Politics (Bureaucracy)":
```
+stat/specialty Marcus/Politics=Bureaucracy
```

### Merit Application

For merits with dots:
```
+stat/merit Marcus/Contacts=2
```

### Skill Dots

For skill dots at level 3:
```
+stat/skill Marcus/Occult=+1
```
(Or set to desired value)

### Other Benefits

For "other" type benefits, record in notes or apply as appropriate for your game.

## Permissions

- **Staff (Admin/Builder)**: Can modify all Mystery Cult benefits
- **Group Leader**: Can modify benefits for their cult
- **Members**: Can view benefits for cults they belong to
- **Anyone**: Can view public cults

## Best Practices

### 1. Start with Templates

Use `+mysterycult/template mammon` or `+mysterycult/template sisters` to see examples before creating your own.

### 2. Document Everything

Use the description field (third part after `:`) to note details:
```
+mysterycult/set 1/3=merit:Allies 2:Academic contacts who provide research assistance
```

### 3. Follow the Guidelines

Stick to the standard benefit levels unless you have a specific reason to deviate:
- Level 1: Specialty or 1-dot merit
- Level 2: 1-dot merit
- Level 3: Skill dot or 2-dot merit
- Level 4: 3-dot merit
- Level 5: 3-dot merit or major advantage

### 4. Coordinate with Players

When a player wants to join a Mystery Cult:
1. Add them to the group
2. Set their Mystery Cult Initiation merit
3. Apply the appropriate benefits to their sheet
4. Note the cult benefits in their character notes

### 5. Track Progression

As characters advance in the cult:
1. Update their Mystery Cult Initiation merit
2. Apply new benefits for higher levels
3. Track in character notes when benefits were gained

## Integration with Character Sheets

### Setting Mystery Cult Initiation

The Mystery Cult Initiation merit should be set on the character sheet:

```
+stat/merit <character>/Mystery Cult Initiation=<level>
```

This is what the `+mysterycult/check` command reads to determine what benefits the character should have.

### Applying Benefits

Staff should manually apply benefits as appropriate:

**Specialties:**
```
+stat/specialty <character>/<skill>=<specialty>
```

**Merits:**
```
+stat/merit <character>/<merit>=<rating>
```

**Skills:**
```
+stat/skill <character>/<skill>=<value>
```

**Other Benefits:**
Record in character notes or apply as appropriate for your game.

## Troubleshooting

### "Group is not a Mystery Cult (cabal)"

Make sure the group type is set to 'cabal':
```
+group/type <id>=cabal
```

### Benefits Not Showing in Check

Make sure:
1. The character has the Mystery Cult Initiation merit on their sheet
2. The character is a member of the group
3. Benefits have been set for those levels

### Can't Modify Benefits

Check permissions:
- You must be staff or the group leader
- Use `+group <id>` to see who the leader is

## Example Mystery Cults

### Academic Mystery Cult

```
+mysterycult/set 1/1=specialty:Academics (Research)
+mysterycult/set 1/2=merit:Library (Occult) 1
+mysterycult/set 1/3=skill:Occult 1
+mysterycult/set 1/4=merit:Encyclopedic Knowledge 3
+mysterycult/set 1/5=other:Access to forbidden archives:Major research advantage
```

### Street-Level Occult Group

```
+mysterycult/set 2/1=specialty:Streetwise (Occult Community)
+mysterycult/set 2/2=merit:Contacts (Occultists) 1
+mysterycult/set 2/3=merit:Allies (Street Mages) 2
+mysterycult/set 2/4=merit:Safe Place 3:Hidden ritual space
+mysterycult/set 2/5=merit:Resources 3:From group pooled funds
```

### Tech-Occult Hybrid

```
+mysterycult/set 3/1=specialty:Computer (Hacking)
+mysterycult/set 3/2=merit:Contacts (Hackers) 1
+mysterycult/set 3/3=skill:Computer 1
+mysterycult/set 3/4=merit:Resources 3:Cryptocurrency funds
+mysterycult/set 3/5=other:Access to God-Machine surveillance network:Major intelligence advantage
```

## Technical Notes

### Data Storage

Mystery Cult benefits are stored in `group.db.mystery_cult_benefits` as a dictionary:

```python
{
    1: {'type': 'specialty', 'name': 'Politics (Bureaucracy)', 'description': ''},
    2: {'type': 'merit', 'name': 'Language (Aramaic) 1', 'description': ''},
    3: {'type': 'merit', 'name': 'Contacts 2', 'description': 'Mammon cultists'},
    4: {'type': 'merit', 'name': 'Thief of Fate 3', 'description': ''},
    5: {'type': 'other', 'name': 'Resources 3 + monthly ••••• purchase', 'description': 'From cult coffers'}
}
```

### Methods Available

On Group objects:
- `set_mystery_benefit(level, type, name, description)` - Set a benefit
- `get_mystery_benefit(level)` - Get benefit at level
- `get_all_mystery_benefits()` - Get all benefits
- `clear_mystery_benefit(level)` - Clear a benefit
- `get_character_mystery_benefits(character)` - Get benefits for a character

## Summary

The Mystery Cult system provides:
- Flexible benefit definition at each initiation level
- Clear tracking of what characters should have
- Integration with the group system
- Example templates for inspiration
- Staff control over benefit application

This allows you to create rich, detailed Mystery Cults that provide progressive rewards as characters advance through the ranks.

