# Building and World Design Guide

Complete guide for builders creating rooms, areas, and world content in PyReach.

## Table of Contents

1. [Area Management](#area-management)
2. [Room System](#room-system)
3. [Places System](#places-system)
4. [Hangout Locations](#hangout-locations)
5. [Room Tags](#room-tags)
6. [Mapping System](#mapping-system)
7. [Building Workflow](#building-workflow)
8. [Best Practices](#best-practices)

---

## Area Management

### Overview
Areas are logical groupings of rooms with automatic room code generation. Each area has a two-letter code that prefixes all room codes within that area.

### Area Codes
- **HE** - The Hedge (Changeling realm between Arcadia and reality)
- **SH** - The Shadow (The Hisil/spirit world)
- **WD** - Wilderness (Beyond city or noted locations)
- **CT** - Court Holdings (Changeling court-controlled areas)
- **EL** - Elysium (Vampire organization holdings)

**Room Code Format:** `AREACODE##` (e.g., HE01, HE02, DT12, DT13)

---

### Area Commands

#### List Areas
```
+area/list                   - List all defined areas
```
Shows: codes, names, room counts, next available room number.

#### Add Area
```
+area/add <code>=<name>/<description>
```
**Examples:**
```
+area/add DT=Downtown/The bustling city center
+area/add HI=Highway/Roads leading out of the city
```

**Rules:**
- Code must be exactly 2 letters
- Code must be unique
- Name and description required

---

#### Remove Area
```
+area/remove <code>          - Remove area (if no rooms use it)
```
**Example:**
```
+area/remove HI
```

**Safety:** Cannot remove area if any rooms are assigned to it.

---

#### View Area Info
```
+area/info <code>            - Show detailed area information
+area/rooms <code>           - List all rooms in area
```

**Examples:**
```
+area/info HE                # Show Hedge area details
+area/rooms DT               # List all Downtown rooms
```

---

#### Initialize Area Manager (Admin Only)
```
+area/init                   - Initialize/reset area manager
```
**⚠️ Warning:** One-time setup command. Only run during initial game setup.

---

## Room System

### Creating Rooms

#### Basic Room Creation
```
@create <room name>:typeclasses.rooms.Room
```

**Example:**
```
@create The Crimson Rose:typeclasses.rooms.Room
```

---

### Room Configuration

#### Set Area and Auto-Assign Code
```
+room/area <target>=<area_code>
```

**Target Options:**
- `here` - Current room
- Room name - "The Square"
- Database reference - "#123"

**Examples:**
```
+room/area here=DT           # Auto-assigns next code like DT05
+room/area The Square=DT     # Set specific room to Downtown
+room/area #123=HE           # Set room by dbref to Hedge
```

**What This Does:**
1. Sets room's area code attribute
2. Automatically assigns next sequential room code
3. Sets room's area name in description header
4. Registers room with area manager

---

#### Manual Room Code Override
```
+room/code <target>=<specific_code>
```

**Example:**
```
+room/code here=DT10         # Manually set to DT10
```

**When to Use:**
- Filling gaps in numbering
- Specific room code requirements
- Advanced building scenarios

**⚠️ Note:** Prefer auto-assignment to avoid code conflicts.

---

#### Set Room Coordinates
```
+room/coords <target>=<x>,<y>
```

**Example:**
```
+room/coords here=10,5       # Set coordinates for mapping
```

**Coordinate System:**
- 0,0 is center/reference point
- Positive X is east, negative X is west
- Positive Y is north, negative Y is south
- Used for ASCII map generation

---

#### Set Room Hierarchy
```
+room/hierarchy <target>=<location1>,<location2>,<location3>
```

**Example:**
```
+room/hierarchy here=The Square,Downtown,City Center
```

**Purpose:**
- Shows nested location structure
- Appears in room descriptions
- Helps players understand where they are
- Format: Specific → General

---

#### Enable/Disable Places
```
+room/places <target>=<on|off>
```

**Example:**
```
+room/places here=on         # Enable places system
```

**When On:**
- Players can view and interact with specific places
- Use `places` command to add places to room
- Enhanced roleplay immersion

---

### Room Information

#### View Room Details
```
roominfo                     - Show comprehensive room information
```

**Displays:**
- Database reference (#dbref)
- Area code and area name
- Room code (if assigned)
- Coordinates (if set)
- Hierarchy levels
- Places enabled/disabled
- All exits
- Current occupants
- Room tags

---

## Places System

### Overview
Places are specific locations within a room that players can reference and interact with. They add depth and detail to room descriptions.

### Places Commands

#### Add a Place
```
places/add <name>=<description>
```

**Examples:**
```
places/add The Bar=A long mahogany bar lines the eastern wall, bottles gleaming behind it
places/add Stone Fountain=An ancient fountain sits in the center, water trickling softly
places/add Private Booth=A secluded booth in the corner, perfect for confidential conversations
```

**Guidelines:**
- Name should be distinctive and memorable
- Description should be detailed and evocative
- Consider using sensory details (sight, sound, smell)

---

#### Remove a Place
```
places/remove <number>       - Remove place by number
```

**Example:**
```
places/remove 3              # Remove place #3
```

---

#### List Places
```
places/list                  - List all places in current room
places                       - Same as /list
```

**Output:**
```
Places in The Crimson Rose:
1. The Bar - A long mahogany bar lines the eastern wall
2. Stone Fountain - An ancient fountain sits in the center
3. Private Booth - A secluded booth in the corner
```

---

#### View Place Details
```
places/info <number>         - View detailed place information
```

**Example:**
```
places/info 2
```

---

### Using Places in Roleplay

Players can reference places in poses:
```
look The Bar
pose sits at the Bar, ordering a drink
```

Places provide:
- Detailed descriptions for examination
- Physical locations for character positioning
- Props for roleplay scenes
- Environmental storytelling

---

## Hangout Locations

### Overview
Hangout system provides quick travel to designated social gathering locations. Two types: public hangouts and group hangouts.

### Public Hangouts
Automatically discovered from room tags. Any room with social/gathering tags becomes a public hangout.

#### Creating Public Hangouts
Simply tag rooms appropriately using the room tag system (see Room Tags section).

**Supported Tags:**
- bar, nightclub, restaurant, cafe
- park, theater, church
- gathering_hall, marketplace, plaza
- ballroom, forum, gym, coffee_shop

---

### Group Hangouts

#### Set Group Hangout (Staff/Leader)
```
+hangout/set <group>=<room>
```

**Examples:**
```
+hangout/set Ordo Dracul=The Dragon's Lair
+hangout/set 1=#123          # Set by group ID and room dbref
+hangout/set The Twilight Circle=Circle Sanctum
```

**Who Can Set:**
- Staff members (builders+)
- Group leaders

---

#### Remove Group Hangout
```
+hangout/remove <group>
```

**Example:**
```
+hangout/remove Ordo Dracul
```

---

#### View Group Hangout
```
+hangout/view <group>
```

**Example:**
```
+hangout/view Ordo Dracul
```

**Output:**
```
Group: Ordo Dracul
Hangout Location: The Dragon's Lair (#456)
Area: Old Quarter - Vampire District
```

---

### Hangout Best Practices

**For Public Hangouts:**
- Create varied types (bars, parks, cafes, clubs)
- Spread across different areas
- Include day and night options
- Consider different social atmospheres

**For Group Hangouts:**
- Match location to group theme
- Consider privacy and security
- Provide appropriate amenities
- Reflect group's status and resources

---

## Room Tags

### Overview
Room tags categorize rooms and enable automated systems like hangout discovery.

### Tag System
```
+room/tag <room>=<tag1>,<tag2>,<tag3>
```

**Example:**
```
+room/tag The Crimson Rose=bar,gathering_hall,modern,downtown
+room/tag Central Park=park,gathering_hall,outdoor,public
+room/tag Moonlight Cafe=cafe,restaurant,gathering_hall,romantic
```

---

### Standard Tag Categories

#### Social/Gathering Tags
Designate public hangout locations:
- `bar` - Drinking establishments
- `nightclub` - Dance clubs and nightlife
- `restaurant` - Dining establishments
- `cafe` - Coffee shops and casual eateries
- `gathering_hall` - General social spaces
- `park` - Public parks and outdoor spaces
- `theater` - Performance venues
- `church` - Religious establishments
- `marketplace` - Trading and commerce areas
- `plaza` - Town squares and public spaces
- `ballroom` - Formal gathering spaces
- `forum` - Meeting and discussion areas
- `gym` - Fitness facilities
- `coffee_shop` - Casual coffee establishments

---

#### Location Tags
Describe room characteristics:
- `indoor` / `outdoor`
- `public` / `private` / `restricted`
- `modern` / `historical` / `contemporary`
- `urban` / `rural` / `wilderness`
- `downtown` / `uptown` / `suburbs`
- `safe` / `dangerous`
- `quiet` / `noisy`
- `dark` / `well-lit`

---

#### Supernatural Tags
Mark supernatural significance:
- `hedge` - Changeling hedge locations
- `shadow` - Shadow realm connections
- `locus` - Werewolf loci
- `consecrated` - Sacred ground
- `haunted` - Ghost activity
- `node` - Mage node locations
- `hollow` - Changeling hollows

---

#### Functional Tags
System functionality:
- `ooc` - Out of character area
- `chargen` - Character generation
- `storage` - Equipment storage
- `workshop` - Crafting location
- `library` - Research location
- `hospital` - Healing location
- `armory` - Weapon storage

---

### Tag Usage Guidelines

**Do:**
- Use consistent tags across similar rooms
- Include both type and characteristic tags
- Update tags when room purpose changes
- Use standard tags when possible

**Don't:**
- Over-tag rooms (3-6 tags is usually enough)
- Create redundant custom tags
- Use tags for temporary conditions
- Forget to tag important social spaces

---

## Mapping System

### Overview
ASCII map generation using room coordinates. Still in alpha - basic functionality works but improvements ongoing.

### Setting Up Maps

#### 1. Assign Coordinates to Rooms
```
+room/coords <room>=<x>,<y>
```

**Example Layout:**
```
+room/coords Town Square=0,0      # Center point
+room/coords East Market=1,0      # 1 unit east
+room/coords West Gate=-1,0       # 1 unit west
+room/coords North Road=0,1       # 1 unit north
+room/coords South Path=0,-1      # 1 unit south
+room/coords NE Corner=1,1        # Northeast
```

---

#### 2. Coordinate System
- **Origin (0,0):** Reference point, usually central location
- **X-axis:** Positive = East, Negative = West
- **Y-axis:** Positive = North, Negative = South
- **Distance:** 1 unit = 1 adjacent room

**Planning Tips:**
- Start with center room at 0,0
- Plan grid before building
- Leave gaps for future expansion
- Consider natural geography

---

### Viewing Maps

#### Show Current Area Map
```
+map                         - Show map of current area
```

#### Show Specific Area Map
```
+map <area_code>             - Show map of specific area
```

**Examples:**
```
+map HE                      # Show Hedge area map
+map DT                      # Show Downtown area map
```

---

#### View Map Legend
```
+map/legend                  - Show map symbols and meanings
```

**Standard Symbols:**
- `@` - Your current location
- `#` - Room with players
- `.` - Empty room
- `+` - Exit/intersection
- `|` - North-south connection
- `-` - East-west connection

---

### Map Limitations (Alpha)
- Basic ASCII rendering only
- No diagonal connections yet
- Limited to cardinal directions
- No elevation/z-axis support
- Manual coordinate assignment required
- No automatic layout generation

**Future Improvements Planned:**
- Enhanced rendering
- Diagonal connections
- Multiple z-levels
- Auto-layout suggestions
- Color-coded areas
- Interactive navigation

---

## Building Workflow

### Standard Room Creation Process

#### 1. Plan Area Structure
- Decide area (Downtown, Hedge, etc.)
- Sketch rough map on paper
- Determine coordinate grid
- Plan room connections

#### 2. Create Room
```
@create Room Name:typeclasses.rooms.Room
```

#### 3. Set Basic Description
```
@desc here=Your room description here. Include sensory details, atmosphere, and key features.
```

#### 4. Assign Area and Code
```
+room/area here=DT           # Auto-assigns next available code
```

#### 5. Set Coordinates (If Mapping)
```
+room/coords here=5,3
```

#### 6. Set Hierarchy
```
+room/hierarchy here=Specific Location,Neighborhood,District
```

#### 7. Add Tags
```
+room/tag here=bar,gathering_hall,modern,downtown
```

#### 8. Enable Places (If Appropriate)
```
+room/places here=on
```

#### 9. Add Places
```
places/add The Bar=Description
places/add Corner Table=Description
```

#### 10. Create Exits
```
@dig/tel North Street;n,s = #<destination dbref>
@dig/tel South Alley;s,n = #<destination dbref>
```

#### 11. Verify with roominfo
```
roominfo                     # Check all settings
```

---

### Quick Building Template

```
# Create room
@create The Crimson Rose:typeclasses.rooms.Room

# Set description
@desc here=A dimly lit bar with red velvet curtains and jazz playing softly. The air smells of whiskey and cigarettes.

# Configure room
+room/area here=DT
+room/coords here=2,5
+room/hierarchy here=The Crimson Rose,Entertainment District,Downtown
+room/tag here=bar,gathering_hall,nightlife,modern
+room/places here=on

# Add places
places/add The Bar=A long mahogany bar stretches along the west wall, bottles gleaming
places/add Private Booths=Secluded booths line the eastern wall with red leather seats
places/add Stage=A small stage in the corner where musicians perform nightly

# Create exits
@dig/tel Main Entrance;entrance,out = #456
@dig/tel Back Room;back,front = #789

# Verify
roominfo
```

---

## Best Practices

### Description Writing

**Do:**
- Use sensory details (sight, sound, smell, touch)
- Create atmosphere and mood
- Include notable features players can interact with
- Keep descriptions 2-4 sentences
- Update descriptions for time of day/season if relevant

**Don't:**
- Write novel-length descriptions
- Use overly flowery or purple prose
- Force character reactions or feelings
- Include temporary conditions in permanent description
- Contradict established game lore

---

### Room Organization

**Area Planning:**
- Group related locations in same area
- Maintain consistent theme within areas
- Consider travel time between locations
- Balance busy and quiet areas
- Provide variety in location types

**Exit Management:**
- Use clear exit names
- Include obvious and aliases (n, north, etc.)
- Ensure exits are bidirectional
- Test all exits work correctly
- Consider locked/restricted exits

---

### Places Guidelines

**When to Use Places:**
- Large rooms with multiple distinct features
- Social gathering spaces
- Rooms with interactive elements
- Locations with hidden or special features

**When Not to Use Places:**
- Small, simple rooms
- Corridors and passages
- Temporary locations
- Rooms with few features

**Good Place Examples:**
- "The Bar" in a tavern
- "The Fountain" in a plaza
- "Private Office" in a building
- "Ancient Oak" in a forest

---

### Tag Consistency

**Tagging Standards:**
- Use lowercase for all tags
- Separate words with underscores
- Use singular form (bar not bars)
- Check existing tags before creating new ones
- Document custom tags if creating new categories

**Example Good Tagging:**
```
+room/tag here=bar,gathering_hall,urban,modern,nightlife
```

---

### Coordinate Planning

**Map Design Tips:**
- Start with 0,0 as central or important location
- Use even spacing (1 unit = 1 room typically)
- Plan for future expansion
- Group related locations
- Consider geographic logic

**Example District Layout:**
```
       Park (0,2)
          |
    West (-1,1) - Plaza (0,1) - East (1,1)
          |           |              |
    Shop (-1,0) - Square (0,0) - Market (1,0)
          |           |              |
    Gate (-1,-1) - South (0,-1) - Port (1,-1)
```

---

### Testing and QA

**Before Going Live:**
- [ ] Test all exits both directions
- [ ] Verify room codes assigned correctly
- [ ] Check coordinates on map
- [ ] Ensure tags are appropriate
- [ ] Test places system if enabled
- [ ] Verify descriptions for typos
- [ ] Check area assignment
- [ ] Confirm hierarchy makes sense
- [ ] Test hangout system if applicable
- [ ] Review with another builder

---

### Maintenance

**Regular Tasks:**
- Update seasonal descriptions
- Fix broken exits
- Add new tags as systems expand
- Adjust coordinates if map changes
- Review and update places
- Check for orphaned rooms
- Update area information

**Documentation:**
- Keep notes on custom areas
- Document special features
- Track connected plot locations
- Note any unusual mechanics
- Record area themes and guidelines

---

## Quick Reference

### Essential Commands
| Command | Purpose |
|---------|---------|
| `+area/list` | List all areas |
| `+room/area here=CODE` | Set area and assign code |
| `+room/coords here=X,Y` | Set coordinates |
| `+room/tag here=tags` | Add room tags |
| `places/add name=desc` | Add a place |
| `+map` | View area map |
| `roominfo` | View room details |

### Room Creation Checklist
1. Create room with `@create`
2. Write description with `@desc`
3. Assign area with `+room/area`
4. Set coordinates with `+room/coords`
5. Set hierarchy with `+room/hierarchy`
6. Add tags with `+room/tag`
7. Enable places if needed
8. Add places
9. Create exits
10. Test and verify

---

*For command details, see COMMANDS.md. For game systems, see GAME_SYSTEMS.md.*

