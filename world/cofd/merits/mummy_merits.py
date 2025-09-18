from world.cofd.stat_types import Merit

# Mummy-Specific Merits
mummy_merits = [
    Merit(
        name="Cult",
        min_value=1,
        max_value=10,
        description="Although the character and composition of a mummy's cult can vary greatly, depending on the mummy and mortals in question, it's a truism that almost every mummy has one. Indeed, although it's represented by a Merit (and sub-Merits) on the character sheet, the cult system is an entire sub-design of its own in Mummy, befitting its importance to the game and to its main characters. The cult system is presented in detail in Chapter Three.",
        merit_type="supernatural",
        prerequisite="mummy"
    ),
    Merit(
        name="Enigma",
        min_value=1,
        max_value=5,
        description="All the Arisen are mysterious, occult figures who exist at the periphery of the supernatural world. That mummies exist at all is barely known to creatures who consider themselves well-kept secrets. Yet there are secrets within secrets, immortals shrouded from notice and attention. Books about them are lost or perish in mysterious fires. An endless string of improbable coincidences lead investigators through wild good chases or frustrating dead ends. Whenever a character takes an action intended to learn about the mummy, track her, or locate her, he suffers a penalty equal to the Enigma rating. This penalty does not inhibit basic perception checks to notice the mummy or contest attempts at stealth unless the mummy's attempting to hide in a crowd. Enigma does not make one invisible, just unremarkable. Members of the mummy's cult reverse the Enigma rating, applying it as a bonus whenever it should apply. In this way, followers may find their hidden demigod without exposing her to enemies and outsiders. Of course, nothing stops enemies from forcing an Arisen's cultists to serve as 'native guides' to plunder her tomb, or worse.",
        merit_type="supernatural",
        prerequisite="mummy,fame:0"
    ),
    Merit(
        name="Guild Status",
        min_value=1,
        max_value=5,
        description="As servants of a higher power, the Arisen aren't as preoccupied with status as some, but the very nature of their existence and efforts predisposes them to heeding its course. Since they are all impossibly ancient beings, it isn't age the Arisen respect, but their own social structures—the five guilds—and they do so instinctively. Each Arisen is a member of one of the five guilds, and thus has at least Guild Status • in her guild. Each guild subdivides its membership into three categories, represented by titles: apprentices (Guild Status •), journeymen (Guild Status •• through ••••), and guildmasters (Guild Status •••••). A player can add her mummy's dots in Guild Status to dice pools for social interactions with members of the Arisen's own guild. As with other uses of Status, these dots are not added to dice pools predicated on supernatural powers such as Affinities and Utterances. A mummy can't ever have more than one form of Guild Status; e.g., if she has any dots in Guild Status (Maa-Kep), she can't also have dots in Guild Status (Su-Menent). When a mummy leaves her guild, she loses all Guild Status dots in that guild and gains Guild Status • in a different guild. When she does, she loses access to her former Guild Affinity and gains use of his new guild's Affinity; this happens automatically, without experience expenditure.",
        merit_type="social",
        prerequisite="mummy"
    ),
    Merit(
        name="Relic",
        min_value=1,
        max_value=5,
        description="While the Arisen are charged with returning most relics they encounter to Duat, there are some notable exceptions. The mummy has a relic at the start of play. If she only has one, she probably uses it as the centering relic of her tomb's energies (though it can be removed and even activated in dire circumstances). Starting relics acquired through this Merit must be of the appropriate type for the mummy's guild. The Storyteller will provide the name and properties of each relic, and if the mummy bears more than one relic, at least one of them must be an object created in lost Irem. • The mummy is the bearer of a single one-dot relic. •• The mummy is the bearer of a single two-dot relic. ••• The mummy is the bearer of a single three-dot relic. •••• Select one: The mummy is the bearer of a single four-dot relic, or the bearer of a one-dot relic and a three-dot relic. ••••• Select one: The mummy is the bearer of a four-dot relic and a one-dot relic, or the bearer of a three-dot relic and a two-dot relic.",
        merit_type="supernatural",
        prerequisite="mummy"
    ),
    Merit(
        name="Tomb",
        min_value=1,
        max_value=10,
        description="A mummy's tomb is not her home. It's where she's buried. It's where her corpse is interred when she isn't using it, but it's also so, so much more. The tomb is infected with her nature and reinforces it, for better or for worse. It is the strong shield the Judges gave her against the fears of ignorant mortals and the ravages of aeons, but it is also the mightiest shackle they placed upon her will. It protects even as it enslaves. Mechanically, players can put up to 10 Merit dots into Tomb, spread between the Geometry, Peril, and Endowments aspects. If one wants to stretch one's point investment a little (or just likes helping the Storyteller heap grief on one's own head), one can reduce its cost by taking Drawbacks. If a player takes five points of Drawbacks, she could get five dots in each Tomb Merit aspect and have a potent tomb, indeed.",
        merit_type="supernatural",
        prerequisite="mummy"
    ),
    Merit(
        name="Tomb Geometry",
        min_value=1,
        max_value=5,
        description="The effects of sacred Egyptian geometry are so great that even the ignorant masses have heard of 'pyramid power' keeping fruit fresh or making razor blades sharpen. The geometry of a mummy's tomb is incalculably more sophisticated. It drains magic out of the sky, the soil, even the gazes of those who unknowingly gawp at it, and keeps that energy ready for its resident. • Perhaps two meters square with a sarcophagus. The interior is lined with worn carvings etched into the walls. Adds one die to attempts to recharge Pillars. •• The size of a small office, completely covered with carvings that look fresh and sharp. Adds two dice to attempts to recharge Pillars. ••• Underground, the burial hold lies beyond an antechamber filled with plunder and guarded by elegant statues and racks of prized possessions. Here and there, a highlight is picked out in gold or precious stones. Above the ground (at the time of the tomb's construction) a statue or obelisk jutted, though by now its inscriptions are worn and difficult to decipher. Adds three dice to attempts to recharge Pillars. •••• The aboveground element is an imposing statue, eerily untouched by the storms and vagaries of ages. Buried beneath (if the statue itself is not interred) is a suite of five or six imposing chambers, clad in breathtaking carvings whose details gleam with gold or coral. Adds four dice to attempts to recharge Pillars. ••••• A breathtaking monument—perhaps a sphinx about the size of a school bus—stands atop this tomb (unless the intervening centuries have buried it under the shifting sands). A staircase and passage lead to a maze of at least a dozen rooms cluttered with weapons, masks, stelae, and ritual tools, all preserved as if they were used yesterday. Guardian statues glare from corners, while the gleam of gold and lapis lazuli strike richly from every surface, even in the dimmest torchlight. Adds five dice to attempts to recharge Pillars.",
        merit_type="supernatural",
        prerequisite="mummy"
    ),
    Merit(
        name="Tomb Peril",
        min_value=1,
        max_value=5,
        description="Transgressing a mummy's crypt is dangerous, to say the least. The foremost danger is that its inhabitant is going to wake up, but some are perilous in their own right, even without an undead guardian lurching forth in rage. This peril can take two forms: Material traps, or an immaterial curse. Material traps range from standard architectural hazards (pits with spikes, a plummeting stone block) to more elaborate devices (spring-loaded darts, a room that seals itself and fills with sand, or a breeding pit for scorpions). Either way, they're presumably cleaned and reset by the inhabitant, or her agents. Material traps are triggered in a small area and do a point of lethal damage and a point of bashing damage for every dot allocated to this Merit aspect. The mummy can have one big trap or several small ones, as desired, but no matter how one handles it, players of interlopers get a Wits + Composure roll for their characters to notice a trap before it springs. Should they succeed, the trap has discharged without harming them, though it may have temporarily blocked their passage forward or backward. The curse, on the other hand, takes the form of a sinking unease, a profound yet sourceless distress that begins 100 feet from the tomb for every point invested. People who take the hint and stay back suffer no ill effects. Roll a pool of dice equal to their Willpower for those who push on and violate the tomb. If it succeeds, they can overcome the terror without further ado. Should it fail, they have to pay Willpower points to enter. The Willpower required is equal to the dots spent on Tomb (Peril). Note that this works on any entity with a Willpower rating, except the rightful inhabitant and those she has invited inside.",
        merit_type="supernatural",
        prerequisite="mummy"
    ),
    Merit(
        name="Tomb Curio",
        min_value=3,
        max_value=3,
        description="Your character's crypt contains something that someone has been seeking for a long, long time. This object has no mystical properties and isn't the missing piece of anyone's occult theory, nor is it objectively precious, but at some point, you can pick a character in your story (NPC only) who has an interest in Egyptian history or mysticism and say, 'That person wants my mummy's curio.' If the character is a researcher, the curio proves he was right all along and gets him tenure. If the character is a mage, it's a vital clue to one of those things wizards get all uptight about. If the character is a vampire, the curio reveals something damaging about a rival (or a rival bloodline, or a rival group, or something of that sort). The exact nature of the desire is in the Storyteller's hands, as are the lengths to which the character would go to acquire it. But make no mistake: It is desperately desired.",
        merit_type="supernatural",
        prerequisite="mummy"
    ),
    Merit(
        name="Tomb Obscure",
        min_value=1,
        max_value=1,
        description="Mortals have a blind spot for your character's tomb. A successful Wits + Occult roll has to be made for them to even notice it. (The Unseen Sense merit negates this.) If the roll fails, they cannot perceive it, nor can another roll be made for them to find it for 24 hours. A mortal can perceive it if he's shown the tomb by someone who knows it's there, but quickly loses it again outside the guide's presence—unless shown by its rightful inhabitant, in which case he can find it normally. If your character's Obscure Tomb is also Famous, it means that the exterior is renowned, but that people have no idea there's a hidden mummy inside.",
        merit_type="supernatural",
        prerequisite="mummy"
    ),
    Merit(
        name="Tomb Piece of Life",
        min_value=2,
        max_value=2,
        description="Your character's tomb incorporates something from her mortal life—not just signs of her service to the Judges, not just tools to aid her in implementing their will, but something intimately connected to her. Perhaps it's the mummy of a favored pet, servant, or spouse. Perhaps it's an image depicting a famous deed she performed, now long lost to history. Or perhaps it's an enigma, like 'Rosebud' in Citizen Kane, and makes sense only to her. Whatever it is, you describe it, and your Storyteller incorporates it into your mummy's forgotten history. This functions just like a one-dot Vestige, except that it cannot be removed from the tomb without losing its occult energies.",
        merit_type="supernatural",
        prerequisite="mummy"
    ),
    Merit(
        name="Tomb Prime Location",
        min_value=1,
        max_value=1,
        description="Your character's tomb has been relocated (probably by her cult) to somewhere eminently desirable. It could be on a museum campus or on a street like Cleopatra's Needle in London (if it's also Famous); it could be deep under Washington, D.C., or it could be ensconced on the top of a Hong Kong skyscraper.",
        merit_type="supernatural",
        prerequisite="mummy"
    ),
    Merit(
        name="Tomb Radiant",
        min_value=4,
        max_value=4,
        description="Pick one Pillar. If you successfully roll for your character to restore any Pillar while in her tomb, she receives a point in the chosen Pillar as well. For example, if you picked Ka, your mummy could meditate in her tomb, and so long as the roll was successful (i.e., restored at least one Pillar point), she'd also get a bonus point of Ka from her tomb.",
        merit_type="supernatural",
        prerequisite="mummy"
    ),
    Merit(
        name="Vestige",
        min_value=1,
        max_value=5,
        description="Your mummy starts play with one or more vestiges—objects filled with unrefined Sekhem. Mummies use these items to refresh memory, empower their tombs, and in dire circumstances, refuel their Pillars ('dire' because once cannibalized, vestiges remain at their new, lower ratings). Starting vestiges acquired through this Merit are assumed to align perfectly with their bearer's fetters. The Storyteller provides the description of each vestige, but players are encouraged to suggest concepts or ideas. • The mummy is the bearer of a single one-dot vestige. •• Select one: The mummy is the bearer of a single two-dot vestige, or the bearer or two one-dot vestiges. ••• Select one: The mummy is the bearer of a single three-dot vestige, or the bearer of a one-dot vestige and a two-dot vestige. •••• Select one: The mummy is the bearer of a single four-dot vestige, or the bearer of a one-dot vestige and a three-dot vestige. ••••• Select one: The mummy is the bearer of a single five-dot vestige; or the bearer of a two-dot vestige and a three-dot vestige.",
        merit_type="supernatural",
        prerequisite="mummy"
    ),
    Merit(
        name="Witness",
        min_value=3,
        max_value=3,
        description="Some mortals see past the awe and horror of Sybaris, witnessing the Arisen like fellow immortals. It is unknown what makes a companion spontaneously arise, though mummies have offered many theories over the millennia. Some believe Witnesses were beloved spouses or concubines whose souls were bound with necromancy to reincarnate and rejoin their loves in future Descents. Others believe they bear souls fit for the Rite of Return. Some Utterances and Affinities can transform mortals into Witnesses outright, either temporarily or permanently. Regardless of origin, Witnesses have always stood by the Arisen as servants, friends, and even occasional nemeses. If mortal, the character gains total immunity to Sybaris (supernatural companions are already immune). Additionally, he also feels an obsessive fascination with the Arisen. Whenever presented with an opportunity to accompany or learn more about mummies, he must do so unless his player makes a successful Wits + Composure roll. Success allows the Witness to act as desired for the rest of the day. Apply a cumulative –1 to the check per month since he last indulged his fascination (maximum –5). Such indulgence must dominate most waking activity for at least a week to reset the penalty to zero. Note that Witnesses aren't compelled to seek out the Arisen constantly. The obsession only flares up in the presence of a mummy or clues that would lead to the Arisen (or genuine information about them). Finally, the mortal gains a limited sixth sense, intuitively recognizing Arisen or the Lifeless as such upon perceiving them directly, in person. He may not know what this instinct means the first time it activates, but he will learn.",
        merit_type="supernatural",
        prerequisite="non_mummy"
    ),
    Merit(
        name="Witness Mentor",
        min_value=1,
        max_value=5,
        description="While mummies often turn to one another for guidance or simply make their own way, some find wisdom among mortals. A Mentor with the Witness Merit costs the same as one without. The advantages of a teacher immune to Sybaris are offset by the obsessive and often domineering attention such mentors pay to their immortal pupils.",
        merit_type="social",
        prerequisite="mummy"
    ),
    Merit(
        name="Witness Retainer",
        min_value=1,
        max_value=5,
        description="Many mummies have servants and agents acquired via the Retainer Merit, often priests or leaders within their cults. By default, such followers do not possess the Witness Merit. Servants capable of bearing witness to Utterances without panic are rarer and more precious, adding one dot to their value as Retainers. Theoretically, non-mummies can purchase Witness retainers, though few outside the Arisen even know that Witnesses exist or have reason to value them. Note: This merit adds +1 to the cost of regular Retainer merits when the retainer has the Witness quality.",
        merit_type="social",
        prerequisite=""
    ),
]

# Create dictionary for easy lookup
mummy_merits_dict = {merit.name.lower().replace(" ", "_").replace("(", "").replace(")", ""): merit for merit in mummy_merits}