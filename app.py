import streamlit as st

st.set_page_config(
    page_title="FilmiZone",
    page_icon="🎬",
    layout="wide"
)

st.markdown("""
<style>
#MainMenu{visibility:hidden;}
footer{visibility:hidden;}
header{visibility:hidden;}

.block-container{
    padding-top:1rem;
}

.navbar{
    background:#111;
    padding:15px;
    border-radius:12px;
}

.logo{
    color:#ff0000;
    font-size:35px;
    font-weight:bold;
}

.banner{
    background:linear-gradient(to right,#111,#222,#333);
    padding:40px;
    border-radius:15px;
    margin-top:20px;
}

.moviecard{
    background:#181818;
    padding:15px;
    border-radius:12px;
}
</style>
""", unsafe_allow_html=True)

st.markdown("""
<div class="navbar">
<div class="logo">🎬 FilmiZone</div>
</div>
""", unsafe_allow_html=True)

st.markdown("""
<div class="banner">
<h1>Unlimited Movies & Web Series</h1>
<p>Watch Your Favourite Videos</p>
</div>
""", unsafe_allow_html=True)
