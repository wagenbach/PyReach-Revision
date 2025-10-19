from world.cofd.stat_types import Merit

# Demon-Specific Merits
demon_merits = [
    Merit(
        name="Advance Form",
        min_value=1,
        max_value=1,
        description="Have one less Modification or Technology, but one more Propulsion or Process.",
        merit_type="demon",
        prerequisite="",
        book="FoH 128"
    ),
    Merit(
        name="Consummate Professional Agenda",
        min_value=2,
        max_value=2,
        description="You can resolve an Agenda Condition twice rather than once per session.",
        merit_type="demon",
        prerequisite="",
        book="DtD 121"
    ),
    Merit(
        name="Cultists",
        min_value=2,
        max_value=5,
        description="You have a cult loyal to your demonic identity. More dots purchase more dedicated and loyal cultists, or at five dots, supernaturally endowed cultists.",
        merit_type="demon",
        prerequisite="",
        book="DtD 121"
    ),
    Merit(
        name="Efficient Dealer",
        min_value=2,
        max_value=2,
        description="Ignore one level of asset on the Demon's side when creating a pact.",
        merit_type="demon",
        prerequisite="",
        book="FoH 128"
    ),
    Merit(
        name="Electromagnetic Linguistics",
        min_value=2,
        max_value=2,
        description="Can speak and understand machine code. Includes instinctively understanding what computer code does or 'hearing' text messages as they're transmitted.",
        merit_type="demon",
        prerequisite="",
        book="FoH 128"
    ),
    Merit(
        name="High Tolerance",
        min_value=1,
        max_value=2,
        description="Can graft one gadget containing a Demon Form ability without losing access to an existing one. One dot allows for Modification or Technology, Two dots allows for Propulsion or Process.",
        merit_type="demon",
        prerequisite="",
        book="FoH 129"
    ),
    Merit(
        name="Living The Lie",
        min_value=1,
        max_value=1,
        description="Allows you to give Covers a Virtue and Vice and regain willpower using them or the Demon's own Virtue and Vice.",
        merit_type="demon",
        prerequisite="primium:2",
        book="FoH 129"
    ),
    Merit(
        name="Monkeywrencher",
        min_value=2,
        max_value=2,
        description="Gain the ability to negate Embeds that match the Demon's Cipher (with known Keys) or Incarnation. Spend an Aether and roll Resolve + Primum, each success subtracting from the Embed user's success. Can also counter Numina from Angels.",
        merit_type="demon",
        prerequisite="primium:2",
        book="FoH 129"
    ),
    Merit(
        name="Multiple Agendas",
        min_value=2,
        max_value=2,
        description="You have dedicated yourself to two Agendas",
        merit_type="demon",
        prerequisite="",
        book="DtD 121"
    ),
    Merit(
        name="Resonance Aware",
        min_value=1,
        max_value=5,
        description="Add the dots in Resonance Awareness to Primum when determining the range of sensing Aether.",
        merit_type="demon",
        prerequisite="wits:3",
        book="FoH 129"
    ),
    Merit(
        name="Resonance Sensitive",
        min_value=1,
        max_value=1,
        description="Activating the ability to detect Aether does not cost Aether. The ability to detect Aether can be turn on and off reflexively and you can automatically detect any nearby Aether.",
        merit_type="demon",
        prerequisite="wits:4",
        book="FoH 129"
    ),
    Merit(
        name="Suborned Infrastructure",
        min_value=1,
        max_value=3,
        description="You have taken over and rigged an instance of God-Machine Infrastructure to produce Aether. Like all Infrastructure, it has a linchpin.",
        merit_type="demon",
        prerequisite="",
        book="DtD 121"
    ),
    Merit(
        name="Subsumed Gadget",
        min_value=2,
        max_value=2,
        description="Integrate a Gadget into your Demonic form so it can be healed as if a part of their body and can be activated by concentrating. However, it cannot be hidden when Demonic Form is exposed.",
        merit_type="demon",
        prerequisite="primium:3",
        book="FoH 129"
    ),
    Merit(
        name="Sympathetic Stigmatic",
        min_value=2,
        max_value=2,
        description="Have a sympathetic friend who understands the Demon's plight. Gain +2 on all rolls to find a Key if the Sympathetic Stigmatic is present. Additionally, gain 9-again on all rolls to use an Interlock that has been unlocked in that Stigmatic's presence. The Stigmatic bears no obvious Stigmata, but suffers the same injury that the Demon does. Comes with the equivalent Stigmatic merit Sympathetic Demon.",
        merit_type="demon",
        prerequisite="true_friend",
        book="FoH 129"
    ),
    Merit(
        name="Tattooed Gadget",
        min_value=2,
        max_value=2,
        description="Can use your own body as hardware for Embedded Gadget creation. Tattooed Gadgets cannot be lost, stolen, destroyed or overclocked and do not need triggers for activation.",
        merit_type="demon",
        prerequisite="",
        book="FoH 129"
    ),
    Merit(
        name="Terrible Form",
        min_value=1,
        max_value=5,
        description="Style. Provides extra form elements.",
        merit_type="demon",
        prerequisite="",
        book="DtD 122"
    ),
    Merit(
        name="Versatile Transformation",
        min_value=1,
        max_value=1,
        description="When you partially transform, it costs one Aether for every two form abilities manifested. Manifesting extra abilities is optional.",
        merit_type="demon",
        prerequisite="",
        book="DtD 122"
    ),
]

# Create dictionary for easy lookup
demon_merits_dict = {merit.name.lower().replace(" ", "_").replace("(", "").replace(")", ""): merit for merit in demon_merits}
