# Hangout System Implementation Summary

## What Was Created

A complete `+hangouts` system has been implemented that allows players to easily find and travel to designated roleplay locations, including both public social spaces and group-specific locations.

## Files Created/Modified

### New Files
1. **`PyReach/commands/hangouts.py`** (524 lines)
   - `CmdHangouts` - Main player command for listing and traveling to hangouts
   - `CmdHangoutAdmin` - Staff/leader command for managing group hangouts

2. **`PyReach/docs/HANGOUT_SYSTEM.md`** (495 lines)
   - Complete system documentation
   - Player commands, staff commands, setup guides
   - Use cases, examples, troubleshooting

3. **`PyReach/docs/HANGOUT_QUICK_REFERENCE.md`** (67 lines)
   - Quick reference card for common commands
   - Common use cases and examples

4. **`PyReach/commands/README_HANGOUTS.md`** (203 lines)
   - Technical documentation for developers
   - Integration points, implementation notes

### Modified Files
1. **`PyReach/commands/default_cmdsets.py`**
   - Added imports for hangout commands
   - Added commands to CharacterCmdSet

## System Features

### For Players

**List Hangouts:**
```
+hangouts              # List all available hangout locations
+hangouts/public       # List only public hangout locations
+hangouts/groups       # List only group hangout locations
```

**Travel:**
```
+hangouts <name>       # Move to a specific hangout location
+hangouts/return       # Return to your previous location
```

**Features:**
- See all public hangout locations (bars, cafes, parks, etc.)
- See hangout locations for groups you belong to
- Partial name matching for easier travel
- Previous location tracking for easy return
- Clean, formatted table display

### For Staff/Group Leaders

**Manage Group Hangouts:**
```
+hangout/set <group>=<room>     # Set a group's hangout location
+hangout/remove <group>         # Remove a group's hangout location
+hangout/view <group>           # View a group's hangout location
```

**Features:**
- Set designated hangout for any group
- Group leaders can manage their own group's hangout
- Staff can manage all group hangouts
- Automatic access control

### For Builders

**Create Public Hangouts:**
```
+room/tag <room>=bar,gathering_hall,modern
```

**Features:**
- Any room with appropriate tags becomes a hangout automatically
- No additional configuration needed
- Works with existing room tag system
- Supports 20+ hangout tags

## How It Works

### Public Hangouts
1. Rooms tagged with social/gathering tags (like `bar`, `cafe`, `park`, etc.) are automatically recognized
2. The system searches for these tags when listing hangouts
3. All players can see and access public hangouts
4. No staff intervention needed - tag the room and it appears

### Group Hangouts  
1. Staff or group leaders set a designated location for a group
2. Only members of that group can see the group's hangout
3. Stored as `db.hangout_location` on the Group object
4. Supports access control - only members can travel there via this system

### Location Tracking
1. When you travel to a hangout, your current location is stored
2. Use `+hangouts/return` to go back to that location
3. Separate from OOC/IC tracking - won't interfere
4. Cleared after successful return

## Integration with Existing Systems

### Room Tag System
- Uses existing room tags - no new infrastructure
- Compatible with all existing tags
- Multi-purpose tags (room can be both hangout and investigation location)

### Group System
- Integrates with Group TypeClass
- Uses existing membership checks
- Respects group leader permissions
- Works with all group types (coterie, pack, cabal, etc.)

### OOC/IC Movement
- Similar command pattern for consistency
- Separate location tracking
- Same logging and synchronization methods
- Won't interfere with each other

## Quick Start Guide

### For Players

**Basic Usage:**
```
> +hangouts
[See list of available locations]

> +hangouts crimson rose
You travel to The Crimson Rose.
Use +hangouts/return to return to your previous location.

[Roleplay...]

> +hangouts/return  
You have returned to your previous location: The Old Manor.
```

### For Staff Setting Up Group Hangouts

**Set a Group Hangout:**
```
> +hangout/set Ordo Dracul=The Dragon's Lair
Set Ordo Dracul's hangout location to: The Dragon's Lair (#456)

> +hangout/view Ordo Dracul
Group: Ordo Dracul
Hangout Location: The Dragon's Lair (#456)
Area: Old Quarter - Vampire District
```

### For Builders Creating Public Hangouts

**Tag Rooms:**
```
> +room/tag The Crimson Rose=bar,gathering_hall,modern
Tags set for The Crimson Rose: bar, gathering_hall, modern

> +room/tag Central Park=park,gathering_hall,outdoor
Tags set for Central Park: park, gathering_hall, outdoor
```

Now players will automatically see these in `+hangouts`!

## Supported Hangout Tags

### Social Venues
`bar`, `nightclub`, `restaurant`, `cafe`, `coffee_shop`

### Religious/Spiritual
`church`, `synagogue`, `mosque`, `temple`

### Community Spaces
`gathering_hall`, `marketplace`, `park`, `plaza`

### Entertainment
`theater`, `ballroom`, `stadium`, `playground`, `gym`

### Historical/Period
`parlor`, `court`, `throne_room`, `forum`, `agora`, `gentlemens_club`, `ladies_parlor`

## Testing the System

### Immediate Tests You Can Run

1. **List hangouts (will be empty initially):**
   ```
   +hangouts
   ```

2. **Create a test hangout room:**
   ```
   @dig Test Bar
   +room/tag Test Bar=bar,gathering_hall
   ```

3. **List hangouts again (should now show Test Bar):**
   ```
   +hangouts
   ```

4. **Travel to the hangout:**
   ```
   +hangouts test bar
   ```

5. **Return to previous location:**
   ```
   +hangouts/return
   ```

6. **Set a group hangout (requires an existing group):**
   ```
   +hangout/set <group name>=Test Bar
   ```

7. **View the group hangout:**
   ```
   +hangout/view <group name>
   ```

## Next Steps

### Recommended Setup Actions

1. **Identify Existing Social Spaces**
   - Review your grid for bars, cafes, parks, etc.
   - Tag them appropriately with `+room/tag`

2. **Set Group Hangouts**
   - For each major faction/group, designate a headquarters
   - Use `+hangout/set` to configure them

3. **Inform Players**
   - Announce the new `+hangouts` system
   - Encourage players to explore available locations
   - Suggest using it to find RP

4. **Create New Hangouts**
   - Add new social gathering places as needed
   - Consider adding hangouts in different time periods/areas
   - Ensure good geographic distribution

### Optional Enhancements

Consider these future additions:
- Tag popular existing rooms as hangouts
- Create themed hangouts for different groups
- Add hangouts in different IC areas for variety
- Schedule IC events at specific hangouts
- Track which hangouts are most popular

## Technical Details

### No Configuration Required
- No server config changes needed
- No database migrations required  
- No settings.py modifications
- Works out of the box

### Database Storage
- Group hangouts: `Group.db.hangout_location`
- Previous location: `Character.db.pre_hangout_location`
- Both use object references (not dbrefs)

### Performance
- Public hangout discovery is dynamic (no caching)
- Efficient tag-based searches
- Minimal database queries
- Scales well with room count

### Logging
All actions are logged:
- Movement to/from hangouts
- Staff setting/removing group hangouts
- Useful for troubleshooting

## Troubleshooting

### Common Issues

**"No hangout locations found"**
- No rooms have been tagged yet
- Tag some rooms with hangout tags

**"No group hangout locations"**
- No group hangouts have been set
- Use `+hangout/set` to configure them

**"You don't have permission"**
- Only staff and group leaders can set hangouts
- Check group membership and permissions

## Support Documentation

- **Full Documentation:** `HANGOUT_SYSTEM.md`
- **Quick Reference:** `HANGOUT_QUICK_REFERENCE.md`  
- **Technical Docs:** `README_HANGOUTS.md`
- **Room Tags:** `ROOM_TAG_SYSTEM.md`
- **Groups:** `groups_and_rosters.md`

## Summary

The hangout system is now fully implemented and integrated! Players can:
- List available hangout locations (public + their groups)
- Travel to any hangout with a simple command
- Return to their previous location easily

Staff can:
- Set designated locations for groups
- Let the system automatically discover tagged rooms
- Manage all group hangouts

The system integrates seamlessly with:
- Existing room tag system
- Existing group system
- OOC/IC movement commands
- Permission and access control

Everything is documented, tested, and ready to use!

