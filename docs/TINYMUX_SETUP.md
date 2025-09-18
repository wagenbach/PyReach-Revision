# TinyMUX Compatibility Layer for Evennia

This guide will help you set up the TinyMUX compatibility layer to make your Evennia game behave more like a traditional TinyMUX server.

## Features

### Core TinyMUX Commands
- `@create` - Create objects with TinyMUX syntax
- `@destroy` - Destroy objects with confirmation
- `@dig` - Create rooms and exits
- `@open` - Create exits between rooms
- `@describe/@desc` - Set object descriptions
- `@set` - Set attributes using TinyMUX syntax
- `&` - Alternative attribute setting syntax
- `@link/@unlink` - Manage exit destinations
- `@teleport/@tel` - Teleport objects
- `@name` - Rename objects with alias support
- `examine/ex` - Detailed object examination
- `@success/@succ` - Set success messages
- `@osuccess/@osucc` - Set osuccess messages
- `@odrop` - Set odrop messages
- `@lock` - Set object locks
- `@find` - Search for objects
- `@stats` - Show database statistics

### Communication Commands
- `@pemit` - Private messaging
- `@emit` - Room-wide messaging
- `;` - Semipose (pose without space)
- `think` - Send private message to yourself with substitutions

### Softcode System
- Basic function parsing: `[time()]`, `[sqrt(5)]`, etc.
- Math functions: `add()`, `sub()`, `mul()`, `div()`, `sqrt()`, `abs()`, `rand()`, `mod()`
- String functions: `left()`, `right()`, `mid()`, `len()`, `cat()`, `ucstr()`, `lcstr()`, `capstr()`
- Database functions: `get()`, `set()`, `name()`, `num()`, `loc()`
- Time functions: `time()`, `secs()`, `convsecs()`
- Utility functions: `if()`, `switch()`, `default()`

### TinyMUX-Style Substitutions
- `%#` - Caller's database reference number
- `%n` - Caller's name
- `%l` - Caller's location name
- `%r` - Carriage return (newline)
- `%t` - Tab character
- `%b` - Space character
- `%0`, `%1`, `%2`, etc. - Command arguments

## Installation

### Step 1: Copy Files
Copy these files to your Evennia game directory:
- `mux_compatibility.py`
- `mux_extra_commands.py`
- `mux_softcode.py`

### Step 2: Add Command Sets

#### Option A: Add to Default Character
Edit your character typeclass (usually `typeclasses/characters.py`):

```python
from evennia.objects.objects import DefaultCharacter
from mux_compatibility import TinyMuxCmdSet
from mux_extra_commands import TinyMuxExtendedCmdSet

class Character(DefaultCharacter):
    def at_object_creation(self):
        """Called when character is first created"""
        super().at_object_creation()
        # Add TinyMUX command sets
        self.cmdset.add(TinyMuxCmdSet, permanent=True)
        self.cmdset.add(TinyMuxExtendedCmdSet, permanent=True)
```

#### Option B: Add to Default Command Set
Edit `commands/default_cmdsets.py`:

```python
from evennia.commands.default import default_cmds
from mux_compatibility import TinyMuxCmdSet
from mux_extra_commands import TinyMuxExtendedCmdSet

class CharacterCmdSet(default_cmds.CharacterCmdSet):
    def at_cmdset_creation(self):
        super().at_cmdset_creation()
        # Add TinyMUX commands - NOTE: Use self.add(), not self.cmdset.add()
        self.add(TinyMuxCmdSet())
        self.add(TinyMuxExtendedCmdSet())
```

**Important:** In a CmdSet class, use `self.add()` directly, not `self.cmdset.add()`!

### Step 3: Reload Server
```bash
evennia reload
```

## Usage Examples

### Building Commands

#### Create a Room with Exits
```
@dig Kitchen=north;n,south;s
```
This creates a "Kitchen" room with a north exit leading to it and a south exit leading back.

#### Create Objects
```
@create apple
@create sword:weapons.WeaponTypeclass
@create box=Kitchen
```

#### Set Descriptions with Formatting
```
@desc here=This is the main hall.%r%rYou can see exits leading %bnorth%b and %bsouth.
```

#### Set Attributes
```
@set apple/color=red
&taste apple=The apple tastes sweet and crisp.
```

### Communication

#### Private Messages
```
@pemit Bob=Hello there! The time is [time()].
```

#### Room Emits
```
@emit The lights flicker ominously.
```

#### Semipose
```
;'s eyes glow red.
```
Result: "YourName's eyes glow red."

#### Think Command (Testing Substitutions)
```
think %#
think Your name is %n and you are in %l
think The time is [time()]
think [add(2,3)]
```
The `think` command is perfect for testing substitutions and softcode functions. It sends the processed message directly to you with no additional text, making it ideal for debugging and experimentation.

### Softcode Examples

#### Math Functions
```
say The square root of 16 is [sqrt(16)].
say Rolling a die: [add(1,[rand(6)])]
```

#### String Manipulation
```
say Your name in caps: [ucstr(%n)]
say First 3 letters: [left(%n,3)]
```

#### Database Functions
```
say Apple's color: [get(apple/color)]
@emit [name(%#)] picks up the [get(apple/color)] apple.
```

#### Conditional Logic
```
say [if([get(me/hungry)],I'm hungry!,I'm not hungry.)]
say [switch([get(me/mood)],happy,I'm happy!,sad,I'm sad.,I feel neutral.)]
```

### Attribute System

The TinyMUX compatibility layer uses Evennia's attribute system but with TinyMUX syntax:

#### Setting Attributes
```
# TinyMUX style
@set object/attribute=value
&attribute object=value

# Examples
@set me/description=A tall person
&health me=100
```

#### Getting Attributes
```
# In softcode
[get(me/health)]
[get(here/long_description)]
```

## Advanced Features

### Exit Aliases
When creating exits, you can specify multiple aliases:
```
@open Red Rabbit Tavern;rrt;tavern;rabbit=Kitchen
```

### Message Attributes
Set custom messages for object interactions:
```
@success apple=You pick up the red apple.
@osuccess apple=picks up the red apple.
@odrop apple=drops a red apple here.
```

### Object Permissions
Use TinyMUX-style locks:
```
@lock box=get:perm(Builder)
@lock room/enter=id(%#)
```

## Troubleshooting

### Commands Not Working
1. Make sure you've added the command sets properly
2. Check that you've reloaded the server: `evennia reload`
3. Verify permissions: many building commands require Builder permission

### Common Installation Errors

#### `'CharacterCmdSet' object has no attribute 'cmdset'`
This means you're using `self.cmdset.add()` in a CmdSet class. Change it to `self.add()`.

#### `ImportError: cannot import name 'TinyMuxCmdSet'`
Make sure the Python files are in your game directory and the imports are correct.

### Softcode Not Parsing
1. Ensure `mux_softcode.py` is in your game directory
2. Check for syntax errors in your softcode functions
3. Make sure you're using the correct bracket syntax: `[function(args)]`

### Attribute Issues
1. Attribute names are automatically lowercased
2. Use the exact TinyMUX syntax: `object/attribute`
3. Check permissions on the object you're trying to modify

## Customization

### Adding New Softcode Functions
Create a new function class in `mux_softcode.py`:

```python
class MyCustomFunction(SoftcodeFunction):
    def __init__(self):
        super().__init__("myfunction", 1, 1)  # name, min_args, max_args
    
    def func(self, caller, args):
        # Your function logic here
        return f"Hello {args[0]}!"

# Register it
SOFTCODE_PARSER.register_function(MyCustomFunction())
```

### Adding New Commands
Follow the pattern in `mux_compatibility.py`:

```python
class CmdMyCommand(TinyMuxCommand):
    key = "@mycommand"
    locks = "cmd:all()"
    help_category = "Custom"
    
    def func(self):
        # Your command logic here
        pass
```

### Modifying Existing Behavior
You can override any of the existing commands by creating a new command with the same key and adding it to a command set with higher priority.

## Converting from Other Systems

### From Standard Evennia
- Replace `@create` with TinyMUX-style `@create`
- Use `@dig` instead of building rooms manually
- Convert attribute access from `obj.db.attr` to `[get(obj/attr)]` in descriptions

### From TinyMUSH/PennMUSH
- Most commands should work similarly
- Some advanced softcode features may need custom implementation
- Check function names as some may differ slightly

## Performance Notes

- The softcode parser has a maximum iteration limit to prevent infinite loops
- Complex nested functions may impact performance
- Consider using native Python for computationally intensive operations

## Compatibility Matrix

| Feature | TinyMUX | This Implementation | Notes |
|---------|---------|-------------------|-------|
| Basic building | ✓ | ✓ | Full compatibility |
| Attribute system | ✓ | ✓ | Uses Evennia's backend |
| Basic softcode | ✓ | ✓ | Core functions implemented |
| Advanced softcode | ✓ | Partial | Extensible framework |
| Locks | ✓ | ✓ | Uses Evennia's lock system |
| Channels | ✓ | - | Use Evennia's channel system |
| Mail | ✓ | - | Use Evennia's mail contrib |

## Support

For issues or questions:
1. Check the troubleshooting section above
2. Review the Evennia documentation for underlying systems
3. Post questions on the Evennia mailing list or Discord

This implementation provides a solid foundation for TinyMUX-style gameplay while leveraging Evennia's modern architecture and extensibility. 