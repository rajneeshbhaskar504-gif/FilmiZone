import streamlit as st
import json

st.set_page_config(page_title="FilmiZone", layout="wide")

st.title("🎬 FilmiZone")

search = st.text_input("🔍 Search Video")

# श्रेणी (Category) का चयन करने के लिए
category = st.selectbox(
    "📂 Select Category",
    ["All", "Hollywood", "Bollywood", "South", "Web Series"]
)

st.markdown("## 🔥 Trending Videos")

# डेटा लोड करना
try:
    with open("data/videos.json", "r") as f:
        videos = json.load(f)
except FileNotFoundError:
    videos = []

# वीडियो लिस्टिंग
for video in videos:
    vid_title = video.get("title", "Untitled")
    vid_category = video.get("category", "Unknown")
    vid_language = video.get("language", "N/A")
    vid_thumbnail = video.get("thumbnail", "")
    vid_id = video.get("id", "0")

    # श्रेणी और सर्च के आधार पर फ़िल्टरिंग
    if category != "All" and vid_category != category:
        continue

    if search.lower() not in vid_title.lower():
        continue

    col1, col2 = st.columns([1, 2])

    with col1:
        # इमेज चेक (सुधार 1)
        if vid_thumbnail:
            st.image(vid_thumbnail, width=180)
        else:
            st.write("🖼️ No Thumbnail")

    with col2:
        st.subheader(vid_title)
        st.write("Category:", vid_category)
        st.write("Language:", vid_language)

        # यूनिक key के साथ बटन
        if st.button("▶ Watch Now", key=f"watch_{vid_id}"):
            st.switch_page("pages/2_Video.py")

# --- Featured Videos सेक्शन ---
st.markdown("---")
st.header("⭐ Featured Videos")

if videos:
    cols = st.columns(3)
    # पहले 3 वीडियो दिखाएं
    for i, video in enumerate(videos[:3]):
        with cols[i % 3]:
            # Featured में इमेज चेक (सुधार 2)
            thumb = video.get("thumbnail", "")
            if thumb:
                st.image(thumb, use_container_width=True)
            else:
                st.write("🖼️ No Thumbnail")
                
            st.write(f"**{video.get('title', 'Untitled')}**")
            st.caption(video.get("category", "N/A"))
else:
    st.info("Currently, there are no featured videos available.")


