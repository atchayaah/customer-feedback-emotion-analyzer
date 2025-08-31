"""------------------ Flask web server for the Emotion Detection application.-------------------- """
from flask import Flask, request
from EmotionDetection import emotion_detector

app = Flask(__name__)


@app.route("/emotionDetector", methods=["GET"])
def detect_emotion():
    text = request.args.get("text", default="", type=str)
    result = emotion_detector(text)

    if result.get("dominant_emotion") is None:
        return "Invalid text! Please try again!", 400

    return (
        "For the given statement, the system response is "
        f"'anger': {result['anger']}, 'disgust': {result['disgust']}, "
        f"'fear': {result['fear']}, 'joy': {result['joy']} and "
        f"'sadness': {result['sadness']}. The dominant emotion is "
        f"{result['dominant_emotion']}.",
        200,
    )


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
