from world.cofd.stat_types import Merit

# Beast-Specific Merits
blank_merits = [
    Merit(
        name="",
        min_value=1,
        max_value=1,
        description="",
        merit_type="",
        prerequisite="",
        book=""
    ),
]

# Create dictionary for easy lookup
blank_merits_dict = {merit.name.lower().replace(" ", "_").replace("(", "").replace(")", ""): merit for merit in blank_merits}
