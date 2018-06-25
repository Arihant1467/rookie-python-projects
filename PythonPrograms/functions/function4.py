#here we will accept certain keyword arguements
def recv(max,*values,block=True):
	if block:
		print(values[:max])
	else:
		print (values[:len(values)])
recv(3,1,2,3,4,5,6,7,8,9,block=True)
#print (dir(recv))			
print (help(recv))			