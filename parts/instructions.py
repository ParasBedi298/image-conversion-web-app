import streamlit as st

def instructions_page():
    st.markdown("- Item 1")
    st.markdown("- Item 2")
    st.markdown("- Item 3")

    # Apply CSS to indent the bullet points
    st.markdown('''
        <style>
            [data-testid="stMarkdownContainer"] ul {
                list-style-position: inside;
            }
        </style>
    ''', unsafe_allow_html=True)

    st.success('''**A Brief Note:**  

    Anything else we might wanna tell''')