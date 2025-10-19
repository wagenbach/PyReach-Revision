from world.cofd.stat_types import Merit

beast_merits = [
# General Beast Merits
    Merit(
        name="Advanced Danger Sense",
        min_value=2,
        max_value=2,
        description="In the first turn of combat, Defense gains +2 and can be applied universally unless sacrificed. If someone attempts and fails to ambush you, set your initiative to one higher than the fastest ambusher.",
        merit_type="beast",
        prerequisite="danger_sense:1",
        book="BtP 113"
    ),
    Merit(
        name="Advanced Direction Sense",
        min_value=2,
        max_value=2,
        description="You can intuit the direction to anything you've directly sensed.",
        merit_type="beast",
        prerequisite="direction_sense:1",
        book="BtP 114"
    ),
    Merit(
        name="Epic Direction Sense",
        min_value=2,
        max_value=2,
        description="You can sense backwards across time, locating since-destroyed objects or spending Willpower to glimpse the past.",
        merit_type="beast",
        prerequisite="advanced_direction_sense:1",
        book="BtP 114"
    ),
    Merit(
        name="Direct Dial",
        min_value=1,
        max_value=1,
        description="Spend 1 Willpower (or none, if you try to speak to a broodmate) to begin a phonecall with a target you could have tracked with Advanced Direction Sense, through the nearest phone or computer.",
        merit_type="beast",
        prerequisite="advanced_direction_sense:1,computer:2,occult:2",
        book="BPG 99"
    ),
    Merit(
        name="Advanced Double Jointed",
        min_value=1,
        max_value=1,
        description=" 	You can fit your entire body through anything that can accommodate your head. Apply Double Jointed's grappling penalty even when you act aggressively.",
        merit_type="beast",
        prerequisite="double_jointed:1",
        book="BtP 114"
    ),
    Merit(
        name="Advanced Eidetic Memory",
        min_value=1,
        max_value=1,
        description="Rolled recollection achieves exceptional success on a threshold of three instead of five. You can perform retroactive Mental or Social analyses.",
        merit_type="beast",
        prerequisite="eidetic_memory:1",
        book="BtP 114"
    ),
    Merit(
        name="Epic Potential",
        min_value=1,
        max_value=1,
        description="Choose one Attribute and raise its trait maximum by one dot. You may not purchase this Merit multiple times for different Attributes.",
        merit_type="beast",
        prerequisite="",
        book="BtP 114"
    ),
    Merit(
        name="Advanced Fame",
        min_value=1,
        max_value=3,
        description="Your Horror has archetypal resonance. Apply your Advanced Fame dots like regular Fame dots, but to all of humanity (including stalking Heroes). Choose a reputation and a corresponding Condition. By acting out your reputation, you can inflict the Condition on human witnesses a number of times per session equal to dots in this Merit.",
        merit_type="beast",
        prerequisite="fame:1",
        book="BtP 115"
    ),
    Merit(
        name="Advanced Fast Reflexes",
        min_value=1,
        max_value=1,
        description="Roll Initiative twice and keep your choice of result",
        merit_type="beast",
        prerequisite="fast_reflexes:3",
        book="BtP 115"
    ),
    Merit(
        name="Fist of Nightmares",
        min_value=2,
        max_value=2,
        description=" 	Spend Willpower and roll a Nightmare to hold it in store up to a scene. Release it by touch, subtracting a success from your roll for every two dots in the victim's relevant Resistance trait.",
        merit_type="beast",
        prerequisite="brawl:2,occult:2",
        book="BtP 115"
    ),
    Merit(
        name="Advanced Giant",
        min_value=2,
        max_value=2,
        description="You gain density proportionally with your Satiety. Deal it in Structure damage to objects that crash into you, and as a penalty to lift you or knock you down.",
        merit_type="beast",
        prerequisite="giant:1",
        book="BtP 116"
    ),
    Merit(
        name="Guilty Pleasure",
        min_value=1,
        max_value=1,
        description="Choose an embarrassing indulgence that can apply when feeding your Hunger. Doing so yields another point of Satiety, a point of Willpower, and the Guilty Condition.",
        merit_type="beast",
        prerequisite="",
        book="BtP 116"
    ),
    Merit(
        name="Hunger Management",
        min_value=1,
        max_value=3,
        description="For each dot in this Merit, you can choose to add or subtract a die when rolling to gain Satiety.",
        merit_type="beast",
        prerequisite="resolve:3",
        book="BtP 116"
    ),
    Merit(
        name="Advanced Iron Skin",
        min_value=1,
        max_value=2,
        description="Add general Armor equal to your dots in this Merit against bashing and lethal attacks. With two dots, when you take aggravated damage from a source other than Anathema, spend Willpower to downgrade one point to lethal.",
        merit_type="beast",
        prerequisite="iron_skin:1,stamina:4",
        book="BtP 117"
    ),
    Merit(
        name="Epic Iron Skin",
        min_value=2,
        max_value=2,
        description="Whenever you take damage from any source other than Anathema, ignore one point.",
        merit_type="beast",
        prerequisite="advanced_iron_skin,stamina:5",
        book="BtP 117"
    ),
    Merit(
        name="Advanced Killer Instinct",
        min_value=1,
        max_value=3,
        description="You can apply your basic Killer Instinct against any target with no preparation. If you do prepare your Killer Instinct normally, when you attack the target, you may spend each dot in this Merit to either convert a point of lethal damage to aggravated, temporarily ruin 1/1 nonmagical Armor, or ignore two points of Defense and one die of called shot penalties.",
        merit_type="beast",
        prerequisite="killer_instinct:3",
        book="BtP 117"
    ),
    Merit(
        name="Spoor",
        min_value=1,
        max_value=5,
        description="Each dot of this Merit can be spent once per story, when a Hero pursues you, to either negate a turn of direct pursuit, reduce the Hero's maximum rolls on an extended investigation, or penalize Heroic Tracking by a die.",
        merit_type="beast",
        prerequisite="fame:0",
        book="BtP 120"
    ),
    Merit(
        name="Advanced Striking Looks",
        min_value=2,
        max_value=2,
        description="Add the Rote quality whenever you benefit from Striking Looks.",
        merit_type="beast",
        prerequisite="striking_looks:2",
        book="BtP 121"
    ),
    Merit(
        name="Horrorspawn",
        min_value=1,
        max_value=5,
        description=" 	Your character has created a permanent Horrorspawn. The Horrorspawn can feed for her, fight for her, and carry out basic tasks.This Merit can be purchased multiple times to reflect multiple Horrorspawn.",
        merit_type="beast",
        prerequisite="",
        book="BPG 99"
    ),
    Merit(
        name="Infernal Machine",
        min_value=2,
        max_value=2,
        description="Your character has a vehicle that she has customized for pursuit. Add two to the vehicle’s Durability, five to its Structure, 10 to its Acceleration and Safe Speed, 20 to its Maximum Speed, and one to its Handling. Only the Durability and Structure bonuses apply if someone other than she is driving her vehicle.",
        merit_type="beast",
        prerequisite="",
        book="BPG"
    ),
    Merit(
        name="Legendary Horror",
        min_value=1,
        max_value=5,
        description="Your Horror gains an Essence pool of 10, which increases by five for each additional dot purchased and. Your Horror also gains one dot of Influence and two Numina for each dot you have in this Merit.",
        merit_type="beast",
        prerequisite="lair<=3",
        book="BPG 99"
    ),
    Merit(
        name="Obcasus Initiate",
        min_value=2,
        max_value=2,
        description="You gain the capacity to lead an Obcasus rite. You immediately learn the Consecrate rite. You may learn a maximum number of rites equal to your Intelligence+Lair.",
        merit_type="beast",
        prerequisite="guidance:1",
        book="BPG 100"
    ),
    #Cult Merits
    Merit(
        name="Primordial Cult",
        min_value=2,
        max_value=5,
        description="You have gathered followers into a cult. You can only have one cult at a time. Dots in this Merit in excess of two are used to purchase additional benefits.",
        merit_type="beast",
        prerequisite="[occult:2,politics:2]",
        book="BPG 100"
    ),
    Merit(
        name="Deceptive",
        min_value=1,
        max_value=1,
        description="Once per chapter you can use your followers to run interference on enemies and spies, inflicting the Distracted Condition on anyone investigating the aftermath of your feeding. If you have the Anonymity Merit, your followers benefit from it as well.",
        merit_type="beast",
        prerequisite="primordial_cult:2",
        book="BPG 100"
    ),
    Merit(
        name="Doctrinal",
        min_value=3,
        max_value=3,
        description=" 	The cult gains a +2 modifier on breaking points in-curred from actions they take to feed you. In addition, once per session you or your followers can remove two Doors in Social maneuvers meant to proselytize or recruit allies.",
        merit_type="beast",
        prerequisite="primordial_cult:2",
        book="BPG 100"
    ),
    Merit(
        name="Edible",
        min_value=1,
        max_value=3,
        description="You can feed by reaping your followers with Nightmares, making a Satiety roll with base potential equal to dots in Edible.",
        merit_type="beast",
        prerequisite="primordial_cult:2",
        book="BPG 100"
    ),
    Merit(
        name="Influential",
        min_value=1,
        max_value=1,
        description="Choose a narrow sphere of influence (bookies, librarians, street kids, etc.). Once per chapter, subtract two from the Availability rating of any service or equipment that would fall under that purview, to a minimum of one. This influence also counts as a dot of Contacts. You can purchase this benefit five times.",
        merit_type="beast",
        prerequisite="primordial_cult:2",
        book="BPG 100"
    ),
    Merit(
        name="Mystic",
        min_value=2,
        max_value=3,
        description="Choose a type (clairvoyants, mediums, tele-paths, etc.); you can access their abilities through the Elect benefit. For two dots, their wisdom grants you the 9-again quality on Occult rolls, or 8-again if you already have that benefit. For three dots, once per chapter you can also use them as a 3-die “equipment bonus” on any roll that would reasonably relate to their wheelhouse, achieving an exceptional success on three successes.",
        merit_type="beast",
        prerequisite="primordial_cult:2",
        book="BPG 100"
    ),
    Merit(
        name="Resonant",
        min_value=3,
        max_value=3,
        description="Once per chapter, if your cult performs a short ritual they can increase an area’s similarity to one of your Chambers by two steps for a scene (see Beast: The Primordial, p. 101). Forgo the Willpower cost to impose a Lair Trait or open a Primordial Pathway.",
        merit_type="beast",
        prerequisite="primordial_cult:2",
        book="BPG 100"
    ),
    #Lair Merits
    Merit(
        name="Connected Lair",
        min_value=2,
        max_value=2,
        description="The lair has access to the information systems of the mundane world ( Internet, radio, TV ).",
        merit_type="beast",
        prerequisite="",
        book="BPG 100"
    ),
    Merit(
        name="Trap Room",
        min_value=2,
        max_value=2,
        description="When opening a Primordial Pathway you may choose to spend a point of Satiety. If she does the duration of the pathway is extended. Characters may enter the area normally but if they attempt to leave they end up in the Beast’s Lair.",
        merit_type="beast",
        prerequisite="",
        book="BPG 101"
    ),
    Merit(
        name="Vast Lair",
        min_value=1,
        max_value=3,
        description="The Chambers of the Lair are larger than normal and require at least 10 minutes per dot in this Merit to traverse.",
        merit_type="beast",
        prerequisite="",
        book="BPG 101"
    ),
    Merit(
        name="Well-Stocked Lair",
        min_value=1,
        max_value=5,
        description="Each dot allows to select two dots worth of Merits that represent the material goods and inhabitants available in the Lair.",
        merit_type="beast",
        prerequisite="",
        book="BPG 101"
    ),
    #Kinship Merits (These All Require Family Ties)
    Merit(
        name="Know Their Falseness",
        min_value=2,
        max_value=2,
        description="Bind promises or agreements by spending 1 Willpower. If the target breaks the promise, you gain a vision of the breach and a +2 bonus to the next three rolls made to retaliate; the target's Defense is halved for your first attack. This Merit has no effect on demons of the Unchained.",
        merit_type="beast",
        prerequisite="family_ties_with_changeling",
        book="BPG 102"
    ),
    Merit(
        name="Feign Death",
        min_value=1,
        max_value=1,
        description="Spend 1 Willpower to appear dead for hours equal to your Lair rating. During this time, you exhibit no signs of life and can suspend the effects of diseases or poisons.",
        merit_type="beast",
        prerequisite="family_ties_with_vampire",
        book="BPG 102"
    ),
    Merit(
        name="Look Between Worlds",
        min_value=2,
        max_value=2,
        description="See and hear ghosts, spirits, and other ephemeral beings, even if they are not Manifested. Possession cases become immediately obvious. Beings in Twilight may notice your scrutiny.",
        merit_type="beast",
        prerequisite="family_ties_with_ghost",
        book="BPG 102"
    ),
    Merit(
        name="Sanguivore",
        min_value=2,
        max_value=2,
        description="Develop retractable fangs capable of inflicting 0L damage and draining blood. Consuming a pint of blood satisfies your need for food and water for a day.",
        merit_type="beast",
        prerequisite="family_ties_with_vampire",
        book="BPG 102"
    ),
    Merit(
        name="Scent Your Prey",
        min_value=1,
        max_value=2,
        description="Gain enhanced olfactory or auditory senses (•) or both (••). Enhanced hearing allows detection of high frequencies and eliminates penalties for quiet or distant sounds. Enhanced smell enables tracking and identification by scent.",
        merit_type="beast",
        prerequisite="family_ties_with_werewolf",
        book="BPG 102"
    ),
    Merit(
        name="Scour Your Body",
        min_value=2,
        max_value=2,
        description="As a reflexive action, reduce one Physical Attribute by 1 and take 1 Lethal damage to activate an Atavism or Nightmare as if you spent 1 Satiety. The Attribute loss lasts 24 hours.",
        merit_type="beast",
        prerequisite="family_ties_with_mage",
        book="BPG 103"
    ),
    Merit(
        name="Step Sideways",
        min_value=3,
        max_value=3,
        description="Gain +1 to rolls to open a Primordial Pathway while staring into a reflective surface. You can choose to transport yourself instantly into your Lair.",
        merit_type="beast",
        prerequisite="family_ties_with_werewolf",
        book="BPG 103"
    ),
    Merit(
        name="Walk Lightly",
        min_value=2,
        max_value=2,
        description="Leave no forensic evidence behind. Attempts to collect DNA, fingerprints, or other traces automatically fail. Mundane tracking methods, like dogs, cannot follow your scent.",
        merit_type="beast",
        prerequisite="family_ties_with_ghost",
        book="BPG 103"
    ),
]

# Create dictionary for easy lookup
beast_merits_dict = {merit.name.lower().replace(" ", "_").replace("(", "").replace(")", ""): merit for merit in beast_merits}
