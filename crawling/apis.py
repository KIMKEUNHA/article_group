import requests
from bs4 import BeautifulSoup

# 네이버 헤드라인에 있는 링크들을 가져오는 기능구현 가져온 링크를 리스트에 append함
def get_headline(num,link):
    url_format = 'https://news.naver.com/main/main.nhn?mode=LSD&mid=shm&sid1='+num
    re = requests.get(url_format,headers={'User-Agent':'Mozilla/5.0'})
    html= BeautifulSoup(re.text,'html.parser')
    headlines = html.select('.cluster_head_more')
    for headline in headlines:
        link.append("https://news.naver.com"+headline.attrs['href'])
    return

def set_list(sart):
    url_format = sart.headline
    re = requests.get(url_format,headers={'User-Agent':'Mozilla/5.0'})
    html= BeautifulSoup(re.text,'html.parser')
    articles = html.select('.type06_headline > li')
    for article in articles:
        sart.li_link.append(article.select_one("a").attrs['href'])
    return

def set_body(sart):
    for link in sart.li_link:
        url_format = link
        re = requests.get(url_format,headers={'User-Agent':'Mozilla/5.0'})
        html= BeautifulSoup(re.text,'html.parser')
        body = html.select_one('#articleBodyContents')
        sart.li_body.append(body)
    return