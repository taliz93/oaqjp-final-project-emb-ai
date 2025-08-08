import requests, json

def emotion_detector(text_to_analyze):
    # T2: setup vars
    api_url = 'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'
    api_hdr =  {'grpc-metadata-mm-model-id': 'emotion_aggregated-workflow_lang_en_stock'}
    api_inp = {'raw_document': {'text': text_to_analyze}}
    # T2: call api
    api_res = requests.post(api_url, json = api_inp, headers = api_hdr)
    # T2: get raw text response
    res_txt = api_res.text
    # T3: convert to dict
    res_json = json.loads(res_txt)
    tmp_emotes = res_json['emotionPredictions'][0]['emotion']
    # T3: find highest rank
    tmp_dom = 'unsure'
    tmp_num = 0.0
    for emote in tmp_emotes:
        if tmp_emotes[emote] >= tmp_num:
            tmp_num = tmp_emotes[emote]
            tmp_dom = emote
    # T3: create output dict
    out_json = {
        'anger': tmp_emotes['anger'],
        'disgust': tmp_emotes['disgust'],
        'fear': tmp_emotes['fear'],
        'joy': tmp_emotes['joy'],
        'sadness': tmp_emotes['sadness'],
        'dominant_emotion': tmp_dom
    }
    return out_json