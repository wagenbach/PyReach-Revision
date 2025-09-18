from evennia.utils import logger
from evennia.commands.default.general import CmdLook
from evennia.utils.search import search_object
from exordium.utils.search_helpers import search_character
from typeclasses.characters import Character
from evennia import Command
from evennia.utils import search
from evennia.commands.default.muxcommand import MuxCommand
from evennia.locks import lockfuncs
from evennia.utils.utils import inherits_from
from datetime import datetime
from django.utils import timezone
from evennia import default_cmds
from evennia.utils.search import search_object
from evennia.utils import evtable
from evennia.utils.utils import crop
from evennia.objects.models import ObjectDB
from world.groups.utils import (
    auto_assign_character_groups, 
    get_character_groups, 
    remove_character_from_group
)

# Import roster models if they exist, otherwise skip roster functionality
try:
    from world.cofd.models import Roster, RosterMember
    ROSTER_AVAILABLE = True
except ImportError:
    ROSTER_AVAILABLE = False

class CmdApprove(MuxCommand):
    """
    Approve a player's character.

    Usage:
      approve <character_name>

    This command approves a player's character, removing the 'unapproved' tag
    and adding the 'approved' tag. This allows the player to start playing.
    The character will also be automatically added to the appropriate roster
    based on their sphere/type.
    """
    key = "approve"
    aliases = ["+approve"]
    locks = "cmd:perm(Admin)"
    help_category = "Admin Commands"

    def func(self):
        if not self.args:
            self.caller.msg("Usage: +approve <character>")
            return
            
        # Use our new search helper
        target = search_character(self.caller, self.args)
        if not target:
            return

        # Check both tag and attribute for approval status
        is_approved = target.tags.has("approved", category="approval") and target.db.approved
        if is_approved:
            self.caller.msg(f"{target.name} is already approved.")
            return

        # Set both the tag and the attribute
        target.db.approved = True
        target.tags.remove("unapproved", category="approval")
        target.tags.add("approved", category="approval")
        
        # Determine character's sphere based on their splat
        sphere = 'Other'  # Default sphere with consistent capitalization
        if hasattr(target, 'db') and hasattr(target.db, 'stats'):
            stats = target.db.stats
            if stats and 'other' in stats and 'splat' in stats['other']:
                splat = stats['other']['splat'].get('Splat', {}).get('perm', '')
                if splat:
                    # Capitalize first letter for consistency
                    sphere = splat.capitalize()

        # Try to find a roster matching the sphere (case-insensitive)
        if ROSTER_AVAILABLE:
            try:
                roster = Roster.objects.filter(sphere__iexact=sphere).first()
                if roster:
                    # Add character to roster
                    if not RosterMember.objects.filter(roster=roster, character=target).exists():
                        RosterMember.objects.create(
                            roster=roster,
                            character=target,
                            approved=True,
                            approved_by=self.caller.account,
                            approved_date=timezone.now()
                        )
                        self.caller.msg(f"Added {target.name} to the {roster.name} roster.")
                else:
                    self.caller.msg(f"No roster found for sphere: {sphere}")
            except Exception as e:
                self.caller.msg(f"Error adding to roster: {str(e)}")
        else:
            self.caller.msg(f"Roster system not available. Character sphere: {sphere}")
        
        # Automatically assign character to appropriate groups
        try:
            assigned_groups = auto_assign_character_groups(target)
            if assigned_groups:
                self.caller.msg(f"Auto-assigned {target.name} to groups: {', '.join(assigned_groups)}")
                target.msg(f"You have been automatically assigned to the following groups: {', '.join(assigned_groups)}")
            else:
                self.caller.msg(f"No automatic group assignments made for {target.name}")
        except Exception as e:
            self.caller.msg(f"Error assigning groups: {str(e)}")
        
        logger.log_info(f"{target.name} has been approved by {self.caller.name}")

        self.caller.msg(f"You have approved {target.name}.")
        target.msg("Your character has been approved. You may now begin playing.")

class CmdUnapprove(MuxCommand):
    """
    Set a character's status to unapproved.

    Usage:
      unapprove <character_name>

    This command removes the 'approved' tag from a character and adds the 'unapproved' tag.
    This effectively reverts the character to an unapproved state, allowing them to use
    chargen commands again. The character will also be removed from any rosters they belong to.
    """
    key = "unapprove"
    aliases = ["+unapprove"]
    locks = "cmd:perm(Admin)"
    help_category = "Admin Commands"

    def func(self):
        if not self.args:
            self.caller.msg("Usage: unapprove <character_name>")
            return

        # Use our new search helper
        target = search_character(self.caller, self.args)
        if not target:
            return

        # Check both tag and attribute for approval status
        is_approved = target.tags.has("approved", category="approval") or target.db.approved
        if not is_approved:
            self.caller.msg(f"{target.name} is already unapproved.")
            return

        # Remove approved status and add unapproved tag
        target.db.approved = False
        target.tags.remove("approved", category="approval")
        target.tags.add("unapproved", category="approval")
        
        # Remove from any rosters
        if ROSTER_AVAILABLE:
            try:
                memberships = RosterMember.objects.filter(character=target)
                if memberships.exists():
                    roster_names = [m.roster.name for m in memberships]
                    memberships.delete()
                    self.caller.msg(f"Removed {target.name} from the following rosters: {', '.join(roster_names)}")
            except Exception as e:
                self.caller.msg(f"Error removing from rosters: {str(e)}")
        
        # Remove from all groups
        try:
            character_groups = get_character_groups(target)
            removed_groups = []
            
            for group in character_groups:
                if remove_character_from_group(target, group):
                    removed_groups.append(group.name)
            
            if removed_groups:
                self.caller.msg(f"Removed {target.name} from the following groups: {', '.join(removed_groups)}")
                target.msg(f"You have been removed from the following groups: {', '.join(removed_groups)}")
            else:
                self.caller.msg(f"{target.name} was not a member of any groups.")
                
        except Exception as e:
            self.caller.msg(f"Error removing from groups: {str(e)}")
        
        logger.log_info(f"{target.name} has been unapproved by {self.caller.name}")

        self.caller.msg(f"You have unapproved {target.name}.")
        target.msg("Your character has been unapproved. You may now use chargen commands again.")

class CmdMassUnapprove(MuxCommand):
    """
    Set all characters (both online and offline) to unapproved status.

    Usage:
      +massunapprove
      +massunapprove/confirm

    This command will list all characters that will be affected when run
    without the /confirm switch. Use /confirm to actually make the changes.
    This command affects ALL characters in the game, both online and offline.
    """

    key = "+massunapprove"
    locks = "cmd:perm(Admin)"
    help_category = "Admin Commands"

    def func(self):
        """Execute command."""
        caller = self.caller
        confirm = "confirm" in self.switches

        # Get all characters using Character typeclass
        all_chars = search_object("", typeclass=Character)
        
        # Filter to only get approved characters
        approved_chars = [char for char in all_chars 
                        if char.db.approved or char.tags.has("approved", category="approval")]
        
        if not approved_chars:
            caller.msg("No approved characters found.")
            return

        if not confirm:
            # Just show what would be affected
            msg = "The following characters would be set to unapproved:\n"
            for char in approved_chars:
                online_status = "online" if char.has_account else "offline"
                msg += f"- {char.name} ({online_status})\n"
            msg += f"\nTotal characters to be affected: {len(approved_chars)}"
            msg += "\nUse +massunapprove/confirm to execute the changes."
            caller.msg(msg)
            return

        # Actually make the changes
        count = 0
        total_groups_removed = 0
        
        for char in approved_chars:
            char.db.approved = False
            char.tags.add("unapproved", category="approval")
            if char.tags.has("approved", category="approval"):
                char.tags.remove("approved", category="approval")
            
            # Remove from groups
            try:
                character_groups = get_character_groups(char)
                for group in character_groups:
                    if remove_character_from_group(char, group):
                        total_groups_removed += 1
                
                if character_groups and char.has_account:  # Only message online characters
                    group_names = [g.name for g in character_groups]
                    char.msg(f"You have been removed from the following groups: {', '.join(group_names)}")
            except Exception as e:
                self.caller.msg(f"Error removing {char.name} from groups: {str(e)}")
            
            if char.has_account:  # Only message online characters
                char.msg("Your character has been set to unapproved status.")
            count += 1
            logger.log_info(f"{char.name} has been mass-unapproved by {caller.name}")

        caller.msg(f"Successfully set {count} character(s) to unapproved status.")
        if total_groups_removed > 0:
            caller.msg(f"Removed characters from a total of {total_groups_removed} group memberships.")

class CmdSummon(MuxCommand):
    """
    Summon a player or object to your location.

    Usage:
      +summon <character>
      +summon/quiet <character>
      +summon/debug <character> - Show additional diagnostic information

    Switches:
      quiet - Don't announce the summoning to the character
      debug - Display debug information about location storage
    """

    key = "+summon"
    locks = "cmd:perm(storyteller)"
    help_category = "Player Storyteller"
    switch_options = ("quiet", "debug")

    def func(self):
        """Implement the command"""
        caller = self.caller
        args = self.args.strip()
        debug_mode = "debug" in self.switches

        if not args:
            caller.msg("Usage: +summon <character>")
            return

        # Use our new search helper
        target = search_character(caller, args)
        if not target:
            return

        # Store their current location for +return
        if inherits_from(target, "evennia.objects.objects.DefaultCharacter"):
            original_location = target.location
            
            # Make sure the location is valid
            if original_location and hasattr(original_location, "id"):
                # Store location for return
                target.db.pre_summon_location = original_location
                
                if debug_mode:
                    caller.msg(f"DEBUG: Stored {original_location.name} (#{original_location.id}) as pre_summon_location for {target.name}")
            else:
                caller.msg(f"Warning: Could not store a valid original location for {target.name}")
                if debug_mode:
                    caller.msg(f"DEBUG: Current location is {original_location}")
            
        # Do the teleport
        if target.move_to(
            caller.location,
            quiet="quiet" in self.switches,
            emit_to_obj=caller,
            move_type="teleport",
        ):
            caller.msg(f"You have summoned {target.name} to your location.")
            if "quiet" not in self.switches:
                target.msg(f"{caller.name} has summoned you.")
            
            # Double-check storage worked
            if debug_mode and hasattr(target, "db"):
                if target.db.pre_summon_location:
                    stored_loc = target.db.pre_summon_location
                    caller.msg(f"DEBUG: Confirmed {target.name} has pre_summon_location: {stored_loc.name} (#{stored_loc.id})")
                else:
                    caller.msg(f"DEBUG: Failed to store pre_summon_location for {target.name}")
        else:
            caller.msg(f"Failed to summon {target.name}.")

class CmdReturn(MuxCommand):
    """
    Return a previously summoned character back to their original location.

    Usage:
      +return <character>
      +return/quiet <character>
      +return/all - Return all summoned characters in current location
      +return/force <character> - Use alternative location attributes if available
      +return/set <character> = <location> - Manually set return location

    Switches:
      quiet - Don't announce the return to the character
      all - Return all summoned characters in current location
      force - Try alternative location attributes (prelogout_location) if available
      set - Manually set a return location for a character
    """

    key = "+return"
    locks = "cmd:perm(storyteller)"
    help_category = "Player Storyteller"
    switch_options = ("quiet", "all", "force", "set")
    rhs_split = ("=",)

    def return_character(self, character, quiet=False, force=False):
        """Return a character to their pre-summon location"""
        # First try the primary location attribute
        if hasattr(character, "db") and character.db.pre_summon_location:
            prev_location = character.db.pre_summon_location
            location_type = "pre-summon"
        # If force is True, try alternative location attributes
        elif force and hasattr(character, "db"):
            # Try prelogout_location as fallback
            if character.db.prelogout_location:
                prev_location = character.db.prelogout_location
                location_type = "prelogout"
            else:
                self.caller.msg(f"{character.name} has no stored locations to return to.")
                return False
        else:
            self.caller.msg(f"{character.name} has no stored previous location to return to.")
            self.caller.msg("Use +return/force to try alternative location attributes, or +return/set to set one manually.")
            return False

        # Verify the location still exists
        if not prev_location or not prev_location.id:
            self.caller.msg(f"The previous {location_type} location for {character.name} no longer exists.")
            if location_type == "pre-summon":
                character.attributes.remove("pre_summon_location")
            return False
            
        # Move the character back
        if character.move_to(
            prev_location,
            quiet=quiet,
            emit_to_obj=self.caller,
            move_type="teleport",
        ):
            self.caller.msg(f"Returned {character.name} to their {location_type} location: {prev_location.name}.")
            if not quiet:
                character.msg(f"{self.caller.name} has returned you to your previous location.")
                
            # Clear the stored location if it was pre_summon_location
            if location_type == "pre-summon":
                character.attributes.remove("pre_summon_location")
            return True
        else:
            self.caller.msg(f"Failed to return {character.name}.")
            return False

    def func(self):
        """Implement the command"""
        caller = self.caller
        args = self.args.strip()
        quiet = "quiet" in self.switches
        force = "force" in self.switches

        # Handle setting a return location manually
        if "set" in self.switches:
            if not self.rhs:
                caller.msg("Usage: +return/set <character> = <location>")
                return
                
            # Use our new search helper
            target = search_character(caller, self.lhs)
            if not target:
                return
                
            destination = caller.search(self.rhs, global_search=True)
            if not destination:
                return
                
            # Set the pre_summon_location attribute
            target.db.pre_summon_location = destination
            caller.msg(f"Set return location for {target.name} to {destination.name}.")
            return

        if "all" in self.switches:
            # Return all summoned characters in the current location
            returned_count = 0
            for character in caller.location.contents:
                if inherits_from(character, "evennia.objects.objects.DefaultCharacter"):
                    if self.return_character(character, quiet, force):
                        returned_count += 1
                        
            if returned_count:
                caller.msg(f"Returned {returned_count} character(s) to their previous locations.")
            else:
                caller.msg("No characters with stored previous locations found here.")
            return

        if not args:
            caller.msg("Usage: +return <character>")
            return

        # Use our new search helper
        target = search_character(caller, args)
        if not target:
            return
            
        # Return the character
        self.return_character(target, quiet, force)