"""
Changeling Template Definition for Chronicles of Darkness.
Changeling: The Lost template with Seeming, Court, and Kith validations.
"""

from . import register_template

# Valid seemings for Changeling characters
CHANGELING_SEEMINGS = [
    "beast", "darkling", "elemental", "fairest", "ogre", "wizened"
]

# Valid courts for Changeling characters  
CHANGELING_COURTS = [
    "spring", "summer", "autumn", "winter", "courtless", 
    "dawn", "day", "dusk", "night"
]

# Valid kiths for Changeling characters (extensive list)
CHANGELING_KITHS = [
    # Darkling kiths
    "shadowsoul", "tunnelgrub", "leechfinger", "gravewight", "mirrorskin", "razorhand",
    # Beast kiths
    "hunterheart", "skitterskulk", "steepscrambler", "venombite", "windwing", "truefriend",
    # Elemental kiths  
    "airtouched", "earthbones", "fireheart", "manikin", "snowskin", "waterskin",
    # Fairest kiths
    "flowering", "bright one", "dancer", "draconic", "muse", "telluric",
    # Ogre kiths
    "gargantuan", "render", "stonebones", "watersense", "witchtooth", "bloodbrute",
    # Wizened kiths
    "artifice", "brewer", "chatelaine", "chirurgeon", "oracle", "soldier"
]

# Valid changeling contracts
CHANGELING_CONTRACTS = [
    "artifice", "autumn", "board", "communion", "darkness", "den", "dream", "elements",
    "fang and talon", "fleeting", "forge", "hearth", "hours", "lucidity", "mirror",
    "moon", "omen", "reflection", "shade and spirit", "smoke", "spring", "stone",
    "summer", "sword", "thorns and brambles", "trade", "vainglory", "wild", "winter"
]

# Changeling template definition
CHANGELING_TEMPLATE = {
    "name": "changeling",
    "display_name": "Changeling", 
    "description": ("Changelings are humans who were taken to the realm of the True Fae and "
                   "transformed, eventually escaping back to the mortal world. They are organized "
                   "by their Seemings (what they became) and Courts (seasonal affiliations)."),
    "bio_fields": ["needle", "thread", "seeming", "court", "kith", "keeper", "motley"],
    "integrity_name": "Clarity",
    "starting_integrity": 7,
    "supernatural_power_stat": "wyrd",
    "starting_power_stat": 1,
    "resource_pool": "glamour",
    "power_systems": CHANGELING_CONTRACTS,
    "anchors": ["needle", "thread"],
    "merit_categories": ["physical", "social", "mental", "supernatural", "fighting", "style", "changeling"],
    "field_validations": {
        "seeming": {
            "valid_values": CHANGELING_SEEMINGS
        },
        "court": {
            "valid_values": CHANGELING_COURTS
        },
        "kith": {
            "valid_values": CHANGELING_KITHS
        }
    },
    "version": "2.0",
    "author": "Chronicles of Darkness",
    "game_line": "Changeling: The Lost",
    "notes": "Enhanced Changeling template with Wyrd, Contracts, and Glamour pool"
}

# Register the template
register_template(CHANGELING_TEMPLATE) 