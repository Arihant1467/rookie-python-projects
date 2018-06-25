num=input("Enter the no of objects:")
num=int(num)
i=0
def list_sort(alist):
    alist[1]=0
    alist[2]=0
    alist[3]=0
    print ("The list of the function:")
    print (alist)
l=[]
for i in range(num):
    l.append(i)
list_sort(l)
print ("The list in global function:")
print (l)