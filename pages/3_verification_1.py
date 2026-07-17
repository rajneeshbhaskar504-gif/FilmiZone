import streamlit as st
import time

st.set_page_config(page_title="Verification 1", layout="centered")

st.title("🔐 Verification Step 1")

st.info("Please wait 15 seconds before continuing.")

progress = st.progress(0)

for i in range(15):
    time.sleep(1)
    progress.progress((i + 1) * 100 // 15)

st.success("✅ Verification Complete")

st.write("Advertisement Space")

if st.button("Next ➜"):
    st.switch_page("pages/4_Verification_2.py")
