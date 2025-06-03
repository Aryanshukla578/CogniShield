import streamlit as st
import pandas as pd
import numpy as np
import os

st.set_page_config(page_title="CogniShield", layout="centered")

st.title("🧠 CogniShield - Cognitive Cyber Defense Platform")
st.markdown("Real-time EEG-based intent and stress detection for secure authentication.")

uploaded_file = st.file_uploader("Upload EEG CSV File", type=["csv"])
if uploaded_file is not None:
    df = pd.read_csv(uploaded_file)
    st.success("EEG data loaded successfully!")
    st.dataframe(df.head())

    st.markdown("### 🔍 Signal Preview")
    st.line_chart(df.iloc[:, 1:4])

    st.markdown("### 🧠 Prediction (Mock)")
    st.write("**Intent Verified:** ✅")
    st.write("**Stress Level:** 🟢 Normal")
else:
    st.info("Please upload an EEG CSV file to begin analysis.")
