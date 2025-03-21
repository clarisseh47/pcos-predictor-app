import streamlit as st
import background
import screening

def display_home():
    st.title("PCOS Predictor")
    st.write(
        "Here is our PCOS predictor web app!"
    )
    st.write(
        "By Risha and Reha"
    )

st.sidebar.title("Menu")
option = st.sidebar.selectbox("select a page",['Home',"Background","Screening Quiz"])

if option == "Home":
    display_home()
elif option == "Background":
    background.display_page()
elif option == "Screening Quiz":
    screening.display_page()