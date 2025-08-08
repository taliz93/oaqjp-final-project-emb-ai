'''
server.py
Flask Server encapsulation of EmotionDetection package.
Using IBM Watson for AI Analysis
'''

from flask import Flask, render_template, request
from EmotionDetection.emotion_detection import emotion_detector

app = Flask(__name__)

# T6: Homepage
@app.route('/')
def do_home_page():
    '''
    do_home_page()
    Just renders the homepage
    '''
    return render_template('index.html')

# T6: process emotions
@app.route('/emotionDetector')
def do_detect_emote():
    '''
    do_detect_emote()
    Takes text input and returns a formatted string.
    '''
    req_text = request.args.get('textToAnalyze')
    res_json = emotion_detector(req_text)
    # T7: Error handle
    if res_json['dominant_emotion'] == 'None':
        return "Invalid text! Please try again!"
    out_text = f"For the given statement, the system response is "\
               f"'anger': {res_json['anger']}, 'disgust': {res_json['disgust']}, "\
               f"'fear': {res_json['fear']}, 'joy': {res_json['joy']} and "\
               f"'sadness': {res_json['sadness']}. "\
               f"The dominant emotion is {res_json['dominant_emotion']}."
    return out_text

if __name__ == "__main__":
    app.run(host='0.0.0.0', port = 5000)
