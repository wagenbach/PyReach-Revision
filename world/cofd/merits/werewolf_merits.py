from world.cofd.stat_types import Merit

# Werewolf-Specific Merits
werewolf_merits = [
    # Location-based Merits
    Merit(
        name="Dedicated Locus",
        min_value=1,
        max_value=5,
        description="You've personally attuned a locus to your pack. The locus has a rating equal to this Merit, and provides the pack the ability to spend a point of Essence above their per-turn cap, a number of times per day equal to this Merit.",
        merit_type="supernatural",
        prerequisite="safe_place:1"
    ),
    Merit(
        name="Lodge Stronghold",
        min_value=2,
        max_value=4,
        description="As a five-dot Safe Place. With four dots, it boasts lines of supernatural defenses or spirit wards.",
        merit_type="supernatural",
        prerequisite="lodge_membership:1"
    ),
    Merit(
        name="Residential Area",
        min_value=1,
        max_value=5,
        description="Your pack has integrated into an inhabited territory. Every session, by canvassing for help, you can redistribute your dots in this Merit among effective dots of Allies, Contacts and Retainers.",
        merit_type="social",
        prerequisite="pack_membership:1"
    ),
]

# Create dictionary for easy lookup
werewolf_merits_dict = {merit.name.lower().replace(" ", "_").replace("(", "").replace(")", ""): merit for merit in werewolf_merits}

