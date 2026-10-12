import pandas as pd
import joblib

from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score, classification_report


# Load dataset
df = pd.read_csv("../data/WA_Fn-UseC_-HR-Employee-Attrition.csv")

# Remove unnecessary columns
df = df.drop([
    "EmployeeNumber",
    "EmployeeCount",
    "Over18",
    "StandardHours"
], axis=1)

# Create separate encoders for each categorical column
encoders = {}

for column in df.select_dtypes(include="object").columns:
    encoder = LabelEncoder()
    df[column] = encoder.fit_transform(df[column].astype(str))
    encoders[column] = encoder


# Separate input and output
X = df.drop("Attrition", axis=1)
y = df["Attrition"]

# Split dataset
X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.2,
    random_state=42,
    stratify=y
)

# Create Random Forest model
model = RandomForestClassifier(
    n_estimators=100,
    random_state=42
)

# Train model
model.fit(X_train, y_train)
joblib.dump(model, "hr_attrition_model.joblib")
joblib.dump(encoders, "hr_attrition_encoders.joblib")
joblib.dump(list(X.columns), "hr_attrition_columns.joblib")

# Prediction
y_pred = model.predict(X_test)

# Accuracy
accuracy = accuracy_score(y_test, y_pred)

print("HR ANALYTICS PRO")
print("----------------")
print("Model Accuracy:", accuracy)

# Classification report
print("\nClassification Report:")
print(classification_report(y_test, y_pred))