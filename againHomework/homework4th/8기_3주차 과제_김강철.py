import requests
from bs4 import BeautifulSoup

# URL을 읽어서 HTML를 받아오고,
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.86 Safari/537.36'}
data = requests.get(
    'https://www.genie.co.kr/chart/top200?ditc=D&ymd=20200523&hh=23&rtm=N&pg=1', headers=headers)

# HTML을 BeautifulSoup이라는 라이브러리를 활용해 검색하기 용이한 상태로 만듦
soup = BeautifulSoup(data.text, 'html.parser')

# select를 이용해서, tr들을 불러오기
albums = soup.select(
    '#body-content > div.newest-list > div > table > tbody > tr')


# movies (tr들) 의 반복문을 돌리기
rank = 0
for album in albums:
    # movie 안에 a 가 있으면,
    a_tag = album.select_one('td > a.title.ellipsis')
    if a_tag is not None:
        # img 태그의 alt 속성값을 가져오기
        rank += 1
        # rank = album.select_one(‘td.number’).find(text=True, recursive=False)
        # a 태그 사이의 텍스트를 가져오기
        title = a_tag.text
        title_strip = title.strip()
        # td 태그 사이의 텍스트를 가져오기
        singer = album.select_one('td > a.artist.ellipsis').text

        print(rank, title_strip, singer)
