from world.cofd.stat_types import Merit

# Changeling-Specific Merits
changeling_merits = [
    Merit(
        name="Acute Senses",
        min_value=1,
        max_value=1,
        description="Double the range and acuity of your senses. Apply your Wyrd as bonus dice to perception rolls and rolls to identify or recall details.",
        merit_type="changeling",
        prerequisite="[wits:3,composure:3]",
        book="CtL2e 111"
    ),
    Merit(
        name="Arcadian Metabolism",
        min_value=2,
        max_value=2,
        description="Heal bashing damage each minute of rest and lethal damage daily in the Hedge.",
        merit_type="changeling",
        prerequisite="",
        book="CtL2e 111"
    ),
    Merit(
        name="Brownie's Boon",
        min_value=1,
        max_value=1,
        description=" 	Extended actions outside the sight of witnesses occur at twice the speed (half intervals), or spend Glamour for four times the speed.",
        merit_type="changeling",
        prerequisite="",
        book="CtL2e 111"
    ),
    Merit(
        name="Cloak of Leaves",
        min_value=1,
        max_value=3,
        description="Apply dots of this Merit as a penalty to supernatural abilities used to physically harm you.",
        merit_type="changeling",
        prerequisite="autumn_mantle:3",
        book="CtL2e 111"
    ),
    Merit(
        name="Cold Hearted",
        min_value=3,
        max_value=3,
        description="Spend Willpower to ignore the effects of a Clarity Condition briefly.",
        merit_type="changeling",
        prerequisite="winter_mantle:3",
        book="CtL2e 111"
    ),
    Merit(
        name="Court Goodwill",
        min_value=1,
        max_value=5,
        description="You have the good favor of another Court's courtiers and patron. Functions like the Allies Merit at equal rating, the Court Mantle at two dots lower, and as a one-dot Mentor.",
        merit_type="changeling",
        prerequisite="",
        book="CtL2e 112"
    ),
    Merit(
        name="Defensive Dreamscaping",
        min_value=2,
        max_value=2,
        description="Add half Wyrd, rounded down, to your Defense in Dream Form.",
        merit_type="changeling",
        prerequisite="",
        book="CtL2e 112"
    ),
    Merit(
        name="Diviner",
        min_value=1,
        max_value=5,
        description="Once per session for each dot in this Merit, comb your dreams for answers and ask the Storyteller a yes or no question.",
        merit_type="beast",
        prerequisite="composure:3,wits:3",
        book="CtL2e 112"
    ),
    Merit(
        name="Dream Warrior",
        min_value=1,
        max_value=1,
        description="When you allocate successes from one of the named Skills in which you have a Specialty to perform subtle oneiromantic shifts in aid of combat, add a bonus success.",
        merit_type="changeling",
        prerequisite="wyrd:2,[presence:3,manipulation:3,composure:3],skill_specialty:1",
        book="CtL2e 112"
    ),
    Merit(
        name="Dreamweaver",
        min_value=3,
        max_value=3,
        description="Once a scene, spend Willpower to achieve a dreamweaving exceptional success on a threshold of three instead of five.",
        merit_type="changeling",
        prerequisite="wyrd:3",
        book="CtL2e 113"
    ),
    Merit(
        name="Dull Beacon",
        min_value=1,
        max_value=5,
        description="When you drop the Mask, open the Hedge as if your Wyrd were reduced by dots in this Merit, to a minimum of 0.",
        merit_type="changeling",
        prerequisite="",
        book="CtL2e 113"
    ),
    Merit(
        name="Fae Mount",
        min_value=1,
        max_value=5,
        description="You've befriended and trained a loyal Hedge denizen and can call it at will there. Each dot in this Merit gives your mount one of a set of gifts, such as natural armor or the ability to exit the Hedge under a Mask.",
        merit_type="changeling",
        prerequisite="",
        book="CtL2e 113"
    ),
    Merit(
        name="Faerie Favor",
        min_value=3,
        max_value=3,
        description="You possess an owed favor from one of the Gentry in the form of a bauble, though cashing it in will render Notoriety for your questionable dealing.",
        merit_type="changeling",
        prerequisite="",
        book="CtL2e 114"
    ),
    Merit(
        name="Fair Harvest",
        min_value=1,
        max_value=2,
        description="You favor one emotional flavor of Glamour over others. Take 8-Again, or with two dots the rote quality, to harvest it, but lose 10-Again, and with two dots subtract a success, to harvest others.",
        merit_type="changeling",
        prerequisite="",
        book="CtL2e 114"
    ),
    Merit(
        name="Firebrand",
        min_value=2,
        max_value=2,
        description="Once a scene, recover Willpower by inciting a fight.",
        merit_type="changeling",
        prerequisite="summer_mantle:3",
        book="CtL2e 115"
    ),
    Merit(
        name="Frightful Incantation",
        min_value=4,
        max_value=4,
        description="Can use Mantle and Mein in place of a hecatomb, opening Doors up to Mantle rating each story.",
        merit_type="changeling",
        prerequisite="hedge_sorcerer,mantle:2,resolve:2",
        book="Hedge 69"
    ),
    Merit(
        name="Gentrified Bearing",
        min_value=2,
        max_value=2,
        description="Hobs are cautious that you might be Gentry. Add your Wyrd as an Intimidation bonus.",
        merit_type="changeling",
        prerequisite="wyrd:2",
        book="CtL2e 115"
    ),
    Merit(
        name="Glamour Fasting",
        min_value=1,
        max_value=1,
        description="Glamour deprivation doesn't set in for one full session unless you exhaust your Willpower.",
        merit_type="changeling",
        prerequisite="",
        book="CtL2e 115"
    ),
    Merit(
        name="Goblin Bounty",
        min_value=1,
        max_value=5,
        description="Each session you have access to three common goblin fruits or oddments for each dot in this Merit.",
        merit_type="changeling",
        prerequisite="",
        book="CtL2e 115"
    ),
    Merit(
        name="Grounded",
        min_value=3,
        max_value=3,
        description="Apply a point of Armor against mild Clarity damage.",
        merit_type="changeling",
        prerequisite="",
        book="CtL2e 115"
    ),
    Merit(
        name="Hedge Brawler",
        min_value=2,
        max_value=2,
        description="Take up to a -3 attack penalty to gain, on success, an equal number of Hedgespinning successes.",
        merit_type="changeling",
        prerequisite="[brawl:2,firearms:2,weaponry:2]",
        book="CtL2e 115"
    ),
    Merit(
        name="Hedge Sense",
        min_value=1,
        max_value=1,
        description="+2 to navigate or search the Hedge.",
        merit_type="changeling",
        prerequisite="",
        book="CtL2e 115"
    ),
    Merit(
        name="Hedge Sorcerer",
        min_value=4,
        max_value=4,
        description="You can perform Hedge Sorcery rituals.",
        merit_type="changeling",
        prerequisite="occult:1,mentor:2",
        book="Hedge 66"
    ),
    Merit(
        name="Hedgewise",
        min_value=2,
        max_value=2,
        description="+2 to ken even magically concealed Hedgeways, and 9-again to Hedgespinning.",
        merit_type="changeling",
        prerequisite="",
        book="DE2 75"
    ),
    Merit(
        name="Hob Kin",
        min_value=1,
        max_value=1,
        description="You benefit from a better impression from hobs you meet.",
        merit_type="changeling",
        prerequisite="",
        book="CtL2e 115"
    ),
    Merit(
        name="Lethal Mien",
        min_value=2,
        max_value=2,
        description="You can deal lethal damage unarmed, or if you already have natural weapons, increase their weapon rating by +1.",
        merit_type="changeling",
        prerequisite="",
        book="CtL2e 117"
    ),
    Merit(
        name="Librarian",
        min_value=3,
        max_value=3,
        description="Your impression level is one higher at the first social interaction with librarians and scholars, you keep or lose the bonus depending on your behaviour on subsequent encounters. Gain two additional dice on rolls about researching written accounts.",
        merit_type="changeling",
        prerequisite="",
        book="DE2 75"
    ),
    Merit(
        name="Magic Dreams",
        min_value=5,
        max_value=5,
        description="May use Hedge Sorcery in dreams, substituting oneiromancy for Hedgespinning.",
        merit_type="changeling",
        prerequisite="hedge_sorcerer:1,occult:3",
        book="Hedge 69"
    ),
    Merit(
        name="Mantle",
        min_value=1,
        max_value=5,
        description="Your mien is attuned to a local Court. Apply Mantle as a Social bonus among friends of the Court. Gain a source of Glamour, Mantle benefits, and Contract access as per your Court.",
        merit_type="changeling",
        prerequisite="",
        book="CtL2e 117"
    ),
    Merit(
        name="Manymask",
        min_value=3,
        max_value=3,
        description="Once a session per dot of Wyrd, spend Glamour to change a feature of your Mask. With Wyrd 5, once per session, spend Glamour to change your Mask almost completely.",
        merit_type="changeling",
        prerequisite="wyrd:2,manipulation:3",
        book="CtL2e 118"
    ),
    Merit(
        name="Market Sense",
        min_value=1,
        max_value=1,
        description="Pay off a Goblin Debt for free once a session through shrewd bargaining.",
        merit_type="changeling",
        prerequisite="",
        book="CtL2e 119"
    ),
    Merit(
        name="Noblesse Oblige",
        min_value=1,
        max_value=3,
        description="Spend Willpower to confer particular bonuses to friends of your Court for a scene.",
        merit_type="changeling",
        prerequisite="mantle:1",
        book="CtL2e 119"
    ),
    Merit(
        name="Blood Liege",
        min_value=3,
        max_value=3,
        description="Swear yourself to a vampire, gain a two dot mentor. Once a lunar month, the vampire may give you a relatively task to be completed in good faith. May cancel this merit to cause a huntsman or true fae to divert their attention to the vampire.",
        merit_type="changeling",
        prerequisite="",
        book="DE2 107"
    ),
    Merit(
        name="Pandemoniacal",
        min_value=1,
        max_value=3,
        description="Apply as bonus dice to incite Bedlam.",
        merit_type="changeling",
        prerequisite="wyrd:6",
        book="CtL2e 119"
    ),
    Merit(
        name="Parallel Lives",
        min_value=3,
        max_value=3,
        description="Share a psychic link with your fetch. You take +2 to read each other's intentions or enter each other's Bastion, or spend Willpower to ride the other's senses or communicate visions telepathically.",
        merit_type="changeling",
        prerequisite="",
        book="CtL2e 119"
    ),
    Merit(
        name="Rigid Mask",
        min_value=3,
        max_value=3,
        description="Mundane humans and devices can't pierce your deceptions, while supernatural beings must force a Clash of Wills to do so. Dropping the Mask causes you lethal damage.",
        merit_type="changeling",
        prerequisite="subterfuge:2",
        book="CtL2e 119"
    ),
    Merit(
        name="Token",
        min_value=1,
        max_value=5,
        description="You have access to one or more Tokens of a total rating equal to dots in this Merit. Multiple characters may share this Merit.",
        merit_type="changeling",
        prerequisite="",
        book="CtL2e 119"
    ),
    Merit(
        name="Touchstone",
        min_value=1,
        max_value=5,
        description="You have an additional Clarity Touchstone for each dot of this Merit.",
        merit_type="changeling",
        prerequisite="",
        book="CtL2e 120"
    ),
    Merit(
        name="Warded Dreams",
        min_value=1,
        max_value=3,
        description="Apply as a bonus to your Bastion's Fortification",
        merit_type="changeling",
        prerequisite="resolve<=3",
        book="CtL2e 120"
    ),
    #Changeling-Specific Styles
    Merit(
        name="Elemental Warrior",
        min_value=1,
        max_value=5,
        description="These maneuvers wield a particular chosen element.",
        merit_type="changeling",
        prerequisite="[dexterity:3,wits:3],[brawl:2,firearms:2,weaponry:2],[elemental_weapon,primal_glory,elemental_seeming]",
        book="CtL2e 113"
    ),
    Merit(
        name="Enchanting Performance",
        min_value=1,
        max_value=3,
        description="Use your performances to enchanting effects.",
        merit_type="changeling",
        prerequisite="presence:3,expression:3",
        book="CtL2e 113"
    ),
    Merit(
        name="Hedge Duelist",
        min_value=1,
        max_value=3,
        description="Fighting maneuvers for combat in the Hedge.",
        merit_type="changeling",
        prerequisite="[presence:2,manipulation:2],[brawl:2,weaponry:2],social_skill:2"
    )
]

# Create dictionary for easy lookup
changeling_merits_dict = {merit.name.lower().replace(" ", "_").replace("(", "").replace(")", ""): merit for merit in changeling_merits}
