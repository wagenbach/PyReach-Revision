from world.cofd.stat_types import Merit

# Infected-Specific Merits
infected_merits = [
    Merit(
        name="Carrier",
        min_value=1,
        max_value=5,
        description="Effectively gain Unseen Sense (Suitable Breeding Grounds); Pass on the Infection with a Stamina + Carrier + Infection Condition roll.",
        merit_type="infected",
        prerequisite="",
        book="HL 88"
    ),
    Merit(
        name="Bloodkin",
        min_value=1,
        max_value=1,
        description="Reduce a target's Doors in a social maneuver if they share the same lineage of the Infection.",
        merit_type="infected",
        prerequisite="carrier:1",
        book="HL 90"
    ),
    Merit(
        name="Bulletman Syndrome",
        min_value=5,
        max_value=5,
        description="Gain 1/1 armor per dot of Stamina. If symptoms are acute or greater, unarmed attacks deal lethal damage at increasing modifiers. Double healing times for lethal and aggravated damage.",
        merit_type="infected",
        prerequisite="carrier:5",
        book="HL 88-89"
    ),
    Merit(
        name="The New Flesh",
        min_value=1,
        max_value=5,
        description="At one dot, halve all healing times. At three, heal one lethal per scene, (Stamina) times a day. At five, aggravated damage heals at the same rate as lethal. Penalise social rolls.",
        merit_type="infected",
        prerequisite="carrier>=merit",
        book="HL 89-90"
    ),
    Merit(
        name="Patient Zero",
        min_value=2,
        max_value=2,
        description="Force the Infection into a short dormancy, effectively becoming a normal human person for a time.",
        merit_type="infection",
        prerequisite="carrier:2",
        book="HL 90"
    ),
    Merit(
        name="Proud Parent",
        min_value=1,
        max_value=1,
        description="Treat spreading the Infection as fulfilling a Virtue, at the cost of a breaking point if something befalls the new Infected.",
        merit_type="infected",
        prerequisite="carrier:1",
        book="HL 90"
    ),
    Merit(
        name="Virulent",
        min_value=2,
        max_value=4,
        description="Style. The character can harness the Infection to cause lesser diseases in those he touches.",
        merit_type="infected",
        prerequisite="carrier>=merit",
        book="HL 90"
    ),
]

# Create dictionary for easy lookup
infected_merits_dict = {merit.name.lower().replace(" ", "_").replace("(", "").replace(")", ""): merit for merit in infected_merits}
