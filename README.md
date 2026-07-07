# 🎓 Student Job Prediction using Machine Learning

## 📌 Project Overview

This project predicts a student's **career aspiration** based on academic performance and personal attributes using Machine Learning. It includes Exploratory Data Analysis (EDA), data preprocessing, model training, evaluation, and a Streamlit web application for real-time predictions.

---

## 🚀 Features

- 📊 Exploratory Data Analysis (EDA)
- 🧹 Data Cleaning & Preprocessing
- 🔠 Label Encoding
- 📏 StandardScaler
- 🌲 Random Forest Classifier
- 📈 Model Evaluation
- 🌐 Streamlit Web Application
- 🎯 Predict Student Career Aspiration

---

## 📂 Dataset Features

The dataset contains the following features:

- Gender
- Part Time Job
- Absence Days
- Extracurricular Activities
- Weekly Self Study Hours
- Math Score
- History Score
- Physics Score
- Chemistry Score
- Biology Score
- English Score
- Geography Score
- Total Score
- Average Score

### 🎯 Target Variable

- Career Aspiration

---

## 📊 Exploratory Data Analysis

The following analyses were performed:

- Missing Value Analysis
- Duplicate Value Check
- Gender Distribution
- Career Aspiration Distribution
- Subject Score Distribution
- Histograms
- Boxplots
- Correlation Heatmap
- Feature Relationship Analysis

---

## ⚙️ Machine Learning Workflow

1. Load Dataset
2. Data Cleaning
3. Feature Engineering
4. Label Encoding
5. Feature Scaling
6. Train-Test Split
7. Train Random Forest Classifier
8. Evaluate Model
9. Save Model using Pickle
10. Build Streamlit Application

---

## 🤖 Machine Learning Model

- Random Forest Classifier

---

## 📈 Model Performance

- **Accuracy:** 68%

Evaluation Metrics:

- Accuracy Score
- Confusion Matrix
- Classification Report

---

## 🛠 Technologies Used

- Python
- Pandas
- NumPy
- Matplotlib
- Seaborn
- Scikit-learn
- Streamlit
- Pickle

---

## 📁 Project Structure

```
Student-Job-Prediction/
│
├── app.py
├── student.ipynb
├── student-scores.csv
├── RandomForestClassifier.pkl
├── scaler.pkl
├── labelencoders.pkl
├── requirements.txt
├── README.md

```

---

## ▶️ Installation

Clone the repository

```bash
git clone https://github.com/your-username/Student-Job-Prediction.git
```

Move into the project folder

```bash
cd Student-Job-Prediction
```

Install dependencies

```bash
pip install -r requirements.txt
```

Run the Streamlit application

```bash
streamlit run app.py
```

---

## 💻 Streamlit Application

The application allows users to:

- Enter student information
- Predict career aspiration
- View prediction confidence

---







## ⭐ If you like this project

Please ⭐ star this repository and share it with others.
