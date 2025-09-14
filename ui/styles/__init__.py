"""
Custom styling for the Streamlit app
"""

import streamlit as st
from pathlib import Path


def load_custom_css():
    """Load custom CSS for the Streamlit app"""
    css_file = Path(__file__).parent / "custom.css"

    if css_file.exists():
        with open(css_file) as f:
            css_content = f.read()

        st.markdown(f"<style>{css_content}</style>", unsafe_allow_html=True)
    else:
        # Fallback CSS if file not found
        st.markdown(
            """
        <style>
        .main-header {
            background: linear-gradient(90deg, #1e3c72 0%, #2a5298 100%);
            padding: 1rem;
            border-radius: 10px;
            color: white;
            text-align: center;
            margin-bottom: 2rem;
        }
        .character-card {
            background: #f8f9fa;
            border: 1px solid #dee2e6;
            border-radius: 8px;
            padding: 1rem;
            margin: 0.5rem 0;
            box-shadow: 0 2px 4px rgba(0,0,0,0.1);
        }
        </style>
        """,
            unsafe_allow_html=True,
        )
