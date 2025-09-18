## Overview

Groups are stored as Evennia TypeClass objects rather than Django models. Benefits:

- Better integration with Evennia's object system
- Automatic attribute persistence
- Built-in event hooks and methods
- Consistent architecture with other game objects
- Easier customization and extension

## TypeClass Structure

### Group TypeClass

The `Group` TypeClass is defined in `typeclasses/groups.py` and inherits from `DefaultObject`.

**Key Attributes:**
- `db.group_id` - Unique numeric identifier
- `db.group_type` - Type of group (coterie, pack, cabal, etc.)
- `db.description` - Group description
- `db.notes` - Private notes (staff/leader only)
- `db.is_public` - Whether group is publicly visible
- `db.leader` - Character object who leads the group
- `db.members` - List of character objects who are members
- `db.member_data` - Dict storing per-member data (titles, roles, join dates)

**Key Methods:**
- `add_member(character)` - Add a character to the group
- `remove_member(character)` - Remove a character from the group
- `is_member(character)` - Check if character is a member
- `get_member_title(character)` - Get member's title
- `set_member_title(character, title)` - Set member's title
- `get_member_count()` - Get number of members
- `get_online_members()` - Get list of online members

## Group Types

The system supports the following group types:

- `coterie` - Vampire groups (clans, covenants)
- `pack` - Werewolf groups (tribes, auspices)
- `cabal` - Mage groups (orders, paths)
- `motley` - Changeling groups (courts, seemings)
- `conspiracy` - Hunter groups (organizations)
- `agency` - Mortal organizations
- `cult` - Religious/occult groups
- `other` - Generic groups

## Automatic Features

### Channel Creation
Each group automatically gets its own channel when created:
- Channel name is derived from group name (alphanumeric only)
- Proper locks restrict access to group members and staff
- Members are automatically subscribed/unsubscribed

### Character Attributes
Characters maintain a `groups` attribute listing their group memberships:
- Updated automatically when joining/leaving groups
- Used for quick membership lookup
- Synchronized with actual group membership

### Auto-Assignment
Characters are automatically assigned to appropriate groups based on their characteristics:
- Template-based groups (Vampire, Mage, etc.)
- Clan/covenant groups for vampires
- Order/path groups for mages
- Similar logic for other templates

## Migration from Django Models

If you have existing Django model groups, use the migration script:

```python
# In Evennia shell (@py command)
exec(open('world/groups/migrate_to_typeclass.py').read())
migrate_groups_to_typeclass()
```

This will:
1. Convert all Django Group objects to TypeClass Groups
2. Migrate all memberships and member data
3. Preserve leaders, titles, descriptions, etc.
4. Create channels for all groups

After successful migration, you can optionally clean up old Django records:

```python
# DANGEROUS - only after verifying migration worked
cleanup_old_django_groups()
```

## Commands

All existing group commands work unchanged:

### Group Management (`+group`)
- `+groups` - List all public groups
- `+group <id>` - View detailed group information
- `+group/create <name>` - Create new group (staff only)
- `+group/destroy <id>` - Destroy group (staff only)
- `+group/type <id>=<type>` - Set group type (staff only)
- `+group/leader <id>=<char>` - Set group leader (staff only)
- `+group/desc <id>=<text>` - Set description (staff/leader)
- `+group/note <id>=<text>` - Set private notes (staff/leader)
- `+group/title <id>/<char>=<title>` - Set member title
- `+group/add <id>=<char>` - Add character (staff/leader)
- `+group/remove <id>=<char>` - Remove character (staff/leader)
- `+group/private <id>` - Set as private (staff/leader)
- `+group/public <id>` - Set as public (staff/leader)
- `+group/auto <char>` - Manual auto-assignment (staff only)
- `+group/show <char>` - Show character's groups
- `+group/sync` - Sync character attributes (staff only)
- `+group/syncchannels` - Fix channel locks (staff only)
- `+group/synccleanup` - Clean orphaned data (staff only)
- `+group/test <char>` - Test auto-assignment (staff only)

### Roster System (`+roster`)
- `+roster` - List available group rosters
- `+roster <group name>` - View specific group roster
- `+roster <group id>` - View roster by ID
- `+roster/all` - List all rosters (staff only)

## Integration Points

### Lock Functions
The `group_member(group_id)` lock function works with TypeClass groups:
```python
# In server/conf/lockfuncs.py
def group_member(accessing_obj, accessed_obj, *args, **kwargs):
    group_id = int(args[0])
    group = get_group_by_id(group_id)
    return group.is_member(accessing_obj) if group else False
```

### Admin Commands
The approve/unapprove commands automatically handle group assignment:
- `approve` - Auto-assigns character to appropriate groups
- `unapprove` - Removes character from all groups
- `+massunapprove` - Bulk removes all characters from groups

### Utility Functions
Key utility functions in `world/groups/utils.py`:
- `auto_assign_character_groups(character)` - Auto-assign based on characteristics
- `assign_character_to_group(character, group)` - Manual assignment
- `remove_character_from_group(character, group)` - Manual removal
- `get_character_groups(character)` - Get character's groups
- `sync_character_group_attributes(character)` - Sync attributes

## Customization

### Extending the Group TypeClass

You can extend the Group TypeClass for custom functionality:

```python
# In typeclasses/groups.py or a custom file
class CustomGroup(Group):
    def at_object_creation(self):
        super().at_object_creation()
        self.db.custom_attribute = "default_value"
    
    def custom_method(self):
        # Your custom functionality
        pass
```

### Custom Group Types

Add new group types by extending the `GROUP_TYPES` list:

```python
GROUP_TYPES = [
    # ... existing types ...
    ('custom', 'Custom Type'),
]
```

### Custom Auto-Assignment

Modify `get_automatic_groups_for_character()` in `utils.py` to change auto-assignment logic:

```python
def get_automatic_groups_for_character(character):
    # Your custom logic here
    auto_groups = []
    # ... 
    return auto_groups
```

## Performance Considerations

- Groups are cached in memory like other Evennia objects
- Member lookups are O(n) but groups are typically small
- Channel operations are handled efficiently by Evennia
- Database queries are minimized through object caching

## Troubleshooting

### Common Issues

1. **Groups not appearing**: Check if they're public and you have access
2. **Channel access issues**: Verify group membership and channel locks
3. **Auto-assignment not working**: Check character stats/template configuration
4. **Migration issues**: Verify Django models exist and are accessible

### Diagnostic Commands

```python
# Check group status
+group/sync          # Sync all character attributes
+group/syncchannels  # Fix channel locks
+group/synccleanup   # Clean orphaned data
+group/test <char>   # Test auto-assignment

# In Python shell
from typeclasses.groups import get_all_groups
groups = get_all_groups()
print(f"Found {len(groups)} groups")
```

### Logs

Check Evennia logs for group-related errors:
- Group creation/deletion messages
- Channel creation/lock updates
- Member assignment/removal
- Auto-assignment results

## API Reference

### Group TypeClass Methods

```python
# Core membership
group.add_member(character) -> bool
group.remove_member(character) -> bool
group.is_member(character) -> bool

# Member data
group.get_member_title(character) -> str
group.set_member_title(character, title) -> bool
group.get_member_role(character) -> str
group.set_member_role(character, role) -> bool

# Group info
group.get_member_count() -> int
group.get_online_members() -> list
group.get_online_count() -> int
```

### Utility Functions

```python
# Group creation/lookup
create_group(name, group_type='other', description='', creator=None) -> Group
get_group_by_id(group_id) -> Group or None
get_group_by_name(name) -> Group or None
get_all_groups() -> list
get_public_groups() -> list

# Character operations
get_character_groups(character) -> list
auto_assign_character_groups(character) -> list
assign_character_to_group(character, group, auto_assigned=True) -> bool
remove_character_from_group(character, group) -> bool
sync_character_group_attributes(character) -> list
```

This new TypeClass-based system provides a solid foundation for group management while maintaining backward compatibility with existing functionality. 
