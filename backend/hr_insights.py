import pandas as pd
from pathlib import Path

def get_hr_insights():
    df = pd.read_csv(
    Path(__file__).resolve().parent.parent
    / "data"
    / "WA_Fn-UseC_-HR-Employee-Attrition.csv"
)

    total_employees = len(df)

    employees_left = (df["Attrition"] == "Yes").sum()

    attrition_rate = (employees_left / total_employees) * 100

    department_attrition = (
        df[df["Attrition"] == "Yes"]
        .groupby("Department")
        .size()
        .to_dict()
    )

    return {
        "total_employees": total_employees,
        "employees_left": int(employees_left),
        "attrition_rate": round(attrition_rate, 2),
        "department_attrition": department_attrition
    }