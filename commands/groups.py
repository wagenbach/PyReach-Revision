from evennia.commands.default.muxcommand import MuxCommand
from evennia.utils import evtable
from evennia.comms.models import ChannelDB
from evennia.utils import create
from world.groups.utils import (
    assign_character_to_group, 
    remove_character_from_group,
    ensure_group_channel_exists,
    auto_assign_character_groups,
    get_character_groups
)
from typeclasses.groups import (
    Group, create_group, get_group_by_id, get_group_by_name, 
    get_all_groups, get_public_groups
)
from django.db.models import Q
from evennia.objects.models import ObjectDB
from evennia.utils.utils import time_format
from django.utils import timezone

class CmdGroups(MuxCommand):
    """
    Commands to create and manage player groups.
    
    Usage:
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
        +group/auto <char>         - Manually trigger automatic group assignment for a character
        +group/show <char>         - Show all groups a character belongs to
        +group/sync                - Sync all characters' group attributes (staff only)
        +group/sync <char>         - Sync a specific character's group attributes (staff only)
        +group/syncchannels        - Ensure all group channels exist and have proper locks (staff only)
        +group/synccleanup         - Remove orphaned group attributes (staff only)
        +group/test <character>    - Test group assignment for a character
        
    Group Types:
        coterie - Vampire groups
        pack - Werewolf groups
        cabal - Mage groups
        motley - Changeling groups
        conspiracy - Hunter groups
        agency - Mortal organizations
        cult - Religious/occult groups
        other - Generic groups
    """
    
    key = "+group"
    aliases = ["+groups"]
    locks = "cmd:all()"
    help_category = "Social and Communications"
    
    def parse(self):
        """Parse the command arguments."""
        super().parse()  # Initialize switches and other MuxCommand attributes
        
        args = self.args.strip()
        self.switches = []
    def list_groups(self):
        """List all public groups."""
        groups = get_public_groups()
        
        if not groups:
            self.caller.msg("No groups have been created yet.")
            return
        
        # Create table
        table = evtable.EvTable(
            "|wID|n", "|wName|n", "|wType|n", "|wMembers|n", "|wLeader|n",
            border="cells", width=78
        )
        
        for group in groups:
            member_count = group.get_member_count()
            leader_name = group.leader.name if group.leader else "None"
            
            table.add_row(
                f"#{group.group_id}",
                group.name,
                group.get_group_type_display(),
                str(member_count),
                leader_name
            )
        
        self.caller.msg(str(table))
    
    def view_group(self, group_id):
        """View detailed information about a group."""
        group = get_group_by_id(group_id)
        if not group:
            self.caller.msg(f"Group #{group_id} does not exist.")
            return
        
        # Check access
        is_staff = self.caller.check_permstring("Admin") or self.caller.check_permstring("Builder")
        is_member = group.is_member(self.caller)
        is_leader = group.leader == self.caller
        
        if not group.is_public and not is_staff and not is_member:
            self.caller.msg(f"Group #{group_id} is private and you don't have access to view it.")
            return
        
        # Build output
        output = [f"|y{group.name}|n (#{group.group_id})"]
        output.append(f"Type: {group.get_group_type_display()}")
        output.append(f"Leader: {group.leader.name if group.leader else 'None'}")
        output.append("")
        
        if group.description:
            output.append("|wDescription:|n")
            output.append(group.description)
            output.append("")
        
        # Members
        members = group.members
        if members:
            output.append("|wMembers:|n")
            for member in members:
                member_line = f"  {member.name}"
                title = group.get_member_title(member)
                if title:
                    member_line += f" - {title}"
                if member == group.leader:
                    member_line += " |y(Leader)|n"
                output.append(member_line)
            output.append("")
        
        # Private notes (if accessible)
        if group.notes and (is_staff or is_member):
            output.append("|wPrivate Notes:|n")
            output.append(group.notes)
        
        self.caller.msg("\n".join(output))
    
    def create_group(self, name):
        """Create a new group."""
        if not (self.caller.check_permstring("Admin") or self.caller.check_permstring("Builder")):
            self.caller.msg("You don't have permission to create groups.")
            return
        
        # Check if group already exists
        if get_group_by_name(name):
            self.caller.msg(f"A group named '{name}' already exists.")
            return
        
        # Create the group using TypeClass function
        try:
            group = create_group(name=name, creator=self.caller)
            self.caller.msg(f"Created group '{name}' with ID #{group.group_id}.")
            self.caller.msg(f"Created channel '{group.channel_name}' for group.")
        except ValueError as e:
            self.caller.msg(f"Error creating group: {str(e)}")
    
    def destroy_group(self, group_id):
        """Destroy a group."""
        if not (self.caller.check_permstring("Admin") or self.caller.check_permstring("Builder")):
            self.caller.msg("You don't have permission to destroy groups.")
            return
        
        group = get_group_by_id(group_id)
        if not group:
            self.caller.msg(f"Group #{group_id} does not exist.")
            return
        
        # Store info for messages
        group_name = group.name
        
        # Delete the group (handles all cleanup automatically)
        group.delete()
        
        self.caller.msg(f"Destroyed group '{group_name}' (ID #{group_id}).")
    
    def set_group_type(self, group_id, group_type):
        """Set the type of a group."""
        if not (self.caller.check_permstring("Admin") or self.caller.check_permstring("Builder")):
            self.caller.msg("You don't have permission to set group types.")
            return
        
        group = get_group_by_id(group_id)
        if not group:
            self.caller.msg(f"Group #{group_id} does not exist.")
            return
        
        valid_types = [choice[0] for choice in Group.GROUP_TYPES]
        if group_type not in valid_types:
            self.caller.msg(f"Invalid group type. Valid types: {', '.join(valid_types)}")
            return
        
        try:
            group.group_type = group_type
            self.caller.msg(f"Set group '{group.name}' type to {group.get_group_type_display()}.")
        except ValueError as e:
            self.caller.msg(f"Error setting group type: {str(e)}")
    
    def set_leader(self, group_id, character_name):
        """Set the leader of a group."""
        if not (self.caller.check_permstring("Admin") or self.caller.check_permstring("Builder")):
            self.caller.msg("You don't have permission to set group leaders.")
            return
        
        group = get_group_by_id(group_id)
        if not group:
            self.caller.msg(f"Group #{group_id} does not exist.")
            return
        
        # Find character
        character = self.caller.search(character_name, global_search=True)
        if not character:
            return
        
        # Set leader (TypeClass handles adding as member if needed)
        old_leader = group.leader.name if group.leader else "None"
        group.leader = character
        
        self.caller.msg(f"Set {character.name} as leader of '{group.name}' (was {old_leader}).")
    
    def set_description(self, group_id, description):
        """Set a group's description."""
        group = get_group_by_id(group_id)
        if not group:
            self.caller.msg(f"Group #{group_id} does not exist.")
            return
        
        # Check permissions
        is_staff = self.caller.check_permstring("Admin") or self.caller.check_permstring("Builder")
        is_leader = group.leader == self.caller
        
        if not is_staff and not is_leader:
            self.caller.msg("You don't have permission to set group descriptions.")
            return
        
        group.description = description
        self.caller.msg(f"Set description for group '{group.name}'.")
    
    def set_notes(self, group_id, notes):
        """Set a group's private notes."""
        group = get_group_by_id(group_id)
        if not group:
            self.caller.msg(f"Group #{group_id} does not exist.")
            return
        
        # Check permissions
        is_staff = self.caller.check_permstring("Admin") or self.caller.check_permstring("Builder")
        is_leader = group.leader == self.caller
        
        if not is_staff and not is_leader:
            self.caller.msg("You don't have permission to set group notes.")
            return
        
        group.notes = notes
        self.caller.msg(f"Set private notes for group '{group.name}'.")
    
    def set_title(self, group_id, character_name, title):
        """Set a character's title in a group."""
        group = get_group_by_id(group_id)
        if not group:
            self.caller.msg(f"Group #{group_id} does not exist.")
            return
        
        # Check permissions
        is_staff = self.caller.check_permstring("Admin") or self.caller.check_permstring("Builder")
        is_leader = group.leader == self.caller
        
        if not is_staff and not is_leader:
            self.caller.msg("You don't have permission to set member titles.")
            return
        
        # Find character
        character = self.caller.search(character_name, global_search=True)
        if not character:
            return
        
        # Check membership
        if not group.is_member(character):
            self.caller.msg(f"{character.name} is not a member of group '{group.name}'.")
            return
        
        old_title = group.get_member_title(character) or "None"
        if group.set_member_title(character, title):
            self.caller.msg(f"Set title for {character.name} in '{group.name}' to '{title}' (was '{old_title}').")
        else:
            self.caller.msg(f"Failed to set title for {character.name}.")
    
    def add_character(self, group_id, character_name):
        """Add a character to a group."""
        group = get_group_by_id(group_id)
        if not group:
            self.caller.msg(f"Group #{group_id} does not exist.")
            return
        
        # Check permissions
        is_staff = self.caller.check_permstring("Admin") or self.caller.check_permstring("Builder")
        is_leader = group.leader == self.caller
        
        if not is_staff and not is_leader:
            self.caller.msg("You don't have permission to add members to this group.")
            return
        
        # Find character
        character = self.caller.search(character_name, global_search=True)
        if not character:
            return
        
        # Use utility function to handle all assignment tasks
        if assign_character_to_group(character, group, auto_assigned=False):
            self.caller.msg(f"Added {character.name} to group '{group.name}' and channel '{group.channel_name}'.")
        else:
            self.caller.msg(f"{character.name} is already a member of '{group.name}'.")
    
    def remove_character(self, group_id, character_name):
        """Remove a character from a group."""
        group = get_group_by_id(group_id)
        if not group:
            self.caller.msg(f"Group #{group_id} does not exist.")
            return
        
        # Check permissions
        is_staff = self.caller.check_permstring("Admin") or self.caller.check_permstring("Builder")
        is_leader = group.leader == self.caller
        
        if not is_staff and not is_leader:
            self.caller.msg("You don't have permission to remove members from this group.")
            return
        
        # Find character
        character = self.caller.search(character_name, global_search=True)
        if not character:
            return
        
        # Check membership
        if not group.is_member(character):
            self.caller.msg(f"{character.name} is not a member of '{group.name}'.")
            return
        
        # Check if leader
        if group.leader == character:
            self.caller.msg(f"{character.name} is the leader. Set a new leader first.")
            return
        
        # Use utility function to handle all removal tasks
        if remove_character_from_group(character, group):
            self.caller.msg(f"Removed {character.name} from group '{group.name}' and channel '{group.channel_name}'.")
        else:
            self.caller.msg(f"Failed to remove {character.name} from group '{group.name}'.")
    
    def set_privacy(self, group_id, is_public):
        """Set a group as public or private."""
        group = get_group_by_id(group_id)
        if not group:
            self.caller.msg(f"Group #{group_id} does not exist.")
            return
        
        # Check permissions
        is_staff = self.caller.check_permstring("Admin") or self.caller.check_permstring("Builder")
        is_leader = group.leader == self.caller
        
        if not is_staff and not is_leader:
            self.caller.msg("You don't have permission to change group privacy.")
            return
        
        if group.is_public == is_public:
            self.caller.msg(f"Group '{group.name}' is already {'public' if is_public else 'private'}.")
            return
        
        group.is_public = is_public
        
        self.caller.msg(f"Set group '{group.name}' to {'public' if is_public else 'private'}.")
    
    def assign_auto_groups(self, character_name):
        """Manually trigger automatic group assignment for a character."""
        if not (self.caller.check_permstring("Admin") or self.caller.check_permstring("Builder")):
            self.caller.msg("You don't have permission to assign automatic groups.")
            return
        
        # Find character
        character = self.caller.search(character_name, global_search=True)
        if not character:
            return
        
        try:
            assigned_groups = auto_assign_character_groups(character)
            if assigned_groups:
                self.caller.msg(f"Auto-assigned {character.name} to groups: {', '.join(assigned_groups)}")
                character.msg(f"You have been automatically assigned to the following groups: {', '.join(assigned_groups)}")
            else:
                self.caller.msg(f"No automatic group assignments made for {character.name}")
        except Exception as e:
            self.caller.msg(f"Error assigning groups: {str(e)}")

    def show_character_groups(self, character_name):
        """Show all groups a character belongs to."""
        # Find character
        character = self.caller.search(character_name, global_search=True)
        if not character:
            return
        
        # Get groups
        groups = get_character_groups(character)
        
        if not groups:
            self.caller.msg(f"{character.name} is not a member of any groups.")
            return
        
        # Create table
        table = evtable.EvTable(
            "|wGroup|n", "|wType|n", "|wTitle|n", "|wRole|n",
            border="cells", width=78
        )
        
        for group in groups:
            # Get membership info
            title = group.get_member_title(character)
            role = group.get_member_role(character)
            
            # Check if leader
            if group.leader == character:
                role = "Leader" if not role else f"Leader, {role}"
            
            table.add_row(
                group.name,
                group.get_group_type_display(),
                title,
                role
            )
        
        output = [f"|y{character.name}'s Group Memberships|n"]
        output.append(str(table))
        
        # Show character attributes
        if character.attributes.has('groups'):
            char_groups = character.attributes.get('groups', [])
            output.append("")
            output.append(f"|wCharacter Group Attributes:|n {', '.join(char_groups)}")
        
        self.caller.msg("\n".join(output))

    def sync_character_groups(self, character):
        """Sync a single character's group attributes."""
        from world.groups.utils import sync_character_group_attributes
        try:
            synced_groups = sync_character_group_attributes(character)
            return synced_groups
        except Exception as e:
            self.caller.msg(f"Error syncing {character.name}: {str(e)}")
            return []
    
    def sync_all_characters(self):
        """Sync all characters' group attributes."""
        from typeclasses.characters import Character
        from evennia.utils.search import search_object
        
        all_chars = search_object("", typeclass=Character)
        synced_count = 0
        
        self.caller.msg(f"Syncing group attributes for {len(all_chars)} characters...")
        
        for char in all_chars:
            try:
                synced_groups = self.sync_character_groups(char)
                if synced_groups:
                    synced_count += 1
                    self.caller.msg(f"  {char.name}: {', '.join(synced_groups)}")
            except Exception as e:
                self.caller.msg(f"  Error with {char.name}: {str(e)}")
        
        self.caller.msg(f"Completed. Synced {synced_count} characters.")

    def test_groups(self):
        if not self.args:
            self.caller.msg("Usage: +testgroups <character>")
            return
        
        # Find character
        character = self.caller.search(self.args.strip(), global_search=True)
        if not character:
            return
        
        self.caller.msg(f"Testing group assignment for {character.name}")
        
        # Show character stats
        if hasattr(character, 'db') and character.db.stats:
            stats = character.db.stats
            other = stats.get('other', {})
            template = other.get('template', 'Unknown')
            self.caller.msg(f"Template: {template}")
            
            if template.lower() == 'vampire':
                clan = other.get('clan', 'Unknown')
                covenant = other.get('covenant', 'Unknown')
                self.caller.msg(f"Clan: {clan}, Covenant: {covenant}")
        
        # Test auto assignment
        try:
            assigned_groups = auto_assign_character_groups(character)
            if assigned_groups:
                self.caller.msg(f"Auto-assigned to groups: {', '.join(assigned_groups)}")
            else:
                self.caller.msg("No automatic group assignments made")
        except Exception as e:
            self.caller.msg(f"Error in assignment: {str(e)}")
            import traceback
            self.caller.msg(traceback.format_exc())
        
        # Show current groups
        try:
            current_groups = get_character_groups(character)
            if current_groups:
                group_names = [g.name for g in current_groups]
                self.caller.msg(f"Current groups: {', '.join(group_names)}")
            else:
                self.caller.msg("Not a member of any groups")
        except Exception as e:
            self.caller.msg(f"Error getting groups: {str(e)}")
        
        # Show attributes
        if character.attributes.has('groups'):
            attr_groups = character.attributes.get('groups', [])
            self.caller.msg(f"Group attributes: {', '.join(attr_groups)}")
        else:
            self.caller.msg("No group attributes set")

    def sync_channels(self):
        """Ensure all group channels exist with proper locks."""
        groups = get_all_groups()
        created_count = 0
        updated_count = 0
        
        self.caller.msg(f"Checking channels for {len(groups)} groups...")
        
        for group in groups:
            try:
                channel_name = group.channel_name
                channel = ChannelDB.objects.filter(db_key=channel_name).first()
                
                if not channel:
                    # Force recreation
                    group._create_group_channel()
                    created_count += 1
                    self.caller.msg(f"  Created channel for {group.name}")
                else:
                    # Check locks
                    expected_lock = (
                        f"control:perm(Admin);"
                        f"listen:group_member({group.group_id}) or perm(Admin);"
                        f"send:group_member({group.group_id}) or perm(Admin)"
                    )
                    if str(channel.locks) != expected_lock:
                        channel.locks.clear()
                        channel.locks.add(expected_lock)
                        updated_count += 1
                        self.caller.msg(f"  Updated locks for {group.name} channel")
            except Exception as e:
                self.caller.msg(f"  Error with {group.name}: {str(e)}")
        
        self.caller.msg(f"Completed. Created {created_count} new channels, updated {updated_count} locks.")
    
    def cleanup_orphaned_attributes(self):
        """Remove group attributes that don't correspond to actual memberships."""
        from typeclasses.characters import Character
        from evennia.utils.search import search_object
        
        all_chars = search_object("", typeclass=Character)
        cleaned_count = 0
        
        self.caller.msg(f"Cleaning up orphaned group attributes for {len(all_chars)} characters...")
        
        for char in all_chars:
            try:
                if char.attributes.has('groups'):
                    attr_groups = char.attributes.get('groups', [])
                    actual_groups = get_character_groups(char)
                    actual_group_names = [g.name for g in actual_groups]
                    
                    # Find orphaned attributes
                    orphaned = [g for g in attr_groups if g not in actual_group_names]
                    if orphaned:
                        # Update to only include actual memberships
                        char.attributes.add('groups', actual_group_names)
                        cleaned_count += 1
                        self.caller.msg(f"  {char.name}: Removed orphaned groups: {', '.join(orphaned)}")
                        
            except Exception as e:
                self.caller.msg(f"  Error with {char.name}: {str(e)}")
        
        self.caller.msg(f"Completed. Cleaned {cleaned_count} characters.")

    def func(self):
        """Execute the command."""
        if not self.args:
            if self.cmdstring == "+groups":
                self.list_groups()
                return
            
            self.caller.msg("Usage: +group <id> or +groups")
            return
        
        # Parse switches
        if self.switches:
            switch = self.switches[0]
            
            # Sync functionality (staff only)
            if switch == "sync":
                if not (self.caller.check_permstring("Admin") or self.caller.check_permstring("Builder")):
                    self.caller.msg("You don't have permission to sync groups.")
                    return
                
                if self.args.strip():
                    # Sync specific character
                    character = self.caller.search(self.args.strip(), global_search=True)
                    if not character:
                        return
                    
                    synced_groups = self.sync_character_groups(character)
                    if synced_groups:
                        self.caller.msg(f"Synced {character.name}: {', '.join(synced_groups)}")
                    else:
                        self.caller.msg(f"No groups found for {character.name}")
                else:
                    # Sync all characters
                    self.sync_all_characters()
                return
            
            if switch == "syncchannels":
                if not (self.caller.check_permstring("Admin") or self.caller.check_permstring("Builder")):
                    self.caller.msg("You don't have permission to sync channels.")
                    return
                self.sync_channels()
                return
            
            if switch == "synccleanup":
                if not (self.caller.check_permstring("Admin") or self.caller.check_permstring("Builder")):
                    self.caller.msg("You don't have permission to cleanup group data.")
                    return
                self.cleanup_orphaned_attributes()
                return
            
            if switch == "test":
                if not (self.caller.check_permstring("Admin") or self.caller.check_permstring("Builder")):
                    self.caller.msg("You don't have permission to test groups.")
                    return
                self.test_groups()
                return
            
            # Auto assignment
            if switch == "auto":
                self.assign_auto_groups(self.args.strip())
                return
            
            # Show character groups
            if switch == "show":
                self.show_character_groups(self.args.strip())
                return
            
            # Create
            if switch == "create":
                self.create_group(self.args.strip())
                return
            
            # Destroy
            if switch == "destroy":
                try:
                    group_id = int(self.args.strip())
                    self.destroy_group(group_id)
                except ValueError:
                    self.caller.msg("Group ID must be a number.")
                return
            
            # Private/Public
            if switch in ["private", "public"]:
                try:
                    group_id = int(self.args.strip())
                    self.set_privacy(group_id, switch == "public")
                except ValueError:
                    self.caller.msg("Group ID must be a number.")
                return
            
            # Title (special format)
            if switch == "title":
                if "/" in self.args and "=" in self.args:
                    group_char, title = self.args.split("=", 1)
                    parts = group_char.split("/", 1)
                    
                    if len(parts) == 2:
                        try:
                            group_id = int(parts[0].strip())
                            character_name = parts[1].strip()
                            self.set_title(group_id, character_name, title.strip())
                        except ValueError:
                            self.caller.msg("Group ID must be a number.")
                        return
                
                self.caller.msg("Usage: +group/title <id>/<char>=<title>")
                return
            
            # Commands with = format
            if "=" in self.args:
                group_id, value = self.args.split("=", 1)
                try:
                    group_id = int(group_id.strip())
                except ValueError:
                    self.caller.msg("Group ID must be a number.")
                    return
                
                value = value.strip()
                
                if switch == "type":
                    self.set_group_type(group_id, value)
                elif switch == "leader":
                    self.set_leader(group_id, value)
                elif switch == "desc":
                    self.set_description(group_id, value)
                elif switch == "note":
                    self.set_notes(group_id, value)
                elif switch == "add":
                    self.add_character(group_id, value)
                elif switch == "remove":
                    self.remove_character(group_id, value)
                else:
                    self.caller.msg(f"Unknown switch: {switch}")
                
                return
            
            self.caller.msg(f"Invalid format for switch '{switch}'.")
            return
        
        # View group
        try:
            group_id = int(self.args.strip())
            self.view_group(group_id)
        except ValueError:
            self.caller.msg("Group ID must be a number.") 

class CmdRoster(MuxCommand):
    """
    View the roster (member list) of a group.
    
    Usage:
        +roster                    - List all groups you can view rosters for
        +roster <group name>       - View the roster for a specific group
        +roster <group id>         - View the roster for a group by ID
        +roster/all                - List all public group rosters (staff only)
        
    This command shows both online and offline members of groups you have access to.
    You can view rosters for:
    - Public groups (anyone can view)
    - Private groups you're a member of
    - Any group (if you're staff)
    
    The roster shows member names, online status, group titles, and roles.
    """
    
    key = "+roster"
    locks = "cmd:all()"
    help_category = "Social and Communications"
    switch_options = ("all",)
    
    def list_available_groups(self):
        """List all groups the player can view rosters for."""
        # Get all public groups
        public_groups = get_public_groups()
        
        # Get private groups the player is a member of
        private_groups = []
        if not (self.caller.check_permstring("Admin") or self.caller.check_permstring("Builder")):
            all_groups = get_all_groups()
            private_groups = [g for g in all_groups if not g.is_public and g.is_member(self.caller)]
        else:
            # Staff can see all groups
            all_groups = get_all_groups()
            private_groups = [g for g in all_groups if not g.is_public]
        
        all_groups = list(public_groups) + list(private_groups)
        
        if not all_groups:
            self.caller.msg("No groups available to view rosters for.")
            return
        
        # Create table
        table = evtable.EvTable(
            "|wID|n", "|wName|n", "|wType|n", "|wAccess|n", "|wMembers|n",
            border="cells", width=78
        )
        
        for group in all_groups:
            member_count = group.get_member_count()
            access_type = "Public" if group.is_public else "Private"
            
            table.add_row(
                f"#{group.group_id}",
                group.name,
                group.get_group_type_display(),
                access_type,
                str(member_count)
            )
        
        output = ["|wAvailable Group Rosters:|n"]
        output.append(str(table))
        output.append("")
        output.append("Use '+roster <name>' or '+roster <id>' to view a specific roster.")
        
        self.caller.msg("\n".join(output))
    
    def view_group_roster(self, group_identifier):
        """View the roster for a specific group."""
        # Try to find group by ID first, then by name
        group = None
        try:
            group_id = int(group_identifier)
            group = get_group_by_id(group_id)
        except ValueError:
            # Try by name (case-insensitive)
            group = get_group_by_name(group_identifier)
        
        if not group:
            self.caller.msg(f"Group '{group_identifier}' not found.")
            return
        
        # Check access permissions
        is_staff = self.caller.check_permstring("Admin") or self.caller.check_permstring("Builder")
        is_member = group.is_member(self.caller)
        
        if not group.is_public and not is_staff and not is_member:
            self.caller.msg(f"Group '{group.name}' is private and you don't have access to view its roster.")
            return
        
        # Get all members for this group
        members = group.members
        
        if not members:
            self.caller.msg(f"Group '{group.name}' has no members.")
            return
        
        # Create table
        table = evtable.EvTable(
            "|wName|n", "|wStatus|n", "|wTitle|n", "|wRole|n", "|wLast Seen|n",
            border="cells", width=78
        )
        
        for member in members:
            # Determine online status
            if member.has_account:
                status = "|gOnline|n"
                last_seen = "Now"
            else:
                status = "|rOffline|n"
                # Try to get last login time
                if hasattr(member, 'db') and member.db.last_login:
                    try:
                        last_login = member.db.last_login
                        if hasattr(last_login, 'strftime'):
                            last_seen = last_login.strftime("%Y-%m-%d")
                        else:
                            last_seen = str(last_login)[:10]  # First 10 chars if it's a string
                    except:
                        last_seen = "Unknown"
                else:
                    last_seen = "Unknown"
            
            # Get title and role
            title = group.get_member_title(member)
            role = group.get_member_role(member)
            
            # Check if leader
            if group.leader == member:
                if role:
                    role = f"Leader, {role}"
                else:
                    role = "Leader"
            
            table.add_row(
                member.name,
                status,
                title,
                role,
                last_seen
            )
        
        # Build output
        output = [f"|y{group.name} Roster|n (#{group.group_id})"]
        output.append(f"Type: {group.get_group_type_display()}")
        output.append(f"Access: {'Public' if group.is_public else 'Private'}")
        output.append(f"Total Members: {len(members)}")
        output.append("")
        
        if group.description:
            output.append(f"|wDescription:|n {group.description}")
            output.append("")
        
        output.append(str(table))
        
        # Show online count
        online_count = group.get_online_count()
        output.append("")
        output.append(f"|wOnline Now:|n {online_count}/{len(members)} members")
        
        self.caller.msg("\n".join(output))
    
    def list_all_rosters(self):
        """List all public group rosters (staff only)."""
        if not (self.caller.check_permstring("Admin") or self.caller.check_permstring("Builder")):
            self.caller.msg("You don't have permission to view all rosters.")
            return
        
        groups = get_all_groups()
        
        if not groups:
            self.caller.msg("No groups exist.")
            return
        
        output = ["|wAll Group Rosters:|n"]
        
        for group in groups:
            members = group.members
            online_count = group.get_online_count()
            total_count = len(members)
            
            access_type = "Public" if group.is_public else "Private"
            output.append(f"|w{group.name}|n (#{group.group_id}) - {group.get_group_type_display()}")
            output.append(f"  {access_type} | {online_count}/{total_count} online | {total_count} total members")
            
            if total_count > 0:
                # Show online members
                online_members = [m.name for m in group.get_online_members()]
                if online_members:
                    output.append(f"  |gOnline:|n {', '.join(online_members)}")
                else:
                    output.append(f"  |rNo members currently online|n")
            
            output.append("")
        
        self.caller.msg("\n".join(output))
    
    def func(self):
        """Execute the command."""
        # Handle switches
        if "all" in self.switches:
            self.list_all_rosters()
            return
        
        # No arguments - list available groups
        if not self.args:
            self.list_available_groups()
            return
        
        # View specific group roster
        self.view_group_roster(self.args.strip()) 