import streamlit as st
def display_page():
    st.title("Resources") 

    col1, col2,col3 = st.columns(3)
    col1.subheader ("Polycystic Ovary Syndrome (PCOS) and Women's Health")
    col1.write("Learn about National Institute of Child Health and Human Development’s (NICHD) research on PCOS and women's health. Here you will find recent advances in understanding, diagnosing, and treating PCOS. ")
    col2.subheader ("FAQ on Polycystic Ovary Syndrome (PCOS) ")
    col2.write("Review the Frequently Asked Questions and answers provided by the American College of Obstetricians and Gynecologists (ACOG). Here you will find information on symptoms and potential treatments for PCOS.")
    col3.subheader("FAQ on Polycystic Ovary Syndrome (PCOS)")
    col3.write("Learn about the connection between PCOS and Diabetes from the Centers for Disease Control and Prevention (CDC). Here you will find information about PCOS and diabetes and how the two health conditions are linked.")
    nih_url = "https://www.nichd.nih.gov/publications/product/532"
    col1.write("Learn more at this [link](%s)." % nih_url)
    acog_url = "https://www.acog.org/womens-health/faqs/polycystic-ovary-syndrome-pcos"
    col2.write("Learn more at this [link](%s)." % acog_url)
    cdc_url = "https://www.cdc.gov/diabetes/risk-factors/pcos-polycystic-ovary-syndrome.html"
    col3.write("Learn more at this [link](%s)." % cdc_url)