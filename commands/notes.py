from evennia.commands.default.muxcommand import MuxCommand
from evennia.utils import evtable
from evennia import search_object
from datetime import datetime


class CmdNote(MuxCommand):
    """
    Manage character notes and long-form narrative content.
    
    Usage:
        +note [title]/[category]=[Note Text]     - Create a new note
        +note                                    - View all your notes
        +note/edit [title]=[New text]           - Edit an existing note
        +note/delete [title]                    - Delete a note (player or staff)
        +note/approve [character]=[title]       - Approve a note (staff only, locks editing)
        +note/unapprove [character]=[title]     - Unapprove a note (staff only, unlocks editing)
        +note/show [title]                      - Show a note to everyone in the room
        +note/show [title]=[player name]        - Show a note privately to a specific player
    
    Notes are long-form narrative content that you can create on your character.
    Each note has a title, category, and text. Staff can approve notes to lock them
    from further editing.
    
    Examples:
        +note My Backstory/Background=I was born in a small town...
        +note
        +note/edit My Backstory=I was actually born in a large city...
        +note/delete My Backstory
        +note/show My Backstory
        +note/show My Backstory=Bob
    """
    
    key = "+note"
    aliases = ["+notes"]
    help_category = "Character"
    locks = "cmd:all()"
    
    def func(self):
        """Execute the command"""
        if not self.switches:
            if not self.args:
                # View all notes
                self.view_notes()
            else:
                # Create a new note
                self.create_note()
        else:
            switch = self.switches[0].lower()
            
            if switch == "edit":
                self.edit_note()
            elif switch == "delete":
                self.delete_note()
            elif switch == "approve":
                self.approve_note()
            elif switch == "unapprove":
                self.unapprove_note()
            elif switch == "show":
                self.show_note()
            else:
                self.caller.msg("Invalid switch. See 'help +note' for usage.")
    
    def create_note(self):
        """Create a new note: +note [title]/[category]=[Note Text]"""
        if "/" not in self.args or "=" not in self.args:
            self.caller.msg("Usage: +note [title]/[category]=[Note Text]")
            return
        
        try:
            # Split the args to get title/category and text
            lhs, rhs = self.args.split("=", 1)
            title, category = lhs.split("/", 1)
            title = title.strip()
            category = category.strip()
            text = rhs.strip()
        except ValueError:
            self.caller.msg("Usage: +note [title]/[category]=[Note Text]")
            return
        
        if not title or not category or not text:
            self.caller.msg("All fields (title, category, and text) must be provided.")
            return
        
        # Initialize notes if not exists
        if not self.caller.db.notes:
            self.caller.db.notes = []
        
        # Check if a note with this title already exists
        existing_note = None
        for note in self.caller.db.notes:
            if note["title"].lower() == title.lower():
                existing_note = note
                break
        
        if existing_note:
            self.caller.msg(f"A note with the title '{title}' already exists. Use +note/edit to modify it.")
            return
        
        # Create the note
        new_note = {
            "title": title,
            "category": category,
            "text": text,
            "approved": False,
            "created": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
            "modified": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        }
        
        self.caller.db.notes.append(new_note)
        self.caller.msg(f"|gNote created:|n '{title}' in category '{category}'")
    
    def view_notes(self):
        """View all notes on the character"""
        notes = self.caller.db.notes or []
        
        if not notes:
            self.caller.msg("You have no notes.")
            return
        
        # Create a table for displaying notes
        table = evtable.EvTable(
            "|wTitle|n",
            "|wCategory|n",
            "|wStatus|n",
            "|wCreated|n",
            border="cells",
            width=78
        )
        
        for note in notes:
            status = "|gApproved|n" if note["approved"] else "|yDraft|n"
            table.add_row(
                note["title"],
                note["category"],
                status,
                note["created"]
            )
        
        output = ["|wYour Notes|n", str(table)]
        output.append("\nUse '+note/show <title>' to view the full text of a note.")
        self.caller.msg("\n".join(output))
    
    def edit_note(self):
        """Edit an existing note: +note/edit [title]=[New text]"""
        if "=" not in self.args:
            self.caller.msg("Usage: +note/edit [title]=[New text]")
            return
        
        try:
            title, new_text = self.args.split("=", 1)
            title = title.strip()
            new_text = new_text.strip()
        except ValueError:
            self.caller.msg("Usage: +note/edit [title]=[New text]")
            return
        
        if not title or not new_text:
            self.caller.msg("Both title and new text must be provided.")
            return
        
        notes = self.caller.db.notes or []
        
        # Find the note
        found_note = None
        for note in notes:
            if note["title"].lower() == title.lower():
                found_note = note
                break
        
        if not found_note:
            self.caller.msg(f"You don't have a note titled '{title}'.")
            return
        
        # Check if the note is approved
        if found_note["approved"]:
            self.caller.msg(f"The note '{title}' is approved and cannot be edited. Contact staff to unapprove it first.")
            return
        
        # Update the note
        found_note["text"] = new_text
        found_note["modified"] = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        
        self.caller.msg(f"|gNote updated:|n '{title}'")
    
    def delete_note(self):
        """Delete a note: +note/delete [title]"""
        if not self.args:
            self.caller.msg("Usage: +note/delete [title]")
            return
        
        title = self.args.strip()
        notes = self.caller.db.notes or []
        
        # Find and remove the note
        found_note = None
        for i, note in enumerate(notes):
            if note["title"].lower() == title.lower():
                found_note = note
                found_index = i
                break
        
        if not found_note:
            self.caller.msg(f"You don't have a note titled '{title}'.")
            return
        
        # Check permissions - staff can always delete
        is_staff = self.caller.check_permstring("builders")
        
        if found_note["approved"] and not is_staff:
            self.caller.msg(f"The note '{title}' is approved and cannot be deleted. Contact staff for assistance.")
            return
        
        # Remove the note
        del notes[found_index]
        self.caller.msg(f"|rNote deleted:|n '{title}'")
    
    def approve_note(self):
        """Approve a note (staff only): +note/approve [character]=[title]"""
        if not self.caller.check_permstring("builders"):
            self.caller.msg("Only staff can approve notes.")
            return
        
        if "=" not in self.args:
            self.caller.msg("Usage: +note/approve [character]=[title]")
            return
        
        try:
            character_name, title = self.args.split("=", 1)
            character_name = character_name.strip()
            title = title.strip()
        except ValueError:
            self.caller.msg("Usage: +note/approve [character]=[title]")
            return
        
        if not character_name or not title:
            self.caller.msg("Both character name and note title must be provided.")
            return
        
        # Search for the character
        character = search_object(character_name)
        
        if not character:
            self.caller.msg(f"Could not find character '{character_name}'.")
            return
        
        if len(character) > 1:
            self.caller.msg(f"Multiple matches found for '{character_name}'. Please be more specific.")
            return
        
        character = character[0]
        
        # Check if it's a character object
        if not character.has_account:
            self.caller.msg(f"'{character_name}' is not a character.")
            return
        
        notes = character.db.notes or []
        
        # Find the note
        found_note = None
        for note in notes:
            if note["title"].lower() == title.lower():
                found_note = note
                break
        
        if not found_note:
            self.caller.msg(f"Character '{character_name}' doesn't have a note titled '{title}'.")
            return
        
        if found_note["approved"]:
            self.caller.msg(f"The note '{title}' is already approved.")
            return
        
        # Approve the note
        found_note["approved"] = True
        found_note["approved_by"] = self.caller.name
        found_note["approved_date"] = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        
        self.caller.msg(f"|gApproved note:|n '{title}' for {character.name}")
        
        # Notify the character owner if they're online
        if character.sessions.all():
            character.msg(f"|gYour note '{title}' has been approved by {self.caller.name}.|n")
    
    def unapprove_note(self):
        """Unapprove a note (staff only): +note/unapprove [character]=[title]"""
        if not self.caller.check_permstring("builders"):
            self.caller.msg("Only staff can unapprove notes.")
            return
        
        if "=" not in self.args:
            self.caller.msg("Usage: +note/unapprove [character]=[title]")
            return
        
        try:
            character_name, title = self.args.split("=", 1)
            character_name = character_name.strip()
            title = title.strip()
        except ValueError:
            self.caller.msg("Usage: +note/unapprove [character]=[title]")
            return
        
        if not character_name or not title:
            self.caller.msg("Both character name and note title must be provided.")
            return
        
        # Search for the character
        character = search_object(character_name)
        
        if not character:
            self.caller.msg(f"Could not find character '{character_name}'.")
            return
        
        if len(character) > 1:
            self.caller.msg(f"Multiple matches found for '{character_name}'. Please be more specific.")
            return
        
        character = character[0]
        
        # Check if it's a character object
        if not character.has_account:
            self.caller.msg(f"'{character_name}' is not a character.")
            return
        
        notes = character.db.notes or []
        
        # Find the note
        found_note = None
        for note in notes:
            if note["title"].lower() == title.lower():
                found_note = note
                break
        
        if not found_note:
            self.caller.msg(f"Character '{character_name}' doesn't have a note titled '{title}'.")
            return
        
        if not found_note["approved"]:
            self.caller.msg(f"The note '{title}' is not approved.")
            return
        
        # Unapprove the note
        found_note["approved"] = False
        if "approved_by" in found_note:
            del found_note["approved_by"]
        if "approved_date" in found_note:
            del found_note["approved_date"]
        
        self.caller.msg(f"|yUnapproved note:|n '{title}' for {character.name}")
        
        # Notify the character owner if they're online
        if character.sessions.all():
            character.msg(f"|yYour note '{title}' has been unapproved by {self.caller.name}. You can now edit it.|n")
    
    def show_note(self):
        """Show a note to the room or to a specific player"""
        if not self.args:
            self.caller.msg("Usage: +note/show [title] or +note/show [title]=[player name]")
            return
        
        # Check if showing to a specific player
        if "=" in self.args:
            title, target_name = self.args.split("=", 1)
            title = title.strip()
            target_name = target_name.strip()
            show_to_room = False
        else:
            title = self.args.strip()
            target_name = None
            show_to_room = True
        
        notes = self.caller.db.notes or []
        
        # Find the note
        found_note = None
        for note in notes:
            if note["title"].lower() == title.lower():
                found_note = note
                break
        
        if not found_note:
            self.caller.msg(f"You don't have a note titled '{title}'.")
            return
        
        # Format the note for display
        output = []
        output.append("|w" + "=" * 78 + "|n")
        output.append(f"|wNote:|n {found_note['title']}")
        output.append(f"|wCategory:|n {found_note['category']}")
        output.append(f"|wAuthor:|n {self.caller.name}")
        
        if found_note["approved"]:
            output.append(f"|wStatus:|n |gApproved|n")
            if "approved_by" in found_note:
                output.append(f"|wApproved by:|n {found_note['approved_by']} on {found_note.get('approved_date', 'Unknown')}")
        else:
            output.append(f"|wStatus:|n |yDraft|n")
        
        output.append("|w" + "=" * 78 + "|n")
        output.append(found_note["text"])
        output.append("|w" + "=" * 78 + "|n")
        
        note_display = "\n".join(output)
        
        if show_to_room:
            # Show to everyone in the room
            location = self.caller.location
            if not location:
                self.caller.msg("You are not in a room.")
                return
            
            # Send to everyone in the room
            location.msg_contents(f"{self.caller.name} shares a note:\n{note_display}", exclude=[self.caller])
            self.caller.msg(f"You show '{title}' to the room:\n{note_display}")
        else:
            # Show to a specific player
            target = search_object(target_name)
            
            if not target:
                self.caller.msg(f"Could not find player '{target_name}'.")
                return
            
            if len(target) > 1:
                self.caller.msg(f"Multiple matches found for '{target_name}'. Please be more specific.")
                return
            
            target = target[0]
            
            # Check if target is online
            if not target.sessions.all():
                self.caller.msg(f"{target.name} is not currently online.")
                return
            
            # Send to target
            target.msg(f"{self.caller.name} shares a note with you:\n{note_display}")
            self.caller.msg(f"You show '{title}' to {target.name}.")

