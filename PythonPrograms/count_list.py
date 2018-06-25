#fname = raw_input("Enter file name: ")
fh = open("romeo.txt","r")
lst = []
for line in fh:
    line=line.rstrip()
    ln=line.split()
    for i in ln:
        if i not in lst:
            lst.append(i)
lst.sort()
print (lst)