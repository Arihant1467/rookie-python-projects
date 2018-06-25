# import Stack
# Stack stack
stack=list()
s=input("Enter String:- ")
inputS=['[','{','(']
outputS=[']',')','}']
try:	
	for char in s:
		if char in inputS:
			stack.append(char)
		if char in outputS:
			stack.pop()
except IndexError:
	print("error")

if len(stack)==0:
	print ("It is a perfect string")
else:
	print ("You are crooked peice of shit")				
