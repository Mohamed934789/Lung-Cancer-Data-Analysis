import streamlit as st
import pandas as pd
import google.generativeai as genai

# =========[ Gemini API Key ]=========
GEMINI_API_KEY = "AIzaSyDiIgLFcrKCOBQPINwA0_AXvzq_VzD-soI"
genai.configure(api_key=GEMINI_API_KEY)

# =========[ Background Image ]=========
BACKGROUND_URL = "https://plus.unsplash.com/premium_photo-1673953509975-576678fa6710?q=80&w=1170&auto=format&fit=crop&ixlib=rb-4.1.0&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D"

# =========[ Page Config ]=========
st.set_page_config(
    page_title="Medical Data Assistant",
    page_icon="🩺",
    layout="wide"
)

# =========[ Background + Text Colors ]=========
background_css = f"""
<style>
.stApp {{
    background-image: url("{BACKGROUND_URL}");
    background-size: cover;
    background-attachment: fixed;
}}

.block-container {{
    background-color: rgba(255, 255, 255, 0.85);
    padding: 25px 40px;
    border-radius: 20px;
    backdrop-filter: blur(10px);
}}

h1, h2, h3, h4, h5, h6 {{
    background-color: rgba(0, 102, 204, 0.8); /* Blue transparent background for titles */
    padding: 10px 15px;
    border-radius: 12px;
    color: white !important;
}}

p, label, span, div {{
    color: #0a0a0a !important;
}}

.stButton button {{
    background-color: #0066cc;
    color: white !important;
    border-radius: 10px;
    padding: 10px 18px;
    font-size: 16px;
    font-weight: bold;
}}

.stButton button:hover {{
    background-color: #004c99;
}}

.sidebar .sidebar-content {{
    background-color: rgba(0, 153, 102, 0.2); /* Light green transparent */
    border-radius: 15px;
    padding: 15px;
}}
</style>
"""
st.markdown(background_css, unsafe_allow_html=True)

# =========[ Suggested Questions ]=========
suggested_questions = [
     "What is the age distribution of the patients?",
    "Which gender has the highest number of cancer cases?",
    "Which countries report the most patients?",
    "What is the distribution of cancer stages?",
    "How does cancer stage relate to patient survival?",
    "Does smoking status affect survival rates?",
    "Is there a correlation between BMI and cancer stage?",
    "How does cholesterol level vary across different age groups?",
    "Does family history influence cancer stage?",
    "What is the most common treatment type?",
    "Which treatment type has the highest survival rate?",
    "How many patients completed treatment successfully?",
    "What is the average treatment duration?",
    "Do chronic diseases like asthma or hypertension affect survival?",
    "What percentage of patients have other cancer types?"
]

# =========[ Sidebar Section ]=========
st.sidebar.title("💡 Suggested Questions")
selected_q = st.sidebar.radio("Select a suggested question:", suggested_questions)
st.sidebar.write("Or copy any question below 👇")

# =========[ Load Data ]=========
uploaded_file = st.file_uploader("Upload your Excel or CSV file", type=["xlsx", "csv"])
df = None
if uploaded_file is not None:
    if uploaded_file.name.endswith(".xlsx"):
        df = pd.read_excel(uploaded_file)
    else:
        df = pd.read_csv(uploaded_file)

# =========[ Ask Function ]=========
def ask_gemini(question, dataframe):
    context = dataframe.head(500).to_string()
    model = genai.GenerativeModel("gemini-2.5-flash-lite")

    prompt = f"""
    ou are a professional healthcare data analyst. 
You are analyzing a large medical dataset related to cancer patients.
The dataset contains patient demographics, cancer stage, treatment details, and survival outcomes.

Assumptions you MUST follow:
- If a question is asked, answer based on the provided columns even if the information is indirect.
- You are allowed to infer insights using counts, grouping, correlations, distributions, etc.
- Do NOT say “The data does not contain enough information” unless the information TRULY does not exist.
- Gender, cancer_stage, treatment_type, and survival can always be analyzed through grouping.
- If the question is broad, interpret it as a data-analysis task and give a meaningful statistical answer."

    {context}

    Question: {question}
    """
    response = model.generate_content(prompt)
    return response.text

# =========[ UI ]=========
st.title("🩺 Medical Data Chatbot")
st.write("Ask any question about the medical data and get accurate answers.")

if df is not None:
    st.write("### Preview of your data:")
    st.dataframe(df)

    question = st.text_area("Type your question here:", value=selected_q)

    if st.button("Ask"):
        if question.strip():
            with st.spinner("Analyzing data..."):
                answer = ask_gemini(question, df)
            st.success("Answer:")
            st.write(answer)
        else:
            st.warning("Please type a question first ✏️")
else:
    st.info("Please upload your data file first 📂")
