from world.cofd.stat_types import Merit

# Psychic Vampire Specific Merits
psychic_vampire_merits = [
    Merit(
        name="Psychic Vampirism",
        min_value=1,
        max_value=5,
        description="Style. The use of psychic contact to drain vital energies from another.",
        merit_type="psychicvampire",
        prerequisite="",
        book="HL 101"
    ),
    Merit(
        name="Breath Stealer",
        min_value=1,
        max_value=3,
        description="Style. You've refined your psychic vampirism to steal from breath instead of touch.",
        merit_type="psychicvampire",
        prerequisite="psychic_vampirism:1",
        book="HL 103"
    ),
    Merit(
        name="Euphoric Touch",
        min_value=1,
        max_value=3,
        description="Style. Your psychic vampirism now numbs or causes euphoria.",
        merit_type="psychicvampire",
        prerequisite="psychic_vampirism:1",
        book="HL 103"
    ),
    Merit(
        name="Burst of Speed",
        min_value=1,
        max_value=1,
        description="Spend Ephemera to add +1 to Defense and +5 to Initiative and Speed for a turn.",
        merit_type="psychicvampire",
        prerequisite="psychic_vampirism:1",
        book="HL 103"
    ),
    Merit(
        name="Ephemeral Battery",
        min_value=1,
        max_value=5,
        description="You may store up to (Resolve + Ephemeral Battery) Ephemera at once.",
        merit_type="psychicvampire",
        prerequisite="psychic_vampirism:1",
        book="HL 103"
    ),
    Merit(
        name="Nocturnal Supremacy",
        min_value=2,
        max_value=5,
        description="You have an affinity for the darkness, and with the vampires with which you share a name.",
        merit_type="psychicvampire",
        prerequisite="psychic_vampirism:1",
        book="HL 103"
    ),
    Merit(
        name="Psychic Infection",
        min_value=1,
        max_value=1,
        description="When your psychic vampirism fills wound penalties or drains the last Willpower from a subject, roll Psychic Vampirism. Success inflicts Psychic Vampirism on the subject, which fades if they suffer full Ephemera Bleed without ever feeding.",
        merit_type="psychicvampire",
        prerequisite="psychic_vampirism:1",
        book="HL 103"
    ),
    Merit(
        name="Psychic Seduction",
        min_value=1,
        max_value=1,
        description="Your psychic vampirism can overwrite the victim's Vice with a Vice of your choice. Recovering their Vice costs Willpower equal to the sum of lethal damage and Willpower loss inflicted.",
        merit_type="psychicvampire",
        prerequisite="psychic_vampirism:1",
        book="HL 104"
    ),
    Merit(
        name="Psychic Transference",
        min_value=2,
        max_value=2,
        description="By bridging a victim and beneficiary with the touch of your psychic vampirism and spending additional Willpower and Ephemera, you may spend the Ephemera yield to heal or restore Willpower to the beneficiary instead of yourself.",
        merit_type="psychicvampire",
        prerequisite="psychic_vampirism:1",
        book="HL 104"
    ),
    Merit(
        name="Shapechanging",
        min_value=2,
        max_value=3,
        description="For each instance of this stackable Merit, choose a predator or nocturnal animal, or for three dots, any appropriate animal. You may spend Ephemera to take that animal's form.",
        merit_type="psychicvampire",
        prerequisite="psychic_vampirism:1",
        book="HL 104"
    ),
    Merit(
        name="Soul Eater",
        min_value=2,
        max_value=2,
        description="Your psychic vampirism can touch a ghost or spirit's ephemera.",
        merit_type="psychicvampire",
        prerequisite="psychic_vampirism:1",
        book="HL 104"
    ),
    Merit(
        name="Unearthly Beauty",
        min_value=1,
        max_value=2,
        description="Spend Ephemera to gain the benefits of Striking Looks ••. Apply 9-Again or 8-Again to appropriate rolls if you already possess Striking Looks • or ••. With two dots of Unearthly Beauty, spend a second Ephemera to extend this beauty for a lunar month.",
        merit_type="psychicvampire",
        prerequisite="psychic_vampirism:1",
        book="HL 104"
    ),
    Merit(
        name="Vampiric Potency",
        min_value=1,
        max_value=5,
        description="For each instance of this stackable Merit, choose one Attribute. You may spend Ephemera to increase that Attribute at a 1:1 rate for the scene, up to your Merit rating in bonus dots.",
        merit_type="psychicvampire",
        prerequisite="psychic_vampirism:1",
        book="HL 104"
    ),
]

# Create dictionary for easy lookup
psychic_vampire_merits_dict = {merit.name.lower().replace(" ", "_").replace("(", "").replace(")", ""): merit for merit in psychic_vampire_merits}
