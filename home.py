import streamlit as st
import background
import screening
import resources 
import about_us

def display_home():
    st.title("PCOS Predictor")
    st.write(
        "Here is our PCOS predictor web app!"
    )
    st.write(
        "By Risha and Reha"
    )

st.sidebar.title("Menu")
option = st.sidebar.selectbox("select a page",['Home',"Background","Screening Quiz","Treatments + Resources","About Us"])

if option == "Home":
    display_home()
elif option == "Background":
    background.display_page()
elif option == "Screening Quiz":
    screening.display_page()
elif option == "Treatments + Resources":
    resources.display_page()
elif option == "About Us":
    about_us.display_page()