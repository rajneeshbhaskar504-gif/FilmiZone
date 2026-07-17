import streamlit as st
import time

st.set_page_config(page_title="Verification 1", layout="centered")

st.title("✅ Verification - Step 1")

st.info("Please wait 15 seconds before continuing.")

progress = st.progress(0)

for i in range(15):
    progress.progress((i + 1) / 15)
    st.write(f"⏳ {15 - i - 1} seconds remaining...")
    time.sleep(1)

st.success("Verification completed.")

if st.button("Next ➜"):
    st.switch_page("pages/4_verification_2.py")
