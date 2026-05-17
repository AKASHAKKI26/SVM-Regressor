# SVM-Regressor

# Insurance Charges Prediction using SVR

This project is a Machine Learning web application built using Streamlit and Support Vector Regression (SVR).

The application predicts medical insurance charges based on user details such as age, BMI, smoking habits, region, and more.

---

## Features Used

- Age
- BMI
- Number of Children
- Sex
- Smoker Status
- Region

---

## Machine Learning Algorithm

- Support Vector Regression (SVR)

---

## Technologies Used

- Python
- Streamlit
- Scikit-learn
- Pandas
- NumPy
- Pickle

---

## Project Structure

```text
InsurancePrediction/
│
├── app.py
├── svmreg.pkl
├── scaler_X.pkl
├── scaler_y.pkl
├── insurance.csv
├── requirements.txt
└── README.md
```

---

## Installation

Install the required libraries using:

```bash
pip install -r requirements.txt
```

---

## Run the Application

```bash
streamlit run app.py
```

---

## Input Parameters

| Feature | Description |
|---|---|
| Age | Person's age |
| BMI | Body Mass Index |
| Children | Number of children |
| Sex | Male or Female |
| Smoker | Smoking status |
| Region | Residential region |

---

## Output

The application predicts:

```text
Estimated Insurance Charges
```

Example:

```text
Estimated Insurance Charges: $15234.50
```

---

## Model Performance

The model is trained using SVR with feature scaling for better prediction accuracy.

---

## Author

Machine Learning Mini Project
