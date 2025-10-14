# Group Merits and Stats System Guide

## Overview

The group system has been enhanced to support group-specific merits and stats that are unique to different types of groups. This is particularly important for supernatural groups like Packs (Werewolf), Krewes (Geist), Cults (Mummy), Mystery Cults (Mage/Mortal), and Cells (Hunter).

## Table of Contents

1. [Group-Specific Merits](#group-specific-merits)
2. [Pack Totems](#pack-totems)
3. [Commands Reference](#commands-reference)
4. [Usage Examples](#usage-examples)

---

## Group-Specific Merits

Different group types have access to different merits that represent their unique capabilities and resources.

### Pack Merits (Werewolf: The Forsaken)

- **Den** (• to •••••): An enclosed physical location for Packs to relax and feel safe
- **Directed Rage** (•••, ••••, or •••••): Helps packs direct Rage-filled members' anger at foes
  - ••• - Packmates in Wasu-Im act one step closer to harmony
  - •••• - Characters in Basu-Im can prioritize non-pack members
  - ••••• - Characters won't target packmates unless threatened
- **Magnanimous Totem** (••, •••, or ••••): Allows non-Uratha to take Totem merit
  - •• - Wolf-Blooded may take up to 5 dots in Totem
  - ••• - Humans may take 1 dot of Totem
  - •••• - Humans may take up to 5 dots of Totem
- **Moon's Grace** (•••, ••••, or •••••): Allows non-Uratha to use werewolf abilities
  - ••• - Pack can use Pack Tactics
  - •••• - Members can learn and lead Wolf Rites
  - ••••• - Members gain Renown and Shadow/Wolf Gifts (cannot have Uratha in pack)
- **Territorial Advantage** (• to •••••): Leverage territory familiarity to affect intruders

### Krewe Merits (Geist: The Sin-Eaters)

- **Krewe Pool** (• to •••••): Shared pool of plasm
- **Krewe Skill** (• to •••••): Shared skill benefit

### Cult Merits (Mummy: The Curse)

- **Cult** (• to •••••): Size and resources of cult
- **Relic** (• to •••••): Ancient artifacts with mystical properties

### Mystery Cult Merits (Mortal/Mage)

- **Mystery Cult Initiation** (• to •••••): Membership and rank
- **High Speech** (•): Knowledge of Supernal language (requires Initiation 3+)

### Cell Merits (Hunter: The Vigil)

- **Safe Place** (• to •••••): Secure location for operations
- **Tactical Operations** (• to •••••): Combat training and coordination

---

## Pack Totems

Packs (Werewolf groups) have a unique totem system. The totem is a spirit bound to the pack, granting them special abilities and advantages.

### Building a Totem

#### Step 1: Totem Points

The totem is powered by the combined Totem merit dots of all pack members. Each member who has the Totem merit contributes their dots to the pack's total.

**Example**: If your pack has:
- Member 1: Totem ••
- Member 2: Totem •••
- Member 3: Totem •
- Total: 6 totem points

#### Step 2: Name and Concept

Give your totem a name and concept that reflects its nature.

**Examples**:
- Silver Wind - Swift storm spirit
- Blood Moon - Hunting spirit
- Stone Sentinel - Protective earth spirit

#### Step 3: Aspiration and Ban

Totems have an Aspiration (which acts as a 4th aspiration for each pack member) and a Ban (a prohibition the pack must uphold).

**Example Ban**: "Cannot immerse in water" for a fire spirit

#### Step 4: Attributes

Distribute totem points among three attributes:
- **Power**: Raw strength and might
- **Finesse**: Speed and precision
- **Resistance**: Durability and willpower

**Rules**:
- Each attribute must have at least 1 dot
- No single attribute can have more than half the total totem points
- Total attributes cannot exceed totem points

**Example with 6 points**: Power 2, Finesse 3, Resistance 1

#### Step 5: Rank and Derived Stats

Rank is automatically calculated from total attributes:
- Rank • (1-5 attributes)
- Rank •• (6-10 attributes)
- Rank ••• (11-15 attributes)
- Rank •••• (16-20 attributes)
- Rank ••••• (21+ attributes)

**Derived Stats**:
- **Corpus** (Health): Power + Resistance
- **Willpower**: Finesse + Resistance
- **Defense**: Lower of Finesse or Resistance
- **Initiative**: Finesse + Resistance
- **Max Essence**: Lower of totem points or rank maximum

#### Step 6: Influence

Totems have Influence over their concept's sphere. Set the type and dots.

**Examples**:
- Wind: 2 dots
- Moon: 3 dots
- Blood: 1 dot

#### Step 7: Numina (Spirit Powers)

Totems gain numina (spirit powers) based on totem points:
- Base: 1 numen
- +1 numen per 4 totem points

**Example**: 6 totem points = 2 numina (1 + 6/4 rounded down)

Common numina for totems:
- **Speed**: Double or triple Speed
- **Awe**: Incapacitate through dread
- **Emotional Aura**: Project an emotion
- **Regenerate**: Heal damage
- **Seek**: Sense specific conditions
- **Pathfinder**: Know quickest path

#### Step 8: Pack Advantage

The totem grants an advantage to ALL pack members based on available experiences:

| Totem Points | Experiences Available |
|--------------|----------------------|
| 1-8          | 1                    |
| 9-14         | 3                    |
| 15-20        | 5                    |
| 20+          | 10                   |

**Experience Costs**:
- Attribute: 5 experiences (grants +1 dot to all members)
- Skill: 3 experiences (grants +1 dot to all members)
- Specialty: 1 experience (grants specialty to all members)
- Merit: 2 experiences per dot

**Example with 6 totem points** (1 experience):
- Could grant: 1 Skill Specialty to all pack members

**Example with 15 totem points** (5 experiences):
- Could grant: 1 dot of Strength to all members (5 exp) OR
- 1 dot of Athletics to all members (3 exp) + 1 Specialty (1 exp) + 1 exp remaining

---

## Commands Reference

### +groupmerit - Manage Group Merits

```
+groupmerit <group id>                  - View all merits for a group
+groupmerit/set <id>=<merit>:<rating>   - Set a group merit (staff/leader)
+groupmerit/remove <id>=<merit>         - Remove a group merit (staff/leader)
+groupmerit/list <type>                 - List available merits for group type
+groupmerit/calc <id>                   - Show member merit contributions
```

**Examples**:
```
+groupmerit 1                    - View merits for group #1
+groupmerit/list pack            - See all available pack merits
+groupmerit/set 1=Den:3          - Set Den to 3 dots for group #1
+groupmerit/remove 1=Den         - Remove Den merit from group #1
+groupmerit/calc 1               - Show which members have relevant merits
```

### +totem - Manage Pack Totems

```
+totem <group id>                       - View totem information
+totem/name <id>=<name>                 - Set totem name (staff/leader)
+totem/concept <id>=<concept>           - Set totem concept (staff/leader)
+totem/aspiration <id>=<text>           - Set totem aspiration (staff/leader)
+totem/ban <id>=<text>                  - Set totem ban (staff/leader)
+totem/attr <id>=<pow>/<fin>/<res>      - Set totem attributes (staff/leader)
+totem/influence <id>=<type>:<dots>     - Set totem influence (staff/leader)
+totem/numen/add <id>=<numen>           - Add a numen (staff/leader)
+totem/numen/remove <id>=<numen>        - Remove a numen (staff/leader)
+totem/numen/list                       - List available numina
+totem/advantage <id>=<type>:<name>:<rating> - Set pack advantage (staff/leader)
+totem/calc <id>                        - Calculate totem points from members
+totem/notes <id>=<text>                - Set totem notes (staff/leader)
```

**Examples**:
```
+totem 1                                - View totem for group #1
+totem/calc 1                           - See totem points breakdown
+totem/name 1=Silver Wind               - Name the totem
+totem/concept 1=Swift storm spirit     - Set concept
+totem/aspiration 1=Hunt the corrupt    - Set aspiration
+totem/ban 1=Cannot enter holy ground   - Set ban
+totem/attr 1=2/3/1                     - Power 2, Finesse 3, Resistance 1
+totem/influence 1=Wind:2               - 2 dots of Wind influence
+totem/numen/list                       - See all available numina
+totem/numen/add 1=Speed                - Add Speed numen
+totem/numen/add 1=Awe                  - Add Awe numen
+totem/advantage 1=specialty:Athletics (Pursuit):1  - Grant Athletics (Pursuit) specialty
+totem/notes 1=Appears as silver wolf   - Add notes
```

### Updated +group Command

The `+group <id>` command now shows:
- Group merits (if any are set)
- Totem information (for packs with totems)
- Pack advantage (what the totem grants to members)

---

## Usage Examples

### Example 1: Setting Up a New Pack

```
# 1. Create the pack
+group/create Silver Fangs
> Created group 'Silver Fangs' with ID #5

# 2. Set it as a pack
+group/type 5=pack
> Set group 'Silver Fangs' type to Pack

# 3. Add members
+group/add 5=Marcus
> Added Marcus to group 'Silver Fangs'

+group/add 5=Luna
> Added Luna to group 'Silver Fangs'

# 4. Set pack merits
+groupmerit/set 5=Den:2
> Set Den to 2 dots for group 'Silver Fangs'

+groupmerit/set 5=Territorial Advantage:3
> Set Territorial Advantage to 3 dots for group 'Silver Fangs'

# 5. Check totem points (members need Totem merit on their sheets)
+totem/calc 5
> Total Totem Points: 6
> Available Advantage Experiences: 1
> Maximum Numina: 2
> 
> Member Contributions:
>   Marcus: 3 dots
>   Luna: 3 dots

# 6. Build the totem
+totem/name 5=Silver Wind
> Set totem name to 'Silver Wind'

+totem/concept 5=Swift storm spirit that guides the hunt
> Set totem concept

+totem/aspiration 5=Hunt down those who prey on the innocent
> Set totem aspiration

+totem/ban 5=Cannot cross running water while material
> Set totem ban

+totem/attr 5=2/3/1
> Set totem attributes: Power 2, Finesse 3, Resistance 1

+totem/influence 5=Wind:2
> Set totem influence Wind to 2 dots

+totem/numen/add 5=Speed
> Added numen 'Speed'

+totem/numen/add 5=Pathfinder
> Added numen 'Pathfinder'

+totem/advantage 5=specialty:Survival (Tracking):1
> Set pack advantage to specialty 'Survival (Tracking)'

# 7. View the complete totem
+totem 5
> Silver Wind
> Totem for Silver Fangs (#5)
> 
> Concept: Swift storm spirit that guides the hunt
> Aspiration: Hunt down those who prey on the innocent
> Ban: Cannot cross running water while material
> 
> Rank: •• (2)
> Totem Points: 6
> 
> Attributes:
>   Power: 2
>   Finesse: 3
>   Resistance: 1
>   Total: 6
> 
> Derived Stats:
>   Corpus: 3
>   Willpower: 4
>   Defense: 1
>   Initiative: 4
>   Essence: 6/10
> 
> Influence:
>   Wind: •• (2)
> 
> Numina:
>   • Speed
>   • Pathfinder
>   (2/2 numina)
> 
> Pack Advantage:
>   Specialty: Survival (Tracking)
```

### Example 2: Managing Group Merits

```
# View available merits for packs
+groupmerit/list pack
> Available Merits for Pack:
> 
> Den (• to •••••)
>   An enclosed physical location for Packs to relax and feel safe
>   Prerequisites: Pack
>   Source: Pack 29
> 
> Directed Rage (•••, ••••, or •••••)
>   Packs have found a way to direct their Rage-filled members anger...
>   3 dots: Packmates suffering Wasu-Im act as if...
>   ...

# Set a merit
+groupmerit/set 5=Directed Rage:3
> Set Directed Rage to 3 dots for group 'Silver Fangs'

# View group merits
+groupmerit 5
> Merits for Silver Fangs (#5)
> 
> Den: •• (2)
> Territorial Advantage: ••• (3)
> Directed Rage: ••• (3)

# See member contributions
+groupmerit/calc 5
> Merit Contributions for Silver Fangs
> 
> Marcus: Totem 3
> Luna: Totem 3
```

### Example 3: Viewing a Pack with Totem

```
+group 5
> Silver Fangs (#5)
> Type: Pack
> Leader: Marcus
> 
> Description:
> A pack dedicated to hunting supernatural predators in the city.
> 
> Members:
>   Marcus - Alpha (Leader)
>   Luna - Tracker
> 
> Group Merits:
>   Den: •• (2)
>   Territorial Advantage: ••• (3)
>   Directed Rage: ••• (3)
> 
> Totem:
>   Silver Wind (Rank ••)
>   Swift storm spirit that guides the hunt
>   6 totem points from pack members
>   Pack Advantage: Specialty - Survival (Tracking)
```

---

## Notes for Staff

### Initializing Existing Groups

For existing groups that need the new merit/totem system:

1. Groups created after this update automatically have the new structure
2. Older groups may need attributes initialized - use `+group/sync` to update all groups

### Balancing Totem Points

Remember that totem points come from character sheets:
- Players must have the Totem merit on their character
- Use `+totem/calc <id>` to see current totals
- Staff can modify character merits with `+stat` commands

### Setting Member Merits

Players should have relevant merits on their sheets:
```
+stat/merit Marcus/Totem=3
+stat/merit Luna/Totem=3
```

### Group Types and Merits

Each group type has specific merits available:
- `pack` - Werewolf packs
- `krewe` - Geist krewes  
- `cult` - Mummy cults
- `cabal` - Mage mystery cults
- `conspiracy` - Hunter cells

Use `+groupmerit/list <type>` to see what's available.

---

## Technical Notes

### Data Storage

- Group merits: Stored in `group.db.merits` dictionary
- Totem data: Stored in `group.db.totem` dictionary
- Merit definitions: `PyReach/world/cofd/group_data.py`
- Numina definitions: Same file

### Merit Calculations

The system automatically:
- Pulls Totem merit from character sheets
- Calculates total totem points
- Determines rank from attributes
- Limits numina based on totem points
- Validates attribute distribution

### Adding New Merits

To add new group-specific merits, edit `group_data.py`:

```python
PACK_MERITS['New Merit'] = {
    'min': 1,
    'max': 5,
    'prerequisites': ['Pack'],
    'description': 'Description here',
    'source': 'Book Page'
}
```

### Adding New Numina

To add new numina, edit the `SPIRIT_NUMINA` dictionary in `group_data.py`.

---

## FAQ

**Q: Can players see totem information?**
A: Yes, anyone can use `+totem <id>` to view a pack's totem if they can view the group.

**Q: Who can modify group merits and totems?**
A: Staff and group leaders can modify merits and totems using the `/set` switches.

**Q: Does the totem advantage automatically apply?**
A: The advantage is recorded in the totem data. Staff/ST should apply it narratively or via character sheets.

**Q: Can we change totem attributes after setting them?**
A: Yes, use `+totem/attr` again with new values. Rank and derived stats recalculate automatically.

**Q: What happens if pack members lose Totem merit?**
A: Use `+totem/calc` to check current total. You may need to reduce attributes or numina if points decrease.

**Q: Can non-packs have totems?**
A: The totem system is primarily for packs. Other group types have different mechanics (coming soon).

