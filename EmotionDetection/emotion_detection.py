import requests
import json
def emotion_detector(text_to_analyse):
    # Define the URL for the emotion detector API
    url = 'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'
    # Create the payload with the text to be analyzed
    myobj = { "raw_document": { "text": text_to_analyse } }    # Set the headers with the required model ID for the API
    header = {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}

    # Make a POST request to the API with the payload and headers
    response = requests.post(url, json=myobj, headers=header)
    # Parse the response from the API
    formatted_response = json.loads(response.text)

    # If the response status code is 200, extract the label and score from the response
    if response.status_code == 200:
        # Access the dictionary containing all emotion scores
        emotions_dict = formatted_response['emotionPredictions'][0]['emotion']

        anger = emotions_dict['anger']
        disgust = emotions_dict['disgust']
        fear = emotions_dict['fear']
        joy = emotions_dict['joy']
        sadness = emotions_dict['sadness']

        # Determine the dominant emotion
        dominant_emotion, max_score = max(emotions_dict.items(), key=lambda item: item[1])

    # Return all scores and the dominant emotion in a dictionary
    return {
        'anger': anger,
        'disgust': disgust,
        'fear': fear,
        'joy': joy,
        'sadness': sadness,
        'dominant_emotion': dominant_emotion # Include the new key
    }
    '''
    # If the response status code is 500, set all values to None
    elif response.status_code == 500:
        anger = None
        disgust = None
        fear = None
        joy = None
        sadness = None
        dominant_emotion = None # Set dominant_emotion to None as well
    '''
