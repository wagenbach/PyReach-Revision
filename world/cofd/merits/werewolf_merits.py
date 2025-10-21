from world.cofd.stat_types import Merit

# Werewolf-Specific Merits
werewolf_merits = [
    #General Werewolf Merits
    Merit(
        name="Anchored",
        min_value=1,
        max_value=2,
        description="Add dots in this Merit to the dice bonus offered by one Touchstone, and subtract them from the bonus offered by the other.",
        merit_type="werewolf",
        prerequisite="",
        book="WtF2e 105"
    ),
    Merit(
        name="Blood and Bone Affinity",
        min_value=2,
        max_value=5,
        description="Choose your Blood or Bone. You must spend Willpower to resist an opportunity to pursue that Anchor. Once per session, take the rote quality on an action that would replenish all Willpower through it. With five dots, applies to both.",
        merit_type="werewolf",
        prerequisite="harmony:3-8",
        book="WtF2e 105"
    ),
    Merit(
        name="Code of Honor",
        min_value=2,
        max_value=2,
        description="Gain a Virtue representing a human code of conduct. +3 to Resistance rolls to uphold your code, but you must spend Willpower to betray it.",
        merit_type="werewolf",
        prerequisite="harmony>=8",
        book="WtF2e 105"
    ),
    Merit(
        name="Controlled Burn",
        min_value=2,
        max_value=2,
        description="Shift into Hishu or Urhan during the Soft Rage. You can spend Willpower during a turn of lucidity to escape Death Rage.",
        merit_type="werewolf",
        prerequisite="resolve:3,composure:3",
        book="WtF2e 105"
    ),
    Merit(
        name="Creative Tactician",
        min_value=3,
        max_value=3,
        description="Reduce penalties on a teamwork action by your Purity, and once per session, offer a beat to the primary actor.",
        merit_type="werewolf",
        prerequisite="purity:2",
        book="WtF2e 105-106"
    ),
    Merit(
        name="Embodiment of the Firstborn",
        min_value=5,
        max_value=5,
        description="You carry yourself like your tribal patron. Raise both the current and maximum rating for one Attribute by a dot. Spend Willpower to render attackers Shaken for a turn.",
        merit_type="werewolf",
        prerequisite="any_tribe",
        book="WtF2e 106"
    ),
    Merit(
        name="Fading",
        min_value=3,
        max_value=3,
        description="When characters roll to notice you, penalize them by the number of failed rolls to do so that scene, by anyone. Once per scene, add Cunning as a die bonus to go unnoticed.",
        merit_type="werewolf",
        prerequisite="cunning:2",
        book="WtF2e 106"
    ),
    Merit(
        name="Fortified Form",
        min_value=3,
        max_value=5,
        description="Choose a non-Hishu form. That form receives 1/0 Armor at three dots, 1/1 at four, or 2/2 at five. May be purchased separately for multiple forms.",
        merit_type="werewolf",
        prerequisite="stamina:3,survival:2",
        book="WtF2e 106"
    ),
    Merit(
        name="Hearing Whispers",
        min_value=2,
        max_value=2,
        description="Take a turn of scrutiny to ascertain a person's Persistent Conditions of weakness, or to roll Wits + Skill to look for a suspected weakness.",
        merit_type="werewolf",
        prerequisite="bone_shadow",
        book="WtF2e 106"
    ),
    Merit(
        name="Impartial Mediator",
        min_value=3,
        max_value=3,
        description="During mediation, roll Presence + Persuasion + Honor vs each side's highest Resolve + Honor. Each side your roll beats must accept your finding.",
        merit_type="werewolf",
        prerequisite="honor:2",
        book="WtF2e 106-107"
    ),
    Merit(
        name="Living Weapon",
        min_value=3,
        max_value=5,
        description="Choose teeth or claws for a non-Hishu form. That attack gains Armor-Piercing 2. With four dots, its weapon rating increases by one. With five dots, it ignores non-magical Armor. May be purchased separately for multiple attacks.",
        merit_type="werewolf",
        prerequisite="stamina:3,survival:2",
        book="WtF2e 107"
    ),
    Merit(
        name="Moon-Kissed",
        min_value=1,
        max_value=1,
        description="Choose an Auspice Skill and a non-Auspice Skill you have dots in. The Auspice Skill gains 9-Again (or 8-Again if it already rerolls nines), and when spending Willpower under your birth moon, an extra bonus die. The other Skill loses 10-Again. May be purchased separately for multiple Skills.",
        merit_type="werewolf",
        prerequisite="auspice_skill:2",
        book="WtF2e 107"
    ),
    Merit(
        name="Nowhere to Run",
        min_value=2,
        max_value=2,
        description="Take a turn of scrutiny to get a rough idea of a person's Safe Places, or to roll Wits + Investigation to look for further homes or hiding places. You can't help leaving a mark when you drop in there.",
        merit_type="werewolf",
        prerequisite="hunter_in_darkness",
        book="WtF2e 107"
    ),
    Merit(
        name="Pack Dynamics",
        min_value=3,
        max_value=5,
        description="Add your dots in this Merit minus two as bonus dice to teamwork actions, and to Resistance rolls standing in defense of your pack. Penalize rolls by the same amount when a packmate goes missing.",
        merit_type="werewolf",
        prerequisite="",
        book="WtF2e 107"
    ),
    Merit(
        name="Resonance Sniper",
        min_value=3,
        max_value=3,
        description="Through a personal ritual or charm, you can redefine the resonance of a wellspring of Essence. Roll Manipulation + Occult as an extended action, once a day for a locus or once an hour otherwise.",
        merit_type="werewolf",
        prerequisite="wisdom:2",
        book="WtF2e 107"
    ),
    Merit(
        name="Self-Control",
        min_value=2,
        max_value=2,
        description="When stress impels you to change form at low Harmony, spend Willpower and break towards the flesh to ignore the stress impulse for a scene.",
        merit_type="werewolf",
        prerequisite="resolve:4",
        book="WtF2e 107"
    ),
    Merit(
        name="Sounds of the City",
        min_value=2,
        max_value=2,
        description="Take a turn of scrutiny and roll Wits + Politics to sense one of the Social Merits flowing through a person. With a scene of efforts, stem the flow of a number of mundane Social Merit dots up to your Cunning, indefinitely. Doing so stems one dot from each of your mundane Social Merits for the duration.",
        merit_type="werewolf",
        prerequisite="iron_master",
        book="WtF2e 107-108"
    ),
    Merit(
        name="Strings of the Heart",
        min_value=2,
        max_value=2,
        description="Take a turn of scrutiny to intuit a glimpse of what a person wants most. When you use the desire as leverage, the character must spend Willpower to resist your lures, you benefit from an improved social impression, and one Door opens both ways between you and the person.",
        merit_type="werewolf",
        prerequisite="storm_lord",
        book="WtF2e 108"
    ),
    Merit(
        name="Totem",
        min_value=1,
        max_value=5,
        description="You're dedicated to a totem spirit. You receive its benefits, are subject to its ban, and add your dots in this Merit to Social rolls with the totem. Packmates can share a totem spirit, contributing dots to its total totem points.",
        merit_type="werewolf",
        prerequisite="",
        book="WtF2e 108"
    ),
    Merit(
        name="Weakest Link",
        min_value=2,
        max_value=2,
        description="Take a turn of scrutiny to pick out the weakest member of a group in the current situation's context.",
        merit_type="werewolf",
        prerequisite="blood_talon",
        book="WtF2e 108"
    ),
    #Pure Merits
    Merit(
        name="Blood of Pangaea",
        min_value=4,
        max_value=4,
        description="While on the Hunt, after the first time suffering lethal damage in a scene, gain the ability to reflexively use the Awe, Dement or Emotional Aura Numina, rolling Presence + Wits to activate.",
        merit_type="werewolf",
        prerequisite="predator_king,primal_urge:4",
        book="NH:SM 21"
    ),
    Merit(
        name="Distillation of Form",
        min_value=4,
        max_value=4,
        description="Gain +1 to Size and Strength in Gauru and Urshul.",
        merit_type="werewolf",
        prerequisite="ivory_claw,primal_urge:3",
        book="NH:SM 21"
    ),
    Merit(
        name="Echoes of Pangaea",
        min_value=2,
        max_value=2,
        description="After a successful Sacred Hunt, gain +2 and 9-again on all rolls to hunt another character, or cause a character interacting with an animal to dramatically fail their action.",
        merit_type="werewolf",
        prerequisite="predator_king,primal_urge:3",
        book="NH:SM 21"
    ),
    Merit(
        name="Hunter's Sacrifice",
        min_value=2,
        max_value=2,
        description="After successfully killing prey in the Hunt, offer the prey as a sacrifice to the Shadow, preventing Essence Bleed for spirits in Flesh for Primal Urge in days.",
        merit_type="werewolf",
        prerequisite="predator_king,primal_urge:3",
        book="NH:SM 21"
    ),
    Merit(
        name="Legacy of the Hunt",
        min_value=3,
        max_value=3,
        description="Reflexively enter a Clash of Wills using the highest Renown against supernatural effects to slow, bind or prevent hunting.",
        merit_type="werewolf",
        prerequisite="ivory_claw,primal_urge:5",
        book="NH:SM 21"
    ),
    Merit(
        name="Refinement of Flesh",
        min_value=2,
        max_value=2,
        description="May choose to regenerate character's choice of bashing or lethal damage each turn, without having spending Essence.",
        merit_type="werewolf",
        prerequisite="ivory_claw,primal_urge:2",
        book="NH:SM 21"
    ),
    Merit(
        name="Refinement of Spirit",
        min_value=3,
        max_value=3,
        description="Increase effective spirit Rank by 1.",
        merit_type="werewolf",
        prerequisite="ivory_claw,primal_urge:3",
        book="NH:SM 21"
    ),
    Merit(
        name="Silver-Scoured",
        min_value=2,
        max_value=2,
        description="Silver is no longer a general Death Rage trigger, and gain 1/1 armor against damage from silver.",
        merit_type="werewolf",
        prerequisite="ivory_claw,primal_urge:3",
        book="NH:SM 21"
    ),
    Merit(
        name="Witch Stride",
        min_value=5,
        max_value=5,
        description="While on the Sacred Hunt, Spend a point of Willpower to Reach without a Locus, regardless of Harmony.",
        merit_type="werewolf",
        prerequisite="predator_king,primal_urge:5",
        book=""
    ),
    #Pack Merits
    Merit(
        name="Den",
        min_value=1,
        max_value=5,
        description="An enclosed Physical location for Packs to relax and feel safe",
        merit_type="werewolf",
        prerequisite="pack",
        book="Pack 29"
    ),
    Merit(
        name="Directed Rage",
        min_value=3,
        max_value=5,
        description="Packs have found a way to direct their Rage-filled members anger at foes rather than friends. At ••• packmates suffering Wasu-Im act as if they were one step closer to harmony 5 for control time. At •••• Characters in Basu-Im may roll Resolve + Composure to prioritize attacking non-pack members. At ••••• Characters won't Target or pursue packmates so long as they aren't a threat and roll Resolve + Composure to ignore innocents",
        merit_type="werewolf",
        prerequisite="pack",
        book="Pack 30"
    ),
    Merit(
        name="Magnanimous Totem",
        min_value=2,
        max_value=4,
        description="Wolf Blooded may take up to 5 dots in the Totem merit. Humans at ••• may take 1 dot of Totem, at •••• they may take up to 5",
        merit_type="werewolf",
        prerequisite="pack,non_werewolf",
        book="Pack 30"
    ),
    Merit(
        name="Moon's Grace",
        min_value=1,
        max_value=1,
        description="At 3 Dots the pack may learn to use Pack Tactics (The Pack 58) as if they were Uratha. At 4 Dots any member of the Pack may learn and leas Wolf Rites as if they were a Werewolf. At 5 dots, pack members may gain Renown and recieve Shadow and Wolf Gifts from spirits, spending Willpower instead of Essence. This cannot be taken if an Uratha is part of the Pack",
        merit_type="werewolf",
        prerequisite="non-werewolf,pack",
        book="Pack 31"
    ),
    Merit(
        name="Territorial Advantage",
        min_value=1,
        max_value=5,
        description="Packs may leverage familiarity with their territory to inflict Conditions or Tilts on intruders in their Territory by rolling the relevant Attribute + Skill + Merit Dots vs Attribute + the same Skill",
        merit_type="werewolf",
        prerequisite="pack",
        book="Pack 31"
    ),
    #Fighting Merits
    Merit(
        name="Call Out",
        min_value=2,
        max_value=2,
        description="Call a challenge as an instant action. So long as none attack your declared opponent but you, you penalize their attacks against others by your Honor. If either of you attack anyone outside the challenge, the opposite takes your Honor as a bonus to attack the violator.",
        merit_type="werewolf",
        prerequisite="honor:2,composure:3,intimidation:2",
        book="WtF2e 108"
    ),
    Merit(
        name="Efficient Killer",
        min_value=2,
        max_value=2,
        description="In Gauru form, you may sacrifice Defense to strike a Killing Blow against a living opponent who has also sacrificed or lost access to Defense. Doing so is a common trigger for Death Rage.",
        merit_type="werewolf",
        prerequisite="purity:2,strength:3,brawl:3,medicine:2",
        book="WtF2e 108"
    ),
    Merit(
        name="Flanking",
        min_value=2,
        max_value=2,
        description="You can sacrifice damage on an attack to instead penalize the victim's Initiative and Defense by your successes for the turn.",
        merit_type="werewolf",
        prerequisite="cunning:2,wits:3,brawl:2,stealth:2",
        book="WtF2e 108"
    ),
    Merit(
        name="Instinctive Defense",
        min_value=2,
        max_value=2,
        description="Calculate Defense in Urshul and Urhan forms using the higher, not lower, of Wits and Dexterity.",
        merit_type="werewolf",
        prerequisite="primal_urge:2,athletics:2",
        book="WtF2e 109"
    ),
    Merit(
        name="Spiritual Blockage",
        min_value=2,
        max_value=2,
        description="Make a Brawl or Weaponry attack at -2. If you deal damage, the victim involuntarily spends a point of Essence, to no benefit.",
        merit_type="werewolf",
        prerequisite="wisdom:2,wits:3,occult:3,brawl:1",
        book="WtF2e 109"
    ),
    Merit(
        name="Warcry",
        min_value=2,
        max_value=2,
        description="When in Gauru, Urshul, or Urhan form, you may roll Presence + Expression to howl across the Gauntlet. A number of listeners up to your successes suffer -2 to Initiative and -1 to Defense and attack rolls for the scene. The howl alerts spirits and seizes their attention.",
        merit_type="werewolf",
        prerequisite="glory:2,presence:3,expression:2,intimidation:2",
        book="WtF2e 110"
    ),
    #Lodge Merits
    Merit(
        name="Lodge Armory",
        min_value=3,
        max_value=5,
        description="Your lodge has a store of weapons, including those made with silver and other rare materials. At five dots, you may, at any given time, borrow one of three fetish weapons rated up to three dots each.",
        merit_type="werewolf",
        prerequisite="lodge",
        book="Pack 81"
    ),
    Merit(
        name="Lodge Connections",
        min_value=1,
        max_value=5,
        description="Once per session, benefit from an equivalent dot rating of Allies, Mentor, Resources, or Retainer.",
        merit_type="werewolf",
        prerequisite="lodge",
        book="Pack 81"
    ),
    Merit(
        name="Lodge Lorehouse",
        min_value=1,
        max_value=5,
        description="Specify a topic of interest for each dot in this Merit. When researching one of these topics at the lorehouse, cut research time in half and receive the rote quality.",
        merit_type="werewolf",
        prerequisite="lodge",
        book="Pack 81"
    ),
    Merit(
        name="Lodge Sorcery",
        min_value=3,
        max_value=5,
        description="You may use one (or two, with five dots) of your Lodge totem's Influences at a two-dot rating, with a dice pool of Presence + Wits. With five dots, once per story you may use an Influence at a four-dot rating.",
        merit_type="werewolf",
        prerequisite="lodge",
        book="Pack 81"
    ),
    #Werewolf Styles
    Merit(
        name="Favored Form",
        min_value=1,
        max_value=5,
        description="Style. You rely on one non-Hishu form more than others. Choose which form. For each dot in this Style, penalize one non-Social Attribute by one dot for an unchosen form.",
        merit_type="werewolf",
        prerequisite="primal_urge>favored_form",
        book="WtF2e 106"
    ),
    Merit(
        name="Tactical Shifting",
        min_value=1,
        max_value=5,
        description="Style. You've learned to incorporate quick shapeshifting into your combat maneuvers.",
        merit_type="werewolf",
        prerequisite="wits:3,dexterity:3,athletics:2",
        book="WtF2e 110"
    ),
    Merit(
        name="Uma Suguthkuth",
        min_value=1,
        max_value=5,
        description="Style. The secret werewolf-killing art of the Lodge of Garm.",
        merit_type="werewolf",
        prerequisite="garmir,strength:3,brawl:4",
        book="Pack 83"
    ),
]

# Create dictionary for easy lookup
werewolf_merits_dict = {merit.name.lower().replace(" ", "_").replace("(", "").replace(")", ""): merit for merit in werewolf_merits}
