# dashboard.py

import streamlit as st
import pandas as pd
import pickle
import re
from sklearn.feature_extraction.text import TfidfVectorizer

#Load model and vectorizer
with open('model/vectorizer.pkl', 'rb') as f:
    vectorizer = pickle.load(f)

with open('model/classifier.pkl', 'rb') as f:
    model = pickle.load(f)

#Function to clean text
def clean_text(text):
    if pd.isnull(text):
        return ""
    text = text.lower()
    text = re.sub(r'[^a-zA-Z0-9\s]', '', text)
    text = re.sub(r'\s+', ' ', text)
    return text.strip()

#Streamlit UI
st.title("🔍 Spot the Scam - Job Fraud Detector")

uploaded_file = st.file_uploader("Upload a CSV file with job postings", type=['csv'])

if uploaded_file:
    df = pd.read_csv(uploaded_file)

    # Clean and prepare
    text_cols = ['title', 'description', 'requirements', 'benefits']
    for col in text_cols:
        df[col] = df[col].apply(clean_text)

    df['text'] = df[text_cols].agg(' '.join, axis=1)

    # Vectorize and predict
    X = vectorizer.transform(df['text'])
    probs = model.predict_proba(X)[:, 1]
    preds = model.predict(X)

    # Add results to dataframe
    df['Fraud Probability'] = probs
    df['Prediction'] = preds
    df['Prediction Label'] = df['Prediction'].map({0: 'Genuine', 1: 'Fraudulent'})

    #Display Results
    st.subheader("📄 Prediction Table")
    st.dataframe(df[['title', 'location', 'Fraud Probability', 'Prediction Label']].sort_values(by='Fraud Probability', ascending=False))

    # Pie Chart
    st.subheader("📊 Real vs Fake Jobs")
    pie_data = df['Prediction Label'].value_counts()
    st.pyplot(pie_data.plot.pie(autopct='%1.1f%%', figsize=(10, 30)).get_figure())

    #Histogram
    st.subheader("📈 Fraud Probability Histogram")
    st.bar_chart(df['Fraud Probability'])

    # Top 10 Suspicious Jobs
    # st.subheader("🚨 Top 10 Most Suspicious Jobs")
    # st.table(df[['title', 'location', 'Fraud Probability']].sort_values(by='Fraud Probability', ascending=False).head(10))
