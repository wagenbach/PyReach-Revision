from world.cofd.stat_types import Merit

# Immortal-Specific Merits
immortal_merits = [
    Merit(
        name="Dead Celebrity",
        min_value=1,
        max_value=3,
        description="You possessed Fame in a previous era. Apply as a Social bonus to appeal to your resemblance to your famed self.",
        merit_type="immortal",
        prerequisite="",
        book="MtC2e 106"
    ),
    Merit(
        name="Endless Potency",
        min_value=1,
        max_value=5,
        description="Choose an Attribute. You may spend Sekhem, Pillars, or for your immortality's favored Attribute, Willpower to channel Endless Potency as bonus Attribute dots for one scene.",
        merit_type="immortal",
        prerequisite="",
        book="MtC2e 106"
    ),
    Merit(
        name="Enigma",
        min_value=1,
        max_value=5,
        description="Fate conspires to erase evidence of your life left behind. Investigation takes a -2 penalty and requires an additional clue for each dot of Enigma.",
        merit_type="immortal",
        prerequisite="fame:0",
        book="MtC2e 106"
    ),
    Merit(
        name="Fount of Vitality",
        min_value=4,
        max_value=4,
        description="Recover from wounds like the Arisen rather than like mortals.",
        merit_type="immortal",
        prerequisite="[sekhem:3,invested:1]",
        book="MtC2e 106"
    ),
    Merit(
        name="Relic Sensitivity",
        min_value=2,
        max_value=2,
        description="Sense vessels of Sekhem through kepher.",
        merit_type="immortal",
        prerequisite="",
        book="MtC2e 107"
    ),
    Merit(
        name="Resplendent Soul",
        min_value=3,
        max_value=3,
        description="Sense vessels of Sekhem through kepher.",
        merit_type="immortal",
        prerequisite="",
        book="MtC2e 107"
    ),
    Merit(
        name="Supernatural Resistance",
        min_value=1,
        max_value=5,
        description="Add this Merit's rating to your Supernatural Tolerance.",
        merit_type="immortal",
        prerequisite="",
        book="MtC2e 108"
    ),
    Merit(
        name="Tenacious Eternity",
        min_value=4,
        max_value=4,
        description="Your curse is more lenient than others of your kind.",
        merit_type="immortal",
        prerequisite="",
        book="MtC2e 108"
    ),
]

# Create dictionary for easy lookup
immortal_merits_dict = {merit.name.lower().replace(" ", "_").replace("(", "").replace(")", ""): merit for merit in immortal_merits}
