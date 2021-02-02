import requests
from bs4 import BeautifulSoup
# 객체를 받아서 객체에 있는 뉴스 리스트를 참조 이를 통해 본문 초기화하는 함수
def get_headline():
    url_format = 'https://news.naver.com/main/read.nhn?mode=LSD&mid=shm&sid1=104&oid=018&aid=0004843179'
    re = requests.get(url_format,headers={'User-Agent':'Mozilla/5.0'})
    html= BeautifulSoup(re.text,'html.parser')
    headlines = html.select_one('#articleBodyContents')
    print(headline)
    return
def get_headline():
    url_format = 'https://news.naver.com/main/read.nhn?mode=LSD&mid=shm&sid1=104&oid=018&aid=0004843179'
    re = requests.get(url_format,headers={'User-Agent':'Mozilla/5.0'})
    html= BeautifulSoup(re.text,'html.parser')
    headlines = html.select('#articleBodyContents')
    for headline in headlines:
        print(headline)
    return