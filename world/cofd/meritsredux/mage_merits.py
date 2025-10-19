from world.cofd.stat_types import Merit

# Mage-Specific Merits
mage_merits = [
    Merit(
        name="Adamant Hand",
        min_value=2,
        max_value=2,
        description="Allows use of prerequisite Skill as reflexive Order tool Yantra in combat.",
        merit_type="mage",
        prerequisite="arrow_status:1,[athletics:3,brawl:3,weaponry:3]",
        book="MtA2e 99"
    ),
    Merit(
        name="Artifact",
        min_value=3,
        max_value=15,
        description="Own a magical item that can cast spells and stores dots x2 Mana, and can act as a Path tool Yantra worth +1 die for Mages of the path of highest spell effect stored.",
        merit_type="mage",
        prerequisite="",
        book="MtA2e 99"
    ),
    Merit(
        name="Astral Adept",
        min_value=3,
        max_value=3,
        description="Can enter Astral Realms from any location if a ceremony is performed and a Willpower point spent.",
        merit_type="mage",
        prerequisite="",
        book="MtA2e 100"
    ),
    Merit(
        name="Astral Intruder",
        min_value=3,
        max_value=3,
        description="Make a Clash of Wills to meditate into the Oneiros of a mage whose soul stone you possess, instead of your own.",
        merit_type="mage",
        prerequisite="astral_adept:3,resolve:3",
        book="SoS 91"
    ),
    Merit(
        name="Awakened Status",
        min_value=1,
        max_value=5,
        description="Hold status in a Consilium or Order. You may temporarily requisition dots of Alternate Identity, Retainer, Imbued Item, Artifact, Grimoire, Mentor, Hallow, Sanctum, Library, Advanced Library, Safe Place, Familiar, and Resources.",
        merit_type="mage",
        prerequisite="",
        book="MtA2e 100"
    ),
    Merit(
        name="Between the Ticks",
        min_value=2,
        max_value=2,
        description="Once per scene can take -1 from Initiative to add +1 to an action for a turn, or vice versa",
        merit_type="mage",
        prerequisite="wits:3,time:1",
        book="MtA2e 100"
    ),
    Merit(
        name="Broad Dedication",
        min_value=1,
        max_value=1,
        description="Instill your nimbus into a specific Yantra that aligns with your spellcasting, making your Dedicated Tool any kind of Yantra.",
        merit_type="mage",
        prerequisite="prime:1",
        book="SoS 57"
    ),
    Merit(
        name="Cabal Theme",
        min_value=1,
        max_value=1,
        description="Must be taken by entire cabal. All members of the cabal are counted as one dot higher in Shadow Name Merit for purposes of personal Yantras",
        merit_type="mage",
        prerequisite="",
        book="MtA2e 100"
    ),
    Merit(
        name="Cognoscente",
        min_value=2,
        max_value=2,
        description="Your character has perfected the art of scribing grimoires. Anyone casting from his tomes may do so without the doubled ritual casting time. He may also imprint his own signature nimbus into the rote imago when scribing the spell. Doing so causes the rote to show his own nimbus instead of hiding the caster's. Once per story, gain +2 to a Social roll that relies on this fame and enjoy the benefits of Occultation •••.",
        merit_type="mage",
        prerequisite="prime:3,[academics:3,occult:3]",
        book="SoS 87"
    ),
    Merit(
        name="Daimonomikon",
        min_value=1,
        max_value=5,
        description="Your character possesses a Daimonomikon for a particular legacy. Each dot corrosponds to the Attainment within the Legacy that can be learned from the Daimonomikon.",
        merit_type="mage",
        prerequisite="",
        book="SoS 87"
    ),
    Merit(
        name="Destiny",
        min_value=1,
        max_value=5,
        description="Gain a pool of rerolls or rote-quality rolls on mundane actions per chapter, but have an associated Doom.",
        merit_type="mage",
        prerequisite="",
        book="MtA2e 100"
    ),
    Merit(
        name="Dominant Soul",
        min_value=1,
        max_value=5,
        description="When your character has another mage's soul stone you can counterspell any Arcanum from its owner, applying Merit dots as your Arcanum rating. If used as a Yantra during a Prime dispellation, reduce Withstand by dots in this Merit.",
        merit_type="mage",
        prerequisite="composure:3",
        book="MtA2e 101"
    ),
    Merit(
        name="Dream",
        min_value=1,
        max_value=5,
        description="Have a number of questions answered directly per chapter in your dreams.",
        merit_type="mage",
        prerequisite="wits:3,composure:3",
        book="MtA2e 101"
    ),
    Merit(
        name="Echo Chamber",
        min_value=4,
        max_value=4,
        description="See flashbacks of a soul stone's owner. Gain exceptional success off 3 dice for active mage sight to investigate a mystery based on the soul stone's Path. Once per story, meditate on the soul stone to ask yes or no questions about the mystery.",
        merit_type="mage",
        prerequisite="Empathy:2",
        book="SoS 91"
    ),
    Merit(
        name="Egregore",
        min_value=1,
        max_value=5,
        description="Style. You have attained a deeper inclusion into the Mysterium.",
        merit_type="mage",
        prerequisite="mysterium_status:1",
        book="MtA2e 101"
    ),
    Merit(
        name="Enhanced Item",
        min_value=1,
        max_value=15,
        description="Own an item enhanced by spells.",
        merit_type="mage",
        prerequisite="",
        book="MtA2e 101"
    ),
    Merit(
        name="Enriched Item",
        min_value=2,
        max_value=4,
        description="Your character owns an item with a natural enhancement or one permanently altered through multiple uses of the same enchantment.",
        merit_type="mage",
        prerequisite="",
        book="SoS 76"
    ),
    Merit(
        name="Epiphany Stone",
        min_value=4,
        max_value=4,
        description="Spend Mana while using active mage sight to roll Clash of Wills to check if you are under some form of illusion, hallucination, forced astral journey or other supernatural power that separates you from reality.",
        merit_type="mage",
        prerequisite="[dream:1,astral_adept:3],mind:2",
        book="SoS 91"
    ),
    Merit(
        name="Familiar",
        min_value=2,
        max_value=4,
        description="Bound to an ephemeral familiar with Rank equal to half this Merit",
        merit_type="mage",
        prerequisite="",
        book="MtA2e 101"
    ),
    Merit(
        name="Fast Spells",
        min_value=2,
        max_value=2,
        description="Opponents Defend against your aim spells as they do against firearms",
        merit_type="mage",
        prerequisite="firearms:2,time:1",
        book="MtA2e 101"
    ),
    Merit(
        name="Fire Keeper",
        min_value=1,
        max_value=1,
        description="Environmental causes can't fully snuff flames in your presence unless you will it.",
        merit_type="mage",
        prerequisite="ancient_obrimos",
        book="DE 50"
    ),
    Merit(
        name="Fluent High Speech",
        min_value=3,
        max_value=3,
        description="You may converse at length in High Speech. Persuasion and Intimidation rolls with mages and supernal entities that use the High Speech gain +2, and Expression rolls are not reduced to chance dice. Participating in a supernal summoning reduces the target number by two.",
        merit_type="mage",
        prerequisite="awakened,presence:4,expression:3",
        book="SoS 26"
    ),
    Merit(
        name="Grimoire",
        min_value=1,
        max_value=5,
        description="Own a Grimoire with two spells per dot.",
        merit_type="mage",
        prerequisite="",
        book="MtA2e 101"
    ),
    Merit(
        name="Hidden High Speech",
        min_value=1,
        max_value=1,
        description="Your character may use mundane language to conceal a message in High Speech. Sleepers or Sleepwalkers who hear or read the message do not hear glossolalia or read gibberish. Use at no cost when writing, though speaking this way is taxing and requires a point of Willpower.",
        merit_type="mage",
        prerequisite="awakened,manipulation:3,expression:3",
        book="SoS 26"
    ),
    Merit(
        name="High Speech",
        min_value=1,
        max_value=1,
        description="Use High Speech as a Yantra.",
        merit_type="mage",
        prerequisite="",
        book="MtA2e 102"
    ),
    Merit(
        name="Imbued Ally",
        min_value=1,
        max_value=15,
        description="You have imbued a spell with indefinite duration into a person or creature who is bound to you. The creature has a single spell and Mana in which to cast it.",
        merit_type="mage",
        prerequisite="",
        book="SoS 76"
    ),
    Merit(
        name="Imbued Item",
        min_value=1,
        max_value=15,
        description="Own an item imbued with spells it can cast.",
        merit_type="mage",
        prerequisite="",
        book="MtA2e 102"
    ),
    Merit(
        name="Imposing Nimbus",
        min_value=3,
        max_value=3,
        description="Your characters Nimbus is a true force of Nature. Whenever someone succumbs to their Nimbus Tilt spend a point of willpower to convert the Tilt into a Persistent Condition for that person. That condition gains an extra resolution option of successfully defeating your character on a contested roll or causing her harm.",
        merit_type="mage",
        prerequisite="",
        book="SoS 95"
    ),
    Merit(
        name="Infamous Mentor",
        min_value=1,
        max_value=5,
        description="Call on Mentor's status and Social Merits by name-dropping.",
        merit_type="mage",
        prerequisite="mentor>=infamous_mentor",
        book="MtA2e 102"
    ),
    Merit(
        name="Inheritance",
        min_value=2,
        max_value=2,
        description="The Mage can use their bloodline as a +1 Yantra to any spell appropriate to their ancestors' reputation. If the spell is cast on a subject who knows their heritage and is aware of the spell being cast, this becomes +2.",
        merit_type="mage",
        prerequisite="fame:1",
        book="SoS 57"
    ),
    Merit(
        name="Keen Periphery",
        min_value=2,
        max_value=2,
        description="Your Peripheral Mage Sight is unusually perceptive. When sensing an effect via Peripheral Mage Sight you can also sense the Arcanum under which the effect falls",
        merit_type="mage",
        prerequisite="wits:3",
        book="SoS 26"
    ),
    Merit(
        name="Legacy Pedagogue",
        min_value=1,
        max_value=1,
        description="Your character's connection to a Legacy is so forceful that when scribing a Daimonomikon part of him remains with it. When characters initiate themselves into the Legacy by your Daimonomika, gain one arcane beat as if you tutored the character yourself.",
        merit_type="mage",
        prerequisite="prime:3,gnosis:3",
        book="SoS 87"
    ),
    Merit(
        name="Mana Battery",
        min_value=1,
        max_value=15,
        description="Your character has an Item imbued with a Mana pool which she can use instead of her own",
        merit_type="mage",
        prerequisite="",
        book="SoS 77"
    ),
    Merit(
        name="Mana Sensitivity",
        min_value=1,
        max_value=1,
        description="Sense Hallows and tass with Peripheral Mage Sight.",
        merit_type="mage",
        prerequisite="wits:3,prime:1",
        book="MtA2e 102"
    ),
    Merit(
        name="Masque",
        min_value=1,
        max_value=5,
        description="Style. Define a symbolic persona, and assume it with Willpower to benefit from the maneuvers.",
        merit_type="mage",
        prerequisite="guardian_status:1",
        book="MtA2e 102"
    ),
    Merit(
        name="Masque Persona",
        min_value=2,
        max_value=2,
        description="Define an additional persona to use with the Masque style merit.",
        merit_type="mage",
        prerequisite="guardian_status:1",
        book="MtA2e 102"
    ),
    Merit(
        name="Mystery Cult Influence",
        min_value=3,
        max_value=5,
        description="Rule a mystery cult and benefit from its Mystery Cult Initiation.",
        merit_type="mage",
        prerequisite="",
        book="MtA2e 103"
    ),
    Merit(
        name="Occultation",
        min_value=1,
        max_value=3,
        description="Penalize attempts to track or identify you by your Nimbus by dots in this Merit.",
        merit_type="mage",
        prerequisite="fame:0",
        book="MtA2e 103"
    ),
    Merit(
        name="Order Archive",
        min_value=1,
        max_value=5,
        description="Your character has access to an archive of information and resources belonging to her Order or Caucus. This Merit doesn't reflect the character's ability to requisition these materials, but indicates what her Order Caucus has available to its members.",
        merit_type="mage",
        prerequisite="[consilium_status:1,order_status:1]",
        book="SoS 97"
    ),
    Merit(
        name="Perfected Item",
        min_value=2,
        max_value=2,
        description="Your Character owns an item made from a Perfected Metal, Amalgam or Alloy with perminant duration.",
        merit_type="mage",
        prerequisite="",
        book="SoS 77"
    ),
    Merit(
        name="Persistant Nimbus",
        min_value=1,
        max_value=1,
        description="Your characters Nimbus effects linger for longer than most. Her Long-Term Nimbus continues to affect an area for one day per dot of Gnosis. When flaring her Immediate nimbus without casting, it lasts turns equal to Gnosis. Signature nimbus persists on subjects of her Magic one week per dot of gnosis as well.",
        merit_type="mage",
        prerequisite="",
        book="SoS 95"
    ),
    Merit(
        name="Piercing Glance",
        min_value=2,
        max_value=4,
        description="You may undertake a Clash of Wills to sense a concealed effect with Peripheral Mage Sight. For •• you suffer a -2 penalty to the roll, for •••• you suffer no penalty to the roll.",
        merit_type="mage",
        prerequisite="gnosis:2",
        book="SoS 26"
    ),
    Merit(
        name="Plunder Mana",
        min_value=2,
        max_value=2,
        description="Take 10 minutes ti perform an Oblation at a Hallow. Regain one Mana if you successfully Counter a spell with any Mana cost.",
        merit_type="mage",
        prerequisite="prime:1,resolve:2",
        book="DE2 300"
    ),
    Merit(
        name="Potent Nimbus",
        min_value=1,
        max_value=2,
        description="Add as a bonus to flare your Nimbus. Determine your Nimbus Tilt as if your Gnosis were raised by twice dots in this Merit.",
        merit_type="mage",
        prerequisite="",
        book="MtA2e 103"
    ),
    Merit(
        name="Potent Soul",
        min_value=3,
        max_value=3,
        description="When holding another Mage's Soul Stone any Social rolls against its owner gain 9-agains, Any social maneuvering automatically opens one Extra Door on every success.",
        merit_type="mage",
        prerequisite="awakened,presence:3",
        book="SoS 91"
    ),
    Merit(
        name="Potent Resonance",
        min_value=2,
        max_value=2,
        description="Characters scrutinizing your Nimbus are subject to your Nimbus Tilt.",
        merit_type="mage",
        prerequisite="gnosis:3",
        book="MtA2e 103"
    ),
    Merit(
        name="Prelacy",
        min_value=1,
        max_value=5,
        description="Style. Choose an Exarch to invite into your soul.",
        merit_type="mage",
        prerequisite="seer_status:3",
        book="MtA2e 103, SoS 122, DE2 301, TotP 142"
    ),
    Merit(
        name="Profane Tool",
        min_value=1,
        max_value=1,
        description="Your character may choose one of the following as a Dedicated Path tool; Scepters, Robes, Crowns, Thrones and Rings. This Merit may be purchased multiple times",
        merit_type="mage",
        prerequisite="prelacy:2",
        book=""
    ),
    Merit(
        name="Profligate Dedication",
        min_value=2,
        max_value=2,
        description="Your character may have up to three Dedicated Magical tools but can only use up to 2 at a time. You have no penalty for using only one (or none) of your Dedicated tools when casting.",
        merit_type="mage",
        prerequisite="",
        book="SoS 57"
    ),
    Merit(
        name="Sea's Hunger",
        min_value=1,
        max_value=1,
        description="Heal twice as quickly each day you destroy an object with magic.",
        merit_type="mage",
        prerequisite="ancient_moros",
        book="DE 49"
    ),
    Merit(
        name="Second-Person High Speech",
        min_value=3,
        max_value=3,
        description="Provide your own High Speech as a Yantra for others. If you meet the required Arcanum for the cast spell give +2 dice as a bonus, If you have at least one dot in the Primary Arcanum but not all dots give a +1. You can also use High Speech to gain a Dice Bonus on Imbued Items and Artifacts. This does not stack if the Caster is using High Speech as a Yantra.",
        merit_type="mage",
        prerequisite="awakened,presence:3,experession:3,high_speech:1",
        book="SoS 26"
    ),
    Merit(
        name="Shadow Name",
        min_value=1,
        max_value=3,
        description="Determine Shadow Name and symbolism, may use those symbols as a persona tool worth the merit's dots. Apply dots as a Withstand rating against spells that identify or target via Sympathy while in mundane persona.",
        merit_type="mage",
        prerequisite="",
        book="MtA2e 104"
    ),
    Merit(
        name="Shadow Self",
        min_value=2,
        max_value=2,
        description="Your Shadow Name isn't just a persona its a legend. Anyone who succumbs to the nimbus tilt takes a -2 penalty to all contested rolls against him for the rest of the scene as long as it aligns with the Shadow Name Identity. If your Shadow Name reflects a Mythological or Divine entity thats well known enough to have a presence in the Temenos he enjoys a +2 bonus to attempts to summon said Goetia.",
        merit_type="mage",
        prerequisite="shadow_name:3,mind:1",
        book="SoS 95"
    ),
    Merit(
        name="Sky's Whispers",
        min_value=1,
        max_value=1,
        description="Read the open sky as an instant action to predict the day's weather and take +3 to endure it.",
        merit_type="mage",
        prerequisite="ancient_acanthus",
        book="DE 48"
    ),
    Merit(
        name="Soul Dealer",
        min_value=1,
        max_value=5,
        description="You character has contacts in the Black Market soul trade or is a soul trader himself. Once per story your character can obtain a soul stone as though you were a member of any order status one for one to dots in this merit.",
        merit_type="mage",
        prerequisite="streetwise:3",
        book="SoS 91"
    ),
    Merit(
        name="Soul Stone",
        min_value=1,
        max_value=2,
        description="Your character owns another Mage's soul stone. One dot is equal or lesser Gnosis to your own. 2 dots is greater.",
        merit_type="mage",
        prerequisite="",
        book="SoS 92"
    ),
    Merit(
        name="Spirit Warden",
        min_value=2,
        max_value=2,
        description="Spirits must spend Willpower to attack you for a scene.",
        merit_type="mage",
        prerequisite="ancient_thyrsus",
        book="DE 50"
    ),
    Merit(
        name="Stalwart Soul",
        min_value=1,
        max_value=2,
        description="A soul stone created by you gains Durability equal to twice your dots in this merit and gains the same bonus to withstand against spells that would harm or destroy it.",
        merit_type="mage",
        prerequisite="composure:3",
        book="SoS 92"
    ),
    Merit(
        name="Supernal Taxonomy",
        min_value=2,
        max_value=2,
        description="You possess a deep understanding of Active Mage Sight. When observing phenomena in either similar effect or origin to one already scrutinized she can recognize the similarity.",
        merit_type="mage",
        prerequisite="intelligence:2,occult:3",
        book="SoS 43"
    ),
    Merit(
        name="Supernal Watcher",
        min_value=2,
        max_value=4,
        description="You have gained the attention of a supernal entity at rank 1 for 2 dots and rank 2 for 4 dots. When summoning your watcher you only need 5 successes, they appear when using Active mage sight and you may use it as a Path tool Yantra.",
        merit_type="mage",
        prerequisite="",
        book="SoS 43"
    ),
    Merit(
        name="Techne",
        min_value=2,
        max_value=2,
        description="Choose a focus that counts as an Order tool, and can treat Sleepers using it as a separate Order tool as long as the spell is subtle.",
        merit_type="mage",
        prerequisite="councillor_status:1",
        book="MtA2e 104"
    ),
    Merit(
        name="Trail Walker",
        min_value=2,
        max_value=2,
        description="Double your rate of travel across forests.",
        merit_type="mage",
        prerequisite="ancient_mastigos",
        book="DE 49"
    ),
]

# Create dictionary for easy lookup
mage_merits_dict = {merit.name.lower().replace(" ", "_").replace("(", "").replace(")", ""): merit for merit in mage_merits}
