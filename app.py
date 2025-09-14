"""
Murder Mystery Detective Game - Main Application
Interactive detective game powered by AI agents
"""

import streamlit as st
from dotenv import load_dotenv

from src.utils.llm_config import initialize_llm, build_graphs
from ui.components.game_setup import setup_game, display_main_header
from ui.components.investigation import display_investigation_phase
from ui.components.game_end import display_game_end
from ui.styles import load_custom_css
from config.settings import initialize_session_state

# Load environment variables
load_dotenv()

# Page configuration
st.set_page_config(
    page_title="Murder Mystery Detective Game",
    page_icon="🔍",
    layout="wide",
    initial_sidebar_state="expanded",
)


def main():
    """Main application function"""
    # Load custom styling
    load_custom_css()

    # Initialize session state and LLM
    initialize_session_state()
    initialize_llm()
    build_graphs()

    # Display main header
    display_main_header()

    # Main game flow based on current phase
    if st.session_state.current_phase == "setup":
        setup_game()

    elif st.session_state.current_phase in ["investigation", "guessing"]:
        display_investigation_phase()

    elif st.session_state.current_phase == "ended":
        display_game_end()


if __name__ == "__main__":
    main()
