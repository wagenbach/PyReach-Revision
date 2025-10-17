"""
Changeling Kith Data for Chronicles of Darkness 2nd Edition.

Kith data including skills, descriptions, blessings, and sources.
Based on Changeling: The Lost 2nd Edition core book, Kith & Kin, and Dark Eras 2.
"""

ALL_KITHS = {
    # Base Changeling: The Lost 2nd Edition kiths
    "artist": {
        "name": "Artist",
        "skill": "Crafts",
        "description": "Creators whose bodies have become one with their medium.",
        "blessing": "Spend Glamour to manifest tools for a Crafts specialty, using your Wyrd as an equipment bonus.",
        "book": "CTL 2e 51"
    },
    "bright_one": {
        "name": "Bright One",
        "skill": "Socialize",
        "description": "Glowing and radiant, lit by the inner flame of their channeled passion.",
        "blessing": "Illumination concealed by the Mask. Spend Glamour for a blinding flash, inflicting bashing damage and a -2 Physical and Mental penalty for a turn.",
        "book": "CTL 2e 52"
    },
    "chatelaine": {
        "name": "Chatelaine",
        "skill": "Empathy",
        "description": "Products of endless drilling in protocol and domestic service.",
        "blessing": "Spend Glamour and roll Manipulation + Socialize to wield another character's Social Merits, in ways remembered as the character's own doing.",
        "book": "CTL 2e 52"
    },
    "gristlegrinder": {
        "name": "Gristlegrinder",
        "skill": "Brawl",
        "description": "Monsters consumed by hunger and haunted by the taste of flesh.",
        "blessing": "Bite for lethal damage without grappling. Spend Glamour and roll Stamina + Survival to swallow something or someone with a smaller Size whole.",
        "book": "CTL 2e 53"
    },
    "helldiver": {
        "name": "Helldiver",
        "skill": "Larceny",
        "description": "Spies and explorers, not free until they break the silver cord anchoring them to Faerie.",
        "blessing": "Spend Glamour and roll Dexterity + Occult to fade over several seconds between matter and the ephemeral state of a Hedge ghost.",
        "book": "CTL 2e 53"
    },
    "hunterheart": {
        "name": "Hunterheart",
        "skill": "Investigation",
        "description": "Hunters escaped from a Durance of bloody predation.",
        "blessing": "Spend Glamour and contest Presence + Wyrd vs Composure + Tolerance to freeze or send fleeing with your gaze.",
        "book": "CTL 2e 54"
    },
    "leechfinger": {
        "name": "Leechfinger",
        "skill": "Medicine",
        "description": "Secret parasites who drain the life force from others.",
        "blessing": "Spend Glamour in physical contact to inflict a point of bashing damage and downgrade a point of your own damage, or inflict and downgrade two points against a changeling.",
        "book": "CTL 2e 55"
    },
    "mirrorskin": {
        "name": "Mirrorskin",
        "skill": "Stealth",
        "description": "Those whose Durance taught them to empty themselves of their nature, becoming anybody and nobody.",
        "blessing": "Spend Glamour and roll Wits + Subterfuge + Wyrd to remold yourself, both Mask and mien.",
        "book": "CTL 2e 55"
    },
    "nightsinger": {
        "name": "Nightsinger",
        "skill": "Expression",
        "description": "Sirens and vocalists whose songs once moved the earth of Faerie.",
        "blessing": "Spend Glamour and contest Presence + Expression + Wyrd vs Composure + Tolerance to root an audience rapt to the spot.",
        "book": "CTL 2e 56"
    },
    "notary": {
        "name": "Notary",
        "skill": "Politics",
        "description": "Humans used as documents to write the oaths of the Gentry upon, with perfect knowledge of all the oath's clauses.",
        "blessing": "Once a session, preside over a pledge to negate its Glamour cost and memorize its terms.",
        "book": "CTL 2e 57"
    },
    "playmate": {
        "name": "Playmate",
        "skill": "Persuasion",
        "description": "Friends, pets and toys who lived by love and trust even in Faerie.",
        "blessing": "Spend Glamour to heal a subject of non-aggravated damage, assuming it yourself as Clarity damage.",
        "book": "CTL 2e 57"
    },
    "snowskin": {
        "name": "Snowskin",
        "skill": "Subterfuge",
        "description": "Those who escaped the grip of Faerie by smothering the warmth within and freezing solid.",
        "blessing": "Spend Glamour and contest Presence + Intimidation + Wyrd vs Composure + Tolerance to shut someone down, leaving them Shaken and on the outs with fae society.",
        "book": "CTL 2e 58"
    },
    
    # Kith & Kin - Crown kiths
    "absinthial": {
        "name": "Absinthial",
        "skill": "Crafts",
        "description": "Green fairies who distill the dream-brews of Arcadia.",
        "blessing": "Once per scene, spend Glamour and roll Presence + Crafts vs Composure + Tolerance to incapacitate with the fog of dreams.",
        "book": "Kith 88"
    },
    "climacteric": {
        "name": "Climacteric",
        "skill": "Investigation",
        "description": "Weather-clocks and forecasters who captured time with the elements.",
        "blessing": "At the outset of Initiative, spend Glamour to push someone else to act first of all.",
        "book": "Kith 88"
    },
    "concubus": {
        "name": "Concubus",
        "skill": "Empathy",
        "description": "Nightly companions and dreamweavers tending the minds of the Others.",
        "blessing": "Heal a dreamer's mental Conditions with a series of oneiromantic paradigm shifts.",
        "book": "Kith 89"
    },
    "draconic": {
        "name": "Draconic",
        "skill": "Brawl/Weaponry",
        "description": "Changelings who evolved into grandiose guardian beasts.",
        "blessing": "Spend Glamour to fly for your Wyrd in turns, or while your Mask is stripped bare to scare others into fleeing.",
        "book": "Kith 90"
    },
    "flowering": {
        "name": "Flowering",
        "skill": "Socialize",
        "description": "These Lost lived amid Arcadian flora and adopted their passive allure.",
        "blessing": "Spend Glamour and roll Presence + Empathy to release a perfumed scent. Those present must contest with Composure + Tolerance or fall vulnerable to your sway.",
        "book": "Kith 90"
    },
    "ghostheart": {
        "name": "Ghostheart",
        "skill": "Perception",
        "description": "Psychopomps and gravediggers sent to tend the dead.",
        "blessing": "Receive three dots' worth of ghostly Allies with handpicked Numina.",
        "book": "Kith 91"
    },
    "moonborn": {
        "name": "Moonborn",
        "skill": "Empathy/Intimidation",
        "description": "Lost roused to wild and restless passions for their Keepers' entertainment.",
        "blessing": "Once per chapter, incite bedlam at no Willpower cost, substituting Expression for your Wyrd.",
        "book": "Kith 92"
    },
    "uttervoice": {
        "name": "Uttervoice",
        "skill": "Intimidation",
        "description": "Changelings whose frustrations have sharpened their voice into a deadly blade.",
        "blessing": "Spend Glamour and contest Presence + Wyrd vs Composure + Tolerance to inflict a bashing wound and shatter glass by voice alone. Presence actions may involuntarily trigger the voice.",
        "book": "Kith 92"
    },
    
    # Kith & Kin - Jewels kiths
    "delver": {
        "name": "Delver",
        "skill": "Investigation",
        "description": "Miners of precious things.",
        "blessing": "Spend Glamour to send a message to any number of people within Wyrd miles, or to decode such messages.",
        "book": "Kith 93"
    },
    "glimmerwisp": {
        "name": "Glimmerwisp",
        "skill": "Persuasion",
        "description": "Fogs and mists of Faerie, concealing shameful and monstrous actions.",
        "blessing": "Spend a Glamour to create a perfumed mist. Those present must contest with Resolve + Composure against your Manipulation + Persuasion + Wyrd or shameful actions and breaking points are hidden to them.",
        "book": "Kith 94"
    },
    "gremlin": {
        "name": "Gremlin",
        "skill": "Crafts",
        "description": "Perfectionists that impulsively destroy flawed creations.",
        "blessing": "Once per scene, spend a Glamour turn an extended action into an instant action if it involves tearing down or destroying something.",
        "book": "Kith 94"
    },
    "manikin": {
        "name": "Manikin",
        "skill": "Socialize",
        "description": "Canvas for the Gentry's art.",
        "blessing": "Spend glamour and roll Presence + Crafts to increase the apparent quality of objects for the purposes of social rolls, and to make any outfit look good.",
        "book": "Kith 95"
    },
    "oculus": {
        "name": "Oculus",
        "skill": "Persuasion",
        "description": "Diplomats and bargainers skilled at making others see their perspective.",
        "blessing": "Spend glamour and roll Presence + Persuasion + Wyrd contested by Resolve + Tolerance to make your own path the only option.",
        "book": "Kith 95"
    },
    "polychromatic": {
        "name": "Polychromatic",
        "skill": "Empathy",
        "description": "Colorful and flashy, with a talent for stirring and soothing emotions.",
        "blessing": "Once per chapter, spend glamour to create a swirl of colors that gives the Swooned condition and penalize attempts to resist your Empathy rolls.",
        "book": "Kith 96"
    },
    "veneficus": {
        "name": "Veneficus",
        "skill": "Survival",
        "description": "Herbalists and cooks of faerie.",
        "blessing": "Spend Glamour to make a toxic plant edible or an edible plant toxic.",
        "book": "Kith 97"
    },
    "witchtooth": {
        "name": "Witchtooth",
        "skill": "Intimidation",
        "description": "Reclusive hermits who know the power of the land.",
        "blessing": "Spend glamour and roll Resolve + Intimidation to reshape the land and penalize survival rolls.",
        "book": "Kith 97"
    },
    
    # Kith & Kin - Mirror kiths
    "bricoleur": {
        "name": "Bricoleur",
        "skill": "Crafts/Expression",
        "description": "Clever manipulators of symbolism and connections.",
        "blessing": "With an appropriate item on hand, spend Glamour and roll Wits + Persuasion to change a core truth about yourself for a number of days equal to your Wyrd.",
        "book": "Kith 98"
    },
    "cloakskin": {
        "name": "Cloakskin",
        "skill": "Social",
        "description": "Lonely Lost with an invisible Mask.",
        "blessing": "Spend Glamour to also make your Mien invisible with a successful Presence+Stealth+Wyrd roll.",
        "book": "Kith 98"
    },
    "doppelganger": {
        "name": "Doppelganger",
        "skill": "Empathy",
        "description": "Thieves of familiar traits.",
        "blessing": "Spend Glamour to temporarily steal someone's visual or auditory traits and add them to your Mask.",
        "book": "Kith 99"
    },
    "lethipomp": {
        "name": "Lethipomp",
        "skill": "Empathy",
        "description": "Emotionless collectors of painful memories.",
        "blessing": "Spend Glamour and make a contested Composure + Empathy + Wyrd to absorb emotions of a memory, gaining a related condition and the ability to Incite Bedlam to make others reenact it.",
        "book": "Kith 99"
    },
    "lullescent": {
        "name": "Lullescent",
        "skill": "Stealth",
        "description": "Silent eavesdroppers with excellent hearing.",
        "blessing": "Spend Glamour to use echolocation, potentially even revealing things hidden by magic with a successful Wits + Occult + Wyrd roll.",
        "book": "Kith 100"
    },
    "riddleseeker": {
        "name": "Riddleseeker",
        "skill": "Investigation",
        "description": "Masters of riddles.",
        "blessing": "Spend Glamour and roll Wits + Expression + Wyrd to make a target agree to solve an argument or conflict with a riddle instead.",
        "book": "Kith 100"
    },
    "sideromancer": {
        "name": "Sideromancer",
        "skill": "Occult",
        "description": "Diviners of the Wyrd.",
        "blessing": "Spend Glamour and roll Wits + Occult + Wyrd to predict outcomes of pledges, promises, and debts within the scene.",
        "book": "Kith 101"
    },
    "spiegelbild": {
        "name": "Spiegelbild",
        "skill": "Persuasion",
        "description": "Advisors residing in mirrors.",
        "blessing": "Spend Glamour to enter a mirror and hide, but bind yourself to answer the truth while inside.",
        "book": "Kith 102"
    },
    
    # Kith & Kin - Shield kiths
    "asclepian": {
        "name": "Asclepian",
        "skill": "Medicine",
        "description": "Healers that use makeshift parts.",
        "blessing": "Spend Glamour and roll Intelligence + Medicine to perform impossible surgeries with mundane objects, which become hidden by the Mask.",
        "book": "Kith 103"
    },
    "bridgeguard": {
        "name": "Bridgeguard",
        "skill": "Intimidation",
        "description": "Changelings that fight against impossible odds and excel when outnumbered.",
        "blessing": "Spend Glamour when outnumbered to add your Composure + Intimidation to your defense and ignore the penalty for multiple attacks.",
        "book": "Kith 104"
    },
    "librorum": {
        "name": "Librorum",
        "skill": "Intimidation",
        "description": "Defenders of libraries and knowledge.",
        "blessing": "Spend Glamour and roll Intelligence + Occult + Wyrd to meditate and recall knowledge gleaned from your Keeper's library.",
        "book": "Kith 104"
    },
    "liminal": {
        "name": "Liminal",
        "skill": "Survival/Streetwise",
        "description": "Defenders of thresholds.",
        "blessing": "Spend Glamour while making a conditional declaration at a threshold to give the Lost condition to those who defy it.",
        "book": "Kith 105"
    },
    "reborn": {
        "name": "Reborn",
        "skill": "Occult",
        "description": "Changelings who were repeatedly killed and brought back to life.",
        "blessing": "Spend Glamour and roll Intelligence + Occult when injured to to redistribute skill dots for a scene, or permanently with the expenditure of a willpower dot.",
        "book": "Kith 105"
    },
    "stoneflesh": {
        "name": "Stoneflesh",
        "skill": "Intimidation",
        "description": "Durable Changelings with hardened resolve and hardened skin.",
        "blessing": "Spend Glamour and roll Stamina + Athletics + Wyrd to increase Armor, Resolve, and/or Composure.",
        "book": "Kith 106"
    },
    "wisewitch": {
        "name": "Wisewitch",
        "skill": "Persuasion",
        "description": "Changelings permanently touched by a Keeper's Title.",
        "blessing": "Make pledges with spirits and angels.",
        "book": "Kith 106"
    },
    
    # Kith & Kin - Steed kiths
    "airtouched": {
        "name": "Airtouched",
        "skill": "Athletics",
        "description": "Changelings disconnected from the rest of the world who spent their time in the skies of Arcadia.",
        "blessing": "Spend Glamour to reduce your effective weight significantly, allowing for impossible feats of balance.",
        "book": "Kith 107"
    },
    "chalomot": {
        "name": "Chalomot",
        "skill": "Empathy",
        "description": "The Gentry's scouts on the Dreaming Roads, experts at breaking into Bastions.",
        "blessing": "Spend Glamour to add half your Wyrd to dreamweaving rolls, and spend additional glamour to share the blessing with additional dreamers.",
        "book": "Kith 107"
    },
    "chevalier": {
        "name": "Chevalier",
        "skill": "Persuasion/Intimidation",
        "description": "Changelings with a connection to their steed, be it animal or vehicle.",
        "blessing": "Spend Glamour to bond with a vehicle or mount. Spend another Glamour point to reflexively call your Noble Steed.",
        "book": "Kith 107"
    },
    "farwalker": {
        "name": "Farwalker",
        "skill": "Survival",
        "description": "Those that patrol the outdoors, at home in the wilderness.",
        "blessing": "Spend Glamour while in the wilderness to create a temporary Safe Place capable of comfortably housing half your Wyrd worth of people, or more if you spend additional Glamour.",
        "book": "Kith 108"
    },
    "flickerflash": {
        "name": "Flickerflash",
        "skill": "Athletics",
        "description": "Lost who gotta go fast.",
        "blessing": "Spend Glamour to triple your speed.",
        "book": "Kith 110"
    },
    "levinquick": {
        "name": "Levinquick",
        "skill": "Computer",
        "description": "Restless scouts and couriers of digital landscapes.",
        "blessing": "Spend Glamour and roll Wits + Athletics + Wyrd to transport yourself up to Wyrd miles away through land-connected communication networks. Spend additional Glamour to bring companions along.",
        "book": "Kith 110"
    },
    "swarmflight": {
        "name": "Swarmflight",
        "skill": "Stealth",
        "description": "Lost capable of dissolving into a swarm of animals, objects, or some other phenomenon.",
        "blessing": "Spend Glamour to dissolve your body into your swarm.",
        "book": "Kith 110"
    },
    "swimmerskin": {
        "name": "Swimmerskin",
        "skill": "Brawl",
        "description": "Mermaids and their kin.",
        "blessing": "Naturally breath both air and water. Spend Glamour to fuse your legs into a tail, double your swimming speed, and ignore penalties for acting underwater.",
        "book": "Kith 111"
    },
    
    # Kith & Kin - Sword kiths
    "bearskin": {
        "name": "Bearskin",
        "skill": "Intimidation/Weaponry",
        "description": "Soldiers of Arcadia dedicated to causes important to them.",
        "blessing": "Spend Glamour to replace one of your defeated or cowed opponents' Aspirations with one of your own.",
        "book": "Kith 111"
    },
    "beastcaller": {
        "name": "Beastcaller",
        "skill": "Animal Ken",
        "description": "Lost with a connection to goblin beasts.",
        "blessing": "Spend Glamour to overtake a goblin beast's body with a successful Presence + Animal Ken + Wyrd roll, taking damage whenever the goblin beast does while doing so.",
        "book": "Kith 112"
    },
    "cyclopean": {
        "name": "Cyclopean",
        "skill": "Investigation",
        "description": "Lost made into magnificent giants or architectural features, often living with a disability.",
        "blessing": "Spend Glamour to learn a target's weak points, reducing penalties for specified targets and upgrading damage to lethal.",
        "book": "Kith 112"
    },
    "plaguesmith": {
        "name": "Plaguesmith",
        "skill": "Medicine",
        "description": "Lost fashioned into bioweapons, capable of spreading diseases.",
        "blessing": "Spend Glamour while touching a target to infect them with an Arcadian Plague, with symptoms reflecting your Keeper's Titles.",
        "book": "Kith 113"
    },
    "razorhand": {
        "name": "Razorhand",
        "skill": "Brawl",
        "description": "Lost with sharp objects replacing or attaching their hands.",
        "blessing": "Spend Glamour to turn one of your hands into a 1L knife that uses Brawl for attacks, or both hands with an additional Glamour.",
        "book": "Kith 114"
    },
    "sandharrowed": {
        "name": "Sandharrowed",
        "skill": "Survival",
        "description": "Lost who survived the deserts of Arcadia.",
        "blessing": "Spend Glamour before a Brawl or Weaponry attack to inflict the Immobilized Tilt by trapping your opponent in a pillar of sand on a success, providing them with cover.",
        "book": "Kith 115"
    },
    "valkyrie": {
        "name": "Valkyrie",
        "skill": "Persuasion/Intimidation",
        "description": "Lost forced to choose who lives and dies on the battlefields of Arcadia.",
        "blessing": "Spend Glamour and roll Wits + Occult + Wyrd vs Resolve + Tolerance to curse enemies with the Frightened or Reckless condition or bless allies with the Inspired or Steadfast conditions.",
        "book": "Kith 115"
    },
    "venombite": {
        "name": "Venombite",
        "skill": "Brawl",
        "description": "Lost turned venomous by their petty resentments.",
        "blessing": "Spend Glamour before making a Brawl attack to make it venomous, dealing lethal damage and inflicting the grave Poisoned Tilt on a success.",
        "book": "Kith 116"
    },
    
    # Kith & Kin - Additional kiths
    "apoptosome": {
        "name": "Apoptosome",
        "skill": "Miscellaneous",
        "description": "Lost left to constantly fight and die in isolation.",
        "blessing": "Spend Glamour when fighting a foe that defeated you before to inflict a point of aggravated damage, and inflict an additional point of aggravated damage to both you and your foes when damaged.",
        "book": "Kith 116"
    },
    "becquerel": {
        "name": "Becquerel",
        "skill": "Stealth",
        "description": "Radioactive Lost.",
        "blessing": "Spend Glamour while grappling to burn your targets with radiation, dealing damage as a fire the size of a torch with the heat of a candle and inflicting the Stunned or Poisoned tilts when you maintain a grapple.",
        "book": "Kith 117"
    },
    "blightbent": {
        "name": "Blightbent",
        "skill": "Disease/Poison",
        "description": "Lost permanently tainted by poisons and pollution.",
        "blessing": "Spend Glamour to inflict the Poisoned Tilt on a successful grapple.",
        "book": "Kith 117"
    },
    "enkrateia": {
        "name": "Enkrateia",
        "skill": "Empathy/Persuasion/Subterfuge",
        "description": "The voice of reason to their Keepers, the advisors, and mediators of Arcadia.",
        "blessing": "Only lose dice on the third Investigation roll.",
        "book": "Kith 118"
    },
    "gravewight": {
        "name": "Gravewight",
        "skill": "Empathy/Intimidation",
        "description": "Lost with a connection to death.",
        "blessing": "Spend Glamour to see and hear ghosts in Twilight. Ghosts appear near you more frequently.",
        "book": "Kith 119"
    },
    "shadowsoul": {
        "name": "Shadowsoul",
        "skill": "Subterfuge",
        "description": "Lost with a connection to the stars and the nighttime.",
        "blessing": "Gain affinity with the Mirror regalia. Inflict the temporary Blindness Condition on an exceptional success with an attack.",
        "book": "Kith 119"
    },
    "telluric": {
        "name": "Telluric",
        "skill": "Drive/Streetwise",
        "description": "Celestial bodies and stars above Arcadia.",
        "blessing": "Spend Glamour to throw a ball of starfire with Dexterity + Athletics, dealing damage with the heat of a torch and the size of a candle.",
        "book": "Kith 120"
    },
    "whisperwisp": {
        "name": "Whisperwisp",
        "skill": "Falsehoods",
        "description": "Spies and saboteurs.",
        "blessing": "Add your Wyrd and gain 9-again to either Stealth or Persuasion rolls.",
        "book": "Kith 120"
    },
    
    # Dark Eras 2 kiths
    "antiquarian": {
        "name": "Antiquarian",
        "skill": "Empathy",
        "description": "Secret holders and living repositories of knowledge.",
        "blessing": "Spend Glamour and roll Intelligence + Composure to look inward for the answer to a question.",
        "book": "DE2 69"
    },
    "chimera": {
        "name": "Chimera",
        "skill": "Subterfuge",
        "description": "Animalistic changelings stitched together from pieces of a multitude of Arcadian beasts.",
        "blessing": "One Goblin Contract, rotating each story, incurs no Goblin Debt when used.",
        "book": "CTL JS 47 / DE2 69"
    },
    "dryad": {
        "name": "Dryad",
        "skill": "Survival",
        "description": "Those who spent their Durance as creatures of gardens and greenery.",
        "blessing": "Spend Glamour when hiding behind foliage to add Wyrd as a Stealth bonus, or while still, disappear.",
        "book": "DE2 70"
    },
    "muse": {
        "name": "Muse",
        "skill": "Mantle",
        "description": "Changelings whose influence over others manifests through their beauty.",
        "blessing": "Spend Glamour and make an appropriate Social roll to confer bonuses on a human's work of art or architecture.",
        "book": "DE2 70"
    },
    "nymph": {
        "name": "Nymph",
        "skill": "Athletics",
        "description": "Changelings who dwelled in Faerie's oceans and waterways.",
        "blessing": "Breathe and move smoothly through water at double Speed.",
        "book": "DE2 70"
    },
    "cleverquick": {
        "name": "Cleverquick",
        "skill": "Occult",
        "description": "Tricksters whose Durance honed their skill at wits and intrigue.",
        "blessing": "Spend Glamour to intuit a foe's frailty, ban or bane, or three Glamour to impose one temporarily on both your foe and yourself.",
        "book": "DE2 368"
    },
}


def get_kith(kith_key):
    """Get a specific kith by key."""
    return ALL_KITHS.get(kith_key.lower().replace(" ", "_"))


def get_all_kiths():
    """Get all kiths."""
    return ALL_KITHS.copy()

