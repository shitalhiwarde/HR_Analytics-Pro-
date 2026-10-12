from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
import pandas as pd
import joblib

app = FastAPI(title="HR Analytics Pro")

# Load trained model and encoders
model = joblib.load("hr_attrition_model.joblib")
encoders = joblib.load("hr_attrition_encoders.joblib")
columns = joblib.load("hr_attrition_columns.joblib")


class EmployeeData(BaseModel):
    employee_data: dict


@app.get("/")
def home():
    return {"message": "HR Analytics Pro API is running!"}


@app.post("/predict")
def predict(data: EmployeeData):
    try:
        employee = pd.DataFrame([data.employee_data])

        # Check that all required features are provided
        missing_columns = [
            column for column in columns
            if column not in employee.columns
        ]

        if missing_columns:
            raise HTTPException(
                status_code=400,
                detail={"missing_columns": missing_columns}
            )

        # Keep features in the correct order
        employee = employee[columns]

        # Convert categorical values using saved encoders
        for column, encoder in encoders.items():
            if column in employee.columns:
                try:
                    employee[column] = encoder.transform(
                        employee[column].astype(str)
                    )
                except ValueError:
                    raise HTTPException(
                        status_code=400,
                        detail=f"Invalid category for {column}. "
                               f"Allowed values: {list(encoder.classes_)}"
                    )

        # Predict employee attrition
        prediction = int(model.predict(employee)[0])

        return {
            "Attrition_Prediction": "Yes" if prediction == 1 else "No"
        }

    except HTTPException:
        raise
    except Exception as error:
        raise HTTPException(status_code=500, detail=str(error))