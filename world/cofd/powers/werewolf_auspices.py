"""
Werewolf: The Forsaken Auspices
Detailed auspice information for Chronicles of Darkness 2nd Edition.
Based on Werewolf: The Forsaken 2nd Edition.
"""

ALL_AUSPICES = {
    "cahalith": {
        "name": "Cahalith",
        "moon_phase": "Gibbous Moon",
        "hunt_role": "Visionary",
        "auspice_skills": ["Crafts", "Expression", "Persuasion"],
        "primary_renown": "Glory",
        "auspice_gifts": ["Gibbous Moon", "Inspiration", "Knowledge"],
        "hunters_aspect": "Monstrous - Inflicts Resigned Condition",
        "auspice_benefit": {
            "name": "Prophetic Dreams",
            "description": "Roll Intelligence + Occult for hints; Storyteller can confer +3 modifier to player/packmate or -3 modifier to NPC, or can fail action/suffer damage/setback to take Beat.",
            "frequency": "Once a Chapter any use"
        },
        "description": "The Gibbous Moon, visionaries and lorekeepers who preserve the history and legends of the Uratha",
        "book": "WTF 2e"
    },
    "elodoth": {
        "name": "Elodoth",
        "moon_phase": "Half Moon",
        "hunt_role": "Walker Between",
        "auspice_skills": ["Empathy", "Investigation", "Politics"],
        "primary_renown": "Honor",
        "auspice_gifts": ["Half Moon", "Insight", "Warding"],
        "hunters_aspect": "Isolating - Inflicts Isolated Condition",
        "auspice_benefit": {
            "name": "Darkness Into Light",
            "description": "Can cease Death Rage, target gains Stunned Tilt for next turn if Basu-Im; Roll Presence + Empathy + Primal Urge - Resolve + Composure to force into Wasu-Im.",
            "frequency": "Once a Chapter any use"
        },
        "description": "The Half Moon, judges and mediators who walk between the worlds of flesh and spirit",
        "book": "WTF 2e"
    },
    "irraka": {
        "name": "Irraka",
        "moon_phase": "New Moon",
        "hunt_role": "Stalker",
        "auspice_skills": ["Larceny", "Stealth", "Subterfuge"],
        "primary_renown": "Cunning",
        "auspice_gifts": ["New Moon", "Evasion", "Stealth"],
        "hunters_aspect": "Blissful - Inflicts Unaware Condition",
        "auspice_benefit": {
            "name": "Closer than You",
            "description": "Can: Move initiative rating within one point of target, must remain higher/lower; Move in range to use teeth/claws on opponent not attacking player; Subtract -2 from number of doors in Social Maneuvering.",
            "frequency": "Once a Chapter any use"
        },
        "description": "The New Moon, scouts and tricksters who strike from the shadows",
        "book": "WTF 2e"
    },
    "ithaeur": {
        "name": "Ithaeur",
        "moon_phase": "Crescent Moon",
        "hunt_role": "Spirit Master",
        "auspice_skills": ["Animal Ken", "Medicine", "Occult"],
        "primary_renown": "Wisdom",
        "auspice_gifts": ["Crescent Moon", "Elemental", "Shaping"],
        "hunters_aspect": "Mystic - Inflicts Mystified Condition",
        "auspice_benefit": {
            "name": "Spirit Howl",
            "description": "Spend Essence point to cause all spirits of lower rank to flee/hide/go dormant, more powerful avoid; spirits allies of pack/tribal totem may come to aid; hostile spirit's Defense penalized by Wisdom Renown.",
            "frequency": "Once a Chapter any use"
        },
        "description": "The Crescent Moon, spirit-talkers and shamans who bridge the Gauntlet",
        "book": "WTF 2e"
    },
    "rahu": {
        "name": "Rahu",
        "moon_phase": "Full Moon",
        "hunt_role": "Warrior",
        "auspice_skills": ["Brawl", "Intimidation", "Survival"],
        "primary_renown": "Purity",
        "auspice_gifts": ["Full Moon", "Dominance", "Strength"],
        "hunters_aspect": "Dominant - Inflicts Swaggering Condition",
        "auspice_benefit": {
            "name": "Tenacious",
            "description": "Can ignore Conditions/Tilts hindering player in combat for 2 turns: Does not resolve Condition/end Tilt, Conditions/Tilts return after 2 turns.",
            "frequency": "Once a Chapter any use"
        },
        "description": "The Full Moon, warriors and protectors who lead the hunt",
        "book": "WTF 2e"
    },
}

# ============================================================================
# HELPER FUNCTIONS
# ============================================================================

def get_auspice(auspice_name):
    """Get a specific auspice by name."""
    auspice_key = auspice_name.lower().replace(" ", "_")
    return ALL_AUSPICES.get(auspice_key)

def get_all_auspices():
    """Get all auspice data."""
    return ALL_AUSPICES.copy()

