# SMS Spam Detection - Project Specification

## Overview

**Project Name:** SMS Spam Detection
**Version:** 0.1.0
**Status:** Active Development
**Created:** 2025-10-27
**Author:** Matthew Hong

A machine learning-powered SMS spam detection system with an interactive Streamlit web interface. The system uses TF-IDF vectorization and Logistic Regression to classify SMS messages as spam or legitimate (ham) with >95% accuracy.

## Project Goals

- Provide real-time SMS spam classification with confidence scores
- Build a simple, user-friendly web interface for testing
- Achieve >95% classification accuracy on test data
- Create a deployable solution for Streamlit Cloud
- Serve as a learning project for ML and web deployment

## Tech Stack

### Core Technologies
- **Python:** 3.11.14
- **ML Framework:** scikit-learn >= 1.4.0
- **Web Framework:** Streamlit >= 1.31.0
- **Data Processing:** pandas >= 2.0.0, numpy >= 1.24.0
- **Visualization:** matplotlib >= 3.8.0, seaborn >= 0.13.0
- **Model Persistence:** joblib >= 1.3.0

### Machine Learning Components
- **Algorithm:** Logistic Regression (C=2.0, class_weight='balanced')
- **Vectorizer:** TfidfVectorizer
  - max_features: 5000
  - ngram_range: (1, 2)
  - min_df: 2
  - sublinear_tf: True
- **Training Split:** 80/20 train-test, stratified by label
- **Model Performance:** >95% accuracy on test set

### Development Tools
- **Package Manager:** uv (pyproject.toml) + pip (requirements.txt)
- **Version Control:** Git
- **Documentation:** OpenSpec (YAML-based change proposals)
- **IDE:** VSCode with Pylance type checking

## Architecture

### Project Structure

```
sms-spam-detection/
├── app/
│   └── streamlit_app.py      # Main web interface
├── scripts/
│   └── train_model.py         # Model training script
├── models/
│   └── spam_classifier.pkl    # Serialized ML pipeline
├── data/
│   └── sms_spam_no_header.csv # Training dataset
├── openspec/
│   ├── project.md             # This file
│   ├── AGENTS.md              # AI agent workflow guide
│   ├── changes/               # Change proposals (features/fixes)
│   └── schemas/               # Data schemas (YAML)
├── .vscode/
│   └── settings.json          # VSCode Python config
├── pyproject.toml             # Project metadata & dependencies
├── requirements.txt           # Pip-installable dependencies
└── README.md                  # User-facing documentation
```

### Component Details

#### 1. **Streamlit Web App** (`app/streamlit_app.py`)
- **Purpose:** User interface for spam detection
- **Features:**
  - Text area for SMS input
  - Quick example buttons (spam/ham)
  - Real-time prediction with confidence scores
  - Visual result display with progress bar
- **Caching:** Model loaded once via `@st.cache_resource`
- **Error Handling:** Checks for model file existence

#### 2. **Model Training Script** (`scripts/train_model.py`)
- **Purpose:** Train and save the spam classifier
- **Process:**
  1. Load CSV data (5574 SMS messages)
  2. Split into train/test (80/20 stratified)
  3. Build TF-IDF + LogisticRegression pipeline
  4. Train on training data
  5. Evaluate on test data
  6. Save pipeline to `models/spam_classifier.pkl`
- **Output:** Accuracy score and test predictions

#### 3. **ML Pipeline** (`models/spam_classifier.pkl`)
- **Type:** sklearn Pipeline (TfidfVectorizer → LogisticRegression)
- **Input:** Raw SMS text (string)
- **Output:**
  - `predict()`: 'spam' or 'ham' label
  - `predict_proba()`: [ham_prob, spam_prob] array

### Data Flow

```
User Input (SMS text)
    ↓
Streamlit Interface (app/streamlit_app.py)
    ↓
ML Pipeline (models/spam_classifier.pkl)
    ├─→ TF-IDF Vectorization
    └─→ Logistic Regression Classifier
    ↓
Prediction Result
    ├─→ Label: 'spam' or 'ham'
    └─→ Confidence: 0-100%
    ↓
Display Result with Visual Feedback
```

## Data Source

**Dataset:** SMS Spam Collection
**Source:** [Hands-On AI for Cybersecurity - Chapter 3](https://github.com/PacktPublishing/Hands-On-Artificial-Intelligence-for-Cybersecurity)
**File:** `data/sms_spam_no_header.csv`
**Records:** ~5574 SMS messages
**Format:** CSV with 2 columns (no header)
  - Column 1: Label ('spam' or 'ham')
  - Column 2: SMS text content
**Distribution:** Imbalanced (more ham than spam)

## Coding Conventions

### Python Style
- **Style Guide:** PEP 8
- **Line Length:** 88 characters (Black formatter default)
- **Type Hints:** Use where beneficial, especially for function signatures
- **Docstrings:** Use for public functions and classes (Google style)

### File Organization
- **Scripts:** Executable Python files in `scripts/`
- **Applications:** Web apps in `app/`
- **Models:** Serialized models in `models/` (gitignored)
- **Data:** Datasets in `data/` (gitignored)
- **Docs:** OpenSpec documentation in `openspec/`

### Import Order
1. Standard library imports
2. Third-party imports (pandas, sklearn, streamlit)
3. Local application imports
4. Blank line between groups

Example:
```python
import os
from pathlib import Path

import pandas as pd
from sklearn.pipeline import Pipeline
import streamlit as st

from utils import helper_function
```

### Naming Conventions
- **Variables/Functions:** `snake_case`
- **Classes:** `PascalCase`
- **Constants:** `UPPER_SNAKE_CASE`
- **Private members:** `_leading_underscore`
- **Files:** `snake_case.py`

### Error Handling
- Use explicit error messages for user-facing issues
- Check file existence before loading models/data
- Validate user input in Streamlit forms
- Use `st.error()`, `st.warning()` for user feedback

### Type Checking
- **Tool:** Pylance (basic mode)
- **Config:** `.vscode/settings.json`
- **Best Practices:**
  - Handle `None` returns from Streamlit widgets
  - Add null checks before calling methods (e.g., `if text and text.strip()`)

## Development Workflow

### Setup
```bash
# Create virtual environment
python -m venv .venv
source .venv/bin/activate  # Linux/Mac
# OR: .venv\Scripts\activate  # Windows

# Install dependencies
pip install -r requirements.txt

# Train model (first time)
python scripts/train_model.py

# Run Streamlit app
streamlit run app/streamlit_app.py
```

### Making Changes
1. **Propose Change:** Create `openspec/changes/<feature-name>/change.yaml`
2. **Implement:** Write code following conventions above
3. **Test:** Manually test Streamlit interface
4. **Update Status:** Mark change as `implemented` in YAML
5. **Commit:** Use descriptive commit messages

### OpenSpec Change Lifecycle
See [AGENTS.md](./AGENTS.md) for detailed workflow with AI agents.

```
proposed → in_progress → implemented → (optional) deprecated
```

## Deployment

**Platform:** Streamlit Cloud
**URL:** TBD (update after deployment)
**Requirements:**
- Python 3.9+ runtime
- Dependencies from `requirements.txt`
- Pre-trained model in `models/` directory

**Deployment Checklist:**
- [ ] Model file included in repository
- [ ] requirements.txt up to date
- [ ] Streamlit config in `.streamlit/config.toml` (if needed)
- [ ] Update README.md with live URL

## Future Enhancements

See `openspec/changes/` for proposed features and improvements.

**Potential Ideas:**
- Model retraining interface
- Batch prediction (CSV upload)
- API endpoint for programmatic access
- Model performance metrics dashboard
- A/B testing with different algorithms
- Explainability features (feature importance)

## References

- **Teacher's Baseline:** https://github.com/huanchen1107/2025ML-spamEmail
- **Dataset Source:** Packt Publishing - Hands-On AI for Cybersecurity
- **Streamlit Docs:** https://docs.streamlit.io
- **scikit-learn Docs:** https://scikit-learn.org/stable/

---

**Last Updated:** 2025-10-27
**Maintained By:** Matthew Hong
