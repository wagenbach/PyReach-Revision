# Hangout System - Quick Reference

## Player Commands

### View Available Hangouts
```
+hangouts              List all available hangout locations
+hangouts/public       List only public hangout locations
+hangouts/groups       List only group hangout locations
```

### Travel to Hangouts
```
+hangouts <name>       Move to a specific hangout location
+hangouts/return       Return to your previous location
```

**Examples:**
```
+hangouts              # See all available locations
+hangouts crimson      # Go to "The Crimson Rose" (partial match)
+hangouts Ordo Dracul  # Go to your group's hangout
+hangouts/return       # Return to where you were before
```

## Staff/Leader Commands

### Manage Group Hangouts
```
+hangout/set <group>=<room>     Set a group's hangout location
+hangout/remove <group>         Remove a group's hangout location
+hangout/view <group>           View a group's hangout location
```

**Examples:**
```
+hangout/set Ordo Dracul=The Dragon's Lair
+hangout/set 1=#123
+hangout/remove Ordo Dracul
+hangout/view Ordo Dracul
```

## Builder Quick Setup

### Create a Public Hangout
```bash
# Tag any room with social/gathering tags
+room/tag The Crimson Rose=bar,gathering_hall,modern
+room/tag Moonlight Cafe=cafe,restaurant,gathering_hall
+room/tag Central Park=park,gathering_hall,outdoor
```

### Supported Tags
Common hangout tags: `bar`, `nightclub`, `restaurant`, `cafe`, `park`, `theater`, `church`, `gathering_hall`, `marketplace`, `plaza`, `ballroom`, `forum`, `gym`, `coffee_shop`

## Common Use Cases

**Finding RP:**
1. Type `+hangouts` to see where people might gather
2. Use `+hangouts <name>` to go there
3. When done, use `+hangouts/return` to go back

**Group Meeting:**
1. Staff/leader sets group hangout: `+hangout/set <group>=<room>`
2. Members see it in `+hangouts`
3. Members travel: `+hangouts <group name>`

**Event Setup:**
1. Create or designate event room
2. Tag it: `+room/tag <room>=gathering_hall,ballroom,event`
3. Players will see it in `+hangouts` automatically

## Related Commands

- `+ooc` - Move to OOC area
- `+ic` - Return to IC area  
- `+join <player>` - Staff: teleport to a player
- `+groups` - View group information
- `+room/tag` - Set room tags (builders)

For full documentation, see: `HANGOUT_SYSTEM.md`

