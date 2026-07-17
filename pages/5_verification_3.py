import streamlit as st
import time

st.set_page_config(
    page_title="Verification 3",
    page_icon="🔒",
    layout="centered"
)

st.title("🔒 Verification Step 3")

st.warning("Final verification is in progress...")

progress = st.progress(0)

for i in range(15):
    time.sleep(1)
    progress.progress((i + 1) * 100 // 15)

st.success("✅ Verification Step 3 Completed")

st.markdown("---")

st.subheader("Advertisement")

st.info("Your ad will appear here.")

if st.button("Continue ➜"):
    st.switch_page("pages/6_Verification_4.py")
