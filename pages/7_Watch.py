import streamlit as st
import json

st.set_page_config(
    page_title="Watch Online",
    page_icon="🎬",
    layout="wide"
)

with open("data/videos.json", "r") as f:
    videos = json.load(f)

video = videos[0]

st.title(video["title"])

col1, col2 = st.columns([1,2])

with col1:
    st.image(video["thumbnail"], width=300)

with col2:
    st.write("### Video Information")
    st.write("📂 Category :", video["category"])
    st.write("🌐 Language :", video["language"])

    if "year" in video:
        st.write("📅 Year :", video["year"])

    if "duration" in video:
        st.write("⏱ Duration :", video["duration"])

st.markdown("---")

st.subheader("▶ Watch Online
