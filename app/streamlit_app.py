import streamlit as st
import joblib
import os

# Page config
st.set_page_config(
    page_title="SMS Spam Detector",
    page_icon="📧",
    layout="centered"
)

# Load model
@st.cache_resource
def load_model():
    model_path = 'models/spam_classifier.pkl'
    if not os.path.exists(model_path):
        st.error("Model not found! Run scripts/train_model.py first.")
        st.stop()
    return joblib.load(model_path)

model = load_model()

# Title
st.title("📧 SMS Spam Detection")
st.markdown("Classify SMS messages as spam or legitimate (ham)")

# Quick examples in columns
col1, col2 = st.columns(2)
with col1:
    if st.button("📧 Use Ham Example", use_container_width=True):
        st.session_state.example = "Hey, are we still meeting for lunch today?"
with col2:
    if st.button("⚠️ Use Spam Example", use_container_width=True):
        st.session_state.example = "URGENT! You've won $1000! Click here NOW to claim!"

# Text input
default_text = st.session_state.get('example', '')
text = st.text_area(
    "Enter SMS message:",
    value=default_text,
    height=150,
    placeholder="Type or paste an SMS message here..."
)

# Clear example after using
if 'example' in st.session_state:
    del st.session_state.example

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