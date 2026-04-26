# 🔐 Phishing URL Detection using Machine Learning

## 📌 Project Overview
Phishing is a type of cyberattack where attackers create fake websites to steal sensitive information like usernames, passwords, and financial details.  

This project aims to build a **Machine Learning model** that can automatically detect whether a given URL is:
- ✅ Legitimate  
- ❌ Phishing  

The system analyzes various URL-based and domain-based features to make predictions.

---

## 🎯 Objective
- Detect phishing websites using Machine Learning techniques  
- Improve cybersecurity by identifying malicious URLs  
- Provide a simple system where users can check URL safety  

---

## ⚙️ Technologies Used
- Python  
- NumPy  
- Pandas  
- Scikit-learn  
- Matplotlib / Seaborn  
- Flask (for deployment, if included)

---

## 📊 Dataset
The dataset contains:
- Phishing URLs  
- Legitimate URLs  

Each URL is labeled as:
- `0` → Legitimate  
- `1` → Phishing  

---

## 🔍 Feature Extraction
Features are extracted from URLs to train the model. Common features include:

### 🔹 URL-based Features
- Length of URL  
- Presence of `@`, `-`, `//`  
- Number of dots  

### 🔹 Domain-based Features
- Domain age  
- DNS record  

### 🔹 Security Features
- HTTPS usage  
- SSL certificate  

Machine learning models learn patterns from these features to classify URLs 2.

---

## 🤖 Machine Learning Models Used
- Logistic Regression  
- Decision Tree  
- Random Forest  
- Support Vector Machine (SVM)  
- K-Nearest Neighbors (KNN)  

Among these, Random Forest often gives the best performance in phishing detection tasks 3.

---

## 🧠 Workflow
