{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 5,
   "id": "c0b4e02a-3a42-4c33-a589-8ebcc6617fde",
   "metadata": {},
   "outputs": [],
   "source": [
    "import streamlit as st\n",
    "import pickle\n",
    "import numpy as np\n",
    "\n",
    "with open(\"heart_model.pkl\", \"rb\") as file:\n",
    "    model = pickle.load(file)\n",
    "\n",
    "st.title(\"💓 Heart Disease Risk Predictor\")\n",
    "\n",
    "age = st.slider(\"Age\", 0, 100)\n",
    "ejection_fraction = st.slider(\"Ejection Fraction (%)\", 10, 70)\n",
    "serum_creatinine = st.number_input(\"Serum Creatinine\")\n",
    "serum_sodium = st.number_input(\"Serum Sodium\")\n",
    "high_blood_pressure = st.selectbox(\"High Blood Pressure\", [\"Yes\", \"No\"])\n",
    "\n",
    "features = np.array([[\n",
    "    age,\n",
    "    1 if high_blood_pressure == \"Yes\" else 0,\n",
    "    ejection_fraction,\n",
    "    serum_creatinine,\n",
    "    serum_sodium\n",
    "]])\n",
    "\n",
    "if st.button(\"Evaluate Risk\"):\n",
    "    pred = model.predict(features)[0]\n",
    "    st.success(\"⚠️ High risk of heart disease!\" if pred == 1 else \"✅ Low risk\")"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "aea8d51b-5363-4931-9ee4-151e4735d7b9",
   "metadata": {},
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python [conda env:base] *",
   "language": "python",
   "name": "conda-base-py"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.12.7"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
