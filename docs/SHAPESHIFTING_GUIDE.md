# Werewolf Shapeshifting System

## Overview

The shapeshifting system allows Werewolf: The Forsaken characters to transform between their five distinct forms, each with unique attributes, abilities, and tactical advantages. This system dynamically modifies character statistics and enforces restrictions to maintain game balance and lore accuracy.

## The Five Forms

### Hishu (Human Form)
**Default Form** - The natural camouflage among humanity.

- **Stat Modifiers:** None (base form)
- **Perception:** +1 die to Perception rolls using wolf senses
- **Special Abilities:**
  - **Sheep's Clothing:** Pursuers suffer Primal Urge penalty when tracking in crowds
- **Notes:** 
  - This is the only form in which characters can spend XP or use +stat
  - All werewolf characters default to Hishu form

### Dalu (Near-Man Form)
A hulking, powerful human hunter - 150% body mass.

- **Stat Modifiers:**
  - Strength +1
  - Stamina +1
  - Manipulation -1
  - Size +1
- **Perception:** +2 dice to Perception rolls using wolf senses
- **Special Abilities:**
  - **Teeth and Claws:** Unarmed attacks deal lethal damage
  - **Defense vs Firearms:** Apply Defense against Firearms attacks
  - **Lunacy:** +2 to Lunacy roll
  - **Badass Motherfucker:** Intimidate crowds with Presence + Primal Urge
- **Tactical Use:** Urban hunting, intimidation, maintaining some human interaction

### Gauru (War Form)
The devastating nightmare of legend - 400% body mass, 1.5x height.

- **Stat Modifiers:**
  - Strength +3
  - Dexterity +1
  - Stamina +2
  - Size +2
- **Perception:** +3 dice to Perception rolls using wolf senses
- **Special Abilities:**
  - **Regeneration:** Heal ALL bashing and lethal damage each turn
  - **Teeth and Claws:** +2L damage, +3 Initiative when using natural weapons
  - **Defense vs Firearms:** Apply Defense against Firearms attacks
  - **Lunacy:** -2 to Lunacy roll (more terrifying to witnesses)
  - **Rage:** Must attack an active opponent each turn or risk Kuruth (Death Rage)
  - **Primal Fear:** Lesser enemies forced to use Down and Dirty combat
- **CRITICAL WARNING:**
  - Limited duration: Stamina + Primal Urge turns
  - Must shift down to Dalu/Urshul or enter Kuruth when duration expires
  - Automatically fails Social rolls except Intimidation
  - Automatically fails Mental rolls except Perception and Resistance
- **Tactical Use:** Ending hunts/battles quickly, surviving killing blows

### Urshul (Near-Wolf Form)
A horse-sized dire wolf - 200% body mass.

- **Stat Modifiers:**
  - Strength +2
  - Dexterity +2
  - Stamina +2
  - Manipulation -1
  - Size +1
- **Perception:** +3 dice to Perception rolls using wolf senses
- **Speed Bonus:** +3 to Speed (species factor)
- **Special Abilities:**
  - **Teeth and Claws:** Claws +1L, Bite +2L
  - **Defense vs Firearms:** Apply Defense against Firearms attacks
  - **Lunacy:** Inflicts Lunacy on witnesses
  - **Weaken the Prey:** Apply Tilt (Arm Wrack/Leg Wrack/Knocked Down) once per scene without targeted attack
- **Communication:** Cannot speak with humans, but can use First Tongue
- **Tactical Use:** Harrying prey, wearing down opponents, setting up for Gauru kills

### Urhan (Wolf Form)
A normal wolf - blends seamlessly with wolf packs.

- **Stat Modifiers:**
  - Dexterity +2
  - Stamina +1
  - Manipulation -1
  - Size -1
- **Perception:** +4 dice to Perception rolls using wolf senses (best tracking form)
- **Speed Bonus:** +3 to Speed (species factor)
- **Special Abilities:**
  - **Teeth:** Bite attacks +1L damage
  - **Chase Down:** Spend 1 Essence to pre-empt actions in combat (replaces normal action)
  - **Enhanced Tracking:** Superior sensory abilities for tracking
  - **Foot Chase:** Uses Speed instead of Stamina + Athletics
- **Communication:** Cannot speak with humans, limited First Tongue (few simple words)
- **Tactical Use:** Long-distance travel, tracking, blending with nature

## Commands

### +shift <form>
Transform into the specified form.

```
+shift gauru    - Transform into Gauru (war form)
+shift hishu    - Return to human form
+shift urshul   - Transform into near-wolf form
+shift dalu     - Transform into near-man form
+shift urhan    - Transform into wolf form
```

**Notes:**
- Case-insensitive
- Shows stat changes and special abilities upon transformation
- Automatically recalculates derived stats (Health, Speed, Defense, Initiative)
- Announces transformation to the room

### +shift/list
Display all five forms with descriptions and your current form.

### +shift/info <form>
Show detailed information about a specific form including:
- Full description
- All stat modifiers
- Perception bonuses
- Special abilities
- Whether you're currently in that form

### +form
Quick reference to check your current form and active modifiers.

## System Mechanics

### Stat Tracking

#### Base Stats Storage
When you first shift from Hishu, the system stores your base (permanent) statistics:
- Strength
- Dexterity
- Stamina
- Manipulation
- Size

These base values are preserved and restored when you return to Hishu.

#### Temporary Modifiers
While in non-Hishu forms:
- Your displayed attributes show the modified values
- All rolls use the modified statistics
- Derived stats (Health, Speed, Defense, Initiative) automatically update
- Base stats remain safely stored

#### Returning to Hishu
When you shift back to Hishu:
- All temporary modifiers are removed
- Base stats are restored
- Derived stats recalculate based on permanent values

### Restrictions While Shifted

Characters in any form OTHER than Hishu CANNOT:
- Use `+stat` to modify statistics
- Use `+xp/spend` to raise attributes or skills
- Use `+xp/buy` to purchase merits

**Error Message:**
```
You cannot modify stats while in <Form> form. Use +shift hishu to return to human form first.
```

**Why?** 
Shapeshifting represents temporary physical changes, not permanent character development. Experience expenditure requires the character to be in their base human form to integrate permanent improvements.

### Derived Stat Calculations

The system automatically updates:

**Health** = Size + Stamina
- Increases in Dalu (+2), Gauru (+4), Urshul (+3)
- Decreases in Urhan (-1)

**Speed** = Strength + Dexterity + 5 (+ Species Factor for wolf forms)
- Significantly increases in Urshul and Urhan (+3 species factor)
- Increases in Gauru due to high Strength/Dexterity bonuses

**Defense** = Lower of (Wits, Dexterity)
- May increase in forms with Dexterity bonuses
- Can apply Defense vs Firearms in Dalu, Gauru, Urshul

**Initiative** = Dexterity + Composure
- Increases in forms with Dexterity bonuses
- Additional +3 in Gauru when using teeth/claws

### Harmony and Shifting (Lore Reference)

The source material notes that Harmony affects the shifting experience:

- **High Harmony (9-10):** Painful transformation, spend 1 Essence as instant action
- **Balanced Harmony:** Natural discomfort, feels "right"
- **Low Harmony:** Warm relief, must shift at least once per scene

*Note: The current system implementation does not enforce Harmony-based shifting restrictions or requirements. This can be added as future functionality.*

## Tactical Considerations

### Form Selection Strategy

**Use Hishu when:**
- Blending with humans
- Social interaction required
- Spending XP or modifying stats
- No immediate combat threat

**Use Dalu when:**
- Urban combat situations
- Need to intimidate without revealing full supernatural nature
- Balance of strength and human appearance needed
- Crowds present that can be manipulated

**Use Gauru when:**
- Ending combat immediately
- Facing overwhelming opposition
- Need maximum damage and regeneration
- Can afford to enter Death Rage if necessary

**Use Urshul when:**
- Need to harry and wear down prey
- Setting up for Gauru kill
- Applying debilitating Tilts
- Balance of speed and combat power

**Use Urhan when:**
- Long-distance pursuit
- Tracking prey
- Need maximum stealth in wilderness
- Escaping through natural terrain
- Pre-empting enemy actions

### Combat Applications

**Opening Moves:**
- Urhan for Chase Down ability
- Dalu for intimidation + combat capability
- Gauru if immediate overwhelming force needed

**Sustained Combat:**
- Urshul for wearing down multiple enemies
- Gauru only when ready to end fight (limited duration!)

**Pursuit:**
- Urhan for speed and tracking
- Urshul for speed + combat readiness

**Defense:**
- Gauru for regeneration
- Urshul/Dalu for speed to escape
- Hishu to blend into crowds

## Integration with Other Systems

### Combat System
- Form bonuses apply to all combat rolls
- Natural weapons (teeth/claws) available in non-Hishu forms
- Special combat abilities (Weaken the Prey, Primal Fear) automatically considered

### Character Sheet (+sheet)
- Displays current form if not Hishu
- Shows modified attributes
- Shows updated derived stats
- Indicates which stats are temporary

### Health and Damage
- Health pool increases/decreases with form
- Existing damage remains proportionally
- Gauru regeneration is separate system (heals per turn in that form)

### Equipment and Inventory
- Clothing and most equipment destroyed by shift (lore-accurate)
- Fetishes and dedicated items typically survive transformation
- *Note: Current implementation doesn't enforce equipment destruction*

## Staff Administration

### Checking Character Form
```python
character.db.current_form  # Returns form name (e.g., "gauru")
character.db.base_attributes  # Dict of stored base stats
character.db.base_size  # Stored base size
```

### Forcing Form Change
Staff can manually adjust forms if needed:
```python
character.db.current_form = "hishu"  # Set to Hishu
character.calculate_derived_stats()  # Recalculate stats
```

### Resetting Form Data
If form data becomes corrupted:
```python
# Reset to Hishu and clear form data
character.db.current_form = "hishu"
character.db.base_attributes = None
character.db.base_size = None
# Then have player re-shift to reinitialize
```

## Troubleshooting

### "I can't use +stat!"
**Solution:** Check your current form with `+form`. If you're not in Hishu, use `+shift hishu` first.

### "My stats seem wrong after shifting"
**Solution:** 
1. Check your current form with `+form`
2. Shift back to Hishu with `+shift hishu`
3. Use `+recalc` to recalculate derived stats
4. If problem persists, contact staff

### "I shifted and my equipment disappeared"
**Expected Behavior:** In lore, non-magical equipment typically doesn't survive transformation. However, the current system doesn't automatically enforce this. Roleplay accordingly.

### "How long can I stay in Gauru?"
Your Gauru duration is Stamina + Primal Urge turns. Check your stats:
- Stamina: From `+sheet`
- Primal Urge: From `+sheet`
- Duration: Sum of these values (in turns)

After this duration, you MUST shift to another form or enter Death Rage.

## Future Enhancements

Potential additions to the system:

1. **Essence Cost:** Implement Essence expenditure for shifting (1 Essence per shift at Harmony 9-10)
2. **Harmony Integration:** Enforce Harmony-based shifting requirements and discomfort
3. **Gauru Duration Tracking:** Automatic turn counter for Gauru form with warnings
4. **Equipment Handling:** Automatic equipment destruction on shift (except fetishes)
5. **First Tongue:** Special communication channel for wolf forms
6. **Lunacy System:** Automatic Lunacy rolls for nearby humans when shifting
7. **Death Rage (Kuruth):** Implement full Death Rage mechanics
8. **Visual Effects:** Enhanced room announcements with form-specific descriptions

## Source Material

Based on **Werewolf: The Forsaken 2nd Edition** from Chronicles of Darkness.

Key concepts:
- Five sacred forms of the Uratha
- Temporary physical transformation
- Each form serves specific tactical purpose
- Hishu as "default" is misnomer - all forms are natural
- Shapeshifting is painful but natural to werewolves

## Developer Notes

### File Location
`PyReach/commands/shapeshifting.py`

### Key Functions

**can_modify_stats_while_shifted(character)**
- Returns: `(bool, str)` - can modify, reason message
- Used by: `+stat`, `+xp/spend`, `+xp/buy`
- Purpose: Prevent stat modification while shifted

**WEREWOLF_FORMS**
- Dictionary containing all form definitions
- Each form has: display_name, description, stat modifiers, special abilities
- Easy to modify for balance adjustments

### Integration Points
- `commands/stats.py`: Checks form before allowing +stat
- `commands/experience.py`: Checks form before allowing +xp/spend and +xp/buy
- `commands/default_cmdsets.py`: Registers commands in CharacterCmdSet
- `typeclasses/characters.py`: Character.calculate_derived_stats() automatically updates

### Testing Checklist
- [ ] Werewolf can shift between all five forms
- [ ] Non-werewolves get appropriate error message
- [ ] Stats correctly modified for each form
- [ ] Derived stats recalculate on shift
- [ ] Returning to Hishu restores base stats
- [ ] Cannot use +stat while shifted (except Hishu)
- [ ] Cannot use +xp/spend while shifted (except Hishu)
- [ ] Cannot use +xp/buy while shifted (except Hishu)
- [ ] +form shows current form correctly
- [ ] +shift/list shows all forms
- [ ] +shift/info provides detailed information
- [ ] Room announcements work
- [ ] Multiple shifts in succession work correctly

## Contact

For bugs, balance concerns, or feature requests related to shapeshifting, contact the development team or your local Storyteller.

