from urllib.request import urlopen
from bs4 import BeautifulSoup

url = "https://finance.naver.com/sise/sise_index.nhn?code=KOSDAQ"

p = urlopen(url)
soup = BeautifulSoup(p, 'lxml') #뷰티풀 숲 자료형으로 html 코드를 변경해주는 것이 lxml
print(soup.title)

all_info = []
# 코스닥 지수 가져오기
kosdaq_index = soup.find("em", id="now_value").text
print(kosdaq_index)
all_info.append(kosdaq_index)
# 거래량(천주) 가져오기
deal_info = soup.find("td", id="quant").text
print(deal_info)
all_info.append(deal_info)

# 52주 최고
week52_max1 = soup.find("table", class_="table_kos_index")
# print(week52_max) 있나 없나 정보 확인
week52_max2 = week52_max1.find_all("tr")[2]
# print(week52_max2) 있나 없나 정보 확인
week52_max3 = week52_max2.find("td", class_='td').text
print("52주 최고 : ", week52_max3)
all_info.append(week52_max3)

print(all_info)
# > 2,3 번째줄을 줄이면
#week52_max2 = week52_max1.find_all("tr")[2].find("td", class_="td").text
#print("52주 최고 : ", week52_max2)

## 파일로 만들기
## 리스트 형태가 필요함
## { key1 : [a,b,c,e] }

import pandas as pd

info_list = ['코스닥지수', '거래량(천주)', '52주최고']

dic_dict = { "구분":info_list,"코스닥 정보":all_info }
dat = pd.DataFrame(dic_dict)
dat.to_csv("코스닥정보.csv", index=False)
dat.to_excel("코스닥정보.xlsx")

