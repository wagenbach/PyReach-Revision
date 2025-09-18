"""
NPC Archetype system for Chronicles of Darkness.

This module defines various NPC archetypes that can be used for random generation.
Archetypes are combinations of templates (Vampire, Werewolf, etc.) and focuses 
(Tank, Dex, Social, etc.) that determine stat distributions.
"""

import random

class NPCArchetype:
    """Base class for NPC archetypes."""
    
    def __init__(self, name, template, focus, description=""):
        self.name = name
        self.template = template
        self.focus = focus
        self.description = description
        
        # Stat priorities - higher values get more points
        self.attribute_priorities = {}
        self.skill_priorities = {}
        self.merit_preferences = []
        self.power_priorities = {}  # Template-specific powers
        
        # Stat ranges for this archetype
        self.attribute_ranges = {}
        self.skill_ranges = {}
        
    def apply_to_npc(self, npc):
        """Apply this archetype to an NPC."""
        # Generate attributes
        self._generate_attributes(npc)
        
        # Generate skills
        self._generate_skills(npc)
        
        # Generate merits
        self._generate_merits(npc)
        
        # Generate template-specific stats
        self._generate_template_stats(npc)
        
        # Set up derived stats
        npc.calculate_derived_stats()
        
    def _generate_attributes(self, npc):
        """Generate attributes based on priorities."""
        # Start with base values
        attributes = {
            "strength": 1, "dexterity": 1, "stamina": 1,
            "presence": 1, "manipulation": 1, "composure": 1,
            "intelligence": 1, "wits": 1, "resolve": 1
        }
        
        # Determine attribute points based on NPC type
        npc_type = npc.db.npc_type
        if npc_type == "minor":
            points = 15  # 5/4/3 spread
        elif npc_type == "major":
            points = 21  # 5/4/3 spread with better stats
        elif npc_type == "boss":
            points = 27  # 5/4/3 spread with exceptional stats
        else:
            points = 18  # Standard spread
        
        # Distribute points based on priorities
        priority_list = sorted(self.attribute_priorities.items(), key=lambda x: x[1], reverse=True)
        
        remaining_points = points
        for attr, priority in priority_list:
            if attr in attributes and remaining_points > 0:
                # Higher priority gets more points
                if priority >= 3:  # Primary
                    points_to_add = min(4, remaining_points)
                elif priority >= 2:  # Secondary
                    points_to_add = min(3, remaining_points)
                else:  # Tertiary
                    points_to_add = min(2, remaining_points)
                
                attributes[attr] += points_to_add
                remaining_points -= points_to_add
        
        # Distribute any remaining points randomly
        while remaining_points > 0:
            attr = random.choice(list(attributes.keys()))
            if attributes[attr] < 5:
                attributes[attr] += 1
                remaining_points -= 1
        
        # Apply to NPC
        if "attributes" not in npc.db.stats:
            npc.db.stats["attributes"] = {}
        npc.db.stats["attributes"].update(attributes)
        
    def _generate_skills(self, npc):
        """Generate skills based on priorities."""
        skills = {}
        
        # Determine skill points based on NPC type
        npc_type = npc.db.npc_type
        if npc_type == "minor":
            points = 15
        elif npc_type == "major":
            points = 25
        elif npc_type == "boss":
            points = 35
        else:
            points = 20
        
        # Distribute points based on priorities
        priority_list = sorted(self.skill_priorities.items(), key=lambda x: x[1], reverse=True)
        
        remaining_points = points
        for skill, priority in priority_list:
            if remaining_points > 0:
                if priority >= 3:  # Primary
                    points_to_add = min(random.randint(3, 5), remaining_points)
                elif priority >= 2:  # Secondary
                    points_to_add = min(random.randint(2, 4), remaining_points)
                else:  # Tertiary
                    points_to_add = min(random.randint(1, 3), remaining_points)
                
                if points_to_add > 0:
                    skills[skill] = points_to_add
                    remaining_points -= points_to_add
        
        # Apply to NPC
        if "skills" not in npc.db.stats:
            npc.db.stats["skills"] = {}
        npc.db.stats["skills"].update(skills)
        
    def _generate_merits(self, npc):
        """Generate merits based on preferences."""
        if not self.merit_preferences:
            return
            
        # Determine merit points based on NPC type
        npc_type = npc.db.npc_type
        if npc_type == "minor":
            merit_points = 5
        elif npc_type == "major":
            merit_points = 10
        elif npc_type == "boss":
            merit_points = 15
        else:
            merit_points = 7
        
        # Try to import merits system
        try:
            from world.cofd.merits.general_merits import merits_dict
            
            if "merits" not in npc.db.stats:
                npc.db.stats["merits"] = {}
            
            remaining_points = merit_points
            for merit_name in self.merit_preferences:
                if merit_name in merits_dict and remaining_points > 0:
                    merit = merits_dict[merit_name]
                    dots = min(random.randint(merit.min_value, merit.max_value), remaining_points)
                    
                    if dots > 0:
                        npc.db.stats["merits"][merit_name] = {
                            "dots": dots,
                            "max_dots": merit.max_value,
                            "merit_type": merit.merit_type,
                            "description": merit.description
                        }
                        remaining_points -= dots
                        
        except ImportError:
            pass  # Merit system not available
            
    def _generate_template_stats(self, npc):
        """Generate template-specific stats like disciplines, gifts, etc."""
        # This will be overridden by specific archetype classes
        pass


# Mortal Archetypes
class MortalTank(NPCArchetype):
    """Tough mortal focused on physical resilience."""
    
    def __init__(self):
        super().__init__("MortalTank", "Mortal", "Tank", 
                        "Physical powerhouse focused on durability and combat")
        
        self.attribute_priorities = {
            "stamina": 3, "strength": 3, "composure": 2,
            "dexterity": 2, "resolve": 2, "wits": 1,
            "intelligence": 1, "presence": 1, "manipulation": 1
        }
        
        self.skill_priorities = {
            "athletics": 3, "brawl": 3, "intimidation": 3,
            "survival": 2, "weaponry": 2, "medicine": 2,
            "drive": 1, "firearms": 1, "streetwise": 1
        }
        
        self.merit_preferences = ["iron_stamina", "fighting_finesse", "quick_healer"]


class MortalDex(NPCArchetype):
    """Agile mortal focused on speed and precision."""
    
    def __init__(self):
        super().__init__("MortalDex", "Mortal", "Dex",
                        "Quick and agile combatant focused on speed")
        
        self.attribute_priorities = {
            "dexterity": 3, "wits": 3, "composure": 2,
            "stamina": 2, "intelligence": 2, "strength": 1,
            "presence": 1, "manipulation": 1, "resolve": 1
        }
        
        self.skill_priorities = {
            "athletics": 3, "firearms": 3, "larceny": 3,
            "drive": 2, "stealth": 2, "weaponry": 2,
            "brawl": 1, "survival": 1, "streetwise": 1
        }
        
        self.merit_preferences = ["fast_reflexes", "gunslinger", "parkour"]


class MortalSocial(NPCArchetype):
    """Charismatic mortal focused on social interaction."""
    
    def __init__(self):
        super().__init__("MortalSocial", "Mortal", "Social",
                        "Charismatic individual skilled in social manipulation")
        
        self.attribute_priorities = {
            "presence": 3, "manipulation": 3, "composure": 2,
            "intelligence": 2, "wits": 2, "resolve": 1,
            "strength": 1, "dexterity": 1, "stamina": 1
        }
        
        self.skill_priorities = {
            "persuasion": 3, "subterfuge": 3, "socialize": 3,
            "empathy": 2, "expression": 2, "intimidation": 2,
            "politics": 1, "streetwise": 1, "investigation": 1
        }
        
        self.merit_preferences = ["striking_looks", "contacts", "allies"]


class MortalMental(NPCArchetype):
    """Intellectual mortal focused on knowledge and investigation."""
    
    def __init__(self):
        super().__init__("MortalMental", "Mortal", "Mental",
                        "Intellectual focused on knowledge and problem-solving")
        
        self.attribute_priorities = {
            "intelligence": 3, "wits": 3, "resolve": 2,
            "composure": 2, "manipulation": 2, "presence": 1,
            "strength": 1, "dexterity": 1, "stamina": 1
        }
        
        self.skill_priorities = {
            "investigation": 3, "science": 3, "medicine": 3,
            "occult": 2, "academics": 2, "crafts": 2,
            "computer": 1, "politics": 1, "empathy": 1
        }
        
        self.merit_preferences = ["eidetic_memory", "encyclopedic_knowledge", "library"]


class MortalSniper(NPCArchetype):
    """Long-range specialist focused on precision and stealth."""
    
    def __init__(self):
        super().__init__("MortalSniper", "Mortal", "Sniper",
                        "Expert marksman focused on long-range precision and stealth")
        
        self.attribute_priorities = {
            "dexterity": 3, "composure": 3, "wits": 2,
            "intelligence": 2, "resolve": 2, "stamina": 1,
            "strength": 1, "presence": 1, "manipulation": 1
        }
        
        self.skill_priorities = {
            "firearms": 3, "stealth": 3, "survival": 3,
            "athletics": 2, "investigation": 2, "crafts": 2,
            "medicine": 1, "drive": 1, "subterfuge": 1
        }
        
        self.merit_preferences = ["sharp_shooter", "firearms_expertise", "trained_observer"]


# Vampire Archetypes
class VampireTank(NPCArchetype):
    """Vampire focused on Fortitude and physical resilience."""
    
    def __init__(self):
        super().__init__("VampireTank", "Vampire", "Tank",
                        "Vampire warrior focused on Fortitude and physical combat")
        
        self.attribute_priorities = {
            "stamina": 3, "strength": 3, "composure": 2,
            "presence": 2, "resolve": 2, "wits": 1,
            "intelligence": 1, "manipulation": 1, "dexterity": 1
        }
        
        self.skill_priorities = {
            "athletics": 3, "brawl": 3, "intimidation": 3,
            "survival": 2, "weaponry": 2, "streetwise": 2,
            "drive": 1, "firearms": 1, "empathy": 1
        }
        
        self.merit_preferences = ["iron_stamina", "fighting_finesse", "contacts"]
        
        self.power_priorities = {
            "fortitude": 3, "potence": 2, "presence": 1
        }


class VampireDex(NPCArchetype):
    """Vampire focused on Celerity and speed."""
    
    def __init__(self):
        super().__init__("VampireDex", "Vampire", "Dex",
                        "Vampire assassin focused on Celerity and precision")
        
        self.attribute_priorities = {
            "dexterity": 3, "wits": 3, "composure": 2,
            "intelligence": 2, "stamina": 2, "strength": 1,
            "presence": 1, "manipulation": 1, "resolve": 1
        }
        
        self.skill_priorities = {
            "athletics": 3, "stealth": 3, "weaponry": 3,
            "larceny": 2, "firearms": 2, "subterfuge": 2,
            "brawl": 1, "survival": 1, "intimidation": 1
        }
        
        self.merit_preferences = ["fast_reflexes", "fighting_finesse", "parkour"]
        
        self.power_priorities = {
            "celerity": 3, "obfuscate": 2, "potence": 1
        }


class VampireSocial(NPCArchetype):
    """Vampire focused on Presence and social manipulation."""
    
    def __init__(self):
        super().__init__("VampireSocial", "Vampire", "Social",
                        "Vampire manipulator focused on Presence and social dominance")
        
        self.attribute_priorities = {
            "presence": 3, "manipulation": 3, "composure": 2,
            "intelligence": 2, "wits": 2, "resolve": 1,
            "strength": 1, "dexterity": 1, "stamina": 1
        }
        
        self.skill_priorities = {
            "persuasion": 3, "subterfuge": 3, "socialize": 3,
            "empathy": 2, "intimidation": 2, "expression": 2,
            "politics": 1, "streetwise": 1, "investigation": 1
        }
        
        self.merit_preferences = ["striking_looks", "allies", "contacts"]
        
        self.power_priorities = {
            "presence": 3, "dominate": 2, "majesty": 1
        }


class VampireMental(NPCArchetype):
    """Vampire focused on Auspex and mental disciplines."""
    
    def __init__(self):
        super().__init__("VampireMental", "Vampire", "Mental",
                        "Vampire scholar focused on Auspex and mental powers")
        
        self.attribute_priorities = {
            "intelligence": 3, "wits": 3, "resolve": 2,
            "composure": 2, "manipulation": 2, "presence": 1,
            "strength": 1, "dexterity": 1, "stamina": 1
        }
        
        self.skill_priorities = {
            "investigation": 3, "occult": 3, "academics": 3,
            "medicine": 2, "science": 2, "empathy": 2,
            "subterfuge": 1, "politics": 1, "crafts": 1
        }
        
        self.merit_preferences = ["eidetic_memory", "encyclopedic_knowledge", "contacts"]
        
        self.power_priorities = {
            "auspex": 3, "obfuscate": 2, "animalism": 1
        }


# Werewolf Archetypes
class WerewolfTank(NPCArchetype):
    """Werewolf focused on Endurance and physical resilience."""
    
    def __init__(self):
        super().__init__("WerewolfTank", "Werewolf", "Tank",
                        "Werewolf warrior focused on Endurance and pack leadership")
        
        self.attribute_priorities = {
            "stamina": 3, "strength": 3, "presence": 2,
            "composure": 2, "resolve": 2, "wits": 1,
            "intelligence": 1, "manipulation": 1, "dexterity": 1
        }
        
        self.skill_priorities = {
            "athletics": 3, "brawl": 3, "intimidation": 3,
            "survival": 2, "animal_ken": 2, "empathy": 2,
            "medicine": 1, "weaponry": 1, "streetwise": 1
        }
        
        self.merit_preferences = ["iron_stamina", "fighting_finesse", "pack_alpha"]
        
        self.power_priorities = {
            "endurance": 3, "strength": 2, "dominance": 1
        }


# Registry of all archetypes
ARCHETYPE_REGISTRY = {
    # Mortal archetypes
    "mortal_tank": MortalTank(),
    "mortal_dex": MortalDex(),
    "mortal_social": MortalSocial(),
    "mortal_mental": MortalMental(),
    "mortal_sniper": MortalSniper(),
    
    # Vampire archetypes
    "vampire_tank": VampireTank(),
    "vampire_dex": VampireDex(),
    "vampire_social": VampireSocial(),
    "vampire_mental": VampireMental(),
    
    # Werewolf archetypes
    "werewolf_tank": WerewolfTank(),
    
    # Aliases for convenience
    "mortaltank": MortalTank(),
    "mortaldex": MortalDex(),
    "mortalsocial": MortalSocial(),
    "mortalmental": MortalMental(),
    "mortalsniper": MortalSniper(),
    "vampiretank": VampireTank(),
    "vampiredex": VampireDex(),
    "vampiresocial": VampireSocial(),
    "vampiremental": VampireMental(),
    "werewolftank": WerewolfTank(),
}


def get_archetype(archetype_name, template=None):
    """Get an archetype by name, optionally filtered by template."""
    archetype_name = archetype_name.lower().replace(" ", "_")
    
    if archetype_name in ARCHETYPE_REGISTRY:
        archetype = ARCHETYPE_REGISTRY[archetype_name]
        
        # If template is specified, check if it matches
        if template and archetype.template.lower() != template.lower():
            return None
            
        return archetype
    
    return None


def get_archetypes_by_template(template):
    """Get all archetypes for a specific template."""
    template = template.lower()
    return [arch for arch in ARCHETYPE_REGISTRY.values() 
            if arch.template.lower() == template]


def list_all_archetypes():
    """Get a list of all available archetype names."""
    return list(ARCHETYPE_REGISTRY.keys()) 