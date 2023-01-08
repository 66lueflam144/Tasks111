import re
import os

import requests
from bs4 import BeautifulSoup
from urllib.request import urlopen
from PIL import Image
from io import BytesIO

url1="https://itawenya.cn/"

rep=requests.get(url1)
html=rep.text
print(html)

dir_name=re.findall('<p style="(.*?)">',html)
urls=re.findall('<img src="(.*?)" alt=".*?">',html)
print(dir_name)
print(urls)
for url in urls:
    file_name=url.split('/')[-1]
    rep=requests.get(url1)
    with open(file_name,'wb') as f:
        f.write(rep.content)
