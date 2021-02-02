from apis import *
from sarticle import sarticle
part = ['101','102','103','104','105','106']#현재 헤드라인을 가지고 있는 분야의 num
links = []#헤드라인링크 받아오는 리스트
sarticles = []#묶음기사의 객체를 담는 리스트
set_num = 10#주제 하나에 대한 기사 최대 갯수지정
# 헤드라인 링크를 받아와 links 리스트에 담는다.
for num in part:
    get_headline(num,links)

print(str(len(links)) + "개의 링크 추출 완료")
sart = sarticle(links[0])
set_list(sart)
set_body(sart)
print(sart.li_link)
print(sart.li_body)