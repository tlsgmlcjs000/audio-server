from flask import Flask, request, jsonify
import speech_recognition as sr
import os

app = Flask(__name__)

@app.route('/upload', methods=['POST'])
def upload():
    if 'audio' not in request.files:
        return jsonify({'error': 'No audio file'}), 400

    audio_file = request.files['audio']
    recognizer = sr.Recognizer()

    with sr.AudioFile(audio_file) as source:
        audio = recognizer.record(source)

    try:
        text = recognizer.recognize_google(audio, language="ko-KR")
    except sr.UnknownValueError:
        text = "음성을 인식할 수 없습니다."
    except sr.RequestError:
        text = "음성 인식 서비스에 접근할 수 없습니다."

    return jsonify({'text': text})


# ⛔️ 여기!! 이게 핵심!!
if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))  # Render가 지정하는 PORT 사용
    app.run(host='0.0.0.0', port=port)
