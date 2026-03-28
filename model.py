<<<<<<< HEAD
import streamlit as st

def load_model():
    if "HUGGINGFACE_API_KEY" not in st.secrets:
        raise Exception("API key not found. Please add it to secrets.toml")

=======
import streamlit as st

def load_model():
    if "HUGGINGFACE_API_KEY" not in st.secrets:
        raise Exception("API key not found. Please add it to secrets.toml")

>>>>>>> 031879b8208dc1e91ff69d266f3b9ccc2159bd37
    return st.secrets["HUGGINGFACE_API_KEY"]