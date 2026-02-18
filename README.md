# 🫁 Chest Disease Classification using AI

## 📌 Project Overview
This project is an AI-powered web application that analyzes chest X-ray images and predicts whether the lungs are Normal or affected by Adenocarcinoma Cancer using deep learning techniques.

The system provides:
- Disease prediction
- Confidence score
- Medical explanation
- Real-time results via web interface

---

## 🎯 Problem Statement
Manual interpretation of chest X-rays is time-consuming and prone to human error.  
This project aims to assist healthcare professionals by providing automated AI-based preliminary diagnosis.

---

## 🧠 AI Approach
A Convolutional Neural Network (CNN) model is used to extract features from chest X-ray images and classify them into disease categories.

Workflow:
1. Image Upload
2. Preprocessing (resize, normalization)
3. Model Inference
4. Prediction Generation
5. Confidence Calculation
6. Result Display

---

## ✨ Features
- Upload chest X-ray image
- AI-based disease classification
- Confidence score visualization
- Medical explanation output
- Real-time prediction
- User-friendly web interface

---

## 🛠️ Technologies Used

Backend:
- Python
- Flask
- TensorFlow / Keras
- NumPy
- Pillow
- PyYAML

Frontend:
- HTML
- CSS
- JavaScript
- Bootstrap
- jQuery

---

## 📂 Project Structure

ChestDisease-AI-App/
│
├── Respire/        → Prediction pipeline & utilities  
├── templates/      → Frontend HTML files  
├── Config/         → Configuration files  
│
├── app.py          → Main Flask application  
├── requirements.txt  
├── README.md  
├── .gitignore  

---

## ▶️ How to Run the Project

1. Clone the repository

git clone <your-repository-link>  
cd ChestDisease-AI-App  

2. Install dependencies

pip install -r requirements.txt  

3. Run the application

python app.py  

4. Open in browser

http://localhost:5000  

---

## 📊 Output
The system displays:
- Predicted disease category
- Confidence percentage
- Medical explanation
- Uploaded image preview

---

## ⚠️ Disclaimer
This project is intended for educational and research purposes only.  
It is not a substitute for professional medical diagnosis.

---

## 👨‍🎓 Internship Project
Developed as part of an AI/ML internship to demonstrate:
- Machine Learning deployment
- AI-based medical image analysis
- Web application integration
- End-to-end project development

---

## 👤 Author
Onkar Dhope

---

## ⭐ If you found this project useful, consider giving it a star!
