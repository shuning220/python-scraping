from urllib.request import urlopen
from bs4 import BeautifulSoup

html=urlopen('https://book.douban.com/subject/3159865/')
bsObj=BeautifulSoup(html)

for child in bsObj.find('div',{'id':'db-tags-section'}).children:
    print(child)