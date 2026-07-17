import streamlit as st
import json

st.set_page_config(page_title="Admin Panel", layout="wide")

st.title("🔐 Admin Panel")

password = st.text_input("Enter Admin Password", type="password")

if password == "12345":

    st.success("Login Successful")

    title = st.text_input("Video Title")
    category = st.selectbox(
        "Category",
        ["Hollywood", "Bollywood", "South", "Web Series"]
    )
    language = st.text_input("Language")
    year = st.text_input("Year")
    duration = st.text_input("Duration")
    thumbnail = st.text_input("Thumbnail URL")
    video = st.text_input("Video URL")
    description = st.text_area("Description")

    if st.button("Save Video"):

        try:
            with open("data/videos.json", "r") as f:
                videos = json.load(f)
        except:
            videos = []

        videos.append({
            "id": len(videos)+1,
            "title": title,
            "category": category,
            "language": language,
            "year": year,
            "duration": duration,
            "thumbnail": thumbnail,
            "video": video,
            "description": description,
            "views": 0,
            "likes": 0,
            "featured": False
        })

        with open("data/videos.json", "w") as f:
            json.dump(videos, f, indent=4)

        st.success("Video Saved Successfully")

else:
    st.warning("Enter Correct Password")
