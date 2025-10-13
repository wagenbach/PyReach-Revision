# PyReach Documentation

Complete documentation for PyReach, a Chronicles of Darkness 2nd Edition MUD built on Evennia.

## Quick Navigation

### 📖 For Players

**[COMMANDS.md](COMMANDS.md)** - Complete command reference
- Character commands (+sheet, +stat, +health, +pool)
- Combat system (+combat, +attack, +dodge)
- Social & investigation (+mystery, +social)
- Movement & travel (+ooc, +ic, +hangouts)
- Groups & organizations (+groups, +roster)
- Notes & journals (+note)
- Communication (channels, +page, +bbs)

**[GAME_SYSTEMS.md](GAME_SYSTEMS.md)** - Game mechanics and rules
- Combat system (initiative, attacks, damage)
- Experience & advancement (beats, XP, merits)
- Merit system (prerequisites, categories)
- Mystery & investigation (clues, discovery)
- Equipment & purchasing
- Conditions & tilts
- Social maneuvering
- Storyteller system

### 🔨 For Builders

**[BUILDING_GUIDE.md](BUILDING_GUIDE.md)** - World building and design
- Area management (codes, regions)
- Room system (configuration, setup)
- Places system (locations within rooms)
- Hangout locations (public and group)
- Room tags (categorization)
- Mapping system (coordinates, ASCII maps)
- Building workflow
- Best practices

### 💻 For Developers

**[TYPECLASSES.md](TYPECLASSES.md)** - TypeClass documentation
- Groups system (TypeClass-based groups)
- NPC system (creation, control)
- Mysteries TypeClass (investigations)
- Characters TypeClass (extended functionality)
- Rooms TypeClass (areas, places, tags)

**[TECHNICAL_NOTES.md](TECHNICAL_NOTES.md)** - Implementation details
- Stat access standardization
- OOC/IC system implementation
- Mystery system integration
- Hangout system implementation
- Storyteller integration
- Template system
- Merit instances
- Equipment combat integration
- Development guidelines

---

## Documentation Overview

### What is PyReach?

PyReach is a comprehensive MUD (Multi-User Dungeon) implementation for Chronicles of Darkness 2nd Edition, built on the Evennia MUD framework. It provides:

- **Complete Character System:** Full character sheets with all CoD 2e stats
- **Combat System:** Automated combat with initiative, attacks, and damage tracking
- **Investigation System:** Mystery and clue-based investigation mechanics
- **Social Systems:** Social maneuvering and influence
- **Template Support:** All major CoD 2e supernatural templates
- **Experience System:** Beats, XP, and character advancement
- **Merit System:** Full merit database with prerequisites
- **Group System:** TypeClass-based groups and organizations
- **Building Tools:** Comprehensive world-building commands
- **Storyteller Tools:** Special permissions and NPC management

---

## Getting Started

### For Players

1. **Creating a Character**
   - Use `+stat` to set your character's attributes and skills
   - Set biographical information with `+stat fullname=`, `+stat concept=`, etc.
   - Choose your template (staff-set): Mortal, Vampire, Werewolf, Mage, Changeling, etc.
   - View your sheet with `+sheet`

2. **Learning the Basics**
   - Read [COMMANDS.md](COMMANDS.md) for command syntax
   - Check [GAME_SYSTEMS.md](GAME_SYSTEMS.md) for game rules
   - Use `help <command>` in-game for detailed help
   - Use `+lookup <term>` to search game mechanics

3. **Earning Experience**
   - Gain beats through roleplay and story participation
   - Use `+xp/beat <source>` to record beats
   - Spend XP with `+xp/spend` and `+xp/buy`
   - See [Experience & Advancement](GAME_SYSTEMS.md#experience--advancement)

4. **Finding Roleplay**
   - Use `+hangouts` to see gathering locations
   - Join groups with `+groups`
   - Check `+jobs` for open plots
   - Use channels to coordinate scenes

### For Storytellers

1. **Getting Storyteller Status**
   - Staff grants storyteller permissions with `+storyteller/add`
   - Check your status with `+storyteller/check`
   - View all storytellers with `+storyteller/list`

2. **Running Scenes**
   - Create mysteries with `+mystery/create`
   - Add clues with `+mystery/addclue`
   - Create NPCs with `+npc/create`
   - Control NPCs with `+npc/possess`

3. **Managing Plots**
   - Grant clues to characters with `+mystery/grant`
   - Award beats with staff commands
   - Set environmental conditions
   - Track investigation progress

4. **Resources**
   - See [Storyteller System](GAME_SYSTEMS.md#storyteller-system)
   - See [Mystery & Investigation](GAME_SYSTEMS.md#mystery--investigation)
   - See [NPC System](TYPECLASSES.md#npc-system)

### For Builders

1. **Setting Up Areas**
   - Define areas with `+area/add`
   - View existing areas with `+area/list`
   - See [Area Management](BUILDING_GUIDE.md#area-management)

2. **Creating Rooms**
   - Create with `@create <name>:typeclasses.rooms.Room`
   - Configure with `+room/area`, `+room/coords`, etc.
   - Add places with `places/add`
   - Tag rooms with `+room/tag`
   - See [Room System](BUILDING_GUIDE.md#room-system)

3. **Building Workflow**
   - Follow [Building Workflow](BUILDING_GUIDE.md#building-workflow)
   - Review [Best Practices](BUILDING_GUIDE.md#best-practices)
   - Test thoroughly with `roominfo`

4. **Creating Hangouts**
   - Tag public spaces appropriately
   - Set group hangouts with `+hangout/set`
   - See [Hangout Locations](BUILDING_GUIDE.md#hangout-locations)

### For Developers

1. **Understanding the Codebase**
   - Review [TypeClasses](TYPECLASSES.md) for object structure
   - See [Technical Notes](TECHNICAL_NOTES.md) for implementation details
   - Check [Stat Access Standardization](TECHNICAL_NOTES.md#stat-access-standardization)

2. **Working with Stats**
   - Use unified stat dictionary structure
   - Follow standard access patterns
   - See [Stats Command Refactoring](TECHNICAL_NOTES.md#stats-command-refactoring)

3. **Creating Systems**
   - Follow Evennia best practices
   - Use TypeClasses for game objects
   - Implement proper error handling
   - See [Development Guidelines](TECHNICAL_NOTES.md#development-guidelines)

4. **Contributing**
   - Follow existing code patterns
   - Document new features
   - Test thoroughly
   - Update documentation

---

## System Features

### Character Management
- **Character Sheets:** Full CoD 2e character sheets with UTF-8 support
- **Stats System:** Unified stats dictionary for all character data
- **Bio Fields:** Template-specific biographical information
- **Pools:** Willpower and supernatural resource pool management
- **Health:** Damage tracking with bashing/lethal/aggravated types
- **Conditions & Tilts:** Status effect management
- **Aspirations:** Character goals and beat generation

### Combat
- **Initiative System:** Automated initiative rolls and turn order
- **Attack Types:** Basic, all-out, charge, specified targets, multiple attacks
- **Defense System:** Dodge, block, cover, and defense calculations
- **Weapons:** Full weapon database with stats
- **Armor:** Armor protection and integration
- **Damage:** Automated damage calculation and health tracking
- **Teams:** Team-based combat with friendly fire prevention
- **Surrender:** Diplomatic combat resolution

### Investigation
- **Mysteries:** Complete mystery creation and management
- **Clues:** Prerequisite chains and relationships
- **Discovery Methods:** Examine, search, interview, research
- **Conditions:** Skill requirements, template restrictions
- **Collaboration:** Share clues and collaborate
- **Progress Tracking:** Monitor investigation progress

### Social & Groups
- **Groups:** TypeClass-based groups and organizations
- **Rosters:** View group membership
- **Channels:** Automatic group channels
- **Auto-Assignment:** Template-based group assignment
- **Social Maneuvering:** Influence and persuasion mechanics

### World Building
- **Areas:** Organized regions with auto-numbering
- **Rooms:** Full configuration with hierarchy and tags
- **Places:** Detailed locations within rooms
- **Hangouts:** Quick travel to gathering locations
- **Mapping:** ASCII map generation from coordinates
- **Tags:** Room categorization and discovery

### Experience & Advancement
- **Beats:** Multiple beat sources and tracking
- **Experience:** Automatic conversion (5 beats = 1 XP)
- **Merits:** Full merit database with prerequisites
- **Arcane XP:** Mage-specific arcane experience
- **Voting:** Player voting and recommendation system
- **Weekly Beats:** Alternative automatic XP distribution

### Special Systems
- **Templates:** All major CoD 2e templates supported
- **Legacy Mode:** 1st Edition compatibility
- **Language System:** Multi-language support
- **Notes System:** Character journals and narrative content
- **Equipment:** Inventory and purchasing
- **Jobs:** Request and ticket system
- **BBS:** Bulletin board system

---

## Chronicles of Darkness Templates

PyReach supports these Chronicles of Darkness templates:

### Supernatural Templates
- **Vampire (The Requiem)** - Undead predators (Blood Potency, Vitae)
- **Werewolf (The Forsaken)** - Shapeshifting warriors (Primal Urge, Essence)
- **Mage (The Awakening)** - Reality-bending sorcerers (Gnosis, Mana, Arcane XP)
- **Changeling (The Lost)** - Fae-touched refugees (Wyrd, Glamour)
- **Geist (The Sin-Eaters)** - Death-bound mediums (Synergy, Plasm)
- **Promethean (The Created)** - Artificial beings seeking humanity (Azoth, Pyros)
- **Hunter (The Vigil)** - Mortal monster hunters
- **Demon (The Descent)** - Fallen angels (Primum, Aether)
- **Deviant (The Renegades)** - Twisted experiments (Deviation, Instability)

### Mortal Templates
- **Mortal** - Ordinary humans
- **Mortal+** - Humans with minor supernatural abilities

Each template has:
- Template-specific power stats
- Resource pools
- Biographical fields
- Unique mechanics
- Special abilities

---

## Documentation Structure

This documentation is organized into focused files:

| File | Purpose | Primary Audience |
|------|---------|------------------|
| **README.md** | Index and overview | Everyone |
| **COMMANDS.md** | Command reference | Players, Staff |
| **GAME_SYSTEMS.md** | Game mechanics | Players, Storytellers |
| **BUILDING_GUIDE.md** | World building | Builders |
| **TYPECLASSES.md** | TypeClass systems | Developers, Builders |
| **TECHNICAL_NOTES.md** | Implementation details | Developers |

---

## Additional Resources

### In-Game Help
- `help` - Show help menu
- `help <command>` - Command-specific help
- `+lookup <term>` - Search game mechanics database
- `+commands` - List available commands

### Community Resources
- **Storytellers:** Use `+stwho` to see who's online
- **Staff:** Check `+staff` for staff list
- **Jobs:** Use `+jobs` for requests and support

### External Resources
- **Evennia Documentation:** https://www.evennia.com/docs/
- **Chronicles of Darkness:** Official rulebooks (required for play)
- **World of Darkness Wiki:** https://whitewolf.fandom.com/

---

## Support and Contribution

### Getting Help
1. Check relevant documentation file
2. Use in-game `help <command>`
3. Ask in game channels
4. Contact staff via `+jobs`

### Reporting Issues
1. Check if issue already reported
2. Submit via `+jobs/create bug` in-game
3. Include:
   - What you were trying to do
   - What happened
   - What you expected to happen
   - Any error messages

### Contributing
1. Read [Technical Notes](TECHNICAL_NOTES.md)
2. Follow existing code patterns
3. Document new features
4. Test thoroughly
5. Update relevant documentation

---

## Version History

**Current Version:** 2.0 (Consolidated Documentation)

### Major Changes in 2.0
- Consolidated 33 documentation files into 6 organized files
- Improved navigation with clear categorization
- Added comprehensive index (this file)
- Enhanced cross-referencing between files
- Updated all content to reflect current implementation
- Added quick reference sections

### Previous Versions
- 1.x: Individual documentation files per feature
- Legacy: Scattered documentation and comments

---

## Quick Reference

### Essential Commands
| Command | Purpose |
|---------|---------|
| `+sheet` | View character sheet |
| `+stat <stat>=<value>` | Set character stat |
| `+xp` | View experience |
| `+xp/beat <source>` | Add a beat |
| `+combat/join` | Join combat |
| `+mystery` | View active mysteries |
| `+hangouts` | Travel to gathering places |
| `+note` | Manage character notes |
| `+ooc` | Go to OOC area |
| `help <command>` | Get command help |

### Staff Commands
| Command | Purpose |
|---------|---------|
| `+template` | Manage character templates |
| `+storyteller` | Manage storyteller permissions |
| `+area` | Manage game areas |
| `+room` | Configure rooms |
| `+group` | Manage groups |
| `+npc` | Create/control NPCs |
| `+mystery/create` | Create investigations |
| `+voteadmin` | Configure XP system |

---

## About PyReach

PyReach is an Evennia-based MUD implementation designed specifically for Chronicles of Darkness 2nd Edition. It provides a complete, automated system for running CoD games online with features including:

- Full character management and progression
- Automated combat and conflict resolution
- Investigation and mystery systems
- Social interaction mechanics
- Group and organization management
- Comprehensive world-building tools
- Storyteller support systems
- Experience and advancement tracking

The system is designed to handle the mechanical aspects of CoD gameplay while preserving the narrative focus and storytelling that makes Chronicles of Darkness compelling.

---

**Last Updated:** October 2025  
**System Version:** PyReach 2.0  
**Evennia Version:** Compatible with Evennia 1.0+  
**Chronicles of Darkness:** 2nd Edition

*For the most current information, always check in-game help and these documentation files.*

