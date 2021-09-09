from bs4 import BeautifulSoup
from urllib.request import urlopen

url = "https://movie.naver.com/movie/point/af/list.naver?st=mcode&sword=171725&target=after"
page = urlopen(url)
soup = BeautifulSoup(page, 'html.parser')
print(soup.title)

# 댓글 가져오기
c_all = soup.find_all("td", class_="title")
#print(len(c_all))
#print(c_all[2])
dat = list(c_all[2].children)
#dat_comment = dat[6].replace("\n", "")
#dat_comment = dat_comment.replace("\t", "")
dat_comment = dat[6].strip()
print(len(dat))
print(dat_comment)

## 한 페이지의 댓글을 가져오기
url1 = "https://movie.naver.com/movie/point/af/list.naver?st=mcode&sword=171725&target=after"
page = urlopen(url1)
soup = BeautifulSoup(page, 'html.parser')
comment_all = soup.find_all('td', class_="title")
print(len(comment_all))


comments = []
for one in comment_all:
    temp = list(one.children)[6].strip()
    #print(temp)
    comments.append(temp)

print(comments)

import pandas as pd
dict_dat = { "영화댓글":comments }
dat = pd.DataFrame(dict_dat)
dat.to_csv("댓글.csv", index=False)
dat.to_excel("댓글.xlsx", index=False)


## 1페이지부터 5페이지까지 가지고 와보기
basic_url = "https://movie.naver.com/movie/point/af/list.naver?st=mcode&sword=171725&target=after&page="

for i in range(1,6,1):
    real_url = basic_url + str(i)
    page = urlopen(url1)
    soup = BeautifulSoup(page, 'html.parser')
    comment_all = soup.find_all('td', class_="title")
    print(len(comment_all))

    comments = []
    for one in comment_all:
        temp = list(one.children)[6].strip()
        # print(temp)
        comments.append(temp)

    print(comments)