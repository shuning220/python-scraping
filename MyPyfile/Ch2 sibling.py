from urllib.request import urlopen
from bs4 import BeautifulSoup

html=urlopen('https://book.douban.com/subject/3159865/')
bsObj=BeautifulSoup(html)

for sibling in bsObj.find('div',{'id':'db-tags-section'}).next_siblings:
    print(sibling)

#previous_sibling(s)
