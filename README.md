# 🧬 Multi-Disease Prediction Using Machine Learning

An intelligent ML-powered system to predict **Parkinson’s, Kidney, and Liver diseases** from clinical data. Built to assist early diagnosis and support healthcare professionals with **fast, accurate, and explainable results** via a clean Streamlit interface.

<p align="center">
  <img src="https://img.shields.io/badge/Machine%20Learning-✓-brightgreen" />
  <img src="https://img.shields.io/badge/Streamlit-✓-red" />
  <img src="https://img.shields.io/badge/Colab%20Demo-Available-blue" />
</p>

---

## 📌 Features

### 🩺 Disease Selection
Choose from:
- Parkinson’s Disease
- Kidney Disease
- Liver Disease

### 🧠 Smart Prediction System
- Input patient parameters
- Get real-time predictions from ML models

### 📊 Model Metrics Dashboard
- Accuracy, F1 Score, Precision, Recall
- Confusion Matrix
- ROC-AUC Curve
- Feature Importance Visuals

### 💡 Streamlit Interface
- Intuitive and user-friendly
- Hosted via Colab + ngrok (no local setup)

---

## 📁 Dataset Summary

| Disease       | Samples | Features | Target | Notes                        |
|---------------|---------|----------|--------|------------------------------|
| Parkinson’s   | 195     | 24       | 0 / 1  | Voice biometric data         |
| Kidney        | 400     | 26       | 0 / 1  | Missing values handled       |
| Liver         | 583     | 11       | 1 / 2  | Addressed class imbalance    |

---

## 🧹 Data Preprocessing

- 🔍 Imputation for Missing Values
- 🔁 Categorical Encoding (Label/OneHot)
- 🧮 Feature Scaling (StandardScaler / MinMaxScaler)
- ⚖️ Balancing Techniques (SMOTE, RandomOverSampler, UnderSampler)
- 📈 Outlier Treatment (IQR Capping)

---

## ⚙️ Models Used

Each disease is modeled using the following classifiers:

- ✅ Logistic Regression  
- ✅ Random Forest  
- ✅ XGBoost  
- ✅ Decision Tree  
- ✅ K-Nearest Neighbors (KNN)  
- ✅ Support Vector Machine (SVM)  
- ✅ Naive Bayes

> For each disease:
> - All models were trained and evaluated using **raw**, **oversampled**, and **undersampled** data.
> - **Stratified K-Fold Cross Validation** was applied to compare performance across multiple folds.
> - Based on overall **cross-validated accuracy, F1-score, and generalization**, the **best performing model** was selected.
> - The selected model was **saved using `joblib`** and **deployed within the Streamlit app** for real-time predictions.

---

## 🖥️ Tech Stack

| Tool             | Purpose                           |
|------------------|-----------------------------------|
| Python           | Core language                     |
| pandas, numpy    | Data manipulation                 |
| scikit-learn     | ML algorithms and evaluation      |
| imbalanced-learn | Data balancing (SMOTE, ROS, RUS)  |
| matplotlib, seaborn | Data visualization             |
| Streamlit        | Web app interface                 |
| ngrok            | Public tunneling for Colab app    |
| joblib           | Model serialization and loading  |

---

## 🎯 Key Highlights

- 🔍 Multi-disease prediction from a single interface
- ⚖️ Tried multiple **ML models** per disease
- 🔁 Used **Stratified K-Fold Cross Validation** to ensure robust performance
- 🏆 Selected the **best model per disease** based on CV metrics
- 💾 Saved best models using **joblib** for efficient deployment
- 📊 Robust model evaluation and visualizations
- 🚀 Live deployed app via Streamlit in Colab
- 💬 Future-ready architecture for expanding more diseases

---

## 🔮 Future Improvements

- Add **more diseases** (e.g., diabetes, heart disease)
- **User authentication** & history tracking
- Add **API integration** for EHR systems
- Visualize **model explanations (SHAP, LIME)**
- Export reports to PDF

---

## 🧑‍💻 Author

Built with ❤️ by **[PREETHI S]**

---

## 🏷️ Tags

#machinelearning #healthcare-ai #streamlit #colab #ngrok #kidney-disease #parkinsons-disease #liver-disease #scikit-learn #data-science #crossvalidation #modelselection #joblib


