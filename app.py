import streamlit as st
import pandas as pd
import joblib
import os
from datetime import datetime

# -------------------------------
# Page Configuration
# -------------------------------
st.set_page_config(
    page_title="Speech-Based Gender Recognition Agent",
    page_icon="🎤",
    layout="centered"
)

# -------------------------------
# Load Saved Files
# -------------------------------
model = joblib.load("gender_model.pkl")
scaler = joblib.load("scaler.pkl")
encoder = joblib.load("label_encoder.pkl")

# -------------------------------
# Title
# -------------------------------
st.title("🎤 Speech-Based Gender Recognition Agent")

st.markdown("""
This AI Agent predicts the **gender of a speaker**
using acoustic speech features and a trained
**Multi-Layer Perceptron (MLP)** model.
""")

st.header("Enter Acoustic Feature Values")

# -------------------------------
# Input Fields
# -------------------------------

meanfreq = st.number_input("Mean Frequency", value=0.0, format="%.6f")
sd = st.number_input("Standard Deviation", value=0.0, format="%.6f")
median = st.number_input("Median", value=0.0, format="%.6f")
Q25 = st.number_input("Q25", value=0.0, format="%.6f")
Q75 = st.number_input("Q75", value=0.0, format="%.6f")
IQR = st.number_input("IQR", value=0.0, format="%.6f")
skew = st.number_input("Skew", value=0.0, format="%.6f")
kurt = st.number_input("Kurtosis", value=0.0, format="%.6f")
sp_ent = st.number_input("Spectral Entropy", value=0.0, format="%.6f")
sfm = st.number_input("Spectral Flatness", value=0.0, format="%.6f")
mode = st.number_input("Mode", value=0.0, format="%.6f")
centroid = st.number_input("Centroid", value=0.0, format="%.6f")
meanfun = st.number_input("Mean Fundamental Frequency", value=0.0, format="%.6f")
minfun = st.number_input("Minimum Fundamental Frequency", value=0.0, format="%.6f")
maxfun = st.number_input("Maximum Fundamental Frequency", value=0.0, format="%.6f")
meandom = st.number_input("Mean Dominant Frequency", value=0.0, format="%.6f")
mindom = st.number_input("Minimum Dominant Frequency", value=0.0, format="%.6f")
maxdom = st.number_input("Maximum Dominant Frequency", value=0.0, format="%.6f")
dfrange = st.number_input("Dominant Frequency Range", value=0.0, format="%.6f")
modindx = st.number_input("Modulation Index", value=0.0, format="%.6f")
