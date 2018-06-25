from collections import deque
alist=['arsenal','chelsea','Tottenham']
alist.append('Liverpool')
#we create a double ended queue using a predined list
que=Queue()
q=deque(alist)
print ("The queue is ",q)
print ("The first element is",q.popleft())
print ("The new size is :",len(q))