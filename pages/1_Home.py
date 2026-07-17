import streamlit as st
import json

st.set_page_config(page_title="FilmiZone", layout="wide")

st.title("🎬 FilmiZone")

search = st.text_input("🔍 Search Video")

category = st.selectbox(
    "📂 Select Category",
    [
        "All",
        "Hollywood",
        "Bollywood",
        "South",
        "Web Series"
    ]
)

st.markdown("## 🔥 Trending Videos")
try:
    with open("data/videos.json", "r") as f:
        videos = json.load(f)
except:
    videos = []

for video in videos:
        if category != "All" and video["category"] != category:
        continue

    if search.lower() not in video["title"].lower():
        continue
    if search.lower() in video["title"].lower():
        col1, col2 = st.columns([1,2])

        with col1:
            st.image(video["thumbnail"], width=180)

        with col2:
            st.subheader(video["title"])
            st.write("Category:", video["category"])
            st.write("Language:", video["language"])

            if st.button(f"Watch Now {video['id']}"):
                st.switch_page("pages/2_Video.py")
