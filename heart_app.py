import streamlit as st
import numpy as np
import joblib

model = joblib.load("heart_model.pkl")
scaler = joblib.load("scaler.pkl")

st.title("💓 Heart Disease Risk Predictor")
st.write("Enter patient details below to assess risk level:")

age = st.number_input("Age", min_value=1, max_value=120, value=50)
high_blood_pressure = st.selectbox("High Blood Pressure", ["Yes", "No"])
ejection_fraction = st.slider("Ejection Fraction (%)", min_value=10, max_value=80, value=40)
serum_creatinine = st.number_input("Serum Creatinine (mg/dL)", min_value=0.1, max_value=20.0, value=1.5)
serum_sodium = st.number_input("Serum Sodium (mEq/L)", min_value=100, max_value=200, value=140)

if st.button("Evaluate Risk"):
    user_inputs = np.array([[
        age,
        1 if high_blood_pressure == "Yes" else 0,
        ejection_fraction,
        serum_creatinine,
        serum_sodium
    ]])

    user_inputs_scaled = scaler.transform(user_inputs)

    pred = model.predict(user_inputs_scaled)[0]

    if pred == 1:
        st.error("⚠️ High risk of heart disease!")
    else:
        st.success("✅ Low risk of heart disease.")