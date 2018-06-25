import json
import urllib.request as req
url=input("Enter URL: ")
print ("Retreiving",url," ....")
num=0
data=req.urlopen(url)
json_data=""
for line in data:
    json_data=json_data+str(line.strip())    
j_data=json.loads(json_data)
#comments=json_data["comments"]
#for comment in comments:
#    num=num+int(comment["count"])
#print (num)    