# -*- coding: utf-8 -*-

#---------------------------------
# quizbot.py
#---------------------------------
import os
from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/keyboard')
def Keyboard():
    dataSend = {
        "type" : "buttons",
        "buttons" : ["시작하기", "도움말"]
    }
    return jsonify(dataSend)

@app.route('/message', methods=['POST'])
def Message():

    dataReceive = request.get_json()
    content = dataReceive['content']

    if content == u"시작하기":
        dataSend = {
            "message": {
            "text": "1. 공지 사항 2. 일정 3. 연락처"
            }
        }
    elif content == u"도움말":
        dataSend = {
            "message": {
            "text": "아직 베타버젼입니다. 잠시만 기다려주시면 감사합니다!"
            }
        }
    elif u"일정" in content:
        dataSend = {
            "message": {
            "text": "1. 2017년 8월 27일 오후 5시 코엑스 인터콘티넨탈 호텔 "+"\n"+"2. 10월 중순 가을 캠프 예정"
            }
        }
    elif u"공지" in content:
        dataSend = {
            "message": {
            "text": "8월 27일 오후 5시 코엑스 인터콘티넨탈 호텔에서 해단식을 할 예정입니다. 많은 참석 부탁드립니다."
            }
        }
    elif u"연락" in content:
        dataSend = {
            "message": {
            "text": "010-9397-6940"+"\n"+"seohwan91@gmail.com"
            }
        }
    else:
        dataSend = {
            "message": {
            "text": "형식에 맞게 입력해주시면 감사합니다."
            }
        }
    return jsonify(dataSend)

if __name__ == "__main__":
    app.run(host='0.0.0.0', port = 5000)
