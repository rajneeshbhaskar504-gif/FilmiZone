import streamlit as st

st.set_page_config(
    page_title="Watch Online",
    page_icon="▶️",
    layout="wide"
)

st.title("▶️ Watch Online")

st.video("https://www.w3schools.com/html/mov_bbb.mp4")

st.markdown("---")

st.subheader("Description")

st.write("""
Watch your uploaded video online.
You can replace this sample video with your own video later.
""")

st.markdown("---")

st.info("Advertisement Space")

st.button("⬅ Back")
