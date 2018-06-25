# this function will accept any number of key word arguments
# this should appear as a last arguement in the function
#here the rest variable is a dict type object
#it is not neccessary that it will store elements in order
def make_element(num1,**rest):
	for key,val in rest.items():
		print ("Key=",key," Val=",val)
make_element(1,FirstName="arihant",LastName="sai",address="Sun apartment",city="Indore")