import streamlit as st

st.set_page_config(
    page_title="Cinema Hub",
    page_icon="🎬",
    layout="wide"
)

st.title("🎬 Cinema Hub")
st.write("Welcome to Cinema Hub")

st.markdown("### 🔥 Latest Videos")

col1, col2 = st.columns(2)

with col1:
    st.image("https://via.placeholder.com/250x350.png?text=Video+1")
    st.write("Sample Video 1")

with col2:
    st.image("https://via.placeholder.com/250x350.png?text=Video+2")
    st.write("Sample Video 2")

st.info("➡️ Left sidebar se pages open kare.")
