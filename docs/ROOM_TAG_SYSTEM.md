# Room Tag System for Chronicles of Darkness

## Overview

The room tag system allows storytellers and builders to mark rooms with functional tags that enable specific investigation methods, supernatural mechanics, and thematic categorization. Tags work seamlessly with the mystery investigation system and can be used for any game mechanics that need to identify room types or capabilities.

## Commands

### Set Room Tags
```
+room/tag <target> = <tag1>,<tag2>,<tag3>,...
```

### View Room Tags
```
+room/tags <target>
+room/tag/list         # Show all standard tag categories
```

### View in Room Info
```
roominfo              # Shows tags in the detailed room information
```

## Standard Tag Categories

### 🔍 **Research & Knowledge**
*Enable investigation and scholarly activities*

| Tag | Purpose | Investigation Use |
|-----|---------|-------------------|
| `library` | Standard library | +mystery/research |
| `occult_library` | Occult/supernatural library | +mystery/occult |
| `grimoire` | Contains occult texts | +mystery/occult |
| `archive` | Historical records | +mystery/research |
| `computer` | Digital research | +mystery/research |
| `research` | General research facility | +mystery/research, +mystery/occult |
| `scriptorium` | Ancient/medieval library | +mystery/research |
| `museum` | Artifacts and exhibits | +mystery/research |
| `university` | Academic institution | +mystery/research |
| `laboratory` | Scientific research | +mystery/research |
| `observatory` | Astronomical research | +mystery/research, +mystery/occult |
| `clinic` | Medical research | +mystery/research |
| `morgue` | Forensic investigation | +mystery/research, +mystery/examine |

### 🎭 **Social & Gathering**
*Locations for social interaction and community*

| Tag | Purpose |
|-----|---------|
| `bar` | Drinking establishment |
| `nightclub` | Modern entertainment venue |
| `restaurant` | Dining establishment |
| `cafe` | Coffee shop, informal gathering |
| `theater` | Performance venue |
| `temple` | Religious site (general) |
| `church` | Christian religious site |
| `synagogue` | Jewish religious site |
| `mosque` | Islamic religious site |
| `gathering_hall` | Community meeting place |
| `court` | Royal or legal court |
| `throne_room` | Seat of power |
| `marketplace` | Trading and commerce |
| `forum` | Ancient public gathering |
| `agora` | Greek-style marketplace |

### 🌙 **Supernatural**
*Locations with supernatural significance*

| Tag | Purpose | Game Mechanics |
|-----|---------|----------------|
| `locus` | Werewolf power source | Essence gathering, spirit gate |
| `consecrated` | Holy ground | Affects undead, demons |
| `desecrated` | Unholy ground | Attracts dark forces |
| `hollow` | Mage sanctum | Spell advantages |
| `verge` | Barrier to Shadow | Spirit world proximity |
| `gate` | Portal or gateway | Planar travel |
| `nexus` | Confluence of power | Multiple supernatural types |
| `ley_line` | Mystical energy line | Power source |
| `haunted` | Ghost presence | Sin-Eater relevant |
| `possessed` | Entity-controlled | Supernatural conflict |
| `tainted` | Corrupted location | Investigation clues |
| `blessed` | Divine protection | Holy mechanics |
| `cursed` | Supernatural curse | Negative effects |
| `warded` | Magically protected | Access restrictions |

### 🕵️ **Investigation**
*Mystery and crime-solving locations*

| Tag | Purpose | Investigation Use |
|-----|---------|-------------------|
| `crime_scene` | Active investigation site | +mystery/examine, +mystery/search |
| `evidence_room` | Evidence storage | +mystery/examine, +mystery/research |
| `interrogation` | Questioning room | +mystery/interview |
| `surveillance` | Monitoring station | +mystery/research |
| `safe_house` | Hidden location | Plot-specific |
| `black_market` | Illegal trade | +mystery/interview |
| `underground` | Hidden/secret area | +mystery/search |
| `hidden` | Concealed location | +mystery/search |
| `secret` | Not publicly known | Plot-specific |
| `restricted` | Limited access | Access control |

### 🔨 **Functional**
*Utility and craft locations*

| Tag | Purpose |
|-----|---------|
| `workshop` | Crafting and repairs |
| `forge` | Blacksmithing |
| `armory` | Weapons storage |
| `vault` | Secure storage |
| `treasury` | Wealth storage |
| `stable` | Animal housing |
| `garage` | Vehicle storage |
| `warehouse` | General storage |
| `storage` | Storage room |
| `kitchen` | Food preparation |
| `infirmary` | Medical care |
| `training_ground` | Combat training |
| `ritual_chamber` | Supernatural rituals |

## Time Period Specific Tags

### ⚱️ **Ancient Era** (Pre-500 CE)

| Tag | Description |
|-----|-------------|
| `ruins` | Crumbling ancient structures |
| `catacombs` | Underground burial chambers |
| `amphitheater` | Roman-style arena |
| `bathhouse` | Roman/Greek baths |
| `colosseum` | Gladiatorial arena |
| `aqueduct` | Water transport system |
| `shrine` | Small religious site |
| `oracle` | Prophetic location |
| `necropolis` | City of the dead |
| `ziggurat` | Mesopotamian temple |

### 🏰 **Medieval Era** (500-1500 CE)

| Tag | Description |
|-----|-------------|
| `castle` | Fortified residence |
| `monastery` | Religious community |
| `dungeon` | Underground prison |
| `keep` | Central tower |
| `bailey` | Outer courtyard |
| `scriptorium` | Writing/copying room |
| `chapel` | Small church |
| `great_hall` | Main gathering hall |
| `tower` | Defensive/living tower |
| `cloister` | Covered walkway |

### 🎩 **Victorian Era** (1837-1901)

| Tag | Description |
|-----|-------------|
| `parlor` | Formal sitting room |
| `ballroom` | Dance hall |
| `gentlemens_club` | Exclusive male club |
| `ladies_parlor` | Female social space |
| `opium_den` | Drug establishment |
| `factory` | Industrial workspace |
| `sanitarium` | Mental health facility |
| `asylum` | Institution |
| `workhouse` | Poor labor facility |
| `drawing_room` | Reception room |

### 🏙️ **Modern Era** (1900+)

| Tag | Description |
|-----|-------------|
| `office` | Business workspace |
| `apartment` | Residential unit |
| `penthouse` | Luxury apartment |
| `parking_garage` | Vehicle storage |
| `server_room` | Computer servers |
| `data_center` | Technology hub |
| `nightclub` | Modern club |
| `gym` | Fitness center |
| `coffee_shop` | Modern cafe |
| `hospital` | Medical facility |
| `police_station` | Law enforcement |

## Mystery System Integration

### Investigation Method Requirements

Tags enable specific investigation commands:

```bash
# Academic Research (requires: library, research, archive, etc.)
+room/tag here=library,research
# Enables: +mystery/research <topic>

# Occult Research (requires: occult_library, grimoire, etc.)
+room/tag here=occult_library,grimoire
# Enables: +mystery/occult <topic>

# Physical Investigation (works anywhere but enhanced with tags)
+room/tag here=crime_scene,evidence_room
# Enhances: +mystery/examine, +mystery/search
```

### Example Room Setups

#### **University Library**
```bash
+room/tag here=library,research,university,archive
```
Enables: Academic research, historical investigation

#### **Occult Bookstore**
```bash
+room/tag here=occult_library,grimoire,research,black_market
```
Enables: Occult research, mysterious connections

#### **Crime Scene**
```bash
+room/tag here=crime_scene,restricted,investigation
```
Enhances: Physical examination, evidence gathering

#### **Ancient Temple Ruins**
```bash
+room/tag here=ruins,temple,consecrated,occult_library,ancient
```
Enables: Occult research, historical context, supernatural mechanics

#### **Victorian Gentleman's Club**
```bash
+room/tag here=gentlemens_club,gathering_hall,victorian,secret
```
Context: Social investigation, period-appropriate

#### **Modern Police Station**
```bash
+room/tag here=police_station,evidence_room,interrogation,computer,modern
```
Enables: All investigation types, secure location

## Best Practices

### Tag Combinations

**Combine functional tags with era tags:**
```bash
+room/tag here=library,scriptorium,medieval     # Medieval library
+room/tag here=laboratory,modern,research       # Modern lab
+room/tag here=temple,ruins,ancient,haunted     # Ancient haunted temple
```

**Combine purpose tags with atmosphere tags:**
```bash
+room/tag here=bar,underground,black_market     # Shady underground bar
+room/tag here=hospital,haunted,morgue          # Haunted hospital morgue
+room/tag here=library,cursed,occult_library    # Cursed occult library
```

### Mystery Clue Integration

When creating mysteries, use tags to guide players:

```bash
# Staff creates mystery
+mystery/create Ancient Ritual=Discover the purpose of the ritual
+mystery/addclue 1 = Temple Inscription/Ancient text on temple walls
+mystery/cluetype 1/clue_0 = academic

# Add location hint in clue description or use tags
# Players will need to go to a library/research location
```

## Custom Tags

You're not limited to the standard tags! Create custom tags for:
- **Plot-specific locations**: `red_court`, `shadow_council`, `order_headquarters`
- **Special mechanics**: `timeloop`, `dreamscape`, `mirror_world`
- **Access control**: `vampires_only`, `mages_only`, `mortals_restricted`
- **Thematic elements**: `gothic`, `noir`, `cyberpunk`, `eldritch`

## Quick Reference

### Mystery Investigation Tag Requirements

| Investigation Method | Required/Useful Tags |
|---------------------|---------------------|
| `+mystery/research` | library, research, archive, computer, university, museum |
| `+mystery/occult` | occult_library, grimoire, occult_research, observatory, temple |
| `+mystery/examine` | Any location (enhanced by: crime_scene, evidence_room) |
| `+mystery/search` | Any location (enhanced by: hidden, secret, underground) |
| `+mystery/interview` | Any social location (bar, cafe, gathering_hall, etc.) |

### Supernatural Mechanics Tags

| Game Line | Relevant Tags |
|-----------|---------------|
| Vampire | consecrated, desecrated, cursed, nightclub, penthouse |
| Werewolf | locus, verge, gate, wilderness, forest, den |
| Mage | hollow, nexus, ley_line, library, observatory, sanctum |
| Changeling | hollow, gate, market, theater, hedge_gate |
| Sin-Eater | haunted, morgue, cemetery, necropolis, death_place |
| Mummy | ruins, tomb, temple, museum, ancient, necropolis |

## Usage Examples

```bash
# Ancient vampire haven
+room/tag here=ruins,catacombs,ancient,desecrated,cursed

# Modern mage sanctum
+room/tag here=hollow,library,research,computer,warded,modern

# Werewolf pack meeting ground
+room/tag here=locus,gathering_hall,sacred,consecrated

# Changeling hollow
+room/tag here=hollow,gate,hidden,market,timeless

# Mortal+ investigation office
+room/tag here=office,evidence_room,computer,research,modern

# Victorian spiritualist parlor
+room/tag here=parlor,haunted,occult_library,victorian,gathering_hall
```

This tag system provides flexible, thematic room categorization that enhances both investigation gameplay and supernatural mechanics!
