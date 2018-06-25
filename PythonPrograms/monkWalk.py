vowels=['a','e','i','o','u','A','E','I','O','U']
t=int(input(""))
for i in range(t):
    count=0
    str=input("")
    for c in str:
        if c in vowels:
            count=count+1
    print (count)        
    