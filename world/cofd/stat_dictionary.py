"""
This is the base stat dictionary for Chronicles of Darkness, it contains everything that would be considered
a 'mortal' stat, and is used to create basic characters before applying a supernatural template.
"""

from world.cofd.stat_types import Anchor, Stat, Advantage, Pool

"""
Attribute Dictionary

The attribute dictionary is comprised of the following elements:

- name: The name of the attribute.
- min_value: The minimum value of the attribute.
- max_value: The maximum value of the attribute.
- temp_value: Certain things can increase or decrease an attribute value temporarily, this is what the character typeclass calls to update the attribute value.
- description: A description of the attribute.
- att_type: The type of attribute (power, finesse, resistance).
"""

attribute_dictionary = {
    "strength": Stat(name="strength", min_value=1, max_value=5, temp_value=0, description="", att_type="power"),
    "dexterity": Stat(name="dexterity", min_value=1, max_value=5, temp_value=0, description="", att_type="finesse"),
    "stamina": Stat(name="stamina", min_value=1, max_value=5, temp_value=0, description="", att_type="resistance"),
    "presence": Stat(name="presence", min_value=1, max_value=5, temp_value=0, description="", att_type="power"),
    "manipulation": Stat(name="manipulation", min_value=1, max_value=5, temp_value=0, description="", att_type="finesse"),
    "composure": Stat(name="composure", min_value=1, max_value=5, temp_value=0, description="", att_type="resistance"),
    "intelligence": Stat(name="intelligence", min_value=1, max_value=5, temp_value=0, description="", att_type="power"),
    "wits": Stat(name="wits", min_value=1, max_value=5, temp_value=0, description="", att_type="finesse"),
    "resolve": Stat(name="resolve", min_value=1, max_value=5, temp_value=0, description="", att_type="resistance"),
}

"""
# Skill Dictionary

The skill dictionary is comprised of the following elements:

- name: The name of the skill.
- min_value: The minimum value of the skill.
- max_value: The maximum value of the skill.
- temp_value: Certain things can increase or decrease a skill value temporarily, this is what the character typeclass calls to update the skill value.
- description: A description of the skill.
- skill_type: The type of skill (mental, physical, social).
- unskilled: The dice penalty applied to the skill when the character has no training in it.
"""

skill_dictionary = {
    "crafts": Stat(name="crafts", min_value=0, max_value=5, temp_value=0, description="", skill_type="mental", unskilled=-3),
    "investigation": Stat(name="investigation", min_value=0, max_value=5, temp_value=0, description="", skill_type="mental", unskilled=-3),
    "medicine": Stat(name="medicine", min_value=0, max_value=5, temp_value=0, description="", skill_type="mental", unskilled=-3),
    "occult": Stat(name="occult", min_value=0, max_value=5, temp_value=0, description="", skill_type="mental", unskilled=-3),
    "politics": Stat(name="politics", min_value=0, max_value=5, temp_value=0, description="", skill_type="mental", unskilled=-3),
    "science": Stat(name="science", min_value=0, max_value=5, temp_value=0, description="", skill_type="mental", unskilled=-3),
    "athletics": Stat(name="athletics", min_value=0, max_value=5, temp_value=0, description="", skill_type="physical", unskilled=-1),
    "brawl": Stat(name="brawl", min_value=0, max_value=5, temp_value=0, description="", skill_type="physical", unskilled=-1),
    "drive": Stat(name="drive", min_value=0, max_value=5, temp_value=0, description="", skill_type="physical", unskilled=-1),
    "firearms": Stat(name="firearms", min_value=0, max_value=5, temp_value=0, description="", skill_type="physical", unskilled=-1),
    "larceny": Stat(name="larceny", min_value=0, max_value=5, temp_value=0, description="", skill_type="physical", unskilled=-1),
    "stealth": Stat(name="stealth", min_value=0, max_value=5, temp_value=0, description="", skill_type="physical", unskilled=-1),
    "survival": Stat(name="survival", min_value=0, max_value=5, temp_value=0, description="", skill_type="physical", unskilled=-1),
    "weaponry": Stat(name="weaponry", min_value=0, max_value=5, temp_value=0, description="", skill_type="physical", unskilled=-1),
    "animal_ken": Stat(name="animal_ken", min_value=0, max_value=5, temp_value=0, description="", skill_type="social", unskilled=-1),
    "empathy": Stat(name="empathy", min_value=0, max_value=5, temp_value=0, description="", skill_type="social", unskilled=-1),
    "expression": Stat(name="expression", min_value=0, max_value=5, temp_value=0, description="", skill_type="social", unskilled=-1),
    "intimidation": Stat(name="intimidation", min_value=0, max_value=5, temp_value=0, description="", skill_type="social", unskilled=-1),
    "persuasion": Stat(name="persuasion", min_value=0, max_value=5, temp_value=0, description="", skill_type="social", unskilled=-1),
    "socialize": Stat(name="socialize", min_value=0, max_value=5, temp_value=0, description="", skill_type="social", unskilled=-1),
    "streetwise": Stat(name="streetwise", min_value=0, max_value=5, temp_value=0, description="", skill_type="social", unskilled=-1),
    "subterfuge": Stat(name="subterfuge", min_value=0, max_value=5, temp_value=0, description="", skill_type="social", unskilled=-1),
}

# Merits are linked to their own specific dictionaries based on merit type and affiliation to supernatural templates

# Merit Types:
# - Physical
# - Social
# - Mental
# - Supernatural
# - Fighting
# - Style

# The above are considered 'mortal' or generic merits that are accessible to any character. Below are supernatural merits that are specific to a particular supernatural template.

# - Changeling
# - Werewolf
# - Vampire
# - Mage
# - Demon
# - Geist
# - Hunter
# - Promethean
# - Beast
# - Renegade
# - Minor-Template (psychics, possessed, etc. any traditional "mortal+" template)

"""
Advantages are any stat that is derived from calculating attributes together.
"""

advantage_dictionary = {
    "integrity": Advantage(name="integrity", min_value=0, max_value=10, temp_value=0, description="", adv_base="7"),
    "size": Advantage(name="size", min_value=0, max_value=10, temp_value=0, description="", adv_base="5"),
    "speed": Advantage(name="speed", min_value=0, max_value=25, temp_value=0, description="", adv_base="strength + dexterity + 5"),
    "health": Advantage(name="health", min_value=0, max_value=20, temp_value=0, description="", adv_base="size + stamina"),
    "power": Advantage(name="power", min_value=0, max_value=30, temp_value=0, description="", adv_base="strength + presence + manipulation"),
    "finesse": Advantage(name="finesse", min_value=0, max_value=30, temp_value=0, description="", adv_base="dexterity + presence + manipulation"),
    "resistance": Advantage(name="resistance", min_value=0, max_value=30, temp_value=0, description="", adv_base="stamina + presence + composure"),
}

"""
Pools are any stat that is can be spent or regained and are used as a resource.
All pools are included here, including ones that are explicitly for supernatural templates.

- health: The amount of health a character has. Derived from size and stamina.
- willpower: The amount of willpower a character has. Derived from resolve and composure.

- essence: The amount of essence a character has. Derived from Primal Urge stat.
  - Primal Urge 1: 10
  - Primal Urge 2: 11
  - Primal Urge 3: 12
  - Primal Urge 4: 13
  - Primal Urge 5: 15
  - Primal Urge 6: 20
  - Primal Urge 7: 25
  - Primal Urge 8: 30
  - Primal Urge 9: 50
  - Primal Urge 10: 75
- blood: The amount of blood a vampire character has. Based on Blood Potency stat.
  - Blood Potency 0: Stamina
  - Blood Potency 1: 10
  - Blood Potency 2: 11
  - Blood Potency 3: 12
  - Blood Potency 4: 13
  - Blood Potency 5: 15
  - Blood Potency 6: 20
  - Blood Potency 7: 25
  - Blood Potency 8: 30
  - Blood Potency 9: 50
  - Blood Potency 10: 75
- glamour: The amount of glamour a changeling character has. Based on Wyrd stat.
  - Wyrd 1: 10
  - Wyrd 2: 11
  - Wyrd 3: 12
  - Wyrd 4: 13
  - Wyrd 5: 15
  - Wyrd 6: 20
  - Wyrd 7: 25
  - Wyrd 8: 30
  - Wyrd 9: 50
  - Wyrd 10: 75
- mana: The amount of mana a mage character has. Derived from Gnosis stat.
  - Gnosis 1: 10
  - Gnosis 2: 11
  - Gnosis 3: 12
  - Gnosis 4: 13
  - Gnosis 5: 15
  - Gnosis 6: 20
  - Gnosis 7: 25
  - Gnosis 8: 30
  - Gnosis 9: 50
  - Gnosis 10: 75
- plasm: The amount of plasm a Geist character has. Based on Synergy stat.
  - Synergy 1: 10
  - Synergy 2: 11
  - Synergy 3: 12
  - Synergy 4: 13
  - Synergy 5: 15
  - Synergy 6: 20
  - Synergy 7: 25
  - Synergy 8: 30
  - Synergy 9: 50
  - Synergy 10: 75
"""

# Pools are the resources that a character can spend or regain.
pool_dictionary = {
    "health": Pool(name="health", min_value=0, max_value=20, temp_value=0, description=""),
    "willpower": Pool(name="willpower", min_value=0, max_value=10, temp_value=0, description=""),
    "essence": Pool(name="essence", min_value=0, max_value=50, temp_value=0, description=""),
    "blood": Pool(name="blood", min_value=0, max_value=50, temp_value=0, description=""),
    "glamour": Pool(name="glamour", min_value=0, max_value=75, temp_value=0, description=""),
    "mana": Pool(name="mana", min_value=0, max_value=50, temp_value=0, description=""),
    "plasm": Pool(name="plasm", min_value=0, max_value=50, temp_value=0, description=""),
}

# Anchors are the core of the character, they are the foundation of the
# character and are used to determine the character's base personality and archetypes.

anchor_dictionary = {
    "virtue": Anchor(name="virtue", min_value=0, max_value=10, temp_value=0, description=""),
    "vice": Anchor(name="vice", min_value=0, max_value=10, temp_value=0, description=""),
    "thread": Anchor(name="thread", min_value=0, max_value=10, temp_value=0, description=""),
    "root": Anchor(name="root", min_value=0, max_value=10, temp_value=0, description=""),
    "mask": Anchor(name="mask", min_value=0, max_value=10, temp_value=0, description=""),
    "dirge": Anchor(name="dirge", min_value=0, max_value=10, temp_value=0, description=""),
    "bloom": Anchor(name="bloom", min_value=0, max_value=10, temp_value=0, description=""),
}
