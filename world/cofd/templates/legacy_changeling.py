"""
Legacy Changeling Template Definition for Chronicles/World of Darkness 1st Edition.
Changeling: The Lost template adapted for 1st edition mechanics.
"""

from . import register_template

# Valid seemings for Legacy Changeling characters (1st edition)
LEGACY_CHANGELING_SEEMINGS = [
    "beast", "darkling", "elemental", "fairest", "ogre", "wizened"
]

BEAST_KITHS = [
    "hunterheart", "skitterskulk", "steepscrambler", "venombite", "windwing", "truefriend",
]

DARKLING_KITHS = [
    "shadowsoul", "tunnelgrub", "leechfinger", "gravewight", "mirrorskin", "razorhand",
]

ELEMENTAL_KITHS = [
    "airtouched", "earthbones", "fireheart", "manikin", "snowskin", "waterskin",
]

FAIREST_KITHS = [
    "flowering", "bright one", "dancer", "draconic", "muse", "telluric",
]

OGRE_KITHS = [
    "gargantuan", "render", "stonebones", "watersense", "witchtooth", "bloodbrute",
]

WIZENED_KITHS = [
    "artisan", "brewer", "chatelaine", "chirurgeon", "oracle", "soldier",
]
# Valid courts for Legacy Changeling characters (1st edition)
LEGACY_CHANGELING_COURTS = [
    "spring", "summer", "autumn", "winter", "courtless", "dawn", "day", "dusk", "night"
]

# Valid contracts for 1st edition changelings (simplified list)
LEGACY_CHANGELING_CONTRACTS = [
    # Universal Contracts
    "dream", "hearth", "mirror", "smoke", "artifice",
    # Court Contracts
    "spring", "summer", "autumn", "winter",
    # Seeming Contracts
    "fang_and_talon", "darkness", "elements", "vainglory", "stone", "artifice",
    # Goblin Contracts
    "goblin_contracts"
]

# Legacy Changeling template definition
LEGACY_CHANGELING_TEMPLATE = {
    "name": "legacy_changeling",
    "display_name": "Changeling (Legacy)",
    "description": ("Legacy Changeling template for World of Darkness 1st Edition. "
                   "Changelings are humans who were taken to Arcadia and transformed by the Fae. "
                   "Uses traditional virtue/vice system and 1st edition mechanics."),
    "bio_fields": ["seeming", "kith", "court", "motley", "keeper"],
    "integrity_name": "Clarity",
    "starting_integrity": 7,
    "supernatural_power_stat": "wyrd",
    "starting_power_stat": 1,
    "resource_pool": "glamour",
    "power_systems": LEGACY_CHANGELING_CONTRACTS,
    "anchors": ["virtue", "vice"],  # Legacy uses virtue/vice only
    "merit_categories": ["physical", "social", "mental", "supernatural", "fighting", "style", "changeling"],
    "field_validations": {
        "seeming": {
            "valid_values": LEGACY_CHANGELING_SEEMINGS
        },
        "court": {
            "valid_values": LEGACY_CHANGELING_COURTS
        }
    },
    "legacy_mode": True,  # Flag to indicate this is a legacy template
    "version": "1.0",
    "author": "Chronicles of Darkness Legacy",
    "game_line": "Changeling: The Lost (1st Edition)",
    "notes": "Legacy Changeling template for World of Darkness 1st Edition mechanics with virtue/vice anchors"
}

# Register the template
register_template(LEGACY_CHANGELING_TEMPLATE)
