t=int(input(""))
g_max=0;
for i in range(t):
    sub=int(input(""))
    local_max=0
    local_max_max=0
    start=int(input(""))
    max_list=[]
    for j in range(sub-1):
        n=int(input(""))
        if(start>n):
            local_max=local_max+1            
        else:
            max_list.append(local_max)
            start=n
            str
    max_list.append(local_max)
    if(g_max<max(max_list)):
        g_max=max(max_list)
print (g_max+1)                