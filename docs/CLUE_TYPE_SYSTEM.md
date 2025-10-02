# Clue Type System - Method-Specific Investigation

## Overview

The mystery system now includes a sophisticated clue type system that requires specific investigation methods for different types of clues. This makes investigations more strategic and realistic, as players must use the appropriate approach for each type of information.

## ✅ **Investigation Methods & Skills**

### **Method-Specific Skill Combinations**

1. **Examine** - `Resolve + Composure` (Perception check)
   - For noticing physical details, examining objects
   - Pure attribute roll for perception

2. **Search** - `Wits + Investigation`
   - For finding hidden clues through systematic searching
   - Mental acuity + investigative training

3. **Interview** - `Best Social Attribute + Persuasion`
   - Uses higher of Presence or Manipulation + Persuasion
   - Social approach to gathering information

4. **Research** - `Intelligence + Academics`
   - Academic research in libraries and databases
   - Scholarly approach to information gathering

5. **Occult** - `Intelligence + Occult`
   - Specialized research for supernatural/occult topics
   - Requires occult research locations

## 🎯 **Clue Types & Required Methods**

### **Clue Type Categories**

| Clue Type | Required Method | Description | Example |
|-----------|----------------|-------------|---------|
| **Academic** | Research | Scholarly information, historical records | "University records show..." |
| **Occult** | Occult | Supernatural knowledge, ritual information | "Ancient grimoire mentions..." |
| **Physical** | Examine | Physical evidence, visible details | "Scratches on the door..." |
| **Hidden** | Search | Concealed items, secret compartments | "Hidden behind the bookshelf..." |
| **Social** | Interview | Information from people, gossip | "Local bartender knows..." |
| **General** | Any | Can be discovered by any method | "Common knowledge..." |

### **Strategic Investigation**

Players must now think strategically about their approach:

- **Academic clues** won't be found by searching rooms - they require library research
- **Occult clues** need specialized occult research, not regular academics
- **Physical clues** require careful examination of objects
- **Hidden clues** need systematic searching of areas
- **Social clues** require talking to the right people

## 🔧 **Staff Commands for Clue Types**

### **Set Clue Type** - `+mystery/cluetype <mystery_id>/<clue_id> = <type>`
Automatically sets appropriate required methods:
```
+mystery/cluetype 1/clue_0 = academic    # Requires research
+mystery/cluetype 1/clue_1 = occult      # Requires occult
+mystery/cluetype 1/clue_2 = physical    # Requires examine
+mystery/cluetype 1/clue_3 = hidden      # Requires search
+mystery/cluetype 1/clue_4 = social      # Requires interview
+mystery/cluetype 1/clue_5 = general     # Any method works
```

### **Manual Method Setting** - `+mystery/methods <mystery_id>/<clue_id> = <methods>`
For complex clues requiring multiple methods:
```
+mystery/methods 1/clue_0 = research,occult    # Requires both academic AND occult research
+mystery/methods 1/clue_1 = examine,search    # Can be found by examination OR search
+mystery/methods 1/clue_2 =                   # Clear restrictions (any method)
```

## 🎮 **Player Experience**

### **Method Feedback**
When players use the wrong method, they get helpful hints:

```
> +mystery/search
You search here thoroughly but find nothing of interest.
Hint: Try using +mystery/research or +mystery/interview for other types of clues.
```

### **Clue Details**
Players can view discovered clues with `+mystery/clue <name>`:
```
> +mystery/clue "ash symbol"
=== Ash Symbol ===
Mystery: The Missing Heir
Description: A strange ash symbol burned into the wooden floor...
Tags: occult, supernatural
Leads to: Ancient Ritual, Blood Circle
```

### **Strategic Planning**
Players must consider:
- **Location**: Are they in the right place? (library for research, etc.)
- **Method**: What type of clue are they looking for?
- **Skills**: Do they have the right skills for the method?
- **Collaboration**: Can they work with others who have different strengths?

## 📊 **Staff View Enhancements**

The staff view now shows clue types and methods:
```
Mystery: The Missing Heir
  clue_0: Torn Letter
    Description: A letter with half the address torn off...
    Type: physical | Methods: examine
    Discovered by: 2 character(s)
    
  clue_1: University Records  
    Description: Academic records from the local university...
    Type: academic | Methods: research
    Discovered by: 0 character(s)
```

## 🔄 **Location Requirements**

### **Research Locations**
- **Regular Research**: `library`, `computer`, `research` tags
- **Occult Research**: `occult_library`, `grimoire`, `occult_research` tags
  - Fallback: Regular libraries work for basic occult research

### **Future Location Types**
The system is ready for additional location requirements:
- **Forensic Labs**: For advanced physical examination
- **Archives**: For historical research
- **Contacts**: For social investigation
- **Workshops**: For crafts-based investigation

## 🎯 **Examples in Practice**

### **Mystery Setup (Staff)**
```
+mystery/create "The Vanishing" = A student has disappeared from the university
+mystery/addclue 1 = Academic Records/University enrollment and class records
+mystery/cluetype 1/clue_0 = academic

+mystery/addclue 1 = Ritual Circle/Strange symbols carved in the dorm room floor  
+mystery/cluetype 1/clue_1 = occult

+mystery/addclue 1 = Torn Photograph/A photograph with someone's face torn out
+mystery/cluetype 1/clue_2 = physical

+mystery/addclue 1 = Hidden Journal/A journal concealed behind loose floorboards
+mystery/cluetype 1/clue_3 = hidden

+mystery/addclue 1 = Roommate's Story/The missing student's roommate knows something
+mystery/cluetype 1/clue_4 = social
```

### **Player Investigation**
```
> +mystery/research "missing student"     # Finds Academic Records
> +mystery/examine photograph             # Finds Torn Photograph  
> +mystery/search dorm room              # Finds Hidden Journal
> +mystery/occult "ritual symbols"       # Finds Ritual Circle
> +mystery/interview roommate            # Finds Roommate's Story
```

## 🚀 **Benefits**

1. **Strategic Depth**: Players must think about their approach
2. **Realistic Investigation**: Different clues require different methods
3. **Character Specialization**: Different characters excel at different methods
4. **Collaborative Play**: Encourages teamwork between specialists
5. **Staff Control**: Fine-grained control over clue discovery
6. **Player Guidance**: Helpful hints when using wrong methods

## 🔮 **Future Enhancements**

The system is ready for:
- **Equipment Requirements**: Specific tools for certain investigations
- **Time-Based Clues**: Clues only available at certain times
- **Collaborative Clues**: Requiring multiple characters working together
- **Skill Specialization**: Bonuses for characters with high relevant skills
- **Location-Specific Methods**: Methods that only work in certain places

This clue type system transforms mystery investigation from simple dice rolling into strategic, method-based gameplay that rewards thoughtful investigation approaches!
