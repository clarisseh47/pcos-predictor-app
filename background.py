import streamlit as st
def display_page():
    st.title('Background')
    col1, col2 = st.columns(2)
    col2.image('page2.webp', caption='Source: lyndhurstgyn.com', use_container_width=True)
    col1.write ('Polycystic ovary syndrome (PCOS) is a reproductive disorder among women that affects their hormone levels. Women with PCOS struggle with the growth and reproduction of eggs in their ovaries due to their hormonal imbalances. Hormone imbalances impact fertility by making it harder for a woman to get pregnant and making them more prone to a miscarriage. Hormonal imbalances can also cause an irregular menstrual cycle, excess hair growth, and acne.')

    col1.write ('We developed this app to help educate people on PCOS. Additionally, it’s important for women to be aware of what is happening to their body and what other medical complications might occur if they have PCOS.')