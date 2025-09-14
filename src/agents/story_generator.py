"""
Story and character generation agents
"""

import streamlit as st
import random
from langchain_core.messages import SystemMessage, HumanMessage

from src.models.state import GenerateGameState
from src.models.character import NPC
from src.models.story import StoryDetails
from src.utils.prompts import (
    CHARACTER_CREATION_PROMPT,
    STORY_CREATION_PROMPT,
    NARRATOR_PROMPT,
)


def create_characters(state: GenerateGameState):
    """Create game characters"""
    environment = state["environment"]
    max_characters = state["max_characters"]

    structured_llm = st.session_state.llm.with_structured_output(
        schema=NPC, method="function_calling"
    )

    system_message = CHARACTER_CREATION_PROMPT.format(
        environment=environment, max_characters=max_characters
    )

    result = structured_llm.invoke(
        [
            SystemMessage(content=system_message),
            HumanMessage(content="Generate the set of characters"),
        ]
    )

    characters = result.characters.copy()
    random.shuffle(characters)

    return {"characters": characters}


def create_story(state: GenerateGameState):
    """Create murder mystery story"""
    environment = state["environment"]
    characters = state["characters"]

    character_list = "\n".join([char.persona for char in characters])

    structured_llm = st.session_state.llm.with_structured_output(
        schema=StoryDetails, method="function_calling"
    )

    system_message = STORY_CREATION_PROMPT.format(
        environment=environment, characters=character_list
    )

    result = structured_llm.invoke(
        [
            SystemMessage(content=system_message),
            HumanMessage(content="Generate the murder mystery scenario"),
        ]
    )

    return {"story_details": result}


def narrator(state: GenerateGameState):
    """Generate Dr. Watson's narration"""
    story = state["story_details"]

    system_message = NARRATOR_PROMPT.format(
        victim=story.victim_name,
        time=story.time_of_death,
        location=story.location_found,
        weapon=story.murder_weapon,
        cause=story.cause_of_death,
        scene=story.crime_scene_details,
    )

    narration = st.session_state.llm.invoke(
        [
            SystemMessage(content=system_message),
            HumanMessage(content="Create an atmospheric narration of the crime scene"),
        ]
    )

    return {"messages": [narration]}
