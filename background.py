import streamlit as st
def display_page():
    col1, col2 = st.columns(2)
    col1.write('background')
    col2.image('page2.webp', caption='Source: lyndhurstgyn.com', use_container_width=True)