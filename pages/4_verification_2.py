import streamlit as st
import time

st.set_page_config(page_title="Verification 2", layout="centered")

st.title("✅ Verification - Step 2")

st.info("Please wait 15 seconds...")

progress = st.progress(0)

for i in range(15):
    progress.progress((i + 1) / 15)
    st.write(f"⏳ {15 - i - 1} seconds remaining")
    time.sleep(1)

st.success("Verification completed.")

if st.button("Next ➜"):
    st.switch_page("pages/5_verification_3.py")
