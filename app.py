from flask import Flask, request
import os

app = Flask(__name__)

@app.route('/')
def index():
    return "Hello from Flask!"

@app.route('/upload', methods=['POST'])
def upload():
    # 파일 업로드 처리 로직 (예시)
    if 'file' not in request.files:
        return "No file", 400
    file = request.files['file']
    file.save("uploaded.wav")
    return "File received", 200

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 10000))
    app.run(host='0.0.0.0', port=port)

