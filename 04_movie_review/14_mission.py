from bs4 import BeautifulSoup
from urllib.request import urlopen
import pandas as pd
from wordcloud import WordCloud
from matplotlib import rc

basic_url = "https://movie.naver.com/movie/point/af/list.naver?st=mcode&sword=187348&target=after&page="

comment_10 = []
for i in range(1,11,1):
    real_url = basic_url + str(i)
    page = urlopen(real_url)
    soup = BeautifulSoup(page, 'html.parser')
    comment_all = soup.find_all("td", class_="title")
    print(len(comment_all))

    for one in comment_all:
        temp = list(one.children)[6].strip()
        comment_10.append(temp)

print(len(comment_10),comment_10)

dict_dat = {"댓글":comment_10}
dat = pd.DataFrame(dict_dat)
dat.to_csv("샹치_댓글.csv", index=False)
dat.to_excel("샹치_댓글.xlsx", index=False)

f = open("샹치_댓글.csv", encoding='utf-8')
text = f.read()
print(text)
f.close()

rc('font', family="NanumGothic")

wcloud = WordCloud('./data/D2Coding.ttf',
                   max_words=1000,
                   relative_scaling=0.2).generate(text)

#print(wcloud)
import matplotlib.pyplot as plt
plt.figure(figsize=(12,12))
plt.imshow(wcloud, interpolation='bilinear')
plt.axis('off')
plt.show()