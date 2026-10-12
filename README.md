HR Analytics Pro

Project Overview

HR Analytics Pro is a machine learning project that predicts employee attrition using HR employee data.

Technologies Used

- Python
- Pandas
- Scikit-learn
- FastAPI
- Streamlit
- Joblib

Project Structure

- "backend/" — model training and prediction API
- "data/" — HR employee dataset
- "streamlit_app.py" — Streamlit user interface
- "requirements.txt" — Python dependencies

Features

- Employee attrition prediction
- Machine learning model using Random Forest
- FastAPI prediction endpoint
- Streamlit frontend

How to Run

1. Install dependencies

pip install -r requirements.txt

2. Start the backend

cd backend
python -m uvicorn app:app --reload

3. Start the frontend

Open a second terminal in the main project folder and run:

python -m streamlit run streamlit_app.py

API Documentation

When the backend is running, visit:
"http://127.0.0.1:8000/docs"

Frontend

"http://localhost:8501"

Purpose

This project demonstrates machine learning, model deployment, and a user interface for employee attrition prediction.