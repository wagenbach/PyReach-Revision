from world.cofd.stat_types import Merit

# Dreamer-Specific Merits
dreamer_merits = [
    Merit(
        name="Subliminal Conditioning",
        min_value=1,
        max_value=5,
        description="Style. Your character has been subliminally conditioned to function as a human weapon.",
        merit_type="dreamer",
        prerequisite="",
        book="HL 83"
    ),
    Merit(
        name="Field Handler",
        min_value=1,
        max_value=5,
        description="Style. Your patrons feel your mission is so important, they've assigned a handler to your case.",
        merit_type="dreamer",
        prerequisite="subliminal_conditioning:1",
        book="HL 85"
    ),
    Merit(
        name="Deja Vu",
        min_value=1,
        max_value=3,
        description="Recover Memory when you experience a Physical Condition or Tilt. With two dots, recover Memory from dramatic failure. With three dots, recover Memory from lethal damage.",
        merit_type="dreamer",
        prerequisite="subliminal_conditioning:1",
        book="HL 85"
    ),
    Merit(
        name="Memory Palace",
        min_value=1,
        max_value=5,
        description="Increase your maximum Memory storage by your Memory Palace rating.",
        merit_type="dreamer",
        prerequisite="subliminal_conditioning:1",
        book="HL 84"
    ),
    Merit(
        name="Mephistopheles",
        min_value=2,
        max_value=2,
        description="Advancing your conditioned mission fulfills your Vice and confers a point of Memory for the scene.",
        merit_type="dreamer",
        prerequisite="subliminal_conditioning:1",
        book="HL 85"
    ),
    Merit(
        name="Not A Bug But A Feature",
        min_value=2,
        max_value=3,
        description="Spend Memory to extrude a strange organic variation on a chosen device or weapon up to Size 1 (or with three dots, Size 3), or to regenerate its charge or ammunition.",
        merit_type="dreamer",
        prerequisite="subliminal_conditioning:1,the_treatment:1",
        book="HL 85"
    ),
    Merit(
        name="Realpolitik",
        min_value=1,
        max_value=3,
        description="Apply as bonus dice to pass as a follower of a political group, or by spending Memory, as a leader.",
        merit_type="dreamer",
        prerequisite="subliminal_conditioning:1",
        book="HL 84"
    ),
    Merit(
        name="The Treatment",
        min_value=1,
        max_value=5,
        description="Choose a catalytic substance and a Skill category. Spend Memory and apply the catalyst to increase one of those Skills by your Treatment rating for a scene, at the cost of lethal damage.",
        merit_type="dreamer",
        prerequisite="subliminal_conditioning:1",
        book="HL 84"
    ),
    Merit(
        name="A Word From Our Sponsor",
        min_value=2,
        max_value=3,
        description="Your conditioned personality has stored independent accounts and resource caches. Spend Memory to recall enough to access an account or contact. With three dots, the network extends into the criminal underground.",
        merit_type="dreamer",
        prerequisite="subliminal_conditioning:1",
        book=""
    ),
]

# Create dictionary for easy lookup
dreamer_merits_dict = {merit.name.lower().replace(" ", "_").replace("(", "").replace(")", ""): merit for merit in dreamer_merits}
