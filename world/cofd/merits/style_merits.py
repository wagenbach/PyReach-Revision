from world.cofd.stat_types import Merit

# Style-Specific Merits
style_merits = [
    #Mental Styles
    Merit(
        name="Professional Training",
        min_value=1,
        max_value=5,
        description="Style. You have skills and connections related to a chosen profession.",
        merit_type="style",
        prerequisite="",
        book="CofD 46"
    ),
    Merit(
        name="Unintended Applications",
        min_value=1,
        max_value=5,
        description="Style. You have learned a good number of tricks when it comes to applying science creatively.",
        merit_type="style",
        prerequisite="wits:3,[crafts:3,science:3]",
        book="DSG 95"
    ),
    #Physical Styles
    Merit(
        name="Aggressive Driving",
        min_value=1,
        max_value=4,
        description="Style. Any vehicle can become a weapon when your character is behind the wheel.",
        merit_type="style",
        prerequisite="resolve:3,drive:3,fast_reflexes:3",
        book=""
    ),
    Merit(
        name="Drone Control",
        min_value=1,
        max_value=3,
        description="Style. Your character knows how to operate weapons systems via remote.",
        merit_type="style",
        prerequisite="intelligence:3,computer:3,drive:2",
        book="HL 56"
    ),
    Merit(
        name="Falconry",
        min_value=1,
        max_value=4,
        description="Style. You have learned to reflexively issue commands to trained birds of prey.",
        merit_type="style",
        prerequisite="wits:3,animal_ken:3,bonded",
        book="HL 48"
    ),
    Merit(
        name="K-9",
        min_value=1,
        max_value=4,
        description="Style. These maneuvers allow you to issue commands to a trained dog Size 3 or larger.",
        merit_type="style",
        prerequisite="wits:3,animal_ken:3,bonded",
        book="HL 49"
    ),
    Merit(
        name="Parkour",
        min_value=1,
        max_value=5,
        description="Style. You are trained in the graceful art of freerunning.",
        merit_type="style",
        prerequisite="dexterity:3,athletics:2",
        book="CofD 48"
    ),
    Merit(
        name="Stunt Driver",
        min_value=1,
        max_value=4,
        description="Style. Your character is an expert behind the wheel and can push a vehicle beyond normal limits.",
        merit_type="style",
        prerequisite="dexterity:3,drive:3,wits:3",
        book="CofD 49"
    ),
    #Social Styles
    Merit(
        name="Etiquette",
        min_value=1,
        max_value=5,
        description="Style. Your character knows their way around society, customs, and traditions.",
        merit_type="style",
        prerequisite="composure:3,socialize:2",
        book="VtR2e 120"
    ),
    Merit(
        name="Fast-Talking",
        min_value=1,
        max_value=5,
        description="Style. Your character is able to talk circles around listeners.",
        merit_type="style",
        prerequisite="manipulation:3,subterfuge:2",
        book="CofD 50"
    ),
    #The Published Mystery Cults are all listed in restricted_merits.py
    Merit(
        name="Mystery Cult Initiation",
        min_value=1,
        max_value=5,
        description="Style. You joined a cult. Decide your cult's guiding purpose, source of power, and cultic doctrine.",
        merit_type="style",
        prerequisite="",
        book="CofD 51"
    ),
    Merit(
        name="Scorpion Cult Initiation",
        min_value=1,
        max_value=5,
        description="Style. You have joined a cult in thrall to the Deathless of ancient Irem.",
        merit_type="style",
        prerequisite="",
        book="MtC2e 114"
    ),
    #Fighting Styles
    Merit(
        name="Armed Defense",
        min_value=1,
        max_value=5,
        description="Style. You're able to use a weapon to stop people from trying to kill you.",
        merit_type="style",
        prerequisite="dexterity:3,weaponry:2,defensive_combat:1",
        book="CofD 60"
    ),
    Merit(
        name="Avoidance",
        min_value=1,
        max_value=4,
        description="Style. Your characters only goal in a fight is to not get hurt.",
        merit_type="style",
        prerequisite="manipulation:3,athletics:2,stealth:2",
        book="HL 46"
    ),
    Merit(
        name="Berserker",
        min_value=1,
        max_value=3,
        description="Style. Your character enters a controlled madness in combat.",
        merit_type="style",
        prerequisite="strength:3,iron stamina:3",
        book="HL 46"
    ),
    Merit(
        name="Bowmanship",
        min_value=1,
        max_value=4,
        description="Style. Your character is a patient hunter with a bow.",
        merit_type="style",
        prerequisite="dexterity:3,firearms:2,trained_observer:1",
        book="HL 47"
    ),
    Merit(
        name="Boxing",
        min_value=1,
        max_value=5,
        description="Style. Your character is trained in one of the many styles of fist-fighting that make up the sweet science.",
        merit_type="style",
        prerequisite="strength:2,dexterity:2,stamina:2,brawl:2,athletics:2",
        book="HL 47"
    ),
    Merit(
        name="Brute Force",
        min_value=1,
        max_value=5,
        description="Style. Your character embraces the devastating monster within their huge form.",
        merit_type="style",
        prerequisite="strength:3,brawl:2,size>=5",
        book="PtC2e 112"
    ),
    Merit(
        name="Chain Weapons",
        min_value=1,
        max_value=2,
        description="Style. Your character knows how to use a length of chain as a weapon.",
        merit_type="style",
        prerequisite="strength:3,dexterity:3,athletics:2,weaponry:2",
        book="HL 48"
    ),
    Merit(
        name="Close Quarters Combat",
        min_value=1,
        max_value=5,
        description="Style. Your character knows the art of using the environment to hurt people.",
        merit_type="style",
        prerequisite="wits:3,athletics:2,brawl:3",
        book="CofD 61"
    ),
    Merit(
        name="Combat Archery",
        min_value=1,
        max_value=5,
        description="Style. Your character uses a bow for rapid draws that riddle opponents with arrows.",
        merit_type="style",
        prerequisite="strength:3,athletics:2,quick_draw:1",
        book="HL 48"
    ),
    Merit(
        name="Disabling Tactics",
        min_value=1,
        max_value=3,
        description="Style. Your character has training in disabling opponents.",
        merit_type="style",
        prerequisite="strength:3,weaponry:2",
        book="DE 247"
    ),
    Merit(
        name="Firefight",
        min_value=1,
        max_value=3,
        description="Style. You are comfortable with a gun and it's use in a stressful situation.",
        merit_type="style",
        prerequisite="composure:3,dexterity:3,athletics:2,firearms:2",
        book="CofD 61"
    ),
    Merit(
        name="Grappling",
        min_value=1,
        max_value=5,
        description="Style. Your character is trained in wrestling or one of many other grappling martial arts. ",
        merit_type="style",
        prerequisite="stamina:3,strength:2,athletics:2,brawl:2",
        book="CofD 62, HL 49"
    ),
    Merit(
        name="Gunslinger",
        min_value=1,
        max_value=5,
        description="Style. Your character is trained in performing rapid fire trick shots.",
        merit_type="style",
        prerequisite="wits:3,firearms:3,revolvers",
        book="DE2 377"
    ),
    Merit(
        name="Heavy Weapons",
        min_value=1,
        max_value=5,
        description="Style. Your character is trained in using heavy two handed melee weapons.",
        merit_type="style",
        prerequisite="stamina:3,strength:3,athletics:2,weaponry:2",
        book="CofD 62"
    ),
    Merit(
        name="Improvised Weaponry",
        min_value=1,
        max_value=3,
        description="Style. Your character is trained to use whatever they can grab as a weapon.",
        merit_type="style",
        prerequisite="wits:3,weaponry:1",
        book="CofD 62"
    ),
    Merit(
        name="Kino Mutai",
        min_value=1,
        max_value=1,
        description="Style. Your character is trained to target soft tissue with bites and gouges.",
        merit_type="style",
        prerequisite="dexterity:2,resolve:3,brawl:2",
        book="HL 50"
    ),
    Merit(
        name="Light Weapons",
        min_value=1,
        max_value=5,
        description="Style. Your character is trained in the use of light, one-handed weapons.",
        merit_type="style",
        prerequisite="[wits:3,fighting_finesse:1],dexterity:3,athletics:2,weaponry:2",
        book="CofD 63"
    ),
    Merit(
        name="Marksmanship",
        min_value=1,
        max_value=4,
        description="Style. You are trained at disciplined and patient rifle use.",
        merit_type="style",
        prerequisite="composure:3,resolve:3,firearms:2",
        book="CofD 63"
    ),
    Merit(
        name="Martial Arts",
        min_value=1,
        max_value=5,
        description="Style. This represents training in a variety of strike based martial arts.",
        merit_type="style",
        prerequisite="resolve:3,dexterity:3,athletics:2,brawl:2",
        book="CofD 63, HL 50"
    ),
    Merit(
        name="Mounted Combat",
        min_value=1,
        max_value=4,
        description="Style. You are trained to fight from horseback.",
        merit_type="style",
        prerequisite="dexterity:3,athletics:2,animal_ken:3",
        book="HL 51"
    ),
    Merit(
        name="Police Tactics",
        min_value=1,
        max_value=3,
        description="Style. Your character is trained in restraint techniques common among law enforcement.",
        merit_type="style",
        prerequisite="brawl:2,weaponry:1",
        book="CofD 64"
    ),
    Merit(
        name="Powered Projectile",
        min_value=1,
        max_value=4,
        description="Style. Your character has trained to use crossbows and slings in combat.",
        merit_type="style",
        prerequisite="dexterity:3,athletics:2,firearms:2",
        book="HL 51"
    ),
    Merit(
        name="Relentless Assault",
        min_value=1,
        max_value=5,
        description="Style. Your character fights with complete abandon.",
        merit_type="style",
        prerequisite="strength:3,stamina:3,brawl:2",
        book="WtF2e 109"
    ),
    Merit(
        name="Spear and Bayonet",
        min_value=1,
        max_value=3,
        description="Style. Your character is trained to fight with long pointed weapons.",
        merit_type="style",
        prerequisite="strength:3,dexterity:2,weaponry:2",
        book="HL 51"
    ),
    Merit(
        name="Staff Fighting",
        min_value=1,
        max_value=4,
        description="Style. Your character has trained to defend themselves with a staff.",
        merit_type="style",
        prerequisite="strength:2,dexterity:3,weaponry:2",
        book="HL 51"
    ),
    Merit(
        name="Street Fighting",
        min_value=1,
        max_value=5,
        description="Style. Your character learned to fight with their bare hands on the street.",
        merit_type="style",
        prerequisite="stamina:3,composure:3,brawl:2,streetwise:2",
        book="CofD 65"
    ),
    Merit(
        name="Strength Performance",
        min_value=1,
        max_value=4,
        description="Style. Your character has specifically trained in lifting, pushing, and pulling enormous weight.",
        merit_type="style",
        prerequisite="strength:3,stamina:2,athletics:2",
        book="HL 52"
    ),
    Merit(
        name="Systema",
        min_value=1,
        max_value=3,
        description="Style. Your character has learned to move with exceptional suppleness, rolling with blows and obstacles.",
        merit_type="style",
        prerequisite="dexterity:3,athletics:3,wits:2",
        book="HL 52"
    ),
    Merit(
        name="Thrown Weapons",
        min_value=1,
        max_value=2,
        description="Style. Your character is adept at throwing knives, darts, throwing stars and tomahawks among other small weapons.",
        merit_type="style",
        prerequisite="dexterity:3,athletics:2,quick_draw:1",
        book="HL 52"
    ),
    Merit(
        name="Two Weapon Fighting",
        min_value=1,
        max_value=4,
        description="Style. Your character has trained in wielding two melee weapons at the same time.",
        merit_type="style",
        prerequisite="wits:3,weaponry:3,fighting_finesse:1",
        book="HL 53"
    ),
    Merit(
        name="Unarmed Defense",
        min_value=1,
        max_value=5,
        description="Style. Your character has adapted to defending themselves while unarmed.",
        merit_type="style",
        prerequisite="dexterity:3,brawl:2,defensive_combat:1",
        book="CofD 65"
    ),
    Merit(
        name="Weapon and Shield",
        min_value=1,
        max_value=4,
        description="Style. Your character is skilled at using a weapon in one hand and a shield in the other.",
        merit_type="style",
        prerequisite="strength:3,stamina:3,weaponry:2",
        book="HL 53"
    ),
]

# Create dictionary for easy lookup
style_merits_dict = {merit.name.lower().replace(" ", "_").replace("(", "").replace(")", ""): merit for merit in style_merits}
