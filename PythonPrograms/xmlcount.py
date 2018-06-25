import urllib.request as req
import xml.etree.ElementTree as ET
url=input("Enter location: ")
print ("Retrieving... ",url)
url=url.strip()
data=req.urlopen(url).read()
print ("Retrieved",len(data),"characters")
tree = ET.fromstring(data)
comments=tree.findall("comments/comment")
print ("Count: ",len(comments))
num=list()
for comment in comments:
    num.append(int(comment.find('count').text))
print ("Sum: ",sum(num))    
    