import streamlit as st
import background
import screening
import resources 
import about_us

def display_home():
    col1, col2 = st.columns(2)
    col1.image('PCOSense_logo.png', use_container_width=True)
    col1.write('Disclaimer: This information is provided for educational purposes only '
    'and is not a substitute for professional medical advice, diagnosis, or treatment. ' \
    'Always consult with a qualified healthcare provider regarding any questions you may ' \
    'have about your health or before making any decisions related to your medical condition.')
    
    col2a, col2b = col2.columns(2)
    url = 'https://stock.adobe.com/search?k=pcos'
    col2a.image('page1_left.jpg', caption='[Image Source](%s)' % url, use_container_width=True)
    col2b.image('page1_right.jpg', caption='[Image Source](%s)' % url, use_container_width=True)
    col2.write('We want to bring awareness to Polycystic Ovary Syndrome (PCOS). ' \
    'Through this web application, users can take a screening quiz, which uses a machine ' \
    'learning model to predict if an individual may have PCOS. ')


st.sidebar.title("Menu")
option = st.sidebar.selectbox("select a page",['Home',"Background","Screening Quiz","Treatments + Resources","About Us"])

if option == "Home":
    display_home()
elif option == "Background":
    background.display_page()
elif option == "Screening Quiz":
    screening.display_page()
elif option == "Resources":
    resources.display_page()
elif option == "About Us":
    about_us.display_page()