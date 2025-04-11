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
    AcneSeverity_input = 0.0
    if AcneSeverity == "No acne":
        AcneSeverity_input = 0.0
    elif AcneSeverity == "Mild":
        AcneSeverity_input = 1.0
    elif AcneSeverity == "Moderate":
        AcneSeverity_input = 2.0
    else: 
        AcneSeverity_input = 3.0
    FamilyHistoryofPCOS = st.radio('Have any of your blood relatives been diagnosed with PCOS before?',["No", "Yes"])
    FamilyHistoryofPCOS_input = 0.0
    if FamilyHistoryofPCOS == "Yes":
        FamilyHistoryofPCOS_input = 1.0
    InsulinResistance = st.radio('Do you have insluin resistance?',["No", "Yes"])
    InsulinResistance_input = 0.0
    if InsulinResistance == "Yes":
        InsulinResistance_input = 1.0
    StressLevels = st.radio('What is your stresslevel?',["Low","Medium","High"])
    StressLevels_input = 0.0
    if StressLevels == "Low":
        StressLevels_input = 0.0
    elif StressLEvels == "Medium":
        StressLevels_input = 1.0
    else: 
        StressLevels_input = 2.0
    UrbanRural = st.radio('Do you live in a urban or rural area?',["Urban","Rural"])
    UrbanRural_input = 0.0
    if UrbanRural == "Rural":
        UrbanRural_input = 1.0
    SocioeconomicStatus = st.radio('What is your socioeconomic status?',["Low","Middle","High"])
    SS_input = 0.0
    if SocioeconomicStatus == "Low":
        SS_input = 0.0
    elif SocioeconomicStatus == "Medium":
        SS_input = 1.0
    else:
        SS_input = 2.0
    FertilityConcerns = st.radio('Do you have fertility concern?',["No","Yes"])
    FertilityConcerns_input = 0.0
    if FertilityConcerns == "Yes"
        FertilityConcerns_input = 1.0
    Ethnicity = st.radio('What is your ethnicity?',["African", "Asian", "Caucasian", "Hispanic", "Other"])
    Ethnicity_input = 0.0
    if Ethnicity == "African":
        Ethnicity_input == 0.0
    elif Ethnicity == "Asian":
        Ethnicity_input == 1.0
    elif Ethnicity == "Caucasian":
        Ethnicity_input == 2.0
    elif Ethnicity == "Hispanic":
        Ethnicity_input == 3.0
    else:
        Ethnicity_input == 4.0
    


