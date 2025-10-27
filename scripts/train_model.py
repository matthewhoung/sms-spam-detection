import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression
from sklearn.pipeline import Pipeline
from sklearn.model_selection import train_test_split
import joblib
import os

# Load data
print("Loading data...")
df = pd.read_csv('data/sms_spam_no_header.csv')

# Split
X_train, X_test, y_train, y_test = train_test_split(
    df['text'], df['label'], 
    test_size=0.2, 
    random_state=42, 
    stratify=df['label']
)

# Create pipeline
print("Training model...")
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
print(f"Accuracy: {accuracy:.3f} ({accuracy*100:.1f}%)")

# Save
os.makedirs('models', exist_ok=True)
joblib.dump(pipeline, 'models/spam_classifier.pkl')
print("Model saved to models/spam_classifier.pkl")

# Test
test_spam = "FREE entry! Win £1000 cash!"
test_ham = "Hey, are we still on for dinner?"
print(f"\nTest spam: {pipeline.predict([test_spam])[0]}")
print(f"Test ham: {pipeline.predict([test_ham])[0]}")