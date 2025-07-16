 ## Heart Disease Risk Prediction ##
This project is a Streamlit-based machine learning web application that predicts the risk of heart failure using patient clinical data. It is built using a trained classification model and includes a preprocessing scaler to ensure reliable predictions.

Demo
Live demo coming soon via Streamlit Community Cloud.

Features
- Interactive patient input interface built with Streamlit
- Uses a trained model (Logistic Regression, XGBoost, etc.) saved with joblib
- Performs input scaling using a saved StandardScaler
- Displays binary risk output (high/low risk)
- Easily deployable on Streamlit Cloud

Dataset Overview
Based on the Heart Failure Clinical Records dataset.
Target variable: DEATH_EVENT (not included as an input)
Model uses all input features:
- age
- anaemia
- creatinine_phosphokinase
- diabetes
- ejection_fraction
- high_blood_pressure
- platelets
- serum_creatinine
- serum_sodium
- sex
- smoking
- time

Technologies Used
- Python 3.9+
- scikit-learn or XGBoost
- Streamlit
- joblib
- NumPy, Pandas
## Installation ##
# Clone the repository
git clone https://github.com/yourusername/heart-risk-predictor
cd heart-risk-predictor

# Install dependencies
pip install -r requirements.txt

# Launch the app
streamlit run heart_app.py
