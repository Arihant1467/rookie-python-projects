import json
import urllib.request as req
import urllib.parse as parse
serviceUrl="http://python-data.dr-chuck.net/geojson?"
location=input("Enter location: ")
url=serviceUrl+parse.urlencode({'sensor':'false','address':location})
print ("Retrieving ",url,"......")
uh=req.urlopen(url)
data=uh.read()
print ("Retrieved",len(data),"characters")
jData=json.loads(data.decode("utf-8"))
#print (json.dumps(jData,indent=4)) 
print (jData["results"][0]["place_id"])