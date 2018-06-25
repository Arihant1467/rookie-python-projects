def connected(p,q,alist): 
    if root(p,alist)==root(q,alist):
        return True
    else:
        return False
# this functions check whether they are connected
def root(n,alist):
    while n!=alist[n]: 
          n=alist[n]
    return n
# this find the root of the node
def union(p,q,alist):
    alist[p]=root(q,alist)
    return True 
# it unions the nodes
num=int(input("Enter the no of objects: "))
i=0
list=[]
for i in range(num):
    list.append(i)
uElements=int(input("Enter the number of union elements: "))
i=0
for i in range(uElements):
    p=int(input("Enter element-1:"))
    q=int(input("Enter element-2:"))
    s=union(p,q,list)
    
while True:    
    choice=input("Enter Y/N")
    if choice=="N":
        break
    print ("Enter two numbers to check whether they are connected: ")
    p=int(input("Enter ele-1: "))
    q=int(input("Enter ele-2: "))
    if connected(p,q,list) :
        print ("Yes they are connected")
    else:
        print ("They are not connected")
print ("The list is :")
print (list)
def connected(p,q,alist):
    if root(p,alist)==root(q,alist):
        return True
    else:
        return False
def root(n,alist):
    while n!=alist[n]: 
          n=alist[n]
    return n
def union(p,q,alist):
    alist[p]=root(q,alist)
    

    
