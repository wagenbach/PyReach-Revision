from world.cofd.stat_types import Merit

# Mummy-Specific Merits
mummy_merits = [
    Merit(
        name="Artisan's Aptitude",
        min_value=3,
        max_value=3,
        description="When you spend Willpower on a dice pool involving your guild's relics, achieve exceptional success on a threshold of three instead of five.",
        merit_type="mummy",
        prerequisite="skill_specialty:1",
        book="MtC2e 105"
    ),
    Merit(
        name="Balanced",
        min_value=3,
        max_value=3,
        description="Your character has a second Balance. Once per chapter, you can restore a Pillar by serving both Balances in one scene.",
        merit_type="mummy",
        prerequisite="",
        book="MtC2e 105"
    ),
    Merit(
        name="Blue Lotus Pillar",
        min_value=3,
        max_value=3,
        description="Your character's defining pillar is particularly potent, enhancing the unique Affinity of their decree.",
        merit_type="mummy",
        prerequisite="pillar:5",
        book="MtC2e 105"
    ),
    Merit(
        name="Dead Celebrity",
        min_value=1,
        max_value=3,
        description="You possessed Fame in a previous Descent. Apply as a Social bonus to appeal to your resemblance to your famed self.",
        merit_type="mummy",
        prerequisite="",
        book="MtC2e 106"
    ),
    Merit(
        name="Dead Flesh",
        min_value=2,
        max_value=4,
        description="Twice per scene, you may spend two turns reassembling your body to reverse the upgrade of a lethal wound to aggravated. With four dots, you may spend a Pillar to reduce a fresh aggravated wound to lethal.",
        merit_type="mummy",
        prerequisite="",
        book="MtC2e 106"
    ),
    Merit(
        name="Enigma",
        min_value=1,
        max_value=5,
        description="Fate conspires to erase evidence of your life left behind. Investigation by non-cultists takes a -2 penalty and requires an additional clue for each dot of Enigma.",
        merit_type="mummy",
        prerequisite="fame:0",
        book="MtC2e 106"
    ),
    Merit(
        name="Fount of Vitality",
        min_value=4,
        max_value=4,
        description="Sealing the flesh lasts for two more turns. You may spend Willpower and sacrifice Defense to instead seal an invested cultist's flesh.",
        merit_type="mummy",
        prerequisite="all_pillars:1",
        book="MtC2e 106"
    ),
    Merit(
        name="Funerary Text",
        min_value=1,
        max_value=5,
        description="Your tomb contains records preparing you for the Trials of Duat. When you enter henet within your tomb, you may ask the Storyteller one yes-or-no question in Duat for each dot of Funerary Text.",
        merit_type="mummy",
        prerequisite="",
        book="MtC2e 107"
    ),
    Merit(
        name="Guild Paragon",
        min_value=3,
        max_value=3,
        description="Your skills are indispensible to your guild. You can stretch your talents to preturnatural levels with a Willpower point.",
        merit_type="mummy",
        prerequisite="guild_membership",
        book="MtC2e 107"
    ),
    Merit(
        name="Interstitial Lives",
        min_value=1,
        max_value=2,
        description="Bond to one mummy or to all Arisen of your meret. When a bonded mummy rises, you rise at the same Sekhem. With two dots, breaking points and Memory rolls gain +2 in their presence.",
        merit_type="mummy",
        prerequisite="",
        book="MtC2e 107"
    ),
    Merit(
        name="Overburdened",
        min_value=3,
        max_value=3,
        description="Your character has a second Burden. Once per chapter, you can restore a Pillar by suffering both Burdens in one scene.",
        merit_type="mummy",
        prerequisite="",
        book="MtC2e 107"
    ),
    Merit(
        name="Relic Sensitivity",
        min_value=2,
        max_value=2,
        description="Receive a +2 kepher bonus.",
        merit_type="mummy",
        prerequisite="",
        book="MtC2e 107"
    ),
    Merit(
        name="Resonant Lifetime",
        min_value=3,
        max_value=3,
        description="Retain clear memories of a single Descent, or if you have reincarnated into another body, the life of that body.",
        merit_type="mummy",
        prerequisite="",
        book="MtC2e 107"
    ),
    Merit(
        name="Resplendant Soul",
        min_value=3,
        max_value=3,
        description="Choose one secondary Pillar. When you replenish your defining Pillar by upholding your decree, also recover a point of the secondary Pillar.",
        merit_type="mummy",
        prerequisite="pillar:3",
        book="MtC2e 107"
    ),
    #Mummy Cult Merits
    Merit(
        name="Cult",
        min_value=1,
        max_value=5,
        description="You rule a scorpion cult, applying each dot after the first as a bonus dot of Reach or Grasp. Apply your cult's Dominance as a Social bonus amid your guild.",
        merit_type="mummy",
        prerequisite="",
        book="MtC2e 106"
    ),
    Merit(
        name="Cult Allies",
        min_value=1,
        max_value=5,
        description="As the Universal Merit",
        merit_type="mummy",
        prerequisite="",
        book="MtC2e 108"
    ),
    Merit(
        name="Cult Contacts",
        min_value=1,
        max_value=1,
        description="As the Universal Merit",
        merit_type="mummy",
        prerequisite="",
        book="MtC2e 109"
    ),
    Merit(
        name="Devotees",
        min_value=3,
        max_value=3,
        description="The cult has a bonus dot of Fidelity.",
        merit_type="mummy",
        prerequisite="",
        book="MtC2e 110"
    ),
    Merit(
        name="Fanatical",
        min_value=1,
        max_value=5,
        description="As the supernatural Merit. Cultists led by a sorcerer may perform the rites as cult actions.",
        merit_type="mummy",
        prerequisite="ritual_sorcerer:1,library:2,sorcerous_knowledge:1",
        book="MtC2e 117"
    ),
    Merit(
        name="Cult Library",
        min_value=1,
        max_value=3,
        description="As the Universal Merit.",
        merit_type="mummy",
        prerequisite="",
        book="MtC2e 112"
    ),
    Merit(
        name="Observance",
        min_value=2,
        max_value=2,
        description="Monthly tomb rites inspire cultists and cult actions. Participating mummies recover Willpower.",
        merit_type="mummy",
        prerequisite="",
        book="MtC2e 112"
    ),
    Merit(
        name="Cult Resources",
        min_value=1,
        max_value=5,
        description="As the Universal Merit.",
        merit_type="mummy",
        prerequisite="",
        book="MtC2e 113"
    ),
    Merit(
        name="Cult Retainer",
        min_value=1,
        max_value=5,
        description="At the universal Merit.",
        merit_type="mummy",
        prerequisite="",
        book="MtC 2e 114"
    ),
    Merit(
        name="Ritualistic Cult",
        min_value=1,
        max_value=1,
        description="The cult maintains a schedule of tomb rituals. Add Dominance as a bonus to restore Pillars through the tomb's Lifeweb.",
        merit_type="mummy",
        prerequisite="",
        book="MtC2e 114"
    ),
    Merit(
        name="Cult Safe Place",
        min_value=1,
        max_value=5,
        description="As the Universal Location Merit",
        merit_type="mummy",
        prerequisite="",
        book="MtC2e 114"
    ),
    Merit(
        name="Scapegoats",
        min_value=1,
        max_value=1,
        description="Once per story, the cult may resolve a mutiny by refocusing to a new cult action, healing two Fidelity wounds without sacrificing Reach or Grasp.",
        merit_type="mummy",
        prerequisite="",
        book="MtC2e 114"
    ),
    Merit(
        name="Scorpion Cult Initiation",
        min_value=1,
        max_value=5,
        description="As the Style Merit",
        merit_type="mummy",
        prerequisite="",
        book="MtC2e 114"
    ),
    Merit(
        name="Secretive",
        min_value=3,
        max_value=3,
        description="Cultists hide their identities from the less initiated. Investigating a cultist's ties requires additional clues equal to their Scorpion Cult Initiation.",
        merit_type="mummy",
        prerequisite="",
        book="MtC2e 115"
    ),
    Merit(
        name="Specialized Cultists",
        min_value=1,
        max_value=1,
        description="Cult assistance provides 9-Again to a given Skill.",
        merit_type="mummy",
        prerequisite="",
        book="MtC2e 115"
    ),
    Merit(
        name="Cult Staff",
        min_value=1,
        max_value=5,
        description="As the Universal Merit.",
        merit_type="mummy",
        prerequisite="",
        book="MtC2e 115"
    ),
    Merit(
        name="Cult Status",
        min_value=1,
        max_value=5,
        description="As the Universal Merit.",
        merit_type="mummy",
        prerequisite="",
        book="MtC2e 116"
    ),
    Merit(
        name="Syncretic",
        min_value=1,
        max_value=1,
        description="The cult incorporates local beliefs, providing a +2 cult action bonus to work alongside believers.",
        merit_type="mummy",
        prerequisite="",
        book="MtC2e 116"
    ),
    Merit(
        name="Vice Ridden Cult",
        min_value=2,
        max_value=2,
        description="As the Universal Merit.",
        merit_type="mummy",
        prerequisite="vice",
        book="MtC2e 116"
    ),
    Merit(
        name="Virtuous Cult",
        min_value=2,
        max_value=2,
        description="As the Universal Merit.",
        merit_type="mummy",
        prerequisite="virtue",
        book="MtC2e 116"
    ),
    Merit(
        name="Wayward Cult",
        min_value=3,
        max_value=3,
        description="The cult maintains no Iremite faith or loyalty and is deceived as to the nature of their Arisen master. It has no Judge's Doctrine, though it can sacrifice Dominance to develop a third Doctrine of its own. Its Reach and Grasp gain a +2 bonus to block other cults, but the first attack by a rival cult under a mummy's leadership inflicts aggravated Fidelity damage.",
        merit_type="mummy",
        prerequisite="",
        book="MtC2e 116"
    ),
]

# Create dictionary for easy lookup
mummy_merits_dict = {merit.name.lower().replace(" ", "_").replace("(", "").replace(")", ""): merit for merit in mummy_merits}
