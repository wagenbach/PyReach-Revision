from world.cofd.stat_types import Merit

# Restricted Merits
# These Merits Should Only Be Used on a case-by-case Storyteller approved basis.
restricted_merits = [
    Merit(
        name="Holy Acquaintances",
        min_value=1,
        max_value=5,
        description="You have friends in the Church hierarchy in a time and place when the Church's authority rivals the state's.",
        merit_type="restricted",
        prerequisite="",
        book="DE2 274"
    ),
    Merit(
        name="Librarian",
        min_value=3,
        max_value=3,
        description="Your training at the Library of Alexandria improves your scholarly impression and helps you locate written records.",
        merit_type="restricted",
        prerequisite="",
        book="DE2 75"
    ),
    Merit(
        name="Party Affiliation Status",
        min_value=1,
        max_value=5,
        description="You have standing in one of the major political parties involved in a time of civil upheaval.",
        merit_type="restricted",
        prerequisite="",
        book="DE2 344"
    ),
    Merit(
        name="Rune Caster",
        min_value=2,
        max_value=2,
        description="+2 on rolls for the Clairvoyance, Medium or Omen Sensitivity Merits, interpreting a Cahalith's Prophetic Dreams, or using the Gift of Insight.",
        merit_type="restricted",
        prerequisite="occult:2",
        book="DE 163"
    ),
    Merit(
        name="Sabbat Knowledge",
        min_value=2,
        max_value=5,
        description="You are learned in the teachings of witches and witch-hunters alike.",
        merit_type="restricted",
        prerequisite="",
        book="DE2 275"
    ),
    #Church of the Wolf Merits
    Merit(
        name="Apocalypsis fidei",
        min_value=1,
        max_value=1,
        description="When afflicted by Lunacy, gain the Enraptured Condition on success and the Awestruck Condition on failure. You may choose to add Enraptured to an exceptional success.",
        merit_type="churchofthewolf",
        prerequisite="",
        book="NH:SM 134"
    ),
    Merit(
        name="Invenire venandi",
        min_value=2,
        max_value=2,
        description="Gain a general sense of being close to werewolf when within (Wits x 10) miles of one. Roll Perception to find a werewolf within (Empathy x 10) yards.",
        merit_type="churchofthewolf",
        prerequisite="apocalypsis_fidei:1",
        book="NH:SM 134"
    ),
    Merit(
        name="Manticae",
        min_value=3,
        max_value=3,
        description="Werewolves in Kuruth treat you like a packmate in a shared Rage and will not attack you.",
        merit_type="churchofthewolf",
        prerequisite="invenire_venandi:2",
        book="NH:SM 134"
    ),
    Merit(
        name="Ligulae",
        min_value=4,
        max_value=4,
        description="Werewolves who come within (Primal Urge) yards treat your presence as a trigger for Death Rage.",
        merit_type="churchofthewolf",
        prerequisite="manticae:3",
        book="NH:SM 134"
    ),
    #Svikiro Merits
    Merit(
        name="Svikiro",
        min_value=3,
        max_value=3,
        description="You're a medium in one of the traditions of the Shona peoples. You cannot be Claimed, and sense and support certain ephemeral entities with Influence Conditions, depending on whether you are wamasikati or wedzinza.",
        merit_type="svikiro",
        prerequisite="resolve:3,composure:3,sleeper:0",
        book="DEC 123"
    ),
    Merit(
        name="Svikiro Channel",
        min_value=1,
        max_value=3,
        description="When Fettered to an entity, you can communicate with it and serve as a channel for its powers. With three dots, you can forcibly channel its power by spending Willpower and contesting the entity.",
        merit_type="svikiro",
        prerequisite="svikiro:3",
        book="DEC 124"
    ),
    Merit(
        name="Svikiro Nganga",
        min_value=2,
        max_value=2,
        description="You're both wamasikati and wedzinza.",
        merit_type="svikiro",
        prerequisite="svikiro:3",
        book="DEC 124"
    ),
    Merit(
        name="Svikiro Ridden",
        min_value=1,
        max_value=3,
        description="You're conscious and can communicate with an entity while it Possesses you. With three dots, you can temporarily seize control back by spending Willpower and contesting the entity.",
        merit_type="svikiro",
        prerequisite="svikiro:3",
        book="DEC 124"
    ),
    #Cybernetics Merits
    Merit(
        name="Cybernetic Limb",
        min_value=3,
        max_value=3,
        description="Limb replacements offer a Strength bonus to certain actions or traits, such as climbing, lifting objects, Speed and Initiative, and can store small objects within compartments. Cybernetic arms can be used as +2 Brawl weapons.",
        merit_type="cybernetics",
        prerequisite="",
        book="DSG 182"
    ),
    Merit(
        name="Implanted Device",
        min_value=1,
        max_value=1,
        description="Voice-activated electronic equipment that is always on your person.",
        merit_type="cybernetics",
        prerequisite="",
        book="DSG 183"
    ),
    Merit(
        name="Implanted Weapon",
        min_value=2,
        max_value=2,
        description="Install a Size 0-1 weapon you may draw effectively.",
        merit_type="cybernetics",
        prerequisite="",
        book="DSG 183"
    ),
    Merit(
        name="Optical Enhancements",
        min_value=3,
        max_value=3,
        description="Telescoping zooming vision grants a +2 bonus to perception, ranged combat, and delicate work.",
        merit_type="cybernetics",
        prerequisite="",
        book="DSG 183"
    ),
    Merit(
        name="Subdermal Armor",
        min_value=1,
        max_value=3,
        description="Fortified bone and tissue grants a point of general Armor for each dot in this Merit.",
        merit_type="cybernetics",
        prerequisite="",
        book="DSG 183"
    ),
    Merit(
        name="Wired",
        min_value=1,
        max_value=1,
        description="Neural augmentation grants a bonus die to rolls using your choice of Composure, Dexterity, Intelligence, Manipulation, Stamina, or Wits.",
        merit_type="cybernetics",
        prerequisite="",
        book="DSG 183"
    ),
    #Nereid Merits
    Merit(
        name="Each to Each",
        min_value=1,
        max_value=1,
        description="Spend a turn sending out a message that all other Nereids withing Blood Potency * 10 miles hear. You cannot do anything except move at half speed.",
        merit_type="nereid",
        prerequisite="",
        book="NH:SB 139"
    ),
    Merit(
        name="Swimmer's Skin",
        min_value=2,
        max_value=3,
        description="At two dots, move at full speed, without movement penalties, in the water and can attack with claws at quickly as if out of the water. At three dots, also be able to roll Dexterity + Athletics to move at triple speed for Blood Potency turns.",
        merit_type="nereid",
        prerequisite="",
        book="NH:SB 139"
    ),
    #Crown Games Merits
    Merit(
        name="Divine Scion",
        min_value=1,
        max_value=3,
        description="Be part of an elite bloodline. +1 to social rolls with those below you. With three dots, be a lost heir and act as though you have 3 status to gain access to elite places once per story.",
        merit_type="crowngames",
        prerequisite="",
        book="GTTN 123"
    ),
    #End of the World Merits
    Merit(
        name="Cult",
        min_value=1,
        max_value=5,
        description="Have a cult following you, making a demand per dot of this merit per story so long as you also make a single action proving yourself worthy of leading. For additional demands, roll Manipulation + Intimidation or Persuasion + Cult, and lose a dot of this merit for the rest of the chapter.",
        merit_type="endoftheworld",
        prerequisite="",
        book="GTTN 123"
    ),
    Merit(
        name="Hidden Cache",
        min_value=1,
        max_value=3,
        description="Once per chapter, gain supplies as if having resource dots equal to this merit.",
        merit_type="endoftheworld",
        prerequisite="",
        book="GTTN 123"
    ),
    Merit(
        name="Strain Resistant",
        min_value=3,
        max_value=3,
        description="Ignore your first failure of being affected by the blood and one level less lethal on a dramatic failure.",
        merit_type="endoftheworld",
        prerequisite="vampire",
        book="GTTN 124"
    ),
    #Ascendancy Merits
    Merit(
        name="Augmented Retainers",
        min_value=1,
        max_value=5,
        description="An alternate version of retainer with Cybernetic Augmentation. One or Two dots have common augmentation, Three or Four dots have Quality, Five has Superb.",
        merit_type="ascendancy",
        prerequisite="",
        book="GTTN 124"
    ),
    Merit(
        name="Feared Among The Mighty",
        min_value=2,
        max_value=2,
        description="Your violent reputation has the Ascendancy avoiding your affairs unless you're provoking them.",
        merit_type="ascendancy",
        prerequisite="",
        book="GTTN 125"
    ),
    Merit(
        name="Synthetic Feast",
        min_value=3,
        max_value=3,
        description="By spending one willpower, you cand feed off of someone with cybernetics as if they were a normal human.",
        merit_type="ascendancy",
        prerequisite="vampire",
        book="GTTN 125"
    ),
    #Night Without End Merits
    Merit(
        name="Celebrity",
        min_value=1,
        max_value=3,
        description="An alternate version of Fame on a galactic scale.",
        merit_type="nightwithoutend",
        prerequisite="",
        book="GTTN 125"
    ),
    Merit(
        name="Impatient Blood",
        min_value=2,
        max_value=4,
        description="Serum made from you takes nine years minus your Blood Potency at two dots, or seven years at four. Feel compared to procreate regardless of grooming.",
        merit_type="nightwithoutend",
        prerequisite="vampire",
        book="GTTN 125"
    ),
    Merit(
        name="Network",
        min_value=1,
        max_value=1,
        description="In a galaxy of imperfect transmission, you have a system that allows uninterrupted transmission of messages.",
        merit_type="nightwithoutend",
        prerequisite="",
        book="GTTN 125"
    ),
    Merit(
        name="Wealth Immeasurable",
        min_value=1,
        max_value=5,
        description="An alternate version of resources on a planetary scale.",
        merit_type="nightwithoutend",
        prerequisite="",
        book="GTTN 125"
    ),
    #War Drums Merits
    Merit(
        name="Night Guardian",
        min_value=1,
        max_value=3,
        description="A community accepts you as their personal monster. Once per story, use the community to use the dots in this merit as contacts, resources, or status.",
        merit_type="wardrums",
        prerequisite="vampire",
        book="GTTN 127"
    ),
    #Shadow Occultist Merits
    Merit(
        name="Shadow Occultism",
        min_value=4,
        max_value=4,
        description="Previously possessed, ridden, or claimed and transgressed. You've developed the ability to work in Shadow Occultism.",
        merit_type="shadowoccult",
        prerequisite="breaking_point:1",
        book="NH:SM 138"
    ),
    Merit(
        name="Shadow Perception",
        min_value=3,
        max_value=3,
        description="You can see spirits in Twilight, understand First Tongue and other perceptive abilities related to the Shadow.",
        merit_type="shadowoccult",
        prerequisite="shadow_occultism:4,breaking_point:2",
        book="NH:SM 138"
    ),
    #Restricted Styles
    Merit(
        name="Athenian",
        min_value=1,
        max_value=5,
        description="Style. You are a member of an insular community of vampires called the Athenians.",
        merit_type="restricted",
        prerequisite="",
        book="NH:SB 115"
    ),
    Merit(
        name="Phoenix Deputy",
        min_value=1,
        max_value=5,
        description="Style. You are a Deputy under Phoenix Sheriff Russell Brown. You hunt Prometheans.",
        merit_type="restricted",
        prerequisite="",
        book="PtC2e 285"
    ),
    Merit(
        name="SPR Status",
        min_value=1,
        max_value=5,
        description="Style. You're a member of the Society for Psychical Research. Also a Status Merit.",
        merit_type="restricted",
        prerequisite="",
        book="DEC 280"
    ),
    Merit(
        name="Theosophical Society Status",
        min_value=1,
        max_value=5,
        description="Style. You're a member of Madame Blavatsky's group of contemporaries. Also a Status Merit.",
        merit_type="restricted",
        prerequisite="",
        book="DEC 278"
    ),
    Merit(
        name="Zero-Gravity Fighting",
        min_value=1,
        max_value=3,
        description="You are adept at fighting in zero or low gravity.",
        merit_type="nightwithoutend",
        prerequisite="",
        book="GTTN 126"
    ),
    #Mystery Cult Initiations
    Merit(
        name="The Bay City Marshals",
        min_value=1,
        max_value=5,
        description="A Nameless Order sworn to peacekeeping and retribution in the wake of the gold rush.",
        merit_type="mysterycult",
        prerequisite="",
        book="DE2 386"
    ),
    Merit(
        name="The Chosen of Mammon",
        min_value=1,
        max_value=5,
        description="Prosperity cult worshipping the power of money.",
        merit_type="mysterycult",
        prerequisite="",
        book="CofD 52"
    ),
    Merit(
        name="The Church of Death's Shards",
        min_value=1,
        max_value=5,
        description="Necromancers who hoard Mementos for their own power and to fight ghostly horrors.",
        merit_type="mysterycult",
        prerequisite="",
        book="GtS2e 228"
    ),
    Merit(
        name="Company of the Codex",
        min_value=1,
        max_value=5,
        description="A Nameless Order sworn to radical freedom in the Pirate Republic of Nassau.",
        merit_type="mysterycult",
        prerequisite="",
        book="DE2 300"
    ),
    Merit(
        name="Cult of Divine Resurrection",
        min_value=1,
        max_value=5,
        description="Archeologists and historians unknowingly worshipping Abyssal powers.",
        merit_type="mysterycult",
        prerequisite="",
        book="NH:NA 105"
    ),
    Merit(
        name="Cult of Huitzilopochtli the Many-Wheeled",
        min_value=1,
        max_value=5,
        description="Aztecs who conflated Huitzilopochtli with the God-Machine",
        merit_type="mysterycult",
        prerequisite="",
        book="DE 250"
    ),
    Merit(
        name="Daughters of Ravana",
        min_value=1,
        max_value=5,
        description="Alchemists who hunt monsters to use their parts as reagents.",
        merit_type="mysterycult",
        prerequisite="",
        book="NH:TT 92"
    ),
    Merit(
        name="Fellowship of the Final Awakening",
        min_value=1,
        max_value=5,
        description="Demon-manipulated apocalypse cult.",
        merit_type="mysterycult",
        prerequisite="",
        book="DtD 358"
    ),
    Merit(
        name="The Forty-Third Nome",
        min_value=1,
        max_value=5,
        description="An Egyptian Sin-Eater krewe seeking the lost heart of the Underworld.",
        merit_type="mysterycult",
        prerequisite="",
        book="GtS2e 87"
    ),
    Merit(
        name="The Grand Order of the Immaculate Three",
        min_value=1,
        max_value=5,
        description="Spiritualist social organization secretly manipulated as a vehicle of vengeance.",
        merit_type="mysterycult",
        prerequisite="",
        book="DEC 286"
    ),
    Merit(
        name="Hand of Destiny",
        min_value=1,
        max_value=5,
        description="An accursed Nameless Order of self-help Scelesti.",
        merit_type="mysterycult",
        prerequisite="",
        book="NH:NA 119"
    ),
    Merit(
        name="Hototogisu Status",
        min_value=1,
        max_value=5,
        description="A conspiratorial business conglomerate in conflict with vampires in Tokyo. Also a Status Merit.",
        merit_type="mysterycult",
        prerequisite="",
        book="VtR2e 267"
    ),
    Merit(
        name="Jaguar Priests",
        min_value=1,
        max_value=5,
        description="Priests of the Aztec City of Tenochtitlan.",
        merit_type="mysterycult",
        prerequisite="",
        book="DE 249"
    ),
    Merit(
        name="Latimer's Followers",
        min_value=1,
        max_value=5,
        description="Unknowing devout followers of a Seer of the Throne's philosophy.",
        merit_type="mysterycult",
        prerequisite="",
        book="NH:NA 36"
    ),
    Merit(
        name="The Order of the Ineffable Flame",
        min_value=1,
        max_value=5,
        description="Worshippers of the Divine Fire. Also a Status Merit. Two or more dots include a Persistant Condition.",
        merit_type="mysterycult",
        prerequisite="",
        book="NT:TT 105"
    ),
    Merit(
        name="Order of the Rose",
        min_value=1,
        max_value=5,
        description="A Nameless Order sworn to perfecting the human body and soul, and exploring other realms.",
        merit_type="mysterycult",
        prerequisite="",
        book="NH:NA 47"
    ),
    Merit(
        name="RAT Squad",
        min_value=1,
        max_value=5,
        description="Washington State Department of Transportation special occult projects team.",
        merit_type="mysterycult",
        prerequisite="",
        book="Seat 20"
    ),
    Merit(
        name="Sisters and Brothers of the Bomb",
        min_value=1,
        max_value=5,
        description="Military mystics fighting a guerrilla war against the God-Machine.",
        merit_type="mysterycult",
        prerequisite="",
        book="CofD 52"
    ),
    Merit(
        name="The Tick-Tock Men",
        min_value=1,
        max_value=5,
        description="A cult which serves the God-Machine in the name of pure order and collectivism.",
        merit_type="mysterycult",
        prerequisite="",
        book="Interface 107"
    ),
    Merit(
        name="The Titgwai Gang",
        min_value=1,
        max_value=3,
        description="Gang containing worshippers of a spirit of death by train.",
        merit_type="mysterycult",
        prerequisite="",
        book="HL 116"
    ),
    Merit(
        name="Tremere",
        min_value=1,
        max_value=5,
        description="A Nameless Order of Reaper liches seeking to understand creation's hunger.",
        merit_type="mysterycult",
        prerequisite="",
        book="NH:NA 128"
    ),
    Merit(
        name="Voyager Membership",
        min_value=1,
        max_value=5,
        description="Tokyo-based cult that studies the power of names.",
        merit_type="mysterycult",
        prerequisite="",
        book="WtF2e 272"
    ),
]

# Create dictionary for easy lookup
restricted_merits_dict = {merit.name.lower().replace(" ", "_").replace("(", "").replace(")", ""): merit for merit in restricted_merits}
