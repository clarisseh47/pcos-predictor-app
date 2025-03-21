import streamlit as st
def display_page():    
    st.title('Screening Quiz')
    BMI = st.radio('Is your BMI value...?',["Underweight", "Normal", "Overweight", "Obese"])