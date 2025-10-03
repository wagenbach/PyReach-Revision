from world.cofd.stat_types import Merit

# Demon: The Descent Specific Merits
demon_merits = [
    # Location-based Merits
    Merit(
        name="Bolthole",
        min_value=1,
        max_value=5,
        description="Your demon has a Bolthole, a pocket dimension tied to his demonic nature. The Bolthole is a Safe Place with a rating equal to this Merit. It exists outside normal space and can only be accessed by the demon who created it and those he permits entry. You may purchase Bolthole features separately.",
        merit_type="supernatural",
        prerequisite="demon"
    ),
    # Bolthole Features
    Merit(
        name="Arsenal",
        min_value=1,
        max_value=5,
        description="Once per session, your bolthole can supply one weapon with a rating equal to your Arsenal dots, two weapons with a rating one less than your Arsenal dots, and any number of weapons with a rating less than that.",
        merit_type="supernatural",
        prerequisite="bolthole:1"
    ),
    Merit(
        name="Cover-Linked",
        min_value=2,
        max_value=2,
        description="Choose one Cover identity. The bolthole only exists while you are in that Cover's form. Anything in the bolthole not provided by these features is lost forever when the bolthole stops existing.",
        merit_type="supernatural",
        prerequisite="bolthole:1"
    ),
    Merit(
        name="Easy Access",
        min_value=3,
        max_value=3,
        description="You can reassign the bolthole's entrance by touching a door and spending Aether. Characters still exit the bolthole the way they came in.",
        merit_type="supernatural",
        prerequisite="bolthole:1"
    ),
    Merit(
        name="No Twilight",
        min_value=1,
        max_value=1,
        description="Ephemeral beings that enter the bolthole manifest physically.",
        merit_type="supernatural",
        prerequisite="bolthole:1"
    ),
    Merit(
        name="Self-Destruct",
        min_value=1,
        max_value=1,
        description="You can implode your bolthole. Anyone inside takes lethal damage equal to your dots in Bolthole and has one turn to leave before the exit to reality is lost.",
        merit_type="supernatural",
        prerequisite="bolthole:1"
    ),
    Merit(
        name="Trap Door",
        min_value=2,
        max_value=2,
        description="The entrance from the physical realm into the bolthole only exists when you're outside it, although those capable can still enter from Twilight.",
        merit_type="supernatural",
        prerequisite="bolthole:1"
    ),
]

# Create dictionary for easy lookup
demon_merits_dict = {merit.name.lower().replace(" ", "_").replace("(", "").replace(")", ""): merit for merit in demon_merits}
