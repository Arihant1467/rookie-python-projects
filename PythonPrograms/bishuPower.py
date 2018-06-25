import sys
t=int(input(""))
power=[]
power= map(int,sys.stdin.readline().split())
q=int(input(""))
for i in range(q):
    p=int(input(""))
    low=0
    high=t-1
    while True:
        mid=int((low+high)/2)
        if(power[mid]>p):
            high=mid
            