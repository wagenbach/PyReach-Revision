# Enhanced Room System Usage Guide

This guide explains how to use the enhanced Room typeclass and related commands to create immersive, formatted room displays.

## Overview

The enhanced Room system provides:
- Formatted room headers with location hierarchy
- Character display with idle times and short descriptions
- Separated cardinal directions from other exits
- Places system for detailed location descriptions
- IC Area mapping integration

## Setting Up a Room

### 1. Create a Room with the Enhanced Typeclass

```
@create The Square:typeclasses.rooms.Room
```

### 2. Set the Room Description

```
@desc The Square = The Square, the hub and heart of this growing hollow and the place with enough room to host the whole freehold if need be. Cobblestones cover the ground here, smooth and rusted red, almost uniform save for the odd few that remain from the junkyard that was here before, an old headlight, a lump of metal, a line of pipe amidst the old world feel of the paving stones.

It is here that the Courts have their holdings, each one taking up a corner of the square, the united seasons of Sentinel rock, looming over this place. Between them there are other buildings, empty ones, old shop faces whose signs have long ago faded into illegibility.

The majority of the buildings here are built in the style of old New England homes, with a few taller A frame structures mixed in. Here and there however there are glimpses of 1950s America, and suggestions of the old junkyard in the building materials, all but seamlessly integrated. The roofs however, are noticeably odd, many of them covered in moss and tall grasses, bright green in the Growing Seasons. Just behind closed doors, there are hints of the Dying seasons as well, the dark alleys that suggest hints of Autumn, the odd winter chill when passing by the wrong doorway. It is bright now, but the darkness is never far.

In the center of the square is a shallow pool of grey stone, perfectly square and filled with still water, the bottom gleaming with uncountable coins from many countries, and currencies, a few not even of the mortal realm.
```

### 3. Configure Room Area Information

```
+room/area=New Redoubt
+room/code=HE03
+room/hierarchy=The Square,New Redoubt,Hedge
+room/places=on
```

### 4. Add Places to the Room

```
placeadd The Stone Pool=A shallow pool of grey stone, perfectly square and filled with still water. The bottom gleams with uncountable coins from many countries and currencies, a few not even of the mortal realm. The water is crystal clear and incredibly still, like a mirror reflecting the sky above.

placeadd Summer Court Corner=The northeastern corner of the square belongs to the Summer Court. Bright banners hang from tall poles, and the air here seems warmer, filled with the scent of blooming flowers and fresh grass.

placeadd Winter Court Corner=The northwestern corner is claimed by Winter. Frost often clings to the stonework here despite the season, and shadows seem deeper and more pronounced.
```

### 5. Create Exits

#### Cardinal Direction Exits
```
@open east;e = Green Street
@open south;s = The Commons  
@open west;w = Dead End
```

#### Named Exits (Non-Cardinal)
```
@open Summer Hollow;sum = #123
@open Winter Hollow;win = #124
@open Hedge;h = #125
@open Spring Hollow;spr = #126
@open Autumn Hollow;aut = #127
@open Out;o = #128
```

## Commands Reference

### Room Setup Commands (Builder+)

- `+room` - Display current room settings
- `+room/area=<name>` - Set the IC area name
- `+room/code=<code>` - Set the area code (like HE03)
- `+room/hierarchy=<loc1>,<loc2>,<loc3>` - Set location hierarchy for header
- `+room/places=on/off` - Enable/disable places system

### Places Commands

#### Builder Commands
- `placeadd <name>=<description>` - Add a new place
- `placeadd <number>:<name>=<description>` - Add a place with specific number
- `placelist` - List all places in the room
- `placeremove <number>` - Remove a place
- `roominfo` - Display detailed room information

#### Player Commands
- `plook` - List all available places
- `plook <number>` - Look at a specific place by number
- `plook <name>` - Look at a place by name (partial matching)

### Character Commands

- `shortdesc <description>` - Set your short description (already exists)

## Expected Room Display

When a player types `look`, they'll see something like this:

```
===========================> The Square - New Redoubt - Hedge <===========================


	The Square, the hub and heart of this growing hollow and the place with enough room to host the whole freehold if need be. Cobblestones cover the ground here, smooth and rusted red, almost uniform save for the odd few that remain from the junkyard that was here before, an old headlight, a lump of metal, a line of pipe amidst the old world feel of the paving stones.

	It is here that the Courts have their holdings, each one taking up a corner of the square, the united seasons of Sentinel rock, looming over this place. Between them there are other buildings, empty ones, old shop faces whose signs have long ago faded into illegibility.

	The majority of the buildings here are built in the style of old New England homes, with a few taller A frame structures mixed in. Here and there however there are glimpses of 1950s America, and suggestions of the old junkyard in the building materials, all but seamlessly integrated. The roofs however, are noticeably odd, many of them covered in moss and tall grasses, bright green in the Growing Seasons. Just behind closed doors, there are hints of the Dying seasons as well, the dark alleys that suggest hints of Autumn, the odd winter chill when passing by the wrong doorway. It is bright now, but the darkness is never far.

	In the center of the square is a shallow pool of grey stone, perfectly square and filled with still water, the bottom gleaming with uncountable coins from many countries, and currencies, a few not even of the mortal realm.


            Places are active here. Use plook and plook # to see descriptions.            

----> Characters <---------------------------------------------------------------
Billy                     0s Inkblots, starlight, white hair, black eyes, SM 1
----> Directions <------------------------------------------------------------------------
Green Street <E>               The Commons <S>               Dead End <W>                 
----> Exits <-----------------------------------------------------------------------------
Summer Hollow <SUM>            Winter Hollow <WIN>           Hedge <H>                    
Spring Hollow <SPR>            Autumn Hollow <AUT>           Out <O>                      
====================================================================> IC Area - HE03 <====
```

## Tips and Best Practices

1. **Room Descriptions**: Write paragraphs that flow naturally. The system will format them with proper indentation.

2. **Location Hierarchy**: Use meaningful location names that help players understand where they are in the game world.

3. **Places**: Add detailed places for important features in your room description. This gives players more to explore.

4. **Exits**: Use consistent naming. Cardinal directions get special formatting, while thematic exits (like "Summer Hollow") display separately.

5. **Area Codes**: Use a consistent naming scheme for area codes to help with mapping and navigation.

6. **Special Characters**: Use special character substitutions in any text input:
   - `%r` = newline/carriage return
   - `%r%r` = paragraph break (double newline with spacing)
   - `%t` = tab indentation (5 spaces)

## Special Character Substitutions

The game supports special character substitutions in all text input including:
- Room descriptions
- Place descriptions
- Character poses (pose, :, ;)
- Speech (say, ", ')
- Emotes (@emit)
- Any other text input

### Examples

```
@desc room = This is the first line.%rThis is the second line.%r%rThis starts a new paragraph.%tThis is indented.

:waves to everyone%rand says "Hello there!"%r%r:grins widely.

placeadd The Fountain=A beautiful fountain sits here.%rWater cascades down%tfrom the top tier%tto the bottom pool.
```

### Configuration

Administrators can configure these substitutions in `server/conf/settings.py`:

```python
# Enable/disable special character substitutions
ENABLE_SPECIAL_CHAR_SUBSTITUTIONS = True

# Customize substitutions (processed in order)
SPECIAL_CHAR_SUBSTITUTIONS = {
    '%r%r': '\n\n',  # Paragraph break
    '%r': '\n',      # Newline
    '%t': '     ',   # Tab (5 spaces)
    # Add custom substitutions here
}
```

## Programmatic Room Setup

You can also set up rooms programmatically using the Room methods:

```python
# In a script or command
room = create_object("typeclasses.rooms.Room", key="The Square")
room.set_area_info("New Redoubt", "HE03", ["The Square", "New Redoubt", "Hedge"])
room.set_places_active(True)
room.add_place("The Stone Pool", "A shallow pool of grey stone...")
room.add_place("Summer Court Corner", "The northeastern corner...")
```

## Troubleshooting

- If rooms don't display correctly, ensure they're using the correct typeclass: `typeclasses.rooms.Room`
- If places don't show, check that `+room/places=on` has been set
- If character idle times show "?", the session tracking may need adjustment
- If exits don't categorize correctly, check that cardinal direction exits start with the direction name
- If special character substitutions aren't working, check `ENABLE_SPECIAL_CHAR_SUBSTITUTIONS` in settings.py 