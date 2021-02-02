
import requests
from bs4 import BeautifulSoup
def get_list(headline):
    li_list = []
    url_format = headline
    re = requests.get(url_format,headers={'User-Agent':'Mozilla/5.0'})
    html= BeautifulSoup(re.text,'html.parser')
    articles = html.select('.type06_headline > li')
    for article in articles:
        li_list.append(article.select_one("a").attrs['href'])
    print(li_list)
    return li_list

def set_list(sart):
    url_format = sart.headline
    re = requests.get(url_format,headers={'User-Agent':'Mozilla/5.0'})
    html= BeautifulSoup(re.text,'html.parser')
    articles = html.select('.type06_headline > li')
    for article in articles:
        sart.li_link.append(article.select_one("a").attrs['href'])
    return