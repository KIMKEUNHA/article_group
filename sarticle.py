class sarticle:
    headline = ""
    li_link = []
    li_body = []
    li_sum = []
    li_sflag = 0
    def __init__(self,headline):
        self.headline = headline
        self.li_body = []
        self.li_link = []
        self.li_sum = []
        self.li_sflag = 0
        print(headline+"주소로 객체 초기화 완료")
    def apd_link(self,link):
        self.li_link = link
        return
    def apd_body(self,body):
        self.li_body = body
        return
    def apd_sum(self,sum):
        self.li_sum = sum
        return