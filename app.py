import pickle
import streamlit as st  
from streamlit_option_menu import option_menu

# Set page configuration
st.set_page_config(page_title="Health Predictor",
                   layout="wide",
                   page_icon="🧑‍⚕️")

# Loading the saved models 
diabetes_model = pickle.load(open('Diabetes_model.sav', 'rb'))
heart_disease_model = pickle.load(open('Heart_disease_model.sav', 'rb'))
parkinsons_model = pickle.load(open('parkinsons_model.sav', 'rb'))

# sidebar for navigation 
with st.sidebar:
    selected = option_menu('Health care',
                           ['Home', 'User Guide',
                            'Diabetes Prediction',
                            'Heart Disease Prediction',
                            'Parkinsons Prediction'],
                           menu_icon='hospital',
                           icons=['house','book','activity', 'heart', 'person'], 
                           default_index=0)
st.title("Health Predictor")

# home 
if(selected == "Home"):
    st.header("Home")
    image_path = r"C:\Users\Vishwa\Desktop\Healthcare\home.jpg"
    st.image(image_path,use_column_width=True)
    st.markdown("""
 ### **Welcome to the Health Predictor System!** 🧑‍⚕️

    Our platform is designed to empower individuals with early health risk detection, using advanced machine learning models to predict potential conditions like **Diabetes**, **Heart Disease**, and **Parkinson’s Disease**. Early detection is crucial in managing and preventing serious health issues, and our system aims to provide a reliable, accessible solution for everyone.

    ### Key Features:
    - **Multiple Health Predictions**: From Diabetes to Heart and Parkinson's Disease, the system analyzes a variety of conditions.
    - **Easy-to-Use Interface**: Simply enter your health metrics, and get a detailed analysis with one click.
    - **Fast and Accurate Results**: Our machine learning models are trained on high-quality datasets to give you fast and reliable predictions.
    
    ### Why Early Detection Matters:
    Early detection is a critical factor in successful treatment and management of chronic diseases. By utilizing data-driven insights, individuals can take proactive steps to improve their health and well-being.

    **Let’s work together to build a healthier future!**

    """)

#About Project
elif(selected  == "User Guide"):
    st.header("User Guide")
    st.markdown("""
   ### Welcome to the Health Predictor User Guide
   This guide will help you navigate through the system and make the most out of its features. Follow these simple steps to get started:

   ### How to Use the System:
    1. **Select a Prediction Category**: Choose from Diabetes, Heart Disease, or Parkinson’s Prediction.
    2. **Enter Your Details**: Input the required health data like age, blood pressure, cholesterol levels, etc. Make sure the information is accurate for the best results.
    3. **Get Your Prediction**: After submitting your details, the system will analyze the data using machine learning algorithms and present you with a prediction.
    4. **Review Your Results**: The results will show the likelihood of having the condition, along with personalized recommendations for further medical consultation if needed.

    ### Detailed Features:
    - **Health Data Input**: For each condition, the system requires specific health metrics, such as glucose levels for diabetes or resting blood pressure for heart disease. Follow the form carefully for each prediction.
    - **Advanced Machine Learning**: The system uses pre-trained models based on real patient data to make accurate and fast predictions.
    - **Data Security**: Your health data is treated with utmost confidentiality, ensuring your privacy is maintained.

    ### Important Notes:
    - The predictions provided by this system are **not a substitute for professional medical advice**. Always consult a doctor for accurate diagnosis and treatment.
    - The system is designed to assist in early detection, but it does not guarantee 100% accuracy. Please use it as a tool for proactive health management.

    ### Tips for Best Results:
    - **Accuracy of Data**: The quality of the prediction depends on the data you input. Ensure you enter valid and recent health metrics.
    - **Interpret Results with Caution**: Use the results as guidance and consult a medical professional for further action.
    
    ### Need Help?
    - If you're unsure about how to use a feature or interpret your results, you can always contact us via  email us at support@healthpredictor.com.
    
    We hope this guide helps you in navigating the Health Predictor platform effectively!
    """)


# Diabetes Prediction Page
if (selected == 'Diabetes Prediction'):
    
    # page title
    st.subheader('Diabetes Prediction')
    
# Getting the input data from the user
    col1, col2, col3 = st.columns(3)
    
    with col1:
        Pregnancies = st.text_input('Number of Pregnancies')

    with col2:
        Glucose = st.text_input('Glucose Level')
    
    with col3:
        BloodPressure = st.text_input('Blood Pressure value')
    
    with col1:
        SkinThickness = st.text_input('Skin Thickness value')
    
    with col2:
        Insulin = st.text_input('Insulin Level')
    
    with col3:
        BMI = st.text_input('BMI value')
    
    with col1:
        DiabetesPedigreeFunction = st.text_input('Diabetes Pedigree Function value')
    
    with col2:
        Age = st.text_input('Age of the Person')
# code for Prediction
    diab_diagnosis = ''
# creating a button for Prediction 
    if st.button('Diabetes Test Result'):
        diab_prediction = diabetes_model.predict([[Pregnancies, Glucose, BloodPressure, SkinThickness, Insulin, BMI, DiabetesPedigreeFunction, Age]])
        
        if (diab_prediction[0] == 1):
          diab_diagnosis = 'The person is afflicted with diabetes.'
        else:
          diab_diagnosis = 'The person is not afflicted with diabetes.'
        
    st.success(diab_diagnosis)
     
# Heart disease Prediction Page    
if (selected == 'Heart Disease Prediction'):
    
    # page title
    st.subheader('Heart Disease Prediction')
    
    col1, col2, col3 = st.columns(3)
    
    with col1:
        age = st.text_input('Age')
        
    with col2:
        sex = st.text_input('Sex')
        
    with col3:
        cp = st.text_input('Chest Pain types')
        
    with col1:
        trestbps = st.text_input('Resting Blood Pressure')
        
    with col2:
        chol = st.text_input('Serum Cholestoral in mg/dl')
        
    with col3:
        fbs = st.text_input('Fasting Blood Sugar > 120 mg/dl')
        
    with col1:
        restecg = st.text_input('Resting Electrocardiographic results')
        
    with col2:
        thalach = st.text_input('Maximum Heart Rate achieved')
        
    with col3:
        exang = st.text_input('Exercise Induced Angina')
        
    with col1:
        oldpeak = st.text_input('ST depression induced by exercise')
        
    with col2:
        slope = st.text_input('Slope of the peak exercise ST segment')
        
    with col3:
        ca = st.text_input('Major vessels colored by flourosopy')
        
    with col1:
        thal = st.text_input('thal: 0 = normal; 1 = fixed defect; 2 = reversable defect')     
 
    # code for Prediction
    heart_diagnosis = ''
    if st.button('Heart Disease Test Result'):

        user_input = [age, sex, cp, trestbps, chol, fbs, restecg, thalach, exang, oldpeak, slope, ca, thal]

        user_input = [float(x) for x in user_input]

        heart_prediction = heart_disease_model.predict([user_input])
    
        if (heart_prediction[0] == 1):
            heart_diagnosis = 'The person is suffering from heart disease.'
        else:
            heart_diagnosis = 'The person is not suffering from heart disease.'
    st.success(heart_diagnosis)
    
#parkinsons prediction page 
if(selected == "Parkinsons Prediction"):
    
    #Page title
    st.subheader("Parkinson's Predction")
    col1, col2, col3, col4, col5 = st.columns(5) 
    with col1:
        fo = st.text_input('MDVP:Fo(Hz)')
    with col2:
        fhi = st.text_input('MDVP: Fhi(Hz)')
    with col3:
        flo = st.text_input('MDVP: Flo(Hz)')
    with col4:
        Jitter_percent = st.text_input('MDVP:Jitter(%)')    
    with col5:
        Jitter_Abs = st.text_input('MDVP:Jitter(Abs)')
   
    with col1:
        RAP = st.text_input('MDVP:RAP')
        
    with col2:
        PPQ = st.text_input('MDVP:PPQ')
        
    with col3:
        DDP = st.text_input('Jitter:DDP')
        
    with col4:
        Shimmer = st.text_input('MDVP:Shimmer')
        
    with col5:
        Shimmer_dB = st.text_input('MDVP:Shimmer(dB)')
        
    with col1:
        APQ3 = st.text_input('Shimmer:APQ3')
        
    with col2:
        APQ5 = st.text_input('Shimmer:APQ5')
        
    with col3:
        APQ = st.text_input('MDVP:APQ')
        
    with col4:
        DDA = st.text_input('Shimmer:DDA')
        
    with col5:
        NHR = st.text_input('NHR')
        
    with col1:
        HNR = st.text_input('HNR')
        
    with col2:
        RPDE = st.text_input('RPDE')
        
    with col3:
        DFA = st.text_input('DFA')
        
    with col4:
        spread1 = st.text_input('spread1')
        
    with col5:
        spread2 = st.text_input('spread2')
        
    with col1:
        D2 = st.text_input('D2')
        
    with col2:
        PPE = st.text_input('PPE')
    # code for Prediction
    parkinsons_diagnosis = ''
    
    # creating a button for Prediction    
    if st.button("Parkinson's Test Result"):
        parkinsons_prediction = parkinsons_model.predict([[fo, fhi, flo, Jitter_percent, Jitter_Abs, RAP, PPQ, DDP, Shimmer, Shimmer_dB, APQ3, APQ5, APQ, DDA, NHR, HNR, RPDE, DFA, spread1, spread2, D2, PPE]])                          
        
        if (parkinsons_prediction[0] == 1):
          parkinsons_diagnosis = "The person is afflicted with Parkinson's disease."
        else:
          parkinsons_diagnosis = "The person is not afflicted with Parkinson's disease"
            
        st.success(parkinsons_diagnosis)
        
        
def set_bg_from_url(url, opacity=1):
    footer = """
    <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.2.0/dist/css/bootstrap.min.css" rel="stylesheet" integrity="sha384-gH2yIJqKdNHPEq0n4Mqa/HGKIhSkIHeL5AyhkYV8i59U5AR6csBvApHHNl/vI1Bx" crossorigin="anonymous">
    <footer>
        <div style='visibility: visible;margin-top:7rem;justify-content:center;display:flex;'>
            <p style="font-size:1.1rem;">
                 Made by Vishwa Nayak
                &nbsp;
                <a href="https://www.linkedin.com/in/vishwanayak/">
                    <svg xmlns="http://www.w3.org/2000/svg" width="23" height="23" fill="Black" class="bi bi-linkedin" viewBox="0 0 16 16">
                    <path d="M0 1.146C0 .513.526 0 1.175 0h13.65C15.474 0 16 .513 16 1.146v13.708c0 .633-.526 1.146-1.175 1.146H1.175C.526 16 0 15.487 0 14.854V1.146zm4.943 12.248V6.169H2.542v7.225h2.401zm-1.2-8.212c.837 0 1.358-.554 1.358-1.248-.015-.709-.52-1.248-1.342-1.248-.822 0-1.359.54-1.359 1.248 0 .694.521 1.248 1.327 1.248h.016zm4.908 8.212V9.359c0-.216.016-.432.08-.586.173-.431.568-.878 1.232-.878.869 0 1.216.662 1.216 1.634v3.865h2.401V9.25c0-2.22-1.184-3.252-2.764-3.252-1.274 0-1.845.7-2.165 1.193v.025h-.016a5.54 5.54 0 0 1 .016-.025V6.169h-2.4c.03.678 0 7.225 0 7.225h2.4z"/>
                    </svg>          
                </a>
                &nbsp;
                <a href="https://github.com/VishwaNayak1812">
                    <svg xmlns="http://www.w3.org/2000/svg" width="23" height="23" fill="Black" class="bi bi-github" viewBox="0 0 16 16">
                        <path d="M8 0C3.58 0 0 3.58 0 8c0 3.54 2.29 6.53 5.47 7.59.4.07.55-.17.55-.38 0-.19-.01-.82-.01-1.49-2.01.37-2.53-.49-2.69-.94-.09-.23-.48-.94-.82-1.13-.28-.15-.68-.52-.01-.53.63-.01 1.08.58 1.23.82.72 1.21 1.87.87 2.33.66.07-.52.28-.87.51-1.07-1.78-.2-3.64-.89-3.64-3.95 0-.87.31-1.59.82-2.15-.08-.2-.36-1.02.08-2.12 0 0 .67-.21 2.2.82.64-.18 1.32-.27 2-.27.68 0 1.36.09 2 .27 1.53-1.04 2.2-.82 2.2-.82.44 1.1.16 1.92.08 2.12.51.56.82 1.27.82 2.15 0 3.07-1.87 3.75-3.65 3.95.29.25.54.73.54 1.48 0 1.07-.01 1.93-.01 2.2 0 .21.15.46.55.38A8.012 8.012 0 0 0 16 8c0-4.42-3.58-8-8-8z"/>
                    </svg>
                </a>
            </p>
        </div>
    </footer>
"""
    st.markdown(footer, unsafe_allow_html=True)
   # Set background image using HTML and CSS
    st.markdown(
        f"""
        <style>
            body {{
                background: url('{url}') no-repeat center center fixed;
                background-size: cover;
                opacity: {opacity};
            }}
        </style>
        """,
        unsafe_allow_html=True
    )

# Set background image from URL
if selected != "Home":
        set_bg_from_url("https://www.training.com.au/wp-content/uploads/TR_Healthcare-Medical-Trends_Feature.png", opacity=0.875)