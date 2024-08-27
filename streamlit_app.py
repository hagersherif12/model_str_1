import streamlit as st
import pickle

# Load the model
with open('diabetes_model.pkl', 'rb') as file:
    model = pickle.load(file)

# Set the title and a brief description
st.title("Diabetes Prediction")
st.write("This application predicts the likelihood of diabetes based on certain health metrics.")

# Add a sidebar for input fields
st.sidebar.header("Patient Input Features")

# Inputs in the sidebar
Pregnancies = st.sidebar.number_input('Pregnancies', min_value=0.0, max_value=20.0, value=1.0)
Glucose = st.sidebar.number_input('Glucose', min_value=0.0, max_value=200.0, value=85.0)
Insulin = st.sidebar.number_input('Insulin', min_value=0.0, max_value=300.0, value=30.0)
BMI = st.sidebar.number_input('BMI', min_value=0.0, max_value=70.0, value=20.0)
DiabetesPedigreeFunction = st.sidebar.number_input('Diabetes Pedigree Function', min_value=0.0, max_value=2.5, value=0.5)
Age = st.sidebar.number_input('Age', min_value=0.0, max_value=120.0, value=25.0)

# Prediction button
if st.sidebar.button('Predict'):
    # Make prediction
    output = model.predict([[Pregnancies, Glucose, Insulin, BMI, DiabetesPedigreeFunction, Age]])
    
    # Display result
    if output[0] == 1:
        st.success("The patient is likely to have diabetes.")
    else:
        st.warning("The patient is unlikely to have diabetes.")
else:
    st.write("Adjust the inputs and click 'Predict' to see the result.")

# Footer
st.markdown("---")
st.write("Developed with ❤️ by [Your Name]")
