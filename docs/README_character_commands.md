# Character Sheet Commands Documentation

This document explains the enhanced character sheet system with UTF-8 support, biographical information, comprehensive pool tracking, and health management.

## Character Sheet Display (+sheet)

### Basic Usage
- `+sheet` - Display your own character sheet
- `+sheet <character>` - Display another character's sheet
- `+sheet/ascii` - Force ASCII display (no Unicode dots)

### UTF-8 Encoding Support

The sheet automatically detects if your client supports UTF-8 encoding and adjusts the display accordingly:

**UTF-8 Supported:** Uses Unicode dots (● ○)
**Non-UTF-8:** Uses ASCII characters (* -)

If your client doesn't support UTF-8, you'll see a warning with instructions on how to fix it:
- Set your MUD client to use UTF-8 encoding
- Use `option encoding=utf-8` command (if not logged in)
- Use `+sheet/ascii` for consistent ASCII display

### Sheet Layout

The sheet now displays information in organized sections with template-specific elements:

- **Bio**: Full Name, Birthdate, Concept, template, Virtue, Vice
- **Attributes**: Mental, Physical, Social (in columns)
- **Skills**: Mental, Physical, Social (in columns)  
- **Advantages**: Defense, Speed, Initiative, etc. (in columns)
  - Shows template-specific power stats when applicable (Kenning, Primal Urge, etc.)
- **Health**: Visual health boxes with damage tracking
- **Willpower**: Permanent/temporary tracking with dots
- **Other sections**: Anchors, Experience, Aspirations, Equipment

### template-Specific Features

The sheet adapts based on your character's template:
- **Changeling**: Shows Wyrd (if > 0)
- **Werewolf**: Shows Primal Urge (if > 0)
- **Vampire**: Shows Blood Potency (if > 0)
- **Mage**: Shows Gnosis (if > 0)
- **Geist**: Shows Synergy (if > 0)
- **Beast**: Shows Satiety (if > 0)
- **Deviant**: Shows Deviation (if > 0)
- **Demon**: Shows Primum (if > 0)
- **Promethean**: Shows Azoth (if > 0)
- **Hunter/Mortal/Mortal+**: Standard advantages only

### Derived Stats (Official Chronicles of Darkness)

The system automatically calculates derived stats according to official CofD rules:
- **Health**: Size + Stamina
- **Willpower**: Resolve + Composure  
- **Speed**: Strength + Dexterity + 5
- **Defense**: Lower of Wits or Dexterity (reflexive evasion)
- **Initiative**: Dexterity + Composure

## Bio Management (+stat)

### Overview
Character biographical information is managed through the `+stat` command, keeping all character data in one consistent system.

### Bio Fields
Bio information can be set using the standard stat command syntax:

**Universal Bio Fields:**
- **fullname** - Character's full name
- **birthdate** - Date of birth
- **concept** - Character concept/profession 

**template-Specific Bio Fields:**

**Mortal:** virtue, vice

**Mage (The Awakening):** virtue, vice, path, order
- Path: Acanthus, Mastigos, Moros, Obrimos, Thyrsus
- Order: Adamantine Arrow, Guardians of the Veil, Mysterium, Silver Ladder, Free Council, Seers of the Throne

**Vampire (The Requiem):** mask, dirge, clan, covenant
- Clan: Daeva, Gangrel, Mekhet, Nosferatu, Ventrue
- Covenant: Carthian Movement, Circle of the Crone, Invictus, Lancea et Sanctum, Ordo Dracul

**Werewolf (The Forsaken):** bone, blood, auspice, tribe
- Auspice: Cahalith, Elodoth, Irraka, Ithaeur, Rahu
- Tribe: Blood Talons, Bone Shadows, Hunters in Darkness, Iron Masters, Storm Lords, Ghost Wolves

**Changeling (The Lost):** virtue, vice, seeming, court, kith
- Seeming: Beast, Darkling, Elemental, Fairest, Ogre, Wizened
- Court: Spring, Summer, Autumn, Winter, Courtless

**Geist (The Sin-Eaters):** virtue, vice, burden, archetype, krewe
- Burden: Abiding, Bereaved, Hungry, Kindly, Vengeful
- Archetype: Advocate, Celebrant, Gatekeeper, Mourner, Necromancer, Pilgrim

**Promethean (The Created):** virtue, vice, lineage, refinement
- Lineage: Frankenstein, Galatea, Osiris, Tammuz, Ulgan
- Refinement: Aurum, Cuprum, Ferrum, Plumbum, Stannum

**Hunter (The Vigil):** virtue, vice, profession, organization, creed

**Demon (The Descent):** vice, incarnation, agenda, agency

**Beast (The Primordial):** virtue, vice, hunger, family, inheritance
- Hunger: Power, Prey, Punishment, Ruin, Secrets
- Family: Anakim, Eshmaki, Makara, Namtaru, Ugallu

**Deviant (The Renegades):** virtue, vice, origin, clade, divergence
- Origin: Cataclysm, Conspiracy, Contamination, Experiment, Invasive
- Clade: Chimeroid, Coactive, Invasive, Mutant, Neurode

**Staff-Only Fields:**
- **template** - Character's supernatural template

### Commands
- `+stat fullname=<value>` - Set full name
- `+stat birthdate=<value>` - Set birthdate  
- `+stat concept=<value>` - Set concept
- `+stat virtue=<value>` - Set virtue
- `+stat vice=<value>` - Set vice
- `+stat <template_field>=<value>` - Set template-specific field
- `+stat template=<value>` - Set template (staff only)
- `+stat/remove <field>` - Clear a bio field
- `+stat/list` - View all stats including bio

**Note**: Spaces in stat names are automatically converted to underscores (e.g., "full name" becomes "full_name"). Both formats work for input.

### Examples
```
+stat fullname=John Smith      # Set full name
+stat "full name"=John Smith   # Same as above (quotes optional)
+stat birthdate=March 15, 1985 # Set birthdate
+stat concept=Detective        # Set concept
+stat virtue=Justice           # Set virtue
+stat vice=Wrath               # Set vice
+stat "animal ken"=3           # Set animal ken skill (quotes optional)

# template-specific examples
+stat clan=Gangrel             # Vampire clan
+stat path=Obrimos             # Mage path
+stat auspice=Rahu             # Werewolf auspice
+stat seeming=Beast            # Changeling seeming
+stat burden=Hungry            # Geist burden

+stat template=Vampire           # Set template (staff only)
+stat/remove concept           # Clear concept field
+stat/list                     # View all character info
```

### Bio Display
Bio information appears in both the character sheet and the `+stat/list` output:

**Character Sheet:**
```
Full Name   : John Smith              template      : Vampire
Birthdate   : March 15, 1985          Virtue      : Justice
Concept     : Detective               Vice        : Wrath

Clan        : Gangrel                 Covenant    : Invictus
Mask        : Tough Cop               Dirge       : The Hunt
```

**Stat List:**
```
Bio:
  Full Name: John Smith
  Birthdate: March 15, 1985
  Concept: Detective
  template: Vampire
  Vampire Template:
    Clan: Gangrel
    Covenant: Invictus
    Mask: Tough Cop
    Dirge: The Hunt
  Missing Vampire fields: (none)
```

### template Validation
The system automatically validates:
- **Field Availability**: Only fields valid for your template can be set
- **Value Validation**: Certain fields (like Clan, Path, etc.) accept only specific values
- **Missing Field Tracking**: Shows which template fields you haven't set yet

Examples of validation:
```
+stat clan=Gangrel           # ✓ Valid (if Vampire)
+stat clan=Gangrel           # ✗ Error (if Mortal - clan not valid for Mortals)
+stat clan=InvalidClan       # ✗ Error (invalid clan name)
```

### Field Guidelines
- **Full Name**: Character's complete name (max 50 characters)
- **Birthdate**: Any format (recommended: Month Day, Year)
- **Concept**: Brief profession/role description (max 50 characters)
- **Virtue**: Highest moral principle (Justice, Fortitude, etc.)
- **Vice**: Greatest moral failing (Wrath, Greed, etc.)
- **template**: Supernatural type (determines available pools/stats)

## Pool Management (+pool)

### Overview
The pool system manages willpower (universal) and supernatural pools based on your character's template.

### Commands
- `+pool` - Show all available pools
- `+pool <pool>` - Show specific pool status
- `+pool/<pool>` - Show specific pool status
- `+pool/<pool>/spend [amount]` - Spend from pool (default: 1)
- `+pool/<pool>/gain [amount]` - Gain pool points (default: 1)
- `+pool/<pool>/set <current>/<max>` - Set pool values (staff only)
- `+pool/<pool>/reset` - Reset pool to maximum (staff only)

### Available Pools by template

**Universal:**
- **willpower** - Mental resilience (all characters)

**template-Specific:**
- **essence** - Werewolf spiritual energy (based on Primal Urge)
- **blood** - Vampire blood pool (based on Blood Potency)
- **glamour** - Changeling glamour (based on Wyrd)
- **mana** - Mage quintessence (based on Gnosis)
- **plasm** - Geist ectoplasm (based on Synergy)
- **satiety** - Beast hunger satisfaction
- **instability** - Deviant reality distortion (based on Deviation)
- **aether** - Demon occult matrix fuel (based on Primum)
- **pyros** - Promethean divine fire (based on Azoth)

### Pool Calculations
Supernatural pools use lookup tables based on power stat values:

**Standard Pool Calculation:**
- Power Stat 1: 10 points
- Power Stat 2: 11 points  
- Power Stat 3: 12 points
- Power Stat 4: 13 points
- Power Stat 5: 15 points
- Power Stat 6: 20 points
- Power Stat 7: 25 points
- Power Stat 8: 30 points
- Power Stat 9: 50 points
- Power Stat 10: 75 points

**Special Cases:**
- **Blood Potency 0**: Uses Stamina attribute value
- **Satiety**: Uses Satiety stat directly (not calculated)

### Examples
```
+pool                        # Show all available pools
+pool/willpower/spend 2      # Spend 2 willpower
+pool essence                # Check essence pool (werewolf)
+pool/blood/gain 3           # Gain 3 blood (vampire)
+pool/glamour                # Check glamour pool (changeling)
+pool/mana/set 15/20         # Set mana to 15/20 (staff)
+pool/essence/reset          # Reset essence to max (staff)
```

### Pool Display
Each pool shows current/maximum: `Essence: 25/30`
- Pools automatically initialize to maximum when first accessed
- Maximum values calculated from power stats using lookup tables
- Only pools available to your template are shown

## Health & Damage Management (+health)

### Commands
- `+health` - Show current health status
- `+health/damage <amount> [type]` - Take damage
- `+health/heal <amount> [type]` - Heal damage
- `+health/set <level> <type>` - Set specific health box (staff)
- `+health/clear` - Clear all damage (staff)
- `+health/max <amount>` - Set maximum health (staff)

### Damage Types
- **Bashing** (b): Represented by `/` (cyan) - bruises, fatigue
- **Lethal** (l): Represented by `X` (red) - cuts, bullets
- **Aggravated** (a): Represented by `*` (bright red) - fire, supernatural

### Examples
```
+health/damage 2 lethal       # Take 2 lethal damage
+health/damage 1              # Take 1 bashing damage (default)
+health/heal 1 bashing        # Heal 1 bashing damage
+health/set 3 aggravated      # Set health level 3 to aggravated (staff)
```

### Health Display
Health shows as boxes: `[ ][ ][/][X][*][ ]`
- `[ ]` = Healthy
- `|c/|n` = Bashing damage (cyan)
- `|rX|n` = Lethal damage (red)
- `|R*|n` = Aggravated damage (bright red)

### Damage Rules
1. Damage fills from left to right
2. More severe damage overwrites less severe:
   - Aggravated > Lethal > Bashing
3. When health track is full, character is incapacitated
4. Healing removes damage from right to left

## Staff Commands

### Bio Management (Builder+)
- `+stat <name>/template=<template>` - Set character's template
- `+stat <name>/fullname=<name>` - Set character's full name
- `+stat <name>/<field>=<value>` - Set any bio field for a character
- `+stat/remove <name>/<field>` - Remove any bio field from a character

### Pool Management (Builder+)
- `+pool/<pool>/set <current>/<max>` - Set pool values
- `+pool/<pool>/reset` - Reset pool to maximum

### Health Management (Builder+)
- `+health/set <level> <type>` - Set specific damage
- `+health/clear` - Remove all damage
- `+health/max <amount>` - Change maximum health

## Installation

The character sheet and bio system integrate with existing stat management. No special installation required beyond ensuring the character sheet and pool commands are available:

```python
# The +stat command handles bio management automatically
# Pool and health commands can be added via command sets as needed
```

## Data Storage

The system stores:

**Bio Information:**
- `caller.db.stats["bio"]["full_name"]` - Character's full name
- `caller.db.stats["bio"]["birthdate"]` - Date of birth
- `caller.db.stats["bio"]["concept"]` - Character concept
- `caller.db.stats["bio"]["virtue"]` - Character virtue
- `caller.db.stats["bio"]["vice"]` - Character vice
- `caller.db.stats["bio"]["<template_field>"]` - template-specific bio fields
- `caller.db.stats["other"]["template"]` - Character template

**template-Specific Bio Fields (examples):**
- `caller.db.stats["bio"]["clan"]` - Vampire clan
- `caller.db.stats["bio"]["covenant"]` - Vampire covenant  
- `caller.db.stats["bio"]["path"]` - Mage path
- `caller.db.stats["bio"]["order"]` - Mage order
- `caller.db.stats["bio"]["auspice"]` - Werewolf auspice
- `caller.db.stats["bio"]["tribe"]` - Werewolf tribe
- `caller.db.stats["bio"]["seeming"]` - Changeling seeming
- `caller.db.stats["bio"]["court"]` - Changeling court
- (and many more based on template)

**Pools:**
- `caller.db.willpower_current` - Current willpower points
- `caller.db.essence_current` - Current essence (werewolf)
- `caller.db.blood_current` - Current blood (vampire)
- `caller.db.glamour_current` - Current glamour (changeling)
- `caller.db.mana_current` - Current mana (mage)
- `caller.db.plasm_current` - Current plasm (geist)
- `caller.db.satiety_current` - Current satiety (beast)
- `caller.db.instability_current` - Current instability (deviant)
- `caller.db.aether_current` - Current aether (demon)
- `caller.db.pyros_current` - Current pyros (promethean)

**Stats:**
- `caller.db.health_damage` - Dictionary of damage by health level
- `caller.db.stats["advantages"]["willpower"]` - Maximum willpower
- `caller.db.stats["advantages"]["health"]` - Maximum health

**Power Stats:**
- `caller.db.stats["advantages"]["primal_urge"]` - Werewolf power stat
- `caller.db.stats["advantages"]["blood_potency"]` - Vampire power stat
- `caller.db.stats["advantages"]["wyrd"]` - Changeling power stat
- `caller.db.stats["advantages"]["gnosis"]` - Mage power stat
- `caller.db.stats["advantages"]["synergy"]` - Geist power stat
- `caller.db.stats["advantages"]["deviation"]` - Deviant power stat
- `caller.db.stats["advantages"]["primum"]` - Demon power stat
- `caller.db.stats["advantages"]["azoth"]` - Promethean power stat

## Compatibility

- Fully compatible with existing character sheet data
- Gracefully handles missing bio data (shows "<not set>")
- Gracefully handles missing pool data (defaults to max)
- Handles clients without UTF-8 support
- ASCII fallback ensures universal compatibility
- Only shows pools appropriate to character's template
- Automatically calculates supernatural pool maximums from power stats using lookup tables
- Bio fields are optional and can be set incrementally
- Proper Chronicle of Darkness supernatural pool calculations (not simple multiplication)
- Automatic space-to-underscore conversion in stat names for consistency
- Automatic cleanup of misplaced stats when viewing or setting character data 