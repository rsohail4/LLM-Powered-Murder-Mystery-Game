"""
Conversation handling agents for character interactions
"""

import streamlit as st
from langchain_core.messages import BaseMessage, HumanMessage, SystemMessage
from langchain_core.prompts import ChatPromptTemplate, MessagesPlaceholder

from src.models.state import ConversationState
from src.utils.prompts import (
    CHARACTER_INTRODUCTION_PROMPT,
    SHERLOCK_ASK_PROMPT,
    ANSWER_QUESTION_PROMPT,
)


def character_introduction(state: ConversationState):
    """Generate character introduction"""
    character = state["character"]
    story = state["story_details"]

    system_message = CHARACTER_INTRODUCTION_PROMPT.format(
        subject_persona=character.persona,
        victim=story.victim_name,
        time=story.time_of_death,
        location=story.location_found,
    )

    narration = st.session_state.llm.invoke(
        [
            SystemMessage(content=system_message),
            HumanMessage(content="Introduce yourself to Sherlock Holmes"),
        ]
    )

    return {"messages": [narration]}


def get_question(state: ConversationState):
    """Generate Sherlock Holmes question"""
    messages = state["messages"]
    character = state["character"]
    story = state["story_details"]

    system_message = SHERLOCK_ASK_PROMPT.format(
        character_name=character.name,
        victim_name=story.victim_name,
        time_of_death=story.time_of_death,
        location_found=story.location_found,
        murder_weapon=story.murder_weapon,
        cause_of_death=story.cause_of_death,
        crime_scene_details=story.crime_scene_details,
        initial_clues=story.initial_clues,
        conversation_history="\n".join(
            [f"{msg.type}: {msg.content}" for msg in messages]
        ),
    )

    prompt = ChatPromptTemplate.from_messages(
        [
            ("system", system_message),
            MessagesPlaceholder(variable_name="messages"),
        ]
    )

    chain = prompt | st.session_state.llm
    question = chain.invoke(messages)

    return question.content


def ask_question(state: ConversationState):
    """Handle question asking - handled by Streamlit UI"""
    return {"messages": []}


def answer_question(state: ConversationState):
    """Generate character's answer"""
    messages = state["messages"]
    character = state["character"]
    last_message = messages[-1]
    story = state["story_details"]

    system_message = ANSWER_QUESTION_PROMPT.format(
        subject_persona=character.persona,
        victim=story.victim_name,
        time=story.time_of_death,
        location=story.location_found,
        weapon=story.murder_weapon,
        cause=story.cause_of_death,
        scene=story.crime_scene_details,
        npc_brief=story.npc_brief,
        question=last_message.content,
    )

    prompt = ChatPromptTemplate.from_messages(
        [
            ("system", system_message),
            MessagesPlaceholder(variable_name="messages"),
        ]
    )

    chain = prompt | st.session_state.llm
    answer = chain.invoke(messages)

    return {"messages": [answer]}


def where_to_go(state: ConversationState):
    """Determine conversation flow"""
    messages = state["messages"]
    last_message = messages[-1]
    if "EXIT" in last_message.content:
        return "end"
    else:
        return "continue"
