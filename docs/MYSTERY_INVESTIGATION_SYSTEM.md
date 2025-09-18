# Mystery Investigation System

## Overview

The Mystery Investigation System allows storytellers and staff to create dynamic, discoverable mysteries that players can investigate through roleplay, skill checks, and interaction. This system supports both individual investigation and collaborative discovery, making it perfect for ongoing storylines and player-driven narratives.

## Key Features

- **Dynamic Mystery Creation**: Staff can create mysteries with multiple interconnected clues
- **Progressive Discovery**: Clues can have prerequisites and unlock new investigation paths
- **Multiple Discovery Methods**: Investigation, examination, research, interviews, and social interaction
- **Collaboration Support**: Players can share clues and work together
- **Automatic Revelations**: System can trigger story revelations when certain clues are discovered
- **Access Controls**: Mysteries can be restricted by template, character, or location
- **Progress Tracking**: Both staff and players can track investigation progress

## For Staff: Creating Mysteries

### Basic Mystery Creation

```
+mystery/create The Missing Heir = A wealthy family's heir has vanished without a trace, leaving behind only cryptic messages and suspicious circumstances.
```

### Adding Clues

```
+mystery/addclue 1 = Torn Letter/A letter with half the address torn off, found in the heir's room
+mystery/addclue 1 = Blood Stains/Small bloodstains on the windowsill that weren't there before
+mystery/addclue 1 = Witness Account/A neighbor saw someone leaving through the back garden
```

### Setting Prerequisites

```
+mystery/prereq 1/clue_1 = clue_0
+mystery/prereq 1/clue_2 = clue_0,clue_1
```

### Discovery Conditions

```
+mystery/conditions 1/clue_1 = {"skill_roll": {"skill": "investigation", "difficulty": 3}}
+mystery/conditions 1/clue_2 = {"attribute_minimum": {"attribute": "wits", "minimum": 3}}
+mystery/conditions 1/clue_3 = {"merit_required": {"merit": "contacts"}}
```

### Automatic Revelations

```
+mystery/revelation 1/major_discovery = clue_0,clue_1,clue_2/The evidence points to the heir being kidnapped by someone they trusted.
```

### Access Controls

```
+mystery/access 1 = templates/mortal,vampire
+mystery/access 1 = areas/downtown,warehouse_district
```

### Creating Physical Clue Objects

```
+clueobj/create torn letter = 1/clue_0
+clueobj/edit torn letter = discovery_message/You notice a crumpled letter under the desk
+clueobj/edit torn letter = skill_required/investigation
+clueobj/edit torn letter = difficulty/2
```

## For Players: Investigation Commands

### Viewing Available Mysteries

```
+investigation/mysteries           # List all mysteries you can access
+investigation/mystery 1           # View specific mystery details
+investigation/progress           # Show your progress across all mysteries
```

### Discovery Methods

```
+investigation/investigate        # General investigation of current area
+investigation/examine <object>   # Carefully examine an object for clues
+investigation/search <area>      # Search for hidden clues
+investigation/interview <person> # Interview someone for information
+investigation/research <topic>   # Research in libraries/databases
```

### Collaboration

```
+investigation/collaborate Alice  # Start collaborating with another investigator
+investigation/share Bob = torn letter  # Share a clue with someone
```

### Personal Clue Management (Original System)

```
+investigation/clue <name> = <description>  # Create personal clue
+investigation/list                        # List your personal clues
+investigation/view <clue>                # View clue details
+investigation/truth <clue1> <clue2>      # Attempt to uncover truth
```

## Example Investigation Scenario

### Staff Setup

1. **Create the Mystery**
```
+mystery/create The Vanishing Artist = Local artist Maria Santos disappeared from her studio, leaving behind unfinished paintings and strange symbols
```

2. **Add Progressive Clues**
```
+mystery/addclue 1 = Paint Smears/Fresh paint smears lead from the studio to the alley
+mystery/addclue 1 = Strange Symbol/An occult symbol carved into the studio wall
+mystery/addclue 1 = Witness Testimony/A homeless man saw "shadows moving wrong" that night
+mystery/addclue 1 = Missing Painting/Her latest painting is missing - it depicted the same symbol
+mystery/addclue 1 = Gallery Connection/The gallery owner has been asking about that specific painting
```

3. **Set Prerequisites**
```
+mystery/prereq 1/clue_2 = clue_0,clue_1  # Need paint smears and symbol to understand witness
+mystery/prereq 1/clue_4 = clue_2,clue_3  # Need symbol and witness to connect to gallery
```

4. **Add Discovery Conditions**
```
+mystery/conditions 1/clue_1 = {"skill_roll": {"skill": "investigation", "difficulty": 2}}
+mystery/conditions 1/clue_2 = {"merit_required": {"merit": "occult"}}
+mystery/conditions 1/clue_3 = {"attribute_minimum": {"attribute": "empathy", "minimum": 2}}
```

5. **Create Physical Clues**
```
+clueobj/create paint can = 1/clue_0
+clueobj/edit paint can = discovery_message/You notice the paint is still wet, forming a trail
```

6. **Set Up Revelation**
```
+mystery/revelation 1/gallery_connection = clue_3,clue_4/The gallery owner is involved in occult art trafficking and Maria discovered something she shouldn't have
```

### Player Experience

1. **Alice arrives at the studio**
```
+investigation/mysteries          # Sees "The Vanishing Artist" available
+investigation/mystery 1          # Views mystery details
+investigation/investigate        # Rolls Intelligence + Investigation
```

2. **Successful investigation reveals first clue**
```
> You discovered a clue: Paint Smears
> Fresh paint smears lead from the studio to the alley
```

3. **Alice examines the studio more carefully**
```
+investigation/examine paint can  # Discovers the paint trail clue
+investigation/search studio      # Might find the symbol
```

4. **Bob joins the investigation**
```
+investigation/collaborate Alice  # They team up
+investigation/share Bob = Paint Smears  # Alice shares what she found
```

5. **They interview the witness**
```
+investigation/interview homeless man  # Requires social roll
> The homeless man reveals: "Shadows moving wrong" testimony
```

6. **Research the symbol**
```
+investigation/research occult symbols  # In a library
> Your research uncovers: Strange Symbol clue
```

7. **Revelation triggers**
```
> REVELATION: The gallery owner is involved in occult art trafficking...
```

## Discovery Methods Detail

### Investigation Rolls
- **Intelligence + Investigation** for general clue discovery
- **Wits + Investigation** for hidden or time-sensitive clues
- Success levels determine how much is discovered

### Examination
- **Perception + Investigation** for detailed object analysis
- Can discover specific clue objects placed by staff
- May require specific skills or merits

### Social Discovery
- **Manipulation + Persuasion** for interviews
- **Presence + Socialize** for casual information gathering
- NPCs can be given specific clue information by staff

### Research
- **Intelligence + Academics** for book/database research
- **Intelligence + Computer** for digital research
- Requires appropriate location (library, computer access)

### Collaborative Bonuses
- Investigators working together get dice bonuses
- Shared clues can unlock new discovery paths
- Different skill sets complement each other

## Staff Management Commands

### Monitoring Progress
```
+mystery/progress                 # View all mystery progress
+mystery/progress 1               # View specific mystery progress
+mystery/discovered 1             # See who discovered what
+mystery/discovered 1 Alice       # See Alice's specific discoveries
```

### Manual Intervention
```
+mystery/grant Alice = 1/clue_2   # Manually grant a clue
+mystery/revoke Bob = 1/clue_1    # Remove a clue (if needed)
```

### Mystery Management
```
+mystery/list                     # List all mysteries
+mystery/view 1                   # Detailed mystery view
+mystery/status 1 = solved        # Mark mystery as solved
+mystery/edit 1/description = New description
```

## Advanced Features

### Time-Based Reveals
- Mysteries can have time-based triggers
- Clues can expire or change over time
- Seasonal or event-based mystery content

### Template Integration
- Different supernatural templates may see different clues
- Template-specific investigation bonuses
- Hidden supernatural elements in mysteries

### Location-Based Discovery
- Clues tied to specific locations
- Area-wide mysteries spanning multiple rooms
- Environmental storytelling through placed objects

### NPC Integration
- NPCs can hold clue information
- Social skills unlock NPC knowledge
- Dynamic NPC responses based on discovered clues

## Best Practices

### For Staff
1. **Start Simple**: Begin with 3-5 clues in a clear progression
2. **Multiple Paths**: Allow different approaches to discover the same information
3. **Collaborative Friendly**: Ensure multiple characters can meaningfully contribute
4. **Clear Prerequisites**: Make clue dependencies logical and discoverable
5. **Reward Creativity**: Use manual grants for creative investigation approaches

### For Players
1. **Work Together**: Collaboration provides bonuses and shared perspectives
2. **Try Different Methods**: Investigation, examination, research, and social approaches all work
3. **Share Information**: The system encourages and rewards information sharing
4. **Be Persistent**: Some clues require multiple attempts or specific conditions
5. **Think Creatively**: Staff can reward unusual but logical investigation approaches

## Integration with Existing Systems

### Experience Points
- Discovering clues can award investigation experience
- Solving mysteries provides story-based XP rewards
- Collaborative investigation builds social connections

### Combat System
- Investigation can reveal combat advantages
- Mystery clues might lead to equipment or allies
- Some mysteries involve dangerous discoveries

### Social System
- Interview mechanics tie into social maneuvering
- Reputation affects NPC willingness to share information
- Social merits provide investigation advantages

### Merit System
- Investigation-related merits provide bonuses
- Contacts and allies can provide clue information
- Occult and academic merits unlock specialized knowledge

This system transforms investigations from staff-dependent scenes into dynamic, player-driven experiences while maintaining story control and narrative coherence.
