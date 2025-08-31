"""
Emotion detection utility using IBM Watson NLP (embedded service).
"""
import requests

WATSON_URL = (
    "https://sn-watson-emotion.labs.skills.network/"
    "v1/watson.runtime.nlp.v1/NlpService/EmotionPredict"
)
WATSON_HEADERS = {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}


def emotion_detector(text_to_analyse):
    """
    Call Watson NLP EmotionPredict and return scores + dominant emotion.
    For blank input, return 0 scores and None as dominant_emotion.
    """
    if not text_to_analyse:
        return {
            "anger": 0,
            "disgust": 0,
            "fear": 0,
            "joy": 0,
            "sadness": 0,
            "dominant_emotion": None,
        }

    payload = {"raw_document": {"text": text_to_analyse}}
    response = requests.post(WATSON_URL, headers=WATSON_HEADERS, json=payload)

    if response.status_code == 200:
        data = response.json()
        emotions = data["emotionPredictions"][0]["emotion"]

        scores = {
            "anger": emotions.get("anger", 0),
            "disgust": emotions.get("disgust", 0),
            "fear": emotions.get("fear", 0),
            "joy": emotions.get("joy", 0),
            "sadness": emotions.get("sadness", 0),
        }
        scores["dominant_emotion"] = max(scores, key=scores.get)
        return scores

    if response.status_code == 400:  # blank/invalid input case
        return {
            "anger": 0,
            "disgust": 0,
            "fear": 0,
            "joy": 0,
            "sadness": 0,
            "dominant_emotion": None,
        }

    # Fallback in case of other errors
    return {
        "anger": 0,
        "disgust": 0,
        "fear": 0,
        "joy": 0,
        "sadness": 0,
        "dominant_emotion": None,
    }
