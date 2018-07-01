from urllib.request import urlopen
from bs4 import BeautifulSoup

html=urlopen('https://book.douban.com/subject/3159865/')
bsObj=BeautifulSoup(html)

nameList=bsObj.findAll('span',{"class":'pl'})
for name in nameList:
    print(name.get_text())

headList=bsObj.findAll('h1')
for head in headList:
    print(head.get_text())