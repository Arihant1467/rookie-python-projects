import urllib.request
response=urllib.request.urlopen("http://data.pr4e.org/intro-short.txt")
fhand=open("info.txt","w")
fhand.write(str(response.info()))