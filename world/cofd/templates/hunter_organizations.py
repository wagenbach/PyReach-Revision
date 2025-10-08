"""
Hunter: The Vigil - Conspiracies and Compacts
Complete listing of all organizations from Hunter the Vigil 1st Edition
including descriptions, status benefits, and book references.
"""

# ============================================================================
# COMPACTS
# ============================================================================

COMPACTS = {
    "ashwood abbey": {
        "name": "Ashwood Abbey",
        "type": "compact",
        "description": "A decadent Hellfire Club dedicated to experiencing everything that life (or unlife) has to offer.",
        "status_benefits": {
            1: "Receive the Barfly Merit.",
            3: "Use the chapterhouse as a two-dot Safehouse.",
            5: "Receive Allies •••• (Legal Aid, Vice, Arms Trafficking, and Abbey Networking)."
        },
        "book": "HTV 102",
        "tags": ["hedonistic", "wealthy", "social"]
    },
    "barrett commission": {
        "name": "The Barrett Commission",
        "type": "compact",
        "description": "A secret elite cabal united to root out the monsters entrenched in America's most gainful institutions.",
        "status_benefits": {
            1: "Gain a dot of Resources.",
            3: "Receive Mentor •••.",
            5: "Receive two dots of Contacts among government, corporations, or the military."
        },
        "book": "NS 89",
        "tags": ["elite", "corporate", "government"]
    },
    "bear lodge": {
        "name": "Bear Lodge",
        "type": "compact",
        "description": "Big game hunters dedicated to killing werewolves above everything else, proving themselves with only human ingenuity.",
        "status_benefits": {
            1: "Receive Contacts • (Bear Lodge).",
            3: "Resist Lunacy as though your Willpower was one higher.",
            5: "Receive the Unseen Sense for werewolves or other tangible quarry."
        },
        "book": "SpSl 87",
        "tags": ["werewolf hunters", "hunters", "trophy hunters"]
    },
    "division six": {
        "name": "Division Six",
        "type": "compact",
        "description": "An ersatz government agency tasked with protecting the laws of the cosmos by eliminating \"reality deviants.\"",
        "status_benefits": {
            1: "Recover an extra Willpower when risking Willpower to flaunt your authority.",
            3: "Worsen Paradoxes by one die when witnessing vulgar spells.",
            5: "Receive a trainee as a three-dot Retainer."
        },
        "book": "WF 86",
        "tags": ["mage hunters", "government", "reality police"]
    },
    "habibti ma": {
        "name": "Habibti Ma",
        "type": "compact",
        "description": "Egyptian-based cult de-programmers.",
        "status_benefits": {
            1: "Distribute two dots between Allies and Contacts.",
            3: "Distribute two dots between Allies and Mentor.",
            5: "Distribute two dots between Mystery Cult Initiation and Retainer."
        },
        "book": "HMR 107",
        "tags": ["cult deprogrammers", "egyptian", "social"]
    },
    "heritage house": {
        "name": "Heritage House",
        "type": "compact",
        "description": "A family oriented group that believes the Vigil should be passed down from generation to generation.",
        "status_benefits": {
            1: "Trial member.",
            3: "Gain two dots of Resources.",
            5: "Gain three dots of Social Merits."
        },
        "book": "GotU 35",
        "tags": ["family", "legacy", "generational"]
    },
    "hunt club": {
        "name": "The Hunt Club",
        "type": "compact",
        "description": "A secret society of serial killers that hunts people for sport, accumulating points in a twisted game.",
        "status_benefits": {
            1: "Receive a one-dot Mentor.",
            3: "Receive or upgrade the Telltale Murder Merit.",
            5: "Receive or upgrade Damnable Certainty."
        },
        "book": "Slash 74",
        "tags": ["serial killers", "dark", "hunting game"]
    },
    "illuminated brotherhood": {
        "name": "The Illuminated Brotherhood",
        "type": "compact",
        "description": "Unfettering their minds with psychoactives, these mediums seek to interact with the spirit world.",
        "status_benefits": {
            1: "Gain an Occult or Science specialty in parapsychology.",
            3: "Receive the Unseen Sense for spirit loci.",
            5: "Receive the Natural Medium Merit."
        },
        "book": "SpSl 92",
        "tags": ["spirit hunters", "mediums", "psychedelics"]
    },
    "keepers of the source": {
        "name": "The Keepers of the Source",
        "type": "compact",
        "description": "Every time a witch siphons power from Mother Earth, the Keepers feel Her pain, and they will see it cease.",
        "status_benefits": {
            1: "Gain a specialty in Weaponry (Improvised Weapons), Expression (Protests), or Science (Environmentalism).",
            3: "Gain two dots of Allies (Keepers of the Source).",
            5: "Gain the Unseen Sense for the Source, or three dots of Mentor."
        },
        "book": "WF 90",
        "tags": ["witch hunters", "environmentalists", "activists"]
    },
    "long night": {
        "name": "The Long Night",
        "type": "compact",
        "description": "Religious hunters who fight the agents of evil in an attempt to bring about the second coming of Christ.",
        "status_benefits": {
            1: "Receive an Expression or Persuasion specialty in evangelism.",
            3: "Gain two dots of Allies (Long Night).",
            5: "Add the benefits of the Inspiring Merit among the Long Night."
        },
        "book": "HTV 106",
        "tags": ["religious", "christian", "evangelical"]
    },
    "loyalists of thule": {
        "name": "The Loyalists of Thule",
        "type": "compact",
        "description": "Hungry for knowledge, this occult group seeks things man was not meant to know in places he was not meant to tread to atone for their part in WWII.",
        "status_benefits": {
            1: "Recover an extra Willpower when risking Willpower with Academics or Occult.",
            3: "Receive a two-dot Mentor.",
            5: "Receive three dots of Contacts among supernatural specialists."
        },
        "book": "HTV 110",
        "tags": ["occult", "knowledge seekers", "german"]
    },
    "maidens blood sisterhood": {
        "name": "Maiden's Blood Sisterhood",
        "type": "compact",
        "description": "An almost exclusively female group, dedicated to policing college campuses and women's shelters.",
        "status_benefits": {
            1: "Gain two dots of Allies (Maiden's Blood Sisterhood).",
            3: "Gain two dots of Safehouse.",
            5: "Receive the Indomitable Merit, or two dots of Retainers."
        },
        "book": "NS 93",
        "tags": ["women", "protectors", "campus"]
    },
    "network zero": {
        "name": "Network Zero",
        "type": "compact",
        "description": "Network Zero uses radio, television and Internet resources to publicize monsters to the world.",
        "status_benefits": {
            1: "Gain a Crafts or Expression specialty in an appropriate medium.",
            3: "Receive Fame ••.",
            5: "Benefit from the effects of Encyclopedic Knowledge as pertains your library of recorded supernatural phenomena."
        },
        "book": "HTV 114",
        "tags": ["media", "internet", "publicity"]
    },
    "night watch": {
        "name": "The Night Watch",
        "type": "compact",
        "description": "Vigilantes of the hard and forgotten streets, patrolling the hunting grounds of the monsters and criminals, leaving no one to be victimized.",
        "status_benefits": {
            1: "Receive a specialty in Streetwise (Who's Who), Larceny (Fences), or Stealth (Stalking).",
            3: "Gain two dots of Retainers.",
            5: "Gain a dot of Fame."
        },
        "book": "NS 98",
        "tags": ["vigilantes", "street level", "urban"]
    },
    "null mysteriis": {
        "name": "Null Mysteriis",
        "type": "compact",
        "description": "Scientists who peruse the supernatural in an attempt to understand it.",
        "status_benefits": {
            1: "Receive an Academics, Occult, or Science specialty in parapsychology.",
            3: "Gain a dot of Allies (Null Mysteriis) and a dot of Contacts in science or academia.",
            5: "Apply the benefits of Common Sense as pertains to the Vigil."
        },
        "book": "HTV 118",
        "tags": ["scientists", "researchers", "rational"]
    },
    "promethean brotherhood": {
        "name": "The Promethean Brotherhood",
        "type": "compact",
        "description": "Sacrificing witches using an ancient ritual, they steal their power for themselves.",
        "status_benefits": {
            1: "Receive Language (Ancient Greek) and an Academics specialty in ancient religions, Greek mythology, or linguistics.",
            3: "Gain two dots of Allies (Promethean Brotherhood).",
            5: "Divide the target number of successes for the Rite of Hecate by three."
        },
        "book": "WF 94",
        "tags": ["witch hunters", "ritualists", "greek"]
    },
    "reckoning": {
        "name": "The Reckoning",
        "type": "compact",
        "description": "Church of Hero-hunting \"sovereign citizens\" deep in the wooded hills of Oregon.",
        "status_benefits": {
            1: "Receive a dot of Anonymity and access to a shared one-dot Safe Place.",
            3: "Receive Allies •••• (Fundamentalist Politicians).",
            5: "Resources •••••, exclusive to the leader, Derek Campbell."
        },
        "book": "T&N 32",
        "tags": ["sovereign citizens", "fundamentalist", "heroes"]
    },
    "talbot group": {
        "name": "The Talbot Group",
        "type": "compact",
        "description": "Using modern therapy and medications, these hunters seek to save monsters from themselves.",
        "status_benefits": {
            1: "Gain a dot each in Allies and Contacts (Talbot Group).",
            3: "Gain another dot of Contacts and receive the Unseen Sense for spirits.",
            5: "Resist Lunacy as though your Willpower was one higher."
        },
        "book": "SpSl 97",
        "tags": ["therapists", "rehabilitation", "compassionate"]
    },
    "union": {
        "name": "The Union",
        "type": "compact",
        "description": "Ragtag blue-collar monster hunters, members of the Union work without government sanction to protect humanity against its most dangerous enemies.",
        "status_benefits": {
            1: "Receive a Politics or Streetwise specialty in your local area.",
            3: "Gain two dots of Contacts among specialists in different kinds of monster.",
            5: "Access two extra dots of Resources for Vigil purposes."
        },
        "book": "HTV 112",
        "tags": ["blue collar", "working class", "independent"]
    },
    "utopia now": {
        "name": "Utopia Now",
        "type": "compact",
        "description": "Builders of a futuristic city that scavenge demonic infrastructure for impossible components.",
        "status_benefits": {
            1: "Take a free Specialty.",
            3: "Receive a two-dot Mentor.",
            5: "Receive either a four-dot Retainer or four dots of Allies in a partner organization."
        },
        "book": "HMR 136",
        "tags": ["futurists", "demon hunters", "builders"]
    },
    "yuris group": {
        "name": "Yuri's Group",
        "type": "compact",
        "description": "Social workers fighting abuse and supernatural abusers.",
        "status_benefits": {
            1: "Gain a dot each of Contacts and Allies among local support groups.",
            3: "Divide three dots between Retainers and Staff of survivors.",
            5: "Rescued survivors may function as one-dot Retainers, Allies, Contacts, or Staff."
        },
        "book": "T&N 30",
        "tags": ["social workers", "abuse survivors", "support"]
    },
}

# ============================================================================
# HISTORICAL COMPACTS
# ============================================================================

HISTORICAL_COMPACTS = {
    "ahl al-jabal": {
        "name": "Ahl al-Jabal",
        "type": "historical_compact",
        "description": "Islamic hunters who seek to understand the supernaturals they meet, and eliminate those that are true monsters.",
        "status_benefits": {
            1: "You can buy the Two Weapon Fighting Style at half cost, ignoring prerequisites.",
            3: "Receive a dot of Allies and an Occult specialty in mysticism, gnosticism or philosophy.",
            5: "Add the benefits of the Inspiring Merit among the Ahl al-Jabal."
        },
        "book": "AB 141",
        "tags": ["islamic", "historical", "philosophers"]
    },
    "ama-san": {
        "name": "Ama-san",
        "type": "historical_compact",
        "description": "Pearl divers familiar with the dangers that lurk off the coasts of Japan.",
        "status_benefits": {
            1: "Receive Small Unit Tactics.",
            3: "Roll Presence + Occult to call a monster out with a special whistling breath.",
            5: "Call six dots worth of Retainers as emergency backup."
        },
        "book": "DE 309",
        "tags": ["japanese", "pearl divers", "coastal"]
    },
    "azusa miko": {
        "name": "Azusa Miko",
        "type": "historical_compact",
        "description": "Transient archer-priestesses plying their trade as oracles and mediums while driving corruption away from the divine.",
        "status_benefits": {
            1: "Receive the Medium Merit.",
            3: "Apply a floating dot as temporary Allies, Contacts, Resources, or Retainer.",
            5: "Command the fear of lesser spirits and ghosts, and the respect of the greater."
        },
        "book": "DE 311",
        "tags": ["japanese", "priestesses", "archers", "mediums"]
    },
    "bijin": {
        "name": "Bijin",
        "type": "historical_compact",
        "description": "Artists and commercial hosts dealing with monstrous intrusions that are bad for business.",
        "status_benefits": {
            1: "Draw upon the rumor mill once per session.",
            3: "Better distinguish true rumors from scuttlebutt.",
            5: "Receive Fame •••."
        },
        "book": "DE 313",
        "tags": ["japanese", "artists", "hosts", "social"]
    },
    "followers of the mansa": {
        "name": "Followers of the Mansa",
        "type": "historical_compact",
        "description": "Scribes and workers seeking to subvert and undo the plans of demons in the Empire of Mali.",
        "status_benefits": {
            1: "Receive an Expression or Politics specialty suitable to your official standing.",
            3: "Gain two dots of Allies (Followers of the Mansa).",
            5: "Gain three dots of Resources."
        },
        "book": "DE2 182",
        "tags": ["mali", "scribes", "demon hunters"]
    },
    "keepers of the weave": {
        "name": "Keepers of the Weave",
        "type": "historical_compact",
        "description": "An Amerindian culture of storytellers who gather and spread knowledge of the occult.",
        "status_benefits": {
            1: "Take two dots of Mentor, and either a third dot or a Language.",
            3: "Receive two dots in Occult, Expression, or Politics.",
            5: "Receive three dots in Socialize or Occult, or four Allies or Contacts."
        },
        "book": "DE 383",
        "tags": ["amerindian", "storytellers", "knowledge"]
    },
    "protectors of the light": {
        "name": "Protectors of the Light",
        "type": "historical_compact",
        "description": "Secret soldiers who keep the Wampanoag Nation clean of monstrous taint.",
        "status_benefits": {
            1: "Receive a dot of Occult, Survival or Weaponry.",
            3: "Receive two dots of Resources or Contacts.",
            5: "Receive three dots of Resources or Safe Place, or two Allies and a Contact."
        },
        "book": "DE 385",
        "tags": ["wampanoag", "soldiers", "native american"]
    },
    "scarlet watch": {
        "name": "The Scarlet Watch",
        "type": "historical_compact",
        "description": "A recurring blood pact of families drawn together mystically to resist the vampiric Curse.",
        "status_benefits": {
            1: "Gain a dot of Allies or Resources.",
            3: "Gain two dots of Allies or Resources.",
            5: "Receive three dots' worth of Merits reflecting your storied lineage."
        },
        "book": "DE 379",
        "tags": ["vampire hunters", "blood pact", "families"]
    },
    "soldiers of the forbidden sun": {
        "name": "Soldiers of the Forbidden Sun",
        "type": "historical_compact",
        "description": "Soldiers of many ethnicities protecting China from the Underworld.",
        "status_benefits": {
            1: "Gain a dot of Occult.",
            3: "Gain two dots of Resources.",
            5: "Gain three dots of Allies (Soldiers of the Forbidden Sun)."
        },
        "book": "DE2 247",
        "tags": ["chinese", "underworld hunters", "soldiers"]
    },
    "les voyageurs": {
        "name": "Les Voyageurs",
        "type": "historical_compact",
        "description": "Forest runners dealing with the threat of werewolves in their hunting lands.",
        "status_benefits": {
            1: "Receive Resources • or Mentor •••.",
            3: "Gain two dots of Contacts, Fame, or Resources.",
            5: "Receive three dots of Fame or Resources, or four dots of Allies."
        },
        "book": "DE 381",
        "tags": ["french canadian", "werewolf hunters", "trappers"]
    },
}

# ============================================================================
# CONSPIRACIES
# ============================================================================

CONSPIRACIES = {
    "aegis kai doru": {
        "name": "Aegis Kai Doru",
        "type": "conspiracy",
        "description": "Greek for \"Shield and Spear,\" the Aegis Kai Doru searches the world for history's legendary artifacts with which to bolster its numbers in its nigh-timeless battle against the forces of darkness.",
        "endowment": "Relic",
        "status_benefits": {
            1: "Acquire Relic Endowments.",
            3: "+1 Academics bonus to rolls involving relics and archaeology.",
            5: "Receive the Unseen Sense for mages or werewolves."
        },
        "book": "HTV 126",
        "tags": ["relics", "artifacts", "ancient", "greek"]
    },
    "ascending ones": {
        "name": "Ascending Ones",
        "type": "conspiracy",
        "description": "The Ascending Ones trace their history and symbology back to both ancient Egypt and Muhammed the Prophet. Like the sacred sun, they see themselves as a cleansing agent that can burn away monstrous impurities.",
        "endowment": "Elixir",
        "status_benefits": {
            1: "Develop the Elixir Endowment.",
            3: "Gain two dots of Resources.",
            5: "Receive a three-dot Retainer."
        },
        "book": "HTV 130",
        "tags": ["alchemists", "egyptian", "islamic", "elixirs"]
    },
    "cainite heresy": {
        "name": "The Cainite Heresy",
        "type": "conspiracy",
        "description": "Self-destructive fanatics driven by their need for revenge against vampires, wherever they may be found.",
        "endowment": "Rites of Denial",
        "status_benefits": {
            1: "Learn the Rites of Denial Endowment.",
            3: "Add the benefits of Danger Sense against vampires.",
            5: "Receive contact with anonymous sources as a three-dot Mentor."
        },
        "book": "NS 103",
        "tags": ["vampire hunters", "fanatics", "self-destructive"]
    },
    "cheiron group": {
        "name": "The Cheiron Group",
        "type": "conspiracy",
        "description": "A medical conglomerate which secretly dispatches hunters to harvest monsters for parts.",
        "endowment": "Thaumatechnology",
        "status_benefits": {
            1: "Acquire Thaumatechnology Endowments.",
            3: "Call on Allies •• corporate backup.",
            5: "Gain three dots of Resources."
        },
        "book": "HTV 134",
        "tags": ["corporate", "medical", "harvesting", "implants"]
    },
    "faithful of shulpae": {
        "name": "The Faithful of Shulpae",
        "type": "conspiracy",
        "description": "Cannibal cultists who believe their rituals bring them closer to communion with their deity.",
        "endowment": "Anthropophagy",
        "status_benefits": {
            1: "Learn the Anthropophagy Endowment.",
            3: "Use a temple as a two-dot Safehouse.",
            5: "Gain four dots of Supernatural Merits."
        },
        "book": "HMR 110",
        "tags": ["cannibals", "cultists", "mesopotamian", "dark"]
    },
    "knights of st adrian": {
        "name": "The Knights of St. Adrian",
        "type": "conspiracy",
        "description": "Violent road warriors who hunt bounties for angels.",
        "endowment": "Ink",
        "status_benefits": {
            1: "Acquire Ink Endowments.",
            3: "Receive two dots of Contacts among witnesses to the demonic.",
            5: "Gain three dots of Resources or a three-dot Retainer."
        },
        "book": "HMR 137",
        "tags": ["road warriors", "angelic", "tattoos", "demon hunters"]
    },
    "knights of saint george": {
        "name": "The Knights of Saint George",
        "type": "conspiracy",
        "description": "A cult of witch-hunters who appease faceless angels to preserve the world under the false guise of Christian worship.",
        "endowment": "Goetic Gospel",
        "status_benefits": {
            1: "Learn Goetic Gospel Endowments.",
            3: "Occult rolls dealing with witches and witchcraft gain 9-Again.",
            5: "Call on squires as three-dot Retainers."
        },
        "book": "WF 99",
        "tags": ["witch hunters", "angels", "christian", "goetic"]
    },
    "merrick institute": {
        "name": "The Merrick Institute",
        "type": "conspiracy",
        "description": "Rebel survivors of a secret government program to produce \"dream warriors.\"",
        "endowment": "Dreamscape",
        "status_benefits": {
            1: "Develop Dreamscape Endowments and receive \"The Procedure\" Tactic.",
            3: "Gain a dot each of Allies, Contacts, and Retainer among institute members.",
            5: "Receive the Easy Out, Easy In Merit."
        },
        "book": "T&N 34",
        "tags": ["dreams", "government experiments", "psychics"]
    },
    "les mysteres": {
        "name": "Les Mystères",
        "type": "conspiracy",
        "description": "A network of mediums and spirit cults who seek a relationship with spirits recognizing reciprocal duties to one another.",
        "endowment": "Rites du Cheval",
        "status_benefits": {
            1: "Learn Rites du Cheval Endowments.",
            3: {
                "fellowship": "Gain two dots of Allies.",
                "spirit": "Add +1 to Occult rolls involving spirits.",
                "beasts": "Gain two dots of Contacts among specialists in monsters.",
                "soul": "Add +1 to Resolve when resisting supernatural influence."
            },
            5: "Receive student apprentices as three-dot Retainers."
        },
        "book": "SpSl 104",
        "tags": ["spirits", "voodoo", "mediums", "possession"]
    },
    "lucifuge": {
        "name": "The Lucifuge",
        "type": "conspiracy",
        "description": "Descendants of infernal bloodlines who strive to wield the darkness against itself.",
        "endowment": "Castigation",
        "status_benefits": {
            1: "Develop the Castigation Endowment.",
            3: "Gain two dots of Resources.",
            5: "Receive the Lady Lucifuge as a four-dot Mentor."
        },
        "book": "HTV 138",
        "tags": ["infernal", "demonic blood", "darkness"]
    },
    "malleus maleficarum": {
        "name": "Malleus Maleficarum",
        "type": "conspiracy",
        "description": "In the Middle Ages, the Malleus Maleficarum wielded the power of the Church against vampires. Today, the Catholic conspiracy pursues supernatural monsters of all sorts with religious zeal.",
        "endowment": "Benediction",
        "status_benefits": {
            1: "Learn Benediction Endowments.",
            3: "Gain a dot of Status (Roman Catholic Church).",
            5: "Gain three dots of Resources."
        },
        "book": "HTV 143",
        "tags": ["catholic", "religious", "witch hunters", "inquisition"]
    },
    "task force: valkyrie": {
        "name": "Task Force: VALKYRIE",
        "type": "conspiracy",
        "description": "As part of a Joint Task Force, this covert government anti-monster brigade includes members from every branch of the military, foreign and domestic.",
        "endowment": "Advanced Armory",
        "status_benefits": {
            1: "Acquire Advanced Armory Endowments.",
            3: "Call on Allies •• tactical backup.",
            5: "Gain three dots of Contacts among federal agencies."
        },
        "book": "HTV 146",
        "tags": ["military", "government", "tactical", "advanced weapons"]
    },
    "vanguard serial crimes unit": {
        "name": "Vanguard Serial Crimes Unit",
        "type": "conspiracy",
        "description": "The agents of VASCU assist police investigations and apprehension of supernatural killers, using induced psychic abilities.",
        "endowment": "Teleinformatics",
        "status_benefits": {
            1: "Develop the Teleinformatics Endowment.",
            3: "Gain a dot of Status (FBI).",
            5: "Add the benefits of the Inspiring Merit among VASCU agents."
        },
        "book": "Slash 56",
        "tags": ["fbi", "psychics", "serial killers", "police"]
    },
}

# ============================================================================
# HISTORICAL CONSPIRACIES
# ============================================================================

HISTORICAL_CONSPIRACIES = {
    "aves minerva": {
        "name": "Aves Minerva",
        "type": "historical_conspiracy",
        "description": "Late Roman worshippers of the goddess Minerva, wielding the secrets of consecrated blood to protect Rome from monstrous infestation.",
        "endowment": "Red Rituals",
        "status_benefits": {
            1: "Learn the Red Rituals Endowment.",
            3: "+2 bonus to exercise learning to recognize the supernatural and their works.",
            5: "Receive Encyclopedic Knowledge by studying the Library of the Owl."
        },
        "book": "Pater 6",
        "tags": ["roman", "minerva", "blood rituals", "ancient"]
    },
    "hototogisu": {
        "name": "Hototogisu",
        "type": "historical_conspiracy",
        "description": "Merchants and traders shrewd enough to gamble with the darkness to remain competitive.",
        "endowment": "Settō",
        "status_benefits": {
            1: "Learn the Settō Endowment.",
            3: "Distribute four dots among Contacts, Resources and Retainers.",
            5: "Receive a five-dot Dread Power from Inoue."
        },
        "book": "DE 315",
        "tags": ["japanese", "merchants", "traders", "dark deals"]
    },
    "otodo": {
        "name": "Otodo",
        "type": "historical_conspiracy",
        "description": "Descendants of oni duty-bound to harness their devilish blood for good.",
        "endowment": "Seitokuten",
        "status_benefits": {
            1: "Develop the Seitokuten Endowment and receive the Unseen Sense for oni.",
            3: "Gain a dot each of Contacts and Resources.",
            5: "Extend the Unseen Sense to all supernatural phenomena."
        },
        "book": "DE 317",
        "tags": ["japanese", "oni", "demonic blood", "duty"]
    },
}

# ============================================================================
# BOOK ABBREVIATIONS
# ============================================================================

BOOK_ABBREVIATIONS = {
    "HTV": "Hunter: The Vigil",
    "NS": "Night Stalkers",
    "SpSl": "Spirit Slayers",
    "WF": "Witch Finders",
    "GotU": "Glimpse of the Unknown",
    "Slash": "Slasher",
    "HMR": "Mortal Remains",
    "T&N": "Tooth and Nail",
    "AB": "Block by Bloody Block",
    "DE": "Dark Eras",
    "DE2": "Dark Eras 2",
    "Pater": "Redlines: Pater Noster",
}

# ============================================================================
# HELPER FUNCTIONS
# ============================================================================

def get_organization(org_name):
    """
    Look up an organization by name (case-insensitive).
    Returns the organization data or None if not found.
    """
    org_key = org_name.lower().strip()
    
    # Check all organization types
    all_orgs = {
        **COMPACTS,
        **HISTORICAL_COMPACTS,
        **CONSPIRACIES,
        **HISTORICAL_CONSPIRACIES
    }
    
    return all_orgs.get(org_key)

def get_organizations_by_type(org_type):
    """
    Get all organizations of a specific type.
    Valid types: 'compact', 'conspiracy', 'historical_compact', 'historical_conspiracy'
    """
    type_map = {
        "compact": COMPACTS,
        "historical_compact": HISTORICAL_COMPACTS,
        "conspiracy": CONSPIRACIES,
        "historical_conspiracy": HISTORICAL_CONSPIRACIES
    }
    
    return type_map.get(org_type.lower(), {})

def get_organizations_by_tag(tag):
    """
    Get all organizations with a specific tag.
    """
    all_orgs = {
        **COMPACTS,
        **HISTORICAL_COMPACTS,
        **CONSPIRACIES,
        **HISTORICAL_CONSPIRACIES
    }
    
    matching_orgs = {}
    for key, org_data in all_orgs.items():
        if tag.lower() in [t.lower() for t in org_data.get("tags", [])]:
            matching_orgs[key] = org_data
    
    return matching_orgs

def get_all_organizations():
    """
    Get all organizations (compacts and conspiracies, both current and historical).
    """
    return {
        **COMPACTS,
        **HISTORICAL_COMPACTS,
        **CONSPIRACIES,
        **HISTORICAL_CONSPIRACIES
    }

def format_status_benefits(org_data):
    """
    Format status benefits for display.
    """
    benefits = org_data.get("status_benefits", {})
    formatted = []
    
    for level, benefit in sorted(benefits.items()):
        if isinstance(benefit, dict):
            formatted.append(f"Status {level}:")
            for key, value in benefit.items():
                formatted.append(f"  • {key.title()}: {value}")
        else:
            formatted.append(f"Status {level}: {benefit}")
    
    return "\n".join(formatted)

def get_organization_summary(org_name):
    """
    Get a formatted summary of an organization.
    """
    org_data = get_organization(org_name)
    if not org_data:
        return f"Organization '{org_name}' not found."
    
    summary = []
    summary.append(f"=== {org_data['name']} ===")
    summary.append(f"Type: {org_data['type'].replace('_', ' ').title()}")
    summary.append(f"\nDescription: {org_data['description']}")
    
    if "endowment" in org_data:
        summary.append(f"\nEndowment: {org_data['endowment']}")
    
    summary.append(f"\nStatus Benefits:")
    summary.append(format_status_benefits(org_data))
    
    summary.append(f"\nSource: {org_data['book']}")
    
    if "tags" in org_data:
        summary.append(f"Tags: {', '.join(org_data['tags'])}")
    
    return "\n".join(summary)

# ============================================================================
# ORGANIZATION LISTS FOR VALIDATION
# ============================================================================

# All valid organization names for validation
ALL_ORGANIZATIONS = list(get_all_organizations().keys())

# All conspiracy names
ALL_CONSPIRACIES = list(CONSPIRACIES.keys()) + list(HISTORICAL_CONSPIRACIES.keys())

# All compact names
ALL_COMPACTS = list(COMPACTS.keys()) + list(HISTORICAL_COMPACTS.keys())

