from pymongo import MongoClient           # pymongo를 임포트 하기(패키지 인스톨 먼저 해야겠죠?)
from bs4 import BeautifulSoup
import requests
from flask import Flask, render_template, jsonify, request
app = Flask(__name__)


client = MongoClient('localhost', 27017)  # mongoDB는 27017 포트로 돌아갑니다.
db = client.dbsparta                      # 'dbsparta'라는 이름의 db를 만듭니다.

# HTML을 주는 부분


@app.route('/')
def home():
    return render_template('home.html')


@app.route('/memo', methods=['GET'])
def listing():
    # 1. 모든 document 찾기 & _id 값은 출력에서 제외하기
    orders = list(db.orders.find({}, {'_id': False}))
    # 2. articles라는 키 값으로 영화정보 내려주기
    return jsonify({'result': 'success', 'msg': 'GET 연결되었습니다!', 'orders': orders})

# API 역할을 하는 부분


@app.route('/memo', methods=['POST'])
def saving():
    # 1. 클라이언트로부터 데이터를 받기
    name = request.form['name_give']
    select = request.form['select_give']
    address = request.form['address_give']
    phone = request.form['phone_give']
    # 2. meta tag를 스크래핑하기
    # 3. mongoDB에 데이터 넣기
    order = {
        'name': name,
        'select': select,
        'address': address,
        'phone': phone,
    }
    db.orders.insert_one(order)
    return jsonify({'result': 'success', 'msg': 'POST 연결되었습니다!'})


if __name__ == '__main__':
    app.run('0.0.0.0', port=5000, debug=True)
