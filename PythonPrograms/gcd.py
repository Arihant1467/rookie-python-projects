def gcd(m,n):
	i=min(m,n)
	while (i>=1):
		if(m%i==0 and n%i==0):
			return i
		else:
			i=i-1
m=int(input(""))
n=int(input(""))
print(gcd(m,n))				