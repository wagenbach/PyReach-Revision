from world.cofd.stat_types import Merit

# Location-Based Merits
location_merits = [
    #Universal Locations
    Merit(
        name="Safe Place",
        min_value=1,
        max_value=5,
        description="You've secured a place from intrusion. Apply your Safe Place rating as an Initiative bonus while there, and a penalty to break in. With Crafts you can install traps, forcing intruders to roll Dexterity + Larceny - Safe Place to avoid up to your Safe Place in lethal damage.",
        merit_type="universal",
        prerequisite="",
        book="CofD 52"
    ),
    Merit(
        name="Hiding Place",
        min_value=3,
        max_value=3,
        description="You have a place that is always secure. If found out, gain a new one at the start of the next chapter. This cannot be shared.",
        merit_type="universal",
        prerequisite="",
        book="GTTN 124"
    ),
    #Vampire Locations
    Merit(
        name="Burrow",
        min_value=1,
        max_value=5,
        description="Replaces Haven. Must be shared. You share a hideout with other revenants. Add Burrow as bonus dice to stir from daysleep and stay awake in the daytime. In combat, intruders and unfamiliar guests are Distracted for one turn per dot of Burrow.",
        merit_type="vampire",
        prerequisite="safe_place:1",
        book="HD 80"
    ),
    Merit(
        name="Haven",
        min_value=1,
        max_value=5,
        description="You've sunproofed your residence and made it a home. Add Haven as bonus dice to stir from daysleep and stay awake in the daytime, and to use Kindred Senses within your home.",
        merit_type="vampire",
        prerequisite="safe_place:1",
        book="VtR2e 112"
    ),
    Merit(
        name="Mandragora Garden",
        min_value=1,
        max_value=5,
        description="Your Safe Place grows ghouled plants, which you must feed Vitae equal to your Merit dots each month, but which produce twice that quantity in Vitae's worth of sap and nectar. Their magical sympathy empowers Crúac cast there and receives it from afar, but can rile the Beast when attacked.",
        merit_type="vampire",
        prerequisite="cruac:1,crone_status:1,safe_place:1",
        book="SotC 181"
    ),
    Merit(
        name="Nest Guardian",
        min_value=1,
        max_value=5,
        description="You are the custodian of a Wyrm's Nest, host to a supernatural phenomenon proportional to dots in this Merit. You may purchase additional features separately, listed below.",
        merit_type="vampire",
        prerequisite="ordo_dracul_status:1",
        book="SotC 197"
    ),
    Merit(
        name="Chapterhouse",
        min_value=1,
        max_value=5,
        description="Vampires in the Nest add dots in this Merit as a bonus to resist violence, and as a penalty to lash out with the Predatory Aura.",
        merit_type="vampire",
        prerequisite="ordo_dracul_status:3",
        book="SotC 199"
    ),
    Merit(
        name="Crucible",
        min_value=3,
        max_value=3,
        description="Vampires may advance study of the Mysteries of the Dragon in the Nest at an experience discount.",
        merit_type="vampire",
        prerequisite="occult:4",
        book="SotC 199"
    ),
    Merit(
        name="Feng Shui",
        min_value=1,
        max_value=5,
        description="Choose a Skill. Vampires in the Nest may add dots in this Merit as bonus dice when rolling that Skill.",
        merit_type="vampire",
        prerequisite="academics:2,occult:3",
        book="SotC 199"
    ),
    Merit(
        name="Perilous Nest",
        min_value=1,
        max_value=5,
        description="You've harnessed a hazard native to the Nest to attack certain unwelcome types. It uses a dice pool equal to twice your dots in this Merit.",
        merit_type="vampire",
        prerequisite="occult:3",
        book="SotC 199"
    ),
    Merit(
        name="Temple of Damnation",
        min_value=1,
        max_value=5,
        description="You've secured and consecrated a gathering place to a particular Sanctified virtue. Apply dots in this Merit as a bonus to actions in service of that virtue while within the temple, or after attending rites there.",
        merit_type="vampire",
        prerequisite="lancea_status:1,safe_place:1",
        book="SotC 194"
    ),
    #Werewolf Locations
    Merit(
        name="Dedicated Locus",
        min_value=1,
        max_value=5,
        description="You've personally attuned a locus to your pack. The locus has a rating equal to this Merit, and provides the pack the ability to spend a point of Essence above their per-turn cap, a number of times per day equal to this Merit.",
        merit_type="werewolf",
        prerequisite="safe_place:1",
        book="WtF2e 106"
    ),
    Merit(
        name="Lodge Stronghold",
        min_value=2,
        max_value=4,
        description="As a five-dot Safe Place. With four dots, it boasts lines of supernatural defenses or spirit wards.",
        merit_type="werewolf",
        prerequisite="lodge_member",
        book="Pack 81"
    ),
    Merit(
        name="Residential Area",
        min_value=1,
        max_value=5,
        description="Your pack has integrated into an inhabited territory. Every session, by canvassing for help, you can redistribute your dots in this Merit among effective dots of Allies, Contacts and Retainers.",
        merit_type="werewolf",
        prerequisite="",
        book="WtF2e 107"
    ),
    #Mage Locations
    Merit(
        name="Demense",
        min_value=3,
        max_value=3,
        description="Your Sanctum has been prepared as a Demesne, providing a +2 Yantra bonus to appropriate spells, and shielding them from the risk of Paradoxes so long as they're not exposed to Sleepers.",
        merit_type="mage",
        prerequisite="sanctum:1",
        book="MtA2e 104, 242"
    ),
    Merit(
        name="Hallow",
        min_value=1,
        max_value=5,
        description="You've secured a geomantic wellspring of Mana. You can draw out up to your dots in this Merit in points of Mana each day, and the Hallow can store up to three times as many unharvested points as some form of tass.",
        merit_type="mage",
        prerequisite="",
        book="MtA2e 101"
    ),
    Merit(
        name="Sanctum",
        min_value=1,
        max_value=5,
        description="Your secure place is secreted away well enough to insulate your sorcery. Increase your spell control when casting there by your dots in this Merit. You can maintain spells cast beyond your normal spell control this way after leaving the Sanctum.",
        merit_type="mage",
        prerequisite="safe_place:1",
        book="MtA2e 104"
    ),
    #Promethean Locations
    Merit(
        name="Hovel",
        min_value=1,
        max_value=5,
        description="You've crafted a space to acclimate it to your Azoth. Time spent in your Hovel doesn't contribute to Wastelands. You can store a dot of Azoth per dot in this Merit in an item aligned with your element in the Hovel, leaving you with reduced Azoth until you retrieve it from the item.",
        merit_type="promethean",
        prerequisite="safe_place:1",
        book="PtC2e 115"
    ),
    #Changeling Locations
    Merit(
        name="Hollow",
        min_value=1,
        max_value=5,
        description="You've secured a residence within the Hedge, impregnable to outsiders with lesser Wyrd. While in your Hollow, penalize attempts to investigate, track or pursue you by dots in this Merit. Dots of Hollow are also distributed among features listed below.",
        merit_type="changeling",
        prerequisite="",
        book="CtL2e 116"
    ),
    Merit(
        name="Easy Access",
        min_value=3,
        max_value=3,
        description="The Hollow has no fixed entrance, and is instead entered (and later exited) through any unlocked door with Glamour and a small ritual.",
        merit_type="changeling",
        prerequisite="hollow:1",
        book="CtL2e 117"
    ),
    Merit(
        name="Escape Route",
        min_value=1,
        max_value=2,
        description="The Hollow has a secondary exit into the material realm, which with two dots may be accessed from anywhere in the Hollow.",
        merit_type="changeling",
        prerequisite="hollow:1",
        book="CtL2e 116"
    ),
    Merit(
        name="Hidden Entry",
        min_value=2,
        max_value=2,
        description="Penalize rolls to find the Hollow's entrance by -2. When all characters sharing the Hollow are within, the entrance disappears.",
        merit_type="changeling",
        prerequisite="hollow:1",
        book="CtL2e 117"
    ),
    Merit(
        name="Hob Alarm",
        min_value=1,
        max_value=1,
        description="Each story, take one Goblin Debt to preserve a domestic guard of friendly hobs. Ambush in the Hollow does not strip Defense and applies Hollow as bonus dice to actions in the first turn of combat.",
        merit_type="changeling",
        prerequisite="hollow:1,hob_kin:1",
        book="CtL2e 116"
    ),
    Merit(
        name="Home Turf",
        min_value=3,
        max_value=3,
        description="Apply Hollow as a bonus to Initiative and Defense against intruders.",
        merit_type="changeling",
        prerequisite="hollow:1",
        book="CtL2e 117"
    ),
    Merit(
        name="Luxury Goods",
        min_value=1,
        max_value=1,
        description="Once a session, roll Hollow as a dice pool and distribute successes among amenities by Availability or Hedgespun items by rating.",
        merit_type="changeling",
        prerequisite="hollow:1",
        book="CtL2e 116"
    ),
    Merit(
        name="Phantom Phone Booth",
        min_value=1,
        max_value=1,
        description="A magical fixture can make outgoing calls to publically listed numbers outside the Hedge.",
        merit_type="changeling",
        prerequisite="hollow:1",
        book="CtL2e 116"
    ),
    Merit(
        name="Route Zero",
        min_value=1,
        max_value=1,
        description="A one-dot trod passes through the Hollow. It may link allied Hollows, or once a day, may be traversed with a Hedge navigation roll to recover Willpower.",
        merit_type="changeling",
        prerequisite="hollow:1",
        book="CtL2e 116"
    ),
    Merit(
        name="Shadow Garden",
        min_value=1,
        max_value=1,
        description="A plot of soil infinitely replenishes copies of goblin fruit without their magical properties, which only temporarily stave off hunger.",
        merit_type="changeling",
        prerequisite="hollow:1",
        book="CtL2e 116"
    ),
    Merit(
        name="Size Matters",
        min_value=1,
        max_value=2,
        description="The Hollow is large enough to sustain up to six residents, or with two dots, the size of a small town.",
        merit_type="changeling",
        prerequisite="hollow:1",
        book="CtL2e 116"
    ),
    Merit(
        name="Workshop",
        min_value=1,
        max_value=5,
        description="Your Hollow contains space and equipment for an appropriate Crafts Specialty for each dot in this Merit. Apply Workshop as bonus dice to relevant Crafts rolls.",
        merit_type="changeling",
        prerequisite="hollow:1",
        book="CtL2e 120"
    ),
    Merit(
        name="Shared Bastion",
        min_value=1,
        max_value=5,
        description="You or your motley have established a permanent location within dreams, impregnable to outsiders with lesser Wyrd. This merit requires group effort to maintain. While in your Bastion, penalize attempts to investigate, track or pursue you or to manipulate your mind, future, or destiny by dots in this merit.",
        merit_type="changeling",
        prerequisite="",
        book="Hedge 115"
    ),
    Merit(
        name="Buttressed Dreaming",
        min_value=1,
        max_value=1,
        description="Penalize Clash of Wills to force open Bastion by merit rating.",
        merit_type="changeling",
        prerequisite="shared_bastion:1",
        book="Hedge 115"
    ),
    Merit(
        name="Calming Eidolons",
        min_value=1,
        max_value=3,
        description="Reduces Composure dice penalty of Subtle Shifts enacted by the Bastion's owners.",
        merit_type="changeling",
        prerequisite="shared_bastion:1",
        book="Hedge 118"
    ),
    Merit(
        name="Fixed Doorway",
        min_value=3,
        max_value=3,
        description="Door in the Motley's hollow functions as a Gate of Horn leading to and from the Shared Bastion.",
        merit_type="changeling",
        prerequisite="shared_bastion:1,hollow:1",
        book="Hedge 118"
    ),
    Merit(
        name="Guardian Eidolon",
        min_value=1,
        max_value=1,
        description="Spend Willpower to activate the guardian for the scene, gaining immunity to surprise and adding dots in the merit on the first round of an action scene.",
        merit_type="changeling",
        prerequisite="shared_bastion:1",
        book="Hedge 118"
    ),
    Merit(
        name="Illusory Armory",
        min_value=2,
        max_value=2,
        description="Once per chapter, spend glamour to summon an unimportant prop with rating equal to twice glamour spent (max +5). Spend willpower to summon additional props.",
        merit_type="changeling",
        prerequisite="shared_bastion:1",
        book="Hedge 118"
    ),
    Merit(
        name="Motley Awareness",
        min_value=1,
        max_value=3,
        description="At one dot, gain +1 to social roles with other motley members. At three dots, gain an instinctive knowledge of other motley members' moods and the ability to send messages, but use the highest clarity perception penalty of the group.",
        merit_type="changeling",
        prerequisite="shared_bastion:1",
        book="Hedge 119"
    ),
    Merit(
        name="Permanent Armory",
        min_value=1,
        max_value=1,
        description="Maintain mundane real items in shared bastion, or magic items by spending Willpower each chapter.",
        merit_type="changeling",
        prerequisite="shared_bastion:1",
        book="Hedge 118"
    ),
    Merit(
        name="Raised Defenses",
        min_value=1,
        max_value=1,
        description="Whenever any motley mate is in the Shared Bastion, all members double the bonuses against the attacks or circumstances normally granted by the merit.",
        merit_type="changeling",
        prerequisite="shared_bastion:1",
        book="Hedge 118"
    ),
    Merit(
        name="Somnambulation",
        min_value=3,
        max_value=4,
        description="Can use an Eidolon to keep your body from being neglected while you sleep, or slightly more complex tasks with the four-dot version. Require significantly more sleep.",
        merit_type="changeling",
        prerequisite="shared_bastion:1",
        book="Hedge 119"
    ),
    Merit(
        name="Subtle Speech",
        min_value=2,
        max_value=2,
        description="Phantom Eidolons of Motley Members can receive messages, but Changelings with clarity damage might suffer further damage as their sense of reality is befuddled.",
        merit_type="changeling",
        prerequisite="shared_bastion:1",
        book="Hedge 118"
    ),
    Merit(
        name="Stable Trod",
        min_value=1,
        max_value=5,
        description="You've secured a local trod of equal rating. A number of Hollows along the trod up to dots in Stable Trod share an extra one-dot Hollow feature. You may roll Stable Trod as a dice pool once a story to farm extra Glamour goblin fruit from it.",
        merit_type="changeling",
        prerequisite="",
        book="CtL2e 119"
    ),
    #Hunter Locations
    Merit(
        name="Hunter Safe Place",
        min_value=1,
        max_value=5,
        description="A secure site for the hunter that provides a bonus to initiative and a number of features (see below) equal to its dots. A hunter cannot be surprised while in their Safe Place.",
        merit_type="hunter",
        prerequisite="resources:1",
        book="HtV2e 94"
    ),
    Merit(
        name="Anathema",
        min_value=1,
        max_value=1,
        description="The Safe Place is warded against monsters with a specific power, prompting a Wits + Resolve - Safe Place roll on any attempt to break through, becoming Immobilized or Stunned on failure.",
        merit_type="hunter",
        prerequisite="hunter_safe_place:1",
        book="HtV2e 94"
    ),
    Merit(
        name="Arsenal",
        min_value=1,
        max_value=1,
        description="Rolls to clean, fix, or improvise equipment gain +2.",
        merit_type="hunter",
        prerequisite="hunter_safe_place:1",
        book="HtV2e 94"
    ),
    Merit(
        name="Concealed",
        min_value=1,
        max_value=1,
        description="Attempts to find the Safe Place through any means are penalised by -2.",
        merit_type="hunter",
        prerequisite="hunter_safe_place:1",
        book="HtV2e 94"
    ),
    Merit(
        name="Escape Hatch",
        min_value=1,
        max_value=1,
        description="The hunter(s) may roll Dexterity + Athletics or Survival to reach the secret exit without suffering any damage from the environment.",
        merit_type="hunter",
        prerequisite="hunter_safe_place:1",
        book="HtV2e 94"
    ),
    Merit(
        name="Infirmary",
        min_value=1,
        max_value=1,
        description="Medicine rolls here are improved by +2 for any invested hunter with dots in the skill, and the space may substitute for a hospital for the purposes of injury and recovery.",
        merit_type="hunter",
        prerequisite="hunter_safe_place:1",
        book="HtV2e 95"
    ),
    Merit(
        name="Home Security System",
        min_value=1,
        max_value=1,
        description="The Safe Place is outfitted with a defense system, penalising attempts to break in by Safe Place dots.",
        merit_type="hunter",
        prerequisite="hunter_safe_place:1",
        book="HtV2e 95"
    ),
    #Geist Locations
    Merit(
        name="Cenote",
        min_value=1,
        max_value=5,
        description="You tend a ghostly place where Plasm accumulates, at your Merit rating in points per chapter.",
        merit_type="geist",
        prerequisite="safe_place:1",
        book="GtS2e 85"
    ),
    #Mummy Locations
    Merit(
        name="Tomb Geometry",
        min_value=1,
        max_value=5,
        description="Apply this rating as a bonus to meditate upon your Pillars.",
        merit_type="mummy",
        prerequisite="",
        book="MtC2e 206"
    ),
    Merit(
        name="Tomb Perils",
        min_value=1,
        max_value=5,
        description="Your tomb resists intruders with traps totalling this rating, and an equal number of curses from released vessels.",
        merit_type="mummy",
        prerequisite="tomb_geometry:1",
        book="MtC2e 206"
    ),
    Merit(
        name="Tomb Provisions",
        min_value=1,
        max_value=5,
        description="Your tomb is furnished with equipment or infrastructure totalling this rating.",
        merit_type="mummy",
        prerequisite="tomb_geometry:1",
        book="MtC2e 206"
    ),
    #Demon Locations
    Merit(
        name="Bolthole",
        min_value=1,
        max_value=5,
        description="You have a tiny extradimensional realm where time doesn't progress. It's warded against angels, and rolls to find the access point are penalized by its Merit rating. Dots of Bolthole are also distributed among features listed below.",
        merit_type="demon",
        prerequisite="",
        book="DtD 120"
    ),
    Merit(
        name="Arsenal",
        min_value=1,
        max_value=5,
        description="Once per session, your bolthole can supply one weapon with a rating equal to your Arsenal dots, two weapons with a rating one less than your Arsenal dots, and any number of weapons with a rating less than that.",
        merit_type="demon",
        prerequisite="bolthole:1",
        book="DtD 120"
    ),
    Merit(
        name="Cover-Linked",
        min_value=2,
        max_value=2,
        description="Choose one Cover identity. The bolthole only exists while you are in that Cover's form. Anything in the bolthole not provided by these features is lost forever when the bolthole stops existing.",
        merit_type="demon",
        prerequisite="bolthole:1",
        book="DtD 120"
    ),
    Merit(
        name="Easy Access",
        min_value=3,
        max_value=3,
        description="You can reassign the bolthole's entrance by touching a door and spending Aether. Characters still exit the bolthole the way they came in.",
        merit_type="demon",
        prerequisite="bolthole:1",
        book="DtD 121"
    ),
    Merit(
        name="No Twilight",
        min_value=1,
        max_value=1,
        description="Ephemeral beings that enter the bolthole manifest physically.",
        merit_type="demon",
        prerequisite="bolthole:1",
        book="DtD 120"
    ),
    Merit(
        name="Self-Destruct",
        min_value=1,
        max_value=1,
        description="You can implode your bolthole. Anyone inside takes lethal damage equal to your dots in Bolthole and has one turn to leave before the exit to reality is lost.",
        merit_type="demon",
        prerequisite="bolthole:1",
        book="DtD 120"
    ),
    Merit(
        name="Trap Door",
        min_value=2,
        max_value=2,
        description="The entrance from the physical realm into the bolthole only exists when you're outside it, although those capable can still enter from Twilight.",
        merit_type="demon",
        prerequisite="bolthole:1",
        book="DtD 121"
    ),
]

# Create dictionary for easy lookup
location_merits_dict = {merit.name.lower().replace(" ", "_").replace("(", "").replace(")", ""): merit for merit in location_merits}
