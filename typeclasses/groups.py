"""
Group TypeClasses for Evennia.

This module contains the TypeClass definitions for groups, replacing the Django model approach
with proper Evennia TypeClasses for better integration and functionality.
"""

from evennia import DefaultObject, create_object, logger
from evennia.comms.models import ChannelDB
from evennia.utils import create as utils_create
from django.conf import settings


class Group(DefaultObject):
    """
    A TypeClass for groups that can contain characters as members.
    
    This replaces the Django model approach with a proper Evennia TypeClass,
    providing better integration with the Evennia architecture.
    """
    
    # Group types as choices
    GROUP_TYPES = [
        ('coterie', 'Coterie'),      # Vampire groups
        ('pack', 'Pack'),            # Werewolf groups  
        ('cabal', 'Cabal'),          # Mage groups
        ('motley', 'Motley'),        # Changeling groups
        ('conspiracy', 'Conspiracy'), # Hunter groups
        ('agency', 'Agency'),        # Mortal organizations
        ('cult', 'Cult'),            # Religious/occult groups
        ('other', 'Other'),          # Generic groups
    ]
    
    def at_object_creation(self):
        """Called when the group is first created."""
        super().at_object_creation()
        
        # Set default attributes
        self.db.group_type = 'other'
        self.db.description = ''
        self.db.notes = ''
        self.db.is_public = True
        self.db.leader = None
        self.db.members = []
        self.db.member_data = {}  # Store member titles, roles, etc.
        self.db.created_at = self.date_created
        
        # Auto-assign group ID
        self._assign_group_id()
        
        # Create associated channel
        self._create_group_channel()
    
    def _assign_group_id(self):
        """Assign a unique group ID."""
        # Get all existing group IDs
        existing_ids = []
        for obj in Group.objects.all():
            if hasattr(obj, 'db') and obj.db.group_id:
                existing_ids.append(obj.db.group_id)
        
        # Find the lowest available ID
        group_id = 1
        while group_id in existing_ids:
            group_id += 1
        
        self.db.group_id = group_id
    
    def _create_group_channel(self):
        """Create the associated channel for this group."""
        channel_name = self.channel_name
        
        if ChannelDB.objects.filter(db_key=channel_name).exists():
            logger.log_info(f"Channel '{channel_name}' already exists for group '{self.name}'")
            return
        
        # Make sure group_id is available
        if not hasattr(self.db, 'group_id') or self.db.group_id is None:
            logger.log_err(f"Cannot create channel for group '{self.name}' - group_id not set")
            return
        
        # Create channel with appropriate locks
        lock_string = (
            f"control:perm(Admin);"
            f"listen:group_member({self.db.group_id}) or perm(Admin);"
            f"send:group_member({self.db.group_id}) or perm(Admin)"
        )
        
        try:
            channel = utils_create.create_channel(
                channel_name,
                desc=f"Group channel for {self.name}",
                locks=lock_string
            )
            logger.log_info(f"Created channel '{channel_name}' for group '{self.name}'")
        except Exception as e:
            logger.log_err(f"Failed to create channel '{channel_name}': {str(e)}")
    
    @property
    def channel_name(self):
        """Returns the channel name for this group."""
        return ''.join(c for c in self.name if c.isalnum())
    
    @property
    def group_id(self):
        """Returns the group ID."""
        return self.db.group_id
    
    @property
    def group_type(self):
        """Returns the group type."""
        return self.db.group_type
    
    @group_type.setter
    def group_type(self, value):
        """Set the group type."""
        valid_types = [choice[0] for choice in self.GROUP_TYPES]
        if value in valid_types:
            self.db.group_type = value
        else:
            raise ValueError(f"Invalid group type. Must be one of: {', '.join(valid_types)}")
    
    def get_group_type_display(self):
        """Get the display name for the group type."""
        type_dict = dict(self.GROUP_TYPES)
        return type_dict.get(self.db.group_type, 'Other')
    
    @property
    def description(self):
        """Returns the group description."""
        return self.db.description
    
    @description.setter
    def description(self, value):
        """Set the group description."""
        self.db.description = value
    
    @property
    def notes(self):
        """Returns the group notes."""
        return self.db.notes
    
    @notes.setter
    def notes(self, value):
        """Set the group notes."""
        self.db.notes = value
    
    @property
    def is_public(self):
        """Returns whether the group is public."""
        return self.db.is_public
    
    @is_public.setter
    def is_public(self, value):
        """Set the group's public status."""
        self.db.is_public = bool(value)
    
    @property
    def leader(self):
        """Returns the group leader."""
        return self.db.leader
    
    @leader.setter
    def leader(self, character):
        """Set the group leader."""
        if character and not self.is_member(character):
            self.add_member(character)
        self.db.leader = character
    
    @property
    def members(self):
        """Returns a list of group members."""
        # Clean up any None entries that might have accumulated
        members = [member for member in self.db.members if member]
        self.db.members = members
        return members
    
    def is_member(self, character):
        """Check if a character is a member of this group."""
        return character in self.members
    
    def add_member(self, character):
        """Add a character to the group."""
        if not self.is_member(character):
            self.db.members.append(character)
            
            # Initialize member data if not exists
            if character not in self.db.member_data:
                self.db.member_data[character] = {
                    'title': '',
                    'role': '',
                    'joined_at': character.db.last_login or self.db.created_at
                }
            
            # Update character's group attribute
            if not character.attributes.has('groups'):
                character.attributes.add('groups', [])
            
            groups = character.attributes.get('groups', [])
            if self.name not in groups:
                groups.append(self.name)
                character.attributes.add('groups', groups)
            
            # Add to channel
            channel = ChannelDB.objects.filter(db_key=self.channel_name).first()
            if channel:
                channel.connect(character)
            
            logger.log_info(f"Added {character.name} to group '{self.name}'")
            return True
        return False
    
    def remove_member(self, character):
        """Remove a character from the group."""
        if self.is_member(character):
            self.db.members.remove(character)
            
            # Remove member data
            if character in self.db.member_data:
                del self.db.member_data[character]
            
            # Clear leader if this was the leader
            if self.db.leader == character:
                self.db.leader = None
            
            # Update character's group attribute
            if character.attributes.has('groups'):
                groups = character.attributes.get('groups', [])
                if self.name in groups:
                    groups.remove(self.name)
                    character.attributes.add('groups', groups)
            
            # Remove from channel
            channel = ChannelDB.objects.filter(db_key=self.channel_name).first()
            if channel:
                channel.disconnect(character)
            
            logger.log_info(f"Removed {character.name} from group '{self.name}'")
            return True
        return False
    
    def get_member_title(self, character):
        """Get a member's title in the group."""
        if character in self.db.member_data:
            return self.db.member_data[character].get('title', '')
        return ''
    
    def set_member_title(self, character, title):
        """Set a member's title in the group."""
        if self.is_member(character):
            if character not in self.db.member_data:
                self.db.member_data[character] = {}
            self.db.member_data[character]['title'] = title
            return True
        return False
    
    def get_member_role(self, character):
        """Get a member's role in the group."""
        if character in self.db.member_data:
            return self.db.member_data[character].get('role', '')
        return ''
    
    def set_member_role(self, character, role):
        """Set a member's role in the group."""
        if self.is_member(character):
            if character not in self.db.member_data:
                self.db.member_data[character] = {}
            self.db.member_data[character]['role'] = role
            return True
        return False
    
    def get_member_count(self):
        """Get the number of members in the group."""
        return len(self.members)
    
    def get_online_members(self):
        """Get list of online members."""
        return [member for member in self.members if member.has_account]
    
    def get_online_count(self):
        """Get the number of online members."""
        return len(self.get_online_members())
    
    def delete(self):
        """Override delete to clean up associated data."""
        # Remove all members (this handles attribute cleanup)
        for member in self.members[:]:  # Copy list to avoid modification during iteration
            self.remove_member(member)
        
        # Delete associated channel
        channel = ChannelDB.objects.filter(db_key=self.channel_name).first()
        if channel:
            # Disconnect any remaining subscribers
            for subscriber in channel.subscriptions.all():
                channel.disconnect(subscriber)
            channel.delete()
            logger.log_info(f"Deleted channel '{self.channel_name}'")
        
        # Call parent delete
        super().delete()
        logger.log_info(f"Deleted group '{self.name}' (ID #{self.db.group_id})")


# Convenience functions for group management
def create_group(name, group_type='other', description='', creator=None):
    """
    Create a new group.
    
    Args:
        name (str): Name of the group
        group_type (str): Type of group (default: 'other')
        description (str): Group description
        creator (Character): Character creating the group
        
    Returns:
        Group: The created group object
    """
    # Check if group with this name already exists
    existing = Group.objects.filter(db_key=name).first()
    if existing:
        raise ValueError(f"A group named '{name}' already exists.")
    
    # Create the group
    group = create_object(
        typeclass="typeclasses.groups.Group",
        key=name,
        location=None  # Groups don't have a physical location
    )
    
    # Set initial properties
    group.group_type = group_type
    group.description = description
    
    if creator:
        group.leader = creator
    
    return group


def get_group_by_id(group_id):
    """
    Get a group by its ID.
    
    Args:
        group_id (int): The group ID
        
    Returns:
        Group or None: The group object if found
    """
    for group in Group.objects.all():
        if hasattr(group, 'db') and group.db.group_id == group_id:
            return group
    return None


def get_group_by_name(name):
    """
    Get a group by its name (case-insensitive).
    
    Args:
        name (str): The group name
        
    Returns:
        Group or None: The group object if found
    """
    return Group.objects.filter(db_key__iexact=name).first()


def get_all_groups():
    """
    Get all groups.
    
    Returns:
        QuerySet: All group objects
    """
    return Group.objects.all()


def get_public_groups():
    """
    Get all public groups.
    
    Returns:
        list: List of public group objects
    """
    all_groups = Group.objects.all()
    return [group for group in all_groups if group.is_public]


def get_character_groups(character):
    """
    Get all groups a character belongs to.
    
    Args:
        character: The character object
        
    Returns:
        list: List of group objects the character belongs to
    """
    all_groups = Group.objects.all()
    return [group for group in all_groups if group.is_member(character)] 