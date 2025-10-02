# Mystery TypeClass Updates

## Overview

The `mysteries.py` typeclass has been updated to support all the new functionality implemented in the unified mystery command system. These updates ensure full compatibility with the enhanced access control, discovery conditions, and participant management features.

## ✅ **Updates Made**

### **1. New Database Attributes**

Added to `at_script_creation()`:
```python
# Access controls (new)
self.db.access_rules = []      # New flexible access rules
self.db.participants = []      # Mystery participants
```

These new attributes support:
- **Access Rules**: Flexible rule-based access control system
- **Participants**: Character-specific mystery participation tracking

### **2. Enhanced Access Control System**

#### **New Method: `_check_access_rules(character)`**
- Supports multiple access rule types:
  - **Group membership**: `{'type': 'group', 'value': 'vampires'}`
  - **Template requirements**: `{'type': 'template', 'value': 'vampire'}`
  - **Bio requirements**: `{'type': 'clan', 'value': 'ventrue'}`
  - **Skill requirements**: `{'type': 'skill', 'skill': 'investigation', 'level': 3}`
  - **Open access**: `{'type': 'open'}`

#### **Updated `can_discover_clue()` Method**
- Now checks new access rules system first
- Falls back to legacy template restrictions for backward compatibility
- Integrates with modern character stat structure (`character.db.stats`)

### **3. Enhanced Discovery Conditions**

#### **Updated `_check_discovery_conditions()` Method**
- **Participant Access**: Checks if character is mystery participant
- **Skill Requirements**: Validates character skill levels
- **Bio Requirements**: Checks template, clan, tribe, order, etc.
- **Backward Compatibility**: Maintains support for legacy condition formats

#### **New Condition Types Supported**
```python
# Access level conditions
'access_level': 'participant'  # or 'open'

# Skill requirements
'skill_requirements': {
    'investigation': 3,
    'occult': 2
}

# Bio requirements  
'bio_requirements': {
    'template': 'vampire',
    'clan': 'ventrue'
}
```

### **4. Character Stat Integration**

Updated all character data access to use the modern stat structure:
- `character.db.stats.get('skills', {})` - Character skills
- `character.db.stats.get('bio', {})` - Bio information
- `character.db.stats.get('other', {})` - Template and other data
- `character.db.stats.get('attributes', {})` - Attributes
- `character.db.stats.get('merits', {})` - Merits

### **5. Group System Integration**

Added integration with the groups system:
```python
from typeclasses.groups import get_character_groups
char_groups = get_character_groups(character)
```

This enables group-based access control for mysteries.

## **Backward Compatibility**

All updates maintain full backward compatibility:
- Legacy template restrictions still work
- Old discovery condition formats are supported
- Existing mystery data structure is preserved
- No breaking changes to existing functionality

## **New Features Enabled**

These updates enable all the new command functionality:

### **Access Control**
- `+mystery/access <id> = group:vampires`
- `+mystery/access <id> = template:vampire,clan:ventrue`
- `+mystery/access <id> = skill:investigation:3`
- `+mystery/access <id> = open`

### **Participant Management**
- `+mystery/participant <id> = <character>`
- Participant-only clue access via `+mystery/conditions <id>/<clue> = participant`

### **Enhanced Discovery Conditions**
- `+mystery/conditions <id>/<clue> = skill:investigation:3,template:vampire`
- `+mystery/conditions <id>/<clue> = clan:ventrue,participant`

### **Bio-Based Restrictions**
- Support for clan, tribe, order, kith, seeming, auspice, covenant requirements
- Template-specific access control
- Skill-level based access

## **Integration Points**

The updated typeclass integrates with:
- **Groups System**: Character group membership checking
- **Character Stats**: Modern stat structure compatibility  
- **Command System**: All new mystery command functionality
- **Discovery System**: Enhanced clue discovery mechanics

## **Testing Recommendations**

Test the following integration points:

### **Access Control**
- [ ] Group-based mystery access
- [ ] Template-based restrictions
- [ ] Bio field requirements (clan, tribe, etc.)
- [ ] Skill-based access control
- [ ] Open access mysteries

### **Discovery Conditions**
- [ ] Participant-only clues
- [ ] Skill requirement validation
- [ ] Bio requirement checking
- [ ] Legacy condition compatibility

### **Character Integration**
- [ ] Modern stat structure compatibility
- [ ] Group membership integration
- [ ] Template and bio data access

## **Migration Notes**

No migration is required for existing mysteries:
- New attributes are initialized with safe defaults
- Legacy access methods continue to work
- Existing discovery conditions remain functional

## **Conclusion**

The mysteries.py typeclass now fully supports all the enhanced functionality implemented in the unified command system, providing a robust foundation for complex mystery and investigation mechanics while maintaining complete backward compatibility.
