from urllib.request import urlopen
from bs4 import BeautifulSoup

# url,
# tag, id, class

url = "https://finance.naver.com/sise/"
page = urlopen(url)
soup = BeautifulSoup(page, 'html.parser')
print(soup.title)

data = soup.find("ul", class_="lst_pop")
dat_all = data.find_all("a")
value_all = data.find_all("span")

for one in dat_all:
    print(one.text)

for one in value_all:
    print(one.text)
