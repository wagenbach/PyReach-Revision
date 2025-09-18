# Equipment and Combat Integration - Chronicles of Darkness: Hurt Locker

## Overview

Fully integrated equipment and combat systems based on the official **Hurt Locker** supplement and core CoD material. Characters must actually own, wield, and wear their combat gear. All of this gear has mechanics pulled from the literature.

## Equipment Types

### Weapons (Hurt Locker Database)
All weapons are based on the official Hurt Locker supplement with accurate game statistics.

**Available Categories:**
- **Melee - Bladed**: battle_axe, fire_axe, great_sword, hatchet, knife_small, knife_hunting, machete, rapier, sword
- **Melee - Blunt**: brass_knuckles, metal_club, nightstick, nunchaku, sap, sledgehammer
- **Melee - Exotic**: catchpole, chain, chainsaw, kusari_gama, shield (small/large), stake, stun_gun_melee, tiger_claws, whip
- **Melee - Improvised**: blowtorch, board_with_nail, improvised_shield, nail_gun, shovel, tire_iron
- **Melee - Polearms**: spear, staff
- **Ranged - Archery**: short_bow, long_bow, crossbow
- **Ranged - Thrown**: throwing_knife
- **Ranged - Firearms**: light_pistol, heavy_pistol, light_revolver, heavy_revolver, smg_small, smg_heavy, rifle, big_game_rifle, assault_rifle, shotgun
- **Ranged - Nonlethal**: pepper_spray, stun_gun_ranged
- **Explosives**: Various grenades, molotov_cocktail, pipe_bomb, grenade launchers
- **Heavy Weapons**: flamethrower_civilian, flamethrower_military

**Weapon Properties:**
- **Damage**: Added to attack successes
- **Initiative**: Modifier to Initiative when wielding
- **Strength**: Minimum Strength requirement  
- **Size**: Weapon size rating (affects concealment)
- **Range**: Effective range category
- **Tags**: Special weapon properties (9-again, stun, etc.)
- **Capacity**: Ammunition/usage capacity
- **Availability**: Resource cost (0-5 dots)

### Armor (Hurt Locker Database)
Protective gear with authentic Chronicles of Darkness mechanics.

**Available Types:**
- **Modern**: reinforced_clothing, sports_gear, kevlar_vest, flak_jacket, full_riot_gear, bomb_suit, helmet_modern
- **Archaic**: leather_hard, lorica_segmentata, chainmail, plate_mail, helmet_archaic

**Armor Properties:**
- **General Armor**: Reduces total damage taken
- **Ballistic Armor**: Downgrades lethal firearm damage to bashing  
- **Strength**: Minimum Strength requirement
- **Defense**: Defense penalty while wearing
- **Speed**: Speed penalty while wearing
- **Coverage**: Body areas protected
- **Availability**: Resource cost (0-5 dots)

## Chronicles of Darkness Mechanics

### Damage Types
- **Bashing**: Blunt trauma (clubs, fists, falling)
- **Lethal**: Cuts, bullets, burns (blades, firearms)  
- **Aggravated**: Supernatural or extreme damage (fire, acid, supernatural claws)

### Armor Mechanics (Official Rules)
1. **Ballistic Armor**: Each point downgrades 1 lethal damage from firearms to bashing
2. **General Armor**: Each point reduces total damage by 1
3. **Application Order**: Apply ballistic first, then general armor
4. **Minimum Damage**: Successful attacks always do at least 1 bashing to mortals
5. **Coverage**: Armor only protects covered body areas

### Weapon Tags (Hurt Locker)
- **9-again**: Re-roll 9s and 10s on attack rolls
- **Accurate**: +1 to attack rolls
- **Armor Piercing**: Reduces target's armor rating
- **Blast**: Area of effect damage
- **Concealed**: Harder to detect when carried
- **Grapple**: Bonus to grappling attempts
- **Inaccurate**: -1 penalty to attack rolls
- **Knockdown**: Enhanced knockdown effects
- **Reach**: +1 Defense vs shorter weapons
- **Stun**: Enhanced stunning effects
- **Two-handed**: Requires both hands to use effectively

## Equipment Commands

### Managing Gear
- `+equipment/list` - Show all your equipment with combat stats
- `+equipment/add <name> weapon` - Add a weapon from Hurt Locker database
- `+equipment/add <name> armor` - Add armor from Hurt Locker database
- `+equipment/remove <name>` - Remove equipment
- `+equipment/view <name>` - View detailed Hurt Locker stats

### Equipping Gear
- `+equipment/wield <weapon>` - Wield weapon (affects Initiative)
- `+equipment/unwield` - Stop wielding weapon
- `+equipment/wear <armor>` - Wear armor (applies penalties/bonuses)
- `+equipment/unwear` - Remove armor

### Information
- `+equipment/weapons` - Browse Hurt Locker weapon database
- `+equipment/armor` - Browse Hurt Locker armor database  
- `+gear [target]` - Show currently equipped gear with stats

## Combat Integration

### Weapon Usage
- **Unarmed**: No weapon = unarmed combat (0 damage, bashing)
- **Wielded Weapons**: Use exact Hurt Locker statistics
- **Initiative Modifier**: Weapon initiative affects your Initiative score
- **Strength Requirements**: Inadequate Strength imposes penalties
- **Weapon Tags**: Special properties automatically applied

### Armor Protection  
- **Automatic Protection**: Worn armor protects according to coverage
- **Ballistic vs General**: Proper Chronicles of Darkness mechanics
- **Stat Penalties**: Defense and Speed penalties applied while worn
- **Strength Requirements**: Inadequate Strength causes additional penalties

### Attack Pool Calculation (Official Rules)
- **Unarmed**: Strength + Brawl
- **Melee Weapons**: Strength + Weaponry
- **Ranged/Thrown**: Dexterity + Athletics  
- **Firearms**: Dexterity + Firearms
- **Special Cases**: Some weapons use different combinations

### Damage Resolution (Chronicles of Darkness)
1. Roll attack pool vs target's Defense
2. Count successes, add weapon damage
3. Apply ballistic armor (firearms only)
4. Apply general armor  
5. Minimum 1 bashing damage for successful attacks
6. Apply final damage to health track

## Character Setup Examples

### Street Fighter
```
+equipment/add brass_knuckles weapon
+equipment/add reinforced_clothing armor  
+equipment/wield brass_knuckles
+equipment/wear reinforced_clothing
```

### Police Officer
```
+equipment/add heavy_pistol weapon
+equipment/add kevlar_vest armor
+equipment/add nightstick weapon
+equipment/wield heavy_pistol
+equipment/wear kevlar_vest
```

### Medieval Knight
```
+equipment/add sword weapon
+equipment/add plate_mail armor
+equipment/add shield_large weapon
+equipment/wield sword
+equipment/wear plate_mail
```

### Tactical Operative
```
+equipment/add assault_rifle weapon
+equipment/add full_riot_gear armor
+equipment/wield assault_rifle  
+equipment/wear full_riot_gear
```

## Tactical Considerations

### Weapon Selection
- **Damage vs Initiative**: High damage weapons often have Initiative penalties
- **Strength Requirements**: Ensure adequate Strength for your weapons
- **Range Categories**: Choose appropriate weapons for expected engagement distances
- **Tags**: Leverage special weapon properties for tactical advantage

### Armor Strategy
- **Protection vs Mobility**: Heavy armor protects but imposes penalties
- **Coverage Areas**: Consider what body parts need protection
- **Ballistic vs General**: Different armor types for different threats  
- **Environmental Factors**: Some armor has situational bonuses/penalties

### Equipment Economics
- **Availability Ratings**: Higher ratings require more Resources or contacts
- **Concealment**: Larger weapons/armor harder to hide
- **Maintenance**: Equipment can be damaged or lost
- **Situational Gear**: Different equipment for different scenarios

## Advanced Features

### Tag System Implementation
- **Automatic Application**: Weapon tags automatically affect combat
- **Stacking Effects**: Multiple tags can combine for enhanced effects
- **Conditional Bonuses**: Some tags only apply in specific situations

### Armor Coverage System
- **Called Shots**: Target unarmored locations to bypass protection
- **Partial Coverage**: Different armor protects different body areas
- **Layered Protection**: Helmets can extend body armor to head

### Realistic Equipment Handling
- **Two-Handed Weapons**: Cannot use shield or other equipment simultaneously
- **Size Restrictions**: Large weapons affect movement and concealment
- **Capacity Management**: Track ammunition and equipment condition

## Future Enhancements

### Planned Features
- **Equipment Condition**: Durability and maintenance systems
- **Ammunition Tracking**: Detailed ammo management for firearms
- **Equipment Modifications**: Attachments and customizations
- **Advanced Tags**: Implementation of all Hurt Locker weapon tags
- **Environmental Interactions**: Weather and terrain effects on equipment

### Advanced Combat Systems
- **Cover Mechanics**: Equipment interactions with environmental cover
- **Autofire Rules**: Burst fire and suppression mechanics
- **Explosive Damage**: Blast radius and force calculations
- **Equipment-based Maneuvers**: Special actions based on gear