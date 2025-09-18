# Groups and Rosters System

## Overview
Group management with automatic assignment based on character characteristics, dedicated channels, and roster viewing.

## Features

### **Automatic Group Assignment**
- Characters are automatically assigned to groups when approved based on their template and characteristics
- Vampire with "Ordo Dracul" covenant → assigned to "Vampire", clan group, and "Ordo Dracul" groups
- Works for all templates: Vampire, Mage, Werewolf, Changeling, Hunter, etc.

### **Character Attributes**
- Each character has a `groups` attribute tracking their memberships
- Automatically maintained when joining/leaving groups
- Accessible via `character.attributes.get('groups', [])`

### **Dedicated Channels**
- Each group automatically gets its own channel
- Proper access controls using `group_member()` lock function
- Members auto-subscribed when joining groups

### **Roster Viewing**
- View online/offline members of groups you have access to
- Shows member status, titles, roles, and last seen dates
- Access control respects group privacy settings

## Commands

### Group Management (`+group`)

```
+groups                    - List all public groups
+group <id>                - View detailed information about a group
+group/create <name>       - Create a new group (staff only)
+group/destroy <id>        - Destroy a group (staff only)
+group/type <id>=<type>    - Set group type (staff only)
+group/leader <id>=<char>  - Set the leader of a group (staff only)
+group/desc <id>=<text>    - Set a group's description (staff or leader)
+group/note <id>=<text>    - Set a group's private notes (staff or leader)
+group/title <id>/<char>=<title> - Set a character's title in the group
+group/add <id>=<char>     - Add a character to a group (staff or leader)
+group/remove <id>=<char>  - Remove a character from a group (staff or leader)
+group/private <id>        - Set a group as private (staff or leader)
+group/public <id>         - Set a group as public (staff or leader)
+group/auto <char>         - Manually trigger automatic group assignment
+group/show <char>         - Show all groups a character belongs to
+group/sync                - Sync all characters' group attributes
+group/sync <char>         - Sync a specific character's group attributes
+group/syncchannels        - Ensure all group channels exist and have proper locks
+group/synccleanup         - Remove orphaned group attributes
+group/test <character>    - Test auto-assignment of groups for a character
```

### Roster Viewing (`+roster`)

```
+roster                    - List all groups you can view rosters for
+roster <group name>       - View the roster for a specific group
+roster <group id>         - View the roster for a group by ID
+roster/all                - List all public group rosters (staff only)
```

### Maintenance Commands (Admin Only)

```
+testgroups <character>    - Test automatic group assignment system
+group/sync                - Sync all characters' group attributes
+group/sync <character>    - Sync a specific character's group attributes
+group/syncchannels        - Ensure all group channels exist and have proper locks
+group/synccleanup         - Remove orphaned group attributes
```

## Group Types

- **coterie** - Vampire groups (clans, covenants)
- **pack** - Werewolf groups (tribes, auspices)
- **cabal** - Mage groups (orders, paths)
- **motley** - Changeling groups (courts, seemings)
- **conspiracy** - Hunter groups (organizations)
- **agency** - Mortal organizations
- **cult** - Religious/occult groups
- **other** - Generic groups

## Access Control

### Group Visibility
- **Public Groups**: Anyone can view basic info and roster
- **Private Groups**: Only members and staff can view details and roster

### Channel Access
- Channels use `group_member(group_id)` lock function
- Only group members can listen/send to group channels
- Staff always have access

### Command Permissions
- **Players**: Can view public groups and rosters, see their own memberships
- **Group Leaders**: Can manage their group (add/remove members, set titles, etc.)
- **Staff**: Full access to all group management functions

## Installation

### 1. Add Command Set
Add the groups command set to your default character command set:

```python
# In typeclasses/characters.py
from commands.cmdsets.groups import GroupsCmdSet

class Character(DefaultCharacter):
    def at_object_creation(self):
        # ... existing code ...
        self.cmdset.add(GroupsCmdSet, permanent=True)
```

### 2. Database Setup
The system uses existing Group, GroupMembership, and GroupRole models from `world.cofd.models`.

### 3. Lock Function
The `group_member()` lock function is automatically available from `server.conf.lockfuncs`.

## Examples

### Automatic Assignment on Approval
```
approve TestVampire
# Output: "Auto-assigned TestVampire to groups: Vampire, Gangrel, Ordo Dracul"
```

### Viewing Rosters
```
+roster
# Shows list of available groups

+roster Vampire
# Shows vampire group roster with online/offline status

+roster "Ordo Dracul"
# Shows Ordo Dracul covenant roster
```

### Manual Group Management
```
+group/create "My Custom Group"
+group/add 5=TestCharacter
+group/title 5/TestCharacter=Initiate
+group/leader 5=TestCharacter
```

### Character Group Viewing
```
+group/show TestVampire
# Shows all groups TestVampire belongs to with titles and roles
```

### Test automatic assignment
+group/test TestVampire

### Sync data consistency
+group/sync
+group/syncchannels

## Technical Details

### Character Attributes
Characters automatically get a `groups` attribute containing a list of group names:
```python
character.attributes.get('groups', [])
# Returns: ['Vampire', 'Gangrel', 'Ordo Dracul']
```

### Channel Naming
Group channels are created using the group name with non-alphanumeric characters removed:
- "Ordo Dracul" → "OrdoDracul" channel
- "Circle of the Crone" → "CircleoftheCrone" channel

### Lock String Format
Group channels use this lock format:
```
control:perm(Admin);listen:group_member(5) or perm(Admin);send:group_member(5) or perm(Admin)
```

### Automatic Group Types
The system automatically determines appropriate group types:
- Vampire clans/covenants → "coterie"
- Werewolf tribes/auspices → "pack"  
- Mage orders/paths → "cabal"
- Changeling courts/seemings → "motley"
- Hunter organizations → "conspiracy"

## Troubleshooting

### Common Issues

1. **Commands not available**: Make sure GroupsCmdSet is added to character command set
2. **Channel access denied**: Run `+group/syncchannels` to fix locks
3. **Missing group attributes**: Run `+group/sync` to sync character attributes
4. **Orphaned data**: Run `+group/synccleanup` to clean up inconsistencies

### Maintenance

- Run `+group/sync` periodically to ensure data consistency
- Use `+testgroups <character>` to verify automatic assignment works
- Check `+group/syncchannels` if channel access issues occur

## Future Enhancements

Potential additions to consider:
- Group hierarchy (sub-groups, parent groups)
- Group-specific message boards or forums
- Group experience point pools
- Group-based merit/resource sharing
- Integration with territory/influence systems 