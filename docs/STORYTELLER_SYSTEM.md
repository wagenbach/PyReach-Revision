# Storyteller System

## Overview

The Storyteller system allows players to run stories (PRPs) and manage game content without needing full staff permissions. Storytellers have access to specialized tools for creating engaging roleplay experiences while maintaining game balance and staff oversight.

## What is a Storyteller?

A Storyteller is a player who has been granted special permissions to:
- Create and manage investigation mysteries
- Create and control NPCs
- Use building commands in designated areas
- Access various storytelling tools

Storytellers are trusted community members who help create content and run stories for other players.

## Storyteller Permissions

### Mystery System Access
- **Create Mysteries**: Use `+mystery/create` and `+mystery/template` commands
- **Manage Clues**: Add clues, set prerequisites, and configure discovery conditions
- **Track Progress**: Monitor player investigation progress
- **Place Physical Clues**: Create discoverable objects with `+clueobj` commands
- **Manual Control**: Grant or revoke clues as needed for story purposes

### NPC Management
- **Create NPCs**: Generate NPCs using archetypes or create custom ones
- **Control NPCs**: Puppet NPCs for roleplay and story purposes
- **Manage Stats**: Apply damage, healing, and stat modifications
- **NPC Permissions**: Add other players as NPC controllers

### Limited Building Access
- **Room Modifications**: Basic room editing in designated story areas
- **Object Creation**: Create story-relevant objects and props
- **Area Management**: Limited access to area management tools

## Commands for Admins

### Managing Storytellers
```
+storyteller/list                    # List all current storytellers
+storyteller/add <character>         # Grant Storyteller flag
+storyteller/remove <character>      # Remove Storyteller flag
+storyteller/check [character]       # Check Storyteller status
+storyteller/info                    # Show system information
```

### Examples
```
+storyteller/add Alice               # Make Alice a storyteller
+storyteller/remove Bob              # Remove Bob's storyteller status
+storyteller/check Alice             # Check if Alice is a storyteller
+storyteller/list                    # See all active storytellers
```

## Commands for Everyone

### Checking Online Storytellers
```
+stwho                               # Show online staff and storytellers
+storyteller/check                   # Check your own storyteller status
+storyteller/info                    # Learn about the storyteller system
```

## Commands for Storytellers

Once granted Storyteller permissions, you have access to:

### Mystery System
```
+mystery/create <title> = <description>          # Create new mystery
+mystery/template <template_name> = [title]      # Use pre-built template
+mystery/addclue <mystery_id> = <name>/<desc>    # Add clues
+mystery/progress [mystery_id]                   # Track progress
+clueobj/create <name> = <mystery_id>/<clue_id>  # Place physical clues
```

### NPC Management
```
+npc/create <name> <type>                        # Create basic NPC
+npc/generate <name> <archetype> [type]          # Generate NPC with stats
+npc/puppet <npc>                                # Control an NPC
+npc/control <npc>                               # Add yourself as controller
+npc/stats <npc>                                 # View NPC sheet
```

### Information Commands
```
+mystery/list                                    # List your mysteries
+npc/list                                        # List NPCs in area
+stwho                                           # See online story staff
```

## How to Become a Storyteller

1. **Be an Active Player**: Demonstrate consistent, positive roleplay
2. **Show Story Interest**: Express interest in running stories for others
3. **Build Trust**: Establish yourself as a reliable community member
4. **Apply to Staff**: Contact an Admin about Storyteller permissions
5. **Get Approved**: Admin reviews your application and grants permissions

## Storyteller Guidelines

### Story Creation
- **Player-Focused**: Create stories that engage multiple players
- **Collaborative**: Work with players to develop their character arcs
- **Balanced**: Ensure challenges are appropriate for character power levels
- **Inclusive**: Make stories accessible to different character types

### NPC Usage
- **Support Role**: NPCs should support player stories, not overshadow them
- **Reasonable Stats**: Keep NPC power levels appropriate for the story
- **Temporary**: Most NPCs should be temporary story elements
- **Documented**: Keep notes on important recurring NPCs

### Mystery Design
- **Multiple Paths**: Allow different approaches to solve mysteries
- **Progressive**: Design clues that build on each other logically
- **Collaborative**: Enable players to work together on investigations
- **Rewarding**: Ensure discoveries feel meaningful and advance the story

### Best Practices
- **Communicate**: Keep staff informed of major story developments
- **Document**: Maintain records of ongoing stories and NPCs
- **Respect Limits**: Don't exceed your designated permissions
- **Ask Questions**: Contact staff when unsure about something

## Integration with Existing Systems

### Staff Oversight
- Storytellers report to staff for major story decisions
- Staff can monitor storyteller activities through logs
- Regular check-ins ensure stories align with game themes

### Player Safety
- Storytellers follow the same content policies as staff
- Players can report concerns about storyteller-run content
- Staff can revoke storyteller permissions if needed

### Game Balance
- Storyteller permissions are limited to prevent game disruption
- Major changes require staff approval
- Experience and resource rewards follow standard guidelines

## Technical Implementation

### Permission Checking
The system uses a flag-based approach:
```python
# Check if character has storyteller permissions
if check_storyteller_permission(character):
    # Grant access to storyteller commands
```

### Flag Management
- Storyteller flags are stored on both character and account objects
- Flags persist across character switches and logins
- Only Admins can grant or revoke storyteller flags

### Command Integration
- Mystery commands check for storyteller permissions
- NPC commands allow storyteller access
- Building commands respect storyteller limitations

## Example Storyteller Session

### Setup Phase
1. **Create Mystery**: `+mystery/template missing_person = The Vanishing Merchant`
2. **Review Mystery**: `+mystery/view 1` to see generated clues
3. **Place Clues**: `+clueobj/create merchant ledger = 1/clue_0`
4. **Create NPCs**: `+npc/generate Worried Wife mortal_social` for witnesses

### Running Phase
1. **Monitor Progress**: `+mystery/progress 1` to track player discoveries
2. **Puppet NPCs**: `+npc/puppet "Worried Wife"` for roleplay
3. **Adjust Story**: `+mystery/grant Alice = 1/clue_2` if needed
4. **Support Players**: Help players who are stuck without giving away answers

### Conclusion Phase
1. **Track Completion**: Monitor mystery resolution
2. **Cleanup NPCs**: `+npc/destroy` temporary NPCs
3. **Document Results**: Keep notes for future reference
4. **Plan Follow-up**: Consider sequel mysteries or character development

## Troubleshooting

### Common Issues
- **Permission Denied**: Contact an Admin to verify your storyteller status
- **Command Not Found**: Ensure you're using the correct command syntax
- **NPC Problems**: Check if you have control permissions for the NPC
- **Mystery Errors**: Verify mystery IDs and clue relationships

### Getting Help
- **+storyteller/info**: Review system information
- **Help Commands**: Use `help +mystery` or `help +npc` for command details
- **Staff Support**: Contact online staff for technical issues
- **Documentation**: Reference the full mystery system documentation

## Future Enhancements

### Planned Features
- **Story Templates**: Pre-built story frameworks for common scenarios
- **Player Feedback**: Systems for players to rate storyteller-run content
- **Advanced NPCs**: More sophisticated NPC behavior and interaction
- **Story Tracking**: Better tools for managing ongoing narratives

### Community Suggestions
The storyteller system evolves based on community feedback and needs. Storytellers and players are encouraged to suggest improvements and new features.
