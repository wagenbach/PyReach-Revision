# Demon Demonic Form Traits

This document describes the Demonic Form trait system for Demon: The Descent characters.

## Character Creation Allocation

At character creation, a demon receives:
- **3 Modifications**
- **2 Technologies**
- **1 Propulsion**
- **1 Process**

## Trait Categories

### Modifications (One-Time Picks)
Modifications are permanent alterations to the demon's form. They are always active and do not require activation. Once chosen, they remain part of the demon's demonic form.

**Total Available**: 44 modifications

**Examples**:
- **Advanced Optics**: +3 bonus to magnification-based rolls
- **Armored Plates**: Armor 3/2, Defense/Speed -1
- **Inhuman Strength**: +2 to Strength rolls
- **Night Vision**: See in darkness, +2 Perception
- **Steel Frame**: Bones cannot be broken, ignore wound penalties

### Technologies (Must Be Activated)
Technologies must be consciously activated when used. Many require spending Aether or taking specific actions.

**Total Available**: 35 technologies

**Examples**:
- **Acidic Spit**: Spit acid attack with 0A weapon rating
- **Aura Sight**: Read body language and supernatural qualities
- **Electric Jolt**: Power or disable devices, spend Aether for armor
- **Mind Reading**: Read surface thoughts with Primum roll
- **Savant Core**: Contains a 5-dot Skill that can be accessed

### Propulsions (One-Time Picks or Activated)
Propulsions govern how the demon moves. Some are passive, others require activation.

**Total Available**: 11 propulsions

**Examples**:
- **Aquatic**: Swim with species factor 10, spend Aether to become liquid
- **Long Limbs**: +2 Athletics, +5 Speed (passive)
- **Plasma Drive**: No Defense penalties, apply Defense vs ranged
- **Teleportation**: Spend Aether to teleport within line of sight
- **Wings**: Fly with species factor 10 added to Speed

### Processes (Must Be Activated)
Processes are complex abilities that must be activated, often requiring Aether expenditure.

**Total Available**: 27 processes

**Examples**:
- **Aegis Protocol**: Summon shield, +2 Defense
- **Amorphous**: Spend Aether to swap form abilities
- **Body Modification**: Reallocate Physical Attributes
- **Extra Mechanical Limbs**: Extra limbs, +3 to Strength rolls
- **Wound Healing**: Heal 1B or 1L per turn

## Data Structure

All demon form traits are stored in `PyReach/world/cofd/templates/demon_form.py` with the following format:

```python
{
    "trait_key": {
        "name": "Trait Name",
        "appearance": "Description of physical appearance",
        "system": "Mechanical effects and rules",
        "source": "Book abbreviation and page number"
    }
}
```

## Source Books

Traits are sourced from the following books:
- **DTD**: Demon: The Descent core rulebook
- **FoH**: Flowers of Hell
- **DTG**: Demon Translation Guide
- **DTF**: Demon: The Fallen (conversions)
- **DPG**: Demon Player's Guide
- **Iface**: Interface

## Lookup System Integration

The demon form traits are integrated into the lookup system and can be searched using:

```python
from world.cofd.lookup_data import LOOKUP_DATA

# Search for specific traits
results = LOOKUP_DATA.search_stats("inhuman")

# Access demon data directly
modifications = LOOKUP_DATA.demon_data['modifications']
technologies = LOOKUP_DATA.demon_data['technologies']
propulsions = LOOKUP_DATA.demon_data['propulsions']
processes = LOOKUP_DATA.demon_data['processes']
```

## Search Results

When searching, demon form traits return with the following type identifiers:
- `demon_modification` - For Modifications
- `demon_technology` - For Technologies
- `demon_propulsion` - For Propulsions
- `demon_process` - For Processes

## Usage in Commands

The demon form traits can be looked up using the standard lookup commands:

```
+lookup demon_modification Advanced Optics
+lookup demon_technology Mind Reading
+lookup demon_propulsion Wings
+lookup demon_process Body Modification
```

## Implementation Notes

1. **Semantic Nature**: Demonic form traits are semantic and chosen from the predefined lists above. Players select specific traits by name.

2. **Activation**: 
   - Modifications and some Propulsions are always active (one-time picks)
   - Technologies and Processes must be activated when used

3. **Aether Costs**: Many Technologies and Processes require Aether expenditure to activate or enhance their effects.

4. **Appearance**: Each trait includes a physical appearance description that should be reflected in the demon's demonic form description.

5. **Stacking**: Check individual trait systems for whether effects stack with other abilities.

## Future Enhancements

Potential future additions to this system:
- Character sheet integration to track selected demonic form traits
- Commands to set and display demonic form configuration
- Validation to ensure proper allocation (3/2/1/1)
- Integration with demonic form transformation mechanics
- Tracking of which traits are currently active vs. available

