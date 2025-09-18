# Mystery Investigation System - Implementation Summary

A comprehensive mystery investigation system that transforms investigations from staff-dependent scenes into dynamic, player-driven experiences. The system allows storytellers to create mysteries with discoverable clues that players can find through various investigation methods.

## Key Components

### 1. Core System (`typeclasses/mysteries.py`)
- **Mystery Class**: Persistent script-based mysteries with clue management
- **ClueObject Class**: Physical objects that can be examined for clues
- **MysteryManager**: Utility class for mystery management across the game
- **Progressive Discovery**: Clues can have prerequisites and unlock paths
- **Access Controls**: Template, character, and location-based restrictions
- **Automatic Revelations**: System triggers story reveals when conditions are met

### 2. Staff Commands (`commands/mystery_admin.py`)
- **Mystery Creation**: `+mystery/create`, `+mystery/template`
- **Clue Management**: `+mystery/addclue`, `+mystery/prereq`, `+mystery/conditions`
- **Progress Tracking**: `+mystery/progress`, `+mystery/discovered`
- **Manual Control**: `+mystery/grant`, `+mystery/revoke`
- **Physical Clues**: `+clueobj/create`, `+clueobj/edit`

### 3. Player Commands (Enhanced `commands/investigation.py`)
- **Mystery Discovery**: `+investigation/mysteries`, `+investigation/mystery`
- **Investigation Methods**: `+investigation/investigate`, `/examine`, `/search`, `/research`
- **Social Discovery**: `+investigation/interview`
- **Collaboration**: `+investigation/collaborate`, `+investigation/share`
- **Progress Tracking**: `+investigation/progress`
- **Original Personal Clues**: Still supported alongside new system

### 4. Mystery Templates (`world/mystery_templates.py`)
- **Pre-built Templates**: Missing person, occult, corporate conspiracy, historical
- **Quick Deployment**: Staff can instantly create complex mysteries
- **Customizable**: Templates can be modified with custom titles/descriptions
- **Template Command**: `+mystery/templates`, `+mystery/template <name>`

## How It Works

### For Staff (Storytellers)
1. **Quick Start**: Use templates for instant mystery creation
   ```
   +mystery/templates
   +mystery/template missing_person = The Vanishing Artist
   ```

2. **Custom Creation**: Build mysteries from scratch
   ```
   +mystery/create Custom Mystery = A unique investigation
   +mystery/addclue 1 = First Clue/Description of the clue
   +mystery/prereq 1/clue_1 = clue_0
   ```

3. **Physical Placement**: Add discoverable objects to rooms
   ```
   +clueobj/create torn letter = 1/clue_0
   +clueobj/edit torn letter = discovery_message/You notice something under the desk
   ```

4. **Monitor Progress**: Track player discoveries
   ```
   +mystery/progress 1
   +mystery/discovered 1
   ```

### For Players
1. **Discover Mysteries**: See what investigations are available
   ```
   +investigation/mysteries
   +investigation/mystery 1
   ```

2. **Investigate**: Use various methods to find clues
   ```
   +investigation/investigate
   +investigation/examine object
   +investigation/search area
   +investigation/interview person
   +investigation/research topic
   ```

3. **Collaborate**: Work with other investigators
   ```
   +investigation/collaborate Alice
   +investigation/share Bob = clue_name
   ```

4. **Track Progress**: Monitor investigation advancement
   ```
   +investigation/progress
   ```

## Discovery Methods

### Skill-Based Discovery
- **Investigation Rolls**: Intelligence + Investigation for general discovery
- **Research**: Intelligence + Academics in libraries/computers
- **Social**: Manipulation + Persuasion for interviews
- **Examination**: Perception + Investigation for detailed analysis

### Collaborative Features
- **Clue Sharing**: Players can share discovered information
- **Team Bonuses**: Working together provides investigation bonuses
- **Multiple Perspectives**: Different skills complement each other

### Progressive Revelation
- **Prerequisites**: Some clues require others to be discovered first
- **Conditions**: Skill checks, attribute minimums, merit requirements
- **Automatic Triggers**: System reveals information when conditions are met

## Integration Points

### With Existing Systems
- **Experience System**: Investigation rewards XP
- **Merit System**: Investigation merits provide bonuses
- **Social System**: Interview mechanics tie into social rules
- **Skill System**: Uses existing skill checks and dice mechanics

### Template Compatibility
- **Supernatural Access**: Different templates can access different mysteries
- **Template-Specific Clues**: Vampire-only or Mage-only investigation paths
- **Mortal Mysteries**: Investigations accessible to all character types

## Example Workflow

1. **Staff creates mystery from template**:
   ```
   +mystery/template occult = The Ritual Murders
   ```

2. **Staff places physical clues**:
   ```
   +clueobj/create bloody symbol = 2/clue_1
   ```

3. **Players discover and investigate**:
   ```
   Alice: +investigation/mysteries
   Alice: +investigation/investigate
   Bob: +investigation/examine bloody symbol
   Alice: +investigation/collaborate Bob
   ```

4. **System tracks progress and triggers revelations**:
   ```
   System: REVELATION: The symbols point to an ancient cult...
   ```

5. **Staff monitors and adjusts**:
   ```
   +mystery/progress 2
   +mystery/grant Charlie = 2/clue_3  # Manual intervention if needed
   ```

## Benefits

### For Players
- **Asynchronous Investigation**: Don't need staff present to discover clues
- **Multiple Approaches**: Various investigation methods work
- **Collaborative Gameplay**: Encourages working together
- **Progressive Discovery**: Mysteries unfold naturally over time
- **Skill Integration**: Uses existing character abilities meaningfully

### For Staff
- **Reduced Workload**: Mysteries run themselves once created
- **Template System**: Quick deployment of common mystery types
- **Progress Tracking**: Easy monitoring of player engagement
- **Flexible Control**: Can intervene manually when needed
- **Scalable Stories**: One mystery can engage multiple players over time

### For the Game
- **Enhanced Roleplay**: Provides structure for investigation scenes
- **Player Agency**: Characters drive their own story discoveries
- **Ongoing Plots**: Mysteries can span weeks or months
- **Community Building**: Encourages player collaboration
- **Rich Storytelling**: Supports complex, multi-layered narratives

## Files Modified/Created

### New Files
- `exordium/typeclasses/mysteries.py` - Core mystery system
- `exordium/commands/mystery_admin.py` - Staff management commands
- `exordium/world/mystery_templates.py` - Pre-built mystery templates
- `exordium/docs/MYSTERY_INVESTIGATION_SYSTEM.md` - Comprehensive documentation

### Modified Files
- `exordium/commands/investigation.py` - Enhanced with mystery system integration
- `exordium/commands/default_cmdsets.py` - Added new commands to character cmdset

This system transforms the investigation experience from passive, staff-dependent scenes into active, player-driven narratives while maintaining story control and providing rich, discoverable content.
