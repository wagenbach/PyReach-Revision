# Hangout Commands Module

## Overview

The `hangouts.py` module provides commands for finding and traveling to designated roleplay locations. It integrates with the existing room tagging system and group system to provide both public and group-specific hangout locations.

## Commands Provided

### CmdHangouts
Main player-facing command for listing and traveling to hangout locations.

**Key:** `+hangouts`  
**Aliases:** `hangout`, `hangouts`  
**Locks:** `cmd:all()`

**Switches:**
- `/public` - List only public hangout locations
- `/groups` - List only group hangout locations  
- `/return` - Return to previous location

**Usage:**
- `+hangouts` - List all available hangouts
- `+hangouts <name>` - Travel to a hangout
- `+hangouts/return` - Return to previous location

### CmdHangoutAdmin
Staff/leader command for managing group hangout locations.

**Key:** `+hangout`  
**Locks:** `cmd:all()` (but checks permissions internally)

**Switches:**
- `/set` - Set a group's hangout location
- `/remove` - Remove a group's hangout location
- `/view` - View a group's hangout location

**Usage:**
- `+hangout/set <group>=<room>` - Set hangout
- `+hangout/remove <group>` - Remove hangout
- `+hangout/view <group>` - View hangout

## Integration Points

### Room Tag System
- Uses existing room tags to identify public hangouts
- Looks for tags: `bar`, `nightclub`, `restaurant`, `cafe`, `park`, `theater`, `church`, `gathering_hall`, `marketplace`, etc.
- No special configuration needed - automatically discovers tagged rooms

### Group System
- Integrates with `typeclasses.groups.Group` TypeClass
- Stores hangout location as `group.db.hangout_location`
- Uses existing `group.is_member()` method for access control
- Respects group leader permissions

### OOC/IC Movement System  
- Similar pattern to `CmdOOC` and `CmdIC`
- Stores previous location in `caller.db.pre_hangout_location`
- Uses same logging and synchronization patterns
- Separate from OOC/IC tracking (won't interfere)

### Search and Permissions
- Uses `utils.search_helpers` for character searching
- Uses `world.utils.permission_utils` for staff permission checks (in related commands)
- Respects room locks via `move_to()` method

## Database Attributes

### On Group Objects
- `db.hangout_location` - Reference to the room object set as hangout

### On Character Objects  
- `db.pre_hangout_location` - Reference to location before traveling to hangout

## Logging

All movements and admin actions are logged:
- Hangout travel: "Hangout Movement: {char} moved from {old} to {new}"
- Hangout return: "Hangout Return: {char} returned from {old} to {new}"
- Set hangout: "{staff} set group {group} hangout to {room}"
- Remove hangout: "{staff} removed group {group} hangout"

## Dependencies

### Python Imports
```python
from evennia import default_cmds
from evennia.utils.evtable import EvTable
import evennia
from typeclasses.groups import Group
from utils.search_helpers import search_character
```

### System Dependencies
- Room tag system (built-in Evennia tags)
- Group TypeClass system (`typeclasses.groups`)
- Search helpers (`utils.search_helpers`)

## Implementation Notes

### Public Hangout Discovery
The system searches for rooms with specific tags using `evennia.search_tag()`. It checks both categorized and uncategorized tags for maximum compatibility.

### Group Hangout Storage
Group hangouts are stored directly on the Group object rather than using a separate database table. This keeps the implementation simple and leverages existing TypeClass persistence.

### Location Tracking
Previous locations are stored using the same pattern as the OOC/IC system:
- Store reference on character when traveling
- Verify validity before returning
- Clean up after successful return
- Force save before and after moves

### Permission Checks
- Public hangouts: All players can access
- Group hangouts: Only group members can see and access
- Set/Remove: Only staff or group leader
- View: Anyone with access to the group (members + staff)

## Testing Considerations

### Manual Testing
```python
# Test public hangout listing
+hangouts/public

# Test group hangout listing  
+hangouts/groups

# Test traveling
+hangouts <some hangout>

# Test return
+hangouts/return

# Test setting (as staff)
+hangout/set <group>=<room>

# Test viewing
+hangout/view <group>

# Test removal (as staff)
+hangout/remove <group>
```

### Edge Cases to Test
- Hangout with no previous location (should fail gracefully)
- Invalid room name (should show error)
- Multiple matches (should list options)
- Non-member accessing group hangout (shouldn't see it)
- Non-leader trying to set hangout (should fail)
- Deleted room reference (should handle gracefully)

## Future Enhancements

Potential improvements:
- Cache public hangout list for performance
- Add popularity tracking (count players at each hangout)
- Add "who's there" display in hangout list
- Add favorite hangouts per character
- Add temporary hangout boosting for events
- Add hangout categories/filtering

## Related Files

- `PyReach/docs/HANGOUT_SYSTEM.md` - Full system documentation
- `PyReach/docs/HANGOUT_QUICK_REFERENCE.md` - Quick command reference
- `PyReach/docs/ROOM_TAG_SYSTEM.md` - Room tagging documentation
- `PyReach/docs/groups_and_rosters.md` - Group system documentation
- `PyReach/commands/ooc_ic_commands.py` - Similar movement command pattern
- `PyReach/typeclasses/groups.py` - Group TypeClass implementation

