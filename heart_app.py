import streamlit as st
import numpy as np
import joblib

model = joblib.load("heart_model.pkl")
scaler = joblib.load("scaler.pkl")

st.title("💓 Heart Disease Risk Predictor")
st.write("Enter patient data to evaluate heart failure risk:")

age = st.number_input("Age", min_value=1, max_value=120, value=50)
anaemia = st.selectbox("Anaemia", ["Yes", "No"])
creatinine_phosphokinase = st.number_input("Creatinine Phosphokinase (mcg/L)", min_value=10, max_value=10000, value=500)
diabetes = st.selectbox("Diabetes", ["Yes", "No"])
ejection_fraction = st.slider("Ejection Fraction (%)", min_value=10, max_value=80, value=40)
high_blood_pressure = st.selectbox("High Blood Pressure", ["Yes", "No"])
platelets = st.number_input("Platelets (kiloplatelets/mL)", min_value=10000, max_value=1000000, value=250000)
serum_creatinine = st.number_input("Serum Creatinine (mg/dL)", min_value=0.1, max_value=10.0, value=1.5)
serum_sodium = st.number_input("Serum Sodium (mEq/L)", min_value=100, max_value=200, value=140)
sex = st.selectbox("Sex", ["Male", "Female"])
smoking = st.selectbox("Smoking", ["Yes", "No"])
time = st.number_input("Follow-up Time (days)", min_value=1, max_value=300, value=120)

if st.button("Evaluate Risk"):

    inputs = np.array([[
        age,
        1 if anaemia == "Yes" else 0,
        creatinine_phosphokinase,
        1 if diabetes == "Yes" else 0,
        ejection_fraction,
        1 if high_blood_pressure == "Yes" else 0,
        platelets,
        serum_creatinine,
        serum_sodium,
        1 if sex == "Male" else 0,
        1 if smoking == "Yes" else 0,
        time
    ]])

    inputs_scaled = scaler.transform(inputs)

    pred = model.predict(inputs_scaled)[0]

    if pred == 1:
        st.error("⚠️ High risk of heart failure!")
    else:
        st.success("✅ Low risk of heart failure.")