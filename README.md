
# Customer Feedback Emotion Analyzer

An AI-powered web application that analyzes customer feedback and detects the underlying emotions. This project leverages Natural Language Processing (NLP) and Machine Learning techniques to classify emotions from text input, helping businesses better understand customer sentiment.


## 📝Features

🔹Detects emotions such as Happy, Sad, Angry, Neutral, Fear, Surprise, Disgust

🔹 User-friendly web interface for real-time emotion detection

🔹 Built with Machine Learning & NLP techniques

🔹 Scalable for integration into e-commerce platforms, chatbots, and feedback systems


## 📝Tech Stack

🔹**Frontend**: HTML

🔹**Backend**: Python (Flask)

🔹**Libraries & Tools**:
        -pandas, numpy – Data -preprocessing
        -scikit-learn – ML models
        -nltk / spacy – NLP processing
        -Flask / Streamlit – Web app deployment


## 📝Project Structure

│── templates/ # HTML templates

│── model/ # Trained ML model & preprocessing files

│── app.py # Main application script

│── requirements.txt # Dependencies

│── README.md # Project documentation

│── dataset.csv # Training dataset (if included)
## 📝Deployment

To deploy this project run
1️⃣ Clone the repository git clone https://github.com/your-username/Emotion-Detector.git cd Emotion-Detector

2️⃣ Create a virtual environment python -m venv venv source venv/bin/activate # On Mac/Linux venv\Scripts\activate # On Windows

3️⃣ Install dependencies pip install -r requirements.txt

4️⃣ Run the application python app.py

The app will be available at: 👉 http://127.0.0.1:5000/


## 📝 Model training & Use Case

Preprocess text data (tokenization, stopword removal, lemmatization).

Train machine learning models (Naive Bayes, Logistic Regression, or Neural Networks).

Save the trained model using Pickle/Joblib for deployment.

**Use Cases**

📌 E-commerce feedback analysis – Detect customer satisfaction trends.

📌 Social media monitoring – Track public emotions on brands/events.

📌 Chatbots & virtual assistants – Enhance emotional intelligence.
## 📜License

[MIT](https://choosealicense.com/licenses/mit/)

The project was developed as part of the **IBM GEN AI ENGINEERING on Coursera**.  
 
