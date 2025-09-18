from world.cofd.stat_types import Merit

# Mental Merits
mental_merits = [
    Merit(
        name="Area of Expertise",
        min_value=1,
        max_value=1,
        description="Uncommonly specialized in one area, +2 specialty bonus instead of +1",
        merit_type="mental",
        prerequisite="resolve:2,skill_specialty:1"
    ),
    Merit(
        name="Common Sense",
        min_value=3,
        max_value=3,
        description="Ask Storyteller questions about courses of action once per chapter",
        merit_type="mental"
    ),
    Merit(
        name="Danger Sense",
        min_value=2,
        max_value=2,
        description="+2 modifier to detect impending ambush",
        merit_type="mental"
    ),
    Merit(
        name="Direction Sense",
        min_value=1,
        max_value=1,
        description="Always aware of location and direction, never get lost",
        merit_type="mental"
    ),
    Merit(
        name="Eidetic Memory",
        min_value=2,
        max_value=2,
        description="Perfect recall, +2 bonus to remember minute facts",
        merit_type="mental"
    ),
    Merit(
        name="Encyclopedic Knowledge",
        min_value=2,
        max_value=2,
        description="Limitless factoids about chosen skill area",
        merit_type="mental"
    ),
    Merit(
        name="Eye for the Strange",
        min_value=2,
        max_value=2,
        description="Identify supernatural vs natural causes of events",
        merit_type="mental",
        prerequisite="resolve:2,occult:1"
    ),
    Merit(
        name="Fast Reflexes",
        min_value=1,
        max_value=3,
        description="+1 Initiative per dot",
        merit_type="mental",
        prerequisite="[wits:3,dexterity:3]"
    ),
    Merit(
        name="Good Time Management",
        min_value=1,
        max_value=1,
        description="Halve time between extended action rolls",
        merit_type="mental",
        prerequisite="[academics:2,science:2]"
    ),
    Merit(
        name="Holistic Awareness",
        min_value=1,
        max_value=1,
        description="Non-traditional healing methods without medical equipment",
        merit_type="mental"
    ),
    Merit(
        name="Indomitable",
        min_value=2,
        max_value=2,
        description="+2 dice to resist supernatural mental influence",
        merit_type="mental",
        prerequisite="resolve:3"
    ),
    Merit(
        name="Interdisciplinary Specialty",
        min_value=1,
        max_value=1,
        description="Apply specialty bonus to other skills when justified",
        merit_type="mental",
        prerequisite="skill:3,specialty:1"
    ),
    Merit(
        name="Investigative Aide",
        min_value=1,
        max_value=1,
        description="Exceptional success on 3 instead of 5 when uncovering clues",
        merit_type="mental",
        prerequisite="chosen_skill:3"
    ),
    Merit(
        name="Investigative Prodigy",
        min_value=1,
        max_value=5,
        description="Uncover multiple clues in single action",
        merit_type="mental",
        prerequisite="wits:3,investigation:3"
    ),
    Merit(
        name="Language",
        min_value=1,
        max_value=1,
        description="Fluency in additional language",
        merit_type="mental"
    ),
    Merit(
        name="Library",
        min_value=1,
        max_value=3,
        description="Add dots to extended rolls involving chosen Mental Skill",
        merit_type="mental"
    ),
    Merit(
        name="Meditative Mind",
        min_value=1,
        max_value=4,
        description="Enhanced meditation benefits",
        merit_type="mental"
    ),
    Merit(
        name="Multilingual",
        min_value=1,
        max_value=1,
        description="Conversational in two languages",
        merit_type="mental"
    ),
    Merit(
        name="Patient",
        min_value=1,
        max_value=1,
        description="Two additional rolls above Attribute + Skill in extended actions",
        merit_type="mental"
    ),
    Merit(
        name="Professional Training",
        min_value=1,
        max_value=5,
        description="Extensive training in particular profession",
        merit_type="mental"
    ),
    Merit(
        name="Tolerance for Biology",
        min_value=1,
        max_value=1,
        description="No rolls needed to withstand biologically strange sights",
        merit_type="mental",
        prerequisite="resolve:3"
    ),
    Merit(
        name="Trained Observer",
        min_value=1,
        max_value=3,
        description="9-again (or 8-again at 3 dots) on Perception rolls",
        merit_type="mental",
        prerequisite="[wits:3,composure:3]"
    ),
    Merit(
        name="Vice-Ridden",
        min_value=2,
        max_value=2,
        description="Character has two Vices",
        merit_type="mental"
    ),
    Merit(
        name="Virtuous",
        min_value=2,
        max_value=2,
        description="Character has two Virtues",
        merit_type="mental"
    )
]

# Physical Merits
physical_merits = [
    Merit(
        name="Ambidextrous",
        min_value=3,
        max_value=3,
        description="No -2 penalty for using off hand",
        merit_type="physical"
    ),
    Merit(
        name="Automotive Genius",
        min_value=1,
        max_value=1,
        description="Triple Crafts dots for vehicle modifications",
        merit_type="physical",
        prerequisite="crafts:3,drive:1,science:1"
    ),
    Merit(
        name="Crack Driver",
        min_value=2,
        max_value=3,
        description="Enhanced driving abilities",
        merit_type="physical",
        prerequisite="drive:3"
    ),
    Merit(
        name="Demolisher",
        min_value=1,
        max_value=3,
        description="Ignore object Durability points equal to Merit dots",
        merit_type="physical",
        prerequisite="[strength:3,intelligence:3]"
    ),
    Merit(
        name="Double Jointed",
        min_value=2,
        max_value=2,
        description="Automatically escape mundane bonds",
        merit_type="physical",
        prerequisite="dexterity:3"
    ),
    Merit(
        name="Fleet of Foot",
        min_value=1,
        max_value=3,
        description="+1 Speed per dot, pursuers at -1 per dot",
        merit_type="physical",
        prerequisite="athletics:2"
    ),
    Merit(
        name="Giant",
        min_value=3,
        max_value=3,
        description="Size 6, +1 Health",
        merit_type="physical"
    ),
    Merit(
        name="Greyhound",
        min_value=1,
        max_value=1,
        description="Exceptional success on 3 instead of 5 in chases",
        merit_type="physical",
        prerequisite="athletics:3,wits:3,stamina:3"
    ),
    Merit(
        name="Hardy",
        min_value=1,
        max_value=3,
        description="Add dots to rolls resisting disease, poison, deprivation",
        merit_type="physical",
        prerequisite="stamina:3"
    ),
    Merit(
        name="Iron Stamina",
        min_value=1,
        max_value=3,
        description="Eliminate negative modifiers from fatigue/injury",
        merit_type="physical",
        prerequisite="[stamina:3,resolve:3]"
    ),
    Merit(
        name="Quick Draw",
        min_value=1,
        max_value=1,
        description="Drawing/holstering chosen weapon is reflexive",
        merit_type="physical",
        prerequisite="wits:3,weapon_specialty:1"
    ),
    Merit(
        name="Relentless",
        min_value=1,
        max_value=1,
        description="Opponents need +2 successes in chases",
        merit_type="physical",
        prerequisite="athletics:2,stamina:3"
    ),
    Merit(
        name="Seizing the Edge",
        min_value=2,
        max_value=2,
        description="Always have Edge in first turn of chase",
        merit_type="physical",
        prerequisite="wits:3,composure:3"
    ),
    Merit(
        name="Sleight of Hand",
        min_value=2,
        max_value=2,
        description="One reflexive Larceny action per turn",
        merit_type="physical",
        prerequisite="larceny:3"
    ),
    Merit(
        name="Small-Framed",
        min_value=2,
        max_value=2,
        description="Size 4, -1 Health, +2 to hide",
        merit_type="physical"
    )
]

# Social Merits
social_merits = [
    Merit(
        name="Allies",
        min_value=1,
        max_value=5,
        description="Organizational connections that provide favors",
        merit_type="social"
    ),
    Merit(
        name="Alternate Identity",
        min_value=1,
        max_value=3,
        description="Established false identity with documentation",
        merit_type="social"
    ),
    Merit(
        name="Anonymity",
        min_value=1,
        max_value=5,
        description="Paper trail searches suffer -1 per dot",
        merit_type="social"
    ),
    Merit(
        name="Barfly",
        min_value=2,
        max_value=2,
        description="Blend into bar environments, rolls to identify as outsider penalized",
        merit_type="social",
        prerequisite="socialize:2"
    ),
    Merit(
        name="Closed Book",
        min_value=1,
        max_value=5,
        description="Add Merit dots as additional Doors in Social Maneuvering",
        merit_type="social",
        prerequisite="manipulation:3,resolve:3"
    ),
    Merit(
        name="Contacts",
        min_value=1,
        max_value=5,
        description="Information sources in various spheres",
        merit_type="social"
    ),
    Merit(
        name="Fame",
        min_value=1,
        max_value=3,
        description="Public recognition, bonus dice to impressed Social rolls",
        merit_type="social"
    ),
    Merit(
        name="Fixer",
        min_value=2,
        max_value=2,
        description="Reduce service Availability by one dot",
        merit_type="social",
        prerequisite="contacts:2,wits:3"
    ),
    Merit(
        name="Hobbyist Clique",
        min_value=2,
        max_value=2,
        description="9-again quality and +2 dice on chosen Skill",
        merit_type="social",
        prerequisite="clique_membership:1,chosen_skill:2"
    ),
    Merit(
        name="Inspiring",
        min_value=3,
        max_value=3,
        description="Grant Inspired Condition to listeners",
        merit_type="social",
        prerequisite="presence:3"
    ),
    Merit(
        name="Iron Will",
        min_value=2,
        max_value=2,
        description="Use Resolve instead of Willpower in Social contests",
        merit_type="social",
        prerequisite="resolve:4"
    ),
    Merit(
        name="Mentor",
        min_value=1,
        max_value=5,
        description="Teacher/advisor with chosen Skills or Resources",
        merit_type="social"
    ),
    Merit(
        name="Mystery Cult Initiation",
        min_value=1,
        max_value=5,
        description="Membership in esoteric organization",
        merit_type="social"
    ),
    Merit(
        name="Pusher",
        min_value=1,
        max_value=1,
        description="Improve Impression when mark accepts soft leverage",
        merit_type="social",
        prerequisite="persuasion:2"
    ),
    Merit(
        name="Resources",
        min_value=1,
        max_value=5,
        description="Disposable income for purchases",
        merit_type="social"
    ),
    Merit(
        name="Retainer",
        min_value=1,
        max_value=5,
        description="Loyal assistant/servant",
        merit_type="social"
    ),
    Merit(
        name="Safe Place",
        min_value=1,
        max_value=5,
        description="Secure location with Initiative bonus and breach penalties",
        merit_type="social"
    ),
    Merit(
        name="Small Unit Tactics",
        min_value=2,
        max_value=2,
        description="Grant Willpower bonus to multiple allies in coordinated actions",
        merit_type="social",
        prerequisite="presence:3"
    ),
    Merit(
        name="Spin Doctor",
        min_value=1,
        max_value=1,
        description="Reduce Tainted Clue penalties",
        merit_type="social",
        prerequisite="manipulation:3,subterfuge:2"
    ),
    Merit(
        name="Staff",
        min_value=1,
        max_value=5,
        description="Crew that automatically succeeds at mundane tasks",
        merit_type="social"
    ),
    Merit(
        name="Status",
        min_value=1,
        max_value=5,
        description="Standing in organization, can block others' Merits",
        merit_type="social"
    ),
    Merit(
        name="Striking Looks",
        min_value=1,
        max_value=2,
        description="Bonus dice to Social rolls influenced by appearance",
        merit_type="social"
    ),
    Merit(
        name="Sympathetic",
        min_value=2,
        max_value=2,
        description="Accept Condition to eliminate two Doors in Social Maneuvering",
        merit_type="social"
    ),
    Merit(
        name="Table Turner",
        min_value=1,
        max_value=1,
        description="Preempt Social Maneuvering with own action",
        merit_type="social",
        prerequisite="composure:3,manipulation:3,wits:3"
    ),
    Merit(
        name="Takes One to Know One",
        min_value=1,
        max_value=1,
        description="+2 and 9-again when investigating crime matching Vice",
        merit_type="social"
    ),
    Merit(
        name="Taste",
        min_value=1,
        max_value=1,
        description="Identify details in artistry and craftsmanship",
        merit_type="social",
        prerequisite="crafts:2,specialty:1"
    ),
    Merit(
        name="True Friend",
        min_value=3,
        max_value=3,
        description="Unbreakable relationship, regain Willpower from interaction",
        merit_type="social"
    ),
    Merit(
        name="Untouchable",
        min_value=1,
        max_value=1,
        description="Investigation rolls suffer Incomplete Clue unless exceptional success",
        merit_type="social",
        prerequisite="manipulation:3,subterfuge:2"
    )
]

# Supernatural Merits
supernatural_merits = [
    Merit(
        name="Aura Reading",
        min_value=3,
        max_value=3,
        description="Perceive auras to read emotional state and supernatural nature",
        merit_type="supernatural"
    ),
    Merit(
        name="Automatic Writing",
        min_value=2,
        max_value=2,
        description="Spirit possession for mysterious clues",
        merit_type="supernatural"
    ),
    Merit(
        name="Biokinesis",
        min_value=1,
        max_value=5,
        description="Shift Physical Attributes, enhanced healing",
        merit_type="supernatural"
    ),
    Merit(
        name="Clairvoyance",
        min_value=3,
        max_value=3,
        description="Project senses to another location",
        merit_type="supernatural"
    ),
    Merit(
        name="Cursed",
        min_value=2,
        max_value=2,
        description="Aware of fate, +2 to resist fear, extra Beats when near death",
        merit_type="supernatural"
    ),
    Merit(
        name="Laying on Hands",
        min_value=3,
        max_value=3,
        description="Faith healing at cost to self",
        merit_type="supernatural"
    ),
    Merit(
        name="Medium",
        min_value=3,
        max_value=3,
        description="Communicate with and influence ghosts",
        merit_type="supernatural",
        prerequisite="empathy:2"
    ),
    Merit(
        name="Mind of a Madman",
        min_value=2,
        max_value=2,
        description="8-again investigating specific culprit, traumatic dreams",
        merit_type="supernatural",
        prerequisite="empathy:3"
    ),
    Merit(
        name="Numbing Touch",
        min_value=1,
        max_value=5,
        description="Psychic paralysis and Willpower drain",
        merit_type="supernatural"
    ),
    Merit(
        name="Omen Sensitivity",
        min_value=3,
        max_value=3,
        description="Interpret signs for yes/no questions, causes obsession",
        merit_type="supernatural"
    ),
    Merit(
        name="Psychokinesis",
        min_value=3,
        max_value=5,
        description="Manipulate specific force (fire, cold, electricity, etc.)",
        merit_type="supernatural"
    ),
    Merit(
        name="Psychometry",
        min_value=3,
        max_value=3,
        description="Read emotional impressions from objects",
        merit_type="supernatural"
    ),
    Merit(
        name="Telekinesis",
        min_value=1,
        max_value=5,
        description="Move objects with mind, dots = effective Strength",
        merit_type="supernatural"
    ),
    Merit(
        name="Telepathy",
        min_value=3,
        max_value=5,
        description="Read surface thoughts, send messages at 5 dots",
        merit_type="supernatural"
    ),
    Merit(
        name="Thief of Fate",
        min_value=3,
        max_value=3,
        description="Steal luck from touched targets",
        merit_type="supernatural"
    ),
    Merit(
        name="Unseen Sense",
        min_value=2,
        max_value=2,
        description="Sixth sense for chosen supernatural creature type",
        merit_type="supernatural"
    )
]

# Style/Fighting Merits
style_merits = [
    Merit(
        name="Armed Defense",
        min_value=1,
        max_value=5,
        description="Defensive techniques with weapons",
        merit_type="style",
        prerequisite="dexterity:3,weaponry:2,defensive_combat_weaponry:1"
    ),
    Merit(
        name="Close Quarters Combat",
        min_value=1,
        max_value=5,
        description="Environmental combat techniques",
        merit_type="style",
        prerequisite="wits:3,athletics:2,brawl:3"
    ),
    Merit(
        name="Defensive Combat",
        min_value=1,
        max_value=1,
        description="Use Brawl or Weaponry for Defense calculation",
        merit_type="fighting",
        prerequisite="[brawl:1,weaponry:1]"
    ),
    Merit(
        name="Fighting Finesse",
        min_value=2,
        max_value=2,
        description="Use Dexterity instead of Strength for chosen weapon",
        merit_type="fighting",
        prerequisite="dexterity:3,weapon_specialty:1"
    ),
    Merit(
        name="Firefight",
        min_value=1,
        max_value=3,
        description="Mobile gunfighting techniques",
        merit_type="style",
        prerequisite="composure:3,dexterity:3,athletics:2,firearms:2"
    ),
    Merit(
        name="Grappling",
        min_value=1,
        max_value=3,
        description="Wrestling and grappling martial arts",
        merit_type="style",
        prerequisite="stamina:3,strength:2,athletics:2,brawl:2"
    ),
    Merit(
        name="Heavy Weapons",
        min_value=1,
        max_value=5,
        description="Two-handed weapon techniques",
        merit_type="style",
        prerequisite="stamina:3,strength:3,athletics:2,weaponry:2"
    ),
    Merit(
        name="Improvised Weaponry",
        min_value=1,
        max_value=3,
        description="Using environmental objects as weapons",
        merit_type="style",
        prerequisite="wits:3,weaponry:1"
    ),
    Merit(
        name="Iron Skin",
        min_value=2,
        max_value=4,
        description="Armor against bashing, downgrade lethal damage",
        merit_type="fighting",
        prerequisite="[martial_arts:2,street_fighting:2],stamina:3"
    ),
    Merit(
        name="Light Weapons",
        min_value=1,
        max_value=5,
        description="Finesse techniques with small weapons",
        merit_type="style",
        prerequisite="[wits:3,fighting_finesse:1],dexterity:3,athletics:2,weaponry:2"
    ),
    Merit(
        name="Marksmanship",
        min_value=1,
        max_value=4,
        description="Precision shooting techniques",
        merit_type="style",
        prerequisite="composure:3,resolve:3,firearms:2"
    ),
    Merit(
        name="Martial Arts",
        min_value=1,
        max_value=5,
        description="Formal martial arts training",
        merit_type="style",
        prerequisite="resolve:3,dexterity:3,athletics:2,brawl:2"
    ),
    Merit(
        name="Parkour",
        min_value=1,
        max_value=5,
        description="Free running and urban movement",
        merit_type="style",
        prerequisite="dexterity:3,athletics:2"
    ),
    Merit(
        name="Police Tactics",
        min_value=1,
        max_value=3,
        description="Law enforcement restraint techniques",
        merit_type="style",
        prerequisite="brawl:2,weaponry:1"
    ),
    Merit(
        name="Stunt Driver",
        min_value=1,
        max_value=4,
        description="Advanced driving maneuvers",
        merit_type="style",
        prerequisite="dexterity:3,drive:3,wits:3"
    ),
    Merit(
        name="Street Fighting",
        min_value=1,
        max_value=5,
        description="Dirty fighting techniques",
        merit_type="style",
        prerequisite="stamina:3,composure:3,brawl:2,streetwise:2"
    ),
    Merit(
        name="Unarmed Defense",
        min_value=1,
        max_value=5,
        description="Defensive unarmed combat techniques",
        merit_type="style",
        prerequisite="dexterity:3,brawl:2,defensive_combat_brawl:1"
    ),
    Merit(
        name="Cheap Shot",
        min_value=2,
        max_value=2,
        description="Dirty tricks to remove opponent's Defense",
        merit_type="fighting",
        prerequisite="street_fighting:3,subterfuge:2"
    ),
    Merit(
        name="Choke Hold",
        min_value=2,
        max_value=2,
        description="Unconsciousness through grappling",
        merit_type="fighting",
        prerequisite="brawl:2"
    ),
    Merit(
        name="Shiv",
        min_value=1,
        max_value=2,
        description="Conceal small weapons, use with Brawl",
        merit_type="fighting",
        prerequisite="street_fighting:2,weaponry:1"
    )
]

# Combine all merits
all_merits = mental_merits + physical_merits + social_merits + supernatural_merits + style_merits

# Create dictionary for easy lookup
merits_dict = {merit.name.lower().replace(" ", "_"): merit for merit in all_merits}