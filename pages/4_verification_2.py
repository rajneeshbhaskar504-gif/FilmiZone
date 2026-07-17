import streamlit as st
import time

st.set_page_config(page_title="Verification 2", layout="centered")

st.title("🛡️ Verification Step 2")

st.info("Please wait 15 seconds...")

progress = st.progress(0)

for i in range(15):
    time.sleep(1)
    progress.progress((i + 1) * 100 // 15)

st.success("✅ Verification Complete")

st.markdown("## Advertisement")
st.write("Ad Space")

if st.button("Next ➜"):
    st.switch_page("pages/5_Verification_3.py")
