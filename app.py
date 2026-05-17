import streamlit as st
import pandas as pd
import numpy as np
import pickle

with open("svmreg.pkl", "rb") as f:
    model = pickle.load(f)

with open("scaler_X.pkl", "rb") as f:
    sc_X = pickle.load(f)

with open("scaler_y.pkl", "rb") as f:
    sc_y = pickle.load(f)

st.set_page_config(
    page_title="Insurance Charges Prediction",
    page_icon="💰",
    layout="centered"
)

st.title("💰 Insurance Charges Prediction")

age = st.slider(
    "Age",
    min_value=18,
    max_value=100,
    value=25
)

bmi = st.number_input(
    "BMI",
    min_value=10.0,
    max_value=60.0,
    value=25.0
)

children = st.slider(
    "Children",
    min_value=0,
    max_value=10,
    value=0
)

sex = st.selectbox(
    "Sex",
    ["male", "female"]
)

smoker = st.selectbox(
    "Smoker",
    ["yes", "no"]
)

region = st.selectbox(
    "Region",
    ["northwest", "northeast", "southwest", "southeast"]
)

if st.button("Predict Charges"):

    input_data = pd.DataFrame({
        'age': [age],
        'bmi': [bmi],
        'children': [children],
        'sex_male': [1 if sex == 'male' else 0],
        'smoker_yes': [1 if smoker == 'yes' else 0],
        'region_northwest': [1 if region == 'northwest' else 0],
        'region_southeast': [1 if region == 'southeast' else 0],
        'region_southwest': [1 if region == 'southwest' else 0]
    })

    input_scaled = sc_X.transform(input_data)

    prediction_scaled = model.predict(input_scaled)

    prediction = sc_y.inverse_transform(
        prediction_scaled.reshape(-1,1)
    )

    st.success(
        f"Estimated Insurance Charges: ${prediction[0][0]:.2f}"
    )