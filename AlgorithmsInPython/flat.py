l=list()
a=[1,2,3,4]
b=[5,7]
c=(1,2,3,)
#now we will flatten the list
l.append(a)
l.append(b)
l.append(c)
l.append(145)
l.append(74)
l.append([134,45,23])
flat=list()
for a in l:
	if isinstance(a,(list,tuple)):
		for num in a:
			flat.append(num)
	elif isinstance(a,int):
		flat.append(a)				
print(flat)		