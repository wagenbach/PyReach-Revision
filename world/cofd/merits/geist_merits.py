from world.cofd.stat_types import Merit

# Geist-Specific Merits
geist_merits = [
    Merit(
        name="Architect",
        min_value=1,
        max_value=5,
        description="Extended actions to create something you care about making last distribute Merit dots as bonus dice across their rolls, and bonus dice grant the roll 8-Again. The Abiding also increase their maximum number of rolls.",
        merit_type="geist",
        prerequisite="",
        book="GTS2e 85"
    ),
    Merit(
        name="Dread Geist",
        min_value=3,
        max_value=3,
        description="Your Geist starts at Rank 4",
        merit_type="geist",
        prerequisite="",
        book="GtS2e 86"
    ),
    Merit(
        name="Grave Goods",
        min_value=1,
        max_value=5,
        description="You've hoarded the ghosts of equipment, tangible to (and consumable by) Sin-Eaters and ghosts. Each chapter, draw on up to your Merit rating in Availability's worth. The Hungry also recover Willpower from acquisition once per chapter.",
        merit_type="geist",
        prerequisite="",
        book="GtS2e 86"
    ),
    Merit(
        name="Manic States",
        min_value=1,
        max_value=5,
        description="Once per chapter, ignore the negative effects of your Condition for a scene, and stock your Merit rating as bonus dice to apply to rolls, which grant the rolls 8-Again. After the scene, lose 10-Again until your next dramatic failure or exceptional success. The Bereaved also achieve exceptional success on rolls using bonus dice on a threshold of three instead of five.",
        merit_type="geist",
        prerequisite="negative_persistant_condition",
        book="GtS2e 86"
    ),
    Merit(
        name="Memento",
        min_value=3,
        max_value=3,
        description="You possess a given Memento.",
        merit_type="geist",
        prerequisite="",
        book="GTS2e 87"
    ),
    Merit(
        name="Reconciler",
        min_value=1,
        max_value=3,
        description="Social Maneuvering to resolve matters and set things aright opens a Door for each Merit dot. The Kindly recover Willpower and gain a beat when they accomplish such maneuvers.",
        merit_type="geist",
        prerequisite="",
        book="GtS2e 87"
    ),
    Merit(
        name="Sympathetic",
        min_value=2,
        max_value=2,
        description="As the Universal Social Merit. The Bereaved inflict the same Condition on the other party.",
        merit_type="geist",
        prerequisite="",
        book="GtS2e 89"
    ),
    Merit(
        name="Retribution",
        min_value=1,
        max_value=5,
        description="Style. These maneuvers must be made while avenging harm done to those you feel responsible for. The Vengeful take 8-Again to Retribution maneuvers.",
        merit_type="geist",
        prerequisite="",
        book="GtS2e 88"
    ),
]

# Create dictionary for easy lookup
geist_merits_dict = {merit.name.lower().replace(" ", "_").replace("(", "").replace(")", ""): merit for merit in geist_merits}
