# PyReach

## Overview

PyReach is a full-featured MUD/MUSH system built on the Evennia framework, designed specifically for Chronicles of Darkness (CoFD) gameplay (also known as new World of Darkness, nWoD, with an eye towards the 2nd edition framework). It provides storytellers and players with an immersive, automated environment for supernatural roleplaying with extensive character management, character generation, investigation systems, and admin tools for staff and player-empowered storytellers.

## 🎮 Core Features

### **Character Management System**
- **Complete Chronicles of Darkness Integration**: Full support for all major CoFD game lines
- **Dynamic Template System**: Modular, Python-based character templates with validation
- **Merit & Flaw System**: Comprehensive merit tracking with template-specific options
- **Conditions & Tilts**: Automated tracking of temporary character states
- **Experience System**: Automated XP tracking and spending with approval workflows, designed for either automated XP weekly or a +vote based XP depending on your game

### **Storytelling Tools**
- **Mystery Investigation System**: Dynamic, clue-based mysteries with progressive discovery
- **NPC Management**: Complete NPC creation, control, and interaction systems
- **Area Management**: Sophisticated room and area organization tools
- **Storyteller Permissions**: Dedicated storyteller role with appropriate access controls
- **Jobs System**: Comprehensive ticket management for player requests and staff tasks

### **Roleplay Enhancement**
- **Combat System**: Automated Chronicles of Darkness combat with initiative tracking
- **Social Systems**: Groups, rosters, and organization management
- **Communication Tools**: Enhanced channels, bulletin boards, and messaging systems
- **Investigation Commands**: Comprehensive tools for mystery solving and clue discovery

### **Administrative Features**
- **Permission System**: Granular access controls for different staff levels
- **Web Integration**: Django-powered web interface for character and game management
- **Database Management**: Robust data storage with backup and recovery systems
- **Logging & Monitoring**: Comprehensive activity tracking and system monitoring

## Available Character Templates

PyReach supports all major Chronicles of Darkness game lines with fully implemented templates:

### **Core Templates**
- **[Mortal](https://github.com/soma-satoro/PyReach/blob/main/docs/TEMPLATE_SYSTEM_SUMMARY.md)** - Basic human characters
- **[Mortal+](https://github.com/soma-satoro/PyReach/blob/main/docs/TEMPLATE_SYSTEM_SUMMARY.md)** - Mortals with minor supernatural abilities (Psychics, Ghouls, Wolf-Blooded, etc.)

### **Major Supernatural Templates**
- **[Vampire](https://github.com/soma-satoro/PyReach/blob/main/docs/TEMPLATE_SYSTEM_SUMMARY.md)** - Vampire: The Requiem (Clans, Covenants, Disciplines)
- **[Mage](https://github.com/soma-satoro/PyReach/blob/main/docs/TEMPLATE_SYSTEM_SUMMARY.md)** - Mage: The Awakening (Paths, Orders, Arcana)
- **[Werewolf](https://github.com/soma-satoro/PyReach/blob/main/docs/TEMPLATE_SYSTEM_SUMMARY.md)** - Werewolf: The Forsaken (Auspices, Tribes, Gifts)
- **[Changeling](https://github.com/soma-satoro/PyReach/blob/main/docs/TEMPLATE_SYSTEM_SUMMARY.md)** - Changeling: The Lost (Seemings, Courts, Contracts)


### **Limited Run Templates**
- **[Hunter](https://github.com/soma-satoro/PyReach/blob/main/docs/TEMPLATE_SYSTEM_SUMMARY.md)** - Hunter: The Vigil (Compacts, Conspiracies, Tactics)
- **[Geist](https://github.com/soma-satoro/PyReach/blob/main/docs/TEMPLATE_SYSTEM_SUMMARY.md)** - Geist: The Sin-Eaters (Thresholds, Krewe, Manifestations)
- **[Promethean](https://github.com/soma-satoro/PyReach/blob/main/docs/TEMPLATE_SYSTEM_SUMMARY.md)** - Promethean: The Created (Lineages, Refinements, Transmutations)
- **[Demon](https://github.com/soma-satoro/PyReach/blob/main/docs/TEMPLATE_SYSTEM_SUMMARY.md)** - Demon: The Descent (Incarnations, Agendas, Embeds)
- **[Beast](https://github.com/soma-satoro/PyReach/blob/main/docs/TEMPLATE_SYSTEM_SUMMARY.md)** - Beast: The Primordial (Families, Hungers, Nightmares)
- **[Mummy](https://github.com/soma-satoro/PyReach/blob/main/docs/TEMPLATE_SYSTEM_SUMMARY.md)** - Mummy: The Curse (Guilds, Decrees, Utterances)
- **[Deviant](https://github.com/soma-satoro/PyReach/blob/main/docs/TEMPLATE_SYSTEM_SUMMARY.md)** - Deviant: The Renegades (Origins, Forms, Scars)
- **Yes I know Changeling technically counts here, but given its popularity it's in the major templates.**

## Documentation & Guides

### **System Documentation**
- **[Template System](https://github.com/soma-satoro/PyReach/blob/main/docs/TEMPLATE_SYSTEM_SUMMARY.md)** - Complete guide to character templates and customization
- **[Merit System](https://github.com/soma-satoro/PyReach/blob/main/docs/README_merit_system.md)** - Merit  implementation details with some examples
- **[Combat System](https://github.com/soma-satoro/PyReach/blob/main/docs/README_combat_system.md)** - Chronicles of Darkness combat mechanics (automated combat, very alpha)
- **[Conditions & Tilts](https://github.com/soma-satoro/PyReach/blob/main/docs/README_tilt_system.md)** - Temporary character state management (not as tested as I would like)

### **Storytelling Tools**
- **[Mystery System](https://github.com/soma-satoro/PyReach/blob/main/docs/MYSTERY_SYSTEM_SUMMARY.md)** - Complete mystery and investigation framework (not tested at all, still WIP)
- **[Investigation Commands](https://github.com/soma-satoro/PyReach/blob/main/docs/MYSTERY_INVESTIGATION_SYSTEM.md)** - Player tools for mystery solving (same as mystery system)
- **[NPC System](https://github.com/soma-satoro/PyReach/blob/main/docs/npc_system.md)** - NPC creation and management tools
- **[Storyteller Integration](https://github.com/soma-satoro/PyReach/blob/main/docs/STORYTELLER_INTEGRATION_SUMMARY.md)** - Player storyteller permissions and tools
- **[Storyteller System](https://github.com/soma-satoro/PyReach/blob/main/docs/STORYTELLER_SYSTEM.md)** - Advanced storytelling features

### **Administrative Guides**
- **[Area Management](https://github.com/soma-satoro/PyReach/blob/main/docs/AREA_MANAGEMENT.md)** - Room and area organization systems (cribbed from how The Reach and Fallcoast did their grid locations)
- **[Room System Usage](https://github.com/soma-satoro/PyReach/blob/main/docs/ROOM_SYSTEM_USAGE.md)** - Advanced room features and management
- **[Groups & Rosters](https://github.com/soma-satoro/PyReach/blob/main/docs/groups_and_rosters.md)** - Organization and group management (not as tested as I would like as of this writing)
- **[Groups System](https://github.com/soma-satoro/PyReach/blob/main/docs/typeclass_groups_system.md)** - Technical implementation of group systems

### **Player Resources**
- **[Character Commands](https://github.com/soma-satoro/PyReach/blob/main/docs/README_character_commands.md)** - Complete player command reference
- **[Equipment & Combat Integration](https://github.com/soma-satoro/PyReach/blob/main/docs/README_equipment_combat_integration.md)** - Equipment system and combat integration

### **Setup & Migration**
- **[TinyMUX Setup](https://github.com/soma-satoro/PyReach/blob/main/docs/TINYMUX_SETUP.md)** - Migration guide from TinyMUX systems (this works *sort of*, but needs a lot more work to get things going properly)

## 🛠️ Technical Features

- **Built on Evennia**: Leverages the powerful Evennia MUD framework
- **Django Integration**: Full web interface with admin tools
- **Python-Based Templates**: Type-safe, IDE-friendly character template system
- **Modular Architecture**: Easy to extend and customize for specific games
- **Database Persistence**: Robust data storage with automatic backups
- **Multi-Protocol Support**: Telnet, SSH, and web client compatibility

## 🚀 Getting Started

1. **Installation**: Set up Evennia and clone the PyReach repository
2. **Configuration**: Configure your game settings and database
3. **Template Setup**: Install character templates using `+template/install builtin`
4. **World Building**: Use area management tools to create your game world
5. **Player Onboarding**: Set up character creation and approval workflows

## 🤝 Contributing

PyReach is actively developed and welcomes contributions. Whether you're adding new templates, fixing bugs, or enhancing existing systems, your contributions help make the platform better for everyone.

## 📄 License

This project is built for the Chronicles of Darkness community and follows appropriate licensing for derivative works based on the World of Darkness intellectual property.
