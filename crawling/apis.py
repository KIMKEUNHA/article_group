import requests
from bs4 import BeautifulSoup
from selenium import webdriver
import time
import json
from pyvirtualdisplay import Display
# 네이버 헤드라인에 있는 링크들을 가져오는 기능구현 가져온 링크를 리스트에 append함
def get_headline(num,link):
    url_format = 'https://news.naver.com/main/main.nhn?mode=LSD&mid=shm&sid1='+num
    re = requests.get(url_format,headers={'User-Agent':'Mozilla/5.0'})
    html= BeautifulSoup(re.text,'html.parser')
    headlines = html.select('.cluster_head_more')
    for headline in headlines:
        link.append("https://news.naver.com"+headline.attrs['href'])
    return
# 각 헤드라인에 대한 기사리스트에서 링크가져옴
def set_list(sart):
    url_format = sart.headline
    re = requests.get(url_format,headers={'User-Agent':'Mozilla/5.0'})
    html= BeautifulSoup(re.text,'html.parser')
    articles = html.select('.type06_headline > li')
    for article in articles:
        sart.li_link.append(article.select_one("a").attrs['href'])
    return
# 링크에 접속하여 본문 초기화
def set_body(sart):
    for link in sart.li_link:
        url_format = link
        re = requests.get(url_format,headers={'User-Agent':'Mozilla/5.0'})
        html= BeautifulSoup(re.text,'html.parser')
        body = clean_body(html.select_one('#articleBodyContents'))
        sart.li_body.append(body)
    return
# 본문 내용 가공
def clean_body(body):
    result = ""
    for item in body.contents:
        stripped = str(item).strip()
        if stripped =="":
            continue
        if stripped[0] not in["<","/"]:
            result += str(item).strip()
    result.replace("&apos;", "")
    result = result[11:]
    return result
# 각 링크에 접속하여 요약가져옴
def set_sum(sart):
    display = Display(visible=0, size=(1920, 1080))
    display.start()
    for link in sart.li_link:
        options = webdriver.ChromeOptions()
        options.add_experimental_option('excludeSwitches', ['enable-logging'])
        driver = webdriver.Chrome(options=options, executable_path="./chromedriver")
        driver.get(link)
        try:
            driver.find_element_by_xpath('//a[@class="media_end_head_autosummary_button _toggle_btn nclicks(sum_summary)"]').click()
            time.sleep(1)
            sum = driver.find_element_by_xpath('//div[@class="_contents_body"]')
            sart.li_sum.append(clean_sum(sum.text))
            sart.li_sflag+=1
            print("요약가져오기 성공")
            if sart.li_sflag>=3:
                break
        except:
            print("요약가져오기 실패")
            pass
#요약 가공
def clean_sum(text):
    result = ""
    result = text.replace("\n\n","")
    return result
#jsonfile로 출력
def print_sarticle(sarticles):
    path = time.strftime('data_news/%y%m%d_%Hh_news.json')
    opfile = {}
    opfile["time"] = time.strftime('%y-%m-%d %H:%M:%S')
    opfile["document"] = []
    for sarticle in sarticles:
        ob = {}
        ob["head"] = sarticle.headline
        ob["body"] = sarticle.li_body
        ob["extract"] = sarticle.li_sum
        opfile["document"].append(ob)
    with open(path,"w") as output:
        json.dump(opfile,output,ensure_ascii=False,indent=4)

def test_print_sarticle(sart):
    path = time.strftime('./%y%m%d_%Hh_news.json')
    opfile = {}
    opfile["time"] = time.strftime('%y-%m-%d %H:%M:%S')
    opfile["document"] = []
    ob = {}
    ob["head"] = sart.headline
    ob["body"] = sart.li_body
    ob["extract"] = sart.li_sum
    opfile["document"].append(ob)
    with open(path,"w") as output:
        json.dump(opfile,output,ensure_ascii=False,indent=4)
