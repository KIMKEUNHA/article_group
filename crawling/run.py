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
# 헤드라인 링크로 묶음기사 객체 초기화 및 생성
idx = 0
for link in links:
    sarticles.append(sarticle(link))

# 각 객체에 있는 헤드라인 링크에서 뉴스 리스트 초기화
print(str(len(sarticles)) + "개의 헤드라인 기사 등록 완료")
idx = 0
for sarticle in sarticles:
    set_list(sarticle)
    set_body(sarticle)
    set_sum(sarticle)
    idx +=1
    print(str(idx)+"/"+str(len(sarticles))+"개의 기사 완료")
print_sarticle(sarticles)


