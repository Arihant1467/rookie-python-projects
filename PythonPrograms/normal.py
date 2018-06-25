t=int(input(""))
alist=input("").split(" ")
for i in range(t):
    n=int(alist[i])
    alist[i]=n
newset=set(alist)
unique=len(newset)
possiblecase=0
for i in range(t+1):
    for j in range(unique-1,t+1):
        s=len(set(alist[i:j]))
        if(s==unique):
            possiblecase=possiblecase+1
print (possiblecase)