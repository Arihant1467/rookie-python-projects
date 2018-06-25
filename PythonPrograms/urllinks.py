import urllib.request
from bs4 import BeautifulSoup
html_doc=urllib.request.urlopen("http://python-data.dr-chuck.net/comments_353058.html").read()
soup=BeautifulSoup(html_doc,"html.parser")
tags=soup("span")
num=list()
for tag in tags:
    num.append(int(tag.contents[0]))
print (sum(num))    