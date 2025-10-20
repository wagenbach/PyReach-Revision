from world.cofd.stat_types import Merit

# Skinchanger-Specific Merits
skinchanger_merits = [
    Merit(
        name="Skinthief",
        min_value=3,
        max_value=3,
        description="You know how to skin a particular type of prey in an occult manner, enchanting it so that you can wear it and become the prey. This costs an amount of Willpower proportional to the longevity of the skin.",
        merit_type="skinchanger",
        prerequisite="animal_ken:1,occult:2",
        book="DE 248-249"
    ),
    Merit(
        name="Animal Speech",
        min_value=1,
        max_value=2,
        description="You can understand the communication of your prey animal, and can communicate in kind in that form. With two dots, your prey animal can understand your communication even in human form.",
        merit_type="skinchanger",
        prerequisite="skinthief:3",
        book="DE 248"
    ),
    Merit(
        name="Bare Necessities",
        min_value=2,
        max_value=3,
        description="You can understand the communication of your prey animal, and can communicate in kind in that form. With two dots, your prey animal can understand your communication even in human form.",
        merit_type="skinchanger",
        prerequisite="skinthief:3",
        book="DE 248"
    ),
    Merit(
        name="Essence Pool",
        min_value=1,
        max_value=5,
        description="You have a pool of Essence the size of your dots in this Merit, from which you can spend only one point a turn. You can restore Essence by feeding on resonance in skinned form, or meditating and spending three Willpower.",
        merit_type="skinchanger",
        prerequisite="skinthief:3,spirit_skin",
        book="DE 248"
    ),
    Merit(
        name="Hybrid Form",
        min_value=2,
        max_value=4,
        description="Substitute for your skinned form for two dots, or supplement it with for four dots, a fierce human-hybrid form. The Hybrid Form has a Strength and a Size equal to the greater Strength or Size of the two forms, plus one.",
        merit_type="skinchanger",
        prerequisite="skinthief:3",
        book="DE 248"
    ),
    Merit(
        name="Renewable Skins",
        min_value=1,
        max_value=1,
        description="You can renew an old skin with the same ritual time and Willpower cost, without having to hunt a new skin.",
        merit_type="skinchanger",
        prerequisite="skinthief:3",
        book="DE 248"
    ),
    Merit(
        name="Resilient Form",
        min_value=1,
        max_value=5,
        description="If your skinned form has less Health than your human form, add a dot of Health per dot in this Merit to make up the difference.",
        merit_type="skinchanger",
        prerequisite="skinthief:3",
        book="DE 248"
    ),
    Merit(
        name="Spirit Powers",
        min_value=1,
        max_value=1,
        description="You can use a dot of your prey's Influence and one of its Numina or Manifestations. You may take this Merit multiple times for multiple Influence dots and Numina or Manifestations.",
        merit_type="skinchanger",
        prerequisite="skinthief:3,spirit_skin",
        book="DE 249"
    ),
    Merit(
        name="Strong Instincts",
        min_value=1,
        max_value=1,
        description="Calculate Defense in skinned form with the higher, not lower, of your Dexterity and Wits.",
        merit_type="skinchanger",
        prerequisite="skinthief:3",
        book="DE 249"
    ),
    Merit(
        name="Quick Change",
        min_value=1,
        max_value=1,
        description="You can don and doff your skin reflexively.",
        merit_type="skinchanger",
        prerequisite="skinthief:3",
        book="DE 249"
    ),
    Merit(
        name="Twisted Tongue",
        min_value=1,
        max_value=1,
        description="You can speak human tongues in skinned form.",
        merit_type="skinchanger",
        prerequisite="skinthief:3,animal_skin",
        book="DE 249"
    ),
    Merit(
        name="Unshared Flesh",
        min_value=3,
        max_value=3,
        description="Track injuries separately for your human and skinned form. An injured form doesn't heal while you're in the other form.",
        merit_type="skinchanger",
        prerequisite="skinthief:3",
        book="DE 249"
    ),
]

# Create dictionary for easy lookup
skinchanger_merits_dict = {merit.name.lower().replace(" ", "_").replace("(", "").replace(")", ""): merit for merit in skinchanger_merits}
