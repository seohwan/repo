# -*- coding: utf-8 -*-

#---------------------------------
# quizbot.py
#nohup 사용
#“ps -ef | grep 쉘스크립트파일명” 명령으로 데몬형식으로 실행
#nohup python3 quizbot.py &
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
            "text": "1. 공지 사항 2. 일정 3. 연락처 "
            }
        }

    elif content == u"도움말":
        dataSend = {
            "message": {
            "text": "아직 베타버젼입니다. 잠시만 기다려주시면 감사합니다!" +"\n"+"1. 공지 사항 2. 일정 3. 연락처"
            }
        }
    elif content == u"유서환3188":
        tmp= posts.find_all({'title': '1'})
        for idx in tmp:
            print(idx[content])
    elif "2" in content:
        dataSend = {
            "message": {
            "text": "다가오는 일정 : 가을 캠프(준비중입니다) "
            }
        }
    elif u"일정" in content:
        dataSend = {
            "message": {
            "text": "다가오는 일정 : 가을 캠프(준비중입니다) "
            }
        }
    elif "1" in content:
        dataSend = {
            "message": {
            "text": "CISV 가을 캠프를 준비하려고 하는데 캠프 날짜 관련하여 JB 선후배님의 의견을 듣고 싶어 설문 조사를 합니다. 아래 링크로 접속하여 선호하시는 날짜 선택해주시면 감사합니다. ( 중복 선택도 가능합니다 )"
+"http://bit.ly/2weuGVq"
            }
        }

    elif u"공지" in content:
        dataSend = {
            "message": {
            "text": "text": "CISV 가을 캠프를 준비하려고 하는데 캠프 날짜 관련하여 JB 선후배님의 의견을 듣고 싶어 설문 조사를 합니다. 아래 링크로 접속하여 선호하시는 날짜 선택해주시면 감사합니다. ( 중복 선택도 가능합니다 )"
+"http://bit.ly/2weuGVq"
            }
        }
    elif "3" in content:
        dataSend = {
            "message": {
            "text": "유서환"+"\n"+"010-9397-6940"+"\n"+"seohwan91@gmail.com"
            }
        }
    elif u"연락" in content:
        dataSend = {
            "message": {
            "text": "유서환"+"\n"+"010-9397-6940"+"\n"+"seohwan91@gmail.com"
            }
        }


    else:
        dataSend = {
            "message": {
            "text": "형식에 맞게 입력해주시면 감사합니다."
            }
        }
    post_data = {
    'title': '1',
    'content': 'PyMongo is fun, you guys'
    }
    post_data['content']=content
    posts.insert_one(post_data)
    return jsonify(dataSend)

if __name__ == "__main__":
    app.run(host='0.0.0.0', port = 5000)
