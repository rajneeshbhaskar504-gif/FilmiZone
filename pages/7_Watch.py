import streamlit as st
import json

st.set_page_config(
    page_title="Watch Video",
    page_icon="🎬",
    layout="wide"
)

# वीडियो डेटा लोड करें
with open("data/videos.json", "r") as f:
    videos = json.load(f)

video = videos[0]

st.title(video["title"])

col1, col2 = st.columns([1,2])

with col1:
    st.image(video["thumbnail"], use_container_width=True)

with col2:
    st.write(f"📂 Category : {video['category']}")
    st.write(f"🌐 Language : {video['language']}")
    st.write(f"📅 Year : {video['year']}")
    st.write(f"⏱ Duration : {video['duration']}")
    st.write(f"👁 Views : {video['views']}")
    st.write(f"❤️ Likes : {video['likes']}")

st.markdown("---")

st.subheader("▶ Watch Online")

st.video(video["video"])

st.markdown("---")

st.subheader("📝 Description")

st.write(video["description"])

st.markdown("---")

st.subheader("⭐ Related Videos")

for item in videos:
    if item["id"] != video["id"]:
        st.write(f"🎬 {item['title']}")

st.markdown("---")

st.info("📢 Advertisement Space")
