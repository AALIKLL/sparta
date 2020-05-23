import requests
from bs4 import BeautifulSoup

# 타겟 URL을 읽어서 HTML를 받아오고,
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.86 Safari/537.36'}
data = requests.get(
    'https://movie.naver.com/movie/sdb/rank/rpeople.nhn', headers=headers)

soup = BeautifulSoup(data.text, 'html.parser')

actors = soup.select('#old_content > table > tbody > tr')

# rank = 1

for actor in actors:
    a_tag = actor.select_one('td.title > a')
    if a_tag is not None:
        rank = actor.select_one('td.ac > img')['alt']
        name = a_tag.text
        birth = actor.select_one('td.birth > a').text
        print(rank, name, birth)
