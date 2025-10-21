from world.cofd.stat_types import Merit

# Vampire-Specific Merits
vampire_merits = [
    Merit(
        name="Acute Senses",
        min_value=1,
        max_value=1,
        description="Add Blood Potency as a bonus to use senses or identify sensory details. Exceptional successes can temporarily inflict Obsession.",
        merit_type="vampire",
        prerequisite="",
        book="VtR2e 109"
    ),
    Merit(
        name="Adaptive Feeding",
        min_value=3,
        max_value=3,
        description="Animal blood can sustain you up to Blood Potency 5. Above that, each willpower spent allows for two vitae rather than one.",
        merit_type="vampire",
        prerequisite="",
        book="GTTN 123"
    ),
    Merit(
        name="Atrocious",
        min_value=1,
        max_value=1,
        description="Take 8-Again to evoke the monstrous Beast, but lose 10-Again to evoke or resist the seductive or competitive Beast.",
        merit_type="vampire",
        prerequisite="cutthroat:0,enticing:0",
        book="VtR2e 110"
    ),
    Merit(
        name="Beloved",
        min_value=2,
        max_value=2,
        description="You have a deep bond with a living Touchstone. Add +1 to resist detachment after spending an hour with your Touchstone.",
        merit_type="vampire",
        prerequisite="",
        book="TY 83"
    ),
    Merit(
        name="Bloodhound",
        min_value=2,
        max_value=2,
        description="Smelling blood is as good as tasting it for your Kindred Senses.",
        merit_type="vampire",
        prerequisite="wits:3",
        book="VtR2e 110"
    ),
    Merit(
        name="Call the Beast",
        min_value=4,
        max_value=4,
        description="Wield Animalism powers against revenants, contested by their Resolve + Vitae.",
        merit_type="vampire",
        prerequisite="humanity<5",
        book="TY 83"
    ),
    Merit(
        name="Casual User",
        min_value=2,
        max_value=2,
        description=" 	Confers the benefits of having one dot of Carthian Status as regard social bonuses and the effects of others' Carthian Law usage. Once a story, call upon a small favor.",
        merit_type="vampire",
        prerequisite="carthian_status:0",
        book="SotC 178"
    ),
    Merit(
        name="Chorister",
        min_value=2,
        max_value=2,
        description="Confers the benefits of having one dot of Crone Status as regard social bonuses and Merit access. May learn one dot of the Crúac Discipline and additional rites. Once a story, call upon a small favor.",
        merit_type="vampire",
        prerequisite="crone_status:0",
        book="SotC 181"
    ),
    Merit(
        name="Claws of the Unholy",
        min_value=1,
        max_value=1,
        description="When you use Unnatural Aspect claws in frenzy, their weapon rating becomes +0A.",
        merit_type="vampire",
        prerequisite="protean:4",
        book="VtR2e 110"
    ),
    Merit(
        name="Close Family",
        min_value=1,
        max_value=1,
        description="Blood sympathy manifests as if blood ties were one step closer, with a +1 bonus and 8-Again, but you can't spend Willpower for bonus dice in a scene where you've felt it.",
        merit_type="vampire",
        prerequisite="",
        book="VtR2e 111"
    ),
    Merit(
        name="Cutthroat",
        min_value=1,
        max_value=1,
        description="Take 8-Again to evoke the competitive Beast, but lose 10-Again to evoke or resist the monstrous or seductive Beast.",
        merit_type="vampire",
        prerequisite="atrocious:0,enticing:0",
        book="VtR2e 111"
    ),
    Merit(
        name="Distinguished Palate",
        min_value=1,
        max_value=1,
        description="All Taste of Blood successes are exceptional, but you lose the first Vitae ingested in a scene from any vessel without a chosen trait you consider a delicacy.",
        merit_type="vampire",
        prerequisite="",
        book="VtR2e 111"
    ),
    Merit(
        name="Dream Visions",
        min_value=1,
        max_value=1,
        description="Once a night, when meeting a new person or visiting a new place, roll Blood Potency to have had prophetic dreams that answer a question about the subject.",
        merit_type="vampire",
        prerequisite="mekhet",
        book="VtR2e 111"
    ),
    Merit(
        name="Enticing",
        min_value=1,
        max_value=1,
        description="Take 8-Again to evoke the seductive Beast, but lose 10-Again to evoke or resist the monstrous or competitive Beast.",
        merit_type="vampire",
        prerequisite="atrocious:0,cutthroat:0",
        book="VtR2e 112"
    ),
    Merit(
        name="Feeding Grounds",
        min_value=1,
        max_value=5,
        description="You hold known influence over territory. While there, add dots in this Merit as a bonus to hunt, and to clash with the Predatory Aura.",
        merit_type="vampire",
        prerequisite="",
        book="VtR2e 112"
    ),
    Merit(
        name="Ghoul Retainers",
        min_value=1,
        max_value=5,
        description="As retainer, except they have dots in the regnant's disciplines equal to half the dots in this merit, rounded up.",
        merit_type="vampire",
        prerequisite="",
        book="VtR2e 101"
    ),
    Merit(
        name="Group Touchstone",
        min_value=1,
        max_value=10,
        description="Gain a communal touchstone at the next level of humanity. A number of benefits are gained and shared by the coterie.",
        merit_type="vampire",
        prerequisite="must_equal_coterie_size",
        book="GTTN 69"
    ),
    Merit(
        name="Heart of Stone",
        min_value=2,
        max_value=2,
        description="Limit your need for and benefit from Touchstones by attaching yourself to a longstanding edifice or organization.",
        merit_type="vampire",
        prerequisite="feeding_grounds:2",
        book="TY 83"
    ),
    Merit(
        name="Herd",
        min_value=1,
        max_value=5,
        description="You have marks willing to offer up twice your dots in this Merit in Vitae weekly, without a roll.",
        merit_type="vampire",
        prerequisite="",
        book="VtR2e 112"
    ),
    Merit(
        name="Honey Trap",
        min_value=1,
        max_value=1,
        description="A vampire who tastes your blood regains Willpower, and also takes a beat if it advances the Vinculum.",
        merit_type="vampire",
        prerequisite="not_revenant",
        book="VtR2e 112"
    ),
    Merit(
        name="Independent Study",
        min_value=2,
        max_value=2,
        description="Confers the benefits of having one dot of Ordo Status as regards social bonuses. Once per story, call upon a small favor.",
        merit_type="vampire",
        prerequisite="ordo_status:0",
        book="SotC 197"
    ),
    Merit(
        name="Kindred Status",
        min_value=1,
        max_value=5,
        description="As the general Status Merit, divided into City, Clan, and Covenant Status. If you hold Status in multiple covenants, your total dots of Covenant Status can't exceed five.",
        merit_type="vampire",
        prerequisite="",
        book="VtR2e 113"
    ),
    Merit(
        name="Kiss of the Succubus",
        min_value=1,
        max_value=1,
        description="When you inflict Swooning by feeding on a mortal vessel, also inflict Addicted.",
        merit_type="vampire",
        prerequisite="daeva",
        book="VtR2e 113"
    ),
    Merit(
        name="Laity",
        min_value=2,
        max_value=2,
        description="Confers the benefits of having one dot of Lancea Status as regards social bonuses. Once per story, call upon a small favor.",
        merit_type="vampire",
        prerequisite="sanctified_status:0",
        book="SotC 193"
    ),
    Merit(
        name="Lineage",
        min_value=1,
        max_value=1,
        description="Once per session, you can borrow one dot of your sire's Allies, Contacts, Mentor, Resources, or Status.",
        merit_type="vampire",
        prerequisite="clan_status:1",
        book="VtR2e 113"
    ),
    Merit(
        name="Lingering Dreams",
        min_value=2,
        max_value=2,
        description="Subjects share your prophetic dreams about them, inflicting Swooning.",
        merit_type="vampire",
        prerequisite="dream_visions:1",
        book="DE2 142"
    ),
    Merit(
        name="Major Domo",
        min_value=3,
        max_value=3,
        description="You operate an Elysium or other Kindred gathering point. Persuasion, Intimidation and Socialize take +2 against Kindred so long as your hospitality is secure.",
        merit_type="vampire",
        prerequisite="",
        book="TY 83"
    ),
    Merit(
        name="Married By Blood",
        min_value=1,
        max_value=1,
        description="You have a strong mutual relationship with a Kindred Touchstone. Pool your Haven and Retainer Merits together, but share each other's Kindred Status loss.",
        merit_type="vampire",
        prerequisite="",
        book="TY 83"
    ),
    Merit(
        name="One Foot In the Door",
        min_value=2,
        max_value=2,
        description="Confers the benefits of having one dot of Invictus Status as regards social bonuses. Once per story, call upon a small favor.",
        merit_type="vampire",
        prerequisite="invictus_status:0",
        book="SotC 187"
    ),
    Merit(
        name="Pack Alpha",
        min_value=1,
        max_value=1,
        description="Decide how you ritually mark a vampire or ghoul as part of your pack. Pack members take 8-Again to teamwork support rolls. When questioned by your pack and you don't cow them, lose Willpower. Exile from the pack is violent and lasting.",
        merit_type="vampire",
        prerequisite="gangrel",
        book="VtR2e 114"
    ),
    Merit(
        name="Receptive Mind",
        min_value=1,
        max_value=5,
        description="When you Lay Open the Mind, add an extra target for each dot in this Merit.",
        merit_type="vampire",
        prerequisite="blood_potency:6,auspex:4",
        book="TY 84"
    ),
    Merit(
        name="Revenant Impostor",
        min_value=1,
        max_value=1,
        description="May replace Alternate Identity. You can masquerade as a revenant.",
        merit_type="vampire",
        prerequisite="manipulation:3,subterfuge:2",
        book="HD 80"
    ),
    Merit(
        name="Savoir of the Lost",
        min_value=3,
        max_value=3,
        description="Replace the Humanity cost to uplift a revenant you did not sire with a detachment roll. On success, spend a Willpower dot instead.",
        merit_type="vampire",
        prerequisite="",
        book="TY 84"
    ),
    Merit(
        name="Special Treat",
        min_value=3,
        max_value=3,
        description="You keep a ghoul with addictive blood, who costs extra Vitae to maintain each month.",
        merit_type="vampire",
        prerequisite="",
        book="TY 84"
    ),
    Merit(
        name="Swarm Form",
        min_value=2,
        max_value=2,
        description="You can become a swarm of Size 0 or 1 creatures when you take the Beast's Skin.",
        merit_type="vampire",
        prerequisite="protean:3",
        book="VtR2e 114"
    ),
    Merit(
        name="Touchstone",
        min_value=1,
        max_value=5,
        description="You have an extra Touchstone for each dot in this Merit. Each Touchstone attaches to the next level of Humanity down after the last.",
        merit_type="vampire",
        prerequisite="",
        book="VtR2e 115"
    ),
    Merit(
        name="Unassuming Guise",
        min_value=2,
        max_value=2,
        description="Apply a +3 bonus to present as an unassuming or human.",
        merit_type="vampire",
        prerequisite="",
        book="GTTN 124"
    ),
    Merit(
        name="Undead Menses",
        min_value=2,
        max_value=2,
        description="You produce unnatural menstrual blood that, once per night when applied, can grant 8-Again to a Crúac ritual or reduce Resistance against a Discipline by up to your Blood Potency.",
        merit_type="vampire",
        prerequisite="female_at_birth",
        book="VtR2e 115"
    ),
    Merit(
        name="Unnatural Affinity",
        min_value=1,
        max_value=5,
        description="Choose another type of supernatural creature for each dot in this Merit. You can feed on their Vitae as if they were Kindred.",
        merit_type="vampire",
        prerequisite="",
        book="VtR2e 114"
    ),
    Merit(
        name="Unsettling Gaze",
        min_value=1,
        max_value=1,
        description="When you roll an exceptional success to infect a victim with Integrity or Humanity greater than yours with the monstrous Beast, your victim experiences a breaking point. If your Humanity is greater than 2, so do you.",
        merit_type="vampire",
        prerequisite="nosferatu",
        book="VtR2e 115"
    ),
    Merit(
        name="Wicked Jaws",
        min_value=2,
        max_value=2,
        description="When feeding violently, your bite is a 2L attack, or +1L if other bonuses already apply.",
        merit_type="vampire",
        prerequisite="",
        book="GTTN 127"
    ),
    #Vampire Style Merits
    Merit(
        name="Blood Chymistry",
        min_value=1,
        max_value=5,
        description="Style. You have learned the art of Hypatian alchemy.",
        merit_type="vampire",
        prerequisite="resources:2,safe_place:1,skill_specialty:1",
        book="NH:SB 93"
    ),
    Merit(
        name="Cacophony Savvy",
        min_value=1,
        max_value=3,
        description="Style. You have your finger on the pulse of the Kindred underground.",
        merit_type="vampire",
        prerequisite="city_status:1",
        book="VtR2e 110"
    ),
    Merit(
        name="Courtoisie",
        min_value=1,
        max_value=3,
        description="Style. You have specialized in polite dueling and have learned how to honorably stab someone into torpor.",
        merit_type="vampire",
        prerequisite="composure:3,socialize:2,weaponry:2",
        book="SotC 187"
    ),
    Merit(
        name="Crusade",
        min_value=1,
        max_value=3,
        description="Style. You are trained in the combat style of the Lancea Et Sanctum's crusaders.",
        merit_type="vampire",
        prerequisite="[theban_sorcery:1,sorcerous_eunuch:1],resolve:3,occult:2,weaponry:2",
        book="SotC 192"
    ),
    Merit(
        name="Dynasty Membership",
        min_value=1,
        max_value=3,
        description="Style. Your character claims membership in a long standing dynasty of Kindred and knows how to use it.",
        merit_type="vampire",
        prerequisite="clan_status:1",
        book="VtR2e 112"
    ),
    Merit(
        name="Kindred Dueling",
        min_value=1,
        max_value=5,
        description="Style. Your character has specifically trained in the variables of Kindred on Kindred violence.",
        merit_type="vampire",
        prerequisite="composure:3,weaponry:2",
        book="VtR2e 117"
    ),
    Merit(
        name="Mobilize Outrage",
        min_value=1,
        max_value=3,
        description="Style. Your character fights with the passion of the oppressed.",
        merit_type="vampire",
        prerequisite="willpower:5,brawl:2,carthian_status:1",
        book="SotC 178"
    ),
    Merit(
        name="Riding The Wave",
        min_value=1,
        max_value=5,
        description="Style. You've learned all the advantages of riding the wave in combat.",
        merit_type="vampire",
        prerequisite="composure:3,resolve:3",
        book="VtR2e 118"
    ),
    Merit(
        name="Rites of the Impaled",
        min_value=1,
        max_value=3,
        description="Style. You have joined the warrior sect of the Ordo Dracul, the Impaled",
        merit_type="vampire",
        prerequisite="resolve:3,stamina:3,weaponry:2,sworn",
        book="SotC 197"
    ),
    Merit(
        name="Temple Guardian",
        min_value=1,
        max_value=3,
        description="Style. You are a devoted protector of the Circle of the Crone's temples.",
        merit_type="vampire",
        prerequisite="athletics:2,brawl:2,weaponry:2,crone_status:1",
        book="SotC 182"
    ),
    #Coterie Merits (All of these require multiple contributors)
    Merit(
        name="Common Enmity",
        min_value=1,
        max_value=3,
        description="The highest dots of this merit in the coterie determines the power of the enemy. Once per scene, you can apply your dots in this merit to any roll meant to harm or inconvenience the target.",
        merit_type="vampire",
        prerequisite="",
        book="GTTN 127"
    ),
    Merit(
        name="Goal",
        min_value=2,
        max_value=5,
        description="The more dots in the merit, the longer and more complicated the communal goal. Everyone who invested in this merit loses the merit but gains experience equal to total dots contributed to the merit upon completion.",
        merit_type="vampire",
        prerequisite="",
        book="GTTN 127"
    ),
    Merit(
        name="History",
        min_value=2,
        max_value=5,
        description="Once per chapter you may add its cumulative dots to a teamwork roll with another member sharing this merit. Add the cumulative dots to all blood sympathy rolls, even without blood relations.",
        merit_type="vampire",
        prerequisite="",
        book="GTTN 128"
    ),
    #Elder Merits
    Merit(
        name="Around The Block",
        min_value=2,
        max_value=2,
        description="Ignore untrained skill penalties.",
        merit_type="vampire",
        prerequisite="elder,any_skill:6",
        book="TY 83"
    ),
    Merit(
        name="Civilization Stalker",
        min_value=3,
        max_value=3,
        description="Politics, Socialize and Streetwise take 9-Again when calling on your experience.",
        merit_type="vampire",
        prerequisite="elder,[intelligence:3,manipulation:3]",
        book="TY 83"
    ),
    Merit(
        name="Dynasty Progenitor",
        min_value=2,
        max_value=2,
        description="You originated this dynasty. Double blood sympathy bonuses to wield Disciplines and Devotions on dynasts.",
        merit_type="vampire",
        prerequisite="elder,dynasty_membership:3",
        book="TY 85"
    ),
    Merit(
        name="Mentor In Immortality",
        min_value=1,
        max_value=5,
        description="You've taken a protegé for each dot in this Merit. Once per story, you may call a favor from each student.",
        merit_type="vampire",
        prerequisite="elder",
        book="TY 83"
    ),
    Merit(
        name="Practiced Puppeteer",
        min_value=2,
        max_value=2,
        description="Take 9-Again when you wield the chosen Discipline's powers against a character without a Supernatural Tolerance of at least your Blood Potency - 3.",
        merit_type="vampire",
        prerequisite="elder,any_discipline:5",
        book="TY 84"
    ),
    Merit(
        name="Prima Donna",
        min_value=1,
        max_value=5,
        description="Each story, once per dot of this Merit, spend Willpower to ignore soft leverage, shut down a Social Condition, exert your Status at one dot higher, or take 8-Again on a Social roll against the covenants.",
        merit_type="vampire",
        prerequisite="covenant_status:0",
        book="TY 84"
    ),
    Merit(
        name="Spectral Communion",
        min_value=4,
        max_value=4,
        description="Once a story, anoint a mirror with three Vitae and contest Resolve + Composure + Auspex vs Power + Resistance to either trap your Ka or let it out with you in Twilight.",
        merit_type="vampire",
        prerequisite="elder,hollow_mekhet",
        book="TY 85"
    ),
    Merit(
        name="Undeniable Aura",
        min_value=3,
        max_value=3,
        description="Your very presence contests your Predatory Aura vs Resolve + Tolerance to reduce your exceptional Social threshold against the subject from five to three.",
        merit_type="vampire",
        prerequisite="elder,[atrocious:1,cutthroat:1,enticing:1]",
        book="TY 85"
    ),
    #Revenant Merits
    Merit(
        name="Blood Farm",
        min_value=1,
        max_value=5,
        description="Replaces Herd. You raise animals you may drain for thrice your Blood Farm dots in Vitae weekly, but large Blood Farms may attract attention.",
        merit_type="vampire",
        prerequisite="resources:1",
        book="HD 80"
    ),
    Merit(
        name="Chains for Hungry Fenrir",
        min_value=2,
        max_value=2,
        description="Half your hunger penalties to resist frenzy.",
        merit_type="vampire",
        prerequisite="revenant,resolve:3",
        book="HD 80"
    ),
    Merit(
        name="Clan Impostor",
        min_value=1,
        max_value=1,
        description="May replace Alternate Identity. You can masquerade as full Kindred of a given clan.",
        merit_type="vampire",
        prerequisite="manipulation:3,subterfuge:2",
        book="HD 80"
    ),
    Merit(
        name="Fertile Vitae",
        min_value=3,
        max_value=3,
        description="You may Embrace revenant childer.",
        merit_type="vampire",
        prerequisite="revenant",
        book="HD 81"
    ),
    Merit(
        name="Kindred Status",
        min_value=1,
        max_value=5,
        description="As for full Kindred. Clan Status requires Clan Impostor.",
        merit_type="vampire",
        prerequisite="",
        book="HD 80, VtR2e 113"
    ),
    Merit(
        name="Revenant Status",
        min_value=1,
        max_value=5,
        description="As the general Status Merit, and provides Chary tutelage.",
        merit_type="vampire",
        prerequisite="",
        book="HD 81"
    ),
    Merit(
        name="Sanctioned Tracker",
        min_value=2,
        max_value=2,
        description="Replaces City Status ••. You maintain respect while on a mission to destroy a criminal for the local Kindred.",
        merit_type="",
        prerequisite="revenant",
        book="HD 81"
    ),
    Merit(
        name="Sire Sense",
        min_value=1,
        max_value=1,
        description="Sense your sire's location. +2 to navigate and employ Blood Sympathy to pursue her.",
        merit_type="vampire",
        prerequisite="revenant",
        book="HD 81"
    ),
    Merit(
        name="Twilight Walker",
        min_value=1,
        max_value=3,
        description="For fifteen minutes at dawn's start and dusk's end, take bashing damage from sunlight. With three dots, take no sunlight damage during that period, and bashing damage for fifteen minutes more.",
        merit_type="vampire",
        prerequisite="revenant,humanity>=7",
        book="HD 81"
    ),
    #Carthian Merits
    Merit(
        name="Alley Cat",
        min_value=1,
        max_value=3,
        description="Reduces the threshold for exceptional success when rolling to prowl city streets.",
        merit_type="vampire",
        prerequisite="athletics:2,stealth:2,streetwise:2",
        book="SotC 177"
    ),
    Merit(
        name="Army of One",
        min_value=1,
        max_value=5,
        description="Roll Presence + Politics + Covenant Status to summon Carthian backup, up to one per dot in this Merit each story.",
        merit_type="vampire",
        prerequisite="carthian_status>=army_of_one",
        book="SotC 177"
    ),
    Merit(
        name="Carthian Pull",
        min_value=1,
        max_value=1,
        description="Every month, you can leverage favors to access your Carthian Status in dots of Allies, Contacts, Haven or Herd.",
        merit_type="vampire",
        prerequisite="",
        book="VtR2e 110"
    ),
    Merit(
        name="Court Jester",
        min_value=2,
        max_value=2,
        description="Reputation as a pundit punishes attempts at official censure by stripping a dot of City Status from the official.",
        merit_type="vampire",
        prerequisite="politics:2,city_status:2",
        book="SotC 178"
    ),
    Merit(
        name="Devotion Experimenter",
        min_value=2,
        max_value=2,
        description="Reroll nines when using Devotions, and learn or teach them at an experience discount.",
        merit_type="vampire",
        prerequisite="science:2,carthian_status:2",
        book="SotC 178"
    ),
    Merit(
        name="Fucking Thief",
        min_value=1,
        max_value=1,
        description="Steal flawed knowledge of a single one-dot advantage restricted to another covenant.",
        merit_type="vampire",
        prerequisite="subterfuge:3",
        book="SotC 178"
    ),
    Merit(
        name="I Know A Guy",
        min_value=1,
        max_value=1,
        description="Once per story, your non-temporary dots of Allies can do double duty as dots of Retainer.",
        merit_type="vampire",
        prerequisite="",
        book="VtR2e 115"
    ),
    Merit(
        name="Jack-Booted Thug",
        min_value=2,
        max_value=2,
        description="Spend Willpower and roll Presence + Intimidation + City Status to shut people down through projected menace.",
        merit_type="vampire",
        prerequisite="intimidation:3,carthian_status:2,city_status:1",
        book="SotC 178"
    ),
    Merit(
        name="Night Doctor Surgery",
        min_value=3,
        max_value=3,
        description="Roll Intelligence + Medicine to treat a vampire medically for an hour, reducing lethal damage to bashing.",
        merit_type="vampire",
        prerequisite="carthian_status:2",
        book="VtR2e 113"
    ),
    Merit(
        name="Sell Out",
        min_value=3,
        max_value=3,
        description="Legalistic title manipulation grants you the full benefits of one dot of Status in each of the city's covenants. Decide arbitrarily at any given time whether Carthian Law counts you as a Carthian.",
        merit_type="vampire",
        prerequisite="politics:3,carthian_status:4,city_status:4",
        book="SotC 179"
    ),
    Merit(
        name="Smooth Criminal",
        min_value=2,
        max_value=2,
        description="Once per story, roll Manipulation + Subterfuge to end discussion of allegations against you or a fellow Carthian.",
        merit_type="vampire",
        prerequisite="politics:1,streetwise:2,subterfuge:2",
        book="SotC 179"
    ),
    Merit(
        name="Toss That Shit Right Back",
        min_value=1,
        max_value=1,
        description="When you dodge a thrown attack, you can catch the object and immediately throw it back.",
        merit_type="vampire",
        prerequisite="dexterity:3,athletics:2",
        book="SotC 179"
    ),
    #Carthian Law Merits
    Merit(
        name="Breaking the Chains",
        min_value=1,
        max_value=1,
        description="Break one Vinculum by accepting a single-step blood bond to a number of fellow Carthians. Actions to betray the old Vinculum act as a supplementary Dirge.",
        merit_type="vampire",
        prerequisite="",
        book="SotC 179"
    ),
    Merit(
        name="Cease Fire",
        min_value=5,
        max_value=5,
        description="Temporarily disrupt the powers of the Blood through a majority vote of local Carthians. Throughout the domain, Disciplines and Devotions cost Willpower to function and risk aggravated damage when in use. The Carthian invoking this law may specify a condition for ending the Cease Fire. It also ends if she herself uses a power of the Blood, leaves the domain or is destroyed.",
        merit_type="vampire",
        prerequisite="carthian_status:5",
        book="SotC 180"
    ),
    Merit(
        name="Coda Against Sorcery",
        min_value=1,
        max_value=5,
        description="Declare a personal censure of sorcery in general, a particular blood sorcery, or a particular sorcerous ritual. Apply this Merit as resistance against the censured sorcery.",
        merit_type="vampire",
        prerequisite="",
        book="SotC 180"
    ),
    Merit(
        name="Empower Judiciary",
        min_value=3,
        max_value=3,
        description="Invest dots of Willpower and of Blood Potency to empower a legal arbiter for the domain. The arbiter may make binding public interpretations of the domain's law, on pain of stripping of Kindred Status or of aggravated damage in its absence, and retains this authority until destroyed or until domain rulership changes hands.",
        merit_type="vampire",
        prerequisite="carthian_status:3",
        book="SotC 180"
    ),
    Merit(
        name="Establish Precedent",
        min_value=2,
        max_value=2,
        description="Invest a dot of Willpower to extend the enforcement of an edict from an individual case to the whole domain for a year and a day. Intentional violation of the edict is punished by a specified marking brand and accompanying bane for a month.",
        merit_type="vampire",
        prerequisite="vampire",
        book="SotC 180"
    ),
    Merit(
        name="Lex Terrae",
        min_value=2,
        max_value=2,
        description="So long as your Feeding Ground has been clearly declared, vampires who feed there without your permission wake the next night and vomit the Vitae out as useless, and are visibly marked for a week.",
        merit_type="vampire",
        prerequisite="carthian_status:2,feeding_grounds:1",
        book="VtR2e 116"
    ),
    Merit(
        name="Mandate from the Masses",
        min_value=5,
        max_value=5,
        description="When you preside over a majority vote of local Carthians to condemn an enemy of the people, you can voluntarily lose access to a dot of Willpower to strip the enemy of Blood Potency proportional to the Carthian vote. Lost dots return when the enemy goes into exile or either you or the enemy are destroyed.",
        merit_type="vampire",
        prerequisite="carthian_status:5",
        book="VtR2e 116"
    ),
    Merit(
        name="Plausible Deniability",
        min_value=4,
        max_value=4,
        description="Supernatural means can't prove your guilt of crimes against domain or Tradition, diablerie doesn't stain your aura, and you penalize nonmagical efforts to perceive your guilt by your Carthian Status. You can't use your Kindred Status against anyone who ascertains your guilt anyway.",
        merit_type="vampire",
        prerequisite="carthian_status:3",
        book="VtR2e 116"
    ),
    Merit(
        name="Right of Return",
        min_value=2,
        max_value=2,
        description="You're authorized to participate in multiple covenants. Your total maximum of Covenant Status dots ignores your dots of Carthian Status, and you improve your Social Maneuvering impression with your other affiliated covenants, but lose 10-Again to conceal suspicious behavior from them.",
        merit_type="vampire",
        prerequisite="carthian_status:2,city_status:1",
        book="VtR2e 116"
    ),
    Merit(
        name="Stare Decisis",
        min_value=2,
        max_value=2,
        description="When you speak on matters of breach of law or Tradition, others must spend Willpower to oppose you. Recover Willpower when you sway the authority to rule in your favor.",
        merit_type="vampire",
        prerequisite="elder,carthian_status:3",
        book="TY 85"
    ),
    Merit(
        name="Strength of Resolution",
        min_value=1,
        max_value=1,
        description="When a supernatural power is used to compel you to violate the law of the domain, add your Carthian Status dots as dice to contest it.",
        merit_type="vampire",
        prerequisite="",
        book="VtR2e 116"
    ),
    Merit(
        name="Weaponize Dissent",
        min_value=2,
        max_value=2,
        description="Irreversibly invokes insurgency for a year and a day, even after the invoking Carthian is destroyed. During insurgency, characters attacking vampires in the presence of the Carthian or his bodily remains apply their target's City Status as an additional weapon bonus, even if it is from a foreign domain.",
        merit_type="vampire",
        prerequisite="carthian_status:2",
        book="SotC 181"
    ),
    #Circle of the Crone Merits
    Merit(
        name="Altar",
        min_value=1,
        max_value=1,
        description="Requires at least 3 characters with the Merit. You've contributed to attuning a blood altar. In the presence of the altar, contributors can apply teamwork to Crúac rituals, even if they don't know Crúac, at the cost of slowing the ritual.",
        merit_type="vampire",
        prerequisite="",
        book="VtR2e 109"
    ),
    Merit(
        name="The Mother-Daughter Bond",
        min_value=1,
        max_value=1,
        description="Apply the benefits of the True Friend Merit to any Acolyte Mentor.",
        merit_type="vampire",
        prerequisite="",
        book="VtR2e 113"
    ),
    Merit(
        name="Mother-Goddess Altar",
        min_value=1,
        max_value=1,
        description="Lead Cruac rituals at an altar at full speed.",
        merit_type="vampire",
        prerequisite="elder,altar:1,crone_status:5",
        book="TY 84"
    ),
    Merit(
        name="Viral Mythology",
        min_value=3,
        max_value=3,
        description="When you make a show of divine glory, roll Presence + Expression, contested by Wits + Composure, to inflict a contagious Condition of awe and splendor. Allies and Herd Merits spread to double their yield.",
        merit_type="vampire",
        prerequisite="presence:3,expression:3,cruac:1",
        book="SotC 182"
    ),
    Merit(
        name="What You've Done For Her Lately",
        min_value=1,
        max_value=1,
        description="Once a story, you can use the casting of a Crúac rite to boost your effective Covenant Status for the scene.",
        merit_type="vampire",
        prerequisite="cruac:2",
        book="SotC 182"
    ),
    #Cruac Style Merits
    Merit(
        name="Opening The Void",
        min_value=1,
        max_value=5,
        description="Your Crúac rites call forth bestial shadow-servants of Size, Retainer value, and longevity proportional to the rite. By spending Willpower when casting, you can attempt to consign a living being to the outer darkness, prompting an extended roll with a Willpower cost for the resisting subject.",
        merit_type="vampire",
        prerequisite="cruac:1",
        book="SotC 184"
    ),
    Merit(
        name="Primal Creation",
        min_value=1,
        max_value=5,
        description="Your rites cause plant overgrowth proportional to the rite, and evoke fertility. By spending Willpower when casting, you can cause life proportional to the rite to mutate and bud off duplicates.",
        merit_type="vampire",
        prerequisite="cruac:1",
        book="SotC 183"
    ),
    Merit(
        name="Unbridled Chaos",
        min_value=1,
        max_value=5,
        description="Your rites provoke unpredictable swelling, mutation and deformation of the environment, proportional to the rite. By spending Willpower when casting, you can cause inclement weather, whose Tilt effects you may ignore.",
        merit_type="vampire",
        prerequisite="cruac:1",
        book="SotC 183"
    ),
    #Invictus Merits
    Merit(
        name="Attache",
        min_value=1,
        max_value=1,
        description="Your Retainers each gain access to your Invictus Status in dots distributed among Contacts, Resources and Safe Place.",
        merit_type="vampire",
        prerequisite="",
        book="VtR2e 110"
    ),
    Merit(
        name="Crowdsourcing",
        min_value=1,
        max_value=3,
        description="Spend Willpower and roll Manipulation + Academics to coordinate the temporary exchange of Social Merit dots from one Invictus member to another, which may then temporarily exceed their normal maximum by your dots in this Merit.",
        merit_type="vampire",
        prerequisite="contacts:1,resources:3",
        book="SotC 187"
    ),
    Merit(
        name="Friends in High Places",
        min_value=1,
        max_value=1,
        description="Every month, you can open up to your Invictus Status in Doors belonging to people held under the local Invictus thumb.",
        merit_type="vampire",
        prerequisite="",
        book="VtR2e 112"
    ),
    Merit(
        name="Information Network",
        min_value=1,
        max_value=1,
        description="Use your Contacts as Skill Specialties.",
        merit_type="vampire",
        prerequisite="invictus_status:2,contacts:1",
        book="SotC 187"
    ),
    Merit(
        name="Invested",
        min_value=1,
        max_value=1,
        description="Distribute your dots in Invictus Status among free dots of Herd, Mentor, Resources and Retainer, provided by the covenant.",
        merit_type="vampire",
        prerequisite="",
        book="VtR2e 112"
    ),
    Merit(
        name="Moderator",
        min_value=1,
        max_value=5,
        description="Administrator access to Invictus networks can be used dot-for-dot as temporary Allies, Contacts, or Library, once per story.",
        merit_type="vampire",
        prerequisite="computer:3,invictus_status:2,contacts:1",
        book="SotC 187"
    ),
    Merit(
        name="Noblesse Oblige",
        min_value=3,
        max_value=3,
        description="Use your station in the domain as a Touchstone.",
        merit_type="vampire",
        prerequisite="city_status:3",
        book="SotC 188"
    ),
    Merit(
        name="Notary",
        min_value=3,
        max_value=3,
        description="You're empowered by the Invictus to preside over Invictus Oaths. Invictus Status can't be used in Social rolls against you, and once a month, you can call upon one dot of Allies, Contacts, Herd, Mentor or Resources from the covenant.",
        merit_type="vampire",
        prerequisite="invictus_status:3",
        book="VtR2e 116"
    ),
    Merit(
        name="Prestigious Sire",
        min_value=1,
        max_value=1,
        description="Draw on your bond with your sire to use your sire's vampiric Status dots instead of your own in a Social action, risking this Merit's loss on failure.",
        merit_type="vampire",
        prerequisite="mentor:4",
        book="SotC 188"
    ),
    Merit(
        name="Social Engineering",
        min_value=4,
        max_value=4,
        description="Spend Willpower and roll Manipulation + Investigation to dig up dirt, weaknesses, advantages or openings against a victim.",
        merit_type="vampire",
        prerequisite="manipulation:3,wits:3,investigation:2,subterfuge:2",
        book="SotC 188"
    ),
    Merit(
        name="Speaker for the Silent",
        min_value=3,
        max_value=3,
        description="You've learned to voluntarily channel the will of a torpid elder. You can cut off an open channel with a point of Willpower.",
        merit_type="vampire",
        prerequisite="dynasty_membership:1",
        book="VtR2e 114"
    ),
    Merit(
        name="Tech-Savvy",
        min_value=1,
        max_value=3,
        description="Retrieve access to devices up to Availability two higher than dots in this Merit, which grant 9-Again and distribute your Tech-Savvy dots among equipment bonus, Structure, and Durability.",
        merit_type="vampire",
        prerequisite="computer:2,crafts:2,science:1,resources:1",
        book="SotC 188"
    ),
    Merit(
        name="Travel Agent",
        min_value=1,
        max_value=5,
        description="When you travel to another domain, name a receiving host, apply half your dots in this Merit as temporary Allies or Contacts in the new domain, and reduce attempts to intercept you between domains by successes equal to this Merit.",
        merit_type="vampire",
        prerequisite="invictus_status:2,contacts:1",
        book="SotC 188"
    ),
    Merit(
        name="Where the Bodies Are Buried",
        min_value=2,
        max_value=2,
        description="Once per story for every dot in this Merit, your notes on dirty work can turn up dirt on a vampire whose associations you know.",
        merit_type="vampire",
        prerequisite="invictus_status:2",
        book="VtR2e 115"
    ),
    #Invictus Oaths
    Merit(
        name="Oath of Abstinence",
        min_value=5,
        max_value=5,
        description="So long as you imbibe no Vitae, you need spend none to wake nightly.",
        merit_type="vampire",
        prerequisite="invictus_status:1",
        book="SotC 189"
    ),
    Merit(
        name="Oath of Action",
        min_value=4,
        max_value=4,
        description="Swear a labor for your liege. For the duration of the Oath, you may access one of your liege's Disciplines (including bloodline gifts), while your liege's Blood Potency increases by one. The Oath concludes when the labor is complete or a month passes, and respectively the liege or the vassal suffers aggravated damage equal to the Discipline dots offered. You can only be party to one Oath of Action at a time.",
        merit_type="vampire",
        prerequisite="",
        book="VtR2e 117"
    ),
    Merit(
        name="Oath of Dynasty",
        min_value=3,
        max_value=3,
        description="You share a closer link to fellow sworn dynasts. You may borrow their Social Merits once a session, communicate with torpid dynasts by rolling Presence + Empathy, or rouse them by rolling an exceptional success with your Blood Potency. These rolls suffer a -5 penalty, reduced by one for each dot after the fifth of your Blood Potency (to communicate) or their Humanity (to rouse).",
        merit_type="vampire",
        prerequisite="covenant_status:3,dynasty_membership:3",
        book="TY 85"
    ),
    Merit(
        name="Oath of Fealty",
        min_value=1,
        max_value=1,
        description="You can draw up to your Invictus Status in Vitae from your liege each week, without feeding from her. Your liege can tell when you lie to her. You can only swear an Oath of Fealty to one liege at a time.",
        merit_type="vampire",
        prerequisite="invictus_status:1",
        book="VtR2e 117"
    ),
    Merit(
        name="Oath of the Handshake Deal",
        min_value=1,
        max_value=1,
        description="One party must be Invictus. Both parties purchase this Merit, swear a service or forbearance, and offer a Social Merit as collateral. Violating the oath awards the other party your collateral for an agreed duration.",
        merit_type="vampire",
        prerequisite="",
        book="SotC 189"
    ),
    Merit(
        name="Oath of the Hard Motherfucker",
        min_value=2,
        max_value=2,
        description="The vassal must kill a Carthian or oathbreaker in exchange for her first dot of Invictus Status, 9-Again on two Skills, and a dot each of Allies, Contacts, and Resources, all stripped if the oath is broken.",
        merit_type="vampire",
        prerequisite="invictus_status:0",
        book="SotC 189"
    ),
    Merit(
        name="Oath of Matrimony",
        min_value=5,
        max_value=5,
        description="One party must be Invictus. Both parties purchase this Merit, swear vows, assume blood sympathy, and become subject to a full mutual Vinculum. Their Social Merits, Blood Potency, and Discipline ratings increase to catch up to the spouse's. Broken vows strip Blood Potency.",
        merit_type="vampire",
        prerequisite="",
        book="SotC 190"
    ),
    Merit(
        name="Oath of the Model Prisoner",
        min_value=3,
        max_value=3,
        description="A prisoner of the Invictus swears as vassal not to attempt escape or sabotage, on pain of occult branding, in exchange for protection from torture and execution.",
        merit_type="vampire",
        prerequisite="",
        book="SotC 190"
    ),
    Merit(
        name="Oath of Office",
        min_value=3,
        max_value=3,
        description="The vassal swears to the duties of an office in vampire society, and may treat it as a supplemental Mask trait, but faces detachment for violation.",
        merit_type="vampire",
        prerequisite="[city_status:3,covenant_status:3]",
        book="SotC 191"
    ),
    Merit(
        name="Oath of Penance",
        min_value=3,
        max_value=3,
        description="For the duration of the Oath, every tenth point of Vitae you ingest is mystically transmitted to your liege as Kindred Vitae, and you are denied the benefits of any other Invictus Oath. Your liege cannot use Disciplines against you.",
        merit_type="vampire",
        prerequisite="",
        book="VtR2e 117"
    ),
    Merit(
        name="Oath of the Refugee",
        min_value=2,
        max_value=2,
        description="The signatory accepts exile from a domain and gains protection from pursuit by agents of the domain.",
        merit_type="vampire",
        prerequisite="covenant_status:1",
        book="SotC 191"
    ),
    Merit(
        name="Oath of the Righteous Kill",
        min_value=3,
        max_value=3,
        description="The signatory can act as a confessor, assuming premeditated risks of detachment from fellow covenant members.",
        merit_type="vampire",
        prerequisite="empathy:3,invictus_status:3",
        book="SotC 191"
    ),
    Merit(
        name="Oath of the Safe Word",
        min_value=2,
        max_value=2,
        description="Both parties purchase this Merit and share the use of Willpower and one Social Merit with the other party. Either party may end the oath to briefly paralyze the other party.",
        merit_type="vampire",
        prerequisite="covenant_status:1",
        book="SotC 191"
    ),
    Merit(
        name="Oath of Serfdom",
        min_value=2,
        max_value=2,
        description="Receive a feudal territory from your liege. While there, or when defending your liege, you gain a free dot of Celerity, Resilience or Vigor. You intuit when another predatory aura crosses into your land and from where. Your liege adds your dots in Feeding Ground as bonus dice against you, and ignores any blood bond you may impose.",
        merit_type="vampire",
        prerequisite="",
        book="VtR2e 117"
    ),
    Merit(
        name="Oath of the True Knight",
        min_value=4,
        max_value=4,
        description="The vassal swears a role of impartial defender of the covenant. She becomes unable to drink Kindred Vitae, and her Invictus Status protects her from mental Disciplines and attacks from Kindred and ghouls.",
        merit_type="vampire",
        prerequisite="invictus_status:2",
        book="SotC 191"
    ),
    #Lancea Et Sanctum Merits
    Merit(
        name="Anointed",
        min_value=2,
        max_value=2,
        description="You're ordained. Once per session, you can roll Presence + Expression to preach the Raptured Condition.",
        merit_type="vampire",
        prerequisite="",
        book="VtR2e 109"
    ),
    Merit(
        name="Faith Militant",
        min_value=2,
        max_value=2,
        description="You may draw on your Herd for Resources.",
        merit_type="vampire",
        prerequisite="",
        book="DE2 109"
    ),
    Merit(
        name="Flock",
        min_value=1,
        max_value=5,
        description="You inspire your Herd. They serve as a source of Willpower. Dots in this Merit apply as additional Herd dots.",
        merit_type="vampire",
        prerequisite="herd>=flock",
        book="SotC 193"
    ),
    Merit(
        name="Lorekeeper",
        min_value=1,
        max_value=1,
        description="Your lorehouse attracts occultists. Distribute your dots in the Library Merit among bonus dots in Retainer and Herd.",
        merit_type="vampire",
        prerequisite="",
        book="VtR2e 113"
    ),
    Merit(
        name="Sanctuary",
        min_value=1,
        max_value=5,
        description="You have authority to shelter one Kindred criminal per dot in this Merit in your Safe Place, who act as Retainers so long as you feed them.",
        merit_type="vampire",
        prerequisite="lancea_status:2,city_status:2,safe_place:1",
        book="SotC 193"
    ),
    Merit(
        name="Sorcerous Eunuch",
        min_value=1,
        max_value=1,
        description="You've had the essence of sorcery scoured from you over an arduous month. Penalize sorcerous effects with your Resolve. You can't learn blood sorcery.",
        merit_type="vampire",
        prerequisite="resolve:3",
        book="SotC 193"
    ),
    Merit(
        name="Stigmata",
        min_value=1,
        max_value=5,
        description="Each week, or at will by spending Willpower, you bleed Vitae equal to your dots in this Merit, which when ingested inspires spiritually and does not cause addiction or bonding. The experience bolsters Theban Sorcery and Willpower.",
        merit_type="vampire",
        prerequisite="stigmata<humanity+3",
        book="SotC 193"
    ),
    #Ordo Dracul Merits
    Merit(
        name="Secret Society Junkie",
        min_value=1,
        max_value=1,
        description="Dots in Status or Mystery Cult Initiation representing human secret societies also count as dots of Herd.",
        merit_type="vampire",
        prerequisite="",
        book="VtR2e 114"
    ),
    Merit(
        name="Sworn",
        min_value=1,
        max_value=1,
        description="Swear yourself to frequent duties either to the silencers of the Axe, learned of the Dying Light, or leaders of the Mysteries. Distribute your dots in Ordo Status among bonus dots of Mentor and Retainer.",
        merit_type="vampire",
        prerequisite="",
        book="VtR2e 114"
    ),
    Merit(
        name="Twilight Judge",
        min_value=3,
        max_value=3,
        description="You're empowered to make binding judgments for the covenant within a domain. Treat the special treatment of your office as equivalent to a five-dot Mentor.",
        merit_type="vampire",
        prerequisite="ordo_status:4",
        book="SotC 198"
    ),
    #Other Covenant Merits
    Merit(
        name="Shahrayad's Tale",
        min_value=1,
        max_value=5,
        description="Once per chapter, spin tales to threaten listeners up to your Merit rating with both vitae and story addiction. Each tale improves your impression on an addicted listener.",
        merit_type="vampire",
        prerequisite="al-amin",
        book="DE2 142"
    ),
    Merit(
        name="Parliament's Apostle",
        min_value=1,
        max_value=1,
        description="Your circle worships a strix who will serve as a Mentor in exchange for tithes of blood.",
        merit_type="vampire",
        prerequisite="circle_of_mor,humanity<6",
        book="DE2 110"
    ),
    Merit(
        name="Ifrit's Might",
        min_value=3,
        max_value=3,
        description="Master one Crúac rite for each dot of Blood Potency after the fifth. Mastered rites reduce their exceptional success threshold from five to three.",
        merit_type="vampire",
        prerequisite="fir'awn,blood_potency:6",
        book="DE2 142"
    ),
    Merit(
        name="Envoy",
        min_value=1,
        max_value=5,
        description="Rolls to intercept you between cities must exceed your Envoy rating in successes. When you arrive in a domain, specify your receiving party and a gift or rumor that serves as expendable Social equipment concerning them. Once per story, apply half your Envoy dots as effective Allies or Contacts.",
        merit_type="vampire",
        prerequisite="gallows_post",
        book="DE 266"
    ),
    Merit(
        name="Contracts of Night and Day",
        min_value=1,
        max_value=1,
        description="You may preside over an Invictus Oath with a changeling vassal, who must drink from his liege. Blood sympathy forms, and the changeling can target his liege with Contracts as a universal loophole.",
        merit_type="vampire",
        prerequisite="legion_of_the_green,occult:2,notary:1",
        book="DE2 109"
    ),
    Merit(
        name="Contract with the Uncanny",
        min_value=1,
        max_value=5,
        description="Choose a supernatural faction or force; you may purchase this Merit multiple times for multiple contracts. You can call upon ancient bargains to request favors proportional in risk or effort to your dots in this Merit, in exchange for offering an equivalent favor. You can call on greater favors than your dots would allow by owing disproportionate labors in return.",
        merit_type="vampire",
        prerequisite="weihan_cynn",
        book="DE 271"
    ),
    #Lingua Bellum Merits
    Merit(
        name="Beating The Drum",
        min_value=3,
        max_value=3,
        description="Once per chapter, before starting a social encounter, you can gain the Danse Macabre or The Edge condition. Roll for frenzy at the end of the social encounter when used.",
        merit_type="vampire",
        prerequisite="",
        book="GTTN 126"
    ),
    Merit(
        name="Blood Station",
        min_value=1,
        max_value=3,
        description="The quality of a vampires mortal blood affects them among the All Night Society. Add dots in this merit to Ego rolls.",
        merit_type="vampire",
        prerequisite="crown_games",
        book="GTTN 123"
    ),
    Merit(
        name="Dragon's Fire",
        min_value=1,
        max_value=5,
        description="Gain a number of maneuvers equal to dots in this merit: Browbeat, Channel the Beast, Consumed by Horror, Give Chase, Inexplicable Dread.",
        merit_type="vampire",
        prerequisite="ordo_status:1",
        book="GTTN 132"
    ),
    Merit(
        name="Flawless Timing",
        min_value=2,
        max_value=2,
        description="Once per chapter, set your timing to one above the highest.",
        merit_type="vampire",
        prerequisite="",
        book="GTTN 127"
    ),
    Merit(
        name="Hecate's Tongue",
        min_value=1,
        max_value=5,
        description="Gain a number of maneuvers equal to dots in this merit: Apply Pressure, Cheap Shot, Dramatic Revelation, Keep 'Em Guessing, Switch it Up.",
        merit_type="vampire",
        prerequisite="crone_status:1",
        book="GTTN 129"
    ),
    Merit(
        name="Howling Support",
        min_value=2,
        max_value=2,
        description="If a member of your coterie is engaged in Lingua Bellum, you may choose to count as a small indifferent audience alone.",
        merit_type="vampire",
        prerequisite="",
        book="GTTN 128"
    ),
    Merit(
        name="Money Talks",
        min_value=1,
        max_value=1,
        description="Leverage your economic might. Once per scene, add dots in Wealth Immeasurable to any maneuver roll.",
        merit_type="vampire",
        prerequisite="wealth_immeasurable:1",
        book="GTTN 125"
    ),
    Merit(
        name="Sound and Fury",
        min_value=1,
        max_value=5,
        description="Gain a number of maneuvers equal to dots in this merit: Alternative Facts, Breakdown, Gish Gallup, Know Your Audience, Loudest Wins.",
        merit_type="vampire",
        prerequisite="carthian_status:1",
        book="GTTN 128"
    ),
    Merit(
        name="The Superior Beast",
        min_value=1,
        max_value=1,
        description="Add your Blood Potency to a maneuver once per scene. Roll for frenzy at the end of the social encounter when used.",
        merit_type="vampire",
        prerequisite="",
        book="GTTN 123"
    ),
    Merit(
        name="Verbum Dei",
        min_value=1,
        max_value=5,
        description="Gain a number of maneuvers equal to dots in this merit: For Your Own Good, Glad You Thought of It, Guilt Trip, Inspiring Speech, Leading Questions.",
        merit_type="vampire",
        prerequisite="lancea_status:1",
        book="GTTN 131"
    ),
    Merit(
        name="Verbum Imperii",
        min_value=1,
        max_value=5,
        description="Gain a number of maneuvers equal to dots in this merit: Acknowledge the Master, Demand Respect, Form Over Function, Impeccable Logic, Veiled Threat.",
        merit_type="vampire",
        prerequisite="invictus_status:1",
        book="GTTN 130"
    ),
    Merit(
        name="Work The Crowd",
        min_value=2,
        max_value=2,
        description="Once per exchange, roll Presence + Socialize, using the successes to increase the intensity of the audience.",
        merit_type="vampire",
        prerequisite="presence:2",
        book="GTTN 127"
    ),
]

# Create dictionary for easy lookup
vampire_merits_dict = {merit.name.lower().replace(" ", "_").replace("(", "").replace(")", ""): merit for merit in vampire_merits}
