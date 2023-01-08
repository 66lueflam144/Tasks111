import re
import os

import requests
from bs4 import BeautifulSoup
from urllib.request import urlopen
from PIL import Image
from io import BytesIO
import bs4

# url1="https://itawenya.cn/"

# rep=requests.get(url1)
# html=rep.text
# print(html)

# dir_name=re.findall('<p style="(.*?)">',html)
# urls=re.findall('<img src="(.*?)" alt=".*?">',html)
# print(dir_name)
# print(urls)
# for url in urls:
#     file_name=url.split('/')[-1]
#     rep=requests.get(url1)
#     with open(file_name,'wb') as f:
#         f.write(rep.content)

# https://itawenya.cn/img/geek.png

rep=requests.get('https://itawenya.cn/')
rep.encoding='utf-8'
bs=bs4.BeautifulSoup(rep.text,"html.parser")
obj=bs.find_all("a",{"class":{"TypeBigPics"}})
objhtml=[]
objimg=[]
for s in obj:
    objhtml.append(s.find("img"))
for o in objhtml:
    objimg.append(o.get("src"))
for img in objimg:
    with open("D:\GitHub\blueflame\Tasks111\pythonn\shitofspider\imgs"+os.path.basename(img),'wb') as f:
        f.write(requests.get(img).content)
    print('done')
