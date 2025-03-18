import streamlit as st

st.title("PCOS Predictor")
st.write(
    "Here is our PCOS predictor web app!"
)
st.write(
    "By Risha and Reha"
)
st.sidebar.title("Background")
option = st.sidebar.selectbox("select",["Background"])

