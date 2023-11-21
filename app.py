from flask import Flask, request,jsonify
from routes import generate_response_from_bard
from flask_cors import CORS
import json


app = Flask(__name__)
CORS(app)
CORS(app,resource={r'*':{'origins':'*'}})

@app.route('/')
def hello():
    return "정상 작동 중!"

# Bard AI
@app.route('/bard', methods=['POST'])
def chat_with_bard():
    data = request.get_json()
    user_message = data['message']
    user_facs = data['facs']
    user_tags = data['tags']

    bot_reply = generate_response_from_bard(user_message, user_facs, user_tags)

    return jsonify({"message": bot_reply})       


if __name__ == '__main__':
    app.run(host= '0.0.0.0',port=5000)  # 포트 번호를 8080으로 변경
