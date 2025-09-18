"""
Data classes for Chronicles of Darkness stat types.
These are used for stat dictionaries and configuration.
"""

from dataclasses import dataclass
from typing import Optional


@dataclass
class Stat:
    """Base stat data class for attributes and skills."""
    name: str
    min_value: int = 0
    max_value: int = 5
    temp_value: int = 0
    description: str = ""
    att_type: Optional[str] = None  # For attributes: power, finesse, resistance
    skill_type: Optional[str] = None  # For skills: mental, physical, social
    unskilled: Optional[int] = None  # Penalty when untrained


@dataclass
class Pool:
    """Resource pool data class (health, willpower, etc)."""
    name: str
    min_value: int = 0
    max_value: int = 10
    temp_value: int = 0
    description: str = ""


@dataclass
class Advantage:
    """Derived stat data class."""
    name: str
    min_value: int = 0
    max_value: int = 10
    temp_value: int = 0
    description: str = ""
    adv_base: str = ""  # Formula for calculating the advantage


@dataclass
class Anchor:
    """Character anchor data class (virtue, vice, etc)."""
    name: str
    min_value: int = 0
    max_value: int = 10
    temp_value: int = 0
    description: str = "" 

@dataclass
class Merit:
    """Merit data class."""
    name: str
    min_value: int = 1
    max_value: int = 5
    temp_value: int = 0
    description: str = ""
    merit_type: str = ""  # Merit type (e.g., "physical", "social", "mental", "style", "fighting", "supernatural")
    cost: int = 0  # Cost in experience points
    prerequisite: str = ""  # Prerequisite (e.g., "strength:2", "brawl:1", "[brawl:1,weaponry:1]", etc.)
    

