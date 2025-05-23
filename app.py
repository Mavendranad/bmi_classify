import streamlit as st
import pickle
import numpy as np

# Load the trained BMI classification model
with open("bmi_class.pkl", "rb") as model_file:
    BMI = pickle.load(model_file)

# Title
st.title("BMI Classifier")
st.write("Enter your Height (cm) and Weight (kg) to get BMI classification")

# User Inputs
height = st.number_input("Enter Height (in cm)", min_value=100, max_value=250, value=170)
weight = st.number_input("Enter Weight (in kg)", min_value=30, max_value=200, value=65)

# Predict Button
if st.button("Classify"):
    # Convert height from cm to m for BMI calculation
    height_m = height / 100
    bmi = weight / (height_m ** 2)

    # Prepare input for model (you might need to adapt this depending on your model input)
    input_data = np.array([[weight, height]])  # Adjust if your model uses BMI instead

    # Make prediction
    prediction = BMI.predict(input_data)

    st.success(f"Based on the input, the BMI class is: **{prediction[0]}**")
    