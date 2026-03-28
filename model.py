import streamlit as st

def load_model():
    if "HUGGINGFACE_API_KEY" not in st.secrets:
        raise Exception("API key not found. Please add it to secrets.toml")

    return st.secrets["HUGGINGFACE_API_KEY"]