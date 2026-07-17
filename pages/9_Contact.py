import streamlit as st

st.set_page_config(
    page_title="Contact",
    page_icon="📞",
    layout="wide"
)

st.title("📞 Contact Us")

name = st.text_input("Your Name")

email = st.text_input("Email")

message = st.text_area("Message")

if st.button("Send"):
    st.success("Message sent successfully.")
