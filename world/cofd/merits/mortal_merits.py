from world.cofd.stat_types import Merit

# Mortal-Specific Merits
mortal_merits = [
    #Supernatural Merits
    Merit(
        name="Accursed Harbinger",
        min_value=3,
        max_value=3,
        description="When an undirected curse settles upon you, roll Resolve + Composure to serve as a carrier for the curse rather than suffering it yourself.",
        merit_type="mortal",
        prerequisite="",
        book="MtC2e 117"
    ),
    Merit(
        name="Animal Possession",
        min_value=2,
        max_value=4,
        description="Spend Willpower and roll Resolve + Animal Ken to enter a projecting trance and control a Bonded animal for a scene. With four dots, control any animal.",
        merit_type="mortal",
        prerequisite="animal_ken:3",
        book="HL 72"
    ),
    Merit(
        name="Animal Speech",
        min_value=1,
        max_value=2,
        description="You can fluently understand the communication of a particular kind of animal. With two dots, they can understand your communication. +3 to relevant Animal Ken rolls.",
        merit_type="mortal",
        prerequisite="",
        book="DE 247"
    ),
    Merit(
        name="Apporation",
        min_value=3,
        max_value=5,
        description="Spend Willpower and roll Resolve + Occult to teleport an object or being up to Size 2, or with five dots, Size 5, inflicting Structure or bashing damage from the strain.",
        merit_type="mortal",
        prerequisite="",
        book="HL 72"
    ),
    Merit(
        name="Assertive Implement",
        min_value=1,
        max_value=4,
        description="You possess a living weapon with its own will. Apply your dots in Assertive Implement as a bonus or penalty to wield it, as befits its whims. It regenerates Structure damage and can attack on its own given the opportunity.",
        merit_type="mortal",
        prerequisite="manipulation:3,occult:3,[weaponry:2,firearms:2]",
        book="HL 72"
    ),
    Merit(
        name="Astral Adept",
        min_value=3,
        max_value=3,
        description="You can spend Willpower and use a given ceremony or implement to project yourself into the Astral Realms.",
        merit_type="mortal",
        prerequisite="",
        book="MtA2e 100"
    ),
    Merit(
        name="Aura Reading",
        min_value=3,
        max_value=3,
        description="Spend Willpower and roll Wits + Empathy - Composure to stare into a subject's aura, asking the player a question per success about their mood, intent or nature. Once a session, the Storyteller can have a supernatural creature roll Wits + Occult - Composure to feel your character's uncanny awareness.",
        merit_type="mortal",
        prerequisite="",
        book="CofD 56"
    ),
    Merit(
        name="Automatic Writing",
        min_value=2,
        max_value=2,
        description="Spend Willpower and roll Wits + Composure to enter a meditative trance, channeling a clue per success. Failure or the lack of a proper channeling charm evokes a grievous week-long haunting.",
        merit_type="mortal",
        prerequisite="",
        book="CofD 56"
    ),
    Merit(
        name="Biokinesis",
        min_value=1,
        max_value=5,
        description="Heal twice as fast. Spend Willpower and concentrate to exchange an Attribute dot per Biokinesis dot between Physical Attributes, for one hour.",
        merit_type="mortal",
        prerequisite="",
        book="CofD 57"
    ),
    Merit(
        name="Biomimicry",
        min_value=1,
        max_value=4,
        description="Spend Willpower and suffer lethal damage to mutate natural weaponry, propulsive venom, heavy 2/1 Armor, or camouflage pigmentation for a scene.",
        merit_type="mortal",
        prerequisite="biokinesis:1",
        book="HL 72"
    ),
    Merit(
        name="Bless Amulet",
        min_value=1,
        max_value=3,
        description="Spend Willpower and roll Resolve + Composure with abjuration modifiers to ritually imbue a charm with protection against ephemeral possession and Claiming, for a duration determined by Merit rating.",
        merit_type="mortal",
        prerequisite="occult:3",
        book="HL 72"
    ),
    Merit(
        name="Camera Obscura",
        min_value=3,
        max_value=3,
        description="Spend Willpower to focus a camera and perceive entities felt through the Unseen Sense, Opening their influence for a scene. While focused, roll Wits + Expression - Defense to inflict photographic bashing damage.",
        merit_type="mortal",
        prerequisite="[unseen_sense_ghosts:1,unseen_sense_spirits:1]",
        book="HL 73"
    ),
    Merit(
        name="Citywalker",
        min_value=3,
        max_value=3,
        description="You can roll Resolve + Streetwise to walk occult correspondences from city to city, with penalties proportional to how unfamiliar your destination is to you.",
        merit_type="mortal",
        prerequisite="streetwise:2",
        book="CofD 236"
    ),
    Merit(
        name="Clairvoyance",
        min_value=3,
        max_value=3,
        description="Spend Willpower and roll Wits + Occult to scry through a particular occult medium.",
        merit_type="mortal",
        prerequisite="",
        book="CofD 57"
    ),
    Merit(
        name="Consecrate Weapon",
        min_value=4,
        max_value=4,
        description="Spend Willpower and roll Resolve + Composure - weapon rating with abjuration modifiers to ritually bless a weapon. It deals lethal damage to ephemeral entities, even in Twilight, for one turn per success.",
        merit_type="mortal",
        prerequisite="resolve:3, occult:4",
        book="HL 73"
    ),
    Merit(
        name="Cursed",
        min_value=2,
        max_value=2,
        description="You're doomed. Decide how doomed you are. Take +2 to Resolve + Composure rolls to resist fear or doubt that doesn't arise from your doom, and take an extra beat when you suffer lethal wound penalties.",
        merit_type="mortal",
        prerequisite="",
        book="CofD 57"
    ),
    Merit(
        name="Curse Effigy",
        min_value=3,
        max_value=3,
        description="Spend Willpower and roll Wits + Occult - Resolve to spend a night crafting a sympathetic effigy of a victim. Spend rolled successes to inflict harmful Personal Tilts, distract and harry the victim, or make lethal attacks with Intelligence + Medicine - Stamina + Tolerance.",
        merit_type="mortal",
        prerequisite="",
        book="HL 73"
    ),
    Merit(
        name="Dark Passenger",
        min_value=2,
        max_value=2,
        description="You have a sinister second mouth on the back of your head. It whispers secrets in threes, one of which is a lie, warns you of ambushes, and insists on being fed hourly.",
        merit_type="mortal",
        prerequisite="",
        book="HL 73"
    ),
    Merit(
        name="Doppelganger",
        min_value=3,
        max_value=3,
        description="Spend Willpower and roll Manipulation + Subterfuge to copy a subject down to the flesh, penalizing attempts to distinguish you by Biokinesis for a scene per success.",
        merit_type="mortal",
        prerequisite="subterfuge:3,biokinesis:1",
        book="HL 73"
    ),
    Merit(
        name="Evil Eye",
        min_value=2,
        max_value=2,
        description="Sacrifice Defense to paralyze with your gaze, contesting Wits + Occult vs Resolve + Composure.",
        merit_type="mortal",
        prerequisite="",
        book="HL 73"
    ),
    Merit(
        name="Hardened Exorcist",
        min_value=1,
        max_value=1,
        description="Add your Occult to your effective Integrity for abjuration modifiers, and ignore Vice penalties.",
        merit_type="mortal",
        prerequisite="",
        book="HL 74"
    ),
    Merit(
        name="Hidden Variable",
        min_value=2,
        max_value=2,
        description="Around infrastructure, take a bonus die to attacks. Ignore 2 Durability or Armor when attacking infrastructure.",
        merit_type="mortal",
        prerequisite="unseen_sense_god_machine:1",
        book="HL 74"
    ),
    Merit(
        name="Incite Ecosystem",
        min_value=1,
        max_value=5,
        description="Spend Willpower and roll Presence + Animal Ken to mark a subject as a threat to an animal or swarm per success. Commanding animals of Size greater than your dots in this Merit inflicts penalties.",
        merit_type="mortal",
        prerequisite="animal_ken:3",
        book="HL 74"
    ),
    Merit(
        name="Invoke Spirit",
        min_value=2,
        max_value=2,
        description="A trauma has attracted a Rank 1 spirit riding you, protecting you but Urging you to recapitulate the trauma.",
        merit_type="mortal",
        prerequisite="resolve:3,medium:3",
        book="HL 74"
    ),
    Merit(
        name="Laying On Hands",
        min_value=3,
        max_value=3,
        description="Spend Willpower and roll Presence + Empathy to take on the ailments of others, either healing two bashing or one lethal per success, or rolling an extended action against a Storyteller-set target to cure sickness. Your character suffers half the damage or sickness he heals.",
        merit_type="mortal",
        prerequisite="",
        book="CofD 57"
    ),
    Merit(
        name="Medium",
        min_value=3,
        max_value=3,
        description="You can sense the presence of ephemeral beings and hear them whispering. You can perform a particular type of ritual or focus and roll Wits + Occult to progress Influence Conditions one step on the continuum from none to Controlled. Once per session, you may have to roll Resolve + Composure to avoid being Shaken or Spooked by the other side.",
        merit_type="mortal",
        prerequisite="empathy:2",
        book="CofD 57"
    ),
    Merit(
        name="Mind Control",
        min_value=3,
        max_value=3,
        description="Spend Willpower and roll Manipulation + Persuasion - Resolve to issue a hypnotic command.",
        merit_type="mortal",
        prerequisite="",
        book="HL 74"
    ),
    Merit(
        name="Mind of a Madman",
        min_value=2,
        max_value=2,
        description="By obsessing over a crime you're investigating, you can go to a dark place. When obsessed, take 8-Again on all rolls to pursue the investigation, but you dream fitfully, and each day that passes without pursuing the investigation is a breaking point.",
        merit_type="mortal",
        prerequisite="empathy:3",
        book="CofD 57"
    ),
    Merit(
        name="Numbing Touch",
        min_value=1,
        max_value=5,
        description="You can spend Willpower to roll Intelligence + Empathy + Numbing Touch vs Stamina + Supernatural Tolerance, inflicting a penalty equal to your dots in the Merit. With a second point of Willpower, you can numb without touching, deny a contesting roll, and sap points of Willpower.",
        merit_type="mortal",
        prerequisite="",
        book="CofD 58"
    ),
    Merit(
        name="Omen Sensitivity",
        min_value=3,
        max_value=3,
        description="Once per session, roll Wits + Occult to interpret incidental omens about your situation or the world, and suffer Obsessed or Spooked. 	",
        merit_type="mortal",
        prerequisite="",
        book="CofD 58"
    ),
    Merit(
        name="Phantasmagoria",
        min_value=2,
        max_value=2,
        description="Spend Willpower and roll Manipulation + Occult to entrance a subject in an illusory experience.",
        merit_type="mortal",
        prerequisite="expression:2,telepathy:5",
        book="HL 74"
    ),
    Merit(
        name="Phantom Limb - Eyes",
        min_value=1,
        max_value=1,
        description="You still have the ghosts of your eyes. See Twilight and when in the Underworld.",
        merit_type="mortal",
        prerequisite="blind",
        book="GtS2e 90"
    ),
    Merit(
        name="Phantom Limb - Ears",
        min_value=1,
        max_value=1,
        description="You still have the ghost of your hearing. Hear Twilight and when in the Underworld. ",
        merit_type="mortal",
        prerequisite="deaf",
        book="GtS2e 90"
    ),
    Merit(
        name="Phantom Limb - Leg",
        min_value=2,
        max_value=2,
        description="You still have the ghost of your leg, which can touch ghosts in Twilight and kick open Avernian Gates.",
        merit_type="mortal",
        prerequisite="leg wrack",
        book="GtS2e 90"
    ),
    Merit(
        name="Phantom Limb - Arm",
        min_value=3,
        max_value=3,
        description="You still have the ghost of your arm. Either you can touch ghostly Twilight with it, or you cannot control it but it always points the way to Essence or Plasm.",
        merit_type="mortal",
        prerequisite="arm wrack",
        book="GtS2e 90"
    ),
    Merit(
        name="Psychic Concealment",
        min_value=3,
        max_value=3,
        description="Spend Willpower and roll Wits + Stealth - Composure to hide your presence from a witness's recognition.",
        merit_type="mortal",
        prerequisite="stealth:3,mind_control:3",
        book="HL 74"
    ),
    Merit(
        name="Psychic Onslaught",
        min_value=3,
        max_value=3,
        description="Spend Willpower and suffer bashing damage to discharge a lethal psychokinetic explosion for your Resolve in meters around you.",
        merit_type="mortal",
        prerequisite="[psychokinesis:3,telekinesis:1]",
        book="HL 74"
    ),
    Merit(
        name="Psychic Poltergeist",
        min_value=2,
        max_value=2,
        description="Spend Willpower to gather small objects in a buffeting, damaging cloud, harrying up to your Telekinesis dots in victims.",
        merit_type="mortal",
        prerequisite="telekinesis:1",
        book="HL 74"
    ),
    Merit(
        name="Psychokinesis",
        min_value=3,
        max_value=5,
        description="Choose an element or force to control. When the element is present, or if you have five dots in the Merit, spend Willpower and roll Resolve + Occult to manipulate its manifestation or attack with it. When out of Willpower, you may have to roll Resolve + Composure to avoid unintended manifestation.",
        merit_type="mortal",
        prerequisite="",
        book="CofD 58"
    ),
    Merit(
        name="Psychokinetic Resistance",
        min_value=1,
        max_value=1,
        description="Apply your Psychokinesis dots as Armor against manifestations of your element.",
        merit_type="mortal",
        prerequisite="psychokinesis:3",
        book="HL 76"
    ),
    Merit(
        name="Psychometry",
        min_value=3,
        max_value=3,
        description="Spend Willpower and roll Wits + Occult to commune with a place or thing and ask questions about its history. You may receive spontaneous communions that inflict a relevant Condition.",
        merit_type="mortal",
        prerequisite="",
        book="CofD 58"
    ),
    Merit(
        name="Sacrificial Offering",
        min_value=1,
        max_value=5,
        description="Suffer a breaking point and roll Wits + Occult as an extended cult ritual to consume a victim's soul, granting supernatural abilities or interventions for a day per dot of Sacrificial Offering.",
        merit_type="mortal",
        prerequisite="occult:3,mystery_cult_initiation:5",
        book="HL 76"
    ),
    Merit(
        name="Sojourner",
        min_value=3,
        max_value=3,
        description="Activate Apportation as an extended action to transport a subject a number of miles.",
        merit_type="mortal",
        prerequisite="apportation:3",
        book="HL 76"
    ),
    Merit(
        name="Stigmata",
        min_value=1,
        max_value=1,
        description="Each week, you may bleed a point of lethal damage from a sacred wound. The blood is supernaturally potent and useful for sorcery. The wound heals after only a day, but you suffer a severe penalty from the pain.",
        merit_type="mortal",
        prerequisite="SotC 193",
        book="SotC 193"
    ),
    Merit(
        name="Supernatural Resistance",
        min_value=1,
        max_value=5,
        description="Apply this dot rating as Supernatural Tolerance.",
        merit_type="mortal",
        prerequisite="any_supernatural_merit",
        book="HL 78"
    ),
    Merit(
        name="Technopathy",
        min_value=2,
        max_value=3,
        description="Spend Willpower and roll Intelligence + Occult to read a device's information and usage at a touch, or with three dots, by wireless network. The device or network suffers or shorts out from the strain.",
        merit_type="mortal",
        prerequisite="",
        book="HL 77"
    ),
    Merit(
        name="Telekinesis",
        min_value=1,
        max_value=5,
        description="Spend Willpower to manifest for a scene, applying dots in the Merit as effective Strength. Attacks cost Willpower and roll Telekinesis + Occult - Stamina to inflict bashing damage. When out of Willpower, you may have to roll Resolve + Composure to avoid unintended manifestation.",
        merit_type="mortal",
        prerequisite="",
        book="CofD 59"
    ),
    Merit(
        name="Telekinetic Evasion",
        min_value=3,
        max_value=3,
        description="Spend Willpower when Dodging to add your dots in Telekinesis as bonus successes.",
        merit_type="mortal",
        prerequisite="telekinesis:1",
        book="HL 77"
    ),
    Merit(
        name="Telepathy",
        min_value=3,
        max_value=5,
        description="Spend Willpower and roll Wits + Empathy - Resolve to read a mind, or with five dots, to project thoughts. You may spontaneously overhear disturbing thoughts that inflict a relevant Condition.",
        merit_type="mortal",
        prerequisite="",
        book="CofD 59"
    ),
    Merit(
        name="Thief of Fate",
        min_value=3,
        max_value=3,
        description="Whenever you touch someone, for the rest of the day, you gain +4 dice instead of +3 when you spend Willpower on a roll, but the subject's rolled failures become dramatic failures, and they intuit a sense that you're responsible. Spend Willpower to suppress Thief of Fate for a scene.",
        merit_type="mortal",
        prerequisite="",
        book="CofD 60"
    ),
    Merit(
        name="Unseen Sense",
        min_value=2,
        max_value=2,
        description="Choose a source of supernatural phenomena, like vampires or the God-Machine, and how your sense of that power manifests when it's close. Once per session, you can become Spooked and pinpoint what's setting off your sense around you, unless it's cloaked by suitable magic.",
        merit_type="mortal",
        prerequisite="",
        book="CofD 60"
    ),
    Merit(
        name="Vengeful Soul",
        min_value=2,
        max_value=2,
        description="Each session, a number of actions to avenge a loved one's witnessed death, up to their Integrity, gains 8-Again.",
        merit_type="mortal",
        prerequisite="",
        book="HL 77"
    ),
    #Supernatural Combat Styles
    Merit(
        name="Fated Ferocity",
        min_value=1,
        max_value=5,
        description="Style. Your character, though condemned to die by fate, has turned their ill-fortune into a grim purpose.",
        merit_type="mortal",
        prerequisite="resolve:3,stamina:2,cursed:1",
        book="HL 73"
    ),
    Merit(
        name="Psychokinetic Combat",
        min_value=1,
        max_value=5,
        description="Style. You have learned several combat maneuvers that tap into your psychokinesis.",
        merit_type="mortal",
        prerequisite="psychokinesis:1",
        book="HL 76"
    ),
    Merit(
        name="Tactical Telepathy",
        min_value=1,
        max_value=5,
        description="Style. You leverage your latent Telepathy into a tactical tool.",
        merit_type="mortal",
        prerequisite="telepathy:5",
        book="HL 76"
    ),
    #Vampire Related Merits
    Merit(
        name="Beast Whispers",
        min_value=2,
        max_value=2,
        description="Talk vampires down from frenzy as if they held you as a Touchstone.",
        merit_type="mortal",
        prerequisite="",
        book="VtR2e 300"
    ),
    Merit(
        name="Beloved",
        min_value=1,
        max_value=1,
        description="Grant a vampire who holds you as a Touchstone +2 to resist frenzy in your presence, and you can talk them down as if their Blood Potency were up to two dots lower (minimum one dot).",
        merit_type="mortal",
        prerequisite="",
        book="VtR2e 300"
    ),
    Merit(
        name="Clear-Sighted",
        min_value=2,
        max_value=2,
        description="Spend Willpower to see through illusions, including the effects of the Obfuscate and Nightmare Disciplines.",
        merit_type="mortal",
        prerequisite="",
        book="VtR2e 299"
    ),
    Merit(
        name="Producer",
        min_value=1,
        max_value=1,
        description="Your blood is worth twice its normal value to vampires as Vitae",
        merit_type="mortal",
        prerequisite="",
        book="VtR2e 299"
    ),
    Merit(
        name="Protected",
        min_value=2,
        max_value=2,
        description="A vampire who has tasted your blood has grown attached to you, and can sense when you are in danger.",
        merit_type="mortal",
        prerequisite="",
        book="VtR2e 299"
    ),
    Merit(
        name="Weakened Bond",
        min_value=3,
        max_value=3,
        description="Respond to a vampire's blood bond as if it were one step weaker.",
        merit_type="mortal",
        prerequisite="",
        book="VtR2e 299"
    ),
    #Ghoul Merits
    Merit(
        name="Empowered to Speak",
        min_value=1,
        max_value=1,
        description="You can borrow your regnant's City Status when speaking as their formal representation.",
        merit_type="ghoul",
        prerequisite="",
        book="VtR2e 300"
    ),
    Merit(
        name="Family Ties",
        min_value=2,
        max_value=2,
        description="You can sense threats to family and trace them with Wits + Investigation, but they cause breaking points if carried through.",
        merit_type="ghoul",
        prerequisite="ghoul_family",
        book="HD 122"
    ),
    Merit(
        name="Inherited",
        min_value=2,
        max_value=2,
        description="You have had multiple regnants. Roll Intelligence + Composure +2 to recall useful information about past regnants when appropriate.",
        merit_type="ghoul",
        prerequisite="",
        book="HD 122"
    ),
    Merit(
        name="Insomniac",
        min_value=1,
        max_value=1,
        description="Three hours of sleep provide complete rest.",
        merit_type="ghoul",
        prerequisite="",
        book="HD 122"
    ),
    Merit(
        name="Lurch",
        min_value=3,
        max_value=3,
        description="Your regnant trusts you as her house ghoul. +2 to notice details of your regnant or her haven.",
        merit_type="ghoul",
        prerequisite="",
        book="HD 122"
    ),
    Merit(
        name="Sexualized",
        min_value=2,
        max_value=2,
        description="+2 to Presence and Manipulation rolls leveraging your unnatural sexual enticement.",
        merit_type="ghoul",
        prerequisite="",
        book="HD 122"
    ),
    Merit(
        name="Source Sympathy",
        min_value=1,
        max_value=1,
        description="Experience vampiric Blood Sympathy as if you were a vampire thrice removed from your regnant.",
        merit_type="ghoul",
        prerequisite="",
        book="VtR2e 299"
    ),
    Merit(
        name="Taste of Fear",
        min_value=2,
        max_value=2,
        description="Spend Willpower and roll Manipulation + Intimidation vs Resolve + Blood Potency to use a dark secret about yourself to inflict the effects of Broken, Fugue, or Guilty for a scene.",
        merit_type="ghoul",
        prerequisite="nosferatu_regnant",
        book="VtR2e 299"
    ),
    Merit(
        name="Taste of Gold",
        min_value=2,
        max_value=2,
        description="Beating someone in a competition counts as satisfying your Vice.",
        merit_type="ghoul",
        prerequisite="ventrue_regnant",
        book="VtR2e 299"
    ),
    Merit(
        name="Taste of Shadow",
        min_value=2,
        max_value=2,
        description="Once per scene, spend Willpower and roll Wits + Occult to intuit knowledge about the Blood.",
        merit_type="ghoul",
        prerequisite="mekhet_regnant",
        book="VtR2e 298"
    ),
    Merit(
        name="Taste of the Serpent",
        min_value=2,
        max_value=2,
        description="You can inflict Swooning on humans by helping to satisfy their Vice.",
        merit_type="ghoul",
        prerequisite="daeva_regnant",
        book="VtR2e 298"
    ),
    Merit(
        name="Taste of the Wild",
        min_value=2,
        max_value=2,
        description="You can ghoul animals and inflict the Vinculum on them.",
        merit_type="ghoul",
        prerequisite="gangrel_regnant",
        book="VtR2e 298"
    ),
    Merit(
        name="Unobtrusive",
        min_value=2,
        max_value=2,
        description="+2 to duck your regnant's notice with Stealth.",
        merit_type="ghoul",
        prerequisite="stealth:2",
        book="HD 122"
    ),
    Merit(
        name="Vitae Hound",
        min_value=1,
        max_value=1,
        description="You can use Kindred Senses, as if you had half your regnant's Blood Potency.",
        merit_type="ghoul",
        prerequisite="",
        book="VtR2e 300"
    ),
    Merit(
        name="Watch Dog",
        min_value=2,
        max_value=2,
        description="Your regnant can loan you the use of her Auspex during the day.",
        merit_type="ghoul",
        prerequisite="regnant_has_auspex",
        book="VtR2e 300"
    ),
    #Dhampir Merits
    Merit(
        name="Altar",
        min_value=1,
        max_value=1,
        description="As per the Kindred Merit",
        merit_type="dhampir",
        prerequisite="crone_status:1,three_acolytes_attuned",
        book="HD 44, VTR2e 109"
    ),
    Merit(
        name="Beloved Stranger",
        min_value=2,
        max_value=2,
        description="You came to awareness from a mortal upbringing. +2 to resist breaking points from the supernatural, and reduce the exceptional threshold for Mental and Social rolls to meddle in, expose or conceal the occult from five to three.",
        merit_type="dhampir",
        prerequisite="nights_child:0",
        book="HD 44"
    ),
    Merit(
        name="Blood Dissonance",
        min_value=1,
        max_value=5,
        description="Force a Clash of Wills with Resolve + Blood Dissonance to supernaturally intuit your nature. Once a story, you may refuse taking your Affliction Condition and instead penalize breaking points brought on by your actions or nature by dots in this Merit for a session.",
        merit_type="dhampir",
        prerequisite="",
        book="HD 44"
    ),
    Merit(
        name="Cacophony Savvy",
        min_value=1,
        max_value=3,
        description="Style. As per the Kindred Style",
        merit_type="dhampir",
        prerequisite="city_status:1",
        book="HD 44, VtR2e 110"
    ),
    Merit(
        name="Dynasty Membership",
        min_value=1,
        max_value=3,
        description="Style. As per the Kindred Style",
        merit_type="dhampir",
        prerequisite="clan_status:1",
        book="HD 44, VtR2e 112"
    ),
    Merit(
        name="Hand of Doom",
        min_value=3,
        max_value=3,
        description="Contest Wits + Occult vs Composure + Tolerance to sense a character's destiny. Furthering their Destiny benefits you like furthering your own.",
        merit_type="dhampir",
        prerequisite="",
        book="HD 44"
    ),
    Merit(
        name="Honey Trap",
        min_value=1,
        max_value=1,
        description="As per the Kindred Merit.",
        merit_type="dhampir",
        prerequisite="",
        book="HD 44, VTR2e 112"
    ),
    Merit(
        name="Kindred Status",
        min_value=1,
        max_value=3,
        description="As per the Kindred Merit, with a lower max.",
        merit_type="dhampir",
        prerequisite="",
        book="HD 44, VtR2e 113"
    ),
    Merit(
        name="Mother's Army Recruit",
        min_value=1,
        max_value=3,
        description="You may sense blood sorcery, use your blood in Crúac, and participate in Crúac teamwork like a vampire. With three dots, you may learn the Crúac Discipline and rites at a one experience surcharge.",
        merit_type="dhampir",
        prerequisite="crone_status:1",
        book="HD 45"
    ),
    Merit(
        name="Night's Child",
        min_value=2,
        max_value=2,
        description="You were raised in the All Night Society. Talk familiar vampires down from frenzy like a Touchstone, and reduce the exceptional threshold for Mental or Social rolls as a go-between twixt Kindred and non-Kindred from five to three.",
        merit_type="dhampir",
        prerequisite="beloved_stranger:0",
        book="HD 45"
    ),
    Merit(
        name="Requiem Counterpoint",
        min_value=1,
        max_value=1,
        description="Your role as a vampire's Touchstone allows you to recover Willpower when they resist detachment in your presence, but you feel Guilty if they fail.",
        merit_type="dhampir",
        prerequisite="",
        book="HD 45"
    ),
    Merit(
        name="Vampire Hunter",
        min_value=1,
        max_value=4,
        description="Hone one Kindred Sense for each dot in this Merit. Apply Vampire Hunter as a bonus to perception concerning vampires, and as your Blood Potency as regards Kindred Senses.",
        merit_type="dhampir",
        prerequisite="wits:3",
        book="HD 45"
    ),
    #Werewolf Related Merits
    Merit(
        name="Shadow Occultism",
        min_value=4,
        max_value=4,
        description="Gain an essence pool, the ability to learn park rites to perform even alone, and gain a 3 dot influence.",
        merit_type="mortal",
        prerequisite="was_ridden",
        book="NH:SM 138"
    ),
    Merit(
        name="Shadow Perception",
        min_value=3,
        max_value=3,
        description="Can see spirits in twilight and speak in first tongue. Can sense resonance of any influence you have.",
        merit_type="mortal",
        prerequisite="shadow_occultism:4",
        book="NH:SM 138"
    ),
    #Wolf-Blooded Merits
    Merit(
        name="Crescent Moon's Birth",
        min_value=2,
        max_value=2,
        description="Grant +3 Durability and +3 Structure when you help craft a fetish.",
        merit_type="wolfblooded",
        prerequisite="birth",
        book="WtF2e 305"
    ),
    Merit(
        name="Fenris-Ur's Blood",
        min_value=2,
        max_value=2,
        description="Take 8-Again to craft or wield silver weapons.",
        merit_type="wolfblooded",
        prerequisite="heritage",
        book="WtF2e 304"
    ),
    Merit(
        name="Full Moon's Birth",
        min_value=2,
        max_value=2,
        description="Once per scene, you can spend Willpower to lead a coordinated action, granting +3 dice and 8-Again to participants up to your Presence.",
        merit_type="wolfblooded",
        prerequisite="birth",
        book="WtF2e 305"
    ),
    Merit(
        name="Ghost Child",
        min_value=2,
        max_value=2,
        description="Take 9-Again to roll Skills rated from one to three dots, but lose 10-Again to roll Skills rated above that.",
        merit_type="wolfblooded",
        prerequisite="heritage",
        book="WtF2e 304"
    ),
    Merit(
        name="Gibbous Moon's Birth",
        min_value=2,
        max_value=2,
        description="Take 8-Again and perform extended actions twice as fast when rolling a chosen Mental Skill.",
        merit_type="wolfblooded",
        prerequisite="birth",
        book="WtF2e 305"
    ),
    Merit(
        name="Half Moon's Birth",
        min_value=2,
        max_value=2,
        description="Take +2 when rolling a breaking point in your territory. Once per session, you can take 8-Again and bonus dice equal to your Safe Place on one roll.",
        merit_type="wolfblooded",
        prerequisite="birth,safe_place:1",
        book="WtF2e 305"
    ),
    Merit(
        name="Hikaon-Ur's Blood",
        min_value=2,
        max_value=2,
        description="Ignore total darkness penalties. When denied a sense, take +2 to compensate with other senses.",
        merit_type="wolfblooded",
        prerequisite="heritage",
        book="WtF2e 304"
    ),
    Merit(
        name="Kamduis-Ur's Blood",
        min_value=2,
        max_value=2,
        description="Roll Intelligence + Occult to create a mark that can trap a ghost for an hour per success.",
        merit_type="wolfblooded",
        prerequisite="heritage",
        book="WtF2e 304"
    ),
    Merit(
        name="No Moon's Birth",
        min_value=2,
        max_value=2,
        description="When you scout on instructions from a pack leader or parental figure, you leave no scent, cannot be followed home, and your point of origin or allegiance can't be ascertained.",
        merit_type="wolfblooded",
        prerequisite="birth",
        book="WtF2e 305"
    ),
    Merit(
        name="Pack Bond",
        min_value=1,
        max_value=3,
        description="You're respected as an important member of the pack. You can buy one dot of Totem, or up to five dots with Pack Bond •••.",
        merit_type="wolfblooded",
        prerequisite="",
        book="WtF2e 305"
    ),
    Merit(
        name="Raised By Wolves",
        min_value=1,
        max_value=1,
        description="You grew up among werewolves. Ignore Resistance rolls to withstand the bizarre or grotesque things you see.",
        merit_type="wolfblooded",
        prerequisite="",
        book="WtF2e 305"
    ),
    Merit(
        name="Sagrim-Ur's Blood",
        min_value=2,
        max_value=2,
        description="Take 8-Again and add Safe Place as bonus dice to roll Crafts or Computer to set up security measures.",
        merit_type="wolfblooded",
        prerequisite="heritage",
        book="WtF2e 304"
    ),
    Merit(
        name="Skolis-Ur's Blood",
        min_value=2,
        max_value=2,
        description="Immunity to Urging, and to being supernaturally forced to appear weak or defeated.",
        merit_type="wolfblooded",
        prerequisite="heritage",
        book="WtF2e 304"
    ),
    Merit(
        name="Tell",
        min_value=3,
        max_value=3,
        description="You have another Wolf-Blooded Tell",
        merit_type="wolfblooded",
        prerequisite="",
        book="WtF2e 305"
    ),
    #Mage Related Merits
    Merit(
        name="Fitful Slumber",
        min_value=1,
        max_value=1,
        description="Suffering repeated exposure to Supernal magic or the Abyss has granted you +2 to relevant breaking points, and made you a Sleepwalker.",
        merit_type="mortal",
        prerequisite="breaking_points:3",
        book="MtA2e 306"
    ),
    Merit(
        name="High Speech Perception",
        min_value=2,
        max_value=2,
        description="Your character may percieve and read High Speech as though they were a mage",
        merit_type="mortal",
        prerequisite="",
        book="SoS 26"
    ),
    Merit(
        name="Sleepwalker",
        min_value=1,
        max_value=1,
        description="You were a Sleeper, but you're not now.",
        merit_type="mortal",
        prerequisite="",
        book="MtA2e 306"
    ),
    #Sleeper Merits
    Merit(
        name="Actively Obvious",
        min_value=2,
        max_value=2,
        description="You can spend Willpower and suffer the Strained Condition to consciously ignore a breaking point. When you do so, you don't count as a witness to a supernal spell.",
        merit_type="sleeper",
        prerequisite="",
        book="MtA2e 302"
    ),
    Merit(
        name="Communal Sleeper",
        min_value=1,
        max_value=1,
        description="When you guide at least one other Sleeper, you count as a group of witnesses to supernal magic one step worse.",
        merit_type="sleeper",
        prerequisite="empathy:2",
        book="MtA2e 302"
    ),
    Merit(
        name="Detail Oriented",
        min_value=2,
        max_value=2,
        description="When you attempt an Investigation or Perception roll previously failed by a non-Sleeper, take an exceptional success on a threshold of three instead of five.",
        merit_type="sleeper",
        prerequisite="",
        book="MtA2e 302"
    ),
    Merit(
        name="Liar",
        min_value=1,
        max_value=1,
        description="Your existence is tainted by the Abyss. Add two dice to Paradox risks and Dissonance rolls. You grant the Open Influence Condition to Abyssal entities, and take a -1 penalty to Abyssal breaking points.",
        merit_type="sleeper",
        prerequisite="",
        book="MtA2e 302"
    ),
    Merit(
        name="Strained",
        min_value=2,
        max_value=2,
        description="You can take the Strained Condition to ignore a Supernal or Abyssal breaking point.",
        merit_type="sleeper",
        prerequisite="integrity<6",
        book="MtA2e 302"
    ),
    #Sleepwalker Merits
    Merit(
        name="Banner-Bearer",
        min_value=1,
        max_value=3,
        description="You can carry an additional supernal spell for each dot of this Merit.",
        merit_type="sleepwalker",
        prerequisite="",
        book="MtA2e 305"
    ),
    Merit(
        name="Deadpan",
        min_value=3,
        max_value=3,
        description="Ignore sources of fear or revulsion, including supernatural sources, that don't play on a preexisting Condition or Vice. Take +2 to Composure to resist those that do.",
        merit_type="sleepwalker",
        prerequisite="",
        book="MtA2e 305"
    ),
    Merit(
        name="Loved",
        min_value=3,
        max_value=3,
        description="Something sincerely loves you. Nobody else can form Strong magical sympathy with you, though you can form it with them. When you're distressed by wound penalties or low Willpower, your love can sense it.",
        merit_type="sleepwalker",
        prerequisite="",
        book="MtA2e 306"
    ),
    Merit(
        name="Proxy Voice",
        min_value=1,
        max_value=3,
        description="You have a mentor in Awakened society. Choose one of his Status Merits: you can borrow it when acting in his stead.",
        merit_type="sleepwalker",
        prerequisite="mentor:1",
        book="MtA2e 306"
    ),
    Merit(
        name="Relic Attuned",
        min_value=3,
        max_value=3,
        description="Your character is not Awakened, but can still access the magics stored in Artifacts. Activation requires a point of willpower. Activation rolls for artifacts can use the character's willpower or the artifacts own activation dice as a die pool.",
        merit_type="sleepwalker",
        prerequisite="",
        book="MtA2e 306"
    ),
    Merit(
        name="Ritual Savvy",
        min_value=2,
        max_value=2,
        description="You understand Awakened ritual enough to set up useful staging or equipment. Roll an Attribute + Skill pool appropriate for the ritual being cast. For each success, one mage can spend a point of Willpower for a bonus die on the spell, which doesn't count towards their Yantra limit.",
        merit_type="sleepwalker",
        prerequisite="occult:2",
        book="MtA2e 306"
    ),
    Merit(
        name="Slippery",
        min_value=2,
        max_value=2,
        description="When the Awakened lay blame, spend Willpower to fly below the radar.",
        merit_type="sleepwalker",
        prerequisite="",
        book="MtA2e 306"
    ),
    #Changeling-Related Merits
    Merit(
        name="Expressive",
        min_value=1,
        max_value=1,
        description="Produce twice the Glamour harvest.",
        merit_type="mortal",
        prerequisite="",
        book="CtL2e 320"
    ),
    #Fae-Touched Merits
    Merit(
        name="Court Goodwill",
        min_value=1,
        max_value=5,
        description="As The Changeling Merit",
        merit_type="faetouched",
        prerequisite="",
        book="Ctl2e 112,319"
    ),
    Merit(
        name="Dream Ghost",
        min_value=2,
        max_value=2,
        description="Can enter the promise-bound Changeling's dreams regardless of distance with three successes to enter the Gate of Ivory. Can perform drewamweaving with Dream Shaper, otherwise can spend a willpower to pass on a message.",
        merit_type="faetouched",
        prerequisite="lucid_dreamer:2",
        book="Hedge 100"
    ),
    Merit(
        name="Dream Shaper",
        min_value=2,
        max_value=2,
        description="Dreamweave within your own dreams.",
        merit_type="faetouched",
        prerequisite="lucid_dreamer:2",
        book="CtL2e 320"
    ),
    Merit(
        name="Dream Tripper",
        min_value=3,
        max_value=3,
        description="Exit your Bastion onto the dreaming roads. Immediately gain Dream Infiltrator in the dreams of strangers or enemies.",
        merit_type="faetouched",
        prerequisite="dream_shaper:1,dreamsteps:1",
        book="Hedge 100"
    ),
    Merit(
        name="Dreamer's Gaze",
        min_value=1,
        max_value=1,
        description="Spend glamour to view promise bound's dream in a reflective surface, and can potentially enter it with Dreamsteps.",
        merit_type="faetouched",
        prerequisite="",
        book="Hedge 101"
    ),
    Merit(
        name="Endymion's Dream",
        min_value=3,
        max_value=3,
        description="Remain asleep and gain immunity to being woken up by paradigm shifts with a successful Resolve + Occult roll.",
        merit_type="faetouched",
        prerequisite="lucid_dreamer:2",
        book="Hedge 101"
    ),
    Merit(
        name="Find the Oathbreaker",
        min_value=2,
        max_value=2,
        description="Sense Oathbreakers like a changeling, and roll Wits + Empathy with a touch to intuit promises broken within a day, or pledges within a week.",
        merit_type="faetouched",
        prerequisite="sense_vows:1",
        book="CtL2e 320"
    ),
    Merit(
        name="Glamour Fasting",
        min_value=1,
        max_value=1,
        description="As the Changeling Merit.",
        merit_type="faetouched",
        prerequisite="",
        book="CtL2e 115, 319"
    ),
    Merit(
        name="Hedge Delver",
        min_value=3,
        max_value=3,
        description="Hedgespin subtle shifts. +2 to help a Changeling navigate the Hedge.",
        merit_type="faetouched",
        prerequisite="survival:2",
        book="CtL2e 320"
    ),
    Merit(
        name="Hollow",
        min_value=1,
        max_value=5,
        description="As the Changeling Merit, but must be shared.",
        merit_type="faetouched",
        prerequisite="",
        book="CtL2e 116, 319"
    ),
    Merit(
        name="Oathkeeper",
        min_value=3,
        max_value=3,
        description="Willpower spent to contest attempts to sway you to break a sealing or oath adds four dice instead of three and reduces the exceptional threshold from five to three.",
        merit_type="faetouched",
        prerequisite="resolve:3",
        book="CtL2e 320"
    ),
    Merit(
        name="Promise of Debt",
        min_value=1,
        max_value=3,
        description="You swore to repay a debt you owed someone. Apply as bonus dice to help settle a debt.",
        merit_type="faetouched",
        prerequisite="",
        book="Ct2e 320"
    ),
    Merit(
        name="Promise of Love",
        min_value=1,
        max_value=3,
        description="You swore unending love. Apply as bonus dice to contest attempts to manipulate your feelings about another.",
        merit_type="faetouched",
        prerequisite="",
        book="Ctl2e 320"
    ),
    Merit(
        name="Promise of Loyalty",
        min_value=3,
        max_value=3,
        description="You swore to stand by another's side. Remove a Door when Social Maneuvering through your relationship or shared history with another. 	",
        merit_type="faetouched",
        prerequisite="",
        book="CtL2e 320"
    ),
    Merit(
        name="Promise of Protection",
        min_value=1,
        max_value=5,
        description="You swore to keep someone safe. When fighting to protect someone, apply as an Initiative bonus, and reduce the Defense penalty from multiple attacks by one.",
        merit_type="faetouched",
        prerequisite="",
        book="CtL2e 320"
    ),
    Merit(
        name="Promise to Provide",
        min_value=3,
        max_value=3,
        description="You swore someone would always have a home with you. Spend Glamour when offering your hospitality. A guest who accepts must spend Willpower to betray that hospitality, but recovers Willpower if they don't.",
        merit_type="faetouched",
        prerequisite="",
        book="CtL2e 320"
    ),
    Merit(
        name="Promise to Serve",
        min_value=1,
        max_value=3,
        description="You swore a service in someone's stead. Apply as bonus teamwork successes.",
        merit_type="faetouched",
        prerequisite="",
        book="CtL2e 321"
    ),
    Merit(
        name="Punish the Oathbreaker",
        min_value=2,
        max_value=2,
        description="Exercise Loopholes to use your Contracts against a found oathbreaker alone.",
        merit_type="faetouched",
        prerequisite="find_the_oathbreaker:2",
        book="CtL2e 321"
    ),
    Merit(
        name="Sense Vows",
        min_value=1,
        max_value=1,
        description="Spend Glamour to sense whether a character was pledgebound within the current story.",
        merit_type="faetouched",
        prerequisite="",
        book="CtL2e 321"
    ),
    Merit(
        name="Twice Shy",
        min_value=3,
        max_value=3,
        description="Can use Dreamer's Gaze on the promise-bound Changeling's fetch.",
        merit_type="faetouched",
        prerequisite="dreamers_gaze:1,fetch_is_alive",
        book="Hedge 101"
    ),
    #Mummy Related Merits
    Merit(
        name="Grave Robber",
        min_value=5,
        max_value=5,
        description="Disturb the tombs of the Arisen without waking them. Stealing an entombed relic wakes the mummy after two hours and taints their investigation to track the relic down.",
        merit_type="mortal",
        prerequisite="",
        book="MtC2e 117"
    ),
    Merit(
        name="Lineal Inheritor",
        min_value=3,
        max_value=3,
        description="One of your parents passed away while invested with the Pillar of a mummy's soul. You now benefit from investment, and the mummy must perform the Rite of Investment on you to withdraw it.",
        merit_type="mortal",
        prerequisite="",
        book="MtC2e 118"
    ),
    Merit(
        name="Witness",
        min_value=3,
        max_value=3,
        description="Gain the effects of Unseen Sense for immortals and the undead. Instead of suffering Sybaris, you become Obsessed with visions of the Arisen from across time.",
        merit_type="mortal",
        prerequisite="",
        book="MtC2e 121"
    ),
    #Mummy Ritual Sorcery Merits
    Merit(
        name="Ritual Sorcerer",
        min_value=3,
        max_value=3,
        description="You have learned how to perform sorcerous rites. For each dot of Resolve, you may learn one Closed Rite or master one Open Rite.",
        merit_type="mortal",
        prerequisite="[intelligence:3,wits:3,resolve:3],occult:3,skill_specialty:1",
        book="MtC2e 120"
    ),
    Merit(
        name="Forbidden Rites",
        min_value=1,
        max_value=5,
        description="You can attempt an additional Closed Rite for each dot of this Merit at extreme ritual costs and a -2 penalty.",
        merit_type="mortal",
        prerequisite="ritual_sorcerer:3,library:2,sorcerous_knowledge:1",
        book="MtC2e 117"
    ),
    Merit(
        name="Sorcerous Knowledge",
        min_value=1,
        max_value=5,
        description="For each dot, you may learn or create one Closed Rite or master one Open Rite.",
        merit_type="mortal",
        prerequisite="ritual_sorcerer:3,occult>=sorcerous_knowledge",
        book="MtC2e 120"
    ),
    Merit(
        name="Sorcerous Prodigy",
        min_value=3,
        max_value=3,
        description="Dots of Resolve or Sorcerous Knowledge used to master Open Rites each master a second Open Rite.",
        merit_type="mortal",
        prerequisite="ritual_sorcerer:3,sorcerous_knowledge:2",
        book="MtC 120"
    ),
    #Demon Related Merits
    #Stigmatic Merits
    Merit(
        name="Potent Blood",
        min_value=1,
        max_value=1,
        description="Bleed a point of lethal damage every other day. Consecrating with the blood confers +2 to a supernatural action, and demons recover a point of Aether by ingesting it. Vampires who feed from you temporarily gain the effects of Unseen Sense (God-Machine).",
        merit_type="stigmatic",
        prerequisite="",
        book="FoH 130"
    ),
    Merit(
        name="Sleeve Integrator",
        min_value=1,
        max_value=5,
        description="Spend Willpower to merge with a demon, allowing her to use your life as a Cover for up to a day, with a rating equal to your Integrity. Afterwards, you gain access to one of the demon's Embeds per dot in this Merit.",
        merit_type="stigmatic",
        prerequisite="integrity>=5",
        book="FoH 130"
    ),
    Merit(
        name="Sympathetic Demon",
        min_value=2,
        max_value=2,
        description="You have a demon friend. Once per session, you can declare the demon's convenient arrival. You suffer any damage the demon suffers.",
        merit_type="stigmatic",
        prerequisite="",
        book="FoH 130"
    ),
    Merit(
        name="Pact Sense Merit",
        min_value=3,
        max_value=3,
        description="You can senses the aspects of reality stitched together by demonic pacts.",
        merit_type="stigmatic",
        prerequisite="",
        book="DE2 175"
    ),
    #Demon-Blooded Merits
    Merit(
        name="Ambient Aether",
        min_value=1,
        max_value=2,
        description="You can gather and spend Aether. Fractals buy for one dot, offspring two.",
        merit_type="demonblooded",
        prerequisite="[offspring,fractal]",
        book="HtH 37"
    ),
    Merit(
        name="Aether Pool",
        min_value=2,
        max_value=2,
        description="Gain a five-point Aether pool.",
        merit_type="demonblooded",
        prerequisite="fractal,ambient_aether:1",
        book="HtH 37"
    ),
    Merit(
        name="Eidetic Memory",
        min_value=1,
        max_value=1,
        description="As the General Merit, but reduced cost.",
        merit_type="demonblooded",
        prerequisite="",
        book="HtH 33, CofD 44"
    ),
    Merit(
        name="Infrastructure Proficiency",
        min_value=2,
        max_value=3,
        description="Find your way through infrastructure, intuit how it works, and identify linchpins. Costs two dots for fractals or three for others.",
        merit_type="demonblooded",
        prerequisite="",
        book="HtH 37"
    ),
    Merit(
        name="Instinctive Deflection",
        min_value=2,
        max_value=2,
        description="Roll Wits + Resolve to avoid compromise",
        merit_type="demonblooded",
        prerequisite="",
        book="HtH 37"
    ),
    Merit(
        name="Language",
        min_value=1,
        max_value=1,
        description="In addition to the general Merit's effects, speak a second language conversationally.",
        merit_type="demonblooded",
        prerequisite="",
        book="HtH 37, CofD 46"
    ),
    Merit(
        name="Multilingual",
        min_value=1,
        max_value=1,
        description="As the general Merit, but with three languages.",
        merit_type="demonblooded",
        prerequisite="",
        book="HtH 37, CofD 46"
    ),
    Merit(
        name="Quantum Understanding",
        min_value=3,
        max_value=3,
        description="Contest Wits + Composure vs Tolerance to read a demon's Liar's Tongue.",
        merit_type="demonblooded",
        prerequisite="fractal",
        book="HtH 37"
    ),
    Merit(
        name="Unknown",
        min_value=1,
        max_value=1,
        description="Begin play without a Cipher Condition, but with only one Embed and no Interlocks. Character creation only.",
        merit_type="demonblooded",
        prerequisite="[offspring,fractal]",
        book="HtH 37"
    ),
    #Nephilim Merits
    Merit(
        name="Unseen Sense",
        min_value=2,
        max_value=2,
        description="As a stigmatic's Unseen Sense, and you may roll Wits + Occult to sense the presence of Aether sources, including angels and demons.",
        merit_type="nephilim",
        prerequisite="",
        book="DSG 156"
    ),
    Merit(
        name="Voice of Hell",
        min_value=2,
        max_value=2,
        description="Spend Aether for fluency in a language for one scene.",
        merit_type="nephilim",
        prerequisite="",
        book="DSG 156"
    ),
]

# Create dictionary for easy lookup
mortal_merits_dict = {merit.name.lower().replace(" ", "_").replace("(", "").replace(")", ""): merit for merit in mortal_merits}
