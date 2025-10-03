# Mortal+ (Minor Template) Merits - Complete Summary

## File Information
- **File**: `PyReach/world/cofd/merits/minor_template_merits.py`
- **Total Lines**: ~1,100
- **Total Merits**: 107
- **Linter Errors**: 0 ✅

## Source Materials
- [Codex of Darkness - Mortal Merits](https://codexofdarkness.com/wiki/Merits,_Mortal)
- [Codex of Darkness - Ghost Merits](https://codexofdarkness.com/wiki/Merits,_Ghost)
- [Codex of Darkness - Atariya Merits](https://codexofdarkness.com/wiki/Merits,_Atariya)
- [Codex of Darkness - Immortal Merits](https://codexofdarkness.com/wiki/Merits,_Immortal)
- [Codex of Darkness - Infected Merits](https://codexofdarkness.com/wiki/Merits,_Infected)
- [Codex of Darkness - Psychic Vampires](https://codexofdarkness.com/wiki/Merits,_Psychic_Vampires)

## System Design

### Template Type System
Template type is set via the `template_type` field (NOT as a merit):
```python
# Character creation
character.db.template_type = "Ghoul"  # This determines which merits are available

# Merit prerequisites
prerequisite="template_type:ghoul"  # ✅ Explicitly requires Ghoul template type
prerequisite="template_type:infected,carrier:3"  # ✅ Template type + other prerequisites
```

## Completed Templates

### ✅ GHOULS (4 merits)
**Template**: `template_type="Ghoul"`

1. **Vital Resilience** (1-5) - Vitae-boosted Stamina
2. **Vital Strength** (1-5) - Vitae-boosted Strength
3. **Vital Swiftness** (1-5) - Vitae-boosted Dexterity
4. **Vital Tenacity** (1-5) - Vitae-boosted Wits

### ✅ DHAMPIR (5 merits)
**Template**: `template_type="Dhampir"`

1. **Blood Affinity** (1) - Sense vampires
2. **Blood Drain** (3) - Bite and drain blood
3. **Daywalker** (2) - No sunlight penalties
4. **Half-Damned** (1-5) - Limited Vitae pool
5. **Predatory Aspect** (2) - Lesser predatory aura

### ✅ FAE-TOUCHED (15 merits)
**Template**: `template_type="Fae-Touched"`

**Pledge Powers:**
1. **Broken Mirror** (2) - Swap with reflection
2. **Dreamer's Gaze** (1) - Enter pledgebound's Bastion
3. **Favored Promise** (1-3) - Bonus to specific promise type
4. **Find the Oathbreaker** (2) - Track pledge violators
5. **Keeper of the Bargain** (3) - Enhanced oath resistance
6. **Punish the Oathbreaker** (2) - Use Contracts on oathbreakers
7. **Sense Vows** (1) - Detect pledgebound
8. **Twice Shy** (3) - Use Dreamer's Gaze on fetch

**Promise Types:**
9. **Promise of Clemency** (1-3) - Forgiveness oath
10. **Promise of Debt** (1-3) - Debt repayment oath
11. **Promise of Love** (1-3) - Love oath
12. **Promise of Loyalty** (3) - Loyalty oath
13. **Promise of Protection** (1-5) - Protection oath
14. **Promise to Provide** (3) - Hospitality oath
15. **Promise to Serve** (1-3) - Service oath

### ✅ DEMON-BLOODED (9 merits)
**Template**: `template_type="Demon-Blooded"`

1. **Ambient Aether** (1-2) - Gather and spend Aether
2. **Aether Pool** (2) - Five-point Aether pool
3. **Eidetic Memory** (1) - Reduced cost version
4. **Infrastructure Proficiency** (2-3) - Navigate God-Machine infrastructure
5. **Instinctive Deflection** (2) - Avoid compromise
6. **Quantum Understanding** (3) - Read Liar's Tongue
7. **Unknown** (1) - Start without Cipher (chargen only)
8. **Unseen Sense (Angels)** (2) - Sense Aether sources
9. **Voice of Hell** (2) - Aether-fueled language fluency

### ✅ STIGMATIC (4 merits)
**Template**: `template_type="Stigmatic"`

1. **Potent Blood** (1) - Blood useful for supernatural actions
2. **Sleeve Integrator** (1-5) - Merge with demon as Cover
3. **Sympathetic Demon** (2) - Demon ally
4. **Pact Sense** (3) - Sense demonic pacts

### ✅ GHOSTS (12 merits)
**Template**: `template_type="Ghost"`

**Core Ghost Merits:**
1. **Brain Eater** (1) - Eat corpse organs for Memories
2. **Dead Meat** (1) - Inhabit dead body
3. **Deep Memory** (1) - Increase Memory storage
4. **Wake** (1-5) - Gain Essence from mourning

**Iconography (Choose Only ONE):**
5. **Ajna** (1) - Perceptive third eye
6. **Banda** (1) - Uncanny sway
7. **Crowned** (1) - Spectral light halo
8. **Immaculate Heart** (1) - Exposed beating heart
9. **Pierced** (1) - Forever wounded
10. **Shackled** (1) - Bound in chains
11. **Veined** (1) - Pulsing veins
12. **Waters** (1) - Water constantly dripping

### ✅ IMMORTALS (10 merits)
**Template**: `template_type="Immortal"`

1. **Dead Celebrity** (1-3) - Fame from previous era
2. **Endless Potency** (1-5) - Boost Attributes with Sekhem/Pillars
3. **Enigma** (1-5) - Erase evidence of your life
4. **Fount of Vitality** (4) - Heal like Arisen
5. **Grave Robber** (5) - Disturb tombs without waking mummies
6. **Lineal Inheritor** (3) - Inherited Pillar investment
7. **Relic Sensitivity** (2) - Sense Sekhem vessels
8. **Resplendent Soul** (3) - Permanent Pillar dot
9. **Supernatural Resistance** (1-5) - Boost Supernatural Tolerance
10. **Tenacious Eternity** (4) - Modify bathing ritual

### ✅ ATARIYA (8 merits)
**Template**: `template_type="Atariya"`

1. **Damn Lucky** (1-4) - Base luck merit, prevent harm
2. **All-In** (3) - Reduce dice pool to special chance die
3. **Count Down** (1) - Know remaining death-cheats
4. **Easy Come, Easy Go** (1) - Exchange Merit dots
5. **Luck Flows Up** (2) - Steal luck like Thief of Fate
6. **Mr. Lucky** (1) - Apparition warns of danger
7. **Nine Lives** (1-5) - Cheat death (chargen only)
8. **See the Flow** (1-5) - Sense and nudge odds

### ✅ INFECTED (7 merits)
**Template**: `template_type="Infected"`

1. **Carrier** (1-5) - Base infection merit, spread disease
2. **Bloodkin** (1) - Social bonus with same infection lineage
3. **Bulletman Syndrome** (5) - Armor per Stamina dot
4. **The New Flesh** (1, 3, 5) - Enhanced healing
5. **Patient Zero** (2) - Force infection into dormancy
6. **Proud Parent** (1) - Spreading infection as Virtue
7. **Virulent** (2-4) - Inflict Sick/Poison Tilts

### ✅ PSYCHIC VAMPIRES (13 merits)
**Template**: `template_type="Psychic Vampire"`

**Core Style:**
1. **Psychic Vampirism** (1-5) - Drain Ephemera through touch

**Enhancement Styles:**
2. **Breath Stealer** (1-3) - Ranged draining
3. **Euphoric Touch** (1-3) - Inflict Conditions while draining

**Power Merits:**
4. **Burst of Speed** (1) - Ephemera for combat bonuses
5. **Ephemeral Battery** (1-5) - Store more Ephemera
6. **Nocturnal Supremacy** (2-5) - Nighttime bonuses
7. **Psychic Infection** (1) - Spread vampirism ability
8. **Psychic Seduction** (1) - Overwrite victim's Vice
9. **Psychic Transference** (2) - Transfer Ephemera to others
10. **Shapechanging** (2-3) - Animal transformation
11. **Soul Eater** (2) - Affect ghosts/spirits
12. **Unearthly Beauty** (1-2) - Ephemera for Striking Looks
13. **Vampiric Potency** (1-5) - Ephemera for Attribute boost

### ✅ PROXIMI (1 merit)
**Template**: `template_type="Proximus"`

1. **Proximi Bloodline** (1) - Family magical traditions

## General Merits

### ✅ GENERAL SUPERNATURAL (23 merits)
**Available to ALL Mortals**

1. Accursed Harbinger (3)
2. Animal Possession (2-4)
3. Animal Speech (1-2)
4. Apportation (3-5)
5. Assertive Implement (1-4)
6. Biomimicry (1-4)
7. Bless Amulet (1-3)
8. Camera Obscura (3)
9. Citywalker (3)
10. Consecrate Weapon (4)
11. Curse Effigy (3)
12. Dark Passenger (2)
13. Doppelganger (3)
14. Evil Eye (2)
15. Hardened Exorcist (1)
16. Hidden Variable (2)
17. Incite Ecosystem (1-5)
18. Invoke Spirit (2)
19. Potent Psyche (1-5)
20. Soul Jar (4)
21. Sojourner (3)
22. Spirit Familiar (3)
23. Psychic Resistance (2)

### ✅ RITUAL SORCERY (4 merits)
**Available to Ritual Sorcerers**

1. Ritual Sorcerer (3) - Foundation merit
2. Forbidden Rites (1-5)
3. Sorcerous Knowledge (1-5)
4. Sorcerous Prodigy (3)

## Templates Awaiting Specific Merits

### ⏳ Needs Source Material
- **Wolf-Blooded** - From Werewolf: The Forsaken 2e
- **Alchemists** - From Promethean: The Created 2e
- **Hosts** - From Demon: The Descent
- **Dreamers** - From Chronicles of Darkness
- **Lost Boys** - URL provided: https://codexofdarkness.com/wiki/Merits,_Lost_Boys
- **Plain** - From Chronicles of Darkness
- **Psychics** - Mostly uses general supernatural merits
- **Skinthieves** - URL provided: https://codexofdarkness.com/wiki/Merits,_Skinchangers_(2nd_Edition)

## Merit Type Breakdown

- **Supernatural**: 78 merits
- **Social**: 14 merits
- **Physical**: 6 merits
- **Mental**: 5 merits
- **Style**: 4 merits

## Prerequisite Format

All template-specific merits use the `template_type:` format:

```python
# Single prerequisite
prerequisite="template_type:ghoul"

# Multiple prerequisites
prerequisite="template_type:infected,carrier:3"
prerequisite="template_type:stigmatic,integrity:5"
prerequisite="template_type:atariya,damn_lucky:1,nine_lives:1"
```

## Notable Features

### Resource Systems by Template

| Template | Resource | Usage |
|----------|----------|-------|
| Ghoul | Vitae | Boost attributes temporarily |
| Dhampir | Vitae (limited) | Heal, fuel vampire powers |
| Fae-Touched | Glamour | Pledge magic, teleportation |
| Demon-Blooded | Aether | Language fluency, powers |
| Stigmatic | Varies | Blood magic, demon bonding |
| Ghost | Essence | Manifestation, powers |
| Immortal | Sekhem/Pillars | Attribute boosts, healing |
| Atariya | Luck | Prevent harm, manipulate odds |
| Infected | Infection | Spread disease, mutations |
| Psychic Vampire | Ephemera | Healing, Willpower, shapechanging |

### Exclusive Merit Systems

**Ghosts - Iconography (Choose Only ONE):**
- 8 mutually exclusive Corpus-shaping merits
- Each provides unique spectral appearance and abilities

**Atariya - Luck Cascade:**
- Damn Lucky (base merit)
- All other Atariya merits require Damn Lucky
- Creates interconnected luck manipulation system

**Infected - Disease Progression:**
- Carrier (base merit, 1-5 dots)
- Most infected merits require Carrier
- Higher Carrier dots unlock more powerful mutations

**Psychic Vampires - Ephemera System:**
- Psychic Vampirism (base style, 1-5 dots)
- Multiple enhancement styles and powers
- Comprehensive draining and conversion mechanics

## Next Steps

### Priority 1: Major Template-Linked
1. **Wolf-Blooded** merits from WTF 2e
2. **Alchemist** merits from PTC 2e
3. **Host** merits from DTD

### Priority 2: Independent Templates
4. **Lost Boys** - Source URL provided
5. **Skinchangers** - Source URL provided
6. **Dreamers** - Research needed
7. **Plain** - Research needed
8. **Psychics** - Clarify template-specific vs general supernatural

### Priority 3: Integration
9. Create template-specific merit validation system
10. Link resource pools to templates
11. Document template restrictions and special rules
12. Test merit prerequisite checking

## Template Compatibility

### Cross-Template Access
Some templates can access merits from multiple lists:

**Psychics** can access:
- General Supernatural Merits (all psychic powers)
- Template-specific merits (if any)

**Ritual Sorcerers** can access:
- General merits
- Ritual Sorcery merits (with Ritual Sorcerer merit)
- Template-specific merits

### Template Supersession
Lesser templates can be superseded by greater ones:
- Ghoul → Vampire (loses ghoul status)
- Proximi → Mage (may retain some benefits)
- Wolf-Blooded → Werewolf (loses wolf-blooded status)

## File Organization

```
minor_template_merits.py
├── Header Documentation (lines 1-16)
├── General Supernatural Merits (23 merits)
├── Ritual Sorcery Merits (4 merits)
├── Vampire-Linked Merits
│   ├── Ghouls (4 merits)
│   └── Dhampir (5 merits)
├── Werewolf-Linked Merits (0 merits - pending)
├── Mage-Linked Merits
│   ├── Proximi (1 merit)
│   └── Alchemists (0 merits - pending)
├── Changeling-Linked Merits
│   └── Fae-Touched (15 merits)
├── Geist-Linked Merits
│   └── Ghosts (12 merits)
├── Mummy-Linked Merits
│   └── Immortals (10 merits)
├── Demon-Linked Merits
│   ├── Hosts (0 merits - pending)
│   ├── Demon-Blooded (9 merits)
│   └── Stigmatic (4 merits)
└── Independent Templates
    ├── Atariya (8 merits)
    ├── Infected (7 merits)
    ├── Psychic Vampires (13 merits)
    ├── Dreamers (0 merits - pending)
    ├── Lost Boys (0 merits - pending)
    ├── Plain (0 merits - pending)
    ├── Psychics (notes only)
    └── Skinthieves (0 merits - pending)
```


