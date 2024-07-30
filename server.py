"""
Emotion Detector Flask Application

This module that provides an interface for detecting emotions in text.
The application has two routes:
1. '/' - Renders the index page.
2. '/emotionDetector' - Accepts a text input as a query parameter and returns the detected emotions.

Modules:
    flask: Flask web framework.
    request: To handle HTTP requests.
    render_template: To render HTML templates.
    emotion_detector: A function to detect emotions in text.

Functions:
    index(): Renders the index.html template.
    emotionDetector(): Analyzes the provided text and returns the detected emotions.
"""
from flask import Flask, request, render_template
from EmotionDetection import emotion_detection

app = Flask(__name__)

@app.route('/')
def index():
    """
    Renders the index page.

    Returns:
        str: The rendered HTML of the index page.
    """
    return render_template('index.html')

@app.route("/emotionDetector")
def emotion_detector():
    """
    Analyzes the provided text and returns the detected emotions.

    Query Parameters:
        textToAnalyze (str): The text to be analyzed for emotions.

    Returns:
        str: A string describing the detected emotions and the dominant emotion.
    """
    text = request.args.get('textToAnalyze')
    result = emotion_detection.emotion_detector(text)

    if not result['dominant_emotion']:
        return 'Invalid text! Please try again!.'

    return f"""For the given statement, the system response is
        'anger': {result['anger']}, 'disgust': {result['disgust']},
        'fear': {result['fear']}, 'joy': {result['joy']},
        'sadness': {result['sadness']}. The dominant emotion is {result['dominant_emotion']}"""


if __name__ == '__main__':
    app.run(debug=True)
