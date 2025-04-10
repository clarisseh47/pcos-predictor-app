import streamlit as st
def display_page():    
    st.title('Screening Quiz')
    height = st.number_input('How tall are you (in inches)?',min_value=1, max_value=100)
    weight = st.number_input ('How much do you weight (in pounds)?',min_value=1,max_value=1000)
    BMI = (weight/(height**2))*703
    BMI_input = 0.0
    if BMI<18.5:
        BMI_input=0.0
    elif BMI<25:
        BMI_input = 1.0
    elif BMI<30:
        BMI_input = 2.0
    else:
        BMI_input = 3.0
    MR = st.radio('Is your period regular or irregular?',['regular','irregular'])
    MR_input = 0.0
    if MR == "irregular":
        MR_input = 1.0
    hirsutism = st.radio('Do you have hirsutism? Hirsutism is excessive hair growth.',['No','Yes'])
    hirsutism_input = 0.0 
    if hirsutism == "Yes":
        hirsutism_input = 1.0
    AcneSeverity = st.radio('How would you describe your acne severity?',["No acne", "Mild", "Moderate", "Severe"])
    FamilyHistoryofPCOS = st.radio('Have any of your blood relatives been diagnosed with PCOS before?',["No", "Yes"])
    InsulinResistance = st.radio('Do you have insluin resistance?',["No", "Yes"])
    StressLevels = st.radio('What is your stresslevel?',["Low","Medium","High"])
    UrbanRural = st.radio('Do you live in a urban or rural area?',["Urban","Rural"])
    SocioeconomicStatus = st.radio('What is your socioeconomic status?',["Low","Middle","High"])
    FertilityConcerns = st.radio('Do you have fertility concern?',["No","Yes"])
    Ethnicity = st.radio('What is your ethnicity?',["African", "Asian", "Caucasian", "Hispanic", "Other"])
    


