import streamlit as st
def display_page():
    st.title("About Us") 
    col1, col2 = st.columns(2)
    col1.image('about_us.jpg', use_container_width=True)
    col2.write("Hi! We ore Risha and Reha. We are twin sisters and are 13 years old.  We live in NYC and are in 7th grade.  PCOS is a prominent issue that not enough people are aware of. Creating this web app is just the first step in our journey of increasing awareness to PCOS and how many women go undiagnosed per year.")