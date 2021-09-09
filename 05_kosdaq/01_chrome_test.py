print("test")

from urllib.request import urlopen
from bs4 import BeautifulSoup

## 01 우리가 가져올 URL
## 02 내가 원하는 정보의 위치(span, id)
## url : https://finance.naver.com/sise/
## tag : span, id : KOSPI_now

## html 코드를 요청해서 가져온다.
url = "https://finance.naver.com/sise/"
page = urlopen(url)
print(page)


## 구체적인 HTML을 확인하고,구조화 (좀 더 쉽게 정보를 가지고 오기 위해서)
soup = BeautifulSoup(page, 'html.parser')
KOSPI = soup.find("span", id="KOSPI_now")
KOSDAQ = soup.find("span", id="KOSDAQ_now")
KPI200 = soup.find("span", id="KPI200_now")
print("코스피 현재 지수는 :" ,KOSPI.text)
print("코스닥 현재 지수는 :" ,KOSDAQ.text)
print("코스피 200의 현재 지수는 :" ,KPI200.text)