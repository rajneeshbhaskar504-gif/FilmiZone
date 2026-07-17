import streamlit as st

st.set_page_config(page_title="Home", layout="wide")

st.title("🎬 Cinema Hub")

search = st.text_input("🔍 Search Video")

category = st.selectbox(
    "Category",
    [
        "All",
        "Action",
        "Comedy",
        "Horror",
        "South",
        "Hollywood",
        "Bollywood",
        "Web Series"
    ]
)

st.markdown("---")

col1, col2, col3 = st.columns(3)

with col1:
    st.image("https://via.placeholder.com/250x350.png?text=Video+1")
    st.write("Video 1")

with col2:
    st.image("https://via.placeholder.com/250x350.png?text=Video+2")
    st.write("Video 2")

with col3:
    st.image("https://via.placeholder.com/250x350.png?text=Video+3")
    st.write("Video 3")
