largest = None
smallest = None
list=[]
def large_num(alist):
    alist.sort()
    return alist[len(alist)-1]
def small_num(alist):
    alist.sort()
    return alist[0]
while True:
    num = input("Enter a number: ")
    if num == "done": 
        break
    try:
        num=float(num)
        list.append(num)
    except:
        print ("Invalid number")
largest=large_num(list)
smallest=small_num(list)
print ("Maximum is ",largest)
print ("Minimum is ",smallest)