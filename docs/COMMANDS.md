# Player and Admin Commands Reference

Complete reference for all commands available in the PyReach Chronicles of Darkness MUSH system.

## Table of Contents

1. [Character Commands](#character-commands)
2. [Sheet & Stats](#sheet--stats)
3. [Experience & Advancement](#experience--advancement)
4. [Combat Commands](#combat-commands)
5. [Social & Investigation](#social--investigation)
6. [Movement & Travel](#movement--travel)
7. [Groups & Organizations](#groups--organizations)
8. [Notes & Journals](#notes--journals)
9. [Communication](#communication)
10. [Admin Commands](#admin-commands)
11. [Building Commands](#building-commands)

---

## Character Commands

### +sheet - View Character Sheet
Display your character sheet with all stats, pools, and information.

```
+sheet                    - View your own character sheet
+sheet <character>        - View another character's sheet
+sheet/ascii              - Force ASCII display (no Unicode dots)
```

**Features:**
- UTF-8 Unicode dots (● ○) or ASCII (* -) for compatible clients
- Template-specific power stats (Gnosis, Wyrd, Primal Urge, etc.)
- Biographical information display
- Health and willpower tracking
- Equipment and conditions

---

### +stat - Manage Character Statistics
Set and manage all character statistics including bio fields.

```
+stat <stat>=<value>          - Set a stat value
+stat/remove <stat>           - Remove a stat
+stat/list                    - View all stats and bio info
+stat <character>/<stat>=<value> - Staff: set stat for another character
```

**Bio Fields:**
- `fullname` - Full character name
- `birthdate` - Date of birth
- `concept` - Character concept/profession
- `virtue` - Highest moral principle
- `vice` - Greatest moral failing

**Template-Specific Fields:**
- **Vampire:** mask, dirge, clan, covenant
- **Werewolf:** bone, blood, auspice, tribe, deed_name
- **Mage:** path, order, shadow_name, cabal
- **Changeling:** seeming, court, kith
- **Geist:** burden, archetype, krewe
- **And more** for each Chronicles of Darkness splat

**Examples:**
```
+stat fullname=John Smith
+stat concept=Detective
+stat virtue=Justice
+stat clan=Gangrel              # Vampire only
+stat auspice=Rahu              # Werewolf only
```

---

### +pool - Manage Resource Pools
Manage willpower and supernatural resource pools.

```
+pool                         - Show all available pools
+pool <pool>                  - Show specific pool status
+pool/<pool>/spend [amount]   - Spend from pool (default: 1)
+pool/<pool>/gain [amount]    - Gain pool points (default: 1)
+pool/<pool>/set <current>/<max> - Set pool values (staff only)
+pool/<pool>/reset            - Reset pool to maximum (staff only)
```

**Available Pools by Template:**
- **Universal:** willpower
- **Werewolf:** essence (based on Primal Urge)
- **Vampire:** blood (based on Blood Potency)
- **Changeling:** glamour (based on Wyrd)
- **Mage:** mana (based on Gnosis)
- **Geist:** plasm (based on Synergy)
- **Deviant:** instability
- **Demon:** aether
- **Promethean:** pyros

**Examples:**
```
+pool/willpower/spend 2
+pool/blood/gain 3
+pool/essence
```

---

### +health - Manage Health and Damage
Track character health and damage types.

```
+health                       - Show current health status
+health/damage <amount> [type] - Take damage (bashing default)
+health/heal <amount> [type]  - Heal damage
+health/set <level> <type>    - Set specific health box (staff)
+health/clear                 - Clear all damage (staff)
+health/max <amount>          - Set maximum health (staff)
```

**Damage Types:**
- **bashing** (b) - Bruises, fatigue (cyan /)
- **lethal** (l) - Cuts, bullets (red X)
- **aggravated** (a) - Fire, supernatural (bright red *)

**Examples:**
```
+health/damage 2 lethal
+health/heal 1 bashing
+health
```

---

### +aspiration - Manage Character Aspirations
Set and fulfill character aspirations for beats.

```
+aspiration/list              - List your current aspirations
+aspiration/add <number> <description> - Add/update aspiration (1-3)
+aspiration/remove <number>   - Remove an aspiration
+aspiration/fulfill <number>  - Mark fulfilled and gain a beat
```

**Examples:**
```
+aspiration/list
+aspiration/add 1 Find my missing sister
+aspiration/fulfill 1
```

---

### +shift - Werewolf Shapeshifting
Transform between the five forms of the Uratha (Werewolf characters only).

```
+shift <form>                - Transform into specified form
+shift/list                  - Show all available forms
+shift/info <form>           - Show detailed form information
+form                        - Quick reference for current form
```

**The Five Forms:**
- **Hishu** - Human form (default, only form allowing XP spending)
- **Dalu** - Near-Man form (Str +1, Sta +1, Man -1, Size +1)
- **Gauru** - War form (Str +3, Dex +1, Sta +2, Size +2, LIMITED DURATION)
- **Urshul** - Near-Wolf form (Str +2, Dex +2, Sta +2, Man -1, Size +1)
- **Urhan** - Wolf form (Dex +2, Sta +1, Man -1, Size -1)

**Important Restrictions:**
- Can only use `+stat`, `+xp/spend`, and `+xp/buy` while in Hishu form
- Form bonuses are temporary - returning to Hishu restores base stats
- Gauru form has limited duration (Stamina + Primal Urge turns)
- Derived stats (Health, Speed, Defense, Initiative) auto-recalculate

**Examples:**
```
+shift gauru        - Transform into war form
+shift hishu        - Return to human form
+shift/list         - See all forms
+shift/info urshul  - Learn about near-wolf form
+form               - Check current form
```

**See Also:** [Shapeshifting Guide](../commands/SHAPESHIFTING_GUIDE.md) for complete details.

---

### +condition - Manage Conditions
Track temporary conditions affecting your character.

```
+condition/list               - List your active conditions
+condition/add <condition>    - Add a condition
+condition/remove <condition> - Remove a condition
+condition/info <condition>   - View condition details
```

---

### +tilt - Manage Tilts
Track environmental and personal tilts in combat.

```
+tilt/list                    - List active tilts
+tilt/add <tilt>              - Add a tilt
+tilt/remove <tilt>           - Remove a tilt
+tilt/info <tilt>             - View tilt details
```

---

## Sheet & Stats

### +finger - View Player Information
Quick view of player online status and basic info.

```
+finger <player>              - View player information
```

---

### +lookup - Search Game Databases
Look up merits, conditions, tilts, contracts, and other game mechanics.

```
+lookup <search term>         - Search all databases
+lookup/merit <name>          - Look up specific merit
+lookup/condition <name>      - Look up specific condition
+lookup/tilt <name>           - Look up specific tilt
+lookup/contract <name>       - Look up Changeling contract
+lookup/gift <name>           - Look up Werewolf gift
+lookup/discipline <name>     - Look up Vampire discipline
```

**Examples:**
```
+lookup fast reflexes
+lookup/merit striking looks
+lookup/condition stunned
```

---

## Experience & Advancement

### +xp - Experience Point Management
Manage beats, experience points, and character advancement.

```
+xp                           - View experience summary
+xp/beat <source>             - Add a beat
+xp/spend <stat>=<dots>       - Spend XP on attributes/skills
+xp/buy <merit>=[dots]        - Purchase a merit
+xp/refund <merit>            - Refund a merit (staff only)
+xp/costs                     - Show XP costs
+xp/list merits [category]    - List available merits
+xp/info <merit>              - Show merit details
```

**Beat Sources:**
- dramatic_failure, exceptional_success, conditions
- aspirations, story, scene, session
- roleplay, challenge, sacrifice
- discovery, relationship, consequence
- learning, growth

**Experience Costs:**
- **Attributes:** 4 XP per dot
- **Skills:** 2 XP per dot
- **Merits:** 1 XP per dot
- **Integrity:** 2 XP per dot
- **Specialties:** 1 XP each

**Examples:**
```
+xp/beat dramatic_failure
+xp/spend strength=4
+xp/buy contacts=3
+xp/list merits social
```

---

### +xp/arcane - Arcane Experience (Mages Only)
Manage Mage-specific arcane experience for magical advancement.

```
+xp/arcane <source>           - Add arcane beat
+xp/spend/arcane <stat>=<dots> - Spend arcane XP
+xp/costs/arcane              - Show arcane XP costs
```

**Arcane Beat Sources:**
- obsession, magical_condition
- spell_dramatic_failure, act_of_hubris
- legacy_tutoring, supernatural_encounter

**Arcane XP Uses:**
- Arcanum dots (4-5 XP)
- Gnosis (5 XP)
- Praxis (1 Arcane XP - mandatory)
- Wisdom (2 Arcane XP - mandatory)
- Rotes (1 XP either regular or arcane)

**Examples:**
```
+xp/arcane obsession
+xp/spend/arcane forces=3
+xp/spend/arcane gnosis=2
```

---

### +vote & +recommend - XP Voting System
Vote for and recommend other players for experience rewards.

```
+vote <player>=<reason>       - Vote for a player
+recommend <player>=<reason>  - Recommend a player (stronger)
+vote/check                   - Check your vote cooldowns
```

**Note:** System may be in weekly beats mode instead of voting mode. Use `+voteadmin/settings` (staff) to check mode.

---

## Combat Commands

### Combat Management

```
+combat/join [team]           - Join combat (optional team number)
+combat/leave                 - Leave combat
+combat/init [modifier]       - Roll initiative
+combat/status                - Show combat status and turn order
+combat/next                  - Advance to next turn
+combat/end                   - End combat (staff only)
+combat/team <number>         - Switch to specific team
+combat/teams                 - Show team composition
```

---

### Attack Actions

```
+combat/attack <target> [weapon] - Basic attack
+combat/attack/allout <target> [weapon] - All-out attack (+2 attack, lose Defense)
+combat/attack/charge <target> [weapon] - Charge (+1 damage, requires movement)
+combat/attack/specify <target>=<location> [weapon] - Targeted attack
+combat/attack/multiple <target1>,<target2>... [weapon] - Multiple attacks
```

---

### Defensive Actions

```
+combat/dodge                 - Dodge (double Defense, lose next action)
+combat/dodge/full            - Full dodge for turn (Instant)
+combat/block <attacker>      - Block (+2 Defense vs one attacker)
+combat/cover <rating>        - Take cover (1-4 rating)
```

---

### Other Combat Actions

```
+combat/move <distance>       - Move up to Speed (Reflexive)
+combat/sprint                - Sprint (roll Strength + Athletics)
+combat/aim <target>          - Aim (+1 per turn, max +3)
+combat/grapple <target>      - Attempt grapple
+combat/reload [weapon]       - Reload weapon
+combat/ready <weapon>        - Ready/change weapon
+combat/delay <initiative>    - Delay action to lower initiative
```

---

### Surrender System

```
+combat/surrender             - Offer surrender for your team
+combat/accept <team>         - Accept surrender from team
+combat/decline <team>        - Decline surrender from team
```

---

### Equipment Commands

```
+equipment                    - View your equipment inventory
+equipment/add <item>         - Add item to inventory
+equipment/remove <item>      - Remove item from inventory
+equipment/equip <item>       - Equip item for combat
+equipment/unequip <item>     - Unequip item

+buy                          - View available items for purchase
+buy <item>                   - Purchase an item
+buyconfig                    - View purchasing configuration (staff)
```

---

## Social & Investigation

### +mystery - Investigation System
Investigate mysteries and manage clues (players and staff).

**Player Commands:**
```
+mystery                      - List active mysteries
+mystery <id>                 - View mystery details
+mystery/progress [id]        - Show investigation progress
+mystery/examine <object>     - Examine for clues
+mystery/search [area]        - Search for hidden clues
+mystery/interview <character> - Interview for information
+mystery/research <topic>     - Research a topic
+mystery/share <char>=<clue>  - Share a clue
+mystery/collaborate <char>   - Begin collaborating
```

**Staff Commands:**
```
+mystery/create <title>=<description>
+mystery/list [category]      - List all mysteries
+mystery/view <id>            - Staff view
+mystery/edit <id>/<field>=<value>
+mystery/delete <id>
+mystery/status <id>=<status>
+mystery/addclue <id>=<name>/<desc>
+mystery/grant <char>=<id>/<clue_id>
+mystery/revoke <char>=<id>/<clue_id>
```

---

### +social - Social Maneuvering
Handle social interactions and influence.

```
+social/open <target>=<goal>  - Open social maneuver
+social/roll <target>         - Make social impression roll
+social/close                 - Close social maneuver
+social/status                - Check active social maneuvers
```

---

## Movement & Travel

### +ooc & +ic - OOC/IC Movement
Move between out-of-character and in-character areas.

```
+ooc                          - Go to OOC room
+ic                           - Return to IC area or IC starting room
```

**Features:**
- Stores previous location
- Returns you to where you were
- Prevents location desync issues

---

### +hangouts - Travel to Gathering Places
Quick travel to designated social spaces and group hangouts.

```
+hangouts                     - List all available hangouts
+hangouts/public              - List only public hangouts
+hangouts/groups              - List only group hangouts
+hangouts <name>              - Travel to a hangout
+hangouts/return              - Return to previous location
```

**Examples:**
```
+hangouts                     # See all locations
+hangouts crimson             # Go to "The Crimson Rose"
+hangouts/return              # Go back to where you were
```

---

### +join - Staff Teleport (Staff Only)
Teleport to a player's location.

```
+join <player>                - Go to player's location
+join/quiet <player>          - Go quietly (no messages)
```

---

## Groups & Organizations

### +groups - View Groups
List and view information about groups and organizations.

```
+groups                       - List all public groups
+group <id>                   - View detailed group information
+group/show <character>       - Show character's groups
```

---

### +roster - View Group Rosters
View group membership rosters.

```
+roster                       - List available group rosters
+roster <group name>          - View specific group roster
+roster <group id>            - View roster by ID
+roster/all                   - List all rosters (staff only)
```

---

## Notes & Journals

### +note - Character Notes System
Create and manage narrative notes on your character.

```
+note [title]/[category]=[text] - Create a new note
+note                         - View all your notes
+note/edit [title]=[new text] - Edit an existing note
+note/delete [title]          - Delete a note
+note/show [title]            - Show note to room
+note/show [title]=[player]   - Show note to specific player
```

**Staff Commands:**
```
+note/approve [char]=[title]  - Approve note (locks editing)
+note/unapprove [char]=[title] - Unapprove note (unlocks)
```

**Examples:**
```
+note My Backstory/Background=I was born in a small village...
+note/edit My Backstory=I was actually born in a city...
+note/show My Backstory
+note/show My Backstory=Bob
```

**Features:**
- Notes organized by category
- Staff approval system locks notes
- Share publicly or privately
- Timestamps for creation and modification

---

## Communication

### +page - Private Messages
Send private messages to other players.

```
+page <player>=<message>      - Send a page
+page <player1>,<player2>=<message> - Page multiple players
```

---

### Channels
Join and use chat channels.

```
addcom <alias>=<channel>      - Add channel with alias
delcom <alias>                - Remove channel alias
comlist                       - List your channels
<alias> <message>             - Send message to channel
```

---

### +bbs - Bulletin Board System
Read and post to bulletin boards.

```
+bbs                          - List all boards
+bbs <board>                  - List posts on board
+bbs <board>/<post>           - Read a post
+bbs/post <board>/<title>=<text> - Create new post
+bbs/reply <board>/<post>=<text> - Reply to post
+bbs/edit <board>/<post>=<text> - Edit your post
+bbs/delete <board>/<post>    - Delete your post
```

---

## Admin Commands

### +migrate - Stat Migration
Migrate legacy character stats to unified system.

```
+migrate                      - Migrate your own character
+migrate <character>          - Migrate another character (Admin)
```

---

### +template - Template Management
Manage character templates (Admin/Builder).

```
+template/list                - List all installed templates
+template/builtin             - List built-in templates
+template/info <template>     - Show template details
+template/install builtin     - Install all built-in templates
+template/uninstall <template> - Uninstall a template
+template/reset               - Clear and reinstall built-ins
+template/export <template>   - Export template as Python code
+template/reload              - Reload template cache
+template/usage               - Show template usage statistics
```

---

### +storyteller - Storyteller Management
Manage Storyteller permissions (Admin).

```
+storyteller/list             - List all storytellers
+storyteller/add <character>  - Grant Storyteller flag
+storyteller/remove <character> - Remove Storyteller flag
+storyteller/check [character] - Check Storyteller status
+storyteller/info             - Show permission info
```

---

### +stwho - View Online Storytellers
See which storytellers and staff are online.

```
+stwho                        - List online storytellers/staff
```

---

### +voteadmin - XP System Administration
Manage XP systems (Builder).

```
+voteadmin/settings           - Show current settings
+voteadmin/set <setting>=<value> - Set a system setting
+voteadmin/mode <voting|weekly> - Switch XP system mode
+voteadmin/weekly             - Show weekly beats info
+voteadmin/distribute         - Force weekly beat distribution
+voteadmin/script <start|stop> - Start/stop automation script
+voteadmin/reset <character>  - Reset vote cooldowns
+voteadmin/stats [character]  - Show voting statistics
```

**Settings:**
- `vote_cooldown_hours` - Hours between votes (default: 168)
- `recc_cooldown_hours` - Hours between recommendations (default: 168)
- `vote_beats` - Beats per vote (default: 0.5)
- `recc_beats` - Beats per recommendation (default: 1.0)
- `weekly_beats_amount` - Weekly beats (default: 5)
- `weekly_beats_day` - Distribution day (default: sunday)
- `weekly_beats_time` - Distribution time (default: 00:00)

---

### +jobs - Job System Management
Manage player requests and jobs (staff functions).

**Basic Commands:**
```
+jobs                         - List all jobs
+jobs <#>                     - View job details
+jobs/create <category>/<title>=<text>
+jobs/comment <#>=<text>
+jobs/close <#>
+jobs/reopen <#>
```

**Staff Commands:**
```
+jobs/assign <#>=<staff>
+jobs/claim <#>
+jobs/unclaim <#>
+jobs/approve <#>
+jobs/reject <#>
+jobs/complete <#>=<reason>
+jobs/cancel <#>=<reason>
+jobs/transfer <#>=<category>
+jobs/from <name>             - List player's jobs
```

**Admin Commands:**
```
+jobs/clear_archive           - Clear archived jobs (DESTRUCTIVE)
```

---

### +npc - NPC Management
Create and manage NPCs (Storyteller/Admin).

```
+npc/create <name>            - Create an NPC
+npc/list                     - List all NPCs
+npc/delete <npc>             - Delete an NPC
+npc/desc <npc>=<description> - Set NPC description
+npc/stat <npc>/<stat>=<value> - Set NPC stat
+npc/possess <npc>            - Possess/control an NPC
+npc/release                  - Release NPC control
```

---

## Building Commands

### +area - Area Management
Manage game areas and codes (Builder).

```
+area/list                    - List all areas
+area/add <code>=<name>/<desc> - Add new area
+area/remove <code>           - Remove area (if no rooms)
+area/info <code>             - Show area details
+area/rooms <code>            - List rooms in area
+area/init                    - Initialize area manager (Admin)
```

**Examples:**
```
+area/list
+area/add DT=Downtown/The city center
+area/info DT
```

---

### +room - Room Configuration
Configure room settings and area assignments (Builder).

```
+room/area <target>=<area_code> - Set room area (auto-assign code)
+room/code <target>=<code>    - Manual room code override
+room/coords <target>=<x>,<y> - Set coordinates for mapping
+room/hierarchy <target>=<loc1>,<loc2>
+room/places <target>=<on|off> - Enable/disable places system
```

**Target Options:**
- `here` - Current room
- Room name - "The Square"
- Database reference - "#123"

**Examples:**
```
+room/area here=DT
+room/coords here=10,5
+room/hierarchy here=The Square,Downtown
+room/places here=on
```

---

### places - Room Places
Add special places within rooms (Builder).

```
places/add <name>=<description> - Add a place
places/remove <number>        - Remove a place
places/list                   - List all places
places/info <number>          - View place details
```

**Examples:**
```
places/add The Bar=A long mahogany bar lines the eastern wall
places/remove 2
places/list
```

---

### roominfo - Room Information
Display comprehensive room information (Builder).

```
roominfo                      - Show current room details
```

Shows: area codes, coordinates, places, exits, occupants, tags.

---

### +map - Area Mapping
Display ASCII maps of areas.

```
+map                          - Show current area map
+map <area_code>              - Show specific area map
+map/legend                   - Show map symbols legend
```

---

### +hangout - Hangout Management (Staff)
Manage group hangout locations.

```
+hangout/set <group>=<room>   - Set group hangout
+hangout/remove <group>       - Remove group hangout
+hangout/view <group>         - View group hangout
```

**Examples:**
```
+hangout/set Ordo Dracul=The Dragon's Lair
+hangout/remove Ordo Dracul
+hangout/view Ordo Dracul
```

---

### +config - OOC/IC Configuration (Developer)
Configure OOC and IC room settings.

```
+config/list                  - Show current settings
+config/ooc <room>            - Set OOC room
+config/ic <room>             - Set IC starting room
```

---

### +group - Group Management (Staff)
Full group management commands.

```
+group/create <name>          - Create new group
+group/destroy <id>           - Destroy group
+group/type <id>=<type>       - Set group type
+group/leader <id>=<character> - Set group leader
+group/desc <id>=<text>       - Set description
+group/note <id>=<text>       - Set private notes
+group/title <id>/<char>=<title> - Set member title
+group/add <id>=<character>   - Add member
+group/remove <id>=<character> - Remove member
+group/private <id>           - Set as private
+group/public <id>            - Set as public
+group/auto <character>       - Manual auto-assignment
+group/sync                   - Sync character attributes
+group/syncchannels           - Fix channel locks
+group/test <character>       - Test auto-assignment logic
```

---

## Legacy Mode

### +legacy - Toggle Legacy Mode
Enable/disable legacy mode for 1st Edition Chronicles of Darkness.

```
+legacy                       - Toggle legacy mode
+legacy/on                    - Enable legacy mode
+legacy/off                   - Disable legacy mode
+legacy/status                - Check legacy mode status
```

**Legacy Mode Changes:**
- Removes Aspirations and Integrity systems
- Uses only Virtue and Vice for character motivation
- Adjusts beats and experience accordingly

---

## Quick Reference Tables

### Common Commands
| Command | Purpose |
|---------|---------|
| `+sheet` | View character sheet |
| `+stat` | Manage statistics |
| `+xp` | Experience management |
| `+pool` | Manage resource pools |
| `+health` | Track health/damage |
| `+shift` | Werewolf shapeshifting |
| `+combat` | Combat system |
| `+mystery` | Investigation system |
| `+hangouts` | Travel to gathering places |
| `+note` | Character notes/journals |
| `+ooc` / `+ic` | OOC/IC movement |

### Staff Commands
| Command | Purpose |
|---------|---------|
| `+template` | Template management |
| `+storyteller` | Storyteller permissions |
| `+area` / `+room` | Building tools |
| `+group` | Group management |
| `+jobs` | Job system |
| `+npc` | NPC management |
| `+voteadmin` | XP system config |

---

*For detailed system documentation, see other docs: GAME_SYSTEMS.md, BUILDING_GUIDE.md, TYPECLASSES.md*

