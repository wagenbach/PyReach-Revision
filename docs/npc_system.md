# NPC System Documentation

NPC (Non-Player Character) system for creating, managing, and controlling NPCs with character sheet support and random generation.

## Overview

NPCs in this system:
- Use the same character sheet system as player characters
- Can be puppeted (controlled) by their creator, authorized controllers, or staff
- Support random generation based on archetypes and templates
- Have different power levels (minor, standard, major, boss)
- Can participate in all game systems (combat, social, investigation, etc.)

## Basic NPC Commands

### Creating NPCs

#### Basic Creation (Manual Stats)
```
+npc/create <name> <type>
```
Creates a basic NPC that you can then manually set stats for using `+stat` commands.

**Examples:**
```
+npc/create "City Guard" standard
+npc/create "Vampire Primogen" major
+npc/create "Ancient Evil" boss
```

#### Generated Creation (Random Stats)
```
+npc/generate <name> <archetype> [type]
```
Creates an NPC with randomly generated stats based on the specified archetype.

**Examples:**
```
+npc/generate "Street Thug" mortal_tank
+npc/generate "Vampire Elder" vampire_social boss
+npc/generate "Werewolf Alpha" werewolf_tank major
+npc/generate "Corporate Spy" mortal_dex
```

### Managing NPCs

#### Viewing NPCs
```
+npc/list                    # List all NPCs in current location
+npc/stats <npc>            # View NPC's character sheet
+npc/archetypes             # List all available archetypes
+npc/archetypes <template>  # List archetypes for specific template
```

#### Controlling NPCs
```
+npc/control <npc>          # Add yourself as an NPC controller
+npc/release <npc>          # Remove yourself as an NPC controller
```

#### Puppeting NPCs
```
+npc/puppet <npc>           # Start puppeting an NPC
+npc/unpuppet               # Stop puppeting and return to your character
```

#### Health Management
```
+npc/damage <npc> <amount> [type]    # Apply damage (bashing/lethal/aggravated)
+npc/heal <npc> <amount> [type]      # Heal damage
```

#### Destruction
```
+npc/destroy <npc>          # Destroy an NPC (staff only)
```

## NPC Types

NPCs come in different power levels that affect their stat generation:

### Minor NPCs
- **Use Case:** Crowds, basic minions, simple encounters
- **Stats:** Lower attribute and skill values
- **Examples:** Street thugs, security guards, civilians

### Standard NPCs
- **Use Case:** Regular antagonists, supporting characters
- **Stats:** Balanced attribute and skill distribution
- **Examples:** Police officers, gang members, skilled mortals

### Major NPCs
- **Use Case:** Important story characters, recurring antagonists
- **Stats:** Enhanced attributes and skills
- **Examples:** Vampire elders, werewolf alphas, experienced mages

### Boss NPCs
- **Use Case:** Major antagonists, legendary beings
- **Stats:** Exceptional capabilities, special abilities
- **Examples:** Ancient vampires, powerful demons, legendary creatures

## Archetypes

Archetypes determine how an NPC's stats are distributed. Each archetype focuses on different aspects:

### Mortal Archetypes

#### MortalTank
- **Focus:** Physical resilience and combat durability
- **Primary Stats:** Stamina, Strength, Composure
- **Skills:** Athletics, Brawl, Intimidation
- **Description:** Tough fighters focused on taking and dealing damage

#### MortalDex
- **Focus:** Speed, agility, and precision
- **Primary Stats:** Dexterity, Wits, Composure
- **Skills:** Athletics, Firearms, Larceny
- **Description:** Quick combatants focused on speed and accuracy

#### MortalSocial
- **Focus:** Social manipulation and charisma
- **Primary Stats:** Presence, Manipulation, Composure
- **Skills:** Persuasion, Subterfuge, Socialize
- **Description:** Charismatic individuals skilled in social interaction

#### MortalMental
- **Focus:** Knowledge, investigation, and intellect
- **Primary Stats:** Intelligence, Wits, Resolve
- **Skills:** Investigation, Science, Medicine
- **Description:** Intellectuals focused on knowledge and problem-solving

### Vampire Archetypes

#### VampireTank
- **Focus:** Fortitude and physical combat
- **Disciplines:** Fortitude (primary), Potence, Presence
- **Description:** Vampire warriors focused on physical dominance

#### VampireDex
- **Focus:** Celerity and precision
- **Disciplines:** Celerity (primary), Obfuscate, Potence
- **Description:** Vampire assassins focused on speed and stealth

#### VampireSocial
- **Focus:** Presence and social dominance
- **Disciplines:** Presence (primary), Dominate, Majesty
- **Description:** Vampire manipulators focused on social control

#### VampireMental
- **Focus:** Auspex and mental powers
- **Disciplines:** Auspex (primary), Obfuscate, Animalism
- **Description:** Vampire scholars focused on mental abilities

### Werewolf Archetypes

#### WerewolfTank
- **Focus:** Endurance and pack leadership
- **Gifts:** Endurance (primary), Strength, Dominance
- **Description:** Werewolf warriors focused on pack protection

## Permissions System

### NPC Creation
- **Who:** Staff members only can create NPCs
- **Note:** Created NPCs are automatically assigned the creator

### NPC Control
NPCs can be controlled by:
1. **Creator:** The character who created the NPC
2. **Controllers:** Characters explicitly given control permissions
3. **Staff:** Always have full control over all NPCs

### Stat Modification
- **NPCs:** Can be modified by their controllers and staff
- **Player Characters:** Can only be modified by staff (except when unapproved)

### Puppeting
NPCs can be puppeted by anyone with control permissions, allowing them to:
- Act as the NPC in roleplay
- Use the NPC's abilities and stats
- Participate in scenes as the NPC

## Stat Management

NPCs use the same stat system as player characters:

### Setting Stats
```
+stat <npc>/<stat>=<value>     # Set any stat on an NPC
+stat strength=3               # Set your own stat (if puppeting)
```

### Viewing Stats
```
+stat/list <npc>               # View NPC's full character sheet
+npc/stats <npc>              # Alternative command
```

### Specialties and Merits
NPCs can have specialties and merits just like player characters:
```
+stat <npc>/specialty/athletics=Running
+stat <npc>/contacts=3
```

## Advanced Features

### Template Support
NPCs support all the same templates as player characters:
- Mortal, Vampire, Werewolf, Mage, Changeling, etc.
- Template-specific bio fields are automatically handled
- Integrity names adjust based on template (Humanity for Vampires, etc.)

### Health Tracking
NPCs use the same advanced health system:
- Separate tracking for bashing, lethal, and aggravated damage
- Automatic incapacitation when health is exceeded
- Healing supports specific damage types

### Integration
NPCs fully integrate with other game systems:
- **Combat:** Can participate in combat scenes
- **Social:** Can be targets of social maneuvering
- **Investigation:** Can provide clues and information
- **Experience:** Track experience and advancement (if desired)

## Examples

### Creating a Vampire Nightclub Owner
```
+npc/generate "Marcus Vein" vampire_social major
+stat "Marcus Vein"/template=Vampire
+stat "Marcus Vein"/clan=Toreador
+stat "Marcus Vein"/covenant=Carthian Movement
+stat "Marcus Vein"/concept=Nightclub Owner
+stat "Marcus Vein"/resources=4
+stat "Marcus Vein"/contacts=3
```

### Creating a Werewolf Pack Leader
```
+npc/generate "Thunder Claw" werewolf_tank boss
+stat "Thunder Claw"/template=Werewolf
+stat "Thunder Claw"/auspice=Rahu
+stat "Thunder Claw"/tribe=Iron Masters
+stat "Thunder Claw"/concept=Pack Alpha
```

### Basic Mortal Security Guard
```
+npc/generate "Security Guard" mortal_tank minor
+stat "Security Guard"/concept=Corporate Security
+stat "Security Guard"/specialty/athletics=Running
+stat "Security Guard"/specialty/firearms=Pistols
```

## Tips for Storytellers

1. **Use Appropriate Types:** Match NPC type to their story importance
2. **Choose Fitting Archetypes:** Pick archetypes that match the NPC's role
3. **Set Control Permissions:** Give players control of recurring NPCs they should influence
4. **Use Puppeting Sparingly:** Puppet important NPCs for key scenes
5. **Track Important NPCs:** Use the stat system to track NPC advancement and changes

## Troubleshooting

### Common Issues

**"Permission denied" when trying to control an NPC:**
- Make sure you have control permissions (`+npc/control <npc>`)
- Check if you're the creator or have staff permissions

**"Cannot puppet - already puppeting":**
- Use `+npc/unpuppet` or `unpuppet` to return to your character first

**"Archetype not found":**
- Check available archetypes with `+npc/archetypes`
- Ensure spelling matches exactly (use underscores: `vampire_tank`)

**NPC stats not calculating properly:**
- Use `+recalc <npc>` to recalculate derived stats
- Ensure all required attributes are set for proper calculation

Creates mechanically-sound NPCs for Chronicles of Darkness stories. 