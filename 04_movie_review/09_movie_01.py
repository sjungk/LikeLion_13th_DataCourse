from bs4 import BeautifulSoup
from urllib.request import urlopen

# 웹 페이지 소스 가져오기 및 파싱
url = "https://movie.naver.com/movie/running/current.naver"
page = urlopen(url)
soup = BeautifulSoup(page, 'lxml')

print(soup.title)

## 상영작 / 예정작 제목만 뽑기
soup_ul_li = soup.find("ul", class_="lst_detail_t1").find_all("li")
print( len(soup_ul_li) )
print( soup_ul_li[122].find("dt", class_="tit").a.text )
## 중간중간 확인하는 습관 꼭 들이기!!
## 내가 보고 있는 데이터가 정확한지 정확하지 않은지 확인 작업도 꼭 해주어야 한다.

##평점
print(soup_ul_li[4].find("span", class_="num").text)

## 참여 명수 확인
print( soup_ul_li[122].find("em").text )

## 예매율
tmp = soup_ul_li[122].find("dl", class_="info_exp")
if tmp is not None:
    t = tmp.span.text
    print("값이 있음", t)
else:
    t = 0
    print("값이 없음", t)

# 개요
text = soup_ul_li[5].find("span", class_="link_txt").text
text_last = text.replace("\n", "") # 한 줄 바꾸기
text_last = text_last.replace("\t", "") # 탭 치는 거
text_last = text_last.replace("\r", "") #맨 끝으로 보내는 거
print( text_last )

## 제목, 평점, 참여 관객수, 개요
all_title = []
all_score = []
all_people = []
all_category = []
all_rate = []


for one in soup_ul_li:
    title = one.find("dt", class_="tit").a.text
    score = one.find("span", class_="num").text
    num_people = one.find("em").text

    #예매율
    tmp = one.find("dl", class_="info_exp")
    if tmp is not None:
        rate = tmp.span.text
    else:
        rate = 0

    category = one.find("span", class_="link_txt").text
    text_last = text.replace("\n", "")  # 한 줄 바꾸기
    text_last = text_last.replace("\t", "")  # 탭 치는 거
    text_last = text_last.replace("\r", "")  # 맨 끝으로 보내는 거

    all_title.append(title)
    all_score.append(score)
    all_people.append(num_people)
    all_category.append(category)
    all_rate.append(rate)

print(len(all_title), len(all_score), len(all_people),
      len(all_category), len(all_rate) )

## 저장을 위한 csv, xlsx파일 만들기
import pandas as pd

dat_dict = {
    "제목":all_title, "평점":all_score, "참여명수":all_people,
    "예매율":all_rate, "개요":all_category }
dat = pd.DataFrame(dat_dict)
dat.to_csv("네이버 영화.csv", index=False)
dat.to_excel("네이버 영화.xlsx", index=False)