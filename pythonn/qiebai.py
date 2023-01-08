import requests
from bs4 import BeautifulSoup

f=open("yu.txt",'w',encoding='utf-8')
url='https://itawenya.cn/'
r=requests.get(url).text
soup=BeautifulSoup(r,"html.parser",from_encoding="utf-8")
ps=soup.find_all('p')
# print(ps)
for i in ps:
    print(i.text)
    f.write(i.text)
    

