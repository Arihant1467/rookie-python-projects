num=list()
count=int(input(""))
for i in range(count):
    x=int(input(""))
    num.append(x)
p=0    
while True:
    while (p<count):
        s=0
        for j in range(0,9,3):
            if (i+j)<count:
                s=s+num[i+j]
        num.append(s)
        p=p+1
    if(len(num)-count<=3):
        break
    else:
        count=len(num)
print (num[count:])        