# Equipment Purchasing System Documentation

## Overview

The Equipment Purchasing System allows characters to buy weapons, armor, and other equipment using their Resources merit and other qualifying merits. The system is highly configurable and can be adapted to different game styles and economies.

## System Architecture

### Core Files
- **`world/equipment_database.py`** - Contains all weapon and armor data
- **`world/equipment_purchasing.py`** - Contains purchasing logic and configuration
- **`commands/equipment.py`** - Contains player commands (`+buy`, `+buyconfig`)

## Resource Modes

The system supports two different resource spending modes:

### Pool Mode (Default)
- Characters gain resource points equal to their Resources merit each refresh period
- Points are spent to purchase items (Item Availability = Cost in points)
- Players can save up points for expensive items (if enabled)
- Example: Resources 3 character gets 3 points per month, can save to buy Availability 5 item

### Absolute Mode
- Resources merit rating determines maximum item availability
- Can purchase any item with Availability ≤ Resources rating
- Purchase frequency is limited by staff-configured limits
- Example: Resources 4 character can buy any Availability 4 or lower item

## Staff Configuration Commands

All configuration is done in-game using the `+buyconfig` command (requires Builder+ permissions):

### Basic Configuration
```
+buyconfig/mode <pool|absolute>     # Set resource spending mode
+buyconfig/period <days>            # Set refresh period (default: 30 days)
+buyconfig/maxpurchases <number>    # Set max purchases per period (or "unlimited")
+buyconfig/saving <on|off>          # Allow saving resource points (pool mode only)
+buyconfig/script <start|stop|status> # Manage automatic refresh script
+buyconfig/status                   # View current configuration
+buyconfig/reset                    # Reset to default settings
```

### Merit Bonus Configuration
```
+buyconfig/bonus <merit_name> <bonus_per_dot>    # Set merit resource bonus
+buyconfig/remove <merit_name>                   # Remove merit resource bonus
```

### Example Configurations

**Conservative Monthly Economy:**
```
+buyconfig/mode pool
+buyconfig/period 30
+buyconfig/maxpurchases 3
+buyconfig/saving on
```

**Liberal Weekly Economy:**
```
+buyconfig/mode absolute
+buyconfig/period 7
+buyconfig/maxpurchases unlimited
```

**High-Resource Game:**
```
+buyconfig/bonus fame 2
+buyconfig/bonus mentor 1
+buyconfig/bonus contacts 1
```

## Modifying Merit Bonuses

### Adding New Merit Bonuses

To add new merits that provide resource bonuses, you have two options:

#### Option 1: In-Game Configuration (Recommended)
Use the `+buyconfig/bonus` command:
```
+buyconfig/bonus <merit_name> <bonus_per_dot>
```

Examples:
```
+buyconfig/bonus fame 2           # Fame merit gives +2 resources per dot
+buyconfig/bonus mentor 1         # Mentor merit gives +1 resource per dot
+buyconfig/bonus safe_place 0.5   # Safe Place gives +0.5 per dot (rounded down)
+buyconfig/bonus retainer 1       # Retainer merit gives +1 per dot
+buyconfig/remove fame            # Remove fame merit bonus entirely
```

#### Option 2: Code Modification
Edit `world/equipment_purchasing.py` and modify the `EquipmentPurchasingConfig` class:

```python
class EquipmentPurchasingConfig:
    def __init__(self):
        # ... other settings ...
        self.bonus_merits = {
            "contacts": 1,      # +1 resource per dot
            "allies": 1,        # +1 resource per dot  
            "status": 0.5,      # +0.5 resource per dot (rounded down)
            "fame": 2,          # +2 resources per dot
            "mentor": 1,        # +1 resource per dot
            "retainer": 1,      # +1 resource per dot
            "safe_place": 0.5,  # +0.5 resource per dot
            # Add more merits here...
        }
```

### Removing Merit Bonuses

#### In-Game Removal (Recommended):
```
+buyconfig/remove <merit_name>     # Completely remove the merit bonus
```

#### Alternative Method:
```
+buyconfig/bonus <merit_name> 0    # Set bonus to 0 to effectively disable it
```

#### Code Removal:
Remove the merit from the `bonus_merits` dictionary in `EquipmentPurchasingConfig.__init__()`.

### Merit Bonus Calculation

The system calculates total resources as:
```
Total Resources = Base Resources Merit + Sum of (Merit Dots × Bonus Per Dot)
```

Example:
- Resources 2
- Contacts 3 (+1 per dot) = +3
- Fame 1 (+2 per dot) = +2
- **Total: 2 + 3 + 2 = 7 resource points per period**

## Advanced Configuration

### Custom Refresh Periods

You can set any refresh period in days:
```
+buyconfig/period 1     # Daily refresh
+buyconfig/period 7     # Weekly refresh  
+buyconfig/period 14    # Bi-weekly refresh
+buyconfig/period 30    # Monthly refresh (default)
+buyconfig/period 90    # Quarterly refresh
```

### Purchase Limits

Control how often players can make purchases:
```
+buyconfig/maxpurchases 1          # One purchase per period
+buyconfig/maxpurchases 5          # Five purchases per period
+buyconfig/maxpurchases unlimited  # No purchase limits
```

### Resource Point Saving

In pool mode, control whether players can save points:
```
+buyconfig/saving on    # Players can save up to 2x their merit rating
+buyconfig/saving off   # Points reset to merit rating each period
```

## Player Commands

### Purchasing Equipment
```
+buy <item_name>           # Purchase an item directly
+buy/list                  # List all available equipment
+buy/list weapons          # List only weapons
+buy/list armor            # List only armor
+buy/info <item_name>      # Get detailed item information
+buy/status                # Check resource status and refresh dates
+buy/help                  # Show purchasing help
```

### Managing Equipment
```
+equipment/list            # List owned equipment
+equipment/wield <weapon>  # Wield a weapon for combat
+equipment/wear <armor>    # Wear armor for protection
+equipment/view <item>     # View item details
```

## Integration with Other Systems

### Combat System Integration
- Purchased weapons automatically work with `+combat` commands
- Weapon tags and special properties are fully supported
- Equipment integrates seamlessly with grappling and special attacks

### Character Sheet Integration
- Reads Resources merit directly from character sheets
- Supports all merit types for bonus calculations
- Integrates with existing `+equipment` inventory system

### Tilt System Integration
- Weapons with special tags (incendiary, stun, etc.) automatically apply tilts
- Integrates with existing `+tilt` command system

## Troubleshooting

### Common Issues

**"You need the Resources merit to purchase equipment"**
- Character needs at least 1 dot in Resources merit
- Use `+stat resources=1` to add the merit

**"Insufficient resources"**
- Check `+buy/status` to see current resource pool
- Wait for next refresh period or use absolute mode

**"You already have this equipment"**
- Character already owns the item
- Use `+equipment/list` to see owned equipment

**"Unknown item"**
- Item name might be misspelled
- Use `+buy/list` to see available items
- Try using underscores instead of spaces (e.g., "assault_rifle")

### Debug Commands

For staff troubleshooting:
```
+buyconfig/status          # Check current system configuration
+buy/status <character>    # Check specific character's resource status (if implemented)
```

## Example Game Configurations

### Street-Level Game (Low Resources)
```
+buyconfig/mode pool
+buyconfig/period 30
+buyconfig/maxpurchases 2
+buyconfig/saving on
+buyconfig/bonus contacts 0.5
+buyconfig/bonus allies 0.5
```

### High-Action Game (Abundant Resources)
```
+buyconfig/mode absolute
+buyconfig/period 7
+buyconfig/maxpurchases unlimited
+buyconfig/bonus fame 3
+buyconfig/bonus status 2
+buyconfig/bonus mentor 2
```

### Survival Horror Game (Scarce Resources)
```
+buyconfig/mode pool
+buyconfig/period 60
+buyconfig/maxpurchases 1
+buyconfig/saving off
# No merit bonuses - only base Resources merit counts
```

## Developer Notes

### Adding New Equipment

To add new weapons or armor to the database:

1. Edit `world/equipment_database.py`
2. Add new entries to `WEAPON_DATABASE` or `ARMOR_DATABASE`
3. Use the `WeaponData` or `ArmorData` classes with proper parameters

Example:
```python
"custom_sword": WeaponData("Custom Sword", damage=4, initiative_mod=-3, weapon_type="melee",
                          size=3, strength_req=3, availability=4, tags="9-again, accurate"),
```

### Modifying Resource Calculation

The resource calculation logic is in `EquipmentPurchasingConfig.get_resource_limit()`. You can modify this method to implement custom resource calculation rules.

### Adding New Merit Types

Merit bonuses are stored in the `bonus_merits` dictionary. The key is the merit name (lowercase), and the value is the bonus per dot. Fractional bonuses are supported and will be rounded down.

## Security Considerations

- Only Builder+ staff can modify purchasing configuration
- Resource pools are stored per-character and cannot be directly modified by players
- Purchase history is tracked to prevent abuse
- All purchases are logged and can be audited

## Automatic Resource Refresh Script

The system includes an automatic server script that refreshes character resource pools without requiring manual intervention.

### Script Management
```
+buyconfig/script start     # Start the automatic refresh script
+buyconfig/script stop      # Stop the automatic refresh script  
+buyconfig/script restart   # Restart the script (useful after config changes)
+buyconfig/script status    # Check if script is running
```

### How It Works
- **Runs every hour** to check all characters
- **Checks individual refresh periods** for each character
- **Only refreshes** characters whose period has elapsed
- **Notifies online players** when their resources refresh
- **Survives server restarts** (persistent script)
- **Error handling** prevents one character's issues from affecting others

### Setting Up the Script
1. Configure your desired settings with `+buyconfig` commands
2. Start the script: `+buyconfig/script start`
3. Verify it's running: `+buyconfig/script status`

### Script Benefits
- **Automatic operation** - no manual refresh needed
- **Individual timing** - each character refreshes on their own schedule
- **Online notifications** - players are informed when resources refresh
- **Robust error handling** - continues working even if individual characters have issues

## Future Enhancements

Potential future additions to the system:
- Bulk purchasing discounts
- Seasonal availability changes
- Merit-specific equipment access
- Equipment degradation and replacement
- Black market purchasing with different rules
- Equipment trading between characters
