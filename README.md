## 💳 AI-Powered Fraud Detection in Financial Transactions

## 📖 Overview
This project focuses on detecting fraudulent financial transactions using Machine Learning techniques. With the rapid growth of digital payments, fraud detection has become a critical challenge. This system uses supervised learning models to identify fraudulent patterns in transaction data.

---

## 🚀 Problem Statement
Traditional rule-based fraud detection systems fail to detect evolving fraud patterns and suffer from high false positives. This project aims to build an intelligent, data-driven system capable of identifying fraudulent transactions efficiently.

---

## 📊 Dataset
- Dataset: PaySim Synthetic Financial Dataset (Kaggle)
- Total Records: ~6.3 Million
- Fraud Cases: ~8,000 (~0.13%)

### Features:
- Transaction Type
- Amount
- Old/New Balance (Sender & Receiver)
- Customer ID
- Fraud Label (0 = Legit, 1 = Fraud)

---

## ⚙️ Methodology

### 1. Data Preprocessing
- Handling missing values
- Label encoding categorical features
- Feature scaling using StandardScaler
- Outlier detection and transformation

### 2. Feature Engineering
- Balance change calculation
- Destination balance variation
- High-value transaction indicator

### 3. Handling Class Imbalance
- SMOTE (Synthetic Minority Oversampling Technique)
- Class Weight Adjustment
- Undersampling

### 4. Models Used
- Logistic Regression
- Random Forest
- XGBoost
- Multi-layer Perceptron (Neural Network)

---

## 📈 Results

| Model                | Accuracy | Precision | Recall | F1 Score | AUC-ROC |
|---------------------|----------|----------|--------|----------|----------|
| Logistic Regression | 96.2%    | 0.61     | 0.49   | 0.54     | 0.87     |
| Random Forest       | 98.4%    | 0.84     | 0.77   | 0.80     | 0.94     |
| XGBoost             | 98.9%    | 0.88     | 0.81   | 0.84     | 0.96     |
| MLP Neural Network  | 97.5%    | 0.79     | 0.69   | 0.74     | 0.91     |

✅ XGBoost performed best across all metrics.

---

## 📊 Visualizations
- Histogram analysis
- Correlation heatmap
- Fraud vs Non-Fraud distribution

(Refer to outputs/plots)

---

## 🧠 Key Insights
- Severe class imbalance required special handling
- Fraud mostly occurs in TRANSFER and CASH_OUT
- Feature engineering significantly improved performance
- Ensemble models outperform simple models

---

## 🔮 Future Work
- Real-time fraud detection system
- Deployment using cloud platforms (AWS / GCP)
- Explainability using SHAP / LIME
- Graph-based fraud detection

---

## 🛠️ Tech Stack
- Python
- Pandas, NumPy
- Scikit-learn
- XGBoost
- Matplotlib, Seaborn

---

## 📎 Report
Full project report available here:  
PDF In Repo

---

## 👨‍💻 Author
Trika Jaiswal  
BTech AI & ML  
Symbiosis Institute of Technology

---

## ⭐ If you like this project, give it a star!
