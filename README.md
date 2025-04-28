# MULTIPLE-DISEASE-PREDICTION USING MACHINE LEARNING
Project Overview
Timely diagnosis and early detection of diseases are crucial for improving treatment outcomes, reducing healthcare costs, and preventing complications. This project focuses on using machine learning (ML) to predict diseases such as Parkinson's Disease, Kidney Disease, and Liver Disease based on clinical data. The goal is to assist healthcare professionals in making data-driven decisions and improve overall patient care.

Objective
This project aims to develop an accurate and efficient machine learning model to predict diseases using clinical datasets. The system will:

Assist in early disease detection.

Support healthcare professionals in making informed decisions.

Reduce diagnostic time and costs by providing quick, data-driven predictions via an interactive interface.

Datasets
Parkinson’s Disease Dataset

Shape: 195 rows × 24 columns

Predicts Parkinson’s Disease (1: Parkinson’s, 0: No Parkinson’s).

Challenges: Imbalanced dataset, outlier handling, feature importance selection.

Kidney Disease Dataset

Shape: 400 rows × 26 columns

Predicts Chronic Kidney Disease (1: CKD, 0: Not CKD).

Challenges: Missing values, categorical encoding, class imbalance.

Liver Disease Dataset

Shape: 583 rows × 11 columns

Predicts liver disease (1: Disease, 2: No Disease).

Challenges: Missing values, duplicates, outliers, class imbalance.

Approach
Data Preprocessing
Data Cleaning: Missing values were handled using model-based imputation techniques (Random Forest Regressor and Classifier). Categorical columns containing “?” were replaced with NaN, followed by encoding.

Outlier Handling: Outliers in continuous numerical columns were detected using the IQR method and capped.

Feature Engineering: Irrelevant columns were removed, top features were selected based on importance, and feature scaling (normalization) was applied for consistency.

Data Balancing: A variety of data balancing techniques were used and compared, including undersampling (reducing the majority class) and oversampling (increasing the minority class). The most effective strategy was selected based on trial-and-error with different models.

Model Building & Evaluation
Model Testing: Multiple machine learning models were used to predict the diseases, and their performance was evaluated using various data handling strategies: original data, undersampled data, and oversampled data.

Model Comparison: Models were compared based on key evaluation metrics such as Accuracy, F1 Score, Precision, Recall, ROC-AUC, and Confusion Matrix. The best-performing model was selected based on these comparisons.

After extensive experimentation with different models and data handling techniques, the optimal model was chosen for deployment.

Streamlit Deployment Using ngrok
The final model was deployed via Streamlit in Google Colab. Since Colab does not support direct hosting of Streamlit apps, ngrok was used to create a secure tunnel and display the app in real-time.

Users can select the disease they want to predict (Parkinson’s, Kidney, or Liver Disease) and input patient details (e.g., age, gender, and clinical features).

Predictions are made instantly and displayed in a user-friendly format with interactive charts and graphs.

Technologies Used
Python: The primary language used for data analysis and machine learning.

pandas: For data manipulation and cleaning.

scikit-learn: For model training, evaluation, and feature scaling.

Streamlit: For building the interactive web interface.

ngrok: For tunneling and displaying the Streamlit app hosted in Google Colab.

matplotlib/seaborn: For visualizations and data insights.

Steps Followed
Data Collection & Exploration: Collected and cleaned datasets.

Data Preprocessing: Addressed missing values, outliers, and class imbalance with multiple techniques (undersampling, oversampling).

Model Training: Trained various models and evaluated them using different data strategies.

Model Comparison & Selection: Compared models based on key metrics and selected the best-performing one.

Deployment with ngrok: Deployed the final model in Google Colab using ngrok to create a tunnel for Streamlit to run the app in real-time.

Project Features
Disease Selection: Users can choose the disease to predict (Parkinson’s, Kidney, or Liver Disease).

Patient Input: Users can enter clinical data such as age, gender, and other features to get disease predictions.

Real-time Prediction: Predictions are made instantly, and results are displayed visually through interactive charts.

Model Performance: Display of key metrics like confusion matrix, ROC curve, and feature importance to evaluate model transparency.

Future Improvements
Add more diseases to the prediction models for broader application.

Implement user authentication for personalized predictions and secure management of patient data.

Improve the Streamlit interface with interactive visualizations and model explanation tools.

Integrate APIs for real-time data input to enable a more dynamic healthcare solution.

Conclusion
This project demonstrates the use of machine learning for disease prediction in healthcare. By experimenting with various models and data handling techniques (undersampling and oversampling), the best-performing model was selected. The system is deployed using Google Colab and ngrok, providing a real-time, user-friendly interface for healthcare professionals to assist in early disease detection and timely decision-making.
