# Technical Notes and Implementation Details

Technical documentation for developers working on PyReach systems.

## Table of Contents

1. [Character Search & Alias System](#character-search--alias-system)
2. [Safe Dictionary Access Patterns](#safe-dictionary-access-patterns)
3. [Stat Access Standardization](#stat-access-standardization)
4. [OOC/IC System Implementation](#oocic-system-implementation)
5. [Mystery System Integration](#mystery-system-integration)
6. [Hangout System Implementation](#hangout-system-implementation)
7. [Storyteller Integration](#storyteller-integration)
8. [Template System](#template-system)
9. [Merit Instances](#merit-instances)
10. [Equipment Combat Integration](#equipment-combat-integration)
11. [Security Best Practices](#security-best-practices)

---

## Character Search & Alias System

### Overview
Centralized character search system that supports both character names and aliases with global search by default.

**File Location:** `utils/search_helpers.py`

### search_character() Function

```python
def search_character(searcher, search_string, global_search=True, quiet=False):
    """
    Search for a character by name or alias.
    
    Finds characters regardless of whether they are currently logged in.
    
    Args:
        searcher: Object performing the search
        search_string: Name or alias to search for
        global_search: Whether to search globally (default: True)
        quiet: Whether to suppress error messages (default: False)
        
    Returns:
        Character object or None if not found
        
    Note:
        Does NOT check if character is online. For sending messages,
        check target.sessions.all() separately.
    """
```

### Search Priority Order

1. **Exact character name match**
2. **Case-insensitive character name match**
3. **Exact alias match** (from `alias` attribute)
4. **Case-insensitive alias match**

### Global vs Local Search

**Global Search (Default):**
```python
# Finds characters anywhere in the game world
target = search_character(self.caller, "Lys")  
# Finds "Lysander" via alias globally
```

**Local Search:**
```python
# Only searches in current location
target = search_character(self.caller, "Lys", global_search=False)
# Only finds if "Lysander" is in same room
```

### Usage in Commands

**Most commands use global search (default):**
```python
from utils.search_helpers import search_character

class CmdMyCommand(MuxCommand):
    def func(self):
        # Global search - finds characters anywhere, online or offline
        target = search_character(self.caller, self.args)
        if not target:
            return  # Error message already shown
        
        # Use target...
```

**Combat commands use local search:**
```python
def search_combat_target(caller, target_name):
    """Search for combat target (same room + online)."""
    # Local search only
    target = search_character(caller, target_name, global_search=False)
    if not target:
        return None
    
    # Verify same location
    if target.location != caller.location:
        caller.msg(f"{target.name} is not in the same location.")
        return None
    
    # Verify online
    if not target.sessions.all():
        caller.msg(f"{target.name} is not currently online.")
        return None
    
    return target
```

### Benefits

- **Alias support** - All commands automatically support aliases
- **Global search** - Find characters anywhere by default
- **Offline character support** - Finds characters whether online or offline
- **Consistent errors** - Unified "character not found" messages
- **Type safety** - Only returns Character typeclass objects
- **Case insensitive** - Finds "lysander", "Lysander", "LYSANDER"

### Alias System

**Setting Aliases:**
```python
# Player command
alias me=Lys  # Sets alias to "Lys"

# Stored as attribute
character.attributes.add("alias", "Lys")
```

**Using Aliases:**
```python
page Lys=Hello!              # Uses alias (global, requires online)
+finger Lys                  # Uses alias (global, works offline)
+stat Lys/strength=3         # Staff can use alias (global, works offline)
+sheet Lys                   # View sheet (global, works offline)
+combat/attack Lys           # Uses alias (LOCAL ONLY, requires online + same room)
+mystery/grant Lys=1/clue0   # Grant clue (global, works offline)
```

**Note:** Most commands work on offline characters globally. Combat commands require same room + online. Communication commands (page, +txt) require online.

---

## Safe Dictionary Access Patterns

### Overview
Best practices for accessing nested dictionaries safely to prevent KeyError crashes.

### The Problem

**Unsafe (Can Crash):**
```python
# If "attributes" key doesn't exist, raises KeyError
strength = character.db.stats["attributes"]["strength"]

# If "stats" is None or empty dict, crashes
character.db.stats["attributes"][stat] = value
```

### The Solution

**Safe Read with .get():**
```python
# Returns default value if key missing
attributes = character.db.stats.get("attributes", {})
strength = attributes.get("strength", 2)  # Defaults to 2

# One-liner
strength = character.db.stats.get("attributes", {}).get("strength", 2)
```

**Safe Write with Initialization:**
```python
# Initialize nested dicts if missing
if "attributes" not in character.db.stats:
    character.db.stats["attributes"] = {}
character.db.stats["attributes"][stat] = value
```

**Complete Safety Pattern:**
```python
def set_stat_safe(character, category, stat, value):
    """Safely set a stat value."""
    # Ensure base stats dict exists
    if not character.db.stats:
        character.db.stats = {}
    
    # Ensure category dict exists
    if category not in character.db.stats:
        character.db.stats[category] = {}
    
    # Now safe to set
    character.db.stats[category][stat] = value
```

### Applied in Commands

**stats.py uses safe patterns:**
```python
# Before setting attributes
if "attributes" not in target.db.stats:
    target.db.stats["attributes"] = {}
target.db.stats["attributes"][stat] = value

# Before reading (for werewolf forms)
attributes = target.db.stats.get("attributes", {})
strength = attributes.get("strength", 2)
```

### When to Use Each Pattern

**Use .get() for reads:**
- Displaying data
- Calculating values
- Checking existence
- Default fallbacks

**Use initialization for writes:**
- Setting character stats
- Creating new data structures
- Modifying existing data
- Critical operations

---

## Stat Access Standardization

### Overview
Unified approach to accessing character statistics across the codebase for consistency and maintainability.

### Standard Access Pattern

**Safe Database Access (Recommended):**
```python
# Use .get() with defaults for safety
attributes = character.db.stats.get("attributes", {})
intelligence = attributes.get("intelligence", 2)

# For nested access
stats = character.db.stats or {}
health = stats.get("advantages", {}).get("health", 7)
```

**Direct Access (Only When Sure Structure Exists):**
```python
# Use only after initialization or validation
character.db.stats["attributes"]["intelligence"]
character.db.stats["skills"]["athletics"]
character.db.stats["advantages"]["health"]
```

### Stat Structure
```python
db.stats = {
    'attributes': {
        'mental': {'intelligence': 2, 'wits': 2, 'resolve': 2},
        'physical': {'strength': 2, 'dexterity': 2, 'stamina': 2},
        'social': {'presence': 2, 'manipulation': 2, 'composure': 2},
    },
    'skills': {
        'mental': {...},
        'physical': {...},
        'social': {...},
    },
    'advantages': {
        'health': 7,
        'willpower': 4,
        'defense': 2,
        'initiative': 4,
        'speed': 9,
        # Template-specific power stats
        'primal_urge': 0,
        'blood_potency': 0,
        'wyrd': 0,
        'gnosis': 0,
        # etc.
    },
    'bio': {
        'fullname': '',
        'birthdate': '',
        'concept': '',
        'virtue': '',
        'vice': '',
        # Template-specific bio
        'clan': '',
        'covenant': '',
        # etc.
    },
    'merits': {
        'contacts': 3,
        'resources': 2,
        # etc.
    },
    'other': {
        'template': 'mortal',
    }
}
```

---

### Helper Functions

**Get Stat with Default (Safe Pattern):**
```python
def get_stat(character, category, stat_name, default=0):
    """
    Safely get a stat with default value.
    
    Args:
        character: Character object
        category: 'attributes', 'skills', 'advantages', 'bio', 'merits'
        stat_name: Name of specific stat
        default: Default value if stat doesn't exist
        
    Returns:
        Stat value or default
    """
    if not character.db.stats:
        return default
    
    # Simple category access
    category_data = character.db.stats.get(category, {})
    return category_data.get(stat_name, default)

# For modern flattened structure (recommended)
```

**Set Stat (Safe Pattern):**
```python
def set_stat(character, category, stat_name, value):
    """
    Safely set a stat value.
    
    Args:
        character: Character object
        category: 'attributes', 'skills', 'advantages', 'bio', 'merits'
        stat_name: Name of specific stat
        value: New value
    """
    # Initialize base structure
    if not character.db.stats:
        character.db.stats = {}
    
    # Initialize category
    if category not in character.db.stats:
        character.db.stats[category] = {}
    
    # Safe to set now
    character.db.stats[category][stat_name] = value

# For modern flattened structure (recommended)
```

---

## OOC/IC System Implementation

### Overview
Location management system with synchronization features.

### Core Features

#### 1. Direct Object Storage
```python
# Store direct object references, NOT dictionaries
character.db.pre_ooc_location = current_location  # Correct
# NOT: character.db.pre_ooc_location = {"dbref": current_location.id}  # Wrong
```

**Why:**
- Avoids dictionary serialization issues
- Prevents memory/database desynchronization
- Direct references are Evennia-native

---

#### 2. Forced Database Synchronization
```python
# Before movement
character.save()
current_location.save()

# Move character
character.location = new_location

# After movement  
character.save()
new_location.save()
```

**Why:**
- Ensures immediate database update
- Prevents cached data issues
- Critical for preventing desync

---

#### 3. Comprehensive Logging
```python
import logging
logger = logging.getLogger("evennia")

logger.info(f"OOC Movement: {character.name} (#{character.id}) "
           f"from {old_loc.name} (#{old_loc.id}) "
           f"to {new_loc.name} (#{new_loc.id})")
```

**Why:**
- Tracks all movements
- Debugging location issues
- Audit trail for problems

---

#### 4. Location Validation
```python
def validate_location(location):
    """Validate stored location is still valid."""
    if not location:
        return False
    if not location.pk:  # Deleted object
        return False
    if not location.access(character, "view"):  # No access
        return False
    return True
```

---

#### 5. Attribute Cleanup
```python
# After successful return
if hasattr(character.db, 'pre_ooc_location'):
    del character.db.pre_ooc_location
```

**Why:**
- Prevents stale data
- Clears completed operations
- Reduces database clutter

---

### Configuration Options

**In-Game Configuration (Recommended):**
```python
# commands/admin.py - CmdConfigOOCIC
+config/ooc #2              # Set OOC room to dbref #2
+config/ic #1               # Set IC starting room
+config/list                # Show current settings
```

**File Configuration:**
```python
# server/conf/settings.py
OOC_ROOM_DBREF = 2
IC_STARTING_ROOM_DBREF = 1
```

---

### Location Storage Attributes

```python
pre_ooc_location        # Location before using +ooc
pre_summon_location     # Location before being summoned
pre_join_location       # Staff location before using +join
```

---

## Mystery System Integration

### Unified Command Structure

- `+mystery` command handles all investigation functions
- Role-based access control for player vs staff features
- Player commands: examine, search, interview, research
- Staff commands: create, edit, grant clues, manage mysteries
- Single unified codebase for consistency

---

### Permission Checking

```python
def check_mystery_permission(caller):
    """Check if caller has mystery management permissions."""
    # Staff permissions
    if caller.check_permstring("builders"):
        return True
    if caller.check_permstring("admin"):
        return True
    if caller.check_permstring("staff"):
        return True
    
    # Storyteller flag
    if caller.db.storyteller:
        return True
    
    return False
```

---

### Discovery System

**Discovery Methods:**
1. **Examine:** Physical object inspection
2. **Search:** Area searching
3. **Interview:** NPC/character questioning  
4. **Research:** Library/knowledge checks

**Discovery Flow:**
```python
def attempt_discovery(character, clue):
    # 1. Check prerequisites
    if not has_prerequisites(character, clue):
        return False
    
    # 2. Check conditions
    if not meets_conditions(character, clue):
        return False
    
    # 3. Make skill roll if required
    if clue.get('skill_roll'):
        success = make_skill_roll(character, clue['skill_roll'])
        if not success:
            return False
    
    # 4. Grant clue
    grant_clue(character, clue)
    return True
```

---

### Clue Relationships

**Prerequisite System:**
```python
# Clue structure
clue = {
    'id': 'clue_2',
    'prerequisites': ['clue_0', 'clue_1'],  # Need both
    'leads_to': ['clue_3', 'clue_4'],       # Opens these
}

# Check if can discover
def can_discover(character, clue):
    discovered = get_discovered_clues(character)
    prereqs = clue.get('prerequisites', [])
    return all(p in discovered for p in prereqs)
```

---

## Hangout System Implementation

### Tag-Based Discovery

```python
def get_public_hangouts():
    """Get all rooms tagged as hangout locations."""
    from evennia.utils.search import search_tag
    
    hangout_tags = [
        'bar', 'nightclub', 'restaurant', 'cafe',
        'park', 'theater', 'church', 'gathering_hall',
        'marketplace', 'plaza', 'ballroom', 'forum',
        'gym', 'coffee_shop'
    ]
    
    rooms = []
    for tag in hangout_tags:
        tagged_rooms = search_tag(tag, category="room_type")
        rooms.extend(tagged_rooms)
    
    # Remove duplicates
    return list(set(rooms))
```

---

### Group Hangout Storage

```python
# Stored on Group TypeClass
group.db.hangout_location = room_object  # Direct reference

# Access control
def can_access_hangout(character, group):
    return group.is_member(character)
```

---

### Location Memory

```python
def travel_to_hangout(character, destination):
    """Travel to hangout, storing previous location."""
    # Store current location
    character.db.pre_hangout_location = character.location
    
    # Move to destination
    character.location = destination
    
    # Notify
    character.msg(f"You travel to {destination.name}.")
    character.msg("Use +hangouts/return to return to your previous location.")

def return_from_hangout(character):
    """Return to stored location."""
    previous = character.db.pre_hangout_location
    
    # Validate location
    if not previous or not previous.pk:
        character.msg("Your previous location is no longer available.")
        return False
    
    # Move back
    character.location = previous
    
    # Clean up
    del character.db.pre_hangout_location
    
    return True
```

---

## Storyteller Integration

### Permission System

**Storyteller Flag:**
```python
# Grant storyteller permissions
character.db.storyteller = True

# Check storyteller status
def is_storyteller(character):
    return character.db.storyteller or character.check_permstring("storytellers")
```

---

### Permission Hierarchy

```
Developer
    ↓
Admin
    ↓
Builder
    ↓
Storyteller
    ↓
Player
```

**Storyteller Permissions:**
- Create/manage mysteries
- Create/control NPCs
- Grant clues/beats
- Set environmental conditions
- Use building commands in designated areas

---

### NPC Control System

```python
class NPC(Character):
    def at_possess(self, controller):
        """Called when storyteller possesses NPC."""
        self.db.current_controller = controller
        controller.db.possessed_npc = self
        
    def at_release(self):
        """Called when control is released."""
        if self.db.current_controller:
            if hasattr(self.db.current_controller.db, 'possessed_npc'):
                del self.db.current_controller.db.possessed_npc
            self.db.current_controller = None
```

---

## Template System

### Template Storage

**Global Template Cache:**
```python
# server/conf/at_server_startstop.py
def at_server_start():
    from world.cofd.template_handler import TemplateHandler
    
    # Load all templates into memory
    GLOBAL_SCRIPTS['template_handler'] = TemplateHandler()
    GLOBAL_SCRIPTS['template_handler'].load_templates()
```

---

### Template Definition Structure

```python
TEMPLATE = {
    'key': 'vampire',
    'name': 'Vampire (The Requiem)',
    'description': 'Undead predators...',
    'category': 'supernatural',
    
    'power_stat': {
        'name': 'blood_potency',
        'display': 'Blood Potency',
        'min': 0,
        'max': 10,
    },
    
    'resource_pool': {
        'name': 'blood',
        'display': 'Vitae',
        'calculation': 'lookup_table',  # or 'formula'
    },
    
    'bio_fields': {
        'mask': {
            'display': 'Mask',
            'required': True,
            'options': None,  # Free text
        },
        'clan': {
            'display': 'Clan',
            'required': True,
            'options': ['Daeva', 'Gangrel', 'Mekhet', 'Nosferatu', 'Ventrue'],
        },
    },
    
    'unique_traits': {...},
    'special_rules': {...},
}
```

---

### Template Application

```python
def apply_template(character, template_name):
    """Apply template to character."""
    template = get_template(template_name)
    
    # Set template
    character.db.stats['other']['template'] = template_name
    
    # Initialize power stat
    power_stat = template['power_stat']['name']
    character.db.stats['advantages'][power_stat] = 0
    
    # Initialize resource pool
    pool_name = template['resource_pool']['name']
    character.db[f"{pool_name}_current"] = 0
    
    # Set up bio fields
    for field in template['bio_fields']:
        if field not in character.db.stats['bio']:
            character.db.stats['bio'][field] = ''
```

---

## Merit Instances

### Problem
Some merits can be purchased multiple times with different specifications:
- Contacts (one per type)
- Allies (one per organization)
- Status (one per organization)
- Area of Expertise (one per specialty)

### Solution

**Merit Instance Storage:**
```python
db.stats['merits'] = {
    'contacts': [
        {'type': 'police', 'dots': 3},
        {'type': 'media', 'dots': 2},
        {'type': 'criminals', 'dots': 1},
    ],
    'allies': [
        {'organization': 'FBI', 'dots': 2},
        {'organization': 'Medical Board', 'dots': 1},
    ],
    'resources': 3,  # Single-instance merit
}
```

---

### Merit Instance System

```python
def is_instanced_merit(merit_name):
    """Check if merit supports multiple instances."""
    instanced = ['contacts', 'allies', 'status', 'area_of_expertise']
    return merit_name in instanced

def add_merit_instance(character, merit_name, instance_data):
    """Add a merit instance."""
    if merit_name not in character.db.stats['merits']:
        character.db.stats['merits'][merit_name] = []
    
    character.db.stats['merits'][merit_name].append(instance_data)

def get_merit_instances(character, merit_name):
    """Get all instances of a merit."""
    return character.db.stats['merits'].get(merit_name, [])

def remove_merit_instance(character, merit_name, instance_id):
    """Remove a specific merit instance."""
    instances = character.db.stats['merits'].get(merit_name, [])
    if 0 <= instance_id < len(instances):
        del instances[instance_id]
```

---

### Command Interface

```
+xp/buy contacts=police:3    # Buy Contacts (Police) at 3 dots
+xp/buy contacts=media:2     # Buy Contacts (Media) at 2 dots
+xp/list merits/contacts     # List all Contact instances
+xp/refund contacts:1        # Refund specific instance
```

---

## Equipment Combat Integration

### Equipment System

```python
# Character equipment storage
db.equipment = {
    'weapons': ['Light Pistol', 'Knife'],
    'armor': ['Ballistic Vest'],
    'general': ['Lockpicks', 'Flashlight'],
}

# Equipped gear for combat
db.equipped_weapon = 'Light Pistol'
db.equipped_armor = 'Ballistic Vest'
```

---

### Combat Integration

**Weapon Selection:**
```python
def get_equipped_weapon(character):
    """Get character's equipped weapon."""
    weapon_name = character.db.equipped_weapon
    if not weapon_name:
        return None
    
    from world.cofd.weapons import WEAPONS
    return WEAPONS.get(weapon_name)

def calculate_attack_pool(character, weapon):
    """Calculate attack dice pool."""
    # Get attributes and skills
    if weapon['type'] == 'melee':
        attribute = get_stat(character, 'attributes', 'physical', 'strength')
        skill = get_stat(character, 'skills', 'physical', 'weaponry')
    elif weapon['type'] == 'ranged':
        attribute = get_stat(character, 'attributes', 'physical', 'dexterity')
        skill = get_stat(character, 'skills', 'physical', 'firearms')
    
    return attribute + skill
```

---

**Armor Application:**
```python
def apply_armor(character, damage_amount, damage_type):
    """Apply armor to reduce damage."""
    armor = get_equipped_armor(character)
    if not armor:
        return damage_amount
    
    # Check armor type vs damage type
    if damage_type == 'bashing':
        reduction = armor['bashing_protection']
    elif damage_type == 'lethal':
        reduction = armor['lethal_protection']
    else:  # aggravated
        reduction = 0  # Most armor doesn't protect vs aggravated
    
    return max(0, damage_amount - reduction)
```

---

## Clue Type System

### Clue Classification

```python
CLUE_TYPES = {
    'physical': {
        'name': 'Physical Evidence',
        'discovery_method': 'examine',
        'skills': ['investigation', 'science'],
    },
    'testimonial': {
        'name': 'Testimonial Evidence',
        'discovery_method': 'interview',
        'skills': ['empathy', 'subterfuge', 'intimidation'],
    },
    'documentary': {
        'name': 'Documentary Evidence',
        'discovery_method': 'research',
        'skills': ['academics', 'investigation'],
    },
    'forensic': {
        'name': 'Forensic Evidence',
        'discovery_method': 'examine',
        'skills': ['science', 'medicine'],
    },
    'supernatural': {
        'name': 'Supernatural Evidence',
        'discovery_method': 'special',
        'skills': ['occult', 'template-specific'],
    },
}
```

---

### Type-Based Discovery

```python
def discover_clue(character, clue, method):
    """Attempt to discover clue using specified method."""
    clue_type = clue.get('type', 'physical')
    type_data = CLUE_TYPES[clue_type]
    
    # Check if method matches clue type
    if type_data['discovery_method'] != method:
        character.msg(f"This clue cannot be discovered by {method}.")
        return False
    
    # Get appropriate skills for this clue type
    applicable_skills = type_data['skills']
    
    # Make skill roll with best applicable skill
    best_skill = get_best_skill(character, applicable_skills)
    return make_skill_roll(character, best_skill, clue['difficulty'])
```

---

## Stats Command Refactoring

### Old Command Structure
Multiple switches for different stat categories, lots of code duplication.

### New Command Structure

**Unified Setter:**
```python
def set_stat(self):
    """Universal stat setter."""
    # Parse args
    stat_name, value = self.parse_args()
    
    # Determine category
    category, subcategory = self.determine_category(stat_name)
    
    # Validate value
    if not self.validate_value(category, stat_name, value):
        return
    
    # Set stat
    self.caller.db.stats[category][subcategory][stat_name] = value
    self.caller.msg(f"Set {stat_name} to {value}")
```

---

### Category Auto-Detection

```python
def determine_category(self, stat_name):
    """Automatically determine stat category."""
    from world.cofd.stat_dictionary import (
        attribute_dictionary,
        skill_dictionary,
        advantage_dictionary,
    )
    
    # Check attributes
    for category, stats in attribute_dictionary.items():
        if stat_name in stats:
            return ('attributes', category)
    
    # Check skills
    for category, stats in skill_dictionary.items():
        if stat_name in stats:
            return ('skills', category)
    
    # Check advantages
    if stat_name in advantage_dictionary:
        return ('advantages', None)
    
    # Check bio fields
    if stat_name in BIO_FIELDS:
        return ('bio', None)
    
    # Check merits
    if stat_name in MERIT_DATABASE:
        return ('merits', None)
    
    return (None, None)
```

---

### Validation System

```python
def validate_value(self, category, stat_name, value):
    """Validate stat value."""
    # Convert to int
    try:
        value = int(value)
    except ValueError:
        self.caller.msg("Value must be a number.")
        return False
    
    # Check range based on category
    if category == 'attributes':
        if not 1 <= value <= 5:
            self.caller.msg("Attributes must be between 1 and 5.")
            return False
    elif category == 'skills':
        if not 0 <= value <= 5:
            self.caller.msg("Skills must be between 0 and 5.")
            return False
    elif category == 'advantages':
        # Advantages have varying ranges
        max_value = self.get_advantage_max(stat_name)
        if value < 0 or value > max_value:
            self.caller.msg(f"{stat_name} must be between 0 and {max_value}.")
            return False
    
    return True
```

---

## Development Guidelines

### Code Standards

**Naming Conventions:**
```python
# Classes: PascalCase
class CmdMystery(MuxCommand):

# Functions: snake_case
def get_character_stats(character):

# Constants: UPPER_CASE
MAX_ATTRIBUTE_VALUE = 5

# Private methods: _leading_underscore
def _internal_helper(self):
```

---

### Error Handling

```python
def safe_operation(character):
    """Always validate and handle errors."""
    try:
        # Validate input
        if not character:
            logger.error("No character provided to safe_operation")
            return None
        
        # Validate state
        if not hasattr(character.db, 'stats'):
            logger.warning(f"Character {character.name} has no stats")
            character.db.stats = initialize_stats()
        
        # Perform operation
        result = perform_operation(character)
        
        # Validate result
        if result is None:
            logger.warning(f"Operation returned None for {character.name}")
            return default_value()
        
        return result
        
    except Exception as e:
        logger.exception(f"Error in safe_operation for {character.name}: {e}")
        return None
```

---

### Testing Patterns

```python
def test_stat_access():
    """Test stat access patterns."""
    # Create test character
    character = create_character("TestChar")
    
    # Test setting stat
    set_stat(character, 'attributes', 'mental', 'intelligence', 3)
    
    # Test getting stat
    value = get_stat(character, 'attributes', 'mental', 'intelligence')
    assert value == 3, f"Expected 3, got {value}"
    
    # Test default value
    value = get_stat(character, 'attributes', 'mental', 'nonexistent', 0)
    assert value == 0, f"Expected 0, got {value}"
    
    # Clean up
    character.delete()
```

---

### Database Performance

**Batch Operations:**
```python
# Bad: Multiple saves
for character in characters:
    character.db.stat = value
    character.save()  # Expensive!

# Good: Batch update
for character in characters:
    character.db.stat = value
# Single bulk save at end
Character.objects.bulk_update(characters, ['db_attributes'])
```

**Caching:**
```python
# Cache expensive lookups
_template_cache = {}

def get_template(template_name):
    """Get template with caching."""
    if template_name not in _template_cache:
        _template_cache[template_name] = load_template(template_name)
    return _template_cache[template_name]
```

---

### Logging Best Practices

```python
import logging
logger = logging.getLogger("evennia.game")

# Log levels:
logger.debug("Detailed info for debugging")
logger.info("General information")
logger.warning("Warning but not critical")
logger.error("Error that needs attention")
logger.exception("Error with traceback")

# Include context:
logger.info(f"Character {char.name} (#{char.id}) used command {cmd}")
```

---

## Quick Reference

### Common Patterns

**Stat Access:**
```python
value = character.db.stats[category][subcategory][stat_name]
```

**Safe Stat Access:**
```python
value = get_stat(character, category, subcategory, stat_name, default=0)
```

**Location Movement:**
```python
# Store location
character.db.previous_location = character.location

# Move character
character.location = new_location

# Save changes
character.save()
```

**Permission Check:**
```python
if character.check_permstring("builders"):
    # Do builder thing
    pass
```

**Template Check:**
```python
template = character.db.stats.get('other', {}).get('template', 'mortal')
if template == 'vampire':
    # Do vampire thing
    pass
```

---

## Security Best Practices

### Overview
Security patterns and guidelines for safe command development.

**Full Documentation:** See `commands/SECURITY_GUIDELINES.md`

### Essential Patterns

**1. Permission Checking:**
```python
from commands.base import AdminOnlyMixin

class MyCommand(MuxCommand, AdminOnlyMixin):
    def func(self):
        if not self.check_admin_access():
            return  # Error message shown automatically
        # Admin-only code here
```

**2. Input Validation:**
```python
from commands.base import BasePyReachCommand

class MyCommand(BasePyReachCommand):
    def func(self):
        # Validate length
        if not self.validate_input_length(self.args, self.MAX_MESSAGE_LENGTH):
            return
        
        # Sanitize input
        clean_input = self.sanitize_input(self.args)
```

**3. Safe Attribute Access:**
```python
# Use whitelisted attributes only
if attr_name in self.SAFE_DB_ATTRIBUTES:
    value = self.safe_getattr(target, attr_name, default)
    success = self.safe_setattr(target, attr_name, value)
```

**4. Error Handling (No Info Disclosure):**
```python
try:
    dangerous_operation()
except Exception as e:
    logger.log_err(f"Operation failed for {self.caller.name}: {str(e)}")
    self.caller.msg("|rAn error occurred. The issue has been logged.|n")
    # DON'T show str(e) to user!
```

**5. Character Search:**
```python
# For most commands: use search_character with global search
from utils.search_helpers import search_character

target = search_character(self.caller, name)  # Global search, works offline
if not target:
    return  # Error already shown

# For combat commands: use local search only
target = search_character(self.caller, name, global_search=False)  # Same room only
if not target:
    return

# Combat also needs online check
if not target.sessions.all():
    self.caller.msg(f"{target.name} is not currently online.")
    return
```

### Security Checklist

Before committing command code:

- [ ] Uses permission mixins for admin/staff functions
- [ ] Validates all user input lengths
- [ ] Sanitizes user input before processing
- [ ] Uses safe dictionary access patterns
- [ ] No direct setattr/getattr with user-controlled names
- [ ] Error messages don't leak system details
- [ ] Uses search_character for character targeting
- [ ] Logs security-relevant actions
- [ ] No SQL injection risks (uses ORM only)
- [ ] No command injection in execute_cmd calls

---

*For user-facing commands, see COMMANDS.md. For game systems, see GAME_SYSTEMS.md.*

