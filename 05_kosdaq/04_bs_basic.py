from urllib.request import urlopen
from bs4 import BeautifulSoup

url = "https://finance.naver.com/sise/"

page = urlopen(url) # 웹 URL로부터 페이지를 가져오기
print(page)

page = '''
<html>
<title>나의 홈페이지 </title>
<body>
<div>
<a href="https://www.naver.com/">naver</a>
<a href="https://www.google.com">google</a>
<img height="300" src="dog_01.jpg" width="500"/>
<p> 내가 가장 좋아하는 동물은 강아지입니다.</p>
<p> 나는 그리고 네이버 홈페이지에 자주 갑니다. </p>
<p class="p3"> 강아지 사진과 네이버 링크 </p>
<p id="p4"> 강아지 사진과 네이버 링크 </p> 
<p class="p3"> 강아지 사진과 네이버 링크222 </p>
</div>
</body>
</html>
'''

## HTML 파서의 종류
#* lxml : c로 구현된 가장 빠름.
#* html5lib : 웹 브라우저 방식으로 HTML 해석.
#* html.parser

#
soup = BeautifulSoup(page, 'lxml')
print(soup.title)

# 태그명을 뒤에 .으로 붙여주면 됨. > soup.태그명 ==> 해당되는 요소의 정보를 가져온다.
#print(soup.title) #위에서 부터 내려가다 딱 걸리는 거 하나만 가지고 옴.
#print(soup.body)
#print(soup.div)
#print(soup.img)

print(soup.a)
print(soup.a.text)
print(soup.div.p.text)

# id, class를 활용해서 정보를 가지고 올 수 있음 - 하나의 요소를 가지고 올 수 있음. (find)
# id, class를 활용해서 정보를 가지고 올 수 있음 - 모든 요소를 가지고 올 수 있음. (find_all)

#print( soup.find("p", id="p4").text ) # find는 문자열 형태로 사용됨.
#print(soup.find_all("p")) # 모든 p태그를 가져옴 / 하나를 가져오든 여러개를 가져오든 find_all을 쓰면 리스트 형태로 만들어 줌.

# find와 find_all을 사용
# naver 정보 가져오기
# 모든 a태그 가져오기

print()

a1 = soup.find("a")
print(type(a1), a1.text)

a = soup.find_all("a")
print(type(a), a[1].text)
#print(soup.find_all("a") )

print()

#print( soup.find_all("p", class_="p3")[1].text )

print( soup.find("a")[1].text )

page1 = '''
<html>
<title>나의 홈페이지</title>
<body>
<div>
    <a href="https://www.naver.com/">naver</a>
    <a href="https://www.google.com">google</a>
    <p class="p3"> [영역1] 필요없는 정보1 </p>
    <p class="p3"> [영역1] 필요없는 정보3 </p>
    <p id="p4"> [영역1] 필요없는 정보2 </p>
</div>
<div>
    <a href="https://www.naver.com/">naver</a>
    <a href="https://www.google.com">google</a>
    <p class="p3"> [영역2] 강아지 사진과 네이버 링크 </p>
    <p class="p3"> [영역2] 강아지 사진과 네이버 링크222 </p>
    <p id="p4"> [영역2] 간단한 나의 홈페이지를 만들다.</p>
</div>
</body>
</html>
'''

#