import requests

WATSON_URL = (
    "https://sn-watson-emotion.labs.skills.network/"
    "v1/watson.runtime.nlp.v1/NlpService/EmotionPredict"
)
WATSON_HEADERS = {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}


def emotion_detector(text_to_analyse):
    """
    Call Watson NLP EmotionPredict and return scores + dominant emotion.
    For blank input, return all None values.
    """
    if not text_to_analyse:
        return {
            "anger": None,
            "disgust": None,
            "fear": None,
            "joy": None,
            "sadness": None,
            "dominant_emotion": None,
        }

    payload = {"raw_document": {"text": text_to_analyse}}
    response = requests.post(WATSON_URL, headers=WATSON_HEADERS, json=payload)

    if response.status_code == 200:
        data = response.json()
        emotions = data["emotionPredictions"][0]["emotion"]

        anger = emotions.get("anger", 0)
        disgust = emotions.get("disgust", 0)
        fear = emotions.get("fear", 0)
        joy = emotions.get("joy", 0)
        sadness = emotions.get("sadness", 0)

        scores = {
            "anger": anger,
            "disgust": disgust,
            "fear": fear,
            "joy": joy,
            "sadness": sadness,
        }
        scores["dominant_emotion"] = max(scores, key=scores.get)
        return scores

    if response.status_code == 400:  # blank input case
        return {
            "anger": None,
            "disgust": None,
            "fear": None,
            "joy": None,
            "sadness": None,
            "dominant_emotion": None,
        }

    return {"anger": None, "disgust": None, "fear": None,
            "joy": None, "sadness": None, "dominant_emotion": None}
