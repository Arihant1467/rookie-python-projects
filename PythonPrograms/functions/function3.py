#here we will supply both type of arguments and keyword arguements

def ar(*key,**keyargs):
	for n in key:
		print (n,end="\t")
	print ("\n")	
	for key,val in keyargs.items():
		print (key,val)
ar(1,2,3,4,5,"hello","yes",FirstName="arihant",LastName="sai",address="Sun apartment",city="Indore")
