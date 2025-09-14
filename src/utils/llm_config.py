"""
LLM configuration and initialization
"""

import streamlit as st
from databricks_langchain import ChatDatabricks
from src.workflows.conversation_graph import build_conversation_graph
from src.workflows.game_graph import build_main_graph


def initialize_llm():
    """Initialize the LLM model"""
    if "llm" not in st.session_state:
        st.session_state.llm = ChatDatabricks(
            endpoint="databricks-llama-4-maverick",
            temperature=0.1,
        )


def build_graphs():
    """Initialize LangGraph workflows"""
    if "conversation_graph" not in st.session_state:
        st.session_state.conversation_graph = build_conversation_graph()

    if "main_graph" not in st.session_state:
        st.session_state.main_graph = build_main_graph()
