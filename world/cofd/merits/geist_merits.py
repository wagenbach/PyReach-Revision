from world.cofd.stat_types import Merit

# Geist: The Sin-Eaters Specific Merits
geist_merits = [
    # Location-based Merits
    Merit(
        name="Bound Possessions",
        min_value=1,
        max_value=5,
        description="Your character has possessions bound to his geist. These items are tied to his supernatural nature and can be called back to him. Each dot in this Merit represents one significant item or a collection of minor items that the character can summon or dismiss at will.",
        merit_type="supernatural",
        prerequisite="geist"
    ),
]

# Create dictionary for easy lookup
geist_merits_dict = {merit.name.lower().replace(" ", "_").replace("(", "").replace(")", ""): merit for merit in geist_merits}

