t=int(input(""))
for i in range(t):
    data=input("").split(" ")
    n,k=int(data[0]),int(data[1])
    friends=list(map(lambda x: int(x),input("").split(" ")))
    deletedCount=0
    while(deletedCount<k):
        deletedFriend=False
        for l in range(len(friends)-1):
            if friends[l]<friends[l+1]:
                friends.pop(l)
                deletedFriend=True
                break
        if not deletedFriend:
                friends.pop()
        deletedCount=deletedCount+1
    for friend in friends:
        print(friend,end=" ")
    print()    
