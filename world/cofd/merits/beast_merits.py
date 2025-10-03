from world.cofd.stat_types import Merit

# Beast-Specific Merits
beast_merits = [
    Merit(
        name="Epic Potential",
        min_value=1,
        max_value=1,
        description="A Beast with this Merit has a defining Attribute that excels beyond normal human limitations. When taking this Merit, choose an Attribute. You may raise that Attribute 1 dot higher than the normal trait maximum. You still have to buy the Attribute with Experiences, but it's not subject to the normal limitation. You may only take this Merit once.",
        merit_type="general",
        prerequisite="beast"
    ),
    Merit(
        name="Advanced Fame",
        min_value=1,
        max_value=3,
        description="Your character not only has Fame in her current identity, but her Horror has a legendary notoriety that shakes humanity on a deep, fundamental level. This acts as additional Fame dots when dealing with humanity. When acting in accordance with the reputation, your character can create that Condition in humans interacting with her once per chapter, per dot. Drawback: Heroes find your character particularly easy to find.",
        merit_type="social",
        prerequisite="beast,fame:1"
    ),
    Merit(
        name="Advanced Fast Reflexes",
        min_value=1,
        max_value=1,
        description="Your character reacts at preternatural rates. When rolling for initiative, roll twice. Each roll benefits from the normal +3 for Fast Reflexes. Take the higher of the two results.",
        merit_type="physical",
        prerequisite="beast,fast_reflexes:3"
    ),
    Merit(
        name="Fast-Talking",
        min_value=1,
        max_value=5,
        description="Your character talks circles around listeners. She speaks a mile a minute and often leaves her targets reeling, but nodding in agreement. Always Be Closing (•): When a mark contests or resists your character's Social interactions, apply a –1 to their Resolve or Composure. Jargon (••): You may apply one relevant Specialty to any Social roll you make, even if the Specialty isn't tied to the Skill in use. Devil's Advocacy (•••): You can reroll one failed Subterfuge roll per scene. Salting (••••): When your character opens a Door using conversation, you may spend a Willpower point to immediately open another Door. Patron's Privilege (•••••): If a target regains Willpower from his Vice while your character is present, you may immediately roll Manipulation + Subterfuge to open a Door.",
        merit_type="style",
        prerequisite="manipulation:3,subterfuge:2"
    ),
    Merit(
        name="Fist of Nightmares",
        min_value=2,
        max_value=2,
        description="Your character may 'store' the effects of a Nightmare and release it upon touching a victim. Your character may store the effects of one Nightmare by spending a Willpower point. Make the relevant roll at that point. The first time your character touches another in that same scene, the Nightmare triggers on him. Subtract one success from the Nightmare for every two full dots of the relevant Resistance trait that the target possesses.",
        merit_type="supernatural",
        prerequisite="brawl:2,occult:2"
    ),
    Merit(
        name="Advanced Giant",
        min_value=2,
        max_value=2,
        description="Your character is dense beyond reason. She remains Size 6, but she gains significant mass as she becomes sated. Her Satiety applies as a penalty to any attempts to knock her over or lift her. In addition, any object smashing into her at fast speed suffers her Satiety in automatic Structure damage. Drawback: Your character's mass is clearly inhuman. Weak floors break beneath her feet.",
        merit_type="physical",
        prerequisite="beast,giant:3"
    ),
    Merit(
        name="Guilty Pleasure",
        min_value=1,
        max_value=1,
        description="Your character has one choice food, vice, or indulgence she utterly adores to the exclusion of other tastes. When taking this Merit, choose that indulgence. Any time she indulges in this guilty pleasure as part of replenishing Satiety, she gains 1 additional Satiety, a point of Willpower, and the Guilty Condition.",
        merit_type="general",
        prerequisite="beast"
    ),
    Merit(
        name="Heavy Weapons",
        min_value=1,
        max_value=5,
        description="Your character is trained with heavy weapons that require strength, wide range, and follow-through. Sure Strike (•): You can reflexively remove three dice from any attack dice pool to add one to your character's weapon damage rating for the turn. Threat Range (••): If you opt not to move or Dodge during your turn, any character moving into your character's proximity suffers 1L damage and a penalty to their Defense equal to your character's weapon damage rating. Bring the Pain (•••): Sacrifice your character's Defense to use Bring the Pain. Any damage you score counts as a penalty to all actions the victim takes during their next turn. Warding Stance (••••): Spend a point of Willpower reflexively to add her weapon's damage rating as armor for the turn. Rending (•••••): By spending a Willpower point before making an attack roll, her successful attacks cause one point of aggravated damage in addition to her weapon's damage rating.",
        merit_type="style",
        prerequisite="stamina:3,strength:3,athletics:2,weaponry:2"
    ),
    Merit(
        name="Hunger Management",
        min_value=1,
        max_value=3,
        description="Your character can manage and maintain her hunger and Satiety more carefully than other Beasts. For every dot in this Merit, you can add or subtract one die from the Satiety potential dice pool you roll when her Horror consumes something. This can ensure she gains more Satiety when starving, or she's less likely to send her Horror into hibernation when nearly sated.",
        merit_type="supernatural",
        prerequisite="beast,resolve:3"
    ),
    Merit(
        name="Advanced Iron Skin",
        min_value=1,
        max_value=2,
        description="Your character's flesh is like fine leather. This Merit grants armor equal to its dot rating. However, the armor granted works against lethal damage as well as bashing damage. With the two-dot version, you may reflexively spend a point of Willpower upon taking aggravated damage to downgrade a point of aggravated damage to lethal damage. These advantages do not apply to Anathemas.",
        merit_type="physical",
        prerequisite="beast,stamina:4"
    ),
    Merit(
        name="Iron Skin (Epic)",
        min_value=2,
        max_value=2,
        description="Your character is nigh invincible. Ignore the first point of damage taken from any source except an Anathema.",
        merit_type="physical",
        prerequisite="beast,stamina:5"
    ),
    Merit(
        name="Killer Instinct",
        min_value=1,
        max_value=3,
        description="Your character's experience with the darkness inherent in this world has left her cold and calculating, so she can see the fragile threads that hold life together. Activating this Merit requires an instant action to assess a creature. When making an attack against that target, you may divide the dots in this Merit among any of the three following effects: • Ignore 1/1 armor on the target. • Convert 1 bashing damage caused in that attack to lethal. • Ignore one point of the target's Defense.",
        merit_type="physical",
        prerequisite="composure:3,medicine:1,wits:3"
    ),
    Merit(
        name="Killer Instinct (Advanced)",
        min_value=1,
        max_value=3,
        description="Your character's killer instincts draw from the primal entropy inherent in the universe. Your character is a devourer — a true destroyer. You do not have to take a turn to activate the mundane Killer Instinct Merit; it's considered always on. However, you may take a full turn to assess a target. When making an Athletics, Brawl, Firearms, or Weaponry attack against that target, divide your Advanced Killer Instinct dots among the following effects: • Convert 1 lethal damage caused in that attack to aggravated. • Destroy 1/1 armor on the target. • Ignore two points of the target's Defense and a single die penalty for making a called shot.",
        merit_type="physical",
        prerequisite="beast,killer_instinct:3"
    ),
    Merit(
        name="Library (Advanced)",
        min_value=1,
        max_value=5,
        description="Your character not only possesses a massive, credible library, but she also hoards thorough information about highly secretive supernatural topics. For each dot in this Merit, choose a topic. This could be 'vampires,' 'mages,' or any other supernatural force in the World of Darkness. When your character consults her library on one of those topics, take the Informed Condition relating to the topic. You can do this once per story, per topic. Advanced Library has a special prerequisite; your character requires a Safe Place equal to its dot rating, or for one Chamber in the Beast's Lair to be dedicated to the library.",
        merit_type="mental",
        prerequisite="library:3,safe_place:1"
    ),
    Merit(
        name="Relentless Assault",
        min_value=1,
        max_value=5,
        description="Your character fights with complete abandon. She throws herself at her opponents without thought or hesitation, turning herself into a ruthless killing machine. Drop of a Hat (•): In the first turn of a fight, your character adds 3 to her Initiative score, so long as she intends to make an all-out attack. Eye of the Tiger (••): When making an all-out attack against a chosen target, your character retains her Defense against him. She still loses it against other characters. Dig Deep (•••): You can choose to remove one die from your dice pool before rolling an attack. If you do, add a point of weapon damage to your character's attack. Grin and Bear It (••••): Any time she takes an all-out attack, she gains 1/1 armor against all attacks for the turn. The Warpath (•••••): Any time she fills a character's last health box with lethal or aggravated damage, she may immediately make an additional attack against one other character within her reach. Doing so costs a point of Willpower.",
        merit_type="style",
        prerequisite="strength:3,stamina:3,brawl:2"
    ),
    Merit(
        name="Spoor",
        min_value=1,
        max_value=5,
        description="Your Beast has developed a habit for dropping false clues as to her whereabouts. When she's pursued by a Hero, Spoor kicks in to keep the Hero off the trail. False evidence appears in her wake. Every dot in Spoor offers one of the following advantages per story: • If in direct pursuit, a dot of Spoor negates one turn of the Hero's pursuit rolls. • If the Hero investigates her as part of an extended action, a dot of Spoor removes one potential roll from the action. • When a Hero uses Heroic Tracking, a dot of Spoor acts as a –1 modifier to the roll. Multiple points can be spent at one time.",
        merit_type="supernatural",
        prerequisite="no_fame"
    ),
    Merit(
        name="Striking Looks (Advanced)",
        min_value=2,
        max_value=2,
        description="Your character's appearance is a composite of iconic imagery throughout the ages. If your character is beautiful, he's the example of beauty throughout the minds of millions. If she's frightening, she's utterly terrifying on a primordial level. When her chosen looks apply, gain the rote quality to the action in addition to the normal +2 for Striking Looks.",
        merit_type="social",
        prerequisite="beast,striking_looks:2"
    ),
    # Location-based Merits
    Merit(
        name="Lair",
        min_value=1,
        max_value=10,
        description="Your character has a physical place that acts as a doorway and anchor to her primordial lair in the Primordial Dream. This Merit functions as Safe Place for the physical structure, but the Beast can travel into the Chambers and Burrows beyond. Special features beyond this are Lair Traits.",
        merit_type="supernatural",
        prerequisite="beast"
    ),
    Merit(
        name="Camouflaged Lair",
        min_value=1,
        max_value=5,
        description="One or more Chambers within the character's Lair has a subtle entranceway. Characters hunting the Beast suffer a penalty equal to the character's dots in this Merit to find them. If such a character is aware of the Lair's location, this penalty applies to his rolls to find the Chamber.",
        merit_type="supernatural",
        prerequisite="lair:1"
    ),
    Merit(
        name="Comfortable Lair",
        min_value=1,
        max_value=1,
        description="One Chamber of the character's Lair is comfortable. It is well-lit and has amenities for living, even if those amenities don't always make sense (food from indeterminate sources, lights with no electrical sockets). A Chamber may be both Comfortable and Secure. This does not cost additional dots in the Lair Merit. Rather, this is a special trait that you choose for the Chamber.",
        merit_type="supernatural",
        prerequisite="lair:1"
    ),
    Merit(
        name="Hidden Lair",
        min_value=1,
        max_value=5,
        description="The Beast's Lair is particularly difficult to find. Maybe the door is hidden behind a secret panel or a Burrow only shows up in the deepest, darkest corridors in the Primordial Dream. Characters hunting the Beast suffer a penalty equal to the character's dots in this Merit to find it.",
        merit_type="supernatural",
        prerequisite="lair:1"
    ),
    Merit(
        name="Massive Lair",
        min_value=1,
        max_value=5,
        description="The character's Lair is incredibly large and intricate. Each dot in this Merit allows her to construct an additional Chamber or Burrow on top of the Chamber and Burrow granted by the Lair itself.",
        merit_type="supernatural",
        prerequisite="lair:1"
    ),
    Merit(
        name="Secure Lair",
        min_value=1,
        max_value=1,
        description="One Chamber of the character's Lair is secure. It is locked. Characters attempting to break in without the key suffer a penalty equal to the rating of the Safe Place component of the Lair Merit. A Chamber may be both Comfortable and Secure. This does not cost additional dots in the Lair Merit. Rather, this is a special trait that you choose for the Chamber.",
        merit_type="supernatural",
        prerequisite="lair:1"
    ),
    Merit(
        name="Vast Lair",
        min_value=1,
        max_value=3,
        description="Uninvited guests require at least 10 minutes per dot in this Merit to traverse a Chamber or Burrow. Further, each dot in this Merit adds five required successes and five minutes to the time increment of any extended action to collapse a Chamber.",
        merit_type="supernatural",
        prerequisite="lair:1"
    ),
    Merit(
        name="Well-Stocked Lair",
        min_value=1,
        max_value=5,
        description="Each dot in this Merit allows the character to select two dots worth of Merits that represent the material goods and inhabitants available in her Lair. Material goods removed from the Lair deteriorate into dust, insects, water, or some other useless substance within a few days. Alternately, one dot of this Merit can be used to make one or more Chambers of a character's Lair comfortable and livable.",
        merit_type="supernatural",
        prerequisite="lair:1"
    ),
]

# Create dictionary for easy lookup
beast_merits_dict = {merit.name.lower().replace(" ", "_").replace("(", "").replace(")", ""): merit for merit in beast_merits}
