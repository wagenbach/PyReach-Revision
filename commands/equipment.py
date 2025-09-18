from evennia.commands.default.muxcommand import MuxCommand
from evennia.utils import create


# Weapon and Armor Data
# Chronicles of Darkness Weapons Database
# Extracted from Hurt Locker supplement

WEAPON_DATA = {
    # MELEE WEAPONS - BLADED
    "battle_axe": {"damage": 3, "initiative": -4, "strength": 3, "size": 3, "tags": "9-again, two-handed", "range": "melee", "availability": 3},
    "fire_axe": {"damage": 2, "initiative": -4, "strength": 3, "size": 3, "tags": "9-again, two-handed", "range": "melee", "availability": 2},
    "great_sword": {"damage": 4, "initiative": -5, "strength": 4, "size": 3, "tags": "9-again, two-handed", "range": "melee", "availability": 4},
    "hatchet": {"damage": 1, "initiative": -2, "strength": 1, "size": 1, "tags": "", "range": "melee", "availability": 2},
    "knife_small": {"damage": 0, "initiative": 0, "strength": 1, "size": 1, "tags": "thrown", "range": "melee", "availability": 1},
    "knife_hunting": {"damage": 1, "initiative": -1, "strength": 1, "size": 2, "tags": "enhance_crafts_survival", "range": "melee", "availability": 2},
    "machete": {"damage": 2, "initiative": -2, "strength": 2, "size": 2, "tags": "", "range": "melee", "availability": 2},
    "rapier": {"damage": 1, "initiative": -2, "strength": 1, "size": 2, "tags": "piercing_1", "range": "melee", "availability": 2},
    "sword": {"damage": 3, "initiative": -3, "strength": 2, "size": 3, "tags": "initiative_bonus_1", "range": "melee", "availability": 3},

    # MELEE WEAPONS - BLUNT
    "brass_knuckles": {"damage": 0, "initiative": 0, "strength": 1, "size": 1, "tags": "brawl", "range": "melee", "availability": 1},
    "metal_club": {"damage": 2, "initiative": -2, "strength": 2, "size": 2, "tags": "stun", "range": "melee", "availability": 1},
    "nightstick": {"damage": 1, "initiative": -1, "strength": 2, "size": 2, "tags": "stun", "range": "melee", "availability": 2},
    "nunchaku": {"damage": 1, "initiative": 1, "strength": 2, "size": 2, "tags": "stun, dexterity_requirement", "range": "melee", "availability": 2},
    "sap": {"damage": 0, "initiative": -1, "strength": 2, "size": 2, "tags": "stun", "range": "melee", "availability": 1},
    "sledgehammer": {"damage": 3, "initiative": -4, "strength": 3, "size": 3, "tags": "knockdown, stun", "range": "melee", "availability": 1},

    # MELEE WEAPONS - EXOTIC
    "catchpole": {"damage": 0, "initiative": -3, "strength": 2, "size": 2, "tags": "grapple, reach", "range": "melee", "availability": 1},
    "chain": {"damage": 1, "initiative": -3, "strength": 2, "size": 2, "tags": "grapple, inaccurate, reach", "range": "melee", "availability": 1},
    "chainsaw": {"damage": 3, "initiative": -6, "strength": 4, "size": 3, "tags": "bleed, inaccurate, two-handed", "range": "melee", "availability": 3},
    "kusari_gama_chain": {"damage": 1, "initiative": -3, "strength": 2, "size": 2, "tags": "grapple, inaccurate, reach", "range": "melee", "availability": 1},
    "kusari_gama_sickle": {"damage": 1, "initiative": -1, "strength": 1, "size": 2, "tags": "", "range": "melee", "availability": 2},
    "shield_small": {"damage": 0, "initiative": -2, "strength": 2, "size": 2, "tags": "concealed", "range": "melee", "availability": 2},
    "shield_large": {"damage": 2, "initiative": -4, "strength": 3, "size": 3, "tags": "concealed", "range": "melee", "availability": 2},
    "stake": {"damage": 0, "initiative": -4, "strength": 1, "size": 1, "tags": "", "range": "melee", "availability": 0},
    "stun_gun_melee": {"damage": 0, "initiative": -1, "strength": 1, "size": 1, "tags": "stun, no_bonus_damage", "range": "melee", "availability": 1},
    "tiger_claws": {"damage": 1, "initiative": -1, "strength": 2, "size": 2, "tags": "brawl", "range": "melee", "availability": 2},
    "whip": {"damage": 0, "initiative": -2, "strength": 1, "size": 2, "tags": "grapple, stun, dexterity_weaponry", "range": "melee", "availability": 1},

    # MELEE WEAPONS - IMPROVISED
    "blowtorch": {"damage": 0, "initiative": -2, "strength": 2, "size": 2, "tags": "incendiary, piercing_2, blinded_tilt", "range": "melee", "availability": 2},
    "board_with_nail": {"damage": 1, "initiative": -3, "strength": 2, "size": 2, "tags": "fragile, stun", "range": "melee", "availability": 0},
    "improvised_shield": {"damage": 0, "initiative": -4, "strength": 2, "size": 2, "tags": "concealed", "range": "melee", "availability": 1},
    "nail_gun": {"damage": 0, "initiative": -2, "strength": 2, "size": 2, "tags": "inaccurate, piercing_1, strength_firearms", "range": "melee", "availability": 1},
    "shovel": {"damage": 1, "initiative": -3, "strength": 2, "size": 2, "tags": "knockdown", "range": "melee", "availability": 1},
    "tire_iron": {"damage": 1, "initiative": -3, "strength": 2, "size": 2, "tags": "guard, inaccurate", "range": "melee", "availability": 2},

    # MELEE WEAPONS - POLEARMS
    "spear": {"damage": 2, "initiative": -2, "strength": 2, "size": 4, "tags": "reach, two-handed", "range": "melee", "availability": 1},
    "staff": {"damage": 1, "initiative": -1, "strength": 2, "size": 4, "tags": "knockdown, reach, two-handed", "range": "melee", "availability": 1},

    # RANGED WEAPONS - ARCHERY
    "short_bow": {"damage": 2, "range": "medium", "capacity": "low", "initiative": -3, "strength": 2, "size": 3, "availability": 2, "tags": ""},
    "long_bow": {"damage": 3, "range": "medium", "capacity": "low", "initiative": -4, "strength": 3, "size": 4, "availability": 2, "tags": ""},
    "crossbow": {"damage": 2, "range": "long", "capacity": "low", "initiative": -5, "strength": 3, "size": 3, "availability": 3, "tags": ""},

    # RANGED WEAPONS - THROWN
    "throwing_knife": {"damage": 0, "range": "close", "capacity": "single", "initiative": 0, "strength": 1, "size": 1, "availability": 1, "tags": "thrown"},

    # RANGED WEAPONS - FIREARMS
    "light_pistol": {"damage": 1, "range": "long", "capacity": "medium", "initiative": 0, "strength": 2, "size": 1, "availability": 2, "tags": ""},
    "heavy_pistol": {"damage": 2, "range": "long", "capacity": "medium", "initiative": -2, "strength": 3, "size": 1, "availability": 3, "tags": ""},
    "light_revolver": {"damage": 1, "range": "long", "capacity": "low", "initiative": 0, "strength": 2, "size": 2, "availability": 2, "tags": ""},
    "heavy_revolver": {"damage": 2, "range": "long", "capacity": "low", "initiative": -2, "strength": 3, "size": 3, "availability": 2, "tags": ""},
    "smg_small": {"damage": 1, "range": "medium", "capacity": "high", "initiative": -2, "strength": 2, "size": 1, "availability": 3, "tags": ""},
    "smg_heavy": {"damage": 2, "range": "medium", "capacity": "high", "initiative": -3, "strength": 3, "size": 2, "availability": 3, "tags": ""},
    "rifle": {"damage": 4, "range": "extreme", "capacity": "low", "initiative": -5, "strength": 2, "size": 3, "availability": 2, "tags": ""},
    "big_game_rifle": {"damage": 5, "range": "extreme", "capacity": "low", "initiative": -5, "strength": 3, "size": 4, "availability": 5, "tags": "stun"},
    "assault_rifle": {"damage": 3, "range": "long", "capacity": "high", "initiative": -3, "strength": 3, "size": 3, "availability": 3, "tags": "9-again"},
    "shotgun": {"damage": 3, "range": "medium", "capacity": "low", "initiative": -4, "strength": 3, "size": 2, "availability": 2, "tags": "9-again"},

    # RANGED WEAPONS - NONLETHAL
    "pepper_spray": {"damage": 0, "range": "close", "capacity": "low", "initiative": 0, "strength": 1, "size": 1, "availability": 1, "tags": "slow"},
    "stun_gun_ranged": {"damage": 0, "range": "close", "capacity": "medium", "initiative": -1, "strength": 1, "size": 1, "availability": 1, "tags": "slow, stun, no_bonus_damage"},

    # EXPLOSIVES - GRENADES
    "frag_grenade_standard": {"damage": 2, "range": "thrown", "capacity": "single", "initiative": 0, "strength": 2, "size": 1, "availability": 4, "tags": "knockdown, stun, blast_10, force_3"},
    "frag_grenade_heavy": {"damage": 3, "range": "thrown", "capacity": "single", "initiative": -1, "strength": 2, "size": 1, "availability": 4, "tags": "knockdown, stun, blast_5, force_4"},
    "molotov_cocktail": {"damage": 1, "range": "thrown", "capacity": "single", "initiative": -2, "strength": 2, "size": 2, "availability": 1, "tags": "incendiary, blast_3, force_2"},
    "pipe_bomb": {"damage": 1, "range": "thrown", "capacity": "single", "initiative": -1, "strength": 2, "size": 1, "availability": 1, "tags": "inaccurate, stun, blast_5, force_2"},
    "smoke_grenade": {"damage": 0, "range": "thrown", "capacity": "single", "initiative": 0, "strength": 2, "size": 1, "availability": 2, "tags": "concealment, blast_10"},
    "stun_grenade": {"damage": 0, "range": "thrown", "capacity": "single", "initiative": 0, "strength": 2, "size": 1, "availability": 2, "tags": "knockdown, stun, blast_5, force_2"},
    "thermite_grenade": {"damage": 3, "range": "thrown", "capacity": "single", "initiative": 0, "strength": 2, "size": 1, "availability": 4, "tags": "ap_8, incendiary, blast_5, force_4"},
    "white_phosphorous": {"damage": 3, "range": "thrown", "capacity": "single", "initiative": 0, "strength": 2, "size": 1, "availability": 4, "tags": "ap_3, incendiary, concealment, blast_5, force_4"},

    # EXPLOSIVES - GRENADE LAUNCHERS
    "grenade_launcher_standalone": {"damage": "varies", "range": "long", "capacity": "low", "initiative": -5, "strength": 3, "size": 3, "availability": 4, "tags": "heavy_recoil"},
    "grenade_launcher_underbarrel": {"damage": "varies", "range": "long", "capacity": "low", "initiative": -3, "strength": 2, "size": 2, "availability": 4, "tags": "attachment"},
    "automatic_grenade_launcher": {"damage": "varies", "range": "extreme", "capacity": "high", "initiative": -6, "strength": 0, "size": 4, "availability": 5, "tags": "vehicle_mounted"},

    # EXPLOSIVES - GRENADE AMMUNITION
    "baton_round": {"damage": 1, "range": "long", "capacity": "single", "initiative": 0, "strength": 0, "size": 1, "availability": 2, "tags": "knockdown, stun, force_5"},
    "buckshot_round": {"damage": 1, "range": "long", "capacity": "single", "initiative": 0, "strength": 0, "size": 1, "availability": 4, "tags": "knockdown, blast_10, force_4"},
    "he_round": {"damage": 3, "range": "long", "capacity": "single", "initiative": 0, "strength": 0, "size": 1, "availability": 4, "tags": "knockdown, blast_10, force_4"},
    "hedp_round": {"damage": 2, "range": "long", "capacity": "single", "initiative": 0, "strength": 0, "size": 1, "availability": 4, "tags": "knockdown, ap_4, blast_10, force_3"},

    # HEAVY WEAPONS - FLAMETHROWERS
    "flamethrower_civilian": {"damage": "special", "range": "short", "capacity": "high", "initiative": -4, "strength": 3, "size": 4, "availability": 3, "tags": "incendiary"},
    "flamethrower_military": {"damage": "special", "range": "medium", "capacity": "high", "initiative": -5, "strength": 3, "size": 4, "availability": 5, "tags": "incendiary"},
}

# ARMOR DATABASE
# Rating: First number is general armor (reduces total damage), second is ballistic armor (downgrades lethal to bashing)
# Strength: Minimum Strength requirement. Lower Strength causes -1 to Brawl and Weaponry rolls
# Defense: Defense penalty while wearing armor
# Speed: Speed penalty while wearing armor  
# Availability: Cost in Resources dots or appropriate Social Merit level
# Coverage: Body areas protected by the armor

ARMOR_DATA = {
    # MODERN ARMOR
    "reinforced_clothing": {
        "general_armor": 1, 
        "ballistic_armor": 0, 
        "strength": 1, 
        "defense": 0, 
        "speed": 0, 
        "availability": 1, 
        "coverage": ["torso", "arms", "legs"]
    },
    "sports_gear": {
        "general_armor": 2, 
        "ballistic_armor": 0, 
        "strength": 2, 
        "defense": -1, 
        "speed": -1, 
        "availability": 1, 
        "coverage": ["torso", "arms", "legs"]
    },
    "kevlar_vest": {
        "general_armor": 1, 
        "ballistic_armor": 3, 
        "strength": 1, 
        "defense": 0, 
        "speed": 0, 
        "availability": 1, 
        "coverage": ["torso"]
    },
    "flak_jacket": {
        "general_armor": 2, 
        "ballistic_armor": 4, 
        "strength": 1, 
        "defense": -1, 
        "speed": 0, 
        "availability": 2, 
        "coverage": ["torso", "arms"]
    },
    "full_riot_gear": {
        "general_armor": 3, 
        "ballistic_armor": 5, 
        "strength": 2, 
        "defense": -2, 
        "speed": -1, 
        "availability": 3, 
        "coverage": ["torso", "arms", "legs"]
    },
    "bomb_suit": {
        "general_armor": 4, 
        "ballistic_armor": 6, 
        "strength": 3, 
        "defense": -5, 
        "speed": -4, 
        "availability": 5, 
        "coverage": ["torso", "arms", "head"]
    },
    "helmet_modern": {
        "general_armor": "special", 
        "ballistic_armor": "special", 
        "strength": 2, 
        "defense": -1, 
        "speed": 0, 
        "availability": 3, 
        "coverage": ["head"],
        "notes": "Extends armor protection to head. Half of worn armor's normal ratings (rounded up). -1 to sight/hearing Perception rolls"
    },

    # ARCHAIC ARMOR
    "leather_hard": {
        "general_armor": 2, 
        "ballistic_armor": 0, 
        "strength": 2, 
        "defense": -1, 
        "speed": 0, 
        "availability": 1, 
        "coverage": ["torso", "arms"]
    },
    "lorica_segmentata": {
        "general_armor": 2, 
        "ballistic_armor": 2, 
        "strength": 3, 
        "defense": -2, 
        "speed": -3, 
        "availability": 4, 
        "coverage": ["torso"]
    },
    "chainmail": {
        "general_armor": 3, 
        "ballistic_armor": 1, 
        "strength": 3, 
        "defense": -2, 
        "speed": -2, 
        "availability": 2, 
        "coverage": ["torso", "arms"],
        "notes": "Full suit can protect entire body at additional cost of one dot"
    },
    "plate_mail": {
        "general_armor": 4, 
        "ballistic_armor": 2, 
        "strength": 3, 
        "defense": -2, 
        "speed": -3, 
        "availability": 4, 
        "coverage": ["torso", "arms", "legs"]
    },
    "helmet_archaic": {
        "general_armor": "special", 
        "ballistic_armor": "special", 
        "strength": 2, 
        "defense": -1, 
        "speed": 0, 
        "availability": 3, 
        "coverage": ["head"],
        "notes": "Extends armor protection to head. Half of worn armor's normal ratings (rounded up). -1 to sight/hearing Perception rolls"
    }
}

# Armor mechanics notes
armor_rules = {
    "general_armor": "Reduces total damage taken by one point per level, starting with most severe damage type",
    "ballistic_armor": "Each point downgrades one point of lethal damage from firearms to bashing damage",
    "application_order": "Apply ballistic armor first, then general armor",
    "minimum_damage": "Successful attack always inflicts at least one bashing damage to armored mortal target",
    "supernatural_exception": "Vampires, spell-protected mages, and werewolves with thick hides are not subject to minimum damage rule",
    "called_shots": "If attacker targets unarmored location, armor protection doesn't apply",
    "riot_shields": "Sometimes come with large bulletproof shields (ballistic armor 2, stacks with armor ratings)"
}

# Coverage area definitions
coverage_areas = {
    "head": "Head and face protection",
    "torso": "Chest, back, and vital organs", 
    "arms": "Arms and shoulders",
    "legs": "Legs and lower body"
}

# Capacity definitions
capacity_types = {
    "single": "Single use per scene",
    "low": "Empties on short burst or failure",
    "medium": "Empties on medium burst, two short bursts, or dramatic failure", 
    "high": "Empties on long burst, two medium bursts, or three short bursts"
}

# Range definitions
range_types = {
    "melee": "Personal space (0-2 meters)",
    "close": "0-5 meters", 
    "short": "5-30 meters",
    "medium": "30-100 meters", 
    "long": "100-300 meters",
    "extreme": "300+ meters",
    "thrown": "Varies by Strength and weapon type"
}

# Availability definitions
availability_costs = {
    0: "Free/No cost",
    1: "• (1 Resources dot or appropriate Social Merit)",
    2: "•• (2 Resources dots or appropriate Social Merit)", 
    3: "••• (3 Resources dots or appropriate Social Merit)",
    4: "•••• (4 Resources dots or appropriate Social Merit)",
    5: "••••• (5 Resources dots or appropriate Social Merit)"
}

# Tag definitions
tag_descriptions = {
    "9-again": "Re-roll 9s and 10s on attack rolls",
    "8-again": "Re-roll 8s, 9s, and 10s on attack rolls", 
    "accurate": "+1 to attack rolls",
    "ap_3": "Armor Piercing 3 - reduces armor by 3",
    "ap_4": "Armor Piercing 4 - reduces armor by 4", 
    "ap_8": "Armor Piercing 8 - reduces armor by 8",
    "bleed": "Doubles weapon bonus for Bleeding Tilt",
    "blast_3": "3 meter blast radius",
    "blast_5": "5 meter blast radius", 
    "blast_10": "10 meter blast radius",
    "brawl": "Uses Brawl skill, enhanced by unarmed bonuses",
    "concealed": "Adds Size to Defense when used defensively",
    "concealment": "Provides concealment modifier",
    "dexterity_requirement": "-1 Damage and Initiative without Dexterity 3+",
    "dexterity_weaponry": "Uses Dexterity + Weaponry to attack",
    "enhance_crafts_survival": "Provides bonus to Crafts or Survival rolls",
    "force_2": "Force rating 2 for explosive knockback",
    "force_3": "Force rating 3 for explosive knockback",
    "force_4": "Force rating 4 for explosive knockback", 
    "force_5": "Force rating 5 for explosive knockback",
    "fragile": "-1 to weapon's Durability",
    "grapple": "Adds weapon dice to grapple rolls",
    "guard": "+1 Defense when wielding",
    "heavy_recoil": "Causes Knocked Down Tilt if not properly braced",
    "inaccurate": "-1 penalty to attack rolls",
    "incendiary": "Causes Burning Tilt",
    "initiative_bonus_1": "+1 Initiative when wielding",
    "knockdown": "Doubles weapon bonus for Knockdown Tilt",
    "no_bonus_damage": "Bonus successes don't add to damage",
    "piercing_1": "Armor Piercing 1 - reduces armor by 1",
    "piercing_2": "Armor Piercing 2 - reduces armor by 2", 
    "reach": "+1 Defense vs smaller weapons, -1 penalty in grapples",
    "slow": "Target gains full Defense against attack",
    "strength_firearms": "Uses Strength + Firearms to attack",
    "stun": "Doubles weapon bonus for Stun Tilt", 
    "thrown": "Can be thrown as ranged attack",
    "two-handed": "Requires two hands, can use one-handed at +1 Strength requirement"
}

class CmdEquipment(MuxCommand):
    """
    Manage equipment, weapons, and armor.
    
    Usage:
        +equipment/list - List your equipment
        +equipment/add <name> <type> [rating] - Add equipment
        +equipment/remove <name> - Remove equipment
        +equipment/view <name> - View equipment details
        +equipment/wield <weapon> - Wield a weapon
        +equipment/unwield - Stop wielding weapon
        +equipment/wear <armor> - Wear armor
        +equipment/unwear - Remove armor
        +equipment/weapons - List available weapons to add
        +equipment/armor - List available armor to add
        
    Types:
        weapon - Combat weapons with damage and availability
        armor - Protective gear with armor ratings
        equipment - General items with availability rating
        style - Fighting styles and specializations
    """
    key = "+equipment"
    aliases = ["+eq", "+gear"]
    help_category = "Character Sheets and Development"
    
    def parse(self):
        """Parse the command arguments."""
        super().parse()  # Initialize switches and other MuxCommand attributes
    
    def func(self):
        """Execute the command"""
        if not self.switches:
            self.caller.msg("Usage: +equipment/list, +equipment/add, +equipment/remove, +equipment/view, +equipment/wield, +equipment/wear, +equipment/weapons, or +equipment/armor")
            return
            
        switch = self.switches[0].lower()
        
        if switch == "list":
            self.list_equipment()
        elif switch == "add":
            self.add_equipment()
        elif switch == "remove":
            self.remove_equipment()
        elif switch == "view":
            self.view_equipment()
        elif switch == "wield":
            self.wield_weapon()
        elif switch == "unwield":
            self.unwield_weapon()
        elif switch == "wear":
            self.wear_armor()
        elif switch == "unwear":
            self.unwear_armor()
        elif switch == "weapons":
            self.list_available_weapons()
        elif switch == "armor":
            self.list_available_armor()
        else:
            self.caller.msg("Invalid switch. See help for usage.")
    
    def list_equipment(self):
        """List all equipment"""
        if not self.caller.db.equipment:
            self.caller.msg("You have no equipment")
            return
            
        output = ["Your Equipment:"]
        
        # Check what's currently equipped
        wielded_weapon = self.caller.db.wielded_weapon
        worn_armor = self.caller.db.worn_armor
        
        # Group by type
        weapons = []
        armor = []
        equipment = []
        styles = []
        
        for name, item in self.caller.db.equipment.items():
            if item["type"] == "weapon":
                status = " (wielded)" if name == wielded_weapon else ""
                weapons.append(f"{name} (Dmg: {item.get('damage', 0)}, Initiative: {item.get('initiative', 0):+d}){status}")
            elif item["type"] == "armor":
                status = " (worn)" if name == worn_armor else ""
                armor.append(f"{name} (Armor: {item.get('general_armor', 0)}/{item.get('ballistic_armor', 0)}){status}")
            elif item["type"] == "equipment":
                equipment.append(f"{name} (Availability {item['rating']})")
            elif item["type"] == "style":
                styles.append(f"{name} ({item['rating']} dots)")
                
        if weapons:
            output.append("\nWeapons:")
            output.extend(f"  {item}" for item in sorted(weapons))
            
        if armor:
            output.append("\nArmor:")
            output.extend(f"  {item}" for item in sorted(armor))
            
        if equipment:
            output.append("\nEquipment:")
            output.extend(f"  {item}" for item in sorted(equipment))
            
        if styles:
            output.append("\nFighting Styles:")
            output.extend(f"  {item}" for item in sorted(styles))
            
        self.caller.msg("\n".join(output))
    
    def add_equipment(self):
        """Add equipment, weapon, or armor"""
        args = self.args.split()
        if len(args) < 2:
            self.caller.msg("Usage: +equipment/add <name> <type> [rating]")
            self.caller.msg("Types: weapon, armor, equipment, style")
            return
            
        name = args[0]
        type_ = args[1].lower()
        rating = int(args[2]) if len(args) > 2 else None
        
        if type_ not in ["weapon", "armor", "equipment", "style"]:
            self.caller.msg("Invalid type. Use: weapon, armor, equipment, or style")
            return
            
        # Initialize equipment if not exists
        if not self.caller.db.equipment:
            self.caller.db.equipment = {}
            
        if name in self.caller.db.equipment:
            self.caller.msg(f"You already have {name}")
            return
            
        # Handle different equipment types
        if type_ == "weapon":
            if name not in WEAPON_DATA:
                self.caller.msg(f"Unknown weapon: {name}")
                self.caller.msg("Use '+equipment/weapons' to see available weapons.")
                return
            weapon_stats = WEAPON_DATA[name]
            self.caller.db.equipment[name] = {
                "type": "weapon",
                "damage": weapon_stats["damage"],
                "initiative": weapon_stats["initiative"],
                "strength": weapon_stats["strength"],
                "size": weapon_stats["size"],
                "range": weapon_stats["range"],
                "availability": weapon_stats["availability"],
                "capacity": weapon_stats.get("capacity"),
                "tags": weapon_stats.get("tags", "")
            }
            
        elif type_ == "armor":
            if name not in ARMOR_DATA:
                self.caller.msg(f"Unknown armor: {name}")
                self.caller.msg("Use '+equipment/armor' to see available armor.")
                return
            armor_stats = ARMOR_DATA[name]
            self.caller.db.equipment[name] = {
                "type": "armor",
                "general_armor": armor_stats["general_armor"],
                "ballistic_armor": armor_stats["ballistic_armor"],
                "strength": armor_stats["strength"],
                "defense": armor_stats["defense"],
                "speed": armor_stats["speed"],
                "availability": armor_stats["availability"],
                "coverage": armor_stats["coverage"],
                "notes": armor_stats.get("notes", "")
            }
            
        elif type_ == "equipment":
            if rating is None:
                self.caller.msg("Equipment requires availability rating (1-5)")
                return
            if not 1 <= rating <= 5:
                self.caller.msg("Equipment availability must be 1-5")
                return
            self.caller.db.equipment[name] = {
                "type": "equipment",
                "rating": rating
            }
            
        elif type_ == "style":
            if rating is None:
                self.caller.msg("Fighting style requires dot rating (1-5)")
                return
            if not 1 <= rating <= 5:
                self.caller.msg("Fighting style ratings must be 1-5")
                return
            self.caller.db.equipment[name] = {
                "type": "style",
                "rating": rating
            }
            
        self.caller.msg(f"Added {type_} {name}")
    
    def remove_equipment(self):
        """Remove equipment or merit"""
        name = self.args.strip()
        
        if not self.caller.db.equipment or name not in self.caller.db.equipment:
            self.caller.msg(f"You don't have {name}")
            return
            
        # Check if item is currently equipped
        if name == self.caller.db.wielded_weapon:
            self.caller.db.wielded_weapon = None
            self.caller.msg(f"You stop wielding {name}")
        if name == self.caller.db.worn_armor:
            self.caller.db.worn_armor = None
            self.caller.msg(f"You remove {name}")
            
        del self.caller.db.equipment[name]
        self.caller.msg(f"Removed {name}")
    
    def view_equipment(self):
        """View equipment details"""
        name = self.args.strip()
        
        if not self.caller.db.equipment or name not in self.caller.db.equipment:
            self.caller.msg(f"You don't have {name}")
            return
            
        item = self.caller.db.equipment[name]
        
        output = [
            f"Name: {name}",
            f"Type: {item['type'].title()}"
        ]
        
        # Add type-specific information
        if item["type"] == "weapon":
            output.extend([
                f"Damage: {item['damage']}",
                f"Initiative: {item['initiative']:+d}",
                f"Strength: {item['strength']}",
                f"Size: {item['size']}",
                f"Range: {item['range']}",
                f"Availability: {item['availability']}"
            ])
            if item.get("capacity"):
                output.append(f"Capacity: {item['capacity']}")
            if item.get("tags"):
                output.append(f"Tags: {item['tags']}")
                
        elif item["type"] == "armor":
            output.extend([
                f"General Armor: {item['general_armor']}",
                f"Ballistic Armor: {item['ballistic_armor']}",
                f"Strength Requirement: {item['strength']}",
                f"Defense Penalty: {item['defense']:+d}",
                f"Speed Penalty: {item['speed']:+d}",
                f"Availability: {item['availability']}"
            ])
            if item.get("coverage"):
                output.append(f"Coverage: {', '.join(item['coverage'])}")
            if item.get("notes"):
                output.append(f"Notes: {item['notes']}")
                
        elif item["type"] == "equipment":
            output.append(f"Availability: {item['rating']}")
            
        elif item["type"] == "style":
            output.extend([
                f"Dots: {item['rating']}",
                f"Description: Fighting style technique"
            ])
            
        self.caller.msg("\n".join(output))
    
    def wield_weapon(self):
        """Wield a weapon"""
        weapon_name = self.args.strip()
        
        if not weapon_name:
            self.caller.msg("Usage: +equipment/wield <weapon>")
            return
            
        if not self.caller.db.equipment or weapon_name not in self.caller.db.equipment:
            self.caller.msg(f"You don't have {weapon_name}")
            return
            
        item = self.caller.db.equipment[weapon_name]
        if item["type"] != "weapon":
            self.caller.msg(f"{weapon_name} is not a weapon")
            return
            
        # Unwield current weapon if any
        if self.caller.db.wielded_weapon:
            self.caller.msg(f"You stop wielding {self.caller.db.wielded_weapon}")
            
        self.caller.db.wielded_weapon = weapon_name
        self.caller.msg(f"You wield {weapon_name}")
        self.caller.location.msg_contents(
            f"{self.caller.name} wields {weapon_name}.",
            exclude=[self.caller]
        )
    
    def unwield_weapon(self):
        """Stop wielding current weapon"""
        if not self.caller.db.wielded_weapon:
            self.caller.msg("You are not wielding a weapon")
            return
            
        weapon_name = self.caller.db.wielded_weapon
        self.caller.db.wielded_weapon = None
        self.caller.msg(f"You stop wielding {weapon_name}")
        self.caller.location.msg_contents(
            f"{self.caller.name} stops wielding {weapon_name}.",
            exclude=[self.caller]
        )
    
    def wear_armor(self):
        """Wear armor"""
        armor_name = self.args.strip()
        
        if not armor_name:
            self.caller.msg("Usage: +equipment/wear <armor>")
            return
            
        if not self.caller.db.equipment or armor_name not in self.caller.db.equipment:
            self.caller.msg(f"You don't have {armor_name}")
            return
            
        item = self.caller.db.equipment[armor_name]
        if item["type"] != "armor":
            self.caller.msg(f"{armor_name} is not armor")
            return
            
        # Remove current armor if any
        if self.caller.db.worn_armor:
            self.caller.msg(f"You remove {self.caller.db.worn_armor}")
            
        self.caller.db.worn_armor = armor_name
        self.caller.msg(f"You wear {armor_name}")
        self.caller.location.msg_contents(
            f"{self.caller.name} puts on {armor_name}.",
            exclude=[self.caller]
        )
    
    def unwear_armor(self):
        """Remove current armor"""
        if not self.caller.db.worn_armor:
            self.caller.msg("You are not wearing armor")
            return
            
        armor_name = self.caller.db.worn_armor
        self.caller.db.worn_armor = None
        self.caller.msg(f"You remove {armor_name}")
        self.caller.location.msg_contents(
            f"{self.caller.name} removes {armor_name}.",
            exclude=[self.caller]
        )
    
    def list_available_weapons(self):
        """List all available weapons that can be added"""
        output = ["Available Weapons (from Chronicles of Darkness: Hurt Locker):"]
        
        categories = {
            "Melee - Bladed": [],
            "Melee - Blunt": [],
            "Melee - Exotic": [],
            "Melee - Improvised": [],
            "Melee - Polearms": [],
            "Ranged - Archery": [],
            "Ranged - Thrown": [],
            "Ranged - Firearms": [],
            "Ranged - Nonlethal": [],
            "Explosives": [],
            "Heavy Weapons": []
        }
        
        for weapon_name, data in WEAPON_DATA.items():
            weapon_str = f"{weapon_name} - Dam:{data['damage']} Init:{data['initiative']:+d} Str:{data['strength']} Size:{data['size']} Avail:{data['availability']}"
            
            # Categorize weapons based on name patterns
            if any(blade in weapon_name for blade in ["axe", "sword", "knife", "machete", "rapier", "hatchet"]):
                categories["Melee - Bladed"].append(weapon_str)
            elif any(blunt in weapon_name for blunt in ["brass_knuckles", "club", "nightstick", "nunchaku", "sap", "sledgehammer"]):
                categories["Melee - Blunt"].append(weapon_str)
            elif any(exotic in weapon_name for exotic in ["chain", "whip", "tiger_claws", "shield", "stake", "stun_gun_melee"]):
                categories["Melee - Exotic"].append(weapon_str)
            elif any(improv in weapon_name for improv in ["blowtorch", "board", "improvised", "nail_gun", "shovel", "tire_iron"]):
                categories["Melee - Improvised"].append(weapon_str)
            elif any(pole in weapon_name for pole in ["spear", "staff"]):
                categories["Melee - Polearms"].append(weapon_str)
            elif any(arch in weapon_name for arch in ["bow", "crossbow"]):
                categories["Ranged - Archery"].append(weapon_str)
            elif "throwing" in weapon_name:
                categories["Ranged - Thrown"].append(weapon_str)
            elif any(firearm in weapon_name for firearm in ["pistol", "revolver", "smg", "rifle", "shotgun"]):
                categories["Ranged - Firearms"].append(weapon_str)
            elif any(nonlethal in weapon_name for nonlethal in ["pepper_spray", "stun_gun_ranged"]):
                categories["Ranged - Nonlethal"].append(weapon_str)
            elif any(explosive in weapon_name for explosive in ["grenade", "molotov", "bomb", "round"]):
                categories["Explosives"].append(weapon_str)
            elif "flamethrower" in weapon_name:
                categories["Heavy Weapons"].append(weapon_str)
        
        for category, weapons in categories.items():
            if weapons:
                output.append(f"\n|c{category}:|n")
                for weapon in sorted(weapons):
                    output.append(f"  {weapon}")
        
        output.append("\nDamage types are determined automatically based on weapon category.")
        output.append("Use '+equipment/add <weapon_name> weapon' to add a weapon.")
        output.append("Use '+equipment/view <weapon_name>' for detailed information.")
        self.caller.msg("\n".join(output))
    
    def list_available_armor(self):
        """List all available armor that can be added"""
        output = ["Available Armor (from Chronicles of Darkness: Hurt Locker):"]
        
        # Separate modern and archaic armor
        modern_armor = []
        archaic_armor = []
        
        for armor_name, data in ARMOR_DATA.items():
            armor_str = f"{armor_name} - Armor:{data['general_armor']}/{data['ballistic_armor']} Str:{data['strength']} Def:{data['defense']:+d} Spd:{data['speed']:+d} Avail:{data['availability']}"
            
            if any(modern in armor_name for modern in ["reinforced", "sports", "kevlar", "flak", "riot", "bomb", "helmet_modern"]):
                modern_armor.append(armor_str)
            else:
                archaic_armor.append(armor_str)
        
        if modern_armor:
            output.append(f"\n|cModern Armor:|n")
            for armor in sorted(modern_armor):
                output.append(f"  {armor}")
                
        if archaic_armor:
            output.append(f"\n|cArchaic Armor:|n")
            for armor in sorted(archaic_armor):
                output.append(f"  {armor}")
        
        output.append("\nArmor format: General/Ballistic armor ratings")
        output.append("General armor reduces total damage, Ballistic downgrades firearm lethal to bashing")
        output.append("Use '+equipment/add <armor_name> armor' to add armor.")
        output.append("Use '+equipment/view <armor_name>' for detailed information.")
        self.caller.msg("\n".join(output)) 