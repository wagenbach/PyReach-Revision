# TypeClass System Documentation

Documentation for custom TypeClasses used in PyReach Chronicles of Darkness.

## Table of Contents

1. [Overview](#overview)
2. [Groups System](#groups-system)
3. [NPC System](#npc-system)
4. [Mysteries TypeClass](#mysteries-typeclass)
5. [Characters TypeClass](#characters-typeclass)
6. [Rooms TypeClass](#rooms-typeclass)

---

## Overview

### What are TypeClasses?
TypeClasses are Evennia's object-oriented database models that combine Django models with Python classes. They provide:
- Automatic attribute persistence
- Built-in event hooks
- Consistent architecture
- Easy customization
- Integration with Evennia's systems

### TypeClass Benefits
- Better than pure Django models for game objects
- Automatic database synchronization
- Event-driven programming
- Inheritance and composition
- Persistent attributes without schema changes

---

## Groups System

### Overview
Groups in PyReach are TypeClass objects, not Django models. This provides better integration with Evennia's systems and easier extensibility.

**File Location:** `typeclasses/groups.py`

---

### Group TypeClass

#### Key Attributes
```python
db.group_id         - Unique numeric identifier
db.group_type       - Type of group (coterie, pack, cabal, etc.)
db.description      - Group description
db.notes            - Private notes (staff/leader only)
db.is_public        - Whether group is publicly visible
db.leader           - Character object who leads the group
db.members          - List of character objects who are members
db.member_data      - Dict storing per-member data (titles, roles, join dates)
```

---

#### Key Methods

**Membership Management:**
```python
add_member(character)        - Add a character to the group
remove_member(character)     - Remove a character from the group
is_member(character)         - Check if character is a member
```

**Member Data:**
```python
get_member_title(character)  - Get member's title
set_member_title(character, title) - Set member's title
get_member_count()           - Get number of members
get_online_members()         - Get list of online members
```

---

### Group Types

The system supports these group types:
- **coterie** - Vampire groups (clans, covenants)
- **pack** - Werewolf groups (tribes, auspices)
- **cabal** - Mage groups (orders, paths)
- **motley** - Changeling groups (courts, seemings)
- **conspiracy** - Hunter groups (organizations)
- **agency** - Mortal organizations
- **cult** - Religious/occult groups
- **other** - Generic groups

---

### Automatic Features

#### Channel Creation
Each group automatically gets its own channel:
- Channel name derived from group name (alphanumeric only)
- Proper locks restrict access to members and staff
- Members automatically subscribed/unsubscribed on join/leave

**Example:**
```python
group_name = "Ordo Dracul"
channel_name = "ordodracul"  # Auto-generated
```

---

#### Character Attributes
Characters maintain a `groups` attribute listing memberships:
```python
character.db.groups = [1, 5, 12]  # List of group IDs
```

**Benefits:**
- Quick membership lookup
- Updated automatically on join/leave
- Synchronized with actual group membership

---

#### Auto-Assignment
Characters automatically assigned to appropriate groups based on characteristics:
- Template-based groups (Vampire, Mage, etc.)
- Clan/covenant groups for vampires
- Order/path groups for mages
- Similar logic for other templates

**Auto-Assignment Logic:**
```python
# Example for Vampire
if template == "vampire":
    - Add to "All Vampires" group
    - Add to clan group if clan set
    - Add to covenant group if covenant set
```

---

### Migration from Django Models

If you have existing Django model groups, use the migration script:

```python
# In Evennia shell (@py command)
exec(open('world/groups/migrate_to_typeclass.py').read())
migrate_groups_to_typeclass()
```

**Migration Process:**
1. Converts all Django Group objects to TypeClass Groups
2. Migrates all memberships and member data
3. Preserves leaders, titles, descriptions, etc.
4. Creates channels for all groups

**After Verification:**
```python
# DANGEROUS - only after verifying migration worked
cleanup_old_django_groups()
```

---

### Integration Points

#### Lock Functions
```python
def group_member(accessing_obj, accessed_obj, *args, **kwargs):
    """Lock function for group membership."""
    group_id = int(args[0])
    group = get_group_by_id(group_id)
    return group.is_member(accessing_obj) if group else False
```

**Usage in Locks:**
```python
channel.locks.add("listen:group_member(5)")  # Only group 5 members
room.locks.add("enter:group_member(12)")     # Only group 12 members
```

---

#### Admin Commands
Group management in admin commands:
- `approve` - Auto-assigns character to appropriate groups
- `unapprove` - Removes character from all groups
- `+massunapprove` - Bulk removes all characters from groups

---

#### Utility Functions
**File Location:** `world/groups/utils.py`

```python
auto_assign_character_groups(character)
    - Auto-assign based on characteristics

assign_character_to_group(character, group)
    - Manual assignment

remove_character_from_group(character, group)
    - Manual removal

get_character_groups(character)
    - Get character's groups

sync_character_group_attributes(character)
    - Sync attributes
```

---

### Customization

#### Creating Custom Group Types

**Define New Group Type:**
```python
# In server/conf/settings.py or appropriate config
GROUP_TYPES = {
    'custom_type': {
        'name': 'Custom Group',
        'description': 'A custom group type',
        'permissions': ['special_perm'],
    }
}
```

#### Adding Custom Methods

**Extend Group TypeClass:**
```python
# In typeclasses/groups.py

class Group(DefaultObject):
    # ... existing code ...
    
    def custom_method(self):
        """Add custom group functionality."""
        # Your custom code here
        pass
```

---

### Example Usage

#### Creating a Group
```python
from evennia import create_object
from typeclasses.groups import Group

group = create_object(
    Group,
    key="Ordo Dracul",
    attributes=[
        ("group_type", "coterie"),
        ("description", "A vampire covenant dedicated to understanding their curse"),
        ("is_public", True),
    ]
)
```

#### Managing Members
```python
# Add member
group.add_member(character)

# Check membership
if group.is_member(character):
    print(f"{character.name} is a member")

# Set title
group.set_member_title(character, "Kogaion")

# Remove member
group.remove_member(character)
```

---

## NPC System

### Overview
NPCs (Non-Player Characters) are specialized Character TypeClass objects that can be created and controlled by storytellers.

**File Location:** `typeclasses/npcs.py`

---

### NPC TypeClass

#### Key Attributes
```python
db.npc              - Boolean flag marking as NPC
db.creator          - Character who created the NPC
db.description      - NPC description
db.stats            - Dict of NPC statistics
db.notes            - Private storyteller notes
db.current_controller - Character currently controlling NPC
```

---

#### NPC Features

**Creation:**
- Created by storytellers using `+npc/create`
- Assigned statistics like player characters
- Can have full character sheets

**Control:**
- Storytellers can possess NPCs
- Issue commands as the NPC
- Release control when done

**Persistence:**
- NPCs remain in game world
- Can be controlled by different storytellers
- Stats and attributes persist

---

### NPC Commands (Storyteller)

```
+npc/create <name>           - Create an NPC
+npc/list                    - List all NPCs
+npc/delete <npc>            - Delete an NPC
+npc/desc <npc>=<description> - Set NPC description
+npc/stat <npc>/<stat>=<value> - Set NPC stat
+npc/possess <npc>           - Possess/control an NPC
+npc/release                 - Release NPC control
```

---

### Example NPC Usage

**Creating an NPC:**
```
+npc/create Marcus the Informant
+npc/desc Marcus=A shifty-eyed man in a worn coat
+npc/stat Marcus/wits=3
+npc/stat Marcus/manipulation=4
+npc/stat Marcus/streetwise=3
```

**Controlling an NPC:**
```
+npc/possess Marcus
say "I heard something interesting at the docks..."
emote leans in conspiratorially
+npc/release
```

---

## Mysteries TypeClass

### Overview
Mysteries are TypeClass objects representing investigation scenarios with clues, conditions, and revelations.

**File Location:** `typeclasses/mysteries.py`

---

### Mystery TypeClass

#### Key Attributes
```python
db.mystery_id       - Unique mystery identifier
db.title            - Mystery title
db.description      - Mystery description
db.category         - Mystery category (supernatural, mundane, etc.)
db.difficulty       - Base difficulty rating (1-10)
db.status           - Status (active, solved, suspended)
db.clues            - List of clue dictionaries
db.access_rules     - Access control rules
db.participants     - List of character participants
```

---

#### Clue Structure

Each clue is a dictionary with:
```python
{
    'id': 'clue_0',
    'name': 'Blood Stain',
    'description': 'A dark stain on the floor',
    'discovered_by': [],  # List of characters who found it
    'prerequisites': [],  # Required clues
    'leads_to': [],       # Clues this one leads to
    'conditions': {},     # Discovery conditions
    'revelation': '',     # Extra info on exceptional success
    'tags': [],           # Clue tags
}
```

---

### Discovery Conditions

Clues can have various discovery conditions:
- **Skill Requirements:** `skill:investigation:3`
- **Template Requirements:** `template:vampire`
- **Bio Requirements:** `clan:ventrue`
- **Participant Only:** `participant`
- **Open Access:** `open`

**Example:**
```python
conditions = {
    'skill_requirements': ['investigation:3'],
    'template_requirements': ['vampire'],
}
```

---

### Mystery Methods

```python
add_clue(name, description)
    - Add a new clue to mystery

remove_clue(clue_id)
    - Remove a clue

grant_clue(character, clue_id)
    - Grant clue to character

revoke_clue(character, clue_id)
    - Revoke clue from character

check_access(character)
    - Check if character can access mystery

get_available_clues(character)
    - Get clues character can discover

get_discovered_clues(character)
    - Get clues character has found
```

---

### Example Mystery Setup

```python
from evennia import create_object
from typeclasses.mysteries import Mystery

# Create mystery
mystery = create_object(
    Mystery,
    key="The Missing Heir",
    attributes=[
        ("mystery_id", 1),
        ("title", "The Missing Heir"),
        ("description", "A wealthy family's heir has vanished"),
        ("category", "investigation"),
        ("difficulty", 5),
        ("status", "active"),
    ]
)

# Add clues
mystery.add_clue(
    "Torn Letter",
    "A letter with half the address torn off"
)

# Set conditions
clue = mystery.db.clues[0]
clue['conditions'] = {
    'skill_requirements': ['investigation:2'],
}
```

---

## Characters TypeClass

### Overview
Extended character TypeClass with Chronicles of Darkness-specific functionality.

**File Location:** `typeclasses/characters.py`

---

### Character Extensions

#### Stats System
```python
db.stats = {
    'attributes': {
        'mental': {'intelligence': 2, 'wits': 2, 'resolve': 2},
        'physical': {'strength': 2, 'dexterity': 2, 'stamina': 2},
        'social': {'presence': 2, 'manipulation': 2, 'composure': 2},
    },
    'skills': {
        'mental': {'academics': 0, 'computer': 0, ...},
        'physical': {'athletics': 0, 'brawl': 0, ...},
        'social': {'animal_ken': 0, 'empathy': 0, ...},
    },
    'advantages': {
        'health': 7,
        'willpower': 4,
        'defense': 2,
        'initiative': 4,
        'speed': 9,
    },
    'bio': {
        'fullname': 'John Smith',
        'concept': 'Detective',
        'virtue': 'Justice',
        'vice': 'Wrath',
    },
    'other': {
        'template': 'vampire',
    }
}
```

---

#### Resource Pools
```python
db.willpower_current    - Current willpower
db.essence_current      - Werewolf essence
db.blood_current        - Vampire vitae
db.glamour_current      - Changeling glamour
db.mana_current         - Mage mana
db.plasm_current        - Geist plasm
# ... etc for other templates
```

---

#### Experience System
```python
db.beats               - Current beats (5 = 1 XP)
db.experience          - Current experience points
db.arcane_beats        - Mage arcane beats (if applicable)
db.arcane_experience   - Mage arcane XP (if applicable)
db.beat_history        - Log of beat gains
db.xp_history          - Log of XP spends
```

---

#### Conditions and Tilts
```python
db.conditions          - List of active conditions
db.tilts               - List of active tilts
```

---

#### Groups and Organizations
```python
db.groups              - List of group IDs character belongs to
```

---

#### Notes System
```python
db.notes = [
    {
        'title': 'My Backstory',
        'category': 'Background',
        'text': 'I was born in...',
        'approved': False,
        'created': '2025-01-01 12:00:00',
        'modified': '2025-01-01 12:00:00',
    },
    # ... more notes
]
```

---

### Character Methods

**Template System:**
```python
get_template()
    - Get character's template

set_template(template_name)
    - Set character's template

get_template_data()
    - Get full template configuration
```

**Stat Management:**
```python
get_stat(category, stat_name)
    - Get a stat value

set_stat(category, stat_name, value)
    - Set a stat value

get_derived_stats()
    - Calculate derived stats (health, speed, etc.)
```

**Pool Management:**
```python
get_pool(pool_name)
    - Get current/max pool values

spend_pool(pool_name, amount)
    - Spend from pool

gain_pool(pool_name, amount)
    - Gain pool points
```

---

## Rooms TypeClass

### Overview
Extended room TypeClass with area management, places system, and tag support.

**File Location:** `typeclasses/rooms.py`

---

### Room Extensions

#### Area System
```python
db.area_code           - Two-letter area code (DT, HE, etc.)
db.area_name           - Full area name
db.room_code           - Full room code (DT05, HE12, etc.)
db.coordinates         - Tuple of (x, y) coordinates
db.hierarchy           - List of location names (specific to general)
```

---

#### Places System
```python
db.places_enabled      - Boolean for places system
db.places = [
    {
        'name': 'The Bar',
        'description': 'A long mahogany bar...',
        'number': 1,
    },
    # ... more places
]
```

---

#### Tags System
```python
# Using Evennia's built-in tag system
room.tags.add('bar')
room.tags.add('gathering_hall')
room.tags.has('bar')  # Returns True
room.tags.all()       # Returns all tags
```

---

### Room Methods

**Area Management:**
```python
set_area(area_code)
    - Set room's area and auto-assign code

set_coordinates(x, y)
    - Set room coordinates for mapping

get_area_info()
    - Get full area information
```

**Places Management:**
```python
add_place(name, description)
    - Add a place to the room

remove_place(number)
    - Remove a place by number

get_place(number)
    - Get place details

list_places()
    - Get all places in room
```

---

### Room Display

Rooms automatically format their display with:
- Area code and name in header
- Hierarchy display
- Available places list
- Exit directions
- Occupant list

**Example Display:**
```
[ DT05: The Crimson Rose ][ Downtown - Entertainment District ]

A dimly lit bar with red velvet curtains and jazz playing softly.

Places: The Bar (1), Private Booths (2), Stage (3)

Exits: Main Entrance (entrance, out), Back Room (back)

Characters: Alice, Bob
```

---

## Quick Reference

### TypeClass Hierarchy
```
DefaultObject (Evennia)
├── Group (Groups)
├── Mystery (Investigations)
└── DefaultCharacter (Evennia)
    ├── Character (Player Characters)
    └── NPC (Non-Player Characters)

DefaultRoom (Evennia)
└── Room (Game Rooms)
```

### Common TypeClass Patterns

**Creating TypeClass Objects:**
```python
from evennia import create_object
from typeclasses.groups import Group

obj = create_object(Group, key="Name", attributes=[...])
```

**Accessing Attributes:**
```python
# Persistent attributes (database)
obj.db.attribute_name = value

# Non-persistent attributes (memory only)
obj.ndb.temp_data = value
```

**Custom Methods:**
```python
class CustomTypeClass(DefaultObject):
    def at_object_creation(self):
        """Called when object is first created."""
        self.db.custom_attribute = "value"
    
    def custom_method(self):
        """Add custom functionality."""
        pass
```

---

*For commands using these systems, see COMMANDS.md. For game mechanics, see GAME_SYSTEMS.md.*

