# Technical Notes and Implementation Details

Technical documentation for developers working on PyReach systems.

## Table of Contents

1. [Stat Access Standardization](#stat-access-standardization)
2. [OOC/IC System Implementation](#oocic-system-implementation)
3. [Mystery System Integration](#mystery-system-integration)
4. [Hangout System Implementation](#hangout-system-implementation)
5. [Storyteller Integration](#storyteller-integration)
6. [Template System](#template-system)
7. [Merit Instances](#merit-instances)
8. [Equipment Combat Integration](#equipment-combat-integration)
9. [Clue Type System](#clue-type-system)
10. [Stats Command Refactoring](#stats-command-refactoring)

---

## Stat Access Standardization

### Overview
Unified approach to accessing character statistics across the codebase for consistency and maintainability.

### Standard Access Pattern

**Direct Database Access:**
```python
# Access stats dictionary
character.db.stats["attributes"]["mental"]["intelligence"]
character.db.stats["skills"]["physical"]["athletics"]
character.db.stats["advantages"]["health"]
character.db.stats["bio"]["fullname"]
character.db.stats["other"]["template"]
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

**Get Stat with Default:**
```python
def get_stat(character, category, subcategory, stat_name, default=0):
    """
    Safely get a stat with default value.
    
    Args:
        character: Character object
        category: 'attributes', 'skills', 'advantages', 'bio', 'merits'
        subcategory: 'mental', 'physical', 'social' (or None for advantages/bio)
        stat_name: Name of specific stat
        default: Default value if stat doesn't exist
        
    Returns:
        Stat value or default
    """
    if not character.db.stats:
        return default
        
    if subcategory:
        return character.db.stats.get(category, {}).get(subcategory, {}).get(stat_name, default)
    else:
        return character.db.stats.get(category, {}).get(stat_name, default)
```

**Set Stat:**
```python
def set_stat(character, category, subcategory, stat_name, value):
    """
    Set a stat value.
    
    Args:
        character: Character object
        category: 'attributes', 'skills', 'advantages', 'bio', 'merits'
        subcategory: 'mental', 'physical', 'social' (or None)
        stat_name: Name of specific stat
        value: New value
    """
    if not character.db.stats:
        character.db.stats = {}
        
    if subcategory:
        if category not in character.db.stats:
            character.db.stats[category] = {}
        if subcategory not in character.db.stats[category]:
            character.db.stats[category][subcategory] = {}
        character.db.stats[category][subcategory][stat_name] = value
    else:
        if category not in character.db.stats:
            character.db.stats[category] = {}
        character.db.stats[category][stat_name] = value
```

---

### Migration Considerations

**From Old System:**
```python
# Old way (individual attributes)
character.db.intelligence = 3
character.db.wits = 2

# New way (unified dictionary)
character.db.stats["attributes"]["mental"]["intelligence"] = 3
character.db.stats["attributes"]["mental"]["wits"] = 2
```

**Migration Function:**
```python
def migrate_character_stats(character):
    """Migrate character from old individual attributes to new unified stats."""
    if not hasattr(character.db, 'stats'):
        character.db.stats = {}
    
    # Migrate attributes
    old_attrs = ['intelligence', 'wits', 'resolve', 'strength', 'dexterity', 
                 'stamina', 'presence', 'manipulation', 'composure']
    
    for attr in old_attrs:
        if hasattr(character.db, attr):
            # Determine category
            if attr in ['intelligence', 'wits', 'resolve']:
                category = 'mental'
            elif attr in ['strength', 'dexterity', 'stamina']:
                category = 'physical'
            else:
                category = 'social'
            
            # Set in new structure
            set_stat(character, 'attributes', category, attr, getattr(character.db, attr))
            
            # Delete old attribute
            delattr(character.db, attr)
```

---

## OOC/IC System Implementation

### Overview
Location management system preventing desynchronization issues from Dies Irae.

### Anti-Desynchronization Features

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

**Before (Fragmented):**
- `+investigation` (player commands)
- `+mystery` (staff commands)
- Duplicate code in two files

**After (Unified):**
- `+mystery` (all commands)
- Role-based access control
- Single source of truth

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

*For user-facing commands, see COMMANDS.md. For game systems, see GAME_SYSTEMS.md.*

