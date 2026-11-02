import streamlit as st
import requests
from backend.hr_chatbot import ask_hr_ai

st.set_page_config(
    page_title="HR Analytics Pro",
    page_icon="👥",
    layout="wide"
)

st.title("👥 HR Analytics Pro")

st.subheader("📊 Model Performance")

try:
    metrics_response = requests.get(
        "https://hr-analytics-pro-pro-backend.onrender.com/metrics",
        timeout=10
    )

    if metrics_response.status_code == 200:
        metrics = metrics_response.json()

        col1, col2, col3, col4 = st.columns(4)

        col1.metric("Accuracy", f"{metrics['accuracy']:.2%}")
        col2.metric("Precision", f"{metrics['precision']:.2%}")
        col3.metric("Recall", f"{metrics['recall']:.2%}")
        col4.metric("F1-Score", f"{metrics['f1_score']:.2%}")

    else:
        st.warning("Metrics not available. Please train the model.")

except requests.exceptions.RequestException:
    st.warning("Backend is not connected.")

st.subheader("Employee Attrition Prediction")
st.write("Enter employee details to predict attrition.")

with st.form("employee_form"):

    st.header("Employee Information")

    col1, col2, col3 = st.columns(3)

    with col1:
        Age = st.number_input("Age", 18, 60, 35)
        BusinessTravel = st.selectbox(
            "Business Travel",
            ["Travel_Rarely", "Travel_Frequently", "Non-Travel"]
        )
        DailyRate = st.number_input("Daily Rate", 100, 1500, 800)
        Department = st.selectbox(
            "Department",
            ["Research & Development", "Sales", "Human Resources"]
        )
        DistanceFromHome = st.number_input(
            "Distance From Home", 1, 30, 5
        )
        Education = st.selectbox("Education", [1, 2, 3, 4, 5])
        EducationField = st.selectbox(
            "Education Field",
            [
                "Life Sciences", "Medical", "Marketing",
                "Technical Degree", "Human Resources", "Other"
            ]
        )
        EnvironmentSatisfaction = st.selectbox(
            "Environment Satisfaction", [1, 2, 3, 4]
        )
        Gender = st.selectbox("Gender", ["Male", "Female"])
        HourlyRate = st.number_input("Hourly Rate", 30, 100, 65)

    with col2:
        JobInvolvement = st.selectbox("Job Involvement", [1, 2, 3, 4])
        JobLevel = st.selectbox("Job Level", [1, 2, 3, 4, 5])
        JobRole = st.selectbox(
            "Job Role",
            [
                "Research Scientist", "Laboratory Technician",
                "Manufacturing Director", "Healthcare Representative",
                "Manager", "Sales Executive", "Sales Representative",
                "Research Director", "Human Resources"
            ]
        )
        JobSatisfaction = st.selectbox("Job Satisfaction", [1, 2, 3, 4])
        MaritalStatus = st.selectbox(
            "Marital Status", ["Single", "Married", "Divorced"]
        )
        MonthlyIncome = st.number_input("Monthly Income", 1000, 20000, 5000)
        MonthlyRate = st.number_input("Monthly Rate", 2000, 27000, 15000)
        NumCompaniesWorked = st.number_input(
            "Number of Companies Worked", 0, 10, 2
        )
        OverTime = st.selectbox("OverTime", ["No", "Yes"])
        PercentSalaryHike = st.number_input(
            "Percent Salary Hike", 11, 25, 12
        )

    with col3:
        PerformanceRating = st.selectbox("Performance Rating", [3, 4])
        RelationshipSatisfaction = st.selectbox(
            "Relationship Satisfaction", [1, 2, 3, 4]
        )
        StockOptionLevel = st.selectbox("Stock Option Level", [0, 1, 2, 3])
        TotalWorkingYears = st.number_input(
            "Total Working Years", 0, 40, 10
        )
        TrainingTimesLastYear = st.number_input(
            "Training Times Last Year", 0, 6, 3
        )
        WorkLifeBalance = st.selectbox("Work Life Balance", [1, 2, 3, 4])
        YearsAtCompany = st.number_input("Years at Company", 0, 40, 5)
        YearsInCurrentRole = st.number_input(
            "Years in Current Role", 0, 18, 3
        )
        YearsSinceLastPromotion = st.number_input(
            "Years Since Last Promotion", 0, 15, 1
        )
        YearsWithCurrManager = st.number_input(
            "Years with Current Manager", 0, 17, 3
        )

    submitted = st.form_submit_button("🔍 Predict Attrition")

if submitted:
    employee_data = {
        "Age": Age,
        "BusinessTravel": BusinessTravel,
        "DailyRate": DailyRate,
        "Department": Department,
        "DistanceFromHome": DistanceFromHome,
        "Education": Education,
        "EducationField": EducationField,
        "EnvironmentSatisfaction": EnvironmentSatisfaction,
        "Gender": Gender,
        "HourlyRate": HourlyRate,
        "JobInvolvement": JobInvolvement,
        "JobLevel": JobLevel,
        "JobRole": JobRole,
        "JobSatisfaction": JobSatisfaction,
        "MaritalStatus": MaritalStatus,
        "MonthlyIncome": MonthlyIncome,
        "MonthlyRate": MonthlyRate,
        "NumCompaniesWorked": NumCompaniesWorked,
        "OverTime": OverTime,
        "PercentSalaryHike": PercentSalaryHike,
        "PerformanceRating": PerformanceRating,
        "RelationshipSatisfaction": RelationshipSatisfaction,
        "StockOptionLevel": StockOptionLevel,
        "TotalWorkingYears": TotalWorkingYears,
        "TrainingTimesLastYear": TrainingTimesLastYear,
        "WorkLifeBalance": WorkLifeBalance,
        "YearsAtCompany": YearsAtCompany,
        "YearsInCurrentRole": YearsInCurrentRole,
        "YearsSinceLastPromotion": YearsSinceLastPromotion,
        "YearsWithCurrManager": YearsWithCurrManager
    }

    try:
        response = requests.post(
            "https://hr-analytics-pro-pro-backend.onrender.com/predict",
            json={"employee_data": employee_data},
            timeout=30
        )

        if response.status_code == 200:
            result = response.json()["Attrition_Prediction"]

            st.divider()
            st.subheader("Prediction Result")

            if result == "Yes":
                st.warning("⚠️ Prediction: Employee may leave the company.")
            else:
                st.success("✅ Prediction: Employee is predicted to stay.")

            st.caption(
                "This is a machine-learning prediction, not a guarantee."
            )
        else:
            st.error(f"API Error: {response.status_code}")
            st.write(response.text)

    except requests.RequestException as error:
        st.error("Backend connection failed. Check whether FastAPI is running.")
        st.write(str(error))




st.divider()

st.header("🤖 HR AI Assistant")

st.write("Ask any HR or Employee Attrition question.")

question = st.text_input(
    "Enter your question",
    placeholder="Why do employees leave the company?"
)

if st.button("Ask AI"):
    if question:
        with st.spinner("AI is thinking..."):
            try:
                answer = ask_hr_ai(question)
                st.success("AI Answer")
                st.write(answer)

            except Exception as e:
                st.error(f"Error: {e}")
    else:
        st.warning("Please enter a question.")