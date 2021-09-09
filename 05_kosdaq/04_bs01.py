from bs4 import BeautifulSoup
from urllib.request import urlopen

page1 = '''
<html>
<title>나의 홈페이지</title>
<body>
<div>
</div>
<div>
</div>
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
soup1 = BeautifulSoup(page1, 'lxml')
#print( soup1.title )

##
one_info = soup1.find_all("div")
#print(len(one_info) )
#print(one_info[3] )

wanted_info = soup1.find_all('div')[3]
print(wanted_info)
last_info_multi = wanted_info.find_all('p', class_="p3")
print(last_info_multi)


for one in last_info_multi:
    print(one.text)

    ##

wanted_info2 = soup1.find_all('div')[2]
print(wanted_info2)
last_info_multi2 = wanted_info2.find_all('p', class_="p3")

a = []
for one in last_info_multi2:
    #print(one.text)
    a.append(one.text)

print(wanted_info2.children) #자기 자신을 빼고 밑에 친구들과 줄바꿈을 포함한 요소들이 들어가게 된다.
print(list(wanted_info2.children)[9])

# 코스피 정보 가져오기
# 거래량 장중 초과