from world.cofd.stat_types import Merit

# Plain-Specific Merits
plain_merits = [
    Merit(
        name="Plain Reader",
        min_value=1,
        max_value=1,
        description="You've devoted your soul to radical pacifism. All acts of violence cause breaking points, but recover Willpower.",
        merit_type="plain",
        prerequisite="",
        book="HL 92"
    ),
    Merit(
        name="The Consequences of Violence",
        min_value=1,
        max_value=1,
        description="When you are struck and harmed unprovoked and do not respond in kind, your assailant then treats all acts of violence as breaking points.",
        merit_type="plain",
        prerequisite="plain_reader:1",
        book="HL 94"
    ),
    Merit(
        name="I'm Bleeding On You",
        min_value=1,
        max_value=1,
        description="When you suffer damage by violence, each point penalizes further attacks by witnesses for the scene.",
        merit_type="plain",
        prerequisite="plain_reader:1",
        book="HL 93"
    ),
    Merit(
        name="Most Infected Thing I've Ever Seen",
        min_value=2,
        max_value=2,
        description="You may convert damage taken into a Condition reflecting an ongoing Tilt from injury. Intensive care resolves Conditions formed by less than five points. Conditions formed by five points or more are Persistent.",
        merit_type="plain",
        prerequisite="plain_reader:1",
        book="HL 94"
    ),
    Merit(
        name="Over Before It Started",
        min_value=1,
        max_value=1,
        description="Once per session, you may intervene to force all violence onto yourself. Roll the number of assailants and take successes as lethal damage, but recover all Willpower.",
        merit_type="plain",
        prerequisite="plain_reader:1",
        book="HL 94"
    ),
    Merit(
        name="Phantom Pain",
        min_value=1,
        max_value=1,
        description="When an assailant damages you, you may inflict an equal number of points of temporary psychological damage. This damage does not injure, kill, or last longer than a scene, but wound penalties inflict Beaten Down, falling unconscious inflicts Guilty or similar Conditions, and dying inflicts a Persistent Condition.",
        merit_type="plain",
        prerequisite="plain_reader:1,im_bleeding_on_you:1",
        book="HL 94"
    ),
    Merit(
        name="The Push",
        min_value=1,
        max_value=5,
        description="You may protect a third party from violent aggressors by pushing them back, step by step. The aggressors may not attack your charges and must accumulate your Merit rating in successes on Resolve + Composure rolls, one per step, to attack you. On the sixth step without being attacked, you force them to withdraw.",
        merit_type="plain",
        prerequisite="plain_reader:1",
        book="HL 94"
    ),
    Merit(
        name="You Are Being Recorded",
        min_value=1,
        max_value=1,
        description="Announce your recorded evidence of violence and roll Presence + Expression. For the rest of the scene, no one can act violently until they successfully contest your roll with Resolve + Composure - (additional people recording).",
        merit_type="plain",
        prerequisite="plain_reader:1",
        book="HL 93"
    ),
]

# Create dictionary for easy lookup
plain_merits_dict = {merit.name.lower().replace(" ", "_").replace("(", "").replace(")", ""): merit for merit in plain_merits}
