"""
Investigation phase UI components
"""

import streamlit as st
import time
from langchain_core.messages import HumanMessage

from src.agents.conversation_handler import (
    character_introduction,
    get_question,
    answer_question,
)
from config.settings import KILLER_ROLE


def display_game_status():
    """Display current game status in sidebar"""
    st.sidebar.markdown("### 📊 Game Status")

    if st.session_state.game_state:
        game_state = st.session_state.game_state

        phase_emoji = {
            "setup": "⚙️",
            "investigation": "🔍",
            "guessing": "🎯",
            "ended": "🏁",
        }
        st.sidebar.markdown(
            f"**Phase:** {phase_emoji.get(st.session_state.current_phase, '❓')} {st.session_state.current_phase.title()}"
        )

        st.sidebar.markdown(
            f"**Guesses Left:** {game_state.get('num_guesses_left', 0)} 🎲"
        )

        interviewed = len(st.session_state.conversation_history)
        total_chars = len(
            [c for c in game_state["characters"] if c.role.lower() != "victim"]
        )
        st.sidebar.markdown(
            f"**Characters Interviewed:** {interviewed}/{total_chars} 👥"
        )


def display_crime_scene():
    """Display crime scene information"""
    if not st.session_state.game_state:
        return

    story = st.session_state.game_state["story_details"]

    st.header("🏢 Crime Scene")

    col1, col2 = st.columns(2)

    with col1:
        st.subheader("📋 Basic Information")
        st.markdown(f"**Victim:** {story.victim_name}")
        st.markdown(f"**Time of Death:** {story.time_of_death}")
        st.markdown(f"**Location:** {story.location_found}")
        st.markdown(f"**Weapon:** {story.murder_weapon}")
        st.markdown(f"**Cause of Death:** {story.cause_of_death}")

    with col2:
        st.subheader("🔍 Scene Details")
        st.markdown(f"**Scene Description:**\n{story.crime_scene_details}")

        st.subheader("👁️ Witnesses")
        st.markdown(story.witnesses)

    st.markdown('<div class="clue-box">', unsafe_allow_html=True)
    st.subheader("🧩 Initial Clues")
    st.markdown(story.initial_clues)
    st.markdown("</div>", unsafe_allow_html=True)

    # Display Watson's narration
    if st.session_state.game_state.get("messages"):
        st.subheader("📖 Dr. Watson's Report")
        narration = st.session_state.game_state["messages"][0]
        st.markdown(f"*{narration.content}*")


def display_characters():
    """Display character list with interview options"""
    if not st.session_state.game_state:
        return

    st.header("👥 Characters")
    characters = st.session_state.game_state["characters"]
    suspects = [c for c in characters if c.role.lower() != "victim"]
    victim = next((c for c in characters if c.role.lower() == "victim"), None)

    if victim:
        st.subheader("💀 Victim")
        st.markdown(
            f"""
        <div class="character-card victim-card">
            <h4>{victim.name}</h4>
            <p><strong>Role:</strong> {victim.role.title()}</p>
            <p><strong>Background:</strong> {victim.backstory}</p>
        </div>
        """,
            unsafe_allow_html=True,
        )

    st.subheader("🕵️ Suspects")

    for i, character in enumerate(suspects):
        interviewed = character.name in st.session_state.conversation_history
        interview_status = "✅ Interviewed" if interviewed else "❓ Not interviewed"

        st.markdown(
            f"""
        <div class="character-card">
            <h4>{character.name} ({interview_status})</h4>
            <p><strong>Background:</strong> {character.backstory}</p>
        </div>
        """,
            unsafe_allow_html=True,
        )

        if st.button(f"🗣️ Interview {character.name}", key=f"interview_{i}"):
            char_index = next(
                (
                    idx
                    for idx, c in enumerate(st.session_state.game_state["characters"])
                    if c.name == character.name
                ),
                None,
            )
            if char_index is not None:
                st.session_state.selected_character = character
                st.session_state.game_state["selected_character_id"] = char_index
                st.session_state.current_page = "investigation"
                st.rerun()


def display_character_interview():
    """Handle character interview interface"""
    if not st.session_state.selected_character:
        st.info("Select a character to interview from the Characters section.")
        return

    character = st.session_state.selected_character
    char_name = character.name

    st.header(f"🗣️ Interviewing {char_name}")

    # Initialize conversation history for this character
    if char_name not in st.session_state.conversation_history:
        st.session_state.conversation_history[char_name] = []
        # Generate character introduction
        conv_state = {
            "character": character,
            "story_details": st.session_state.game_state["story_details"],
            "messages": [],
        }
        intro_result = character_introduction(conv_state)
        intro_message = intro_result["messages"][0].content

        st.session_state.conversation_history[char_name].append(
            {"type": "character", "content": intro_message, "timestamp": time.time()}
        )

    # Display conversation history
    st.subheader("💬 Conversation")
    conversation = st.session_state.conversation_history[char_name]

    for msg in conversation:
        if msg["type"] == "character":
            st.markdown(
                f"""
            <div class="conversation-bubble">
                <strong>{char_name}:</strong> {msg["content"]}
            </div>
            """,
                unsafe_allow_html=True,
            )
        elif msg["type"] == "player":
            st.markdown(
                f"""
            <div class="sherlock-bubble">
                <strong>🕵️ You:</strong> {msg["content"]}
            </div>
            """,
                unsafe_allow_html=True,
            )
        elif msg["type"] == "sherlock_ai":
            st.markdown(
                f"""
            <div class="sherlock-bubble">
                <strong>🤖 Sherlock AI:</strong> {msg["content"]}
            </div>
            """,
                unsafe_allow_html=True,
            )

    # Question input section
    st.subheader("❓ Ask a Question")
    col1, col2 = st.columns([3, 1])

    with col1:
        question = st.text_area(
            "Your question:",
            height=100,
            placeholder="What were you doing around the time of the murder?",
            key="question_input",
        )

    with col2:
        st.markdown("**Options:**")
        use_sherlock_ai = st.checkbox("🤖 Use Sherlock AI", value=False)

        if st.button(
            "📤 Ask Question",
            type="primary",
            disabled=not question and not use_sherlock_ai,
        ):
            handle_question_submission(character, question, use_sherlock_ai)

    if st.button("🚪 End Interview", type="secondary"):
        st.session_state.selected_character = None
        st.session_state.current_page = "characters"
        st.rerun()


def handle_question_submission(character, question, use_sherlock_ai):
    """Handle question submission and response generation"""
    char_name = character.name

    # Create conversation state
    messages = []
    for msg in st.session_state.conversation_history[char_name]:
        if msg["type"] == "character":
            messages.append(HumanMessage(content=msg["content"]))
        else:
            messages.append(HumanMessage(content=msg["content"]))

    conv_state = {
        "character": character,
        "story_details": st.session_state.game_state["story_details"],
        "messages": messages,
    }

    if use_sherlock_ai:
        # Generate AI question
        ai_question = get_question(conv_state)
        st.session_state.conversation_history[char_name].append(
            {
                "type": "sherlock_ai",
                "content": ai_question,
                "timestamp": time.time(),
            }
        )

        # Generate character response
        messages.append(HumanMessage(content=ai_question))
        conv_state["messages"] = messages
        response_result = answer_question(conv_state)
        response = response_result["messages"][0].content

        st.session_state.conversation_history[char_name].append(
            {"type": "character", "content": response, "timestamp": time.time()}
        )

    elif question:
        st.session_state.conversation_history[char_name].append(
            {"type": "player", "content": question, "timestamp": time.time()}
        )

        # Generate character response
        messages.append(HumanMessage(content=question))
        conv_state["messages"] = messages
        response_result = answer_question(conv_state)
        response = response_result["messages"][0].content

        st.session_state.conversation_history[char_name].append(
            {"type": "character", "content": response, "timestamp": time.time()}
        )

    st.rerun()


def display_guessing_phase():
    """Handle the final guessing phase"""
    st.header("🎯 Final Deduction")

    game_state = st.session_state.game_state
    suspects = [c for c in game_state["characters"] if c.role.lower() != "victim"]

    st.markdown(f"**Guesses Remaining:** {game_state['num_guesses_left']} 🎲")
    st.subheader("🕵️ Who is the killer?")

    for i, suspect in enumerate(suspects):
        interviewed = suspect.name in st.session_state.conversation_history
        status = "✅ Interviewed" if interviewed else "❓ Not interviewed"

        col1, col2 = st.columns([3, 1])
        with col1:
            st.markdown(
                f"""
            <div class="character-card">
                <h4>{suspect.name} ({status})</h4>
                <p>{suspect.backstory}</p>
            </div>
            """,
                unsafe_allow_html=True,
            )

        with col2:
            if st.button(
                f"🎯 Accuse {suspect.name}", key=f"accuse_{i}", type="primary"
            ):
                make_accusation(suspect)

    if st.button("🔍 Continue Investigation", type="secondary"):
        st.session_state.current_phase = "investigation"
        st.rerun()


def make_accusation(accused_character):
    """Handle player accusation"""
    game_state = st.session_state.game_state
    killer = next(
        (c for c in game_state["characters"] if c.role.lower() == KILLER_ROLE), None
    )

    is_correct = accused_character.name == killer.name

    st.session_state.guesses_made.append(
        {
            "character": accused_character.name,
            "correct": is_correct,
            "timestamp": time.time(),
        }
    )

    if is_correct:
        st.session_state.game_result = "win"
        st.session_state.current_phase = "ended"
        game_state["result"] = "end"
        st.success(
            f"🎉 Congratulations! You correctly identified {accused_character.name} as the killer!"
        )
        st.balloons()
    else:
        game_state["num_guesses_left"] -= 1
        if game_state["num_guesses_left"] <= 0:
            st.session_state.game_result = "lose"
            st.session_state.current_phase = "ended"
            game_state["result"] = "end"
            st.error(
                f"💀 Game Over! The killer was {killer.name}. Better luck next time!"
            )
        else:
            st.error(
                f"❌ Wrong! {accused_character.name} is not the killer. You have {game_state['num_guesses_left']} guesses left."
            )
            game_state["result"] = "sherlock"

    st.rerun()


def display_investigation_phase():
    """Main investigation phase coordinator"""
    display_game_status()

    # Sidebar navigation
    st.sidebar.markdown("### 🧭 Navigation")

    navigation_buttons = [
        ("🏢 Crime Scene", "crime_scene"),
        ("👥 Characters", "characters"),
        ("🔍 Investigation", "investigation"),
    ]

    for label, page_key in navigation_buttons:
        button_type = (
            "primary" if st.session_state.current_page == page_key else "secondary"
        )
        if st.sidebar.button(label, type=button_type):
            st.session_state.current_page = page_key
            st.rerun()

    st.sidebar.markdown("---")

    if st.sidebar.button("🎯 Make Final Accusation", type="primary"):
        st.session_state.current_phase = "guessing"
        st.rerun()

    if st.sidebar.button("🔄 Reset Game", type="secondary"):
        for key in list(st.session_state.keys()):
            if key not in ["llm", "conversation_graph", "main_graph"]:
                del st.session_state[key]
        st.rerun()

    # Display current page content
    if st.session_state.current_phase == "guessing":
        display_guessing_phase()
    elif st.session_state.current_page == "crime_scene":
        display_crime_scene()
    elif st.session_state.current_page == "characters":
        display_characters()
    elif st.session_state.current_page == "investigation":
        display_character_interview()
