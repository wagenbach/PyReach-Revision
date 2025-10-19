from world.cofd.stat_types import Merit

# Atariya-Specific Merits
atariya_merits = [
    Merit(
        name="Damn Lucky",
        min_value=1,
        max_value=4,
        description="Spend Willpower to prevent harm, up to your Damn Lucky rating in lethal damage or twice your rating in bashing per scene. You may choose to inflict the averted misfortune on another within the scene.",
        merit_type="atariya",
        prerequisite="",
        book="HL 79"
    ),
    Merit(
        name="All-In",
        min_value=3,
        max_value=3,
        description="Spend Willpower to reduce an action's dice pool to a special 8-Again chance die. On success, add half the removed dice as bonus successes.",
        merit_type="atariya",
        prerequisite="damn_lucky:1,resolve:3",
        book="HL 81"
    ),
    Merit(
        name="Count Down",
        min_value=1,
        max_value=1,
        description=" 	Your character has knowledge of their ability to cheat death and how many uses remain, but living with that knowledge inflicts a Persistent Condition.",
        merit_type="atariya",
        prerequisite="damn_lucky:1,nine_lives:1",
        book="HL 80"
    ),
    Merit(
        name="Easy Come, Easy Go",
        min_value=1,
        max_value=1,
        description="Unlikely circumstances permit you to exchange up to five Merit dots per session.",
        merit_type="atariya",
        prerequisite="damn_lucky:1",
        book="HL 81"
    ),
    Merit(
        name="Luck Flows Up",
        min_value=2,
        max_value=2,
        description="As the Thief of Fate Merit, at reduced cost.",
        merit_type="atariya",
        prerequisite="damn_lucky:1",
        book="HL 81"
    ),
    Merit(
        name="Mr. Lucky",
        min_value=1,
        max_value=1,
        description=" 	You notice a smiling apparition present when danger is looming. Ignore perception penalties to notice ambushes, and a successful such roll is always exceptional.",
        merit_type="atariya",
        prerequisite="damn_lucky:1",
        book="HL 80"
    ),
    Merit(
        name="Nine Lives",
        min_value=1,
        max_value=5,
        description="Character creation only. Redeem a dot of this Merit to cheat death.",
        merit_type="atariya",
        prerequisite="damn_lucky:1",
        book="HL 80"
    ),
    Merit(
        name="See The Flow",
        min_value=1,
        max_value=5,
        description="Gain a sense for the odds in or against a character's favor in an endeavor. Spend Willpower to nudge toward or away from those odds with dice modifiers, up to your See the Flow rating in dice per scene.",
        merit_type="atariya",
        prerequisite="damn_lucky:1",
        book="HL 81"
    ),
]

# Create dictionary for easy lookup
atariya_merits_dict = {merit.name.lower().replace(" ", "_").replace("(", "").replace(")", ""): merit for merit in atariya_merits}
