# Language System for Chronicles of Darkness

## Overview

The language system allows characters to learn and speak different languages through the **Language merit**. Characters can speak in foreign languages during roleplay, and only those who know the language will understand what's being said.

## Language Merit

The **Language** merit can be purchased from 1-5 dots. Each dot provides **one language point** that can be spent to learn a new language.

**Cost**: 1 Merit dot per language point
**Range**: 1-5 dots

### Free Languages
- **English**: All characters know English by default (free)
- **Native Language**: Characters can set one native language during character creation (free)

### Example
A character with Language ••• (3 dots) can learn 3 additional languages beyond English and their native language.

## Commands

### Player Commands

#### `+language`
View your known languages and currently speaking language.

#### `+language <language>`
Set your speaking language (must be a language you know).
Example: `+language Spanish`

#### `+language none`
Stop speaking in a foreign language, return to English.

#### `+language/add <language>`
Learn a new language (costs 1 language point from Language merit).
Example: `+language/add French`

#### `+language/rem <language>`
Remove a language you've learned (frees up 1 language point).
Example: `+language/rem German`

#### `+language/all`
View all available languages organized by region.

#### `+language/native <language>`
Set your native language during character creation (before approval).
Example: `+language/native Spanish`

### Staff Commands

#### `+language/set <character>=<lang1>,<lang2>,...`
Add languages to a character.
Example: `+language/set Bob=French,Spanish,German`

#### `+language/view <character>`
View a character's known languages and language points.
Example: `+language/view Bob`

#### `+language/rem <character>=<language>`
Remove a language from a character.
Example: `+language/rem Bob=French`

## Roleplay Commands with Language Support

### Say Command: `say <message>` or `"<message>`

When you have a language set with `+language`, your speech will be in that language.

**Examples:**
```
+language Spanish
say Hello, how are you?
```
Output:
- **You see**: You say in Spanish, "Hello, how are you?"
- **Spanish speakers see**: Bob says in Spanish, "Hello, how are you?"
- **Non-Spanish speakers see**: Bob says something in Spanish, but you don't understand.

### Pose Command: `:` or `;` or `pose <action>`

Poses support language-tagged speech using `"~text"` syntax.

**Examples:**
```
+language French
:waves and says "~Bonjour!"
```
Output:
- **You and French speakers see**: Bob waves and says "Bonjour!"
- **Non-French speakers see**: Bob waves and says "[gibberish]"

### Emit Command: `@emit <message>` or `\\<message>`

Emits support language-tagged speech and can emit entire messages in a language.

**Switches:**
- `/language` - Make the entire emit in your current language

**Examples:**
```
@emit A voice calls out "~Hello!"
@emit/language The sign reads clearly.
```

## Available Language Categories

- **Common Languages**: English, Spanish, French, German, Italian, Portuguese, Mandarin, Cantonese, Japanese, Korean, Arabic, Hindi, Russian
- **African Languages**: Swahili, Yoruba, Zulu, Amharic, and many more
- **European Languages**: Polish, Greek, Swedish, Norwegian, Czech, and many more
- **Asian Languages**: Thai, Vietnamese, Tamil, Bengali, and many more
- **Middle Eastern Languages**: Arabic, Hebrew, Farsi, Turkish, Kurdish, and more
- **Indigenous American Languages**: Navajo, Quechua, Cherokee, and more
- **Pacific Languages**: Hawaiian, Maori, Samoan, and more
- **Ancient Languages**: Latin, Ancient Greek, Sanskrit, Old Norse, and more
- **Supernatural Languages**: Enochian, Spirit Speech, First Tongue, High Speech, Animal Speech

Use `+language/all` to see the complete list with all available languages.

## Setting Up Your Character

### During Character Creation

1. **Set your native language** (optional, defaults to English):
   ```
   +language/native Spanish
   ```

2. **Purchase the Language merit** with `+stat`:
   ```
   +stat language=3
   ```

3. **Learn languages**:
   ```
   +language/add French
   +language/add German  
   +language/add Italian
   ```

### During Roleplay

1. **Choose which language to speak**:
   ```
   +language French
   ```

2. **Speak normally** - your speech will be in French:
   ```
   say Bonjour, mes amis!
   ```

3. **Return to English**:
   ```
   +language none
   ```

## Technical Details

### For Staff

The language system is integrated into:
- **Character typeclass** (`typeclasses/characters.py`): Methods for language handling
- **Language data** (`world/utils/language_data.py`): List of available languages
- **RP commands** (`commands/diesiraecode/`): Say, Pose, Emit commands with language support
- **Language command** (`commands/diesiraecode/CmdLanguage.py`): All language management

### Language Obfuscation

When characters speak in a language that others don't understand, the speech is automatically obfuscated (turned into gibberish) while preserving:
- Word lengths
- Punctuation
- Capitalization
- Spacing

This makes it clear that someone is speaking, but not what they're saying.

### Merit Validation

The system automatically validates that characters don't have more languages than their Language merit allows. If a character loses dots in the Language merit, excess languages will be automatically removed.

## Troubleshooting

**Problem**: "You don't know [language]"
- **Solution**: Use `+language/add <language>` to learn it first. Make sure you have enough language points from the Language merit.

**Problem**: Can't add more languages
- **Solution**: You need to increase your Language merit dots with `+stat language=X` where X is the new rating.

**Problem**: Can't set native language
- **Solution**: Native language can only be set during character creation (before approval). Contact staff if you need it changed.

## Examples in Play

### Bilingual Conversation
```
Alice: +language Spanish
Alice: say Buenos días, Bob!
Bob (knows Spanish): Bob hears: "Alice says in Spanish, 'Buenos días, Bob!'"
Charlie (doesn't know Spanish): Charlie hears: "Alice says something in Spanish, but you don't understand."

Bob: +language Spanish
Bob: say ¡Hola Alice! ¿Cómo estás?
Alice hears: "Bob says in Spanish, '¡Hola Alice! ¿Cómo estás?'"
Charlie hears: "Bob says something in Spanish, but you don't understand."
```

### Mixed Language Pose
```
Alice: +language French
Alice: :greets everyone warmly and says "~Bienvenue!" then switches to English, "Welcome!"
- French speakers see: Alice greets everyone warmly and says "Bienvenue!" then switches to English, "Welcome!"
- Non-French speakers see: Alice greets everyone warmly and says "[gibberish]" then switches to English, "Welcome!"
```

