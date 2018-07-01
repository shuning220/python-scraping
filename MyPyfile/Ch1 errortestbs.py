from urllib.request import urlopen
from urllib.error import HTTPError
from bs4 import BeautifulSoup

def getTitle(url):
    try:
        html=urlopen(url)
    except HTTPError as _:
        return None
    try:
        bsObj=BeautifulSoup(html,"html.parser")
        title=bsObj.body.h1
    except AttributeError as _:
        return None
    return title
title = getTitle('http://www.doubn.com')
if title==None:
    print('Title could not be found')
else: 
    print(title)
