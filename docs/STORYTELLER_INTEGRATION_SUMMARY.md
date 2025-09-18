# Storyteller System Integration Summary

## What We Added

A comprehensive Storyteller flag system that allows trusted players to use staff-level storytelling tools without full administrative permissions.

## Key Components

### 1. Permission System Updates (`world/utils/permission_utils.py`)
- **`check_storyteller_permission(caller)`**: Checks for Storyteller flag on character or account
- **`check_mystery_permission(caller)`**: Combined check for staff or storyteller permissions  
- **Updated existing functions**: All staff permission checks now include Storyteller flag support
- **Dual Storage**: Storyteller flags stored on both character and account for persistence

### 2. Storyteller Management Commands (`commands/storyteller_admin.py`)
- **`+storyteller/add <character>`**: Grant Storyteller flag (Admin only)
- **`+storyteller/remove <character>`**: Remove Storyteller flag (Admin only)
- **`+storyteller/list`**: List all current storytellers
- **`+storyteller/check [character]`**: Check Storyteller status
- **`+storyteller/info`**: Show system information and permissions
- **`+stwho`**: Quick command to see online storytellers and staff

### 3. Mystery System Integration
- **Permission Updates**: All mystery commands now check for Storyteller permissions
- **Command Category**: Changed from "Staff Commands" to "Storytelling Commands"
- **Access Control**: Storytellers can create, manage, and track mysteries
- **Clue Objects**: Storytellers can place physical clue objects in rooms

### 4. NPC System Integration  
- **Creation Access**: Storytellers can create and generate NPCs
- **Control Permissions**: Storytellers can puppet and control NPCs
- **Management Tools**: Access to NPC stats, damage, and healing commands
- **Command Category**: Changed from "Roleplaying Tools" to "Storytelling Commands"

## How It Works

### For Admins
```bash
# Grant storyteller permissions
+storyteller/add Alice

# Remove storyteller permissions  
+storyteller/remove Bob

# Check who has storyteller permissions
+storyteller/list

# Check specific character
+storyteller/check Alice
```

### For Storytellers
Once granted the flag, storytellers gain access to:

```bash
# Mystery creation and management
+mystery/create The Missing Heir = A wealthy merchant has vanished
+mystery/template occult = Ritual Murders
+clueobj/create bloody knife = 1/clue_0

# NPC creation and control
+npc/create Guard standard
+npc/generate "Vampire Elder" vampire_social boss
+npc/puppet Guard

# Information and tracking
+mystery/progress 1
+npc/list
+stwho
```

### For Players
```bash
# See who's available to run stories
+stwho

# Check if someone is a storyteller
+storyteller/check Alice

# Learn about the system
+storyteller/info
```

## Permission Flow

```
Command Execution
       ↓
Check Staff Permissions
       ↓
   Staff? → YES → Allow Access
       ↓
      NO
       ↓
Check Storyteller Flag
       ↓
Storyteller? → YES → Allow Access
       ↓
      NO
       ↓
   Deny Access
```

## Technical Details

### Flag Storage
- **Character Level**: `character.db.storyteller = True`
- **Account Level**: `account.db.storyteller = True`
- **Persistence**: Flags persist across character switches and sessions

### Permission Checking
```python
def check_storyteller_permission(caller):
    # Check character flag
    if hasattr(caller, 'db') and caller.db.storyteller:
        return True
    
    # Check account flag  
    if hasattr(caller, 'account') and caller.account.db.storyteller:
        return True
    
    return False
```

### Integration Points
- **Mystery System**: All mystery commands check `check_mystery_permission()`
- **NPC System**: NPC creation/management checks storyteller permissions
- **Building System**: Future integration for limited building access
- **Experience System**: Future integration for story rewards

## Benefits

### For Staff
- **Reduced Workload**: Trusted players can run stories independently
- **Community Building**: Empowers active players to contribute content
- **Oversight Maintained**: Staff retain ultimate control and monitoring
- **Scalable Growth**: System scales with community size

### For Players
- **More Stories**: More people able to create engaging content
- **Player Agency**: Trusted community members can drive narratives
- **Accessible Tools**: Complex storytelling tools made available
- **Recognition**: Storyteller status recognizes trusted contributors

### For the Game
- **Rich Content**: More mysteries, NPCs, and stories available
- **Active Community**: Players invested in creating content for others
- **Flexible Moderation**: Graduated permissions between player and staff
- **Sustainable Growth**: Community-driven content creation

## Security Features

### Access Control
- **Admin Only**: Only Admins can grant/revoke Storyteller flags
- **Limited Scope**: Storytellers can't access full staff commands
- **Audit Trail**: All storyteller actions are logged
- **Revocable**: Permissions can be removed instantly if needed

### Safeguards
- **No Database Access**: Storytellers can't directly modify database
- **No Player Stats**: Can't modify other players' character sheets
- **No Permissions**: Can't grant permissions to other players
- **Area Restrictions**: Building access limited to designated areas

## Future Enhancements

### Planned Features
- **Story Templates**: Pre-built story frameworks
- **Player Ratings**: Feedback system for storyteller-run content
- **Advanced Tracking**: Better story progress monitoring
- **Integration Expansion**: More systems supporting storyteller access

### Possible Expansions
- **Graduated Levels**: Junior/Senior storyteller tiers
- **Specializations**: Mystery-focused vs NPC-focused storytellers  
- **Temporary Permissions**: Time-limited storyteller access
- **Area-Specific**: Storyteller permissions for specific game areas

## Command Summary

### Admin Commands
- `+storyteller/add <character>` - Grant flag
- `+storyteller/remove <character>` - Remove flag  
- `+storyteller/list` - List storytellers
- `+storyteller/check [character]` - Check status

### Storyteller Commands
- `+mystery/*` - All mystery management commands
- `+clueobj/*` - Clue object placement commands
- `+npc/*` - NPC creation and management commands
- `+stwho` - See online story staff

### Player Commands  
- `+stwho` - See online storytellers and staff
- `+storyteller/check` - Check your own status
- `+storyteller/info` - Learn about the system

This system successfully bridges the gap between regular players and staff, enabling trusted community members to create rich storytelling experiences while maintaining proper oversight and security.
