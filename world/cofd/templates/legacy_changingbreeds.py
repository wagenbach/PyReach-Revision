"""
Legacy Changing Breeds from World of Darkness 1st Edition. This currently includes
a list of explicit and specific breeds based on the examples referenced in the book
Changing Breeds: World of Darkness. This is not to be used with the 2nd edition version
of Chronicles of Darkness/God Machine Chronicle.
"""

from . import register_template

# Legacy Changing Breeds List (all 51 breeds)
LEGACY_CHANGING_BREEDS = [
    # Werecats (Bastet)
    "rajanya", "bubasti", "hatara", "bahgrasha", "balam", "cait_sith", "qualmi", "klinerash",
    
    # Megafauna
    "azubuike", "jhaa", "mhole_rho", "iravati",
    
    # Small Shifters
    "minjur", "baitu", "archunen", "reynardi", "mistai", "wapathemwa",
    
    # Canines
    "maerans", "riantes", "warrigal",
    
    # Primates
    "hanumani_brahmin", "sun_wukong", "abathaki", "tothian", "babi_ahsh", "hugranjah",
    
    # Arachnids (Spiders)
    "nanekisu", "carapache", "chi_hsu", "sicarius",
    
    # Ursines (Bears)
    "yonah", "nanuq", "storm_bear",
    
    # Ungulates (Hoofed Animals)
    "uchchaihshravi", "alces", "flidaisin", "takuskansa",
    
    # Avians (Birds and Bats)
    "gente_alada", "corvians", "chevalier_rapace", "vagahuir", "strigoi", "brythian",
    
    # Shadow Breeds
    "whiskey_croc", "mendeans", "olutakami", "kinno_balo", "melusinae", "mimma_lemnua", "yumni"
]

# Changing Breed Categories (Nahual types)
CHANGING_BREED_CATEGORIES = {
    "bastet": ["rajanya", "bubasti", "hatara", "bahgrasha", "balam", "cait_sith", "qualmi", "klinerash"],
    "land_titans": ["azubuike", "jhaa", "mhole_rho", "iravati"],
    "laughing_strangers": ["minjur", "baitu", "archunen", "reynardi", "mistai", "wapathemwa"],
    "the_pack": ["maerans", "riantes", "warrigal"],
    "royal_apes": ["hanumani_brahmin", "sun_wukong", "abathaki", "tothian", "babi_ahsh", "hugranjah"],
    "spinner_kin": ["nanekisu", "carapache", "chi_hsu", "sicarius"],
    "ursara": ["yonah", "nanuq", "storm_bear"],
    "wind_runners": ["uchchaihshravi", "alces", "flidaisin", "takuskansa"],
    "wing_folk": ["gente_alada", "corvians", "chevalier_rapace", "vagahuir", "strigoi", "brythian"],
    "shadow_breeds": ["whiskey_croc", "mendeans", "olutakami", "kinno_balo", "melusinae", "mimma_lemnua", "yumni"]
}

# Accords (where human nature meets animal instinct)
CHANGING_BREED_ACCORDS = [
    "den_warder",      # Loyal, nurturing, protective (Respect: Loyalty)
    "heart_ripper",    # Ferocious, voracious, implacable (Respect: Ferocity)
    "root_weaver",     # Clever, inventive, imaginative (Respect: Cleverness)
    "sun_chaser",      # Devious, passionate, tricky (Respect: Passion)
    "wind_dancer"      # Flighty, inquisitive, uncanny (Respect: Insight)
]

# Accord Specialty Skills (each accord gets 1 free specialty from these)
ACCORD_SPECIALTIES = {
    "den_warder": ["empathy", "medicine", "survival"],
    "heart_ripper": ["brawl", "intimidation", "subterfuge"],
    "root_weaver": ["academics", "crafts", "science"],
    "sun_chaser": ["athletics", "expression", "socialize"],
    "wind_dancer": ["investigation", "occult", "stealth"]
}

# Respect types (social advantage tied to accord)
RESPECT_TYPES = [
    "cleverness",  # Root-Weaver: Cunning and intelligent
    "ferocity",    # Heart-Ripper: Fierce and dangerous
    "insight",     # Wind-Dancer: Wise and perceptive
    "loyalty",     # Den-Warder: Steadfast and trustworthy
    "passion"      # Sun-Chaser: Vital and emotional
]

# Changing Breed Aspects (supernatural powers/traits)
# Based on Changing Breeds 1st Edition mechanics
CHANGING_BREED_ASPECTS = [
    # Physical Aspects
    "alarming_alacrity", "aww", "catwalk", "clamber", "darksight", "echolocation",
    "exoskeleton", "extra_limb", "fang_and_claw", "gross_eater", "hare_heart", 
    "hybrid_forms", "keen_senses", "leap", "many_legged", "natural_armor", 
    "needleteeth", "nine_lives", "razorskin", "resilient_form", "spinebite", 
    "swift_wing", "tiger_heart", "unnerving_cry", "venomous", "wallwalking", 
    "war_heart", "weatherskin", "webbing", "wings",
    
    # Mental/Social Aspects
    "blend_in", "clever_monkey", "foretelling", "fortune_favor", "grave_misfortune",
    "hypnotic_allure", "invisible_marking", "magnificence", "mercy_touch", 
    "mimic", "mindmap", "mindspeech", "sense_familiarity", "skin_double",
    "slumber_touch", "spook_herd", "stash", "sweet_voiced_fiend", "tell",
    "the_wild_cry", "toss_scent", "truth_sense", "twisted_tongue", 
    "unsettling_eye", "unspeakable",
    
    # Supernatural/Spiritual Aspects
    "aquatic", "beast_magic", "beast_surge", "birth_blessing", "carnivore_puissance",
    "culling_weak", "durga_blessing", "earthbond", "hound_honor", "limbless",
    "mother_fury", "pack_bond", "partial_change", "pearl_great_price", 
    "sexual_dimorphism", "shadow_bond", "size_variable", "speed_variable",
    "spirit_animal", "spirit_bond", "spirit_gift", "spirit_secrets", "spirit_sight",
    "stampede_rush", "swarm_form", "territory_bond", "totem_guardian",
    "warrior_restoration", "waterbreath", "weaver_wisdom"
]

# Valid forms for changing breeds (varies by breed)
CHANGING_BREED_FORMS = [
    "human",           # Human/Homid form
    "war_beast",       # War-Beast/Crinos form
    "primal_beast",    # Primal Beast/Animal form
    "throwback",       # Throwback/Hybrid form (some breeds)
    "dire_beast"       # Dire Beast/Legendary form (some breeds)
]

# Legacy Changing Breeds template definition
LEGACY_CHANGING_BREEDS_TEMPLATE = {
    "name": "legacy_changing_breeds",
    "display_name": "Changing Breeds (Legacy)",
    "description": ("Legacy Changing Breeds template for World of Darkness 1st Edition. "
                   "Shapeshifters come in many forms - werecats, megafauna, spiders, bears, "
                   "birds, and more. Each breed has unique forms and supernatural Aspects. "
                   "Uses traditional virtue/vice system and 1st edition mechanics."),
    "bio_fields": ["breed", "nahual", "accord", "animal_type", "pack", "territory", "respect_type"],
    "integrity_name": "Harmony",
    "starting_integrity": 7,
    "supernatural_power_stat": "feral_heart",  # Feral Heart (not Primal Urge)
    "starting_power_stat": 1,
    "resource_pool": "essence",  # Max = 10 + Feral Heart; starts at Harmony rating
    "power_systems": CHANGING_BREED_ASPECTS,
    "anchors": ["virtue", "vice"],  # Legacy uses virtue/vice only
    "merit_categories": ["physical", "social", "mental", "supernatural", "fighting", "style", "changing_breed"],
    "field_validations": {
        "breed": {
            "valid_values": LEGACY_CHANGING_BREEDS,
            "description": "Specific breed/species of shapeshifter (e.g., Rajanya, Bubasti, etc.)"
        },
        "nahual": {
            "valid_values": list(CHANGING_BREED_CATEGORIES.keys()),
            "description": "Breed category: Bastet, Land Titans, Laughing Strangers, The Pack, Royal Apes, etc."
        },
        "accord": {
            "valid_values": CHANGING_BREED_ACCORDS,
            "description": "Accord is the 'auspice' of the Changing Breeds (Den-Warder, Heart-Ripper, etc.)"
        },
        "animal_type": {
            "description": "Animal type (auto-populated from breed data)"
        },
        "respect_type": {
            "valid_values": RESPECT_TYPES,
            "description": "Type of Respect: Cleverness, Ferocity, Insight, Loyalty, or Passion"
        }
    },
    "legacy_mode": True,  # Flag to indicate this is a legacy template
    "version": "1.0",
    "author": "Chronicles of Darkness Legacy",
    "game_line": "Changing Breeds (1st Edition)",
    "creation_notes": (
        "CHARACTER CREATION:\n"
        "1. Choose Breed & Nahual (e.g., Rajanya from Bastet)\n"
        "2. Select Accord (Den-Warder, Heart-Ripper, Root-Weaver, Sun-Chaser, Wind-Dancer)\n"
        "3. Attributes: 5/4/3 (Physical often primary or secondary)\n"
        "4. Skills: 11/7/4 (Suggested: 1+ dot in Animal Ken, Stealth, Survival)\n"
        "5. Skill Specialties: 3 normally + 1 free from Accord list (if you have that Skill)\n"
        "6. Aspects: 7 points to spend on supernatural abilities\n"
        "7. Merits: 7 points (can spend 3 Merit dots per extra Feral Heart dot)\n"
        "8. Respect: 3 dots (1 assigned by Accord, 2 free)\n"
        "9. Feral Heart: Starts at 1 (increase costs 3 Merit dots per dot)\n"
        "10. Harmony: Starts at 7 (can trade for 5 XP per dot, max 2 dots)\n"
        "11. Essence: Starts at Harmony rating; Max = 10 + Feral Heart\n\n"
        "COMMON TRAITS: All Changing Breeds have Shapeshifting, Fast Healing, Fury/Berserk, "
        "Silver Weakness, and cause the Delusion in witnesses.\n\n"
        "BREEDS: 51 breeds across 10 categories (Bastet, Land Titans, Laughing Strangers, "
        "The Pack, Royal Apes, Spinner-Kin, Ursara, Wind-Runners, Wing-Folk, Shadow Breeds)."
    ),
    "notes": ("Legacy Changing Breeds template for World of Darkness 1st Edition mechanics. "
              "Includes 51 different breeds across 10 categories. Each breed has unique forms "
              "(Human, War-Beast, Primal Beast; some have Throwback or Dire Beast) and Favors. "
              "Purchase Aspects (supernatural powers) with 7 starting points. Uses +shift command "
              "to transform between forms. Feral Heart powers Essence pool. Requires legacy mode.")
}

# Register the template
register_template(LEGACY_CHANGING_BREEDS_TEMPLATE)