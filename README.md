# SMS Spam Detection

Simple Streamlit app for detecting SMS spam using machine learning.

## Live Demo

🔗 [View App](https://your-app-url.streamlit.app) *(update after deployment)*

## Features

- ✅ Real-time spam detection
- ✅ Confidence scores
- ✅ Quick test examples
- ✅ Clean, simple interface

## Tech Stack

- Python 3.11.14
- Streamlit
- scikit-learn
- Logistic Regression + TF-IDF

## Local Setup
```bash
# Clone repo
git clone <your-repo-url>
cd sms-spam-detection

# Install dependencies
pip install -r requirements.txt

# Run app
streamlit run app/streamlit_app.py
```

## Dataset

From [Hands-On AI for Cybersecurity](https://github.com/PacktPublishing/Hands-On-Artificial-Intelligence-for-Cybersecurity/blob/master/Chapter03/datasets/sms_spam_no_header.csv)

## Documentation

This project uses **OpenSpec** for specification-driven development:

- **[openspec/project.md](openspec/project.md)** - Complete project specification, architecture, and coding conventions
- **[openspec/AGENTS.md](openspec/AGENTS.md)** - Guide for working with AI agents on this project
- **[openspec/changes/](openspec/changes/)** - Feature proposals and change history
- **[openspec/schemas/](openspec/schemas/)** - Data structure definitions (YAML)

### For Developers
1. Read [openspec/project.md](openspec/project.md) to understand the codebase
2. Review [openspec/AGENTS.md](openspec/AGENTS.md) for the development workflow
3. Check [openspec/changes/](openspec/changes/) for current and planned features

### For AI Agents
When working on this project, always:
1. Read [openspec/project.md](openspec/project.md) for conventions and architecture
2. Follow the workflow in [openspec/AGENTS.md](openspec/AGENTS.md)
3. Create change proposals before implementing new features

## Teacher's Baseline

Based on: https://github.com/huanchen1107/2025ML-spamEmail