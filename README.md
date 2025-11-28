# 🫁🦠 Lung Cancer Analytics & AI Decision Support System  
### 🔥 End-to-End Data Science Project (EDA + Power BI + Machine Learning + Chatbot)

---

## 📖 Overview  
This project delivers a complete analytical & predictive healthcare system for lung cancer patients.  
We transformed raw clinical data → into insights → dashboards → machine learning models → AI chatbot capable of answering medical queries.

---

## 🧠 Key Features

| Feature | Description |
|---|---|
| 🩺 Descriptive Analytics | Full overview of patient profiles, stage distribution & risk segmentation |
| 📊 Power BI Dashboard | 3 interactive pages — 21+ visual charts, KPIs & slicers |
| 🤖 Machine Learning | Logistic Regression + Random Forest for survival prediction |
| 🧬 Feature Engineering | Age groups, BMI categories, risk scoring system |
| 🔥 Chatbot System | Answers survival-related & treatment-effectiveness queries instantly |

---

## 📂 Repository Structure

Lung-Cancer-Analytics-AI-System/
├─ data/
│   ├─ raw_dataset.csv
│   └─ lung_cancer_cleaned_vFinal.csv

├─ notebooks/
│   ├─ 01_data_cleaning.ipynb
│   ├─ 02_eda_analysis.ipynb
│   ├─ 03_feature_engineering.ipynb
│   └─ 04_machine_learning_models.ipynb

├─ models/
│   ├─ random_forest.pkl
│   └─ logistic_regression.pkl

├─ powerBI_dashboard/
│   └─ LungCancer_Analytics.pbix

└─ chatbot/
    └─ medical_chatbot.py


---

## 📊 Power BI Dashboard Summary

### Page 1 — Patient Distribution Overview
✔ Age groups, gender & country breakdown  
✔ BMI levels + smoking categories  
✔ Risk segmentation (Low/Medium/High)  
✔ KPI Cards → Avg Age, Avg BMI, Survival %, High-Risk %  

### Page 2 — Treatment & Survival Analytics
✔ Survival % by cancer stage  
✔ Treatment outcome comparison  
✔ BMI + Smoking correlations  
✔ Risk & survival cross-analysis  
✔ Treatment duration effectiveness review  

### Page 3 — Predictive Intelligence Layer
✔ Feature importance from ML models  
✔ Risk clusters & probability distribution  
✔ Low/High survival groups detected  
✔ Early-detection decision support  

---

## 🔍 Key Insights

- Age **51–70** dominates patient population → critical target group  
- Survival rate is low overall (~22%) → urgent need for early detection  
- Medium + High Risk groups = **≈98%** of dataset  
- Best outcome seen in **Stage I + Chemo + Normal BMI (33% survival approx.)**
- Smoking effect increases drastically when combined with Stage III/IV  
- Surgery/Radiation outperform Chemotherapy alone in similar stage cases  
- Duration of treatment does NOT always correlate with survival → review required  
- Obesity & comorbidities strongly shift patients into high-risk categories  

---

## 🤖 Machine Learning Models

| Model | Accuracy | Purpose |
|---|---|---|
| Logistic Regression | 77% | Baseline survival prediction model |
| Random Forest | Higher performance | Better for non-linear medical relationships |

Why Random Forest was chosen  
✔ Handles mixed clinical features well  
✔ Captures deeper stage-treatment interactions  
✔ Provides feature importance for doctors & analysts  

---

## 🧠 Chatbot Capabilities  
The chatbot answers analytical questions like:

"What stage has lowest survival?"
"Which treatment is best for Stage II patients?"
"Show survival rate for overweight smokers."


Useful for → doctors, research units, medical decision-making.

---

## 📌 Recommendations

| Recommendation | Benefit |
|---|---|
| Early diagnosis focus on ages 51–70 | Most affected & highest risk |
| Weight & smoking intervention programs | Modifiable survival-improving factors |
| Review Chemo-only strategies | Lower recovery performance |
| Prioritize high-risk cases via model | ICU allocation strategy |
| Expand clinical attributes collected | Improve predictive accuracy |

---

## 🏁 Conclusion  
This project successfully builds a **complete AI-driven medical analytics ecosystem** capable of:

✔ Risk assessment  
✔ Survival forecasting  
✔ Treatment outcome analysis  
✔ Automated medical knowledge retrieval  

A scalable foundation for real hospital integration.

---

## 🔧 How to Run

git clone https://github.com/Mohamed934789/Lung-Cancer-Data-Analysis.git

cd project-folder
pip install -r requirements.txt
jupyter notebook


Power BI → open `.pbix`  
Chatbot → run `medical_chatbot.py`

---

## 👤 Author  
**Mohamed Kassab — AI/Data Science Engineer**  
🔬 Machine Learning | Analytics | Healthcare Systems  

⭐ If you like this project, don't forget to star the repository!

