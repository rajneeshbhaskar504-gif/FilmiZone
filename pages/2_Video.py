import streamlit as st

st.set_page_config(page_title="Video", layout="wide")

st.title("🎬 Video Details")

st.image("https://via.placeholder.com/350x500.png?text=Thumbnail")

st.subheader("Video Title")

st.write("Category : Action")
st.write("Language : Hindi")
st.write("Duration : 18 Minutes")
st.write("Quality : Full HD")

st.markdown("---")

st.subheader("Description")

st.write("""
Yahan par video ki description ayegi.
Aap apni video ka description likh sakte ho.
""")

st.markdown("---")

if st.button("➡ Continue"):
    st.switch_page("pages/3_Verification_1.py")
