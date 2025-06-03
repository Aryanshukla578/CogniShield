# 🧠 CogniShield – AI-Powered Cognitive Cyber Defense Platform

![CogniShield](https://i.imgur.com/xGmmPfW.png)

> A **real-time cognitive cybersecurity system** that uses **EEG signals** to verify user intent, detect stress, and prevent unauthorized actions using cutting-edge AI & ML.

---

## 🚀 Live Demos

- 🌐 **Streamlit App**:  
  [https://cognishield-htfkbtbqvvowdbbbux2x99.streamlit.app](https://cognishield-htfkbtbqvvowdbbbux2x99.streamlit.app)

- 🌐 **NeuroSentry Nexus** (Integrated version):  
  [https://neuro-sentry-nexus.lovable.app](https://neuro-sentry-nexus.lovable.app)

---

## 🧠 Overview

**CogniShield** is a pioneering brain-computer interface (BCI) application that enhances security using neural intent and stress detection. Unlike traditional systems that rely on passwords or biometrics, CogniShield evaluates your **real-time cognitive state** during critical operations such as:

- 💳 Financial transactions
- 🔐 Login authentication
- 🛡️ Insider threat monitoring

---

## 🎯 Core Features

| Feature | Description |
|--------|-------------|
| 🧠 Neural Authentication | Authenticates users based on EEG signals |
| 🚨 Stress & Duress Detection | Identifies if the user is under pressure or coercion |
| 🧾 Intent Verification | Ensures the user *intended* to perform the action |
| 📊 EEG Signal Visualization | Real-time data charts for 3 EEG channels |
| 🧬 Machine Learning Ready | Modular structure for EEG-based classifiers |

---

## 📦 Folder Structure

CogniShield/
│
├── backend/ # Flask API backend (placeholder)
│ └── app.py
│
├── frontend/ # Streamlit GUI
│ └── app_streamlit.py
│
├── ml_models/ # EEG classification models (placeholder)
│ └── model.py
│
├── utils/ # Signal preprocessing scripts
│ └── signal_processing.py
│
├── eeg_data/ # EEG samples
│ └── sample.csv
│
└── README.md

---

## 🧪 Sample EEG Data

Test the app with the sample file:
[📥 Download sample_eeg_data.csv](https://chat.openai.com/sandbox:/mnt/data/sample_eeg_data.csv)

---

## 🛠️ Tech Stack

| Component     | Tech Used                         |
|---------------|-----------------------------------|
| Frontend      | Streamlit                         |
| Backend API   | Flask (optional, for full version)|
| ML Frameworks | Scikit-learn, TensorFlow, PyTorch |
| EEG I/O       | OpenBCI SDK, MuseIO (Future Scope)|
| Signal Proc.  | NumPy, Pandas, SciPy              |

---

## 🧠 Sample Workflow

1. User wears an EEG headset.
2. Upload or stream real-time EEG data.
3. CogniShield evaluates the following:
   - 🧬 Is the brainwave pattern consistent with the user?
   - 😰 Is there stress or coercion?
   - ✅ Is the action intentional?
4. Displays results and flags any anomalies.

---

## 🧩 Future Enhancements

- 🔗 Live EEG device integration (Muse/OpenBCI)
- 📉 Model training using CNN/LSTM for improved classification
- 🧠 Dataset expansion using [OpenNeuro](https://openneuro.org/) / [PhysioNet](https://physionet.org/)
- 🪪 Blockchain-based decentralized identity with neural signatures

---

## 📸 Screenshots

<img src="https://i.imgur.com/2qSxyDO.png" width="700"/>
<img src="https://i.imgur.com/HRs0B3W.png" width="700"/>

---

## 🤖 Lovable Deployment Prompt (for https://lovable.dev/projects/4dd196d1...)

Use the following prompt for a proper **Lovable.dev** deployment:

Build a Streamlit app that securely analyzes EEG CSV data to detect user intent and stress for authentication. The app should:

Accept a CSV upload (timestamp, channel_1, channel_2, channel_3)

Display signal charts

Show mock predictions: intent verified ✅, stress level 🟢 normal

Be styled with a clear title and section headers
Project name: CogniShield – Cognitive Cyber Defense Platform

---

## 🧑‍💻 Run Locally

```bash
git clone https://github.com/yourname/CogniShield.git
cd CogniShield/frontend
pip install streamlit pandas numpy
streamlit run app_streamlit.py
📜 License
MIT License – open for academic and research use. Attribution appreciated.

🙋 Contact & Collaboration
Built with ❤️ by Aryan Shukla
Contact: [as3061693@gmail.com]

---

Let me know if you'd like:
- A **PowerPoint pitch deck** or **project report**  
- **Custom ML model** trained on real EEG datasets  
- A **GitHub-ready version** with badges, CI/CD, and auto-deploy  

Ready to launch 🚀
