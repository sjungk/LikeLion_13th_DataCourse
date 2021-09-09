# 시황뉴스 목록을 csv 파일로 만들기
# import pandas as pd
# dat = pd.DataFrame( {"시황뉴스" :news} )
# print(dat)
# dat.to_csv("210908_14_index.csv", index=False)
# dat.to_csv("news_excel.xlsx", index=False)

# 코스닥 정보에 대한
# 지수 정보 210908_14_index.csv
# 시황정보 리포트 210908_14_news.csv
# 시황정보 리포트 210908_14_report.csv
# 인기검색어, 가장 많이 본 뉴스 20210908_14_cnt_news.csv



from urllib.request import urlopen
from bs4 import BeautifulSoup

k_index_list = ["코스닥 지수", "거래량"]
k_index = []
url = "https://finance.naver.com/sise/sise_index.nhn?code=KOSDAQ"
page = urlopen(url)
soup = BeautifulSoup(page, 'lxml')
#print(soup.title)

#코스닥 지수 정보 가져오기
kosdaq_info = soup.find("em", id="now_value")
k_index.append(kosdaq_info.text)

deal_info = soup.find('td', id='quant')
print("거래량 : ", deal_info.text)
k_index.append(deal_info.text)

# # 코스닥 지수 정보를 csv 파일로 만들기
# now_value = []

import pandas as pd
dict_dat = {"구분":k_index_list, "지수":k_index}
all_dat = pd.DataFrame(dict_dat)
print(all_dat)
all_dat.to_csv("210908_14_news.csv", index=True)
all_dat.to_excel("210908_14_news.xlsx", index=True)

# #코스닥 시황뉴스
# tmp_news = soup.find("ul", class_="sise_report")
# tmp_li_all = tmp_news.find_all("span", class_="tit")
#
# news = []
# str1 = ""
# for one in tmp_li_all:
#     news.append(one.text)
#     str1 = str1 + one.text + ","
#
# # print(news)
# print(str1)