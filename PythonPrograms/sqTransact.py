length=int(input(""))
num=input("").strip()split(" ")
l=[]
s=0
for n in num:
    s=s+int(n)
    l.append(s)
q=int(input(""))
for j in range(q):
    query=int(input(""))
    disp=False
    for i in range(length):
        if l[i]>=query:
            print (i+1)
            disp=True
            break 
    if not disp: print ("-1")         
    