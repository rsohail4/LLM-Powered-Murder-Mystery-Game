"""
State models for LangGraph workflows
"""

from typing import List, Dict, Optional, Any, Sequence, Annotated
from typing_extensions import TypedDict
import operator

from langchain_core.messages import BaseMessage
from .character import Character
from .story import StoryDetails


class ConversationState(TypedDict):
    messages: Annotated[Sequence[BaseMessage], operator.add]
    character: Character
    story_details: Optional[StoryDetails]


class GenerateGameState(TypedDict):
    messages: Annotated[Sequence[BaseMessage], operator.add]
    environment: str
    max_characters: int
    characters: List[Character]
    story_details: Optional[StoryDetails]
    selected_character_id: Optional[int]
    num_guesses_left: int
    result: str
