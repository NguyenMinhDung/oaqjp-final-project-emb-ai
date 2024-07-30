import requests
import json

def emotion_detector(text_to_analyze):
    url = 'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'
    data = json.dumps({
        "raw_document": {
            "text": text_to_analyze
        }
    })
    headers = {
        'grpc-metadata-mm-model-id': 'emotion_aggregated-workflow_lang_en_stock',
        'Content-Type': 'application/json'
    }
    response = requests.post(url, headers=headers, data=data)

    if response.status_code == 400:
        return {
            "anger": None, 
            "disgust": None, 
            "fear": None, 
            "joy": None, 
            "sadness": None, 
            'dominant_emotion': None
        }

    formatted_response = json.loads(response.text)
    predicted_emotion = formatted_response['emotionPredictions'][0]['emotion']
    dominant_emotion = max(predicted_emotion, key=predicted_emotion.get)

    return {
        **predicted_emotion,
        'dominant_emotion': dominant_emotion
    }