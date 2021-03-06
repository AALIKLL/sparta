from pymongo import MongoClient           # pymongo를 임포트 하기(패키지 인스톨 먼저 해야겠죠?)
from flask import Flask, render_template, jsonify, request
app = Flask(__name__)

client = MongoClient('localhost', 27017)  # mongoDB는 27017 포트로 돌아갑니다.
db = client.dbsparta                      # 'dbsparta'라는 이름의 db를 만듭니다.

# HTML을 주는 부분


@app.route('/')
def home():
    return render_template('index.html')

# API 역할을 하는 부분


@app.route('/reviews', methods=['POST'])
def write_review():
    print(request.form)
    # 데이터를 읽어 온다
    title_receive = request.form['title_give']
    author_receive = request.form['author_give']
    review_receive = request.form['review_give']
    # 저자, 제목, 리뷰
    review = {
        'title': title_receive,
        'author': author_receive,
        'review': review_receive,
    }
    # DB에 넣는다
    db.reviews.insert_one(review)
    return jsonify({'result': 'success', 'msg': '성공적으로 등록을 완료하였습니다!'})


@app.route('/reviews', methods=['GET'])
def read_reviews():
    # DB야 리뷰 다 들고 와 (마지막에서 '_id'는 False로 들고 오지 않도록!!)
    reviews = list(db.reviews.find({}, {'_id': False}))
    # jsonify로 읽어들어오기
    return jsonify({
        'result': 'success',
        'msg': '이 요청은 GET!',
        'reviews': reviews
    })


if __name__ == '__main__':
    app.run('0.0.0.0', port=5000, debug=True)
