import streamlit as st
import pandas as pd
import pickle

# -------------------------------
# Load Model and Preprocessing Files
# -------------------------------
model = pickle.load(open("RandomForestClassifier.pkl", "rb"))
scaler = pickle.load(open("scaler.pkl", "rb"))
encoders = pickle.load(open("labelencoders.pkl", "rb"))

st.set_page_config(
    page_title="Student Job Prediction",
    page_icon="🎓",
    layout="centered"
)

st.title("🎓 Student Job Prediction")
st.markdown("Predict a student's career aspiration using Machine Learning.")

st.divider()

# -------------------------------
# User Inputs
# -------------------------------

gender = st.selectbox("Gender", ["Male", "Female"])

part_time_job = st.selectbox(
    "Part Time Job",
    ["Yes", "No"]
)

absence_days = st.number_input(
    "Absence Days",
    min_value=0,
    max_value=100,
    value=5
)

extracurricular = st.selectbox(
    "Extracurricular Activities",
    ["Yes", "No"]
)

weekly_self_study_hours = st.slider(
    "Weekly Self Study Hours",
    0,
    30,
    10
)

math_score = st.slider("Math Score",0,100,60)
history_score = st.slider("History Score",0,100,60)
physics_score = st.slider("Physics Score",0,100,60)
chemistry_score = st.slider("Chemistry Score",0,100,60)
biology_score = st.slider("Biology Score",0,100,60)
english_score = st.slider("English Score",0,100,60)
geography_score = st.slider("Geography Score",0,100,60)

# -------------------------------
# Prediction
# -------------------------------

if st.button("Predict Career"):

    input_df = pd.DataFrame({
        "gender":[gender],
        "part_time_job":[part_time_job],
        "absence_days":[absence_days],
        "extracurricular_activities":[extracurricular],
        "weekly_self_study_hours":[weekly_self_study_hours],
        "math_score":[math_score],
        "history_score":[history_score],
        "physics_score":[physics_score],
        "chemistry_score":[chemistry_score],
        "biology_score":[biology_score],
        "english_score":[english_score],
        "geography_score":[geography_score]
    })

    # Encode categorical columns
    categorical = [
        "gender",
        "part_time_job",
        "extracurricular_activities"
    ]


    
    # Manual mapping (same as training)
    input_df["gender"] = input_df["gender"].map({
       "Male": 1,
       "Female": 0
    })
    
    input_df["part_time_job"] = input_df["part_time_job"].map({
       "Yes": 1,
       "No": 0
    })


    input_df["extracurricular_activities"] = input_df["extracurricular_activities"].map({
       "Yes": 1,
       "No": 0
    })

    input_df["total_score"] = (
    input_df["math_score"] +
    input_df["history_score"] +
    input_df["physics_score"] +
    input_df["chemistry_score"] +
    input_df["biology_score"] +
    input_df["english_score"] +
    input_df["geography_score"]
   )

    input_df["average_score"] = input_df["total_score"] / 7

    # Scale
    input_scaled = scaler.transform(input_df)

    # Prediction
    prediction = model.predict(input_scaled)[0]

    # Decode prediction
    prediction = model.predict(input_scaled)[0]

    career = encoders["career_aspiration"].inverse_transform([prediction])[0]

    st.success(f"🎯 Predicted Career: {career}")

    # Probability
    # if hasattr(model, "predict_proba"):
    #     probability = model.predict_proba(input_scaled).max() * 100
    #     st.info(f"Confidence : {probability:.2f}%")

    probabilities = model.predict_proba(input_scaled)[0]

    st.subheader("Prediction Probabilities")

    career_names = encoders["career_aspiration"].classes_

    prob_df = pd.DataFrame({
       "Career": career_names,
        "Probability (%)": probabilities * 100
    })

    prob_df = prob_df.sort_values("Probability (%)", ascending=False)

    st.dataframe(prob_df)

    st.bar_chart(prob_df.set_index("Career"))