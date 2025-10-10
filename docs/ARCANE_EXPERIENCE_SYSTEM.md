# Arcane Experience System (Mage: The Awakening)

## Overview

Mages in Chronicles of Darkness have a unique advancement system called **Arcane Experience**, which works alongside the regular Experience system. Arcane Experience represents magical understanding and mastery gained through interaction with the supernatural and magical practice.

## Key Concepts

### Dual Experience Systems

Mages track TWO types of experience:

1. **Regular Beats/Experience** - Used for mundane traits (attributes, skills, merits)
2. **Arcane Beats/Arcane Experience** - Used for magical advancement (arcana, gnosis, wisdom, praxes)

Both systems work the same way: **5 Beats = 1 Experience**

### Arcane Experience Uses

Some abilities can be purchased with **EITHER** regular XP or Arcane XP:
- Arcanum (to limit): 4 XP per dot
- Arcanum (above limit): 5 XP per dot
- Gnosis: 5 XP per dot
- Rotes: 1 XP
- Legacy Attainments (with tutor): 1 XP

Some abilities **MUST** be purchased with Arcane XP only:
- **Praxis**: 1 Arcane XP (mandatory)
- **Wisdom**: 2 Arcane XP per dot (mandatory)
- **Legacy Attainments (without tutor)**: 1 Arcane XP (mandatory)

## Earning Arcane Beats

Mages earn Arcane Beats through magical practice and supernatural interaction. Like regular Beats, each category can only award one Beat per scene.

### Arcane Beat Sources

| Source | Description | Command |
|--------|-------------|---------|
| **Obsession** | Fulfill or make major headway into an Obsession | `+xp/arcane obsession` |
| **Magical Condition** | Resolve a Condition from spellcasting, Paradox, or magical effect (does not include letting it expire) | `+xp/arcane magical_condition` |
| **Spell Dramatic Failure** | Voluntarily make a spellcasting roll a dramatic failure | `+xp/arcane spell_dramatic_failure` |
| **Act of Hubris** | Risk an Act of Hubris against Wisdom | `+xp/arcane act_of_hubris` |
| **Legacy Tutoring** | Spend a scene being tutored in a Legacy or tutoring students | `+xp/arcane legacy_tutoring` |
| **Supernatural Encounter** | Have a meaningful and new encounter with the supernatural (Storyteller discretion) | `+xp/arcane supernatural_encounter` |

### Obsessions

Mages set their Obsessions on their mage character sheet:
```
+stat/mage obsession=Understand the digital realm
```

Mages can have up to 3 Obsessions (1 short-term, 2 long-term). When you fulfill or make major headway into an Obsession, you earn an Arcane Beat.

## Commands

### Viewing Experience

```
+xp                    - View all experience (regular and arcane for mages)
```

**Example Output for Mages:**
```
Experience Summary
----------------------------------------
Beats: 3
Experience Points: 5
(5 beats = 1 experience point)

Mage Arcane Experience:
----------------------------------------
Arcane Beats: 4
Arcane Experience: 2
(5 arcane beats = 1 arcane experience)

Use +xp/arcane <source> to add arcane beats
Use +xp/costs/arcane to see arcane XP costs
```

### Adding Arcane Beats

```
+xp/arcane <source>    - Add an arcane beat (Mages only)
```

**Examples:**
```
+xp/arcane obsession                    - Fulfilled an Obsession
+xp/arcane magical_condition            - Resolved a magical Condition
+xp/arcane spell_dramatic_failure       - Made spellcasting a dramatic failure
+xp/arcane act_of_hubris                - Risked an Act of Hubris
+xp/arcane legacy_tutoring              - Tutored/was tutored in Legacy
+xp/arcane supernatural_encounter       - Meaningful supernatural encounter
```

### Spending Arcane Experience

```
+xp/spend/arcane <stat>=<dots>    - Spend arcane XP on mage abilities
```

**Examples:**
```
+xp/spend/arcane forces=3          - Raise Forces arcanum to 3 dots
+xp/spend/arcane death=2           - Raise Death arcanum to 2 dots
+xp/spend/arcane gnosis=2          - Raise Gnosis to 2 dots (grants 1 free praxis!)
+xp/spend/arcane wisdom=8          - Raise Wisdom to 8 dots
```

### Buying Praxes

Praxes MUST be purchased with Arcane XP (1 Arcane XP each):
```
+stat/mage praxis=<spell_name>     - Learn a praxis (costs 1 Arcane XP if beyond free)
```

**Examples:**
```
+stat/mage praxis=telekinesis      - Learn Telekinesis as a praxis
+stat/mage praxis=create locus     - Learn Create Locus as a praxis
```

**Note:** You get 1 free praxis per Gnosis dot. Additional praxes cost 1 Arcane XP each.

### Viewing Costs

```
+xp/costs              - Show regular experience costs
+xp/costs/arcane       - Show arcane experience costs (Mages only)
```

## Experience Cost Tables

### Regular Experience Costs

| Trait | Cost |
|-------|------|
| Attributes | 4 XP per dot |
| Skills | 2 XP per dot |
| Merits | 1 XP per dot |
| Integrity | 2 XP per dot |
| Specialties | 1 XP each |

### Arcane Experience Costs (Mages)

| Trait | Cost | Currency Options |
|-------|------|------------------|
| Arcanum (to limit) | 4 XP per dot | Regular XP OR Arcane XP |
| Arcanum (above limit) | 5 XP per dot | Regular XP OR Arcane XP |
| Gnosis | 5 XP per dot | Regular XP OR Arcane XP |
| Rote | 1 XP | Regular XP OR Arcane XP |
| **Praxis** | **1 Arcane XP** | **Arcane XP ONLY** |
| **Wisdom** | **2 Arcane XP per dot** | **Arcane XP ONLY** |
| Legacy Attainment (tutored) | 1 XP | Regular XP OR Arcane XP |
| **Legacy Attainment (untutored)** | **1 Arcane XP** | **Arcane XP ONLY** |

**Notes:**
- Arcanum limit = Gnosis + 5 (for ruling arcana)
- Increasing Gnosis grants 1 free Praxis
- Willpower increases automatically when Composure or Resolve increase (cost to rebuy spent Willpower: 1 XP per dot)

## Mage Character Sheet

View your mage-specific details including Obsessions, Praxes, and Nimbus:
```
+sheet/mage            - Display mage-specific character sheet
+sheet/mage/ascii      - Display mage sheet in ASCII mode
```

## Example Progression

### Starting Mage
- Gnosis 1 = 1 free praxis
- 0 Arcane Beats, 0 Arcane Experience

### After First Story Arc
Earned Arcane Beats:
- Fulfilled Obsession: 1 Arcane Beat
- Resolved magical Condition: 1 Arcane Beat
- Risked Act of Hubris: 1 Arcane Beat
- Tutored in Legacy: 1 Arcane Beat
- Supernatural encounter: 1 Arcane Beat

**Total: 5 Arcane Beats = 1 Arcane Experience**

### Spending Arcane Experience
```
+xp/spend/arcane forces=2          - Spend 4 Arcane XP (need more beats!)
```

Continue earning Arcane Beats until you have enough Arcane Experience to advance your magical abilities!

## Staff Commands

Staff can award Arcane Beats and Arcane Experience directly:

```
+xp/award <character>=<amount>              - Award regular XP
+xp/award/arcane <character>=<amount>       - Award Arcane XP (staff only)
```

## Integration with Character Approval

- **Unapproved Characters**: Can set praxes freely (with warnings about future costs)
- **Approved Characters**: Must spend Arcane XP to learn praxes beyond free ones
- Both systems work seamlessly with the existing character approval workflow

## Related Documentation

- See `MYSTERY_SYSTEM_SUMMARY.md` for Condition resolution mechanics
- See `mage.py` template for Mage-specific bio fields and validation
- See `experience.py` for the full experience handler implementation

## Technical Implementation

The Arcane Experience system is implemented in:
- `pyreach/world/experience.py` - ExperienceHandler class with arcane beat/XP tracking
- `PyReach/commands/experience.py` - CmdExperience command with arcane switches
- `PyReach/world/cofd/templates/mage.py` - Mage template with praxis cost handling

All arcane experience data is stored in character attributes:
- `arcane_beats` - Current arcane beats (0-4)
- `arcane_experience` - Current arcane experience (accumulated)
- `fractional_arcane_beats` - Partial beats for fine-grained awards

