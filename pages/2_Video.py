import streamlit as st
import json

st.set_page_config(page_title="Video", layout="wide")

with open("data/videos.json", "r") as f:
    videos = json.load(f)

video = videos[0]

st.title(video["title"])

st.image(video["thumbnail"], width=300)

st.write("### Video Information")

st.write("📂 Category :", video["category"])
st.write("🌐 Language :", video["language"])

if "year" in video:
    st.write("📅 Year :", video["year"])

if "duration" in video:
    st.write("⏱ Duration :", video["duration"])

if "description" in video:
    st.write(video["description"])

st.markdown("---")

if st.button("Continue ➜"):
    st.switch_page("pages/3_verification_1.py")
