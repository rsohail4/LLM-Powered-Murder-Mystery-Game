"""
Configuration and session state initialization
"""

import streamlit as st


def initialize_session_state():
    """Initialize all session state variables"""
    if "game_state" not in st.session_state:
        st.session_state.game_state = None
    if "current_phase" not in st.session_state:
        st.session_state.current_phase = "setup"
    if "conversation_history" not in st.session_state:
        st.session_state.conversation_history = {}
    if "selected_character" not in st.session_state:
        st.session_state.selected_character = None
    if "guesses_made" not in st.session_state:
        st.session_state.guesses_made = []
    if "game_result" not in st.session_state:
        st.session_state.game_result = None
    if "clues_discovered" not in st.session_state:
        st.session_state.clues_discovered = []
    if "current_page" not in st.session_state:
        st.session_state.current_page = "crime_scene"


# Game constants
KILLER_ROLE = "killer"
VICTIM_ROLE = "victim"

DEFAULT_ENVIRONMENT = "Mistral office in Paris"
DEFAULT_MAX_CHARACTERS = 5
DEFAULT_NUM_GUESSES = 3

MIN_CHARACTERS = 3
MAX_CHARACTERS = 8
MIN_GUESSES = 1
MAX_GUESSES = 5
