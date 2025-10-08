from world.cofd.stat_types import Merit

# Promethean: The Created Specific Merits
promethean_merits = [
    Merit(
        name="Acid Stomach",
        min_value=1,
        max_value=1,
        description="Digest even inorganic matter as food",
        merit_type="physical",
        prerequisite="promethean"
    ),
    Merit(
        name="Azothic Object",
        min_value=1,
        max_value=5,
        description="Possess an object invested with a flare of your Azoth. Sense its direction intuitively, and distribute dots in this Merit among bonuses to its equipment rating, roll qualities, Durability, or ability to store Pyros",
        merit_type="supernatural",
        prerequisite="promethean"
    ),
    Merit(
        name="Benign Festering",
        min_value=1,
        max_value=3,
        description="Cause Wastelands as if your Azoth were lower by your dots in this Merit. Cause Festering using the lower of your effective Azoth and the Wasteland's",
        merit_type="supernatural",
        prerequisite="promethean"
    ),
    Merit(
        name="Companion",
        min_value=1,
        max_value=5,
        description="A spirit of Rank 1 has taken a liking to your character and follows her around. Distribute dots in this Merit past the first to assign either an extra Attribute dot and Numen to the spirit, or to grant it a physical body",
        merit_type="supernatural",
        prerequisite="promethean,ephemeral_flesh:1"
    ),
    Merit(
        name="Driven",
        min_value=1,
        max_value=5,
        description="Your Elpis renews your drive to press on. Receive a beneficial Condition each session for each dot in this Merit",
        merit_type="mental",
        prerequisite="promethean"
    ),
    Merit(
        name="Efficient Conductor",
        min_value=1,
        max_value=1,
        description="Electrocution restores an additional point of Health and an additional point of Pyros for every two points respectively restored",
        merit_type="supernatural",
        prerequisite="promethean"
    ),
    Merit(
        name="Famous Face",
        min_value=1,
        max_value=3,
        description="You were created with parts from somebody famous. When your donor's fame positively influences an action, take 8-Again and a bonus die",
        merit_type="social",
        prerequisite="promethean"
    ),
    Merit(
        name="Good Brain",
        min_value=1,
        max_value=5,
        description="Enough knowledge remains in the makeup of your nervous system to take the wheel for certain actions. Choose a Skill for each dot in this Merit. Once per story, you can reroll an action made with one of those Skills",
        merit_type="mental",
        prerequisite="promethean"
    ),
    Merit(
        name="Moth to the Flame",
        min_value=1,
        max_value=1,
        description="Recover a point of Pyros for every point of aggravated damage from fire",
        merit_type="supernatural",
        prerequisite="promethean,stamina:3"
    ),
    Merit(
        name="Repute",
        min_value=1,
        max_value=3,
        description="Your tale is told among the Created. Add dots in this Merit to Social rolls to influence those who've heard it, and once per story, call upon an equivalent rating of Allies if anyone who listens to the Ramble is around",
        merit_type="social",
        prerequisite="promethean"
    ),
    Merit(
        name="Residual Memory",
        min_value=1,
        max_value=5,
        description="Reflexes have soaked into the parts used to make you. Choose a Skill for each dot in this Merit. Every session, you can distribute twice your Residual Memory in bonus dice among rolls of these Skills",
        merit_type="mental",
        prerequisite="promethean"
    ),
    Merit(
        name="Sleepless",
        min_value=2,
        max_value=2,
        description="You don't have to sleep, and suffer no fatigue",
        merit_type="physical",
        prerequisite="promethean"
    ),
    Merit(
        name="Terrible Disfigurement",
        min_value=1,
        max_value=1,
        description="You look especially grotesque. Penalize Composure rolls by -2 for any human who's witnessed your disfigurements within the scene. You can use this shock as Hard Leverage",
        merit_type="social",
        prerequisite="promethean"
    ),
    Merit(
        name="Vivid Dreams",
        min_value=1,
        max_value=5,
        description="Take a special Aspiration that grants visions instead of beats. Add dots in this Merit to roll to recover Pyros from sleeping within your element. Each story, recover extra Willpower from sleep a number of times up to your dots in this Merit",
        merit_type="supernatural",
        prerequisite="promethean,wits:3"
    ),
    Merit(
        name="Weatherproof",
        min_value=1,
        max_value=1,
        description="Immune to Extreme Environments",
        merit_type="physical",
        prerequisite="promethean"
    ),
]

# Create dictionary for easy lookup
promethean_merits_dict = {merit.name.lower().replace(" ", "_").replace("(", "").replace(")", ""): merit for merit in promethean_merits}

