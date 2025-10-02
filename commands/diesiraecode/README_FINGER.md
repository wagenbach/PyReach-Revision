# +finger Command Documentation

## Overview
The `+finger` command displays OOC (Out of Character) information about characters in the game. This information should generally not be considered IC unless game policy specifically states otherwise.

## Usage

### Viewing Finger Information
```
+finger <name>    - Display finger information for a character
+finger me        - Display your own finger information
```

### Setting Finger Attributes
```
+finger/set <attribute>=<value>
```

## Available Attributes

The following attributes can be set using the `/set` switch:

| Attribute | Description |
|-----------|-------------|
| **EMAIL** | Your email address (can be set to "unlisted") |
| **POSITION** | Your character's position or role |
| **AGE** | Your character's real age |
| **FAME** | What your character is known for |
| **APP-AGE** | Your character's apparent age |
| **PLAN** | Any plans your character may have |
| **RP-PREFS** | Your RP preferences as a player |
| **THEMESONG** | A theme song for your character |
| **QUOTE** | A typical quote from your character |
| **OFF-HOURS** | When you are usually online |
| **TEMPERAMENT** | Your character's temperament |
| **VACATION** | Dates you expect to be gone |
| **URL** | Your homepage or character wiki, if any |

Note: The **ALTS** field is automatically populated from the `+alts` command system.

## Examples

### Setting Attributes
```
+finger/set fame=Princess Angelina Contessa Louisa Francesca Banana Fanna Bobesca the Third
+finger/set email=myemail@example.com
+finger/set rp-prefs=Whatever goes!
+finger/set email=unlisted
+finger/set themesong=Bohemian Rhapsody - Queen
+finger/set off-hours=Evenings EST, weekends
```

### Viewing Finger Information
```
+finger Melvin
+finger me
```

## Display Format

The finger display shows:
- Character name (in header)
- Alias (if set)
- Sex/Gender
- Email address
- Online status (time connected and idle time)
- Mail status (unread/total messages)
- Current location
- RP preferences
- Any other attributes that have been set
- Public alts (from +alts system)

Example output:
```
<---======##======================[ Melvin ]======================##======--->
Alias: Mel                             |On for: 2m          Idle: 0s          
Sex: None Set                          |Mail: 3 unread / 0 total.            
E-Mail: (unlisted)                     |                                      
<-------------=============++++++++++++++++++++++++=============------------->
Location:       Kingwood - Lastra Farm - Main Room      
RP-Prefs:       Whatever goes!        
<-------------=============++++++++++++++++++++++++=============------------->
```

## Integration

The `+finger` command integrates with:
- **+alts** system: Automatically displays public alts
- **alias** system: Shows character aliases
- **@mail** system: Displays mail counts
- Session system: Shows online time and idle time

## Technical Notes

- All finger data is stored in the character's `finger_data` attribute
- The email field can be set to "(unlisted)" by using `+finger/set email=unlisted`
- All attribute names are case-insensitive when setting
- The command is available to all players (lock: `cmd:all()`)
- The display automatically handles online/offline status

## Command Class
- **Location**: `PyReach/commands/diesiraecode/CmdFinger.py`
- **Base Class**: `MuxCommand`
- **Key**: `+finger`
- **Aliases**: `finger`
- **Help Category**: Character

