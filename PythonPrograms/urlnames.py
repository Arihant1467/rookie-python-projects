import urllib.request
from bs4 import BeautifulSoup
count=int(input("Enter count: ")) #17 refers to 18 link of the list
position=int(input("Enter position: ")) # refers to how many times loop will execute
position=position-1
link=input("Enter URL:-")
link=link.strip()
print ("Retrieving -",link)
html_doc=urllib.request.urlopen(link)
html_str=""
for line in html_doc:
    html_str=html_str+str(line)
soup=BeautifulSoup(html_str,"html.parser")
tags=soup('a')
for i in range(count):
    link=tags[position]['href']
    print ("Retrieving -",link)
    html_doc=urllib.request.urlopen(link)
    html_str=""
    for line in html_doc:
        html_str=html_str+str(line)
    soup=BeautifulSoup(html_str,"html.parser")
    tags=soup("a")

     
