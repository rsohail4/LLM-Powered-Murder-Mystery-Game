"""
Game end UI components
"""

import streamlit as st


def display_game_end():
    """Display game end screen"""
    st.header("🏁 Game Complete")

    if st.session_state.game_result == "win":
        st.success("🎉 Congratulations! You solved the mystery!")
    else:
        st.error("💀 The killer got away this time...")

    # Game statistics
    st.subheader("📊 Game Statistics")

    col1, col2, col3 = st.columns(3)

    with col1:
        st.metric("Characters Interviewed", len(st.session_state.conversation_history))

    with col2:
        st.metric("Guesses Made", len(st.session_state.guesses_made))

    with col3:
        st.metric("Clues Found", len(st.session_state.clues_discovered))

    # Show the detailed murder explanation
    if st.session_state.game_state:
        killer = next(
            (
                c
                for c in st.session_state.game_state["characters"]
                if c.role.lower() == "killer"
            ),
            None,
        )
        story = st.session_state.game_state["story_details"]

        if killer and story:
            st.markdown("---")
            st.header("🔍 The Complete Truth Revealed")

            # Killer Identity
            st.subheader("🎭 The Killer")
            st.markdown(
                f"""
            <div class="character-card" style="background: #ffebee; border-color: #f44336;">
                <h4>🔴 {killer.name}</h4>
                <p><strong>Background:</strong> {killer.backstory}</p>
            </div>
            """,
                unsafe_allow_html=True,
            )

            # Detailed Motive
            st.subheader("💭 The Motive")
            st.markdown(
                f"""
            <div class="clue-box" style="background: #fff3e0; border-color: #ff9800;">
                {story.killer_motive}
            </div>
            """,
                unsafe_allow_html=True,
            )

            # How the murder happened
            st.subheader("⚔️ How the Murder Was Committed")
            st.markdown(
                f"""
            <div class="clue-box" style="background: #fce4ec; border-color: #e91e63;">
                {story.murder_method_details}
            </div>
            """,
                unsafe_allow_html=True,
            )

            # Timeline
            st.subheader("⏰ Complete Timeline")
            st.markdown(
                f"""
            <div class="clue-box" style="background: #e8f5e8; border-color: #4caf50;">
                {story.complete_timeline}
            </div>
            """,
                unsafe_allow_html=True,
            )

            # Key Evidence
            st.subheader("🔎 Key Evidence")
            st.markdown(
                f"""
            <div class="clue-box" style="background: #e3f2fd; border-color: #2196f3;">
                {story.key_evidence}
            </div>
            """,
                unsafe_allow_html=True,
            )

            # Red Herrings Explained
            st.subheader("🎭 Red Herrings Explained")
            st.markdown(
                f"""
            <div class="clue-box" style="background: #f3e5f5; border-color: #9c27b0;">
                {story.red_herrings_explanation}
            </div>
            """,
                unsafe_allow_html=True,
            )

    # Play again button
    if st.button("🎮 Play Again", type="primary", use_container_width=True):
        # Reset session state
        for key in list(st.session_state.keys()):
            if key not in ["llm", "conversation_graph", "main_graph"]:
                del st.session_state[key]
        st.rerun()
