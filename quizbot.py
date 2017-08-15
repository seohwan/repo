# -*- coding: utf-8 -*-

#---------------------------------
# quizbot.py
#nohup 사용
#“ps -ef | grep 쉘스크립트파일명” 명령으로 데몬형식으로 실행
#---------------------------------
import os
from pymongo import MongoClient
client = MongoClient()
from flask import Flask, request, jsonify
client = MongoClient('localhost', 27017)
db = client['cisv']
app = Flask(__name__)
posts = db.ask
annouce = db.announce
#result = posts.insert_one(post_data)
#print('One post: {0}'.format(result.inserted_id))
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
            "text": "1. 공지 사항 2. 일정 3. 연락처 4. 문의 및 건의"
            }
        }

    elif content == u"도움말":
        dataSend = {
            "message": {
            "text": "아직 베타버젼입니다. 잠시만 기다려주시면 감사합니다!" +"\n"+"1. 공지 사항 2. 일정 3. 연락처 4. 문의 및 건의"
            }
        }
    elif u"일정" or "2" in content:
        dataSend = {
            "message": {
            "text": "다가오는 일정 :2017년 8월 27일 오후 5시 코엑스 인터콘티넨탈 호텔 "
            }
        }
    elif u"문의" or "건의" or "4" in content:
        dataReceive = request.get_json()
        content = dataReceive['content']
        post_data = {
        'title': '1',
        'content': 'PyMongo is fun, you guys',
        'author': 'Scott'
        }
        post_data['content']=content
        posts.insert_one(post_data)

    elif u"공지" or "1" in content:
        dataSend = {
            "message": {
            "text": "8월 27일 오후 5시 코엑스 인터콘티넨탈 호텔에서 해단식을 할 예정입니다. 많은 참석 부탁드립니다."
            }
        }
    elif u"연락" or "3" in content:
        dataSend = {
            "message": {
            "text": "유서환"+"\n"+"010-9397-6940"+"\n"+"seohwan91@gmail.com"
            }
        }
    elif u"문의" or "건의" or "4" in content:
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
