from world.cofd.stat_types import Merit

# Ghost-Specific Merits
ghost_merits = [
    #General Ghost Merits
    Merit(
        name="Brain Eater",
        min_value=1,
        max_value=1,
        description="Touch human corpses from Twilight. Eat organs for Memories left behind by death.",
        merit_type="ghost",
        prerequisite="",
        book="GtS2e 288"
    ),
    Merit(
        name="Dead Meat",
        min_value=1,
        max_value=1,
        description="Inhabit your dead body, substituting Health for Corpus. Healing non-bashing Health damage and resisting the degredation of your body requires raw meat by the pound. You must spend Willpower to gain people's attention nonviolently.",
        merit_type="ghost",
        prerequisite="",
        book="GtS2e 288"
    ),
    Merit(
        name="Deep Memory",
        min_value=1,
        max_value=1,
        description="Add your Resistance to your maximum stock of Memories before suffering Memory Bleed.",
        merit_type="ghost",
        prerequisite="",
        book="GtS2e 288"
    ),
    Merit(
        name="Wake",
        min_value=1,
        max_value=5,
        description="The living still mourn you enough to provide a point of Essence each chapter for each dot of Wake.",
        merit_type="ghost",
        prerequisite="",
        book="GtS2e"
    ),
    #Iconography Merits. Each Ghost May Only Have One.
    Merit(
        name="Ajna",
        min_value=1,
        max_value=1,
        description="You manifest a perceptive eye where an eye should not be. Gain a +3 Perception bonus, but double any penalties from sensory overload.",
        merit_type="ghost",
        prerequisite="",
        book="GtS2e 289"
    ),
    Merit(
        name="Banda",
        min_value=1,
        max_value=1,
        description="You have the uncanny sway of the ghede. Gain a +3 bonus to benefit from stealing the spotlight, but suffer a -2 Stealth penalty.",
        merit_type="ghost",
        prerequisite="",
        book="GtS2e 289"
    ),
    Merit(
        name="Crowned",
        min_value=1,
        max_value=1,
        description="You are surmounted by a glory of spectral light. When those around you roll to resist breaking points or crisis points, they gain a bonus die, but you lose Essence.",
        merit_type="ghost",
        prerequisite="",
        book="GtS2e 289"
    ),
    Merit(
        name="Immaculate Heart",
        min_value=1,
        max_value=1,
        description="Your ribcage is open, exposing a still-beating heart. Gain a +3 bonus to earn trust, but suffer -2 to guard your feelings.",
        merit_type="ghost",
        prerequisite="",
        book="GtS2e 289"
    ),
    Merit(
        name="Pierced",
        min_value=1,
        max_value=1,
        description="You remain forever impaled by weapons or openly wounded. The first time you take damage in a scene, you ignore it, but you also suffer a permanent -1 wound penalty.",
        merit_type="ghost",
        prerequisite="",
        book="GtS2e 289"
    ),
    Merit(
        name="Shackled",
        min_value=1,
        max_value=1,
        description="Chains or bindings weigh you down and suggest pain. You can recover two Essence from the presence of an Anchor once per chapter, but your Speed is permanently halved.",
        merit_type="ghost",
        prerequisite="",
        book="GtS2e 289"
    ),
    Merit(
        name="Veined",
        min_value=1,
        max_value=1,
        description="Veins pulse visibly through your Corpus and beyond. Spend Essence like a ghost of one Rank higher, but the first time in a scene you suffer damage, suffer an additional point.",
        merit_type="ghost",
        prerequisite="",
        book="GtS2e 289"
    ),
    Merit(
        name="Waters",
        min_value=1,
        max_value=1,
        description="Water always pours and drips from you. Spend Essence to adopt a pool of water as an Anchor for a scene, and while submerged in that pool, nothing can coerce you to leave it.",
        merit_type="ghost",
        prerequisite="",
        book="GtS2e 290"
    ),
]

# Create dictionary for easy lookup
ghost_merits_dict = {merit.name.lower().replace(" ", "_").replace("(", "").replace(")", ""): merit for merit in ghost_merits}
