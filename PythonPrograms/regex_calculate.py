import re
fh=open("regex_sum_new.txt")
s=list()
regexp="([0-9]+)"
for line in fh:
    line=line.rstrip()
    y=re.findall(regexp,line)
    if len(y)>0:
        s.extend(y)
list_sum=0
for num in s:
    num=int(num)
    list_sum=list_sum+num
print (list_sum)
    