def valley(p):
    length=len(p)
    decIndex,incIndex=0,0
    if length==0 or length==1:
        return False
    for i in range(length-1):
        if(p[i]==p[i+1]):
            return False
        elif(p[i]<p[i+1]):
            decIndex=i
            break
    for i in range(length-1,-1,-1):
        if(p[i]==p[i-1]):
            return False
        if(p[i]<p[i-1]):
            incIndex=i
            break
    if(p[incIndex]==p[decIndex]):
        return True
    else:
        return False

#print(valley([3,2,1,2,3]))
#print(valley([31,12,14,2,3]))
#valley([3,2,1,2,3])
print(valley([2]))
print(valley([13,12,14,14]))
print(valley([5,4,3,2,1,2]))
print(valley([17,1,2,3,4,5]))