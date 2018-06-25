nodes=int(input(""))
graph=list()
parent=list()

for i in range(nodes):
	graph.append([int(n) for n in input("").strip().split(" ")])
	parent.append(0)
def minNode(mSet,mList,n):
	#m belongs to boolean mst set
	#l belongs correponding list of node
	min=10000
	minIndex=0
	for i in range(n):
		if(min>mList[i] and not mSet[i]):
			minIndex=i
	return minIndex	
def printGraph(parent,nodes,graph):
	print ("Edge\t\t Weight")
	for i in range(1,nodes):
		print(parent[i],"-",i,"\t",graph[i][parent[i]])
mstSet=list()
for i in range(nodes):
	mstSet.append(False)	
mst=list()
mst=graph[0]
mstSet[0]=True
parent[0]=-1
for i in range(1,nodes):
	minIndex=minNode(mstSet,mst,nodes)
	mstSet[minIndex]=True
	for i in range(nodes):
		if(mst[i]>graph[minIndex][i] and mstSet[i]==False and graph[mstSet][i]):
			parent[u]=minIndex
			mst[i]=graph[minIndex][i]
printGraph(parent,nodes,graph)			