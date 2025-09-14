"""
Character models for the murder mystery game
"""

from pydantic import BaseModel, Field
from typing import List


class Character(BaseModel):
    role: str = Field(description="Primary role of the character in the story")
    name: str = Field(description="Name of the character")
    backstory: str = Field(
        description="Backstory of the character focus, concerns, and motives"
    )

    @property
    def persona(self) -> str:
        return f"Name: {self.name}\nRole: {self.role}\nBackstory: {self.backstory}\n"


class NPC(BaseModel):
    characters: List[Character] = Field(
        description="Comprehensive list of characters with their roles and backstories",
        default_factory=list,
    )
