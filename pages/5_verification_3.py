import streamlit as st
import time

st.set_page_config(page_title="Verification 3", layout="centered")

st.title("✅ Final Verification")

st.info("Final verification in progress. Please wait 15 seconds.")

progress = st.progress(0)

status = st.empty()

for i in range(15):
    progress.progress((i + 1) / 15)
    status.write(f"⏳ {15 - i - 1} seconds remaining...")
    time.sleep(1)

status.empty()

st.success("✅ Verification Completed Successfully!")

if st.button("🎬 Continue to Watch"):
    st.switch_page("pages/7_Watch.py")
