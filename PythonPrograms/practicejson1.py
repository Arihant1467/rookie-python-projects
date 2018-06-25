import json
import urllib.request as req
url=input("Enter url: ")
print ("Retrieving ",url,"......")
uh=req.urlopen(url)
data=uh.read()
print ("Retrieved",len(data),"characters")
jData=json.loads(data.decode("utf-8"))
comments=jData["comments"]
print ("Count",len(comments))
num=0
for comment in comments:
    num=num+int(comment["count"])
print (num)    