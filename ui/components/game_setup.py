"""
Game setup UI components
"""

import streamlit as st
import time
import traceback

from config.settings import (
    DEFAULT_ENVIRONMENT,
    DEFAULT_MAX_CHARACTERS,
    DEFAULT_NUM_GUESSES,
    MIN_CHARACTERS,
    MAX_CHARACTERS,
    MIN_GUESSES,
    MAX_GUESSES,
)


def display_main_header():
    """Display the main game header"""
    st.markdown(
        """
        <div class="main-header">
            <h1>🕵️ Murder Mystery Detective Game</h1>
            <p>Step into the shoes of Sherlock Holmes and solve the mystery!</p>
        </div>
    """,
        unsafe_allow_html=True,
    )


def setup_game():
    """Handle game setup phase"""
    st.header("🎮 Game Setup")

    col1, col2 = st.columns(2)

    with col1:
        st.subheader("Game Configuration")
        environment = st.text_input(
            "Environment/Setting",
            value=DEFAULT_ENVIRONMENT,
            help="Describe the setting where the murder takes place",
        )

        max_characters = st.slider(
            "Number of Characters",
            min_value=MIN_CHARACTERS,
            max_value=MAX_CHARACTERS,
            value=DEFAULT_MAX_CHARACTERS,
            help="Total number of characters including victim and killer",
        )

        num_guesses = st.slider(
            "Number of Guesses",
            min_value=MIN_GUESSES,
            max_value=MAX_GUESSES,
            value=DEFAULT_NUM_GUESSES,
            help="How many attempts you get to identify the killer",
        )

    with col2:
        st.subheader("Game Instructions")
        st.markdown("""
        **How to Play:**
        1. 📚 Review the crime scene and character backgrounds
        2. 🗣️ Interview suspects by asking questions
        3. 🤖 Use Sherlock AI assistant for help
        4. 🔍 Gather clues and evidence
        5. 🎯 Make your final guess to identify the killer
        
        **Tips:**
        - Pay attention to character motivations
        - Look for inconsistencies in stories
        - Use the AI assistant when stuck
        """)

    if st.button("🚀 Start New Game", type="primary", use_container_width=True):
        with st.spinner("🎭 Creating characters and storyline..."):
            try:
                game_input = {
                    "environment": environment,
                    "max_characters": max_characters,
                    "num_guesses_left": num_guesses,
                    "messages": [],
                    "characters": [],
                    "story_details": None,
                    "selected_character_id": None,
                    "result": "",
                }

                # Generate game using LangGraph
                result = st.session_state.main_graph.invoke(game_input)
                st.session_state.game_state = result
                st.session_state.current_phase = "investigation"
                st.success("✅ Game created successfully!")

                time.sleep(1)
                st.rerun()

            except Exception as e:
                st.error("❌ Error creating game.")
                st.text(f"Exception: {str(e)}")
                st.text(traceback.format_exc())
