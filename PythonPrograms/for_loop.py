fruits=['banana','apple','python','mango']
x=len(fruits)
print ("The length of fruits array is:",x)
i=0
while i<x:
    print("The fruits at index :",i+1," is ",fruits[i])
    i=i+1;
print ("The end of while loop")  
print ("Now we will start looping with for loop")
i=0
for i in range(0,x):
    print("The fruits at index :",i+1," is ",fruits[i])
print ("The end of for loop")    