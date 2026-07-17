import streamlit as st

st.set_page_config(
    page_title="Cinema Hub",
    page_icon="🎬",
    layout="wide"
)

st.title("🎬 Cinema Hub")
st.write("Welcome to Cinema Hub")

movie = st.text_input("🔍 Search Movie")

category = st.selectbox(
    "Select Category",
    [
        "All",
        "Hollywood",
        "Bollywood",
        "South",
        "Web Series"
    ]
)

if movie:
    st.success(f"Searching for: {movie}")

st.markdown("---")

st.subheader("🔥 Latest Movies")

st.image("https://via.placeholder.com/300x450.png?text=Movie+Poster", width=200)
st.write("Movie Name")
st.write("Genre : Action")
st.write("Language : Hindi")
st.button("View Details")
