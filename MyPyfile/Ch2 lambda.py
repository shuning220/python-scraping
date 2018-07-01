#email address
#[A-Za-z0-9\._+]+@[A-Za-z]+\.(com|org|net|edu)

from urllib.request import urlopen
from bs4 import BeautifulSoup
import re

#image is contained in img
html=urlopen('https://book.douban.com/subject/3159865/')
bsObj=BeautifulSoup(html,'html.parser')
x=bsObj.findAll(lambda tag: len(tag.attrs) == 3)
print(x)
