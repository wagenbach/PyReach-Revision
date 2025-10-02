# Unified Mystery Investigation System

## Overview

The mystery investigation system has been consolidated from two separate command structures (`+investigation` for players and `+mystery` for staff) into a single, unified `+mystery` command that handles both player investigation and staff management functionality through role-based switches.

## Key Changes

### Before (Fragmented System)
- **Player Commands**: `+investigation` with switches like `/examine`, `/search`, `/interview`
- **Staff Commands**: `+mystery` with switches like `/create`, `/addclue`, `/grant`
- **Clue Objects**: Separate `+clueobj` command for staff
- **Duplicate Code**: Similar discovery logic in both files
- **Inconsistent Patterns**: Different from established codebase patterns

### After (Unified System)
- **Single Command**: `+mystery` handles all functionality
- **Role-Based Access**: Automatic permission checking for staff functions
- **Consistent Patterns**: Follows established command structure like BBS system
- **Streamlined Code**: Single discovery method, no duplication
- **Integrated Clue Objects**: Managed through `/clueobj/` subcommands

## Command Structure

### Player Investigation Commands
```
+mystery                          - List active mysteries you can participate in
+mystery <mystery_id>             - View mystery details and your progress
+mystery/progress [mystery_id]    - Show your investigation progress
+mystery/examine <object>         - Carefully examine an object for clues
+mystery/search [area]            - Search an area for hidden clues
+mystery/interview <character>    - Interview someone for information
+mystery/research <topic>         - Research a topic (requires library/resources)
+mystery/share <character> = <clue_name> - Share a mystery clue with another character
+mystery/collaborate <character>  - Begin collaborating on investigations
```

### Staff Mystery Management Commands
```
+mystery/create <title> = <description>
+mystery/list [category]          - List all mysteries (staff view)
+mystery/view <mystery_id>        - View mystery details (staff view)
+mystery/edit <mystery_id>/<field> = <value>
+mystery/delete <mystery_id>
+mystery/status <mystery_id> = <active|solved|suspended>

+mystery/addclue <mystery_id> = <name>/<description>
+mystery/editclue <mystery_id>/<clue_id> = <field>/<value>
+mystery/delclue <mystery_id>/<clue_id>
+mystery/prereq <mystery_id>/<clue_id> = <prerequisite_clue_ids>
+mystery/leads <mystery_id>/<clue_id> = <leads_to_clue_ids>

+mystery/conditions <mystery_id>/<clue_id> = <conditions_json>
+mystery/skillroll <mystery_id>/<clue_id> = <skill>/<attribute>/<difficulty>
+mystery/revelation <mystery_id>/<trigger_id> = <required_clues>/<revelation>
+mystery/access <mystery_id> = <templates|characters|areas>

+mystery/discovered <mystery_id> [character]
+mystery/grant <character> = <mystery_id>/<clue_id>
+mystery/revoke <character> = <mystery_id>/<clue_id>

+mystery/templates                - List available mystery templates
+mystery/template <template_name> = [custom_title] - Create from template
```

### Staff Clue Object Commands
```
+mystery/clueobj/create <name> = <mystery_id>/<clue_id>
+mystery/clueobj/edit <object> = <field>/<value>
+mystery/clueobj/list [here]
+mystery/clueobj/delete <object>
```

## Permission System

The unified system uses the existing permission framework:

- **Player Commands**: No permission check required - available to all players
- **Staff Commands**: Require `check_mystery_permission()` which checks for:
  - Staff permissions (`builders`, `admin`, `staff`)
  - Storyteller flag (`caller.db.storyteller`)

## Aliases

The command supports multiple aliases for backward compatibility:
- `+mystery` (primary)
- `+investigation` (for player familiarity)
- `+inv` (short form)
- `+mysteries` (plural form)
- `+mystadmin` (for staff familiarity)

## Future Enhancements

The unified system provides a solid foundation for future enhancements:

1. **Enhanced Collaboration**: Better mechanics for group investigations
2. **Advanced Discovery**: More sophisticated clue discovery conditions
3. **Dynamic Mysteries**: Time-based or event-triggered mystery evolution
4. **Investigation Tools**: Specialized equipment or abilities for investigations
5. **Reporting System**: Better tracking and reporting of investigation progress

The system is also designed to easily support:
- Mystery templates (placeholder methods exist)
- Advanced revelation triggers
- Time-based mystery mechanics (cron/scripted)
- Enhanced collaboration features
- Reporting and analytics for staff

#### **Edit Mystery** - `+mystery/edit <mystery_id>/<field> = <value>`
- **Fields**: `desc`, `category`, `diff`
- **Difficulty Range**: 1-10 (provides threshold for skill rolls)
- **Examples**:
  - `+mystery/edit 3/desc=This is a new description`
  - `+mystery/edit 3/category=supernatural`
  - `+mystery/edit 3/diff=7`

#### **Delete Mystery** - `+mystery/delete <mystery_id>`
- Completely removes mystery from system
- Deletes all associated clues and clue objects
- Provides confirmation of deletion count

#### **Set Status** - `+mystery/status <mystery_id> = <status>`
- **Valid Statuses**: Active, Hold, Complete, Cancelled
- **Example**: `+mystery/status 3 = hold`

### **Clue Management**

#### **Edit Clue** - `+mystery/editclue <mystery_id>/<clue_id> = <field>/<value>`
- **Fields**: `desc`, `tags`, `prereq`
- **Examples**:
  - `+mystery/editclue 3/clue_0 = desc/This is a new description`
  - `+mystery/editclue 3/clue_1 = tags/incomplete,tainted,critical`
  - `+mystery/editclue 3/clue_2 = prereq/clue_0,clue_1`

#### **Delete Clue** - `+mystery/delclue <mystery_id>/<clue_id>`
- Removes clue from mystery
- Cleans up all references (prerequisites, leads, discoveries)
- **Example**: `+mystery/delclue 3/clue_1`

#### **Set Leads** - `+mystery/leads <mystery_id>/<clue_id> = <target_clue_ids>`
- Links clues together for investigation flow
- Comma-separated list for multiple leads
- **Example**: `+mystery/leads 3/clue_0 = clue_1,clue_2`

### **Discovery Conditions**

#### **Set Conditions** - `+mystery/conditions <mystery_id>/<clue_id> = <conditions>`
- **Condition Types**:
  - `skill:investigation:3` - Requires skill level
  - `template:vampire` - Requires specific template
  - `clan:ventrue` - Requires bio information (clan, tribe, order, kith, etc.)
  - `participant` - Visible to mystery participants only
  - `open` - Visible to anyone
- **Example**: `+mystery/conditions 3/clue_0 = skill:investigation:3,template:vampire`

#### **Add Revelation** - `+mystery/revelation <mystery_id>/<clue_id> = <revelation_text>`
- Provides additional information on exceptional success
- **Example**: `+mystery/revelation 3/clue_0 = You notice something else entirely...`

### **Access Control**

#### **Set Access** - `+mystery/access <mystery_id> = <access_rules>`
- **Access Types**:
  - `group:vampires` - Requires group membership
  - `template:vampire` - Requires template
  - `clan:ventrue` - Requires bio details
  - `skill:investigation:3` - Requires skill level
  - `open` - Accessible to anyone
- **Example**: `+mystery/access 3 = group:vampires,template:vampire`

#### **Add Participant** - `+mystery/participant <mystery_id> = <character>`
- Links character as mystery participant
- Enables participant-only clue access
- **Example**: `+mystery/participant 3 = JohnDoe`

### **Character Management**

#### **Grant Clue** - `+mystery/grant <character> = <mystery_id>/<clue_id>`
- Manually grants clue to character
- **Example**: `+mystery/grant JohnDoe = 3/clue_0`

#### **Revoke Clue** - `+mystery/revoke <character> = <mystery_id>/<clue_id>`
- Removes clue from character
- Cleans up all discovery records
- **Example**: `+mystery/revoke JohnDoe = 3/clue_0`

### **Progress Tracking**

#### **Show Discovered** - `+mystery/discovered <mystery_id> [character]`
- Shows all discovered clues for mystery
- Optional character filter
- **Examples**:
  - `+mystery/discovered 3` - All discoveries
  - `+mystery/discovered 3 JohnDoe` - Specific character

#### **Staff Progress** - `+mystery/staffprogress [mystery_id]`
- Detailed progress view for staff
- Shows completion percentage and participant count
- **Example**: `+mystery/staffprogress 3`

### **Clue Object Management**

#### **Create Clue Object** - `+mystery/clueobj/create <name> = <mystery_id>/<clue_id>`
- Creates discoverable physical objects
- **Example**: `+mystery/clueobj/create "torn letter" = 3/clue_0`

#### **Edit Clue Object** - `+mystery/clueobj/edit <object> = <field>/<value>`
- **Fields**: `discovery_message`, `skill_required`, `difficulty`, `hidden`
- **Example**: `+mystery/clueobj/edit "torn letter" = difficulty/3`

#### **List Clue Objects** - `+mystery/clueobj/list [here]`
- Lists all clue objects or just local ones
- Shows location and discovery status

#### **Delete Clue Object** - `+mystery/clueobj/delete <object>`
- Removes clue object from game
- **Example**: `+mystery/clueobj/delete "torn letter"`

## ✅ **Enhanced Player Commands**

All existing player investigation commands remain fully functional:

- `+mystery` - List available mysteries
- `+mystery <id>` - View mystery details
- `+mystery/progress` - Show investigation progress
- `+mystery/examine <object>` - Examine for clues
- `+mystery/search [area]` - Search for hidden clues
- `+mystery/interview <character>` - Interview for information
- `+mystery/research <topic>` - Research clues
- `+mystery/share <character> = <clue>` - Share clues
- `+mystery/collaborate <character>` - Start collaboration

## **Integration Features**

### **Group System Integration**
- Access control works with existing group system
- `group:groupname` access rules check group membership
- Uses `get_character_groups()` from groups system

### **Character Stats Integration**
- Skill requirements check character skill levels
- Template and bio requirements check character sheet data
- Works with existing character stat structure

### **Difficulty System**
- Mystery difficulty (1-10) sets success thresholds
- Individual clue difficulty overrides mystery default
- Integrates with existing dice roll system

## **Security & Validation**

- All staff commands require `check_mystery_permission()`
- Input validation for all numeric fields
- Clue object field whitelist for security
- Proper cleanup of references when deleting

## **Testing Checklist**

### **Player Commands**
- [x] List mysteries with `+mystery`
- [x] View mystery details with `+mystery <id>`
- [x] Search for clues with `+mystery/search`
- [ ] Examine objects with `+mystery/examine`
- [ ] Share clues with `+mystery/share`
- [ ] Check progress with `+mystery/progress`
- [ ] Test all investigation commands (`/examine`, `/search`, `/interview`, `/research`)
- [ ] Verify mystery listing and progress tracking
- [ ] Test clue sharing and collaboration

### **Staff Testing**:
- [ ] Test mystery creation and management
- [ ] Test clue addition and configuration
- [ ] Test clue object creation and management
- [ ] Verify permission checks work correctly

### **Integration Testing**
- [ ] Create mystery with `+mystery/create`
- [ ] Edit mystery fields with `+mystery/edit`
- [ ] Set mystery status with `+mystery/status`
- [ ] Add clues with `+mystery/addclue`
- [ ] Edit clues with `+mystery/editclue`
- [ ] Set clue conditions with `+mystery/conditions`
- [ ] Set clue leads with `+mystery/leads`
- [ ] Add revelations with `+mystery/revelation`
- [ ] Set access rules with `+mystery/access`
- [ ] Add participants with `+mystery/participant`
- [ ] Grant/revoke clues with `+mystery/grant` and `+mystery/revoke`
- [ ] Create/manage clue objects with `+mystery/clueobj/*`
- [ ] Delete mysteries and clues
- [ ] Group-based access control
- [ ] Template-based restrictions
- [ ] Skill-based discovery conditions
- [ ] Clue prerequisite chains
- [ ] Lead following mechanics
- [ ] Test that existing mysteries continue to work
- [ ] Verify that clue discovery mechanics are unchanged
- [ ] Test that staff can still manage existing mysteries