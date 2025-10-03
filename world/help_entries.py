"""
File-based help entries. These complements command-based help and help entries
added in the database using the `sethelp` command in-game.

Control where Evennia reads these entries with `settings.FILE_HELP_ENTRY_MODULES`,
which is a list of python-paths to modules to read.

A module like this should hold a global `HELP_ENTRY_DICTS` list, containing
dicts that each represent a help entry. If no `HELP_ENTRY_DICTS` variable is
given, all top-level variables that are dicts in the module are read as help
entries.

Each dict is on the form
::

    {'key': <str>,
     'text': <str>}``     # the actual help text. Can contain # subtopic sections
     'category': <str>,   # optional, otherwise settings.DEFAULT_HELP_CATEGORY
     'aliases': <list>,   # optional
     'locks': <str>       # optional, 'view' controls seeing in help index, 'read'
                          #           if the entry can be read. If 'view' is unset,
                          #           'read' is used for the index. If unset, everyone
                          #           can read/view the entry.

"""

HELP_ENTRY_DICTS = [
    {
        "key": "evennia",
        "aliases": ["ev"],
        "category": "General",
        "locks": "read:perm(Developer)",
        "text": """
            Evennia is a MU-game server and framework written in Python. You can read more
            on https://www.evennia.com.

            # subtopics

            ## Installation

            You'll find installation instructions on https://www.evennia.com.

            ## Community

            There are many ways to get help and communicate with other devs!

            ### Discussions

            The Discussions forum is found at https://github.com/evennia/evennia/discussions.

            ### Discord

            There is also a discord channel for chatting - connect using the
            following link: https://discord.gg/AJJpcRUhtF

        """,
    },
    {
        "key": "legacy",
        "aliases": ["legacies", "mage legacy"],
        "category": "Character Creation",
        "text": """
            |wMage: The Awakening - Legacy System|n

            Legacies are specialized magical practices that Mages can join based on their
            Path or Order. Each Legacy represents a unique approach to the Supernal World.

            |wSetting Your Legacy:|n
            Use: |c+stat legacy=<legacy name>|n

            Your character must have the appropriate Path or Order to take a Legacy.
            Some Legacies are "Unlinked" and available to any Mage.

            # Path-Based Legacies

            ## Acanthus Path
            Chronologue, House of Ariadne, Awakening Gambit, Blank Badge, 
            Carnival Melancholy, Pygmalion Society, Sisterhood of the Blessed, 
            Storm Keepers, Walkers in Mists

            ## Mastigos Path
            Intendants of the Building, Logophages, Nagaraja, Reality Stalkers,
            Bearers of the Eternal Voice, Bene Ashmedai, Brotherhood of the Demon Wind,
            Clavicularius, Cryptologos, Parliament of the Needle, Subtle Ones

            ## Moros Path
            Eleventh Question, Kitchen Alchemists, Nighthawks, Stone Scribes,
            Bokor, Forge Masters, Uncrowned Kings, Votaries of the Ordained, Legion

            ## Obrimos Path
            Illumined Path, Perfected Adepts, Shapers of the Invisible, Tyrian Archons,
            Daksha, Echowalkers, Tamers of Fire, Thrice-Great, Transhuman Engineers

            ## Thyrsus Path
            Engineers of the System, Keepers of the Covenant, Chrysalides, Dreamspeakers,
            Gilgamesh's Lions, Orphans of Proteus, Tamers of Blood

            # Order-Based Legacies

            ## Adamantine Arrow
            Perfected Adepts, Awakening Gambit, Brotherhood of the Demon Wind,
            Devourers of the Flesh, Hunters of the Golden Wing, Votaries of the Ordained

            ## Free Council
            Blank Badge, Cryptologos, Dreamspeakers, Parliament of the Needle,
            Transhuman Engineers

            ## Guardians of the Veil
            Eleventh Question, House of Ariadne, Bearers of the Eternal Voice,
            Subtle Ones, Votaries of the Ordained, Legion

            ## Mysterium
            Eleventh Question, Logophages, Reality Stalkers, Stone Scribes,
            Cryptologos, Daksha, Walkers in Mists

            ## Silver Ladder
            Illumined Path, Keepers of the Covenant, Logophages, Nighthawks,
            Bene Ashmedai, Carnival Melancholy, Clavicularius, Sisterhood of the Blessed,
            Thrice-Great

            ## Seers of the Throne
            Chronologue, Engineers of the System, House of Ariadne, Tyrian Archons,
            Architects of the Future, Bene Ashmedai, Chrysalides, Clavicularius,
            Cryptologos, Secret Order of the Gate

            ## Tremere
            House Nagaraja, House Seo Hel, House Thrax, House Vedmak

            ## Abyssal
            Hand of Destiny, Keepers of the Chrysalis

            # Unlinked Legacies

            These Legacies are available to any Mage, regardless of Path or Order:

            Archimandrite, Aurora Auricalcinae, Bull's Children, Celestial Masters,
            Emergent, Fallen Pillar, Filiae Philosopharum, Hollow Keepers,
            Lords of Mars, Singers in Silence, Skalds, Sphinxes, Tamers of the Cave,
            Tamers of the Winds, Tephra, Thread-Cutters, Timori, Torches of Artemis,
            Wind-Singers

            |wExamples:|n
            +stat path=Obrimos
            +stat order=Adamantine Arrow
            +stat legacy=Perfected Adepts    (Valid - accessible by both Obrimos and Adamantine Arrow)
            +stat legacy=Archimandrite       (Valid - Unlinked Legacy)
            +stat legacy=Chronologue         (Invalid for Obrimos/Adamantine Arrow)

            |wNote:|n You must set your Path and/or Order before setting a Legacy.
            If you attempt to set an invalid Legacy, the system will show you which
            Paths and Orders qualify for that Legacy.

        """,
    },
    {
        "key": "athanor",
        "aliases": ["athanors", "promethean athanor"],
        "category": "Character Creation",
        "text": """
            |wPromethean: The Created - Athanor System|n

            Athanors are the spiritual engines that drive a Promethean's Pilgrimage toward
            humanity. Each Lineage has access to specific Athanors that reflect their 
            unique approach to the Great Work.

            |wSetting Your Athanor:|n
            Use: |c+stat athanor=<athanor name>|n

            Your character must have the appropriate Lineage to take an Athanor.

            # Athanors by Lineage

            ## Frankenstein Lineage
            Basilisk, Caladrius, Griffon, Lion, Manticore

            ## Galatea Lineage
            Dove, Gorgon, Unicorn, Seraph, Swan

            ## Osiris Lineage
            Ant, Eel, Dragon, Eagle, Honeybee, Owl, Scorpion, Sphinx

            ## Tammuz Lineage
            Cerberus, Crab, Humbaba, Pelican, Phoenix

            ## Ulgan Lineage
            Chimera, Crane, Dragon, Fox, La Llorona, Raven, Salamander, Toad

            ## Unfleshed Lineage
            Caucasian Eagle, Chi Wiou, Golden Maiden

            ## Zeka Lineage
            Cockroach, Machine

            |wExamples:|n
            +stat lineage=Frankenstein
            +stat athanor=Basilisk         (Valid - Frankenstein can take Basilisk)
            +stat athanor=Lion             (Valid - Frankenstein can take Lion)
            +stat athanor=Dove             (Invalid - Dove is for Galatea, not Frankenstein)

            |wNote:|n You must set your Lineage before setting an Athanor.
            If you attempt to set an invalid Athanor, the system will show you which
            Lineages qualify for that Athanor.

            |wAbout Athanors:|n
            Athanors represent the spiritual furnace that refines a Promethean's Azoth
            and drives their transformation. Each Athanor is associated with symbolic
            animals or concepts that embody different aspects of the Great Work. The
            choice of Athanor affects how a Promethean approaches their journey toward
            humanity and the specific challenges they face along the Pilgrimage.

        """,
    },
    {
        "key": "transmutations",
        "aliases": ["alembics", "promethean powers", "bestowments"],
        "category": "Character Creation",
        "text": """
            |wPromethean: The Created - Transmutations & Alembics|n

            Prometheans possess supernatural powers called Transmutations, which are organized
            into categories (like Alchemicus, Corporeum, Electrification, etc.). Within each
            Transmutation category are individual Alembics - specific powers that are purchased
            individually, not as dots in a category.

            |wSetting Alembics:|n
            Use: |c+stat alembic=<alembic name>|n

            Alembics use underscore naming (e.g., "human_flesh" not "Human Flesh")

            |wSetting Bestowments:|n
            Use: |c+stat bestowment=<bestowment name>|n

            # Transmutations

            Prometheans learn individual Alembics from the following Transmutation categories:

            ## Alchemicus
            Mastery over matter and transformation
            - Stone Distillation: purification, fortification, transformation
            - Aqua Regia Distillation: decay, degradation, dissolution
            - Spagyria Distillation: temperature_modification, alteration, resize
            - Elixir Distillation: apprentices_brooms, spark_of_life, flesh_to_stone

            ## Benefice
            Powers of the Throng (cooperative powers)
            - Command, Consortium, Control, Community Distillations
            - Enables throng teamwork and shared abilities

            ## Contamination
            Powers of emotional and social corruption
            - Indulgence, Leverage, Madness, Suffering Distillations
            - Manipulate Vices, secrets, mental states, and pain

            ## Corporeum
            Physical enhancement and athletic prowess
            - Charites, Zephyrus, Hygeius, Motus Distillations
            - Enhance Dexterity, Speed, Defense, and physical resilience

            ## Deception
            Powers of concealment and disguise
            - Anonymity, Assimilation, Doppelganger, Stalker Distillations
            - Blend in, impersonate, hide, and stalk

            ## Disquietism
            Mastery over Disquiet and Flux
            - Externalize, Internalize, Redirect, Weaponize Distillations
            - Control the dread that Prometheans inspire

            ## Electrification
            Control over electricity and lightning
            - Machinus, Arc, Oscillitus, Imperatus Distillations
            - Sense, generate, and manipulate electrical energy

            ## Flux
            Dark powers of the Wasteland (dangerous)
            - Blight, Cannibalize, Lordship, Mutation, Solvent, Unleash
            - Powers that draw on corruption and Pandoran essence

            ## Luciferus
            Powers of radiance and inspiration
            - Solar Flare, Morning Star, Blaze of Glory, Beacon of Helios
            - Inspire, dazzle, and lead through inner fire

            ## Metamorphosis
            Shapeshifting and physical transformation
            - Aptare, Bestiae Facies, Tegere, Verto Distillations
            - Adapt body, grow natural weapons, harden skin

            ## Mesmerism
            Powers of emotional manipulation
            - Phobos (fear), Eros (desire), Eris (confusion), Penthos (sorrow)
            - Evoke powerful emotions in others

            ## Saturninus
            Powers of Azothic memory and Pyros
            - Heed the Call, Plumb the Fathoms, Stoke the Furnace, Prime the Vessel
            - Connect to the collective Promethean experience

            ## Sensorium
            Enhanced senses and perception
            - Vitreous Humour, Receptive Humour, Stereo Humour, Somatic Humour
            - See in darkness, sense auras, hear thoughts, enhanced smell/taste

            ## Spiritus
            Powers against supernatural threats
            - Clades, Clupeum, Veritas, Laruae Distillations
            - Defend against and understand the supernatural

            ## Vitality
            Powers of endurance and strength
            - Unbowed, Unbroken, Unconquered, Unfettered Distillations
            - Increase Resolve, Stamina, and Strength; resist control

            ## Vulcanus
            Powers of the Divine Fire
            - Cauterio, Ignus Aspiratus, Mutatus Aspiratus, Sanctus Aspiratus
            - Brand, ignite, sense Flux, manipulate Pyros

            # Bestowments

            Bestowments are unique gifts tied to a Promethean's Lineage:
            - Spare Parts, Titan's Strength, Symbiotic Muse, Unearthly Mien
            - Corpse Tongue, Revivification, Heart of Clay, Inscription
            - Ephemeral Flesh, Twilight Fluidity, Heart of Steel
            - Soul is in the Software, Big Brother, The Void, Half-Life
            - Crucible of Anguish, Chem-Shell, Living Wall, Bloody Feast
            - Vice Eater, Blood Offering

            |wExamples:|n
            +stat alembic=human_flesh        (Corporeum - Hygeius Distillation)
            +stat alembic=purification       (Alchemicus - Stone Distillation)
            +stat alembic=spark              (Electrification - Arc Distillation)
            +stat bestowment=spare_parts     (Bestowment)
            +stat bestowment=titans_strength (Bestowment)

            |wNote:|n Alembics are individual powers, not dots. You either know an Alembic or you don't.
            This is similar to how Changeling Contracts work.

            |wReference:|n For full details on each Alembic's mechanics, see:
            https://codexofdarkness.com/wiki/Transmutations

        """,
    },
]
