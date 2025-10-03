from world.cofd.stat_types import Merit

# Hunter-Specific Merits
hunter_merits = [
    # Safe Place Features for Hunters
    Merit(
        name="Anathema",
        min_value=1,
        max_value=1,
        description="The Safe Place is warded against monsters with a specific power, prompting a Wits + Resolve - Safe Place roll on any attempt to break through, becoming Immobilized or Stunned on failure.",
        merit_type="supernatural",
        prerequisite="safe_place:1"
    ),
    Merit(
        name="Arsenal",
        min_value=1,
        max_value=1,
        description="Rolls to clean, fix, or improvise equipment gain +2.",
        merit_type="mental",
        prerequisite="safe_place:1"
    ),
    Merit(
        name="Concealed",
        min_value=1,
        max_value=1,
        description="Attempts to find the Safe Place through any means are penalised by -2.",
        merit_type="social",
        prerequisite="safe_place:1"
    ),
    Merit(
        name="Escape Hatch",
        min_value=1,
        max_value=1,
        description="The hunter(s) may roll Dexterity + Athletics or Survival to reach the secret exit without suffering any damage from the environment.",
        merit_type="physical",
        prerequisite="safe_place:1"
    ),
    Merit(
        name="Infirmary",
        min_value=1,
        max_value=1,
        description="Medicine rolls here are improved by +2 for any invested hunter with dots in the skill, and the space may substitute for a hospital for the purposes of injury and recovery.",
        merit_type="mental",
        prerequisite="safe_place:1"
    ),
    Merit(
        name="Home Security System",
        min_value=1,
        max_value=1,
        description="The Safe Place is outfitted with a defense system, penalising attempts to break in by Safe Place dots.",
        merit_type="social",
        prerequisite="safe_place:1"
    ),
]

# Create dictionary for easy lookup
hunter_merits_dict = {merit.name.lower().replace(" ", "_").replace("(", "").replace(")", ""): merit for merit in hunter_merits}

