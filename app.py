from flask import Flask, request, jsonify
import speech_recognition as sr

app = Flask(__name__)

@app.route('/upload', methods=['POST'])
def upload():
    if 'audio' not in request.files:
        return jsonify({'error': 'No audio file'}), 400

    file = request.files['audio']
    recognizer = sr.Recognizer()
    with sr.AudioFile(file) as source:
        audio = recognizer.record(source)
        text = recognizer.recognize_google(audio, language='ko-KR')

    return jsonify({'text': text})

@app.route('/')
def home():
    return "서버 살아있음"
