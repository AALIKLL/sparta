from pymongo import MongoClient
client = MongoClient('localhost', 27017)
db = client.dbsparta

## 코딩 할 준비 ##

title_movie = db.cinema.find_one({'title': '매트릭스'})
metrix = title_movie['star']


sameStarMovies = list(db.cinema.find({'star': metrix}))
for sameStar in sameStarMovies:
    print(sameStar['title'])
