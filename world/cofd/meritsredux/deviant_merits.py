from world.cofd.stat_types import Merit

# Deviant-Specific Merits
deviant_merits = [
    Merit(
        name="Armed and Extremely Dangerous",
        min_value=3,
        max_value=3,
        description="Overt. Conspirators pursuing you do not plan to confront you lightly, and will back down when not heavily armed.",
        merit_type="deviant",
        prerequisite="",
        book="DtR 100"
    ),
    Merit(
        name="Bleeding Heart",
        min_value=3,
        max_value=3,
        description="Once per chapter, you can roll Resolve + Composure to recover Willpower when achieving what would be your Virtue.",
        merit_type="deviant",
        prerequisite="",
        book="DtR 96"
    ),
    Merit(
        name="Blood on My Hands",
        min_value=3,
        max_value=3,
        description="Once per scene, you can roll Resolve + Composure to recover Willpower when feeding what would be your Vice.",
        merit_type="deviant",
        prerequisite="",
        book="DtR 96"
    ),
    Merit(
        name="The Company Line",
        min_value=2,
        max_value=2,
        description="Gain +2 on Intimidation, Persuasion, or Subterfuge rolls to win over a target for the conspiracy.",
        merit_type="deviant",
        prerequisite="",
        book="DevC 18"
    ),
    Merit(
        name="Flashback",
        min_value=1,
        max_value=1,
        description="Once per chapter, become Shaken to recollect information about your Divergence.",
        merit_type="deviant",
        prerequisite="",
        book="DtR 96"
    ),
    Merit(
        name="Good Samaritan",
        min_value=2,
        max_value=2,
        description="+2 to Intimidate or Persuade baseline humans away from the Web of Pain. When you risk yourself protecting them with your power, take a beat.",
        merit_type="deviant",
        prerequisite="",
        book="DtR 97"
    ),
    Merit(
        name="Lifeline",
        min_value=2,
        max_value=4,
        description="Sustain an additional Loyalty or Conviction Touchstone beyond the maximum, or at four dots, sustain two.",
        merit_type="deviant",
        prerequisite="",
        book="DtR 101"
    ),
    Merit(
        name="Linchpin",
        min_value=3,
        max_value=5,
        description="You are the Linchpin of a non-Hierarchical Node, or Hierarchical with five dots.",
        merit_type="deviant",
        prerequisite="[status:1,status:3]",
        book="DevC 18"
    ),
    Merit(
        name="Living Progenitor",
        min_value=3,
        max_value=5,
        description="Assign your Progenitor as an unwavering Touchstone so long as she lives. At five dots, heal instability by aiding her as a Loyalty Touchstone, or sparing her life as a Conviction Touchstone.",
        merit_type="deviant",
        prerequisite="",
        book="DtR 101"
    ),
    Merit(
        name="Loose Cannon",
        min_value=2,
        max_value=2,
        description="Once per scene, regain a point of Willpower when violating a conspiracy Principle to further an Objective.",
        merit_type="deviant",
        prerequisite="devoted_form",
        book="DevC 17"
    ),
    Merit(
        name="Manticore Companion",
        min_value=1,
        max_value=5,
        description="Overt. You keep a transformed animal as a pet, with Variations chosen as if entangled with a Scar equal to Merit rating.",
        merit_type="deviant",
        prerequisite="",
        book="DtR 101"
    ),
    Merit(
        name="Moral Compass",
        min_value=2,
        max_value=2,
        description="Once per chapter, grant Inspired to nearby conspiracy members and Devoted to further the conspiracy's Virtue or Principle.",
        merit_type="deviant",
        prerequisite="devoted_form",
        book="DevC 18"
    ),
    Merit(
        name="Prized Experiment",
        min_value=3,
        max_value=3,
        description="Overt. Conspirators pursuing you want to capture you alive and unharmed.",
        merit_type="deviant",
        prerequisite="",
        book="DtR 103"
    ),
    Merit(
        name="Prototype",
        min_value=1,
        max_value=5,
        description="Overt. Possess an abnormal tool with capabilities and design flaws equivalent to Variations and Scars.",
        merit_type="deviant",
        prerequisite="",
        book="Clades 57"
    ),
    Merit(
        name="Shared Suffering",
        min_value=2,
        max_value=2,
        description="+2 to Empathy or Medicine when aiding fellow Remade. When you save or spare the life of fellow Remade, take a beat.",
        merit_type="deviant",
        prerequisite="",
        book="DtR 98"
    ),
    Merit(
        name="Stabilizer",
        min_value=1,
        max_value=3,
        description="You have access to an item or treatment which staves off instability. Reduce Scar Resistance penalties from instability by dots in this Merit.",
        merit_type="deviant",
        prerequisite="",
        book="DtR 100"
    ),
    Merit(
        name="Voice of the Wild",
        min_value=2,
        max_value=3,
        description="+2 to soothe with Animal Ken. With three dots, communicate with manticores as if you shared a language.",
        merit_type="deviant",
        prerequisite="",
        book="DtR 104"
    ),
]

# Create dictionary for easy lookup
deviant_merits_dict = {merit.name.lower().replace(" ", "_").replace("(", "").replace(")", ""): merit for merit in deviant_merits}
