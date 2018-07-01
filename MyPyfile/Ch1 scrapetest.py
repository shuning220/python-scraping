from urllib.request import urlopen
from bs4 import BeautifulSoup

html=urlopen('https://movie.douban.com/subject/1763308/')
bsObj=BeautifulSoup(html,"html.parser")
bsObj.body.h1 #alternatively: print(bsObj.h1)