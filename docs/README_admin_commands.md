# Admin Commands Reference

This document provides comprehensive documentation for all administrative commands available in the PyReach MUD system. Admin commands are powerful tools for managing the game world, players, and system functionality.

## Table of Contents

1. [Permission Levels](#permission-levels)
2. [Core System Administration](#core-system-administration)
3. [Character Template Management](#character-template-management)
4. [Mystery & Investigation System](#mystery--investigation-system)
5. [Storyteller Management](#storyteller-management)
6. [World Building Commands](#world-building-commands)
7. [Experience & Voting Administration](#experience--voting-administration)
8. [Job System Management](#job-system-management)
9. [Staff Management](#staff-management)
10. [Communication Commands](#communication-commands)
11. [Bulletin Board Administration](#bulletin-board-administration)
12. [Safety & Best Practices](#safety--best-practices)

---

## Permission Levels

The admin command system uses several permission levels:

- **Admin**: Full administrative access to all systems
- **Builder**: Building permissions and some admin functions
- **Staff**: General staff permissions
- **Storyteller**: Special permissions for running stories and managing NPCs

**⚠️ Warning**: Admin commands can permanently modify game data. Always test on development systems first and maintain regular backups.

---

## Core System Administration

### +migrate
**Purpose**: Migrate legacy character stats to the new unified stats system  
**Permission**: Admin (for others), All (for self)  
**File**: `commands/admin_commands.py`

```
Usage:
  +migrate                    - Migrate your own character's legacy stats
  +migrate <character>        - Migrate another character's stats (Admin only)
```

**Description**: 
Converts old individual attribute storage (e.g., `db.strength`, `db.dexterity`) to the new unified stats dictionary format. This command also cleans up old database attributes to prevent bloat.

**What it migrates**:
- Attributes (strength, dexterity, stamina, etc.)
- Skills (crafts, investigation, athletics, etc.)
- Advantages (health, willpower, defense, etc.)
- Bio fields (fullname, concept, virtue, vice, etc.)
- Template-specific fields (clan, auspice, seeming, etc.)

**Safety Notes**:
- Creates backup of data before migration
- Only migrates if legacy data is found
- Cleans up old attributes after successful migration
- Reports what was migrated

---

## Character Template Management

### +template
**Purpose**: Manage character templates for Chronicles of Darkness  
**Permission**: Admin/Builder  
**File**: `commands/template_admin.py`

```
Usage:
  +template/list                          - List all installed templates
  +template/builtin                       - List available built-in template definitions  
  +template/info <template>               - Show detailed info about a template
  +template/install builtin               - Install all built-in templates
  +template/install module <module>       - Install template from Python module
  +template/uninstall <template>          - Uninstall a template
  +template/force_uninstall <template>    - Force uninstall a template (even system templates)
  +template/clear                         - Remove ALL templates (force uninstall everything)
  +template/reset                         - Clear all templates and reinstall built-ins fresh
  +template/export <template>             - Export template as Python code
  +template/reload                        - Reload template cache
  +template/force_reload                  - Force complete reload from database
  +template/create <template>             - Create a new template interactively
  +template/usage                         - Show template usage statistics
```

**Examples**:
```
+template/list
+template/info vampire
+template/install builtin
+template/install module hunter           # Install hunter.py from templates folder
+template/uninstall custom_template
+template/export vampire
```

**Safety Notes**:
- `/clear` removes ALL templates - use with extreme caution
- `/force_uninstall` can remove system templates - may break character creation
- Always backup before major template operations

---

## Mystery & Investigation System

### +mystery
**Purpose**: Create and manage investigation mysteries for storytelling  
**Permission**: Admin/Storyteller  
**File**: `commands/mystery_admin.py`

```
Usage:
  +mystery/create <title> = <description>
  +mystery/list [category]
  +mystery/view <mystery_id>
  +mystery/edit <mystery_id>/<field> = <value>
  +mystery/delete <mystery_id>
  +mystery/status <mystery_id> = <active|solved|suspended>
  
  +mystery/addclue <mystery_id> = <name>/<description>
  +mystery/editclue <mystery_id>/<clue_id> = <field>/<value>
  +mystery/delclue <mystery_id>/<clue_id>
  +mystery/prereq <mystery_id>/<clue_id> = <prerequisite_clue_ids>
  +mystery/leads <mystery_id>/<clue_id> = <leads_to_clue_ids>
  
  +mystery/conditions <mystery_id>/<clue_id> = <conditions_json>
  +mystery/revelation <mystery_id>/<trigger_id> = <required_clues>/<revelation>
  +mystery/access <mystery_id> = <templates|characters|areas>
  
  +mystery/progress [mystery_id]
  +mystery/discovered <mystery_id> [character]
  +mystery/grant <character> = <mystery_id>/<clue_id>
  +mystery/revoke <character> = <mystery_id>/<clue_id>
  
  +mystery/templates - List available mystery templates
  +mystery/template <template_name> = [custom_title] - Create from template
```

**Examples**:
```
+mystery/create The Missing Heir = A wealthy family's heir has vanished
+mystery/addclue mystery_1 = Torn Letter/A letter with half the address torn off
+mystery/prereq mystery_1/clue_1 = clue_0
+mystery/conditions mystery_1/clue_2 = {"skill_roll": {"skill": "investigation", "attribute": "wits", "difficulty": 3}}
+mystery/grant Alice = mystery_1/clue_1
```

### +clueobj
**Purpose**: Create discoverable clue objects in rooms  
**Permission**: Admin/Storyteller  
**File**: `commands/mystery_admin.py`

Allows placement of physical objects that players can discover and examine to uncover mystery clues.

---

## Storyteller Management

### +storyteller
**Purpose**: Manage Storyteller flags and permissions  
**Permission**: Admin  
**File**: `commands/storyteller_admin.py`

```
Usage:
  +storyteller/list                    - List all current storytellers
  +storyteller/add <character>         - Grant Storyteller flag
  +storyteller/remove <character>      - Remove Storyteller flag
  +storyteller/check [character]       - Check if character has Storyteller flag
  +storyteller/info                    - Show information about Storyteller permissions
```

**Storyteller Permissions Include**:
- Create and manage mysteries
- Create and control NPCs
- Use building commands in designated areas
- Access storytelling tools

**Examples**:
```
+storyteller/add Alice
+storyteller/remove Bob
+storyteller/check Alice
+storyteller/list
```

### +stwho
**Purpose**: Quick view of online storytellers and staff  
**Permission**: All  
**File**: `commands/storyteller_admin.py`

```
Usage:
  +stwho
```

Shows all online storytellers and staff members with idle times.

---

## World Building Commands

### +area
**Purpose**: Manage game areas and their codes  
**Permission**: Builder  
**File**: `commands/building.py`

```
Usage:
  +area/list                           - List all defined areas
  +area/add <code>=<name>/<description> - Add a new area
  +area/remove <code>                  - Remove an area (if no rooms use it)
  +area/info <code>                    - Show detailed info about an area
  +area/rooms <code>                   - List all rooms in an area
  +area/init                           - Initialize/reset area manager (admin only)
```

**Examples**:
```
+area/list
+area/add TW=The Thorns/Twisted pathways of the deep Hedge
+area/info HE
+area/rooms HE
+area/remove TW
```

### +room
**Purpose**: Set up room area information and display properties  
**Permission**: Builder  
**File**: `commands/building.py`

```
Usage:
  +room/area <target>=<area_code>           - Set area and auto-assign room code
  +room/code <target>=<specific_code>       - Manual override of room code (advanced)
  +room/coords <target>=<x>,<y>             - Set room coordinates for mapping
  +room/hierarchy <target>=<location1>,<location2>
  +room/places <target>=on/off
```

**Target Options**:
- `here` for current room
- Room name (e.g., "The Square")
- Database reference (e.g., "#123")

**Examples**:
```
+room/area here=HE               # Set current room to Hedge area
+room/area #123=SH               # Set room #123 to Shadow area
+room/code here=HE05             # Manual override to set current room to HE05
+room/coords here=10,5           # Set current room coordinates for mapping
+room/hierarchy here=The Square,New Redoubt
+room/places here=on
```

### places
**Purpose**: Add special places to rooms for detailed descriptions  
**Permission**: Builder  
**File**: `commands/building.py`

```
Usage:
  places/add <name>=<description>
  places/remove <number>
  places/list or places
  places/info <number>
```

**Examples**:
```
places/add The Stone Pool=A shallow pool in the center of the square
places/remove 5
places/list
places/info 5
```

### roominfo
**Purpose**: Display detailed information about room settings  
**Permission**: Builder  
**File**: `commands/building.py`

```
Usage:
  roominfo
```

Shows comprehensive room information including area codes, coordinates, places, exits, and occupants.

### +map
**Purpose**: Display ASCII maps of areas  
**Permission**: All  
**File**: `commands/building.py`

```
Usage:
  +map                    - Show map of current area
  +map <area_code>        - Show map of specific area
  +map/legend             - Show map legend and symbols
```

**Examples**:
```
+map         # Show map of current room's area
+map HE      # Show map of Hedge area
+map/legend  # Show what symbols mean
```

### @init_area_manager
**Purpose**: Initialize the area manager system  
**Permission**: Admin  
**File**: `commands/admin_area_init.py`

```
Usage:
  @init_area_manager
```

**⚠️ Warning**: This is a one-time setup command that should only be run when setting up the game for the first time.

---

## Experience & Voting Administration

### +voteadmin
**Purpose**: Manage XP systems (voting and weekly beats)  
**Permission**: Builder  
**File**: `commands/voting.py`

```
Usage:
  +voteadmin/settings                    - Show current settings
  +voteadmin/set <setting>=<value>       - Set a system setting
  +voteadmin/reset <character>           - Reset vote cooldowns for character
  +voteadmin/stats [character]           - Show voting statistics
  +voteadmin/mode <voting|weekly>        - Switch between voting and weekly beats systems
  +voteadmin/weekly                      - Show weekly beats system info
  +voteadmin/distribute                  - Force weekly beat distribution (weekly mode only)
  +voteadmin/script <start|stop>         - Start/stop weekly beats automation script
```

**Available Settings**:

*Voting System*:
- `vote_cooldown_hours` - Hours between votes (default: 168 = 1 week)
- `recc_cooldown_hours` - Hours between recommendations (default: 168 = 1 week)
- `vote_beats` - Beats awarded per vote (default: 0.5)
- `recc_beats` - Beats awarded per recommendation (default: 1.0)

*Weekly Beats System*:
- `weekly_beats_amount` - Beats distributed weekly (default: 5)
- `weekly_beats_day` - Day of week for distribution (default: sunday)
- `weekly_beats_time` - Time of day for distribution (default: 00:00)

**Examples**:
```
+voteadmin/mode weekly
+voteadmin/set weekly_beats_amount=6
+voteadmin/set weekly_beats_day=monday
+voteadmin/weekly
+voteadmin/distribute
```

---

## Job System Management

### +jobs (Admin Functions)
**Purpose**: Comprehensive job/request management system  
**Permission**: Various (see individual functions)  
**File**: `commands/jobs/jobs_commands.py`

The job system includes extensive administrative functions for managing player requests:

**Basic Usage**:
```
+jobs                      - List all jobs
+jobs <#>                  - View details of a specific job
+jobs/create <category>/<title>=<text>
+jobs/comment <#>=<text>   - Add a comment to a job
+jobs/close <#>           - Close a job
+jobs/reopen <#>          - Reopen an archived job
```

**Staff Functions**:
```
+jobs/assign <#>=<staff>
+jobs/claim <#>
+jobs/unclaim <#>
+jobs/approve <#>
+jobs/reject <#>
+jobs/reassign <#>=<new assignee>
+jobs/complete <#>=<reason>
+jobs/cancel <#>=<reason>
+jobs/transfer <#>=<category>  - Move a job to a different category/queue
+jobs/from <name>              - List all jobs associated with a player (staff only)
```

**Admin-Only Functions**:
```
+jobs/clear_archive        - Clear all archived jobs and reset job numbers (Admin only)
```

**Available Categories**:
- REQ - General requests
- BUG - Bug reports
- PLOT - Plot-related requests
- BUILD - Building/room requests
- MISC - Miscellaneous requests
- XP - XP requests
- PRP - PRP requests
- VAMP, SHIFT, MORT, POSS, COMP, LING, MAGE - Template-specific requests
- EQUIP - Equipment requests

**⚠️ Warning**: `/clear_archive` permanently deletes all archived jobs and resets job numbering. This cannot be undone.

---

## Staff Management

### +staff
**Purpose**: List and manage staff members  
**Permission**: Various (see individual functions)  
**File**: `commands/DiesIraeCode/CmdStaff.py`

```
Usage:
  +staff                              - Display staff list
  +staff/position <account> = <position> - Set the position of a staff member (Admin only)
  +staff/add <account>                - Add an account to staff (Admin only)
  +staff/remove <account>             - Remove an account from staff (Admin only)
  +staff/duty                         - Toggle your duty status (Staff only)
  +staff/duty on|off                  - Explicitly set duty status (Staff only)
  +staff/dark                         - Toggle your visibility (Staff only)
  +staff/dark on|off                  - Explicitly set visibility (Staff only)
```

**Examples**:
```
+staff
+staff/position Wizard = Head Admin
+staff/add NewStaff
+staff/remove FormerStaff
+staff/duty
+staff/duty on
+staff/dark
+staff/dark on
```

**Features**:
- Dark mode hides staff from public +staff, who, and +where commands
- Duty status shows whether staff are actively available
- Position titles can be customized

### +pst
**Purpose**: Manage Player Storytellers  
**Permission**: Various (Admin for management functions)  
**File**: `commands/DiesIraeCode/CmdStaff.py`

```
Usage:
  +pst                                - Display PST list
  +pst/position <account> = <position> - Set the position of a player storyteller (Admin only)
  +pst/add <account>                  - Add an account as player storyteller (Admin only)
  +pst/remove <account>               - Remove an account from player storytellers (Admin only)
  +pst/claim <account>                - Claim a PST position (Admin only)
  +pst/unclaim <account>              - Unclaim a PST position (Admin only)
```

**Examples**:
```
+pst
+pst/position PST = Garou PST
+pst/add NewPST
+pst/remove FormerPST
+pst/claim NewPST
+pst/unclaim FormerPST
```

---

## Communication Commands

### @emit
**Purpose**: Send messages to a room without your name attached  
**Permission**: All (with some restrictions)  
**File**: `commands/DiesIraeCode/CmdEmit.py`

```
Usage:
  @emit <message>
  @emit/language <message>
```

**Features**:
- Supports language system with `~` tagged speech
- Respects reality layers (Umbra, Material, Dreaming)
- Blocked in Quiet Rooms
- Includes pose break functionality

**Examples**:
```
@emit A cool breeze blows through the room.
@emit "~Bonjour, mes amis!" A voice calls out in French.
@emit/language The entire message is in the set language.
```

---

## Bulletin Board Administration

### +bbs/reset
**Purpose**: Reinitialize the BBS system, wiping all boards and posts  
**Permission**: Admin  
**File**: `commands/bbs/bbs_admin_commands.py`

```
Usage:
  +bbs/reset
```

**⚠️ Critical Warning**: This command completely wipes all bulletin boards and posts. It requires confirmation and cannot be undone. Use only for complete system resets.

**Safety Features**:
- Requires confirmation step
- Creates or reinitializes BBSController
- Resets board numbering system

---

## Safety & Best Practices

### General Safety Guidelines

1. **Always Backup First**: Before running destructive commands, ensure you have recent database backups
2. **Test in Development**: Try commands on a development server first when possible
3. **Read Confirmations**: Many destructive commands have confirmation steps - read them carefully
4. **Document Changes**: Keep logs of major administrative actions
5. **Coordinate with Team**: Inform other staff before major system changes

### High-Risk Commands

These commands can cause permanent data loss or system disruption:

- `+template/clear` - Removes ALL character templates
- `+template/force_uninstall` - Can break character creation
- `+jobs/clear_archive` - Permanently deletes all archived jobs
- `+bbs/reset` - Wipes all bulletin board data
- `@init_area_manager` - Resets area system (should only be run once)

### Permission Best Practices

1. **Principle of Least Privilege**: Only grant the minimum permissions needed
2. **Regular Audits**: Periodically review who has admin access
3. **Storyteller Delegation**: Use Storyteller permissions for story management rather than full admin
4. **Document Permissions**: Keep records of who has what access level

### Recovery Procedures

If something goes wrong:

1. **Stop Immediately**: Don't try to "fix" with more commands
2. **Assess Damage**: Determine what was affected
3. **Restore from Backup**: Use the most recent clean backup
4. **Document Incident**: Record what happened for future prevention
5. **Review Procedures**: Update safety protocols as needed

---

## Command Quick Reference

| Command | Permission | Purpose | Risk Level |
|---------|------------|---------|------------|
| `+migrate` | Admin/Self | Migrate legacy stats | Low |
| `+template` | Admin/Builder | Manage character templates | Medium-High |
| `+mystery` | Admin/Storyteller | Manage investigation mysteries | Low |
| `+storyteller` | Admin | Manage storyteller permissions | Medium |
| `+area` | Builder | Manage game areas | Low |
| `+room` | Builder | Configure room settings | Low |
| `+voteadmin` | Builder | Manage XP systems | Medium |
| `+jobs` | Various | Manage job system | Low-Medium |
| `+staff` | Various | Manage staff listings | Medium |
| `@emit` | All | Room communication | Low |
| `+bbs/reset` | Admin | Reset bulletin boards | **HIGH** |

---

## Getting Help

- Use `help <command>` in-game for detailed command help
- Check command docstrings in the source files
- Consult with other administrators before major changes
- Keep this documentation updated as commands change

---

*Last Updated: September 2025*  
*For the most current information, always check the in-game help system and source code.*
