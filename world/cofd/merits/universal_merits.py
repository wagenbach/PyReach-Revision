from world.cofd.stat_types import Merit

# Universal (Available to All Characters) Merits
universal_merits = [
    #Mental Merits
    Merit(
        name="Advanced Library",
        min_value=1,
        max_value=5,
        description="Your library is vast enough to contain useful, direct information about supernatural topics. Choose a topic per Advanced Library dot. Every story, once per topic, you can take the Informed Condition when you consult your library about that topic.",
        merit_type="universal",
        prerequisite="library:3,safe_place>=advanced_library",
        book="MtA2e 105"
    ),
    Merit(
        name="Area of Expertise",
        min_value=1,
        max_value=1,
        description="Raise one Specialty's die bonus to +2",
        merit_type="universal",
        prerequisite="resolve:2",
        book="CofD 44"
    ),
    Merit(
        name="Common Sense",
        min_value=3,
        max_value=3,
        description="Once per chapter, roll Wits + Composure as an instant action to ask the Storyteller a question about risks and choices.",
        merit_type="universal",
        prerequisite="",
        book="CofD 44"
    ),
    Merit(
        name="Danger Sense",
        min_value=2,
        max_value=2,
        description="+2 bonus to detect an ambush.",
        merit_type="universal",
        prerequisite="",
        book="CofD 44"
    ),
    Merit(
        name="Direction Sense",
        min_value=1,
        max_value=1,
        description="Keep perfect track of your relative location and direction, and ignore penalties to navigate or find your way.",
        merit_type="universal",
        prerequisite="",
        book="CofD 44"
    ),
    Merit(
        name="Eidetic Memory",
        min_value=2,
        max_value=2,
        description="Ignore rolls for recall or memory. +2 bonus to recall minute facts buried in other information.",
        merit_type="universal",
        prerequisite="",
        book="CofD 44"
    ),
    Merit(
        name="Encyclopedic Knowledge",
        min_value=2,
        max_value=2,
        description="Roll Intelligence + Wits to recall useful trivia relating to a particular field or pursuit.",
        merit_type="universal",
        prerequisite="",
        book="CofD 44"
    ),
    Merit(
        name="Eye for the Strange",
        min_value=2,
        max_value=2,
        description="Roll Intelligence + Composure to identify evidence of supernatural involvement.",
        merit_type="universal",
        prerequisite="resolve:2,occult:1",
        book="CofD 44"
    ),
    Merit(
        name="Fast Reflexes",
        min_value=1,
        max_value=3,
        description="Add Fast Reflexes dots to Initiative",
        merit_type="universal",
        prerequisite="[wits:3,dexterity:3]",
        book="CofD 44"
    ),
    Merit(
        name="Good Time Management",
        min_value=1,
        max_value=1,
        description="Make extended action rolls in half the necessary time.",
        merit_type="universal",
        prerequisite="[academics:2,science:2]",
        book="CofD 44"
    ),
    Merit(
        name="Holistic Awareness",
        min_value=1,
        max_value=1,
        description="Roll Wits + Survival to substitute woodland scavengings for equipment when treating patients with Medicine, unless the patient suffers non-bashing wound penalties.",
        merit_type="universal",
        prerequisite="",
        book="CofD 44"
    ),
    Merit(
        name="Human Prey",
        min_value=2,
        max_value=2,
        description="Your nerves react instinctively to danger. When violence erupts, you may suffer Insane to boost Strength, suffer Beaten Down but gain 8-Again to flee, or suffer Stunned but recover Willpower.",
        merit_type="universal",
        prerequisite="",
        book="DtR 97"
    ),
    Merit(
        name="Hypervigilance",
        min_value=1,
        max_value=1,
        description="You're overly cautious of hidden dangers. Take 8-Again to perceive traps or ambushes, but on exceptional success, suffer Spooked.",
        merit_type="universal",
        prerequisite="",
        book="DtR 97"
    ),
    Merit(
        name="Indomitable",
        min_value=2,
        max_value=2,
        description="+2 to a contesting dice pool or resistance trait applied against supernatural mental influence.",
        merit_type="universal",
        prerequisite="resolve:3",
        book="CofD 45"
    ),
    Merit(
        name="Interdisciplinary Specialty",
        min_value=1,
        max_value=1,
        description="Choose a Specialty in the corresponding Skill. Apply the Specialty's bonus die to relevant rolls of any Skill, except unskilled rolls.",
        merit_type="universal",
        prerequisite="any_skill:3",
        book="CofD 45"
    ),
    Merit(
        name="Investigative Aide",
        min_value=1,
        max_value=1,
        description="When you roll the selected Skill to uncover clues, achieve exceptional success with only three successes. Add a bonus element to any clues uncovered with this Skill.",
        merit_type="universal",
        prerequisite="any_skill:3",
        book="CofD 45"
    ),
    Merit(
        name="Investigative Prodigy",
        min_value=1,
        max_value=5,
        description="When you roll to uncover clues, you uncover a clue per success, capped by your dots in Investigative Prodigy. Clues from extra successes never have more than one element each.",
        merit_type="universal",
        prerequisite="wits:3,investigation:3",
        book="CofD 45"
    ),
    Merit(
        name="Language",
        min_value=1,
        max_value=1,
        description="You can speak, read and write in a chosen language.",
        merit_type="universal",
        prerequisite="",
        book="CofD 45"
    ),
    Merit(
        name="Library",
        min_value=1,
        max_value=3,
        description="You have a cache of information relating to a particular Skill. Add your dots in Library to relevant extended rolls.",
        merit_type="universal",
        prerequisite="",
        book="CofD 46"
    ),
    Merit(
        name="Lucid Dreamer",
        min_value=2,
        max_value=2,
        description="You may roll Resolve + Composure while asleep to dream lucidly, and may wake up at will.",
        merit_type="universal",
        prerequisite="resolve:3",
        book="CtD2e 123"
    ),
    Merit(
        name="Meditative Mind",
        min_value=1,
        max_value=4,
        description="Ignore environmental and wound penalties on meditation rolls. With two dots, meditation grants +3 to Resolve + Composure rolls for the remainder of the day. With four dots, meditation rolls only need to accumulate one success.",
        merit_type="universal",
        prerequisite="",
        book="CofD 46"
    ),
    Merit(
        name="Multilingual",
        min_value=1,
        max_value=1,
        description="You can speak conversationally in two chosen languages. Roll Intelligence + Academics for reading comprehension.",
        merit_type="universal",
        prerequisite="",
        book="CofD 46"
    ),
    Merit(
        name="Object Fetishism",
        min_value=1,
        max_value=5,
        description="You obsess over a given possession relating to a chosen Specialty. Recover Willpower each session from your obsession, and spending Willpower to roll that Specialty exaggerates both failure and success.",
        merit_type="universal",
        prerequisite="",
        book="HL 42"
    ),
    Merit(
        name="Patient",
        min_value=1,
        max_value=1,
        description="Add +2 to your maximum number of allowed rolls on extended actions.",
        merit_type="universal",
        prerequisite="",
        book="CofD 46"
    ),
    Merit(
        name="Renowned Artisan",
        min_value=3,
        max_value=3,
        description="You've been taught the ways of an ancient Iremite guild. Once per chapter, you may reroll a relevant Crafts action.",
        merit_type="universal",
        prerequisite="crafts:3,skill_specialty:1",
        book="MtC2e 113"
    ),
    Merit(
        name="Scarred",
        min_value=1,
        max_value=1,
        description="Suffer a Persistent Condition which prevents you from recovering Integrity, but inures you from a particular breaking point.",
        merit_type="universal",
        prerequisite="integrity<=5",
        book="HL 43"
    ),
    Merit(
        name="Tolerance for Biology",
        min_value=1,
        max_value=1,
        description="Ignore Resistance rolls from witnessing biological grotesquerie.",
        merit_type="universal",
        prerequisite="resolve:3",
        book="CofD 46"
    ),
    Merit(
        name="Trained Observer",
        min_value=1,
        max_value=3,
        description="Take 9-again, or 8-again with three dots, on Perception rolls.",
        merit_type="universal",
        prerequisite="[wits:3,composure:3]",
        book="CofD 46"
    ),
    Merit(
        name="Vice-Ridden",
        min_value=2,
        max_value=2,
        description="Take a second Vice.",
        merit_type="universal",
        prerequisite="vice",
        book="CofD 46"
    ),
    Merit(
        name="Virtuous",
        min_value=2,
        max_value=2,
        description="Take a second Virtue.",
        merit_type="universal",
        prerequisite="virtue",
        book="CofD 46"
    ),
    #Physical Merits
    Merit(
        name="Ambidextrous",
        min_value=3,
        max_value=3,
        description="Ignore offhand penalties. Character creation only.",
        merit_type="universal",
        prerequisite="",
        book="CofD 47"
    ),
    Merit(
        name="Automotive Genius",
        min_value=1,
        max_value=1,
        description="Raise maximum modifications to a vehicle to thrice Crafts rating, plus number of relevant Crafts Specialties.",
        merit_type="universal",
        prerequisite="crafts:3,drive:1,science:1",
        book="CofD 47"
    ),
    Merit(
        name="Covert Operative",
        min_value=1,
        max_value=1,
        description="When launching an ambush, deny 10-again to notice it, and take +3 Initiative on the first turn.",
        merit_type="universal",
        prerequisite="wits:3,dexterity:3,stealth:2",
        book="HL 53"
    ),
    Merit(
        name="Crack Driver",
        min_value=2,
        max_value=3,
        description="When not taking any non-Drive actions, add your Composure as a bonus to Drive rolls, and penalize attempts to disable your vehicle by your Composure. With three dots, you can take a reflexive Drive action once per turn.",
        merit_type="universal",
        prerequisite="drive:3",
        book="CofD 47"
    ),
    Merit(
        name="Demolisher",
        min_value=1,
        max_value=3,
        description="When breaking objects, ignore a point of Durability per dot of Demolisher.",
        merit_type="universal",
        prerequisite="[strength:3,intelligence:3]",
        book="CofD 47"
    ),
    Merit(
        name="Double Jointed",
        min_value=2,
        max_value=2,
        description="Dislodge joints at will. Escape from mundane bondage automatically. When grappled and not acting aggressively, penalize your attacker's overpowering rolls by your Dexterity.",
        merit_type="universal",
        prerequisite="dexterity:3",
        book="CofD 47"
    ),
    Merit(
        name="Fleet of Foot",
        min_value=1,
        max_value=3,
        description="Add dots in Fleet of Foot to your Speed, and penalize pursuit rolls in a foot chase by your Fleet of Foot dots.",
        merit_type="universal",
        prerequisite="athletics:2",
        book="CofD 47"
    ),
    Merit(
        name="Freediving",
        min_value=1,
        max_value=1,
        description="Add Athletics to Stamina when holding a deep breath, and succeed exceptionally on three successes to fight the gasp reflex.",
        merit_type="universal",
        prerequisite="athletics:2",
        book="DtR 99"
    ),
    Merit(
        name="Giant",
        min_value=3,
        max_value=3,
        description="+1 Size. Character creation only.",
        merit_type="universal",
        prerequisite="",
        book="CofD 47"
    ),
    Merit(
        name="Greyhound",
        min_value=1,
        max_value=1,
        description="Succeed exceptionally on three successes in a chase action.",
        merit_type="universal",
        prerequisite="athletics:3,wits:3,stamina:3",
        book="CofD 48"
    ),
    Merit(
        name="Hardy",
        min_value=1,
        max_value=3,
        description="Add Hardy dots as a bonus to rolls against disease, poison, deprivation, suffocation and unconsciousness.",
        merit_type="universal",
        prerequisite="stamina:3",
        book="CofD 47"
    ),
    Merit(
        name="Iron Stamina",
        min_value=1,
        max_value=3,
        description="Ignore penalties from fatigue or wounds up to your rating in Iron Stamina.",
        merit_type="universal",
        prerequisite="[stamina:3,resolve:3]",
        book="CofD 48"
    ),
    Merit(
        name="Punch Drunk",
        min_value=2,
        max_value=2,
        description="Spend Willpower to preserve your last Health point, upgrading preexisting damage instead.",
        merit_type="universal",
        prerequisite="willpower:6",
        book="HL 43"
    ),
    Merit(
        name="Relentless",
        min_value=1,
        max_value=1,
        description="Add 2 to the successes needed against you in a chase.",
        merit_type="universal",
        prerequisite="athletics:2,stamina:3",
        book="CofD 49"
    ),
    Merit(
        name="Roadkill",
        min_value=3,
        max_value=3,
        description="When you try and run someone over, Knock Down even if you miss, and double your velocity bonus.",
        merit_type="universal",
        prerequisite="aggressive_driving:2",
        book="HL 55"
    ),
    Merit(
        name="Seizing The Edge",
        min_value=2,
        max_value=2,
        description="You get the Edge in the first turn of a chase, and if your opponent fails a roll as if being ambushed, you can calculate your target successes without their Speed or Initiative.",
        merit_type="universal",
        prerequisite="wits:3,composure:3",
        book="CofD 49"
    ),
    Merit(
        name="Sleight of Hand",
        min_value=2,
        max_value=2,
        description="You can take a Larceny instant action reflexively once per turn, and victims of your Larceny can't notice your attempts if they aren't specifically looking for them.",
        merit_type="universal",
        prerequisite="larceny:3",
        book="CofD 49"
    ),
    Merit(
        name="Small-Framed",
        min_value=2,
        max_value=2,
        description="-1 Size. Take a +2 bonus to hide, go unnoticed, or otherwise benefit from your size. Character creation only.",
        merit_type="universal",
        prerequisite="",
        book="CofD 49"
    ),
    Merit(
        name="Survivalist",
        min_value=1,
        max_value=1,
        description="You can resist Extreme Cold and Extreme Heat for hours equal to your Stamina.",
        merit_type="universal",
        prerequisite="survival:3,iron_stamina:3",
        book="HL 43"
    ),
    #Social Merits
    Merit(
        name="Air of Menace",
        min_value=2,
        max_value=2,
        description="You wear a history of violence on your sleeve. +2 to menace others, and less rough characters must spend Willpower to pick a fight, but social maneuvering is harder.",
        merit_type="universal",
        prerequisite="intimidation:2",
        book="HL 41"
    ),
    Merit(
        name="Allies",
        min_value=1,
        max_value=5,
        description="You have influence and goodwill with a chosen group proportional to your dots in this Merit.",
        merit_type="universal",
        prerequisite="",
        book="CofD 49"
    ),
    Merit(
        name="Alternate Identity",
        min_value=1,
        max_value=3,
        description="You've laid groundwork establishing a false identity: an informal history with one dot, a veneer of documentation with two, or an airtight paper trail with three. +1 to Subterfuge rolls to maintain the false identity, or +2 with three dots.",
        merit_type="universal",
        prerequisite="",
        book="CofD 50"
    ),
    Merit(
        name="Anonymity",
        min_value=1,
        max_value=5,
        description="Penalize attempts to find you by paper trail or living evidence by a die per Anonymity dot.",
        merit_type="universal",
        prerequisite="fame:0",
        book="CofD 50"
    ),
    Merit(
        name="Barfly",
        min_value=2,
        max_value=2,
        description="You can get in anywhere socially. Penalize attempts to recognize you as out of place by your Socialize dots.",
        merit_type="universal",
        prerequisite="socialize:2",
        book="CofD 50"
    ),
    Merit(
        name="Beneath Notice",
        min_value=3,
        max_value=3,
        description="You appear as a servant and do not need to roll stealth around those who see you as of lower standing. Gain +3 to eavesdrop on those same people.",
        merit_type="universal",
        prerequisite="",
        book="GTTN 123"
    ),
    Merit(
        name="Closed Book",
        min_value=1,
        max_value=5,
        description="Add dots in this Merit to your number of Doors, and as a die bonus to contest Social assessment actions.",
        merit_type="universal",
        prerequisite="manipulation:3,resolve:3",
        book="CofD 50"
    ),
    Merit(
        name="Cohesive Unit",
        min_value=1,
        max_value=3,
        description="Confer +2 to teamwork. With two dots, confer bonus dice each scene. With three dots, confer rerolls.",
        merit_type="universal",
        prerequisite="presence:3",
        book="HL 42"
    ),
    Merit(
        name="Contacts",
        min_value=1,
        max_value=5,
        description="Choose a group or field for each dot of Contacts. You can roll Manipulation + (relevant Social Skill) to gather information or dirt from acquaintances in any of these groups or fields.",
        merit_type="universal",
        prerequisite="",
        book="CofD 50"
    ),
    Merit(
        name="Defender",
        min_value=1,
        max_value=3,
        description="Gain bonus Willpower to spend on protecting loved ones, but losing them causes a crisis of grief or retribution.",
        merit_type="universal",
        prerequisite="",
        book="HL 42"
    ),
    Merit(
        name="Den of Vice",
        min_value=2,
        max_value=2,
        description="Have a location that reflects your vice that allows you to recover all your willpower once per chapter. Anytime you use your vice to regain willpower normally, roll Stamina + Composure, gaining the Addicted condition on a failure.",
        merit_type="universal",
        prerequisite="",
        book="GTTN 124"
    ),
    Merit(
        name="Empath",
        min_value=2,
        max_value=2,
        description="Contest Wits + Empathy against Manipulation + Subterfuge for insight into a character's mental state, which can open Doors or ease breaking points.",
        merit_type="universal",
        prerequisite="empathy:2",
        book="HL 42"
    ),
    Merit(
        name="Fame",
        min_value=1,
        max_value=3,
        description="You're known for something, locally or selectively with one dot, broadly in an area with two dots, or universally with three. Add Fame dots as a die bonus to Social rolls targeting those impressed by your reputation, and to rolls by other characters to find or identify you.",
        merit_type="universal",
        prerequisite="anonymity:0",
        book="CofD 50"
    ),
    Merit(
        name="Fixer",
        min_value=2,
        max_value=2,
        description="Obtain services as if they were one Availability lower.",
        merit_type="universal",
        prerequisite="contacts:2,wits:3",
        book="CofD 51"
    ),
    Merit(
        name="Friends in Low Places",
        min_value=1,
        max_value=5,
        description="An alternate version of Status, focused on the dregs of society.",
        merit_type="universal",
        prerequisite="",
        book="GTTN 124"
    ),
    Merit(
        name="Hobbyist Clique",
        min_value=2,
        max_value=2,
        description="So long as you keep up with your fellow hobbyists, their support provides 9-Again to roll your hobby Skill, and a +2 die bonus to extended actions using that Skill.",
        merit_type="universal",
        prerequisite="any_skill:2",
        book="CofD 51"
    ),
    Merit(
        name="Inspiring",
        min_value=3,
        max_value=3,
        description="Roll Presence + Expression to confer the Inspired Condition.",
        merit_type="universal",
        prerequisite="presence:3",
        book="CofD 51"
    ),
    Merit(
        name="Iron Will",
        min_value=2,
        max_value=2,
        description="When you spend Willpower to contest or resist Social influence, substitute your Resolve rating for the usual Willpower bonus. If the roll is contested, take 8-Again.",
        merit_type="universal",
        prerequisite="resolve:4",
        book="CofD 51"
    ),
    Merit(
        name="Mentor",
        min_value=1,
        max_value=5,
        description="You have a guide who expects something from you proportional to his or her influence, as measured by your dots in Mentor. ",
        merit_type="universal",
        prerequisite="",
        book="CofD 51"
    ),
    Merit(
        name="Mobster",
        min_value=1,
        max_value=1,
        description="You become entangled in with organized crime. Gain access to areas controlled by the criminal organization the controls or favors you. You become a target for rivals.",
        merit_type="universal",
        prerequisite="",
        book="GTTN 124"
    ),
    Merit(
        name="Moonlighting",
        min_value=2,
        max_value=2,
        description="Once per story, gain 2 dots in Resources from your (probably illegal) side hustle.",
        merit_type="universal",
        prerequisite="",
        book="GTTN 124"
    ),
    Merit(
        name="Peacemaker",
        min_value=2,
        max_value=3,
        description="You can spend Willpower to attempt to negotiate a nonviolent end to hostilities through Social Maneuvering. With three dots, you can attempt to talk down even supernatural rages.",
        merit_type="universal",
        prerequisite="wits:3,empathy:3",
        book="HL 42"
    ),
    Merit(
        name="Pusher",
        min_value=1,
        max_value=1,
        description="When you use soft leverage, improve your impression as if you'd also satisfied the mark's Vice.",
        merit_type="universal",
        prerequisite="persuasion:2",
        book="CofD 53"
    ),
    Merit(
        name="Resources",
        min_value=1,
        max_value=5,
        description="You have disposable income proportional to your dots in this Merit, and can reach beyond your resources occasionally.",
        merit_type="universal",
        prerequisite="",
        book="CofD 53"
    ),
    Merit(
        name="Small Unit Tactics",
        min_value=2,
        max_value=2,
        description="Once per scene when you coordinate allies, you can spend Willpower as an instant action to confer the die bonus to a number of allies up to your Presence rating.",
        merit_type="universal",
        prerequisite="presence:3",
        book="CofD 54"
    ),
    Merit(
        name="Spin Doctor",
        min_value=1,
        max_value=1,
        description="Using Tainted Clues inflicts an additional -1 penalty instead of consuming any successes.",
        merit_type="universal",
        prerequisite="manipulation:3,subterfuge:2",
        book="CofD 54"
    ),
    Merit(
        name="Staff",
        min_value=1,
        max_value=5,
        description="You have employees corresponding to one Skill per dot of Staff. They can achieve a single automatic success at relevant actions using one of those Skills.",
        merit_type="universal",
        prerequisite="",
        book="CofD 54"
    ),
    Merit(
        name="Status",
        min_value=1,
        max_value=5,
        description="You have influence as part of a chosen group. You can draw on their facilities and resources, block the use of a relevant Social Merit lower than your Status rating once per session, and apply Status as a die bonus to Social rolls drawing on your influence.",
        merit_type="universal",
        prerequisite="",
        book="CofD 54"
    ),
    Merit(
        name="Striking Looks",
        min_value=1,
        max_value=2,
        description="Your appearance is noteworthy and memorable. Add Striking Looks as a die bonus to Social rolls that benefit from your appearance, and to rolls by other characters to notice or remember you.",
        merit_type="universal",
        prerequisite="",
        book="CofD 54"
    ),
    Merit(
        name="Support Network",
        min_value=1,
        max_value=5,
        description="Choose a Social Merit to represent supportive ties. You can spend Willpower to turn to those ties to weather a breaking point, using this Merit as bonus dice.",
        merit_type="universal",
        prerequisite="appropriate_social_merit:1",
        book="HL 43"
    ),
    Merit(
        name="Sympathetic",
        min_value=2,
        max_value=2,
        description="When you engage in Social Maneuvering, you can accept a Condition such as Leveraged or Swooning to immediately open two Doors.",
        merit_type="universal",
        prerequisite="",
        book="CofD 55"
    ),
    Merit(
        name="Table Turner",
        min_value=1,
        max_value=1,
        description="When targeted by Social Maneuvering, you can spend Willpower to preemptively respond with a Social action of your own.",
        merit_type="universal",
        prerequisite="composure:3,manipulation:3,wits:3",
        book="CofD 55"
    ),
    Merit(
        name="Takes One To Know One",
        min_value=1,
        max_value=1,
        description="When you investigate an incident that resonates with your Vice, instead of suffering the normal -2 penalty, your roll gains +2 dice and 9-Again. Succeeding on the roll satisfies your Vice.",
        merit_type="universal",
        prerequisite="vice",
        book="CofD 55"
    ),
    Merit(
        name="Taste",
        min_value=1,
        max_value=1,
        description="Choose a Specialty in Crafts or Expression. You can roll Wits + (Skill in question) to draw information about the nature of a work that falls within the chosen Specialty.",
        merit_type="universal",
        prerequisite="crafts:2",
        book="CofD 55"
    ),
    Merit(
        name="True Friend",
        min_value=3,
        max_value=3,
        description="You have an unbreakable bond of friendship with a chosen character. Rolls to influence your friend to your detriment suffer a -5 penalty. Once per story, you can recover one Willpower through a meaningful interaction with your friend.",
        merit_type="universal",
        prerequisite="",
        book="CofD 56"
    ),
    Merit(
        name="Tutelage",
        min_value=3,
        max_value=3,
        description="As either the student or teacher, meet your counterpart for a lesson once per story. The student gains 1 experience to be used towards purchasing the topic of the lesson, in exchange for a favor the teacher calls in. The Teacher gains a 1 experience reduction to the next purchase, in exchange for some kind of social trouble the student brings upon them.",
        merit_type="universal",
        prerequisite="",
        book="GTTN 127"
    ),
    Merit(
        name="Untouchable",
        min_value=1,
        max_value=1,
        description="You're a smooth criminal. Rolls to investigate your deeds must achieve an exceptional success or else turn up Incomplete Clues.",
        merit_type="universal",
        prerequisite="manipulation:3,subterfuge:2",
        book="CofD 56"
    ),
    #Supernatural Merits
    Merit(
        name="Esoteric Armory",
        min_value=1,
        max_value=5,
        description="You've collected enough esoterica to supply the banes of ephemeral entities with a Rank up to your rating in this Merit.",
        merit_type="universal",
        prerequisite="",
        book="CofD 139"
    ),
    Merit(
        name="Relic",
        min_value=1,
        max_value=5,
        description="You possess an incorruptible item sorcerously crafted with the world's life force, with unique cursed powers.",
        merit_type="universal",
        prerequisite="",
        book="MtC2e 113"
    ),
    Merit(
        name="Sandglass",
        min_value=2,
        max_value=2,
        description="Your soul can instinctively roll Wits + Composure to sense ripples in the waters of time like the Arisen, spending Willpower instead of Pillars and Willpower dots instead of Sekhem.",
        merit_type="universal",
        prerequisite="",
        book="MtC2e 114"
    ),
    Merit(
        name="Vestige",
        min_value=1,
        max_value=5,
        description="You possess vessels for the world's life force which can be called upon for cursed strength.",
        merit_type="universal",
        prerequisite="",
        book="MtC2e 116"
    ),
    #Fighting Merits
    Merit(
        name="Armed Restraint",
        min_value=2,
        max_value=2,
        description="Use a hooking pole when grappling to instantly Hold and penalize your opponent by its weapon rating.",
        merit_type="universal",
        prerequisite="staff_fighting:3",
        book="HL 53"
    ),
    Merit(
        name="Body As Weapon",
        min_value=2,
        max_value=2,
        description="Unarmed strikes add one point of bashing damage on a successful hit.",
        merit_type="universal",
        prerequisite="stamina:3,brawl:2",
        book="HL 41"
    ),
    Merit(
        name="Boot Party",
        min_value=2,
        max_value=2,
        description="Attack a prone target at -3 to deal lethal damage unarmed.",
        merit_type="universal",
        prerequisite="brawl:2",
        book="HL 53"
    ),
    Merit(
        name="Cheap Shot",
        min_value=2,
        max_value=2,
        description="During a fight, you can reflexively contest Dexterity + Subterfuge against Wits + Composure to deny an opponent Defense next turn through dirty tricks and distractions.",
        merit_type="universal",
        prerequisite="street_fighting:3,subterfuge:2",
        book="CofD 61"
    ),
    Merit(
        name="Choke Hold",
        min_value=2,
        max_value=2,
        description="After a successful Hold, add the Choke grapple maneuver: accumulates successes across multiple turns to knock unconscious for a few minutes.",
        merit_type="universal",
        prerequisite="brawl:2",
        book="CoFD 61"
    ),
    Merit(
        name="Clinch Strike",
        min_value=1,
        max_value=1,
        description="Use the Damage maneuver instantly in a grapple.",
        merit_type="universal",
        prerequisite="brawl:2",
        book="HL 53"
    ),
    Merit(
        name="Defensive Combat",
        min_value=1,
        max_value=1,
        description="You can substitute the chosen Skill for Athletics when calculating your Defense, as long as you're currently equipped to make attacks with that Skill.",
        merit_type="universal",
        prerequisite="[brawl:1,weaponry:1]",
        book="CofD 61"
    ),
    Merit(
        name="Fighting Finesse",
        min_value=2,
        max_value=2,
        description="You can substitute Dexterity for Strength when making rolls with a chosen Brawl or Weaponry Specialty.",
        merit_type="universal",
        prerequisite="dexterity:3",
        book="CofD 61"
    ),
    Merit(
        name="Ground and Pound",
        min_value=3,
        max_value=3,
        description="Take the rote quality to strike a prone target with Brawl, falling prone yourself.",
        merit_type="universal",
        prerequisite="brawl:2",
        book="HL 54"
    ),
    Merit(
        name="Ground Fighter",
        min_value=3,
        max_value=3,
        description="Deny close combat bonuses from being prone, and gain the Stand Up grapple maneuver.",
        merit_type="universal",
        prerequisite="wits:3,dexterity:3,brawl:2",
        book="HL 54"
    ),
    Merit(
        name="Headbutt",
        min_value=1,
        max_value=1,
        description="Gain the Headbutt grapple maneuver; inflict Stunned.",
        merit_type="universal",
        prerequisite="brawl:2",
        book="HL 54"
    ),
    Merit(
        name="Iron Chin",
        min_value=2,
        max_value=4,
        description="Don't suffer Beaten Down from bashing damage. With four dots, never suffer Beaten Down.",
        merit_type="universal",
        prerequisite="resolve:3,stamina:3",
        book="HL 54"
    ),
    Merit(
        name="Iron Skin",
        min_value=2,
        max_value=4,
        description="Confers half your Iron Skin dots in points of general Armor against bashing attacks. When hurt, you can spend Willpower to reduce half your Iron Skin dots in lethal damage to bashing.",
        merit_type="universal",
        prerequisite="[martial_arts:2,street_fighting:2],stamina:3",
        book="CofD 63"
    ),
    Merit(
        name="Loaded for Bear",
        min_value=1,
        max_value=2,
        description="Gain extra reloads on weapons, including single shot weapons.",
        merit_type="universal",
        prerequisite="athletics:1,survival:1",
        book="HL 143"
    ),
    Merit(
        name="Phalanx Fighter",
        min_value=2,
        max_value=2,
        description="Wield a spear with a shield, substituting it in Weapon and Shield maneuvers.",
        merit_type="universal",
        prerequisite="weapon_and_shield:2,spear_and_bayonet:1",
        book="HL 54"
    ),
    Merit(
        name="Retain Weapon",
        min_value=2,
        max_value=2,
        description="Reduce successes on a Control Weapon or Disarm maneuver against you by your Brawl.",
        merit_type="universal",
        prerequisite="wits:2,brawl:2",
        book="HL 54"
    ),
    Merit(
        name="Shiv",
        min_value=1,
        max_value=2,
        description="You can conceal a 0L brawling weapon with one dot, or 1L with two, on your person. Penalize rolls to detect it by your Weaponry.",
        merit_type="universal",
        prerequisite="street_fighting:2,weaponry:1",
        book="CoFD 64"
    ),
    Merit(
        name="Subduing Strikes",
        min_value=1,
        max_value=1,
        description="You can pull blows with a weapon to deal bashing damage without spending Willpower.",
        merit_type="universal",
        prerequisite="weaponry:2",
        book="DE 247"
    ),
    Merit(
        name="Transfer Maneuver",
        min_value=1,
        max_value=3,
        description="Cross-apply a Brawling maneuver to a Weaponry Style, or vice-versa.",
        merit_type="universal",
        prerequisite="intelligence:2,wits:3,brawl:2,weaponry:2",
        book=""
    ),
    Merit(
        name="Trigger Discipline",
        min_value=1,
        max_value=1,
        description="Increase a firearm's effective capacity, or allow an additional long burst at high capacity.",
        merit_type="universal",
        prerequisite="wits:2,firearms:2",
        book="HL 143"
    ),
    Merit(
        name="Trunk Squeeze",
        min_value=2,
        max_value=2,
        description="Gain the Trunk Squeeze grapple maneuver: deal bashing damage and cumulatively penalize the opponent's contesting rolls.",
        merit_type="universal",
        prerequisite="brawl:2",
        book="HL 54"
    ),
]

# Create dictionary for easy lookup
universal_merits_dict = {merit.name.lower().replace(" ", "_").replace("(", "").replace(")", ""): merit for merit in universal_merits}
