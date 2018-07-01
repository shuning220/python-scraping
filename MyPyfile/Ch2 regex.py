#email address
#[A-Za-z0-9\._+]+@[A-Za-z]+\.(com|org|net|edu)

from urllib.request import urlopen
from bs4 import BeautifulSoup
import re

html=urlopen('https://book.douban.com/subject/3159865/')
bsObj=BeautifulSoup(html,'html.parser')
images=bsObj.findAll('img',{'src':re.compile(
    'https\:\/\/img3\.doubanio\.com\/f\/shire\/[A-Za-z0-9]*\/pics\/rating\_icons\/star\_hollow\_hover\.png')})
for image in images:
    print(image['src'])

