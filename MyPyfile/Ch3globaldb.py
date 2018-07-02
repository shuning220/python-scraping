from urllib.request import urlopen
from bs4 import BeautifulSoup
import re

pages = set()

def getLinks(pageUrl):
    global pages
    html=urlopen('https://movie.douban.com/celebrity/'+pageUrl)
    bsObj=BeautifulSoup(html,'html.parser')
    for link in bsObj.findAll('a',href=re.compile('https\:\/\/movie\.douban\.com\/celebrity\/[0-9]*\/')):
        if 'href' in link.attrs:
            if link.attrs['href'] not in pages:
                newPage = link.attrs['href']
                print(newPage)
                pages.add(newPage)
                getLinks(newPage)

getLinks("")