str1=input("")
str2=input("")
a=[0]+ [int(x) for x in str1.split()]
b=[0]+ [int(x) for x in str2.split()]
table=[[0 for c in range(len(a))] for d in range(len(b))]
for i in range(1,len(b)):
	for j in range(1,len(a)):
		if a[j]==b[i]:
			table[i][j]=table[i-1][j-1]+1
		else:
			table[i][j]=max(table[i][j-1],table[i-1][j])
curr=len(a),len(b)				