# Game Systems Documentation

Complete reference for all game mechanics and systems in PyReach Chronicles of Darkness.

## Table of Contents

1. [Combat System](#combat-system)
2. [Experience & Advancement](#experience--advancement)
3. [Merit System](#merit-system)
4. [Mystery & Investigation](#mystery--investigation)
5. [Equipment & Purchasing](#equipment--purchasing)
6. [Conditions & Tilts](#conditions--tilts)
7. [Social Maneuvering](#social-maneuvering)
8. [Storyteller System](#storyteller-system)
9. [Language System](#language-system)
10. [Legacy Mode](#legacy-mode)

---

## Combat System

### Overview
Comprehensive Chronicles of Darkness 2nd Edition combat system with automated mechanics and narrative flexibility.

### Quick Start
1. `+combat/join [team]` - Join combat
2. `+combat/init` - Roll initiative
3. `+combat/status` - Check status
4. `+combat/attack <target>` - Attack
5. `+combat/next` - Advance turns
6. `+combat/surrender` or `+combat/leave` - Exit

---

### Core Mechanics

#### Initiative System
- **Calculation:** Initiative Stat (Dex + Composure) + 1d10 + modifiers
- **Order:** Highest initiative acts first each turn
- **Re-rolling:** New initiative each scene

#### Action Types
- **Instant Actions:** Standard actions that take one turn (most combat actions)
- **Reflexive Actions:** Quick actions that don't consume turn (movement up to Speed)
- **Extended Actions:** Complex actions requiring multiple turns

#### Multiple Actions
- Each additional action has cumulative penalty
- 1st action: No penalty
- 2nd action: -1 penalty
- 3rd action: -2 penalty, etc.

---

### Attack Resolution

**Attack Roll Steps:**
1. Calculate Attack Pool: Attribute + Skill (varies by weapon)
2. Apply Modifiers: Multiple action penalties, situational modifiers
3. Subtract Defense: Target's Defense rating (min 1 die remains)
4. Roll Dice: Count successes (8+ on d10, 10s count as 2)
5. Calculate Damage: Successes + weapon damage rating
6. Apply Armor: Subtract armor rating from damage
7. Apply to Health: Use health system for damage tracking

**Defense Calculation:**
- Formula: min(Wits, Dexterity) + Athletics
- Modifiers: Status effects, cover, prone, etc.

---

### Team System

#### Team Management
- **Auto-Assignment:** Players automatically balanced across teams
- **Manual Assignment:** `+combat/join <team>` to specify team
- **Team Changes:** `+combat/team <number>` to switch teams
- **Team Display:** Teams shown in `+combat/status` and `+combat/teams`

#### Team Rules
- **Friendly Fire Prevention:** Same-team allies cannot attack each other
- **Attack Blocking:** All attack commands check team affiliation
- **Grapple Prevention:** Team members cannot grapple each other
- **Visual Identification:** Team numbers color-coded in displays

---

### Surrender System

#### How Surrender Works
1. **Offer Surrender:** Any team member offers surrender for entire team
2. **Team Consensus:** All team members must agree (use `+combat/surrender`)
3. **Enemy Response:** Opposing teams can accept or decline
4. **Combat Resolution:** Accepted surrender immediately ends combat

#### Surrender Commands
- `+combat/surrender` - Offer surrender for your team
- `+combat/accept <team>` - Accept surrender from specified team
- `+combat/decline <team>` - Decline surrender from specified team

#### Strategic Considerations
- Tactical retreat for losing battles
- Story-driven combat resolution
- Training scenarios and sparring
- Roleplay opportunities and character development

---

### Weapon System

#### Weapon Categories

**Unarmed Combat:**
- Unarmed: No damage bonus, bashing damage
- Brass Knuckles: No damage bonus, bashing, Size 1

**Melee Weapons - Bludgeoning:**
- Club: +2 damage, bashing, Size 2
- Baseball Bat: +2 damage, bashing, Size 3
- Crowbar: +2 damage, bashing, Size 2
- Mace: +3 damage, bashing, Size 2

**Melee Weapons - Bladed:**
- Knife/Dagger: +1 damage, lethal, Size 1
- Sword: +3 damage, lethal, Size 2
- Machete: +2 damage, lethal, Size 2
- Axe: +3 damage, lethal, Size 2

**Ranged Weapons:**
- Bow: +2 damage, lethal, 50 yard range
- Crossbow: +3 damage, lethal, 80 yard range
- Throwing Knife: +1 damage, lethal, Str+Dex range

**Firearms:**
- Light Pistol: +1 damage, lethal, 20 yard range, 7 rounds
- Heavy Pistol: +2 damage, lethal, 30 yard range, 8 rounds
- Hunting Rifle: +4 damage, lethal, 200 yard range, 5 rounds
- Assault Rifle: +3 damage, lethal, 150 yard range, 30 rounds, autofire
- Shotgun: +3 damage, lethal, 20 yard range, 6 rounds

---

### Combat Modifiers

#### Attack Modifiers
- **All-Out Attack:** +2 to attack, lose Defense
- **Charge:** +1 damage, requires movement
- **Specified Target:** Additional difficulty based on location
- **Multiple Targets:** Cumulative penalties for each target
- **Aiming:** +1 per turn spent aiming (max +3)

#### Defensive Modifiers
- **Dodge:** Double Defense, lose next action
- **Full Dodge:** Dodge for entire turn
- **Block:** +2 Defense vs one attacker
- **Cover:** +1 to +4 Defense based on cover rating

#### Environmental Modifiers (Staff Only)
- Darkness, weather, terrain
- Set with `+combat/environment <condition> <value>`

---

### Damage and Health

#### Damage Types
- **Bashing (/):** Bruises, fatigue - cyan in display
- **Lethal (X):** Cuts, bullets - red in display
- **Aggravated (*):** Fire, supernatural - bright red in display

#### Damage Rules
1. Damage fills left to right
2. More severe damage overwrites less severe (Aggravated > Lethal > Bashing)
3. When health track is full, character is incapacitated
4. Healing removes damage right to left

#### Health Management
- **View Health:** `+combat/health [target]`
- **Apply Damage:** `+combat/damage <target>=<amount>/<type>` (staff)
- **Heal Damage:** `+combat/heal <target>=<amount>/<type>` (staff)

---

## Experience & Advancement

### Regular Experience System

#### Beats and Experience
- **5 Beats = 1 Experience Point**
- Beats automatically convert to XP

#### Beat Sources
Players earn beats from valid sources (one per scene per category):
- **dramatic_failure** - Voluntary dramatic failure
- **exceptional_success** - Exceptional success on roll
- **conditions** - Resolving conditions
- **aspirations** - Fulfilling aspirations
- **story** - Major story developments
- **scene** - Participating in scenes
- **session** - Attending game sessions
- **roleplay** - Exceptional roleplay
- **challenge** - Overcoming challenges
- **sacrifice** - Character sacrifices
- **discovery** - Discovering important information
- **relationship** - Relationship development
- **consequence** - Accepting consequences
- **learning** - Learning new things
- **growth** - Character growth

#### Experience Costs
| Trait | Cost |
|-------|------|
| Attributes | 4 XP per dot |
| Skills | 2 XP per dot |
| Merits | 1 XP per dot |
| Integrity | 2 XP per dot |
| Specialties | 1 XP each |

#### Commands
```
+xp                          - View experience summary
+xp/beat <source>            - Add a beat
+xp/spend <stat>=<dots>      - Spend XP on attributes/skills
+xp/costs                    - Show XP costs
```

---

### Arcane Experience System (Mages Only)

#### Dual Experience Tracking
Mages track **two** types of experience:
1. **Regular Beats/Experience** - For mundane traits
2. **Arcane Beats/Arcane Experience** - For magical advancement

Both systems: **5 Beats = 1 Experience**

#### Arcane Experience Uses

**Can use EITHER Regular XP OR Arcane XP:**
- Arcanum (to limit): 4 XP per dot
- Arcanum (above limit): 5 XP per dot
- Gnosis: 5 XP per dot
- Rotes: 1 XP

**MUST use Arcane XP (mandatory):**
- **Praxis:** 1 Arcane XP
- **Wisdom:** 2 Arcane XP per dot
- **Legacy Attainments (without tutor):** 1 Arcane XP

#### Earning Arcane Beats
| Source | Description |
|--------|-------------|
| **Obsession** | Fulfill or make major headway into an Obsession |
| **Magical Condition** | Resolve a Condition from spellcasting or Paradox |
| **Spell Dramatic Failure** | Voluntarily make spellcasting roll a dramatic failure |
| **Act of Hubris** | Risk an Act of Hubris against Wisdom |
| **Legacy Tutoring** | Tutor or be tutored in Legacy |
| **Supernatural Encounter** | Meaningful encounter with supernatural (ST discretion) |

#### Commands
```
+xp/arcane <source>          - Add arcane beat
+xp/spend/arcane <stat>=<dots> - Spend arcane XP
+xp/costs/arcane             - Show arcane XP costs
+stat/mage praxis=<spell>    - Learn praxis (1 Arcane XP)
```

**Note:** You get 1 free praxis per Gnosis dot. Additional praxes cost 1 Arcane XP each.

---

### Voting System

#### Vote and Recommend
Players can vote for and recommend each other for beats/XP.

```
+vote <player>=<reason>      - Vote for a player
+recommend <player>=<reason> - Recommend a player (stronger)
+vote/check                  - Check your vote cooldowns
```

**Default Settings (Voting Mode):**
- Vote cooldown: 168 hours (1 week)
- Recommendation cooldown: 168 hours (1 week)
- Beats per vote: 0.5
- Beats per recommendation: 1.0

#### Weekly Beats Mode
Alternative to voting system - automatic weekly beat distribution.

**Staff Configuration:**
```
+voteadmin/mode weekly       - Switch to weekly beats mode
+voteadmin/set weekly_beats_amount=5
+voteadmin/set weekly_beats_day=sunday
+voteadmin/set weekly_beats_time=00:00
+voteadmin/distribute        - Force distribution
+voteadmin/script start      - Start automation script
```

---

## Merit System

### Overview
Complete Chronicles of Darkness merit database with prerequisite validation and XP integration.

### Merit Categories

#### Mental Merits
Cognitive advantages and intellectual capabilities:
- Area of Expertise
- Common Sense
- Danger Sense
- Eidetic Memory
- Fast Reflexes
- Professional Training

#### Physical Merits
Physical advantages and capabilities:
- Ambidextrous
- Fleet of Foot
- Hardy
- Iron Stamina
- Quick Draw

#### Social Merits
Social connections and advantages:
- Allies
- Contacts
- Fame
- Resources
- Status
- Striking Looks

#### Fighting/Style Merits
Combat techniques and martial arts:
- Defensive Combat
- Fighting Finesse
- Martial Arts
- Street Fighting
- Armed Defense

#### Supernatural Merits
Psychic and supernatural abilities:
- Aura Reading
- Telepathy
- Telekinesis
- Medium
- Psychometry

---

### Merit Commands

```
+xp/buy <merit>=[dots]       - Purchase a merit
+xp/refund <merit>           - Refund a merit (staff only)
+xp/list merits [category]   - List available merits
+xp/info <merit>             - Show merit details
```

**Examples:**
```
+xp/buy contacts=3
+xp/buy fast_reflexes 2
+xp/list merits mental
+xp/info striking_looks
```

---

### Prerequisites System

#### Format
- `attribute:value` - Requires specific attribute level
- `skill:value` - Requires specific skill level
- `[option1:value,option2:value]` - OR requirement (either option)
- `requirement1,requirement2` - AND requirement (both needed)

#### Examples
- `resolve:2` - Requires Resolve 2+
- `[wits:3,dexterity:3]` - Requires Wits 3+ OR Dexterity 3+
- `strength:3,brawl:2` - Requires Strength 3+ AND Brawl 2+
- `martial_arts:2,stamina:3` - Requires Martial Arts 2+ AND Stamina 3+

### Character Sheet Integration
Merits appear on sheet organized by category with dot notation (●○○○○).

---

### Merit Instances
Some merits can be purchased multiple times with different specifications:
- **Contacts:** One purchase per type (police, media, criminals, etc.)
- **Allies:** One purchase per organization
- **Status:** One purchase per organization
- **Area of Expertise:** One purchase per specialty

System tracks these separately and displays all instances.

---

## Mystery & Investigation

### Overview
Unified mystery investigation system for storytelling. Players investigate mysteries by discovering clues through examination, searching, interviews, and research.

### Player Investigation

#### Discovery Methods

**Examine Objects:**
```
+mystery/examine <object>    - Carefully examine for clues
```
- Requires physical object in room
- May require skill rolls (Investigation, etc.)
- Reveals clues attached to object

**Search Areas:**
```
+mystery/search [area]       - Search for hidden clues
```
- Searches current room or specified area
- May require Wits + Investigation roll
- Discovers hidden clues meeting conditions

**Interview Characters:**
```
+mystery/interview <character> - Interview for information
```
- Requires social skills (Manipulation + Persuasion, etc.)
- NPCs or other players can provide clues
- Difficulty based on character's willingness to talk

**Research Topics:**
```
+mystery/research <topic>    - Research in library/resources
```
- Requires appropriate resources merit or library access
- Intelligence + Academics or specialized skills
- Discovers information-based clues

---

#### Collaboration

**Share Clues:**
```
+mystery/share <character>=<clue> - Share discovered clue
```
- Transfer clue knowledge to another character
- Both characters must have access to mystery
- Encourages teamwork

**Collaborate:**
```
+mystery/collaborate <character> - Begin collaborating
```
- Link investigations with another character
- Pool clue discoveries
- Enhanced teamwork bonuses

---

### Staff Management

#### Creating Mysteries

**Basic Setup:**
```
+mystery/create <title>=<description> - Create mystery
+mystery/edit <id>/<field>=<value> - Edit mystery
+mystery/status <id>=<status> - Set status (active/solved/suspended)
```

**Adding Clues:**
```
+mystery/addclue <id>=<name>/<description> - Add clue
+mystery/editclue <id>/<clue_id>=<field>/<value> - Edit clue
+mystery/delclue <id>/<clue_id> - Delete clue
```

---

#### Clue Structure

**Clue Relationships:**
```
+mystery/prereq <id>/<clue>=<prereq_clues> - Set prerequisites
+mystery/leads <id>/<clue>=<lead_clues> - Set leads
```
- Prerequisites: Clues required before this one can be discovered
- Leads: Clues this one points toward

**Example Flow:**
- Clue 0 (Initial): "Blood stain on floor"
- → Leads to Clue 1: "Blood matches victim's type"
- → Leads to Clue 2: "Pattern suggests struggle"

---

#### Discovery Conditions

**Skill Requirements:**
```
+mystery/skillroll <id>/<clue>=<skill>/<attribute>/<difficulty>
```
- Sets required skill roll for discovery
- Example: `investigation/wits/3`

**Access Conditions:**
```
+mystery/conditions <id>/<clue>=<conditions>
```
Condition types:
- `skill:investigation:3` - Requires skill level
- `template:vampire` - Requires specific template
- `clan:ventrue` - Requires bio information
- `participant` - Visible to mystery participants only
- `open` - Visible to anyone

**Example:**
```
+mystery/conditions 3/clue_0=skill:investigation:3,template:vampire
```

---

#### Access Control

**Mystery Access:**
```
+mystery/access <id>=<access_rules>
```
Access types:
- `group:vampires` - Requires group membership
- `template:vampire` - Requires template
- `clan:ventrue` - Requires bio details
- `skill:investigation:3` - Requires skill level
- `open` - Accessible to anyone

**Participants:**
```
+mystery/participant <id>=<character> - Add participant
```
- Links character as mystery participant
- Enables participant-only clue access

---

#### Clue Objects

**Physical Clues:**
```
+mystery/clueobj/create <name>=<id>/<clue_id> - Create clue object
+mystery/clueobj/edit <object>=<field>/<value> - Edit clue object
+mystery/clueobj/list [here] - List clue objects
+mystery/clueobj/delete <object> - Delete clue object
```

Clue objects can be examined and interact with investigation system.

---

#### Progress Tracking

**View Progress:**
```
+mystery/progress [id] - Show investigation progress
+mystery/discovered <id> [character] - Show discovered clues
+mystery/staffprogress [id] - Detailed staff view
```

**Manual Clue Management:**
```
+mystery/grant <character>=<id>/<clue> - Grant clue to character
+mystery/revoke <character>=<id>/<clue> - Revoke clue from character
```

---

### Clue Types

The system supports different types of clues:
- **Physical Evidence:** Objects that can be examined
- **Testimonial:** Information from interviews
- **Documentary:** Written records and research
- **Forensic:** Technical analysis results
- **Supernatural:** Magical or psychic impressions

Each type may have different discovery conditions and requirements.

---

## Equipment & Purchasing

### Overview
Equipment management system for weapons, armor, and general items with purchasing mechanics.

### Inventory Management

```
+equipment                   - View your inventory
+equipment/add <item>        - Add item to inventory
+equipment/remove <item>     - Remove item from inventory
+equipment/equip <item>      - Equip item for combat
+equipment/unequip <item>    - Unequip item
```

---

### Purchasing System

```
+buy                         - View available items for purchase
+buy <item>                  - Purchase an item
+buyconfig                   - View purchasing configuration (staff)
```

#### Resource-Based Purchasing
- Items have resource costs (Resources 1-5)
- Characters must have appropriate Resources merit
- Availability rating affects purchase difficulty

#### Types of Purchases
- **Weapons:** Melee weapons, firearms, ammunition
- **Armor:** Light armor, heavy armor, ballistic vests
- **Equipment:** Tools, electronics, vehicles
- **Services:** Information, contacts, transportation

---

### Combat Integration

**Equipped Gear:**
```
+combatgear                  - View equipped combat gear
```

During combat:
- Equipped weapons automatically available for attacks
- Armor automatically applied to damage reduction
- Quick-draw merit affects weapon readiness

---

## Conditions & Tilts

### Conditions
Temporary effects that modify character capabilities and provide story hooks.

#### Condition Management
```
+condition/list              - List your active conditions
+condition/add <condition>   - Add a condition
+condition/remove <condition> - Remove a condition
+condition/info <condition>  - View condition details
```

#### Condition Types
- **Persistent:** Last until resolved through specific action
- **Lasting:** Last for specific duration
- **Environmental:** Affect everyone in area

#### Resolving Conditions
- Many conditions grant beats when resolved
- Some require specific actions to remove
- Staff can force resolve conditions

---

### Tilts
Environmental and personal effects that provide mechanical modifiers.

#### Tilt Management
```
+tilt/list                   - List active tilts
+tilt/add <tilt>             - Add a tilt
+tilt/remove <tilt>          - Remove a tilt
+tilt/info <tilt>            - View tilt details
```

#### Tilt Categories
- **Environmental:** Darkness, extreme cold/heat, heavy rain
- **Personal:** Arm wrack, blinded, deafened, knocked down
- **Combat:** Cover, concealment, immobilized

#### Tilt Effects
- Modify dice pools
- Change combat capabilities
- Affect movement and actions
- May require specific actions to remove

---

## Social Maneuvering

### Overview
Social influence system for diplomatic interactions and manipulation.

### Opening Social Maneuvers
```
+social/open <target>=<goal> - Start social interaction
```

**Goal Types:**
- Persuade target to take action
- Change target's opinion
- Gain information
- Establish relationship

---

### Making Impressions
```
+social/roll <target>        - Make impression roll
```

- Uses appropriate social skills (Manipulation + Persuasion, etc.)
- Accumulate impressions toward goal
- Target's Resolve + Composure determines doors (resistance)

### Resolution
```
+social/close                - Close social maneuver
```

- Compare impressions to doors
- Determine success level
- Apply results

### Social Doors
- **Doors:** Target's Resolve + Composure
- Each impression opens one door
- Must open all doors to achieve goal
- Modified by relationship, evidence, leverage

---

## Storyteller System

### Overview
Special permissions and tools for player storytellers to run scenes and plots.

### Storyteller Permissions
- Create and manage mysteries
- Create and control NPCs
- Use building commands in designated areas
- Access storytelling tools
- Grant beats and XP for scenes

---

### Storyteller Management (Admin)
```
+storyteller/list            - List all storytellers
+storyteller/add <character> - Grant Storyteller flag
+storyteller/remove <character> - Remove Storyteller flag
+storyteller/check [character] - Check Storyteller status
+storyteller/info            - Show permission info
```

---

### Storyteller Commands

**NPCs:**
```
+npc/create <name>           - Create an NPC
+npc/possess <npc>           - Control an NPC
+npc/stat <npc>/<stat>=<value> - Set NPC stat
```

**Mysteries:**
```
+mystery/create <title>=<desc> - Create mystery
+mystery/grant <char>=<id>/<clue> - Grant clue
```

**Scene Management:**
- Set environmental conditions
- Apply damage/healing
- Force skill rolls
- Grant beats for participation

---

### Who's Online
```
+stwho                       - View online storytellers/staff
```
Shows all online storytellers with idle times for player reference.

---

## Language System

### Overview
Multi-language support for in-character communication.

### Setting Language
Characters can speak in different languages during roleplay.

### Language Tags
Use special syntax to indicate speech in specific languages:
```
say "~Bonjour, mes amis!"    - French
@emit "~Hola!" calls a voice in Spanish.
```

### Language Comprehension
- Characters understand based on language skills/merits
- Unknown languages appear as "[Speaking in French]"
- Language merit determines fluency
- Staff can set language skills on characters

### Common Languages
- English (default)
- French, Spanish, German, Italian
- Latin, Greek, Hebrew
- Japanese, Mandarin, etc.

### Language Skill Levels
- **1 dot:** Basic comprehension
- **2 dots:** Conversational
- **3 dots:** Fluent
- **4+ dots:** Native speaker quality

---

## Legacy Mode

### Overview
Enable 1st Edition Chronicles of Darkness rules instead of 2nd Edition.

### Enabling Legacy Mode
```
+legacy                      - Toggle legacy mode
+legacy/on                   - Enable legacy mode
+legacy/off                  - Disable legacy mode
+legacy/status               - Check legacy mode status
```

---

### Legacy Mode Changes

#### Removed Systems (2e Only)
- **Aspirations:** Not used in 1e
- **Integrity:** Replaced with Morality/equivalent
- **Conditions:** Simplified condition system

#### Retained Systems
- **Virtue and Vice:** Primary character motivation
- **Beats and Experience:** Same conversion rate
- **Power Stats:** Function similarly with minor differences

#### Modified Mechanics
- Different pool calculations
- Adjusted derived stats
- Alternative advancement costs

---

### When to Use Legacy Mode
- Running published 1st Edition adventures
- Player preference for 1e rules
- Consistency with existing 1e characters
- Game-wide decision to use 1e

**Note:** Most new content assumes 2nd Edition rules.

---

## Quick Reference Tables

### Combat Quick Reference
| Action | Command | Type |
|--------|---------|------|
| Attack | `+combat/attack <target>` | Instant |
| Dodge | `+combat/dodge` | Instant |
| Move | `+combat/move <distance>` | Reflexive |
| Aim | `+combat/aim <target>` | Instant |
| Grapple | `+combat/grapple <target>` | Instant |
| Reload | `+combat/reload` | Instant |

### Damage Types
| Type | Symbol | Color | Examples |
|------|--------|-------|----------|
| Bashing | / | Cyan | Fists, clubs, fatigue |
| Lethal | X | Red | Knives, bullets, falls |
| Aggravated | * | Bright Red | Fire, silver, sunlight |

### Experience Costs
| Trait | Cost (XP) |
|-------|-----------|
| Attribute | 4 per dot |
| Skill | 2 per dot |
| Merit | 1 per dot |
| Integrity | 2 per dot |
| Specialty | 1 each |

### Arcane XP (Mages)
| Trait | Cost | Type |
|-------|------|------|
| Arcanum (to limit) | 4 XP | Either |
| Arcanum (above limit) | 5 XP | Either |
| Gnosis | 5 XP | Either |
| Praxis | 1 XP | Arcane Only |
| Wisdom | 2 XP/dot | Arcane Only |
| Rotes | 1 XP | Either |

---

*For command syntax, see COMMANDS.md. For building, see BUILDING_GUIDE.md.*

