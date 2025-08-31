# Customer Feedback Emotion Analyzer

Final project: AI-based web application for analyzing customer feedback emotions.

## Features
- Uses IBM Watson NLP embedded endpoint for emotion detection.
- Returns 5 emotions: anger, disgust, fear, joy, sadness.
- Identifies the dominant emotion.
- Flask web deployment (`/emotionDetector` endpoint).
- Handles blank input with proper error messages.
- Unit tests included.
- PEP8/Pylint compliant.

## Quickstart
```bash
# Create virtual environment
python3 -m venv .venv
source .venv/bin/activate   # Windows: .venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt

# Run unit tests
python -m unittest

# Start Flask server
python server.py
