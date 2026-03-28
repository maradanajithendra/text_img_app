import streamlit as st
import time
from model import load_model
from generate import generate_image

# 🎨 Page Config
st.set_page_config(page_title="AI Image Generator", page_icon="🎨")

# 🎨 Custom CSS (Light Green Theme)
st.markdown("""
    <style>
    .stApp {
        background-color: #eaffea;
    }
    .title {
        text-align: center;
        color: green;
        font-size: 35px;
        font-weight: bold;
    }
    </style>
""", unsafe_allow_html=True)

st.markdown('<div class="title">🎨 AI Text-to-Image Generator</div>', unsafe_allow_html=True)

# 📦 Load API Key
@st.cache_resource
def get_model():
    return load_model()

api_key = get_model()

# 🧠 Session State for History
if "history" not in st.session_state:
    st.session_state.history = []

# ✏️ Prompt Input
prompt = st.text_input("Enter your prompt:")

# ⏱️ Timer Function
def countdown(sec):
    timer_placeholder = st.empty()
    for i in range(sec, 0, -1):
        timer_placeholder.info(f"⏳ Generating image in {i} sec...")
        time.sleep(1)
    timer_placeholder.empty()

# 🎯 Generate Button
if st.button("🚀 Generate Image"):
    if prompt.strip() == "":
        st.warning("Please enter a prompt")
    else:
        countdown(5)  # Timer before generation

        with st.spinner("Creating your image... 🎨"):
            try:
                image = generate_image(api_key, prompt)

                # Show Image
                st.image(image, caption="Generated Image", use_column_width=True)

                # Save to history
                st.session_state.history.append((prompt, image))

                # 💾 Download Button
                st.download_button(
                    label="📥 Download Image",
                    data=image.tobytes(),
                    file_name="generated_image.png",
                    mime="image/png"
                )

            except Exception as e:
                st.error(str(e))

# 📜 History Section
st.subheader("🕘 Image History")

if len(st.session_state.history) == 0:
    st.info("No images generated yet.")
else:
    for i, (p, img) in enumerate(st.session_state.history[::-1]):
        st.markdown(f"**Prompt:** {p}")
        st.image(img, width=300)

# 🗑️ Clear History Button
if st.button("🗑️ Clear History"):
    st.session_state.history = []
    st.success("History cleared successfully!")