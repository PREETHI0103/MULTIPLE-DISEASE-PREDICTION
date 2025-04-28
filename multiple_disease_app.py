import streamlit as st
import joblib
import pandas as pd
import plotly.graph_objects as go
import os

st.set_page_config(page_title="Multi-Disease Prediction App",page_icon="🧬",layout="centered",initial_sidebar_state="expanded")

st.markdown("""<style>/* Main background with light overlay */.stApp {background: linear-gradient(rgba(255, 255, 255, 0.60), rgba(255, 255, 255, 0.60)), 
url("https://www.sparshhospital.com/wp-content/uploads/2024/12/infec.jpg");
background-size: cover;background-position: center;background-attachment: fixed;}

/* Content container */
.main .block-container {background-color: rgba(255, 255, 255, 0.85);border-radius: 15px;padding: 2.5rem;box-shadow: 0 4px 20px rgba(0, 0, 0, 0.08);
border: 1px solid rgba(0, 0, 0, 0.05);}

/* Sidebar */
.sidebar .sidebar-content {background-color: rgba(255, 255, 255, 0.9);border-radius: 15px;box-shadow: 0 4px 20px rgba(0, 0, 0, 0.08);backdrop-filter: blur(4px);}

/* ===== IMPROVED FEATURE LABELS/VALUES ===== */
.feature-label {color: #2c3e50 !important;  /* Dark blue-gray for better contrast */font-weight: 600 !important;font-size: 16px !important;margin-bottom: 0.2rem !important;}

.feature-value input {background-color: rgba(245, 245, 245, 0.9) !important;border: 1px solid #dfe6e9 !important;border-radius: 8px !important;padding: 8px 12px !important;}

.stNumberInput, .stSelectbox {background-color: rgba(245, 245, 245, 0.9) !important;border-radius: 8px !important;}

/* ===== HEADERS ===== */
.multiple-disease-header {color: #FF6347;font-size: 36px;font-weight: 700;text-align: center;margin-bottom: 1.5rem;text-shadow: none;}

.disease-header {color: #c0392b;font-size: 28px;font-weight: 600;text-align: center;margin-bottom: 1.2rem;}

.patient-details {color: #7f8c8d;font-size: 18px;font-weight: 500;text-align: center;margin-bottom: 2rem;font-style: italic;}

/* ===== BUTTONS ===== */
.stButton>button {background-color: #e74c3c !important;color: white !important;font-weight: 600 !important;border-radius: 8px !important;padding: 10px 24px !important;
border: none !important;}
        
.stButton>button:hover {background-color: #c0392b !important;transform: scale(1.02);}

/* ===== INPUT FOCUS EFFECTS ===== */
.stTextInput input:focus, 
.stNumberInput input:focus, 
.stSelectbox select:focus {border-color: #e74c3c !important;box-shadow: 0 0 0 2px rgba(231, 76, 60, 0.2) !important;}</style>""", unsafe_allow_html=True)

st.sidebar.title("Select Disease to Predict 🧬")

disease_options = [("Kidney Disease 🩺", "kidney"),("Liver Disease 🏥", "liver"),("Parkinson's Disease 🧠", "parkinsons")]

selected_disease = st.sidebar.selectbox("Choose Disease to Predict 🧬",options=[option[0] for option in disease_options])

def load_components(model_path, scaler_path, features_path):
  model = joblib.load(model_path)
  scaler = joblib.load(scaler_path)
  features = joblib.load(features_path)
  return model, scaler, features

def show_probability_chart(probability):
  if probability <= 0.3:
      color = "#2ecc71"
  elif probability <= 0.7:
      color = "#f1c40f"
  else:
      color = "#FF6347"

  fig = go.Figure(go.Indicator(
      mode="gauge+number+delta",
      value=probability * 100,
      domain={'x': [0, 1], 'y': [0, 1]},
      title={'text': "Probability of Disease", 'font': {'size': 24}},
      gauge={
          'axis': {'range': [0, 100], 'tickwidth': 1, 'tickcolor': "black"},
          'bar': {'color': color, 'thickness': 0.4},
          'steps': [
              {'range': [0, 30], 'color': "#2ecc71"},
              {'range': [30, 70], 'color': "#f1c40f"},
              {'range': [70, 100], 'color': "#FF6347"},
          ],
          'threshold': {
              'line': {'color': "black", 'width': 4},
              'thickness': 0.75,
              'value': probability * 100
          }
      }
  ))

  st.plotly_chart(fig, use_container_width=True)

st.markdown("<h2 class='multiple-disease-header'>MULTIPLE DISEASE PREDICTION 🔬</h2>", unsafe_allow_html=True)

# KIDNEY
if "Kidney" in selected_disease:
  st.markdown("<h3 class='disease-header'>Kidney Disease Prediction 🩺</h3>", unsafe_allow_html=True)
  st.markdown("<h4 class='patient-details'>*Fill the Patient's Details to Get the Prediction*</h4>", unsafe_allow_html=True)

  model, scaler, features = load_components("/content/drive/MyDrive/xgboost_model_kidney.pkl","/content/drive/MyDrive/scaler_kidney.pkl",
      "/content/drive/MyDrive/top10_features_kidney.pkl")

  labels = {'pcv': ('Packed Cell Volume (pcv)', '🩸'),
      'hemo': ('Hemoglobin (hemo)', '🩸'),
      'sg': ('Specific Gravity (sg)', '🌊'),
      'sc': ('Serum Creatinine (sc)', '🧬'),
      'rc': ('Red Blood Cell Count (rc)', '🩸'),
      'al': ('Albumin Level (al)', '🥛'),
      'htn': ('Hypertension (htn)', '💔'),
      'sod': ('Sodium (sod)', '🧂'),
      'bu': ('Blood Urea (bu)', '💉'),
      'dm': ('Diabetes Mellitus (dm)', '🍬')}

  user_input = {}
  for f in features:
    label, emoji = labels.get(f, (f, '🔬'))
    if f in ['htn', 'dm']:
        user_input[f] = 1 if st.selectbox(f"{emoji} {label}:", ['Yes', 'No']) == 'Yes' else 0
    else:
        user_input[f] = st.number_input(f"{emoji} {label}:", step=0.01, format="%.2f")

  if st.button("🔍 Predict Kidney Disease 🩺"):
    df = pd.DataFrame([user_input])
    scaled = scaler.transform(df[features])
    pred = model.predict(scaled)[0]
    prob = model.predict_proba(scaled)[0][1]

    show_probability_chart(prob)

    if pred == 1:
        st.error("⚠️ The person **has kidney disease**.")
    else:
        st.success("✅ The person **does not have kidney disease**.")

# LIVER
elif "Liver" in selected_disease:
  st.markdown("<h3 class='disease-header'>Liver Disease Prediction 🏥</h3>", unsafe_allow_html=True)
  st.markdown("<h4 class='patient-details'>*Fill the Patient's Details to Get the Prediction*</h4>", unsafe_allow_html=True)

  model, scaler, features = load_components("/content/drive/MyDrive/best_random_forest_model_liver.pkl","/content/drive/MyDrive/scaler_liver.pkl",
      "/content/drive/MyDrive/top7_features_liver.pkl")

  labels = {'Total_Bilirubin': ('Total Bilirubin', '🧪'),
      'Direct_Bilirubin': ('Direct Bilirubin', '🔬'),
      'Alkaline_Phosphotase': ('Alkaline Phosphotase', '💉'),
      'Alamine_Aminotransferase': ('Alamine Aminotransferase', '🧬'),
      'Aspartate_Aminotransferase': ('Aspartate Aminotransferase', '🔬'),
      'Albumin_and_Globulin_Ratio': ('Albumin/Globulin Ratio', '💊'),
      'Age': ('Age', '👶')}

  user_input = {}
  for f in features:
    label, emoji = labels.get(f, (f, '🧬'))
    user_input[f] = st.number_input(f"{emoji} {label}:", step=0.01, format="%.2f")

  if st.button("🔍 Predict Liver Disease 🏥"):
    df = pd.DataFrame([user_input])
    scaled = scaler.transform(df[features])
    pred = model.predict(scaled)[0]
    prob = model.predict_proba(scaled)[0][1]

    show_probability_chart(prob)

    if pred == 1:
        st.error("⚠️ The person **has liver disease**.")
    else:
        st.success("✅ The person **does not have liver disease**.")

# PARKINSON'S
elif "Parkinson" in selected_disease:
  st.markdown("<h3 class='disease-header'>Parkinson's Disease Prediction 🧠</h3>", unsafe_allow_html=True)
  st.markdown("<h4 class='patient-details'>*Fill the Patient's Details to Get the Prediction*</h4>", unsafe_allow_html=True)

  model, scaler, features = load_components("/content/drive/MyDrive/random_forest_model_parkinsons.pkl","/content/drive/MyDrive/minmax_scaler_parkinsons.pkl",
      "/content/drive/MyDrive/top10_features(parkinsons).pkl")

  labels = {'ppe': ('PPE', '🧠'),
      'spread1': ('Spread1', '🔊'),
      'shimmer:apq5': ('Shimmer (APQ5)', '🎶'),
      'mdvp:fo(hz)': ('MDVP Fo (Hz)', '🎧'),
      'spread2': ('Spread2', '📡'),
      'mdvp:shimmer': ('MDVP Shimmer', '🎙'),
      'mdvp:fhi(hz)': ('MDVP Fhi (Hz)', '🎵'),
      'shimmer:dda': ('Shimmer DDA', '🎤'),
      'mdvp:apq': ('MDVP APQ', '🎼'),
      'mdvp:flo(hz)': ('MDVP Flo (Hz)', '🎵')}

  user_input = {}
  for f in features:
    label, emoji = labels.get(f, (f, '🔋'))
    user_input[f] = st.number_input(f"{emoji} {label}:", step=0.01, format="%.2f")

  if st.button("🔍 Predict Parkinson's Disease 🧠"):
    df = pd.DataFrame([user_input])
    scaled = scaler.transform(df[features])
    pred = model.predict(scaled)[0]
    prob = model.predict_proba(scaled)[0][1]

    show_probability_chart(prob)

    if pred == 1:
        st.error("⚠️ The person **has Parkinson's disease**.")
    else:
        st.success("✅ The person **does not have Parkinson's disease**.")
