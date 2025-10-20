from world.cofd.stat_types import Merit

# Lost Boys-Specific Merits
lostboys_merits = [
    Merit(
        name="The Protocol",
        min_value=1,
        max_value=5,
        description="Style. An augmentation system unique to the Lost Boys.",
        merit_type="lostboys",
        prerequisite="",
        book="HL 96"
    ),
    Merit(
        name="Jumper",
        min_value=1,
        max_value=3,
        description="Style. Augmentations that power enhanced jumping ability.",
        merit_type="lostboys",
        prerequisite="protocol>=jumper",
        book="HL 99"
    ),
    Merit(
        name="Protocol Fixer",
        min_value=1,
        max_value=5,
        description="Style. You have been assigned a Delta Protocol handler who administers Serum regularly.",
        merit_type="lostboys",
        prerequisite="protocol:1",
        book="HL 97"
    ),
    Merit(
        name="Archangel System",
        min_value=5,
        max_value=5,
        description="Spend Willpower to activate a faintly luminous neuromuscular lattice for a scene.",
        merit_type="lostboys",
        prerequisite="protocol:5",
        book="HL 97"
    ),
    Merit(
        name="Augmented Resilience",
        min_value=1,
        max_value=3,
        description="Increase your effective Stamina by dots in this Merit. While Deprived, gain 2/1 Armor.",
        merit_type="lostboys",
        prerequisite="protocol>=augmented_resilience",
        book="HL 98"
    ),
    Merit(
        name="Augmented Speed",
        min_value=1,
        max_value=5,
        description="Apply this Merit as a bonus to Initiative and Speed. While Deprived, double the Speed bonus.",
        merit_type="lostboys",
        prerequisite="protocol>=augmented_speed",
        book="HL 98"
    ),
    Merit(
        name="Cloaking Device",
        min_value=3,
        max_value=3,
        description="While holding your breath, your body refracts light, hiding you from cameras, motion sensors, and thermal detectors. Penalize attempts to spot you by -5. While Deprived, you also may suffer lethal damage to activate the Cloaking Device for three turns once per scene.",
        merit_type="lostboys",
        prerequisite="protocol:3",
        book="HL 99"
    ),
    Merit(
        name="Holdout Storage",
        min_value=1,
        max_value=3,
        description="A cavity in your body can store items up to your Merit rating in Size, which you may withdraw as an instant action. While Deprived, suffer lethal damage to withdraw reflexively.",
        merit_type="lostboys",
        prerequisite="protocol>=holdout_storage",
        book="HL 99"
    ),
    Merit(
        name="Implanted Interface",
        min_value=2,
        max_value=2,
        description="Your nervous system has an integrated computer with wireless access, providing a +3 equipment bonus. Suffer lethal damage to overclock to a +5 bonus for the scene.",
        merit_type="lostboys",
        prerequisite="protocol:2",
        book="HL 99"
    ),
    Merit(
        name="Last-Chance",
        min_value=5,
        max_value=5,
        description="Roll Resolve + Composure as an instant action to deploy a traumatic internal weapon, which in turn rolls Stamina + Firearms + 5 as a 3L firearms attack against everyone for 10 meters. Suffer five aggravated damage and roll five dice for additional lethal damage. While Deprived, the attack has a 4L rating and 3 Armor Piercing.",
        merit_type="lostboys",
        prerequisite="protocol:5",
        book="HL 99"
    ),
    Merit(
        name="Pulse Generator",
        min_value=1,
        max_value=5,
        description="Once per scene, your touch can reflexively inflict Stunned and your Merit rating in bashing damage, or against electronics, twice your Merit rating in Structure damage, ignoring Durability. While Deprived, suffer lethal damage to recharge the Generator.",
        merit_type="lostboys",
        prerequisite="protocol>=pulse_generator",
        book="HL 99"
    ),
    Merit(
        name="Strength Augmentation",
        min_value=1,
        max_value=3,
        description="Increase your effective Strength by dots in this Merit. While Deprived, suffer lethal damage to also gain +1 Strength for the scene.",
        merit_type="lostboys",
        prerequisite="protocol>=strength_augmentation",
        book="HL 100"
    ),
    Merit(
        name="Sub-Dermal Armor",
        min_value=2,
        max_value=4,
        description="Stack +1/+1 Armor, or with ••••, +2/+2 Armor. While Deprived, stack an additional +1/+1 Armor.",
        merit_type="lostboys",
        prerequisite="protocol>=sub-dermal_armor",
        book="HL 100"
    ),
    Merit(
        name="Uncanny Perception",
        min_value=1,
        max_value=3,
        description="Apply this Merit as a bonus to Perception and aimed attacks. While Deprived, double the bonus, but suffer lethal damage and sensory blowout from extreme stimuli.",
        merit_type="lostboys",
        prerequisite="protocol>=uncanny_perception",
        book="HL 100"
    ),
    Merit(
        name="Voice Box",
        min_value=1,
        max_value=1,
        description="Perfectly mimic voices you've studied in person. While Deprived, mimic voices you've heard recorded or in passing.",
        merit_type="lostboys",
        prerequisite="protocol:1",
        book="HL 100"
    ),
]

# Create dictionary for easy lookup
lostboys_merits_dict = {merit.name.lower().replace(" ", "_").replace("(", "").replace(")", ""): merit for merit in lostboys_merits}
