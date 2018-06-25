a,b=0,1
num=input("How many fibonacci numers you want? ")
num=int(num)
x=0
while x<num:
    print (a)
    a,b=b,a+b
    x=x+1
print ("The end of the series")    