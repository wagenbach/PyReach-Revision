# Hangout System Documentation

## Overview

The hangout system provides players with easy access to designated roleplay locations, including both public social spaces (bars, cafes, parks, etc.) and group-specific locations. This system encourages roleplay by making it easy to find and travel to locations where other players may be gathering.

## Features

### Public Hangouts
- Automatically discovers rooms tagged with social/gathering tags
- Includes bars, restaurants, cafes, parks, theaters, and more
- Available to all players

### Group Hangouts  
- Special locations set by staff or group leaders
- Accessible only to group members
- Perfect for faction headquarters, club houses, secret meeting places
- Automatically displayed to members when they use `+hangouts`

### Location Memory
- Stores your previous location when traveling to a hangout
- Easy return with `+hangouts/return`
- Prevents location desynchronization issues

## Player Commands

### List Available Hangouts

```
+hangouts              - List all available hangout locations
+hangouts/public       - List only public hangout locations  
+hangouts/groups       - List only group hangout locations
```

**Example Output:**
```
==============================================================================
                        Available Hangout Locations
==============================================================================

Public Hangout Locations:
------------------------------------------------------------------------------
╔════════════════════════╦═══════════════╦═══════════════════════════════╗
║ Name                   ║ Type          ║ Location                      ║
╠════════════════════════╬═══════════════╬═══════════════════════════════╣
║ The Crimson Rose       ║ Bar           ║ Downtown                      ║
║ Moonlight Cafe         ║ Cafe          ║ Arts District                 ║
║ Central Park           ║ Park          ║ Midtown                       ║
║ The Dragon's Den       ║ Nightclub     ║ Waterfront                    ║
╚════════════════════════╩═══════════════╩═══════════════════════════════╝

Group Hangout Locations:
------------------------------------------------------------------------------
╔════════════════════════╦═══════════════════════╦══════════════════════╗
║ Group                  ║ Location              ║ Area                 ║
╠════════════════════════╬═══════════════════════╬══════════════════════╣
║ Ordo Dracul            ║ The Dragon's Lair     ║ Old Quarter          ║
║ The Twilight Circle    ║ Circle Sanctum        ║ University District  ║
╚════════════════════════╩═══════════════════════╩══════════════════════╝

Usage: +hangouts <name> to travel to a location
       +hangouts/return to return to your previous location
==============================================================================
```

### Travel to a Hangout

```
+hangouts <name>       - Move to a specific hangout location
```

You can use:
- The exact room name: `+hangouts The Crimson Rose`
- A partial match: `+hangouts crimson`
- A group name (for group hangouts): `+hangouts Ordo Dracul`

**Example:**
```
> +hangouts crimson
You travel to The Crimson Rose.
Use +hangouts/return to return to your previous location.
```

### Return to Previous Location

```
+hangouts/return       - Return to your previous location
```

**Example:**
```
> +hangouts/return
You have returned to your previous location: The Old Manor.
```

## Staff/Leader Commands

### Set Group Hangout

```
+hangout/set <group>=<room>
```

Sets a group's designated hangout location. Only staff members and group leaders can use this command.

**Examples:**
```
+hangout/set Ordo Dracul=The Dragon's Lair
+hangout/set 1=#123
+hangout/set The Twilight Circle=Circle Sanctum
```

### Remove Group Hangout

```
+hangout/remove <group>
```

Removes a group's hangout location.

**Example:**
```
+hangout/remove Ordo Dracul
Removed Ordo Dracul's hangout location.
```

### View Group Hangout

```
+hangout/view <group>
```

View a group's current hangout location.

**Example:**
```
> +hangout/view Ordo Dracul
Group: Ordo Dracul
Hangout Location: The Dragon's Lair (#456)
Area: Old Quarter - Vampire District
```

## Setting Up Hangout Locations

### For Builders: Creating Public Hangouts

Public hangouts are automatically discovered by the system based on room tags. To create a public hangout:

1. Create or designate a room
2. Tag it with appropriate social/gathering tags

```bash
# Example: Create a bar
+room/tag The Crimson Rose=bar,gathering_hall,modern

# Example: Create a cafe
+room/tag Moonlight Cafe=cafe,restaurant,gathering_hall

# Example: Create a park
+room/tag Central Park=park,gathering_hall,outdoor
```

### Supported Hangout Tags

The following tags will automatically mark a room as a public hangout:

**Social Venues:**
- `bar` - Drinking establishment
- `nightclub` - Modern entertainment venue
- `restaurant` - Dining establishment
- `cafe` - Coffee shop, informal gathering
- `coffee_shop` - Modern cafe

**Religious/Spiritual:**
- `church` - Christian religious site
- `synagogue` - Jewish religious site  
- `mosque` - Islamic religious site
- `temple` - Religious site (general)

**Community Spaces:**
- `gathering_hall` - Community meeting place
- `marketplace` - Trading and commerce
- `park` - Outdoor park
- `plaza` - Open public square

**Entertainment:**
- `theater` - Performance venue
- `ballroom` - Dance hall
- `stadium` - Sports/events venue

**Historical/Period:**
- `parlor` - Formal sitting room (Victorian)
- `court` - Royal or legal court
- `throne_room` - Seat of power
- `forum` - Ancient public gathering
- `agora` - Greek-style marketplace
- `gentlemens_club` - Exclusive male club (Victorian)
- `ladies_parlor` - Female social space (Victorian)

**Recreation:**
- `gym` - Fitness center
- `playground` - Play area

### For Staff/Leaders: Setting Group Hangouts

Group hangouts are manually set and can be any room in the game. They don't need special tags.

**Best Practices:**
1. Choose a room appropriate to the group's theme and purpose
2. Consider location (should it be hidden, public, central, remote?)
3. Ensure the room has a good description
4. Set appropriate locks if the room should be restricted
5. Tag the room with relevant thematic tags for flavor

**Example Setup:**
```bash
# Create a vampire covenant meeting hall
@dig The Dragon's Lair
@desc The Dragon's Lair=A shadowy chamber deep beneath the old quarter...

# Tag it for theme
+room/tag The Dragon's Lair=gathering_hall,desecrated,hidden,vampire

# Set as group hangout
+hangout/set Ordo Dracul=The Dragon's Lair
```

## Integration with Other Systems

### OOC/IC Commands
- The hangout system works alongside `+ooc` and `+ic` commands
- Location tracking is separate - using `+hangouts` won't affect your `+ic` return location
- Both systems use similar location-saving technology

### Group System
- Automatically checks group membership
- Uses the existing Group TypeClass system
- Group leaders can manage their own hangout locations
- Staff can manage all group hangouts

### Room Tag System
- Leverages the existing room tagging system
- No special configuration needed beyond standard room tags
- Works with all existing social/gathering tags
- Can be combined with other tag categories (time period, supernatural, etc.)

### Mystery/Investigation System
- Hangout locations may also serve as investigation locations
- A room can be both a hangout and a research location
- Tags are cumulative and multi-purpose

## Use Cases

### Player Perspective

**Finding Roleplay:**
```
> +hangouts
[See list of available locations]
> +hangouts crimson rose
You travel to The Crimson Rose.
[Roleplay with other players]
> +hangouts/return
You have returned to your previous location.
```

**Group Meeting:**
```
> +hangouts
[See that your group has a designated location]
> +hangouts Ordo Dracul
You travel to The Dragon's Lair.
[Participate in group meeting]
```

### Staff Perspective

**Setting Up Faction Locations:**
```
# Create locations for each major faction
+hangout/set Ordo Dracul=The Dragon's Lair
+hangout/set Circle of the Crone=The Sacred Grove
+hangout/set Lancea et Sanctum=St. Michael's Cathedral
+hangout/set Carthian Movement=The Underground

# Players can now easily find and access their faction's space
```

**Event Management:**
```
# For a special event at a location
+room/tag The Grand Ballroom=ballroom,gathering_hall,event
# Players will see it in their +hangouts list
# After the event, remove the tag if desired
```

## Logging and Tracking

All hangout movements are logged for troubleshooting and staff awareness:

```
Hangout Movement: Alice (#123) moved from The Old Manor (#456) to The Crimson Rose (#789)
Hangout Return: Alice (#123) returned from The Crimson Rose (#789) to The Old Manor (#456)
```

Staff actions are also logged:
```
Alice set group Ordo Dracul (#1) hangout to The Dragon's Lair (#456)
Bob removed group Circle of the Crone (#2) hangout (was: Sacred Grove #789)
```

## Security and Permissions

### Player Commands
- All players can use `+hangouts`, `+hangouts <name>`, and `+hangouts/return`
- Players can only see group hangouts for groups they belong to
- Public hangouts are visible to everyone

### Staff/Leader Commands
- `+hangout/set` requires staff permissions OR group leader status
- `+hangout/remove` requires staff permissions OR group leader status
- `+hangout/view` can be used by anyone with access to the group
- Staff can manage all groups' hangouts

### Room Access
- The hangout system respects room locks
- Moving to a hangout uses the standard `move_to()` method
- If a player can't access a room, the movement will fail gracefully
- Group hangouts don't automatically lock rooms (set locks separately)

## Troubleshooting

### "No hangout location found matching..."
- Check that the room name is spelled correctly
- Use `+hangouts` to see the exact names
- Try a partial match (e.g., "crimson" instead of "The Crimson Rose")

### "You don't have a previous location to return to"
- You must use `+hangouts <name>` before using `+hangouts/return`
- The system only stores location when traveling via hangout commands
- Using other movement methods (walking, teleporting) won't set this

### "Multiple hangouts match..."
- Be more specific with the name
- Use the full room name from the `+hangouts` list
- Use a dbref if necessary: `+hangouts #123`

### Group hangout not appearing
- Verify you're a member of the group: `+groups`
- Check that the hangout is actually set: `+hangout/view <group>`
- Contact the group leader or staff if issues persist

### Public hangout not appearing  
- Verify the room has appropriate tags: `+room/tags <room>`
- Check that the tag is in the supported list (see above)
- Contact a builder or staff member to add tags if needed

## Examples

### Complete Player Workflow

```
> +who
[See several players online]

> +hangouts
[See The Crimson Rose is a bar in Downtown]

> +hangouts crimson
You travel to The Crimson Rose.

> look
[See other players are here]

> "Hey everyone!"
You say, "Hey everyone!"

[Roleplay for a while...]

> +hangouts/return
You have returned to your previous location: The Old Manor.
```

### Complete Staff Workflow

```
# Create a new group hangout
> +hangout/set Ordo Dracul=The Dragon's Lair
Set Ordo Dracul's hangout location to: The Dragon's Lair (#456)

# Verify it's set correctly
> +hangout/view Ordo Dracul
Group: Ordo Dracul
Hangout Location: The Dragon's Lair (#456)
Area: Old Quarter - Vampire District

# Later, if needed, remove it
> +hangout/remove Ordo Dracul
Removed Ordo Dracul's hangout location.
```

## Technical Notes

### Database Storage
- Group hangouts are stored as `db.hangout_location` on Group objects
- Previous locations are stored as `db.pre_hangout_location` on Character objects
- Public hangouts are discovered dynamically via room tags

### Performance
- Room tag searches are efficient using Evennia's built-in tag system
- Results are generated on-demand (no caching required)
- Group membership checks use existing Group TypeClass methods

### Compatibility
- Works with Evennia 1.0+
- Integrates with existing PyReach systems
- No database migrations required
- No configuration changes needed

## Future Enhancements

Potential future additions:
- Hangout popularity tracking (who's where)
- Recently visited hangouts list
- Favorite hangouts shortlist
- Scheduled events at hangouts
- Temporary hangout boosting for events
- Cross-realm hangout support

