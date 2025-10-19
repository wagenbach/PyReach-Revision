from world.cofd.stat_types import Merit

# Hunter-Specific Merits
hunter_merits = [
    Merit(
        name="Back Road Atlas",
        min_value=1,
        max_value=1,
        description="Navigate through urban routes with a +2 to evade an enemy's notice, and gain the Edge in Chases outside of main streets.",
        merit_type="hunter",
        prerequisite="wits:2,[drive:2,athletics:2]",
        book="HtV2e 88"
    ),
    Merit(
        name="Cover Tracks",
        min_value=1,
        max_value=1,
        description="Wipe all traces of movement and interaction, rolling Intelligence + Survival or Stealth vs. Intelligence + Investigation.",
        merit_type="hunter",
        prerequisite="[survival:2,stealth:2]",
        book="HtV2e 90"
    ),
    Merit(
        name="Custom Gear Broker",
        min_value=1,
        max_value=3,
        description="Trade any equipment for any other equipment of equal or lesser cost once per chapter. Once per story, treat any merit as one higher when obtaining custom gear.",
        merit_type="hunter",
        prerequisite="socialize:2",
        book="HtV2e 92"
    ),
    Merit(
        name="Face In The Crowd",
        min_value=2,
        max_value=2,
        description="Blend into crowds with a +3 to evade or tail a target, and a -3 to opponents attempting to spot you.",
        merit_type="hunter",
        prerequisite="striking_looks:0",
        book="HtV2e 90"
    ),
    Merit(
        name="Force Multiplier",
        min_value=2,
        max_value=2,
        description="May treat non-Hunters (including supernaturals) as Hunters when using tactics. Requires leading the action yourself and risking more willpower for each participant.",
        merit_type="hunter",
        prerequisite="",
        book="PGttCC 26"
    ),
    Merit(
        name="Gut Feeling",
        min_value=2,
        max_value=2,
        description="Understand when something unnatural is going on with an investigation. Become Obsessed during occult investigations, but roll with +2 on Occult rolls.",
        merit_type="hunter",
        prerequisite="occult:2",
        book="HtV2e 88"
    ),
    Merit(
        name="Last Stand",
        min_value=2,
        max_value=2,
        description="Once a chapter, Roll Wits + Resolve or Stamina to take one action without penalties.",
        merit_type="hunter",
        prerequisite="[resolve:3,stamina:3]",
        book="HtV2e 90"
    ),
    Merit(
        name="Lucky Charm",
        min_value=1,
        max_value=1,
        description="While holding the charm, roll Resolve + Composure at the start of a scene. Success supresses the effects of negative mental Conditions. This action can be taken once per chapter.",
        merit_type="hunter",
        prerequisite="resolve:1,[occult:1,academics:1]",
        book="HtV2e 90"
    ),
    Merit(
        name="Masked Scent",
        min_value=1,
        max_value=1,
        description="Using something to alter or cover scent, roll Wits + Survival or Streetwise to gain the Edge and +1 to all rolls in a chase while being tracked by scent.",
        merit_type="hunter",
        prerequisite="[survival:2,streetwise:2]",
        book="HtV2e 91"
    ),
    Merit(
        name="Natural Tinkerer",
        min_value=2,
        max_value=2,
        description="Ignore penalties for improvised equipment and materials, with potentially adjusted equipment costs.",
        merit_type="hunter",
        prerequisite="wits:3,crafts:3",
        book="HtV2e 89"
    ),
    Merit(
        name="Robust Health",
        min_value=2,
        max_value=2,
        description="Substitute Intelligence or Dexterity + Survival for Medicine rolls to heal yourself.",
        merit_type="hunter",
        prerequisite="survival:3",
        book="HtV2e 91"
    ),
    Merit(
        name="Seance Devotee",
        min_value=1,
        max_value=5,
        description="Know a person per dot of the merit who is willing to help conduct a séance with you.",
        merit_type="hunter",
        prerequisite="occult:2",
        book="HtV2e 89"
    ),
    Merit(
        name="Tactical Insight",
        min_value=2,
        max_value=2,
        description="Roll Wits + Survival or Streetwise to choose when to act in initiative once per chapter. Dodge freely on an exceptional success.",
        merit_type="hunter",
        prerequisite="wits:3,[survival:3,streetwise:3]",
        book="HtV2e 89"
    ),
    Merit(
        name="Tight Lipped",
        min_value=2,
        max_value=2,
        description="Gain +2 to resist mundane interrogations.",
        merit_type="hunter",
        prerequisite="resolve:2",
        book="HtV2e 96"
    ),
    Merit(
        name="Touchstone",
        min_value=1,
        max_value=5,
        description="Gain an additional touchstone per dot.",
        merit_type="hunter",
        prerequisite="",
        book="HtV2e 96"
    ),
]

# Create dictionary for easy lookup
hunter_merits_dict = {merit.name.lower().replace(" ", "_").replace("(", "").replace(")", ""): merit for merit in hunter_merits}
