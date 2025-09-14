"""
Conversation workflow graph for character interactions
"""

from langgraph.graph import StateGraph, START, END
from src.models.state import ConversationState
from src.agents.conversation_handler import (
    character_introduction,
    ask_question,
    answer_question,
    where_to_go,
)


def build_conversation_graph():
    """Build the conversation subgraph"""
    conversation_builder = StateGraph(ConversationState)

    conversation_builder.add_node("character_introduction", character_introduction)
    conversation_builder.add_node("ask_question", ask_question)
    conversation_builder.add_node("answer_question", answer_question)

    conversation_builder.add_edge(START, "character_introduction")
    conversation_builder.add_edge("character_introduction", "ask_question")
    conversation_builder.add_conditional_edges(
        "ask_question", where_to_go, {"continue": "answer_question", "end": END}
    )
    conversation_builder.add_edge("answer_question", "ask_question")

    conversation_graph = conversation_builder.compile()
    return conversation_graph
