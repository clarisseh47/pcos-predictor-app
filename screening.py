import streamlit as st
import pickle

def display_page():
    model_file_path = 'model.pkl'
    with open(model_file_path, 'rb') as f:
        screening_model = pickle.load(f)
    
    st.title('Screening Quiz')

    st.write('Fill out this screening quiz to see if you may be at risk of having PCOS.')
    st.write('DISCLAIMER: This information is provided for educational purposes only and is not a substitute for professional ' \
    'medical advice, diagnosis, or treatment. Always consult with a qualified healthcare provider regarding any questions ' \
    'you may have about your health.')

    # Questions for screening quiz. User answers are formatted for model input.
    height = st.number_input('How tall are you (in inches)?',min_value=1, max_value=100)
    weight = st.number_input ('How much do you weigh (in pounds)?',min_value=1,max_value=1000)
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
    MR = st.radio('Is your period regular or irregular?',['Regular','Irregular'])
    MR_input = 0.0
    if MR == "Irregular":
        MR_input = 1.0
    hirsutism = st.radio('Do you have hirsutism? Hirsutism is defined as excessive hair growth.',['No','Yes'])
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
    InsulinResistance = st.radio('Do you have insluin resistance? People with insulin resistance may have prediabetes '
    'or type 2 diabetes.',["No", "Yes"])
    InsulinResistance_input = 0.0
    if InsulinResistance == "Yes":
        InsulinResistance_input = 1.0
    StressLevels = st.radio('How would you rate your stress level?',["Low","Medium","High"])
    StressLevels_input = 0.0
    if StressLevels == "Low":
        StressLevels_input = 0.0
    elif StressLevels == "Medium":
        StressLevels_input = 1.0
    else: 
        StressLevels_input = 2.0
    UrbanRural = st.radio('Do you live in an urban or rural area?',["Urban","Rural"])
    UrbanRural_input = 0.0
    if UrbanRural == "Rural":
        UrbanRural_input = 1.0
    SocioeconomicStatus = st.radio("Which of the following best describes your household's socioeconomic status?",
                                   ["Low","Middle","High"])
    SS_input = 0.0
    if SocioeconomicStatus == "Low":
        SS_input = 0.0
    elif SocioeconomicStatus == "Middle":
        SS_input = 1.0
    else:
        SS_input = 2.0
    FertilityConcerns = st.radio('Do you have any concerns about your fertility? Fertility is defined as the ability ' \
    'to conceive or reproduce.',["No","Yes"])
    FertilityConcerns_input = 0.0
    if FertilityConcerns == "Yes":
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
    age_input = st.number_input('How old are you (in years)?',min_value=1, max_value=150)
    lifestyle_input = st.slider('How would you rate your current lifestyle in terms of adhering to healthy habits (diet, exercise, etc.), ' \
    'using a scale from 1 (very unhealthy) to 10 (very healthy)', 1, 10)
    
    if st.button('Submit'):
        input_data = [[BMI_input, MR_input, hirsutism_input, AcneSeverity_input, FamilyHistoryofPCOS_input, InsulinResistance_input, 
                       StressLevels_input, UrbanRural_input, SS_input, FertilityConcerns_input, Ethnicity_input, age_input, lifestyle_input]]
        prediction = screening_model.predict(input_data)
        if prediction[0] == 'Yes':
            st.write('You may be at risk of having PCOS. Please consult a healthcare provider if you are concerned you may have PCOS.')
        else:
            st.write('You may not be at risk of having PCOS. However, please consult your healthcare provider if you are concerned you may have PCOS.')

