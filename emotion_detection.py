import requests

def emotion_detector(text_to_analyze):
    api_url = 'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'
    api_hdr =  {'grpc-metadata-mm-model-id': 'emotion_aggregated-workflow_lang_en_stock'}
    api_inp = {'raw_document': {'text': text_to_analyze}}
    
    api_res = requests.post(api_url, json = api_inp, headers = api_hdr)

    return api_res.text