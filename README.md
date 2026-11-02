HR Analytics Pro

Project Overview

HR Analytics Pro is a Full Stack Data Science project that analyzes employee data and predicts employee attrition using Machine Learning. It also includes an AI-powered HR Assistant using Groq and LangChain.

Technologies Used

- Python
- Pandas, NumPy
- Scikit-learn
- Random Forest Classifier
- FastAPI
- Streamlit
- LangChain
- Groq API
- Joblib

Features

- Employee Attrition Prediction
- Random Forest Machine Learning Model
- HR Analytics Dashboard
- Employee Attrition Insights
- FastAPI Prediction Backend
- Streamlit Frontend
- AI-powered HR Chatbot using Groq and LangChain

Project Structure

- "backend/" – Model training, prediction API and chatbot
- "data/" – HR employee dataset
- "streamlit_app.py" – Streamlit user interface
- "requirements.txt" – Project dependencies

How to Run

1. Install Dependencies

pip install -r requirements.txt

2. Start Backend

Open a terminal and run:

cd backend
.venv\Scripts\python.exe -m uvicorn app:app --reload

3. Start Frontend

Open another terminal in the main project folder:

python -m streamlit run streamlit_app.py

4. Access the Application

- Frontend: http://localhost:8501
- API Documentation: http://127.0.0.1:8000/docs

AI Chatbot Setup

Create a ".env" file inside the "backend/" folder and add your Groq API key:

GROQ_API_KEY=your_groq_api_key

Never upload your API key to GitHub.

Purpose

This project demonstrates practical skills in Machine Learning, Data Analytics, API Development, Full Stack Data Science and Generative AI.
