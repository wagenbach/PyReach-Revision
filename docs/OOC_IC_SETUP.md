# OOC/IC Movement Commands Setup

## Overview

This document explains how to set up and configure the OOC/IC movement commands (`+ooc`, `+ic`, `+join`, `+summon`, `+return`) that were enhanced to prevent the location desynchronization bugs experienced on Dies Irae.

## Commands Created

### Player Commands
- **+ooc**: Teleports player to designated OOC room, stores current location
- **+ic**: Returns player to previous location or IC starting room

### Staff Commands  
- **+join <player>**: Staff teleports to player's location
- **+summon <player>**: Staff brings player to their location, stores player's previous location
- **+return <player>**: Staff returns player to their stored previous location

## Configuration Required

### Option 1: In-Game Configuration (Recommended)
Developer-level staff can set these values from within the game using the `+config` command:

```
+config/list                    # Show current settings
+config/ooc #2                  # Set OOC room to dbref #2
+config/ooc OOC Lounge         # Set OOC room by name
+config/ic #1                  # Set IC starting room to dbref #1
+config/ic Town Square         # Set IC starting room by name
+config/ooc/clear              # Clear OOC room setting
+config/ic/clear               # Clear IC starting room setting
```

### Option 2: Manual Configuration File Edit
Alternatively, staff can manually edit the server settings file:

```python
# In your server/conf/settings.py file, add:
OOC_ROOM_DBREF = 2      # The dbref of your OOC lounge/room
IC_STARTING_ROOM_DBREF = 1   # The dbref of your IC starting/arrival room
```

**Note:** The in-game configuration method is preferred as it doesn't require server restarts and provides immediate feedback.

## How to Find Room Dbrefs

1. Go to the room you want to designate
2. Type `examine here` or `examine #<room_name>`
3. Look for the dbref number (e.g., `Room(#123)`)
4. Use that number in the settings

## Anti-Desynchronization Features

These commands include several features to prevent the location bugs from Dies Irae:

### 1. Direct Object Storage
- Locations are stored as direct object references, not serialized dictionaries
- This prevents the dict serialization issues that caused desync

### 2. Forced Synchronization
- `caller.save()` is called before and after each move operation
- This ensures the database is updated immediately

### 3. Server Logging
- All movements are logged to the server log with full details
- Format: `{Action}: {Caller} (#{ID}) moved from {From} (#{ID}) to {To} (#{ID})`

### 4. Location Validation
- Stored locations are validated before use
- Invalid/deleted locations are cleaned up automatically

### 5. Proper Attribute Cleanup
- Location storage attributes are removed after use
- This prevents stale data from causing issues

## Usage Examples

### Player Usage
```
+ooc                    # Go to OOC room
+ic                     # Return to previous location or IC start
```

### Staff Usage
```
+join PlayerName        # Go to player's location
+join/quiet PlayerName  # Go to player's location quietly

+summon PlayerName      # Bring player to your location  
+summon/quiet PlayerName # Bring player quietly

+return PlayerName      # Send player back to stored location
+return/quiet PlayerName # Send player back quietly
```

## Permissions

- **+ooc, +ic**: Available to all players
- **+join**: Staff only (requires `perm(staff)`)
- **+summon, +return**: Staff only (requires `perm(storyteller)`)

## Troubleshooting

### "No OOC room has been designated"
- Use `+config/ooc <room>` to set the OOC room (recommended)
- Or add `OOC_ROOM_DBREF = <number>` to settings.py and restart server

### "No IC starting room has been designated"  
- Use `+config/ic <room>` to set the IC starting room (recommended)
- Or add `IC_STARTING_ROOM_DBREF = <number>` to settings.py and restart server

### "Room not found"
- Verify the dbref exists: `examine #<number>`
- Check that the room hasn't been deleted
- Use `+config/list` to see current settings
- Update the setting with `+config/ooc <room>` or `+config/ic <room>`

### Player has no stored location to return to
- This is normal if they haven't been summoned
- Use `+summon` first, then `+return` will work

## Technical Notes

### Location Storage Attributes
- `pre_ooc_location`: Stores location before using +ooc
- `pre_summon_location`: Stores location before being summoned
- `pre_join_location`: Stores staff location before using +join

### Database Safety
- All moves use `move_type="teleport"` for reliability
- Forced saves prevent memory/database desync
- Object references avoid serialization issues

### Logging Format
All movements are logged with this format:
```
{Command} Movement: {Actor} (#{ActorID}) {action} {Target} (#{TargetID}) {from/to} {Location} (#{LocationID})
```

Examples:
```
OOC Movement: Alice (#45) moved from Town Square (#12) to OOC room
Staff Summon: Bob (#23) summoned Alice (#45) from Town Square (#12) to Staff Office (#67)
Staff Return: Bob (#23) returned Alice (#45) from Staff Office (#67) to Town Square (#12)
```
