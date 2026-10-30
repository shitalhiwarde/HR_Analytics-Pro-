import os
from dotenv import load_dotenv
from langchain_groq import ChatGroq
from langchain_core.prompts import ChatPromptTemplate
from backend.hr_insights import get_hr_insights

load_dotenv()

llm = ChatGroq(
    model="openai/gpt-oss-20b",
    temperature=0.3,
    api_key=os.getenv("GROQ_API_KEY")
)

prompt = ChatPromptTemplate.from_messages([
    ("system", "You are an HR Analytics AI assistant. Answer HR and employee attrition questions in simple English."),
    ("human", "{question}")
])

chain = prompt | llm

def ask_hr_ai(question):
    hr_data = get_hr_insights()

    context = f"""
    HR Dataset Information:
    Total Employees: {hr_data['total_employees']}
    Employees Left: {hr_data['employees_left']}
    Attrition Rate: {hr_data['attrition_rate']}%
    Department Attrition: {hr_data['department_attrition']}
    """

    response = chain.invoke({
        "question": f"""
        Use this HR dataset information to answer.
        {context}

        Question: {question}
        """
    })

    return response.content