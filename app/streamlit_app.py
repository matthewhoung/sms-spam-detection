import streamlit as st
import joblib
import os
import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression
from sklearn.pipeline import Pipeline
from sklearn.model_selection import train_test_split

# Page config
st.set_page_config(
    page_title="SMS Spam Detector",
    page_icon="📧",
    layout="centered"
)

# Train model function
def train_model():
    """Train the spam classifier if model doesn't exist"""
    data_path = 'data/sms_spam_no_header.csv'

    if not os.path.exists(data_path):
        st.error(f"Training data not found at {data_path}")
        st.stop()

    with st.spinner("Training model for the first time... This will take a moment."):
        # Load data
        df = pd.read_csv(data_path, header=None, names=['label', 'text'])

        # Split
        X_train, X_test, y_train, y_test = train_test_split(
            df['text'], df['label'],
            test_size=0.2,
            random_state=42,
            stratify=df['label']
        )

        # Create pipeline
        pipeline = Pipeline([
            ('tfidf', TfidfVectorizer(
                max_features=5000,
                ngram_range=(1, 2),
                min_df=2,
                sublinear_tf=True
            )),
            ('clf', LogisticRegression(
                C=2.0,
                class_weight='balanced',
                max_iter=1000,
                random_state=42
            ))
        ])

        pipeline.fit(X_train, y_train)

        # Evaluate
        accuracy = pipeline.score(X_test, y_test)

        # Save
        os.makedirs('models', exist_ok=True)
        joblib.dump(pipeline, 'models/spam_classifier.pkl')

        st.success(f"Model trained successfully! Accuracy: {accuracy:.1%}")

        return pipeline

# Load model
@st.cache_resource
def load_model():
    model_path = 'models/spam_classifier.pkl'
    if not os.path.exists(model_path):
        # Auto-train if model doesn't exist
        return train_model()
    return joblib.load(model_path)

model = load_model()

# Title
st.title("📧 SMS Spam Detection")
st.markdown("Classify SMS messages as spam or legitimate (ham)")

# Quick examples in columns
col1, col2 = st.columns(2)
with col1:
    if st.button("📧 Use Ham Example", use_container_width=True):
        st.session_state.sms_text_area = "Hey, are we still meeting for lunch today?"
with col2:
    if st.button("⚠️ Use Spam Example", use_container_width=True):
        st.session_state.sms_text_area = "URGENT! You've won $1000! Click here NOW to claim!"

# Text input
text = st.text_area(
    "Enter SMS message:",
    height=150,
    placeholder="Type or paste an SMS message here...",
    key="sms_text_area"
)

# Predict
if st.button("🔍 Predict", type="primary", use_container_width=True):
    if text and text.strip():
        with st.spinner("Analyzing..."):
            # Predict
            prediction = model.predict([text])[0]
            proba = model.predict_proba([text])[0]
            
            # Get spam probability
            classes = list(model.classes_)
            spam_idx = classes.index('spam') if 'spam' in classes else 1
            spam_prob = proba[spam_idx]
        
        # Display result
        st.markdown("---")
        st.subheader("Result")
        
        if prediction == 'spam':
            st.error(f"🚨 **SPAM**")
            st.metric("Confidence", f"{spam_prob*100:.1f}%")
        else:
            st.success(f"✅ **HAM (Legitimate)**")
            st.metric("Confidence", f"{(1-spam_prob)*100:.1f}%")
        
        # Progress bar
        st.markdown("**Spam Probability**")
        st.progress(spam_prob)
        
    else:
        st.warning("⚠️ Please enter a message")

# Footer
st.markdown("---")
st.markdown("Built with Streamlit • Dataset from [Packt AI for Cybersecurity](https://github.com/PacktPublishing/Hands-On-Artificial-Intelligence-for-Cybersecurity)")