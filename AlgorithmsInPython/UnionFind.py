num=int(input("Enter the no of objects:"))
i=0
list=[]
def union(p,q,alist):
    pid=alist[p]
    qid=alist[q]
    alist[q]=pid
    i=0
    for i in range(len(alist)):
        if alist[i]==qid:
            alist[i]=pid
def connected(p,q,alist):
    if alist[p]==alist[q]:
       return True
    else:return False                
for i in range(num):
    list.append(i)
uElements=int(input("Enter the number of union elements"))
i=0
for i in range(uElements):
    p=int(input("Enter element-1"))
    q=int(input("Enter element-2"))
    union(p,q,list)
print ("Enter two numbers to check whether they are connected")
p=int(input("Enter ele-1"))
q=int(input("Eneter ele-2"))
if connected(p,q,list):
    print ("Yes they are connected")
else:
    print ("No they are not connected")