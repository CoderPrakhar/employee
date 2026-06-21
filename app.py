import streamlit as st
import pandas as pd
import joblib

# Load Model
model = joblib.load("employee_attrition_model.pkl")

st.title("Employee Attrition Prediction")

# Inputs
satisfactoryLevel = st.slider("Satisfactory Level", 0.0, 1.0, 0.5)

lastEvaluation = st.slider("Last Evaluation", 0.0, 1.0, 0.5)

numberOfProjects = st.number_input(
    "Number Of Projects",
    min_value=1,
    max_value=20,
    value=3
)

avgMonthlyHours = st.number_input(
    "Average Monthly Hours",
    min_value=50,
    max_value=400,
    value=160
)

timeSpent = st.number_input(
    "Time Spent In Company",
    min_value=1,
    max_value=20,
    value=3
)

workAccident = st.selectbox(
    "Work Accident",
    [0, 1]
)

promotionInLast5years = st.selectbox(
    "Promotion In Last 5 Years",
    [0, 1]
)

dept = st.selectbox(
    "Department Code",
    [0,1,2,3,4,5,6,7,8,9]
)

salary = st.selectbox(
    "Salary Code",
    [0,1,2]
)

workload = st.number_input(
    "Workload",
    min_value=0,
    value=314
)

# Prediction
if st.button("Predict"):

    input_data = pd.DataFrame({
        "satisfactoryLevel":[satisfactoryLevel],
        "lastEvaluation":[lastEvaluation],
        "numberOfProjects":[numberOfProjects],
        "avgMonthlyHours":[avgMonthlyHours],
        "timeSpent.company":[timeSpent],
        "workAccident":[workAccident],
        "promotionInLast5years":[promotionInLast5years],
        "dept":[dept],
        "salary":[salary],
        "workload":[workload]
    })

    st.subheader("Debug Information")
    st.write(input_data)

    try:
        prediction = model.predict(input_data)

        if prediction[0] == 1:
            st.error("❌ Employee Likely To Leave")
        else:
            st.success("✅ Employee Likely To Stay")

    except Exception as e:
        st.error(f"Error: {e}")