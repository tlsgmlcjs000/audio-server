from flask import Flask, request, jsonify
import speech_recognition as sr
from werkzeug.utils import secure_filename
import os

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = 'uploads'

# uploads 폴더 없으면 생성
os.makedirs(app.config['UPLOAD_FOLDER'], exist_ok=True)

@app.route('/')
def index():
    return 'Flask 서버 정상 동작 중!'

@app.route('/upload', methods=['POST'])
def upload():
    if 'audio' not in request.files:
        return 'No file', 400

    file = request.files['audio']
    filename = secure_filename(file.filename)
    filepath = os.path.join(app.config['UPLOAD_FOLDER'], filename)
    file.save(filepath)

    recognizer = sr.Recognizer()

    try:
        with sr.AudioFile(filepath) as source:
            audio = recognizer.record(source)
            text = recognizer.recognize_google(audio, language='ko-KR')
            return jsonify({'text': text})
    except sr.UnknownValueError:
        return jsonify({'text': '음성을 인식할 수 없습니다.'})
    except sr.RequestError as e:
        return jsonify({'text': f'Google API 오류: {e}'})
    except Exception as e:
        return jsonify({'text': f'오류 발생: {str(e)}'})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=10000)


