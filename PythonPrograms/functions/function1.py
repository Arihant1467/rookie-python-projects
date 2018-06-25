# this function will accept any number of arguments
# the argument which take multiple values is a tuple
def avg(num1,*rest):
	print ("The number of arguments posted are:-",1+len(rest))
	print ("The type of rest variable is ",type(rest))
avg(1,2,3,4,5,6,7,8)	