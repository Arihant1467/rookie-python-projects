sad="The streak is broken!"
happy="The streak lives still in our heart!"
#fh=open("rip.txt","w")
t=int(input(""))
for i in range(t):
    num=input("")
    l=len(num)
    val21=False
    mod21=False
    for j in range(l-1):
        if num[j]=='2'and num[j+1]=='1':
            val21=True
            break
    num=int(num)
    mod21=not bool(num%21)
    if mod21 or val21:
        print (sad)
    else:
        print (happy)
                    