"""
Demon: The Descent Template Definition for Chronicles of Darkness.
Demons are fallen angels who have escaped from the God-Machine's control.
"""

from . import register_template

# Valid demon incarnations
DEMON_INCARNATIONS = [
    "destroyer", "guardian", "messenger", "psychopomp"
]

# Valid demon agendas
DEMON_AGENDAS = [
    "inquisitor", "integrator", "saboteur", "tempter"
]

# Valid demon catalysts
DEMON_CATALYSTS = [
    "abandonment", "betrayal", "destruction", "fear", "guilt", "memory", "withdrawal"
]

# Valid demon embeds
DEMON_EMBEDS = [
    "acceleration", "authenticate", "decrypt", "download", "enhance", "firewall", "overclock", "search"
]

# Valid demon exploits
DEMON_EXPLOITS = [
    "backdoor", "ghost in the machine", "kill process", "modify", "reboot", "spam", "system restore", "total corruption"
]

# Demon template definition
DEMON_TEMPLATE = {
    "name": "demon",
    "display_name": "Demon",
    "description": "Demons are fallen angels who have escaped from the God-Machine's control and now struggle to maintain their human identities.",
    "bio_fields": ["virtue", "vice", "incarnation", "agenda", "catalyst", "ring", "cover_identity"],
    "integrity_name": "Cover",
    "starting_integrity": 7,
    "supernatural_power_stat": "primum",
    "starting_power_stat": 1,
    "resource_pool": "aether",
    "power_systems": DEMON_EMBEDS + DEMON_EXPLOITS,
    "anchors": ["virtue", "vice"],
    "merit_categories": ["physical", "social", "mental", "supernatural", "fighting", "style", "demon"],
    "field_validations": {
        "incarnation": {
            "valid_values": DEMON_INCARNATIONS
        },
        "agenda": {
            "valid_values": DEMON_AGENDAS
        },
        "catalyst": {
            "valid_values": DEMON_CATALYSTS
        }
    },
    "version": "2.0",
    "author": "Chronicles of Darkness",
    "game_line": "Demon: The Descent",
    "notes": "Enhanced Demon template with Primum, Embeds, Exploits, and Aether pool"
}

# Register the template
register_template(DEMON_TEMPLATE) 