"""
Geist: The Sin-Eaters Template Definition for Chronicles of Darkness.
Sin-Eaters are those who have died and returned, bound to powerful ghosts called geists.
"""

from . import register_template


# Valid geist burdens (how they died)
GEIST_BURDENS = [
    "abiding", "bereaved", "hungry", "kindly", "vengeful"
]

# Valid krewe types
GEIST_KREWE_TYPES = [
    "family", "industrial", "network", "military", "academic"
]

# Primary powers (rated 1-5 dots) - Haunts
GEIST_PRIMARY_POWERS = [
    "boneyard", "caul", "curse", "dirge", "marionette", "memoria", "oracle", "rage", "shroud", "tomb"
]

# Secondary powers (individual abilities) - Keys and Ceremonies
GEIST_SECONDARY_POWERS = [
    # Keys (individual abilities)
    "beasts", "blood", "chance", "cold wind", "deep waters", "disease", "grave dirt", "pyre flame", "stillness",
    # Ceremonies (individual rituals)
    # Level 1 Ceremonies
    "dead man's camera", "death watch", "diviner's jawbone", "lovers' telephone", "ishtar's perfume",
    # Level 2 Ceremonies
    "crow girl kiss", "gifts of persephone", "ghost trap", "skeleton key",
    # Level 3 Ceremonies
    "bestow regalia", "krewe binding", "speaker for the dead", "black cat's crossing", "bloody codex", "dumb supper",
    # Level 4 Ceremonies
    "forge anchor", "maggot homonculus",
    # Level 5 Ceremonies
    "pass on", "ghost binding", "persephone's return"
]

# All geist powers combined
GEIST_ALL_POWERS = GEIST_PRIMARY_POWERS + GEIST_SECONDARY_POWERS

# Backwards compatibility aliases
GEIST_HAUNTS = GEIST_PRIMARY_POWERS
GEIST_KEYS = ["beasts", "blood", "chance", "cold wind", "deep waters", "disease", "grave dirt", "pyre flame", "stillness"]
GEIST_CEREMONIES = [
    "dead man's camera", "death watch", "diviner's jawbone", "lovers' telephone", "ishtar's perfume",
    "crow girl kiss", "gifts of persephone", "ghost trap", "skeleton key",
    "bestow regalia", "krewe binding", "speaker for the dead", "black cat's crossing", "bloody codex", "dumb supper",
    "forge anchor", "maggot homonculus",
    "pass on", "ghost binding", "persephone's return"
]

# Valid crisis point triggers for geists
GEIST_CRISIS_TRIGGERS = [
    "betrayal", "abandonment", "mortality", "innocence", "loss", "helplessness", "failure", "isolation"
]

# Valid remembrance trait types (skills or merits ≤3 dots)
GEIST_REMEMBRANCE_SKILLS = [
    "athletics", "brawl", "drive", "firearms", "larceny", "stealth", "survival", "weaponry",
    "animal_ken", "empathy", "expression", "intimidation", "persuasion", "socialize", "streetwise", "subterfuge",
    "crafts", "investigation", "medicine", "occult", "politics", "science"
]

GEIST_REMEMBRANCE_MERITS = [
    "contacts", "allies", "resources", "safe_place", "library", "mentor", "retainer", "status"
]

# ==================== HAUNT DETAILS ====================

# The Boneyard
HAUNT_BONEYARD = {
    "raise_the_boneyard": {
        "name": "Raise the Boneyard",
        "rank": 1,
        "cost": "●+",
        "description": "Spread Plasm to haunt a Boneyard, which becomes Open to ghosts. Understand the Boneyard's layout and defeat attempts to hide from you in it.",
        "book": "GTS 2e p.102"
    },
    "eyes_in_the_paintings": {
        "name": "Eyes in the Paintings",
        "rank": 2,
        "cost": "●",
        "description": "See and sense through places in the Boneyard.",
        "book": "GTS 2e p.102"
    },
    "no_escape": {
        "name": "No Escape",
        "rank": 3,
        "cost": "—",
        "description": "Raise larger Boneyards.",
        "book": "GTS 2e p.102",
        "additional": "●/die to penalize attempts to leave the Boneyard by any means."
    },
    "earthquake_weather": {
        "name": "Earthquake Weather",
        "rank": 4,
        "cost": "●●●",
        "description": "Conjure Environmental Tilts within the Boneyard.",
        "book": "GTS 2e p.103"
    },
    "the_new_law": {
        "name": "The New Law",
        "rank": 5,
        "cost": "●●",
        "description": "Impose an Old Law upon the Boneyard, penalizing actions to break it.",
        "book": "GTS 2e p.103",
        "additional": "●● to punish violators with the rote quality and as a ghostly bane."
    }
}

# The Caul
HAUNT_CAUL = {
    "extrude_the_caul": {
        "name": "Extrude the Caul",
        "rank": 1,
        "cost": "● to ●●●●●",
        "description": "Take on a geistly flesh charged by Plasm. Spend a charge to ignore wound penalties, substitute your geist's Attribute for yours, or reduce the exceptional success threshold from five to three on an action making use of your plasmic form.",
        "book": "GTS 2e p.104"
    },
    "cold_flesh": {
        "name": "Cold Flesh",
        "rank": 2,
        "cost": "●●●",
        "description": "For each dot of Caul, gain +1/+½ Armor.",
        "book": "GTS 2e p.104"
    },
    "vitiate": {
        "name": "Vitiate",
        "rank": 3,
        "cost": "—",
        "description": "Extrude the Caul generates twice the charges.",
        "book": "GTS 2e p.105",
        "additional": "Various Plasm costs for: Swell in Size (+2 Size per Strength dot), Contort into skittering shape (●), Inflict lethal unarmed (●), Grow wings (●●), Explode into swarm (●●●●)"
    },
    "disarticulation": {
        "name": "Disarticulation",
        "rank": 4,
        "cost": "● to ●●●●●",
        "description": "Disgorge an obedient homunculus with Plasm as Health and twice Plasm as a Physical dice pool.",
        "book": "GTS 2e p.105"
    },
    "the_hungry_dead": {
        "name": "The Hungry Dead",
        "rank": 5,
        "cost": "●/Size",
        "description": "Devour a fresh corpse or incapacitated ghost. You may spend remaining charges to take the victim's shape or substitute their traits for your own.",
        "book": "GTS 2e p.105"
    }
}

# The Curse
HAUNT_CURSE = {
    "lay_the_curse": {
        "name": "Lay the Curse",
        "rank": 1,
        "cost": "● to ●●●●",
        "description": "Mark a subject with a Plasm-charged curse. Spend a charge to impose a -2 penalty on an action.",
        "book": "GTS 2e p.106"
    },
    "gremlin": {
        "name": "Gremlin",
        "rank": 2,
        "cost": "●●",
        "description": "Spend a charge to invert equipment bonuses into penalties, or two charges to cause tools to deal their bonus as damage on use.",
        "book": "GTS 2e p.106",
        "additional": "●● to spend a charge to extinguish all fires set by the subject for a scene."
    },
    "malady": {
        "name": "Malady",
        "rank": 3,
        "cost": "—",
        "description": "Lay the Curse generates twice the charges.",
        "book": "GTS 2e p.107",
        "additional": "●● to spend a charge to inflict an injurious Personal Tilt for a scene through dangerous misfortune. ●● to spend the Curse to deal three lethal damage through misfortune."
    },
    "exhaustion": {
        "name": "Exhaustion",
        "rank": 4,
        "cost": "●●",
        "description": "Spend a charge to reduce a Social roll to a chance die.",
        "book": "GTS 2e p.107",
        "additional": "●● to spend a charge to deny Willpower recovery."
    },
    "forgotten": {
        "name": "Forgotten",
        "rank": 5,
        "cost": "●●●",
        "description": "Spend a charge to force the subject to spend Willpower to be noticed.",
        "book": "GTS 2e p.107",
        "additional": "●●● to spend a charge to block the use of a Social Merit. ●●● to spend a charge to bring the subject in contact with ghostly Twilight."
    }
}

# The Dirge
HAUNT_DIRGE = {
    "sing_the_dirge": {
        "name": "Sing the Dirge",
        "rank": 1,
        "cost": "● to ●●●●●",
        "description": "Sing the wordless Dirge to evoke a feeling or simple response. While you sing, (Plasm) subjects gain a +2 bonus to obey, but must spend Willpower to act in contradiction.",
        "book": "GTS 2e p.108"
    },
    "exaltation": {
        "name": "Exaltation",
        "rank": 2,
        "cost": "●/Essence",
        "description": "Share your Plasm as Essence with ghostly subjects.",
        "book": "GTS 2e p.108",
        "additional": "●● to render a living subject Inspired."
    },
    "communion": {
        "name": "Communion",
        "rank": 3,
        "cost": "—",
        "description": "Sing the Dirge to entire areas.",
        "book": "GTS 2e p.108",
        "additional": "●● to give a perfect impression to subjects. You may roll Synergy + Dirge to open their Doors."
    },
    "exaltation_greater": {
        "name": "Exaltation (Greater)",
        "rank": 4,
        "cost": "●●",
        "description": "Lift a negative mental Condition from a subject, or suppress a Persistent Condition while you sing.",
        "book": "GTS 2e p.108",
        "additional": "●●● to inflict a negative mental Condition on a subject."
    },
    "visitation": {
        "name": "Visitation",
        "rank": 5,
        "cost": "●/Rank",
        "description": "Impose a Manifestation Condition on a ghostly subject.",
        "book": "GTS 2e p.109"
    }
}

# The Marionette
HAUNT_MARIONETTE = {
    "string_the_marionette": {
        "name": "String the Marionette",
        "rank": 1,
        "cost": "● to ●●●",
        "description": "Cast strings of Plasm upon a subject of (Plasm) Size. You may take the marionette's actions as it could normally move, or swing it about as an improvised throwing weapon.",
        "book": "GTS 2e p.109"
    },
    "swarm": {
        "name": "Swarm",
        "rank": 2,
        "cost": "●●",
        "description": "You may simultaneously string a number of marionettes equal to your Haunt rating.",
        "book": "GTS 2e p.110"
    },
    "phantom_strength": {
        "name": "Phantom Strength",
        "rank": 3,
        "cost": "● to ●●●",
        "description": "String marionettes of (Marionette + 2 × Plasm) Size.",
        "book": "GTS 2e p.110",
        "additional": "●● to impose a -3 penalty to contest your control."
    },
    "servant": {
        "name": "Servant",
        "rank": 4,
        "cost": "●●",
        "description": "Sink your strings into a marionette to render it an obedient servant, which will follow orders without direct manipulation.",
        "book": "GTS 2e p.110",
        "additional": "●●●● to extend the Servant Condition for 24 hours."
    },
    "traitor_flesh": {
        "name": "Traitor Flesh",
        "rank": 5,
        "cost": "●●",
        "description": "Retain control of a marionette through lethal damage or a breaking point.",
        "book": "GTS 2e p.110",
        "additional": "●●● to inflict two lethal damage to a marionette contesting your control."
    }
}

# The Memoria
HAUNT_MEMORIA = {
    "recall_the_memoria": {
        "name": "Recall the Memoria",
        "rank": 1,
        "cost": "● to ●●●●●",
        "description": "Witness a place or Anchor's memories of a particular death. Spend a Plasm charge for 8-Again to investigate the death or put it to rest, or to store memories as soft leverage that opens a Door.",
        "book": "GTS 2e p.112"
    },
    "denouement": {
        "name": "Dénouement",
        "rank": 2,
        "cost": "● to ●●●●●",
        "description": "Weave Plasm into a phantasm of the witnessed memories across an area, visible but not tangible to others.",
        "book": "GTS 2e p.112"
    },
    "memory_in_a_bottle": {
        "name": "Memory in a Bottle",
        "rank": 3,
        "cost": "—",
        "description": "Recall the Memoria generates twice the charges.",
        "book": "GTS 2e p.112",
        "additional": "●●● to seal the Memoria in a container to be released later, taking the memory with it."
    },
    "mystery_play": {
        "name": "Mystery Play",
        "rank": 4,
        "cost": "● to ●●●●●",
        "description": "Cast Plasm upon witnesses to draft them into roles in the memory.",
        "book": "GTS 2e p.112"
    },
    "break_the_cycle": {
        "name": "Break the Cycle",
        "rank": 5,
        "cost": "●●",
        "description": "Actors in a Mystery Play can roll Resolve + Synergy to play out other actions in the memory. At the conclusion of the memory, Actors can resolve a Condition related to the memory, and ghostly Actors can resolve an Anchor and gain Rank 2.",
        "book": "GTS 2e p.113"
    }
}

# The Oracle
HAUNT_ORACLE = {
    "consult_the_oracle": {
        "name": "Consult the Oracle",
        "rank": 1,
        "cost": "● to ●●●●",
        "description": "Release your ghost from your body into the ether. Spend a Plasm charge for your body to answer a question put to it about the touch of death, desires, and the hidden.",
        "book": "GTS 2e p.114"
    },
    "wandering_shade": {
        "name": "Wandering Shade",
        "rank": 2,
        "cost": "●",
        "description": "Your ghost wanders farther. You may spend a charge to answer a question about finding threats, the needy, the lost, and crimes against the dead.",
        "book": "GTS 2e p.114"
    },
    "spirit_reading": {
        "name": "Spirit Reading",
        "rank": 3,
        "cost": "—",
        "description": "Consult the Oracle generates twice the charges.",
        "book": "GTS 2e p.115",
        "additional": "●● to spend a charge to answer a question about ghostly bans, banes, and attachments to life."
    },
    "descent": {
        "name": "Descent",
        "rank": 4,
        "cost": "●●●",
        "description": "Your ghost roams the Underworld. Answer one question about ferrymen, the Old Laws, or Irkalla's Gates.",
        "book": "GTS 2e p.115"
    },
    "nekyia": {
        "name": "Nekyia",
        "rank": 5,
        "cost": "●●●●",
        "description": "Answer one question about future betrayal, opportunities, brushes with death, or Underworld trials.",
        "book": "GTS 2e p.115"
    }
}

# The Rage
HAUNT_RAGE = {
    "vent_the_rage": {
        "name": "Vent the Rage",
        "rank": 1,
        "cost": "● to ●●●●",
        "description": "Channel ghostly assaults for a scene, applying Plasm as a weapon rating and dealing lethal damage to ghosts. Roll the higher of your Brawl or Rage in your unarmed dice pool, ignoring unskilled penalties.",
        "book": "GTS 2e p.116"
    },
    "black_iron_blade": {
        "name": "Black-Iron Blade",
        "rank": 2,
        "cost": "●●",
        "description": "Your strike inflicts a disabling or poisonous Personal Tilt.",
        "book": "GTS 2e p.116"
    },
    "maelstrom": {
        "name": "Maelstrom",
        "rank": 3,
        "cost": "—",
        "description": "Make unarmed ranged attacks out to 30 yards.",
        "book": "GTS 2e p.117",
        "additional": "●● to unleash an unarmed autofire medium burst."
    },
    "shatter": {
        "name": "Shatter",
        "rank": 4,
        "cost": "●●●",
        "description": "Deal aggravated damage with an unarmed attack.",
        "book": "GTS 2e p.117",
        "additional": "●● to traumatize a victim who suffers a breaking point from the Rage, inflicting Fugue."
    },
    "breaking_the_world": {
        "name": "Breaking the World",
        "rank": 5,
        "cost": "●●●●",
        "description": "Lash out with an Environmental Tilt to which you remain immune.",
        "book": "GTS 2e p.117"
    }
}

# The Shroud
HAUNT_SHROUD = {
    "don_the_shroud": {
        "name": "Don the Shroud",
        "rank": 1,
        "cost": "● to ●●●●",
        "description": "Wear your geist as a ghostly apparition. Ignore physiological needs and mundane disabling, and spend a Plasm charge to pass into Twilight for (Shroud) turns.",
        "book": "GTS 2e p.118"
    },
    "vision_of_mist": {
        "name": "Vision of Mist",
        "rank": 2,
        "cost": "●",
        "description": "Exude no body heat and pass through motion and laser sensors unnoticed.",
        "book": "GTS 2e p.118",
        "additional": "●● to fly at half Speed."
    },
    "haunting_presence": {
        "name": "Haunting Presence",
        "rank": 3,
        "cost": "—",
        "description": "Spend charges to enter Twilight for minutes instead of turns.",
        "book": "GTS 2e p.118",
        "additional": "●●● to choose a Manifestation (Discorporate, Fetter, Image, or Possess) or Numen (Sign or Hallucination) to use while Twilit."
    },
    "harrow": {
        "name": "Harrow",
        "rank": 4,
        "cost": "●●",
        "description": "You may spend a charge to pull another person with you into Twilight.",
        "book": "GTS 2e p.119"
    },
    "descent_shroud": {
        "name": "Descent",
        "rank": 5,
        "cost": "●●●",
        "description": "You may spend a charge to cross directly into or out of the Upper Reaches, guided by emotional ties. You may spend another charge to pull another person with you into the Underworld.",
        "book": "GTS 2e p.119"
    }
}

# The Tomb
HAUNT_TOMB = {
    "open_the_tomb": {
        "name": "Open the Tomb",
        "rank": 1,
        "cost": "● to ●●●●",
        "description": "Reassemble part of a corpse or destroyed object of (Tomb + Plasm) Size into a completed inanimate replica for (Tomb) days. The replica is also tangible to Twilit ghosts.",
        "book": "GTS 2e p.120"
    },
    "headstone": {
        "name": "Headstone",
        "rank": 2,
        "cost": "●●",
        "description": "Open the Tomb using an item depicting or strongly tied to the object or creature.",
        "book": "GTS 2e p.120"
    },
    "empty_graves": {
        "name": "Empty Graves",
        "rank": 3,
        "cost": "—",
        "description": "Double the Size capability of Open the Tomb, and extend its duration indefinitely.",
        "book": "GTS 2e p.120",
        "additional": "— to Open the Tomb may produce obedient undead replicas of creatures. ●●● for the replica to become Open to ghosts, and can be Possessed by the ghost of its model."
    },
    "stygian_treasures": {
        "name": "Stygian Treasures",
        "rank": 4,
        "cost": "●●",
        "description": "The replica's user can either see, hear, or communicate with the dead or the Underworld.",
        "book": "GTS 2e p.120"
    },
    "terra_cotta_soldiers": {
        "name": "Terra Cotta Soldiers",
        "rank": 5,
        "cost": "● to ●●●●●",
        "description": "Open the Tomb can reproduce notional objects from representations, producing Merits or services by their rating in Plasm.",
        "book": "GTS 2e p.120"
    }
}

# The Void
HAUNT_VOID = {
    "awaken_the_void": {
        "name": "Awaken the Void",
        "rank": 1,
        "cost": "● to ●●●●",
        "description": "Welcome a blinding darkness. Within the darkness, your attacks ignore (Void) Durability and Armor, and the attacks of others ignore half that.",
        "book": "Mem p.24"
    },
    "annihilation_of_form": {
        "name": "Annihilation of Form",
        "rank": 2,
        "cost": "●●●",
        "description": "Make ranged attacks within the darkness, dealing lethal damage unarmed.",
        "book": "Mem p.25",
        "additional": "●+ to destroy objects, terrain, or immobilized creatures, paying extra for Size greater than Synergy."
    },
    "feasting_on_infinity": {
        "name": "Feasting on Infinity",
        "rank": 3,
        "cost": "—",
        "description": "Recover Plasm for every 10 points of Health, Corpus, or Structure you devour.",
        "book": "Mem p.25",
        "additional": "●● to remain unblinded by Awakening the Void. ●● to consume material without adverse effects, and deal aggravated damage with a grappling bite."
    },
    "the_end_of_all_things": {
        "name": "The End of All Things",
        "rank": 4,
        "cost": "●+",
        "description": "Open an annihilatory vacuum from within the darkness, which deals aggravated damage for each turn of contact, and pulls in anything without Size greater than Plasm spent. If that Plasm exceeds your Synergy, the vacuum threatens to persist as long as it can feed.",
        "book": "Mem p.25"
    },
    "the_wrong_way_door": {
        "name": "The Wrong-Way Door",
        "rank": 5,
        "cost": "●●●●●+",
        "description": "Tear open a wound that directly connects the material realm to the Underworld for a day. Spend Plasm to open larger or more persistent wounds.",
        "book": "Mem p.25"
    }
}

# The Well
HAUNT_WELL = {
    "submerge_the_self": {
        "name": "Submerge the Self",
        "rank": 1,
        "cost": "●+",
        "description": "Your identity runs deep and fluid, allowing you to trade and use Memories like a ghost, treating Plasm as a maximum applicable Memory Skill bonus.",
        "book": "Mem p.27"
    },
    "awash_in_unknown_tides": {
        "name": "Awash in Unknown Tides",
        "rank": 2,
        "cost": "● to ●●●●●",
        "description": "Summon a wellspring from one of the Underworld's Rivers, causing an Environmental Tilt or Extreme Environment proportionate to Plasm spent. Rivers may produce other effects at the Storyteller's discretion.",
        "book": "Mem p.27"
    },
    "lightless_depths": {
        "name": "Lightless Depths",
        "rank": 3,
        "cost": "●●",
        "description": "Dissolve all memories formed in your presence while the self is submerged, inflicting Amnesia.",
        "book": "Mem p.28",
        "additional": "●●● to steal a Memory with skin to skin contact, but suffer a crisis point."
    },
    "vortices_of_self_and_memory": {
        "name": "Vortices of Self and Memory",
        "rank": 4,
        "cost": "●+",
        "description": "Fuse two Memories into a new Memory that synthesizes their themes, paying additional Plasm to carry over dots of Memory Skills.",
        "book": "Mem p.28",
        "additional": "●/Resolve to infuse a Memory into a third party, living or dead."
    },
    "remade_in_the_oceans_womb": {
        "name": "Remade in the Ocean's Womb",
        "rank": 5,
        "cost": "●/feature",
        "description": "Take intrinsic features such as Memories, physical characteristics, or dots of Attributes or Merits from a subject submerged in water into yourself.",
        "book": "Mem p.29",
        "additional": "●/feature to graft such an intrinsic feature into a subject submerged in water."
    }
}

# All Haunts dictionary
ALL_HAUNTS = {
    "boneyard": HAUNT_BONEYARD,
    "caul": HAUNT_CAUL,
    "curse": HAUNT_CURSE,
    "dirge": HAUNT_DIRGE,
    "marionette": HAUNT_MARIONETTE,
    "memoria": HAUNT_MEMORIA,
    "oracle": HAUNT_ORACLE,
    "rage": HAUNT_RAGE,
    "shroud": HAUNT_SHROUD,
    "tomb": HAUNT_TOMB,
    "void": HAUNT_VOID,
    "well": HAUNT_WELL
}

# ==================== KEY DETAILS ====================

# Key descriptions with unlock attributes and mechanics
GEIST_KEY_DETAILS = {
    "beasts": {
        "name": "Beasts",
        "full_name": "The Key of Beasts",
        "alternate_names": "The Primeval Key, the Key of Tooth and Claw",
        "attribute": "Wits",
        "description": "The Primeval Key of Tooth and Claw rules all beasts and haunts places hidden or reclaimed from mankind.",
        "doom": "Fail an action due to animal interference.",
        "book": "GTS 2e p.122"
    },
    "blood": {
        "name": "Blood",
        "full_name": "The Key of Blood", 
        "alternate_names": "The Stigmatic Key, the Key of Crimson Agony",
        "attribute": "Presence",
        "description": "The Stigmatic Key of Crimson Agony turns when danger creeps unexpected and inevitable.",
        "doom": "Dramatically fail an action to avoid violence.",
        "book": "GTS 2e p.122"
    },
    "chance": {
        "name": "Chance",
        "full_name": "The Key of Chance",
        "alternate_names": "The Bastard's Key, the Key of Jinx and Hex", 
        "attribute": "Dexterity",
        "description": "The Bastard's Key of Jinx and Hex rules foolhardy gambles, improbable misfortune and dangerous machinery.",
        "doom": "Invert a roll with a +3 bonus into a chance die.",
        "book": "GTS 2e p.122"
    },
    "cold wind": {
        "name": "Cold Wind",
        "full_name": "The Key of Cold Wind",
        "alternate_names": "The Breathless Key, the Key of Gale and Garrote",
        "attribute": "Resolve", 
        "description": "The Breathless Key of Gale and Garrote unlocks conditions of exposure and howling noise.",
        "doom": "Confess a dark secret or suffer Extreme Cold.",
        "book": "GTS 2e p.122"
    },
    "deep waters": {
        "name": "Deep Waters",
        "full_name": "The Key of Deep Waters",
        "alternate_names": "The Tear-Stained Key, the Key of Azure Futility",
        "attribute": "Manipulation",
        "description": "The Tear-Stained Key of Azure Futility haunts through enclosure, submergence and suffocation.",
        "doom": "Reduce a full Willpower refresh to only one point.",
        "book": "GTS 2e p.123"
    },
    "disease": {
        "name": "Disease",
        "full_name": "The Key of Disease",
        "alternate_names": "The Wasting Key, the Key of Plague and Pestilence",
        "attribute": "Stamina",
        "description": "The Wasting Key of Plague and Pestilence turns wherever sickness and poison can be found.",
        "doom": "Suffer the Sick Tilt for a full scene.",
        "book": "GTS 2e p.123"
    },
    "grave dirt": {
        "name": "Grave Dirt",
        "full_name": "The Key of Grave Dirt", 
        "alternate_names": "The Crushing Key, the Key of Slate Bereavement",
        "attribute": "Strength",
        "description": "The Crushing Key of Slate Bereavement haunts subterranean hollows and anything dominated by the past.",
        "doom": "Extended actions cost Willpower unless fed by sacrifice.",
        "book": "GTS 2e p.123"
    },
    "pyre flame": {
        "name": "Pyre Flame",
        "full_name": "The Key of Pyre Flame",
        "alternate_names": "The Burning Key, the Key of Ash and Brand", 
        "attribute": "Intelligence",
        "description": "The Burning Key of Ash and Brand rules fire and extreme heat.",
        "doom": "Destroy a possession of value or suffer Extreme Heat.",
        "book": "GTS 2e p.123"
    },
    "stillness": {
        "name": "Stillness",
        "full_name": "The Key of Stillness",
        "alternate_names": "The Silent Key, the Key of Shroud and Shadow",
        "attribute": "Composure", 
        "description": "The Silent Key of Shroud and Shadow haunts those who are helpless, cornered, or caught unaware.",
        "doom": "You may not speak, dispelling your Haunt if you do.",
        "book": "GTS 2e p.124"
    }
}

# Geist template definition
GEIST_TEMPLATE = {
    "name": "geist",
    "display_name": "Geist",
    "description": "Sin-Eaters are those who have died and returned to life, bound to powerful ghosts called geists who saved them from true death.",
    "bio_fields": ["root", "bloom",  "burden", "geist_name", "krewe"],
    "integrity_name": "Synergy",
    "starting_integrity": 7,
    "supernatural_power_stat": "psyche",
    "starting_power_stat": 1,
    "resource_pool": "plasm",
    "power_systems": GEIST_ALL_POWERS,
    "anchors": ["root", "bloom"],
    "merit_categories": ["physical", "social", "mental", "supernatural", "fighting", "style", "geist"],
    "field_validations": {
        "burden": {
            "valid_values": GEIST_BURDENS
        },
        "krewe": {
            "valid_values": GEIST_KREWE_TYPES
        }
    },
    "version": "2.0",
    "author": "Chronicles of Darkness",
    "game_line": "Geist: The Sin-Eaters",
    "notes": "Enhanced Geist template with Psyche, Manifestations, Keys, and Plasm pool",
    
    # Geist-specific secondary character sheet configuration
    "geist_config": {
        "rank": 3,
        "size": 5,
        "base_attributes": {
            "power": 1,
            "finesse": 1, 
            "resistance": 1
        },
        "attribute_dots_to_assign": 12,
        "max_attribute": 9,
        "crisis_triggers": GEIST_CRISIS_TRIGGERS,
        "remembrance_skills": GEIST_REMEMBRANCE_SKILLS,
        "remembrance_merits": GEIST_REMEMBRANCE_MERITS,
        "remembrance_max_dots": 3,
        "innate_keys": GEIST_KEYS,
        "bio_fields": ["concept", "remembrance_description", "virtue", "vice", "crisis_trigger", "ban", "bane", "innate_key"]
    }
}

# Register the template
register_template(GEIST_TEMPLATE)


# Sheet Rendering Functions
def render_geist_sheet(character, caller, force_ascii=False):
    """
    Render the Geist character sheet for a Sin-Eater.
    
    Args:
        character: The character object with geist_stats
        caller: The caller (for messaging)
        force_ascii: If True, use ASCII dots instead of Unicode
        
    Returns:
        list: Lines of formatted output for the geist sheet
    """
    from evennia.utils import ansi
    
    # Check if geist stats exist
    if not hasattr(character.db, 'geist_stats') or not character.db.geist_stats:
        return None  # Signal that no geist sheet exists
    
    geist_stats = character.db.geist_stats
    
    # Determine dot characters
    if force_ascii:
        filled_char, empty_char = "*", "-"
    else:
        filled_char, empty_char = "●", "○"
    
    def format_dots(value, max_value):
        """Format dots for display"""
        filled = filled_char * value
        empty = empty_char * (max_value - value)
        return filled + empty
    
    def format_section_header(section_name):
        """Create an arrow-style section header with magenta coloring"""
        total_width = 78
        name_length = len(section_name) - 4  # Account for color codes |w and |n
        available_dash_space = total_width - name_length - 4
        left_dashes = available_dash_space // 2
        right_dashes = available_dash_space - left_dashes
        return f"|m<{'-' * left_dashes}|n {section_name} |m{'-' * right_dashes}>|n"
    
    # Build the geist sheet display with magenta color scheme
    output = []
    output.append(f"|m{'='*78}|n")  # Magenta border
    
    # Get geist concept or use default
    geist_concept = geist_stats.get("bio", {}).get("concept", f"{character.name}'s Geist")
    output.append(f"|m{geist_concept.center(78)}|n")  # Magenta text
    output.append(f"|M{'GEIST CHARACTER SHEET'.center(78)}|n")  # Bright magenta
    output.append(f"|m{'='*78}|n")
    
    # Bio Section
    output.append(format_section_header("|wBIO|n"))
    
    bio = geist_stats.get("bio", {})
    other = geist_stats.get("other", {})
    
    # Bio data with defaults
    concept = bio.get("concept", "<not set>")
    virtue = bio.get("virtue", "<not set>")
    vice = bio.get("vice", "<not set>")
    crisis_trigger = bio.get("crisis_trigger", "<not set>")
    ban = bio.get("ban", "<not set>")
    bane = bio.get("bane", "<not set>")
    innate_key = bio.get("innate_key", "<not set>")
    rank = other.get("rank", 3)
    
    # Remembrance section
    remembrance = geist_stats.get("remembrance", {})
    remembrance_desc = bio.get("remembrance_description", "<not set>")
    remembrance_trait = remembrance.get("trait", "<not set>")
    remembrance_dots = remembrance.get("dots", 0)
    remembrance_type = remembrance.get("trait_type", "")
    
    if remembrance_trait != "<not set>":
        # Show trait even if dots aren't set
        if remembrance_dots > 0:
            trait_display = f"{remembrance_trait.replace('_', ' ').title()} ({remembrance_type}) {format_dots(remembrance_dots, 3)}"
        else:
            trait_display = f"{remembrance_trait.replace('_', ' ').title()} ({remembrance_type})"
    else:
        trait_display = "<not set>"
    
    # Create bio items list for display
    short_bio_items = [
        ("Concept", concept),
        ("Rank", f"{rank}"),
        ("Virtue", virtue),
        ("Vice", vice),
        ("Crisis Trigger", crisis_trigger.title() if crisis_trigger != "<not set>" else crisis_trigger),
        ("Bane", bane),
        ("Innate Key", innate_key.title() if innate_key != "<not set>" else innate_key),
        ("Trait", trait_display)
    ]

    # long fields that need their own lines
    long_bio_items = [
        ("Ban", ban),
        ("Remembrance", remembrance_desc)
    ]
    
    # Display short bio items in two-column format
    for i in range(0, len(short_bio_items), 2):
        left_label, left_value = short_bio_items[i]
        left_text = f"{left_label:<15}: {left_value}"
        
        if i + 1 < len(short_bio_items):
            right_label, right_value = short_bio_items[i + 1]
            # Use less padding for right column labels to prevent overflow
            right_text = f"{right_label:<12}: {right_value}"
        else:
            right_text = ""
        
        left_formatted = left_text.ljust(39)
        output.append(f"{left_formatted} {right_text}")
    
    # Add newline before long bio items
    output.append("")
    
    # Display long bio items on their own lines
    for label, value in long_bio_items:
        if value != "<not set>":
            output.append(f"{label:<15}: {value}")

    
    # Geist Attributes (simplified - Power, Finesse, Resistance)
    attrs = geist_stats.get("attributes", {"power": 1, "finesse": 1, "resistance": 1})
    if attrs:
        output.append(format_section_header("|wATTRIBUTES|n"))
        
        # Format geist attributes
        power_val = attrs.get("power", 1)
        finesse_val = attrs.get("finesse", 1)
        resistance_val = attrs.get("resistance", 1)
        
        power_dots = format_dots(power_val, 9)
        finesse_dots = format_dots(finesse_val, 9)
        resistance_dots = format_dots(resistance_val, 9)
        
        output.append(f"Power          {power_dots} ({power_val})")
        output.append(f"Finesse        {finesse_dots} ({finesse_val})")
        output.append(f"Resistance     {resistance_dots} ({resistance_val})")
    
    # Keys Section
    keys = geist_stats.get("keys", {})
    output.append(format_section_header("|wKEYS|n"))
    
    if keys:
        key_list = []
        for key_name, has_key in keys.items():
            if has_key:
                key_lookup = key_name  # Keep as stored (with spaces)
                key_details = GEIST_KEY_DETAILS.get(key_lookup, {})
                full_name = key_details.get("full_name", key_name.replace("_", " ").title())
                unlock_attr = key_details.get("attribute", "")
                
                key_display = f"|c{full_name}|n"
                if unlock_attr:
                    key_display += f" (Unlock: {unlock_attr})"
                key_list.append(key_display)
        
        if key_list:
            for i, key_display in enumerate(key_list):
                output.append(f"  {key_display}")
                
                clean_key_name = key_display.split(" (")[0]
                # Remove color codes from the key name
                clean_key_name = clean_key_name.replace("|c", "").replace("|n", "").lower()
                for key_code, details in GEIST_KEY_DETAILS.items():
                    if details["full_name"].lower() == clean_key_name:
                        output.append(f"    |cDescription:|n {details['description']}")
                        output.append(f"    |rDoom:|n {details['doom']}")
                        output.append("")
                        break
        else:
            output.append("  No keys unlocked yet.")
    else:
        output.append("  No keys unlocked yet.")
    
    # Derived Stats for Geist
    advantages = geist_stats.get("advantages", {})
    output.append(format_section_header("|wADVANTAGES|n"))
    
    # Calculate derived stats if not already calculated
    if not advantages:
        defense = min(attrs.get("power", 1), attrs.get("finesse", 1))
        initiative = attrs.get("finesse", 1) + attrs.get("resistance", 1)
        speed = attrs.get("power", 1) + attrs.get("finesse", 1) + 5
        size = other.get("size", 5)
    else:
        defense = advantages.get("defense", 0)
        initiative = advantages.get("initiative", 0) 
        speed = advantages.get("speed", 0)
        size = other.get("size", 5)
    
    geist_advantages = [
        ("Defense", defense),
        ("Size", size),
        ("Initiative", initiative),
        ("Speed", speed)
    ]
    
    # Display advantages in rows of 2 columns
    for i in range(0, len(geist_advantages), 2):
        row_parts = []
        for j in range(2):
            if i + j < len(geist_advantages):
                name, value = geist_advantages[i + j]
                part = f"{name:<16} : {value}"
                row_parts.append(part.ljust(39))
            else:
                row_parts.append(" " * 39)
        output.append("".join(row_parts))
    output.append(f"|m{'='*78}|n")
    
    # Add encoding info to bottom if ASCII mode is being used
    if force_ascii:
        output.append("|g(ASCII mode active - use +sheet/geist without /ascii for Unicode)|n")
    
    return output


# Power list helper functions
def get_primary_powers():
    """Get list of primary geist powers (haunts rated 1-5)."""
    return GEIST_PRIMARY_POWERS.copy()


def get_secondary_powers():
    """Get list of secondary geist powers (keys and ceremonies - individual abilities)."""
    return GEIST_SECONDARY_POWERS.copy()


def get_all_powers():
    """Get all geist powers for validation."""
    return GEIST_ALL_POWERS.copy()


# Geist Stat Management Utilities
def initialize_geist_stats(character):
    """
    Initialize the geist stats structure for a Sin-Eater.
    
    Args:
        character: The character object
    """
    if not hasattr(character.db, 'geist_stats') or not character.db.geist_stats:
        character.db.geist_stats = {
            "attributes": {"power": 1, "finesse": 1, "resistance": 1},
            "bio": {},
            "remembrance": {},
            "keys": {},
            "haunts": {},
            "advantages": {},
            "other": {"rank": 3, "size": 5}
        }


def set_geist_stat_value(character, stat, value, caller):
    """
    Set a geist stat value with validation.
    
    Args:
        character: The character object
        stat: The stat name to set
        value: The value to set (string or int)
        caller: The caller object (for messages)
        
    Returns:
        tuple: (success, message)
    """
    # Initialize geist_stats if needed
    initialize_geist_stats(character)
    
    geist_stats = character.db.geist_stats
    
    # Get template config for validation
    from . import get_template_definition
    template_def = get_template_definition("geist")
    geist_config = template_def.get("geist_config", {}) if template_def else {}
    
    # Try to convert value to int for numeric stats
    original_value = value
    try:
        value = int(value)
    except ValueError:
        # Keep as string for non-numeric stats
        pass
    
    # Handle different stat categories
    if stat in ["power", "finesse", "resistance"]:
        # Geist attributes
        if not isinstance(value, int):
            return False, "Geist attributes must be numbers."
        
        max_attr = geist_config.get("max_attribute", 9)
        if not 1 <= value <= max_attr:
            return False, f"Geist attributes must be between 1 and {max_attr}."
        
        # Check total attribute dots (base 3 + 12 to assign = 15 total)
        current_total = sum(geist_stats["attributes"].values())
        current_value = geist_stats["attributes"].get(stat, 1)
        new_total = current_total - current_value + value
        max_total = 3 + geist_config.get("attribute_dots_to_assign", 12)
        
        if new_total > max_total:
            error_msg = f"Cannot set {stat} to {value}. Total attribute dots would be {new_total}, maximum is {max_total}.\n"
            error_msg += f"Current totals: Power {geist_stats['attributes']['power']}, Finesse {geist_stats['attributes']['finesse']}, Resistance {geist_stats['attributes']['resistance']}"
            return False, error_msg
        
        geist_stats["attributes"][stat] = value
        return True, f"Set geist's {stat} to {value}."
    
    elif stat in ["concept", "remembrance_description", "virtue", "vice", "crisis_trigger", "ban", "bane"]:
        # Bio fields (string values)
        if isinstance(value, int):
            value = original_value  # Use original string value
        
        if len(str(value)) > 100:
            return False, "Geist bio fields cannot exceed 100 characters."
        
        # Validate specific fields
        if stat == "virtue":
            geist_stats["bio"][stat] = str(value).title()
            return True, f"Set geist's virtue to {value}."
        elif stat == "vice":
            geist_stats["bio"][stat] = str(value).title()
            return True, f"Set geist's vice to {value}."
        elif stat == "crisis_trigger":
            valid_triggers = geist_config.get("crisis_triggers", [])
            if valid_triggers and value.lower() not in valid_triggers:
                return False, f"Invalid crisis trigger. Valid options: {', '.join(valid_triggers)}"
            geist_stats["bio"][stat] = str(value).lower()
            return True, f"Set geist's crisis trigger to {value}."
        else:
            geist_stats["bio"][stat] = str(value)
            return True, f"Set geist's {stat.replace('_', ' ')} to {value}."
    
    elif stat == "innate_key":
        # Innate key selection
        valid_keys = geist_config.get("innate_keys", [])
        if valid_keys and value.lower() not in valid_keys:
            return False, f"Invalid innate key. Valid options: {', '.join(valid_keys)}"
        geist_stats["bio"]["innate_key"] = str(value).lower()
        return True, f"Set geist's innate key to {value}."
    
    elif stat == "remembrance_trait":
        # Remembrance trait (skill or merit)
        if not isinstance(value, str):
            return False, "Remembrance trait must be a skill or merit name."
            
        value_lower = value.lower().replace(" ", "_")
        valid_skills = geist_config.get("remembrance_skills", [])
        valid_merits = geist_config.get("remembrance_merits", [])
        
        if value_lower not in valid_skills + valid_merits:
            error_msg = f"Invalid remembrance trait. Must be a valid skill or merit (≤3 dots).\n"
            error_msg += f"Valid skills: {', '.join(valid_skills)}\n"
            error_msg += f"Valid merits: {', '.join(valid_merits)}"
            return False, error_msg
        
        geist_stats["remembrance"]["trait"] = value_lower
        geist_stats["remembrance"]["trait_type"] = "skill" if value_lower in valid_skills else "merit"
        return True, f"Set geist's remembrance trait to {value}."
    
    elif stat == "remembrance_dots":
        # Remembrance trait dots
        if not isinstance(value, int):
            return False, "Remembrance dots must be a number."
            
        max_dots = geist_config.get("remembrance_max_dots", 3)
        if not 1 <= value <= max_dots:
            return False, f"Remembrance trait dots must be between 1 and {max_dots}."
        
        geist_stats["remembrance"]["dots"] = value
        return True, f"Set geist's remembrance dots to {value}."
    
    else:
        # Unknown stat
        error_msg = f"Unknown geist stat: {stat}\n"
        error_msg += "Valid geist stats:\n"
        error_msg += "  Attributes: power, finesse, resistance\n"
        error_msg += "  Bio: concept, remembrance_description, virtue, vice, crisis_trigger, ban, bane, innate_key\n"
        error_msg += "  Remembrance: remembrance_trait, remembrance_dots\n"
        error_msg += "  Note: For keys, use the semantic syntax: +stat key=beasts\n"
        error_msg += "  Note: For haunts, use regular numeric syntax: +stat boneyard=3"
        return False, error_msg


def calculate_geist_derived_stats(character, caller):
    """
    Calculate derived stats for a geist.
    
    Args:
        character: The character object
        caller: The caller object (for messages)
        
    Returns:
        dict: Calculated advantages
    """
    if not hasattr(character.db, 'geist_stats') or not character.db.geist_stats:
        return {}
    
    geist_stats = character.db.geist_stats
    attrs = geist_stats.get("attributes", {})
    
    # Calculate derived stats per Geist rules
    defense = min(attrs.get("power", 1), attrs.get("finesse", 1))
    initiative = attrs.get("finesse", 1) + attrs.get("resistance", 1)
    speed = attrs.get("power", 1) + attrs.get("finesse", 1) + 5
    size = geist_stats.get("other", {}).get("size", 5)
    
    # Store derived stats
    geist_stats["advantages"] = {
        "defense": defense,
        "initiative": initiative,
        "speed": speed
    }
    
    if caller:
        caller.msg(f"Recalculated geist derived stats: Defense {defense}, Initiative {initiative}, Speed {speed}")
    
    return geist_stats["advantages"] 