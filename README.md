# 🎤 Speech-Based Gender Recognition Agent

## 📌 Project Overview

The **Speech-Based Gender Recognition Agent** is an AI-powered application that predicts the gender of a speaker using acoustic features extracted from speech recordings. The project applies machine learning techniques to classify speakers as **Male** or **Female** and provides an interactive web interface built with Streamlit.

---

## 🎯 Objectives

* Predict speaker gender using speech acoustic features.
* Compare multiple machine learning models.
* Select the best-performing model based on evaluation metrics.
* Deploy the trained model as an AI-powered Streamlit application.
* Generate prediction reports and maintain interaction logs.

---

## 📂 Dataset

**Dataset:** Voice Gender Recognition Dataset

Source: https://www.kaggle.com/datasets/primaryobjects/voicegender

The dataset contains acoustic speech features such as:

* meanfreq
* sd
* median
* Q25
* Q75
* IQR
* skew
* kurt
* sp.ent
* sfm
* mode
* centroid
* meanfun
* minfun
* maxfun
* meandom
* mindom
* maxdom
* dfrange
* modindx

Target Variable:

* label (Male/Female)

---

## 🛠️ Technologies Used

* Python
* Streamlit
* Pandas
* NumPy
* Scikit-learn
* Joblib

---

## 🤖 Machine Learning Models Compared

* Random Forest
* Support Vector Machine (SVM)
* K-Nearest Neighbors (KNN)
* Multi-Layer Perceptron (MLP)
* XGBoost

### Best Model

**Multi-Layer Perceptron (MLP)**

---

## 📊 Evaluation Metrics

The models were evaluated using:

* Accuracy
* Precision
* Recall
* F1-Score
* Confusion Matrix

---

## 🚀 Features of the AI Agent

* Predicts speaker gender using acoustic features.
* Interactive Streamlit web interface.
* Displays prediction results.
* Generates a simple analysis report.
* Maintains interaction logs.
* Fast and easy to use.

---

## 📁 Project Structure

```text
Speech-Gender-Recognition-Agent/
│
├── app.py
├── gender_model.pkl
├── scaler.pkl
├── label_encoder.pkl
├── requirements.txt
├── README.md
└── .gitignore
```

---

## ▶️ How to Run the Project

1. Clone the repository.

2. Install the required libraries:

```bash
pip install -r requirements.txt
```

3. Run the Streamlit application:

```bash
streamlit run app.py
```

4. Open the URL displayed in the terminal to access the application.

---

## 📈 Future Enhancements

* Support direct audio (.wav) file uploads.
* Extract acoustic features automatically from audio.
* Display prediction confidence scores.
* Add voice visualization graphs.
* Support deep learning models such as CNN and LSTM.

---

## 👩‍💻 Author

**Kotapati Gayatri**

AI & Machine Learning Project

Speech-Based Gender Recognition Agent
