from bs4 import BeautifulSoup
from urllib.request import urlopen
page = '''
<html>
<title>나의 홈페이지 </title>
<body>
<div>
<a href="https://www.naver.com/">naver</a>
<a href="https://www.google.com">google</a>
<img height="300" src="dog_01.jpg" width="500"/>
<p>내가 가장 좋아하는 동물은 강아지입니다.</p>
</div>
</body>
</html>
'''

soup = BeautifulSoup(page, 'lxml')
#title 요소 정보 가져오기
print(soup.title)
# a 태그 요소 가져오기
print(soup.a)
# a 태그 요소 가져오기
print(soup.find_all("a"))