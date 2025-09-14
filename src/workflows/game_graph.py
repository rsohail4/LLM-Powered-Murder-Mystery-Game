"""
Main game workflow graph
"""

from langgraph.graph import StateGraph, START, END
from src.models.state import GenerateGameState
from src.agents.story_generator import create_characters, create_story, narrator


def build_main_graph():
    """Build the main game graph - stops after narrator for user input"""
    builder = StateGraph(GenerateGameState)

    builder.add_node("create_characters", create_characters)
    builder.add_node("create_story", create_story)
    builder.add_node("narrator", narrator)

    builder.add_edge(START, "create_characters")
    builder.add_edge("create_characters", "create_story")
    builder.add_edge("create_story", "narrator")
    builder.add_edge("narrator", END)  # Stop after narrator for user input

    main_graph = builder.compile()
    return main_graph
