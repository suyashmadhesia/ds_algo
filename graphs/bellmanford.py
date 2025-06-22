'''#Bellman Ford Algorithm-- Shortest path algorithm with -ve weighted edge
#  mix of dijkastra and kruskal
#1 edge list
#2 array to kee track the distance(weighted currCost) initially all set infinite
#3 parent array to generate cost path
#  -all set to -1 assume start from node 0 having no parent and currCost=0
#4 Relax all the edges v-1 times (v=no of vertices) -looping
#4-1 vertex wt is not infinite
#4-2 cost of curr vertex + cost to adj vertex is smaller than current cost of adj,d[u]+d[uv]<d[v]
#4-3 if we see any step where none of the vetex gets new shortest path 
#    -then definetly we won't have any -ve edge cycle  (break out of loop)
#5 else we relax once more and see if we have any new shortest path

#Each round of relaxation, we iteratve ALL the edges and do the relaxation based on the prices we got from previous round.
# In the k-th round of relaxation, we could find the min prices for cities whose path from source is no more than k edges.
# Therefore, we do k+1 round relaxations, instead of the traditional V-1 rounds.'''

class Edge: 
    def __init__(self,src,dest,weight):
        self.src=src
        self.dest=dest
        self.wt=weight

class Graph:
    def __init__(self,size):
        self.size=size  
        self.edge_list=[] 
        #no need of adj_list in bellman ford

    def addEdge(self,src,dest,weight):
        self.edge_list.append(Edge(src,dest,weight))


def bellmanFord(graph):

    vtxCount = graph.size  #no of vertices
    
    currCost = [float('inf') for i in range(vtxCount)]
    currCost[0] = 0 #source
    
    # parent=[None for i in range(vtxCount)]
    # parent[0] = -1  
    
    for i in range(vtxCount-1):         #v-1 relaxations
        updated = False                 # to check for atleast one edge is relaxed
        for edge in graph.edge_list:    #relax all the edges
            u ,v ,wt = edge.src ,edge.dest ,edge.wt
            if currCost[u]!=float('inf') and (currCost[u] + wt) < currCost[v] :
                currCost[v] = currCost[u] + wt
                # parent[v] = u
                updated = True
        if not updated:
            break

    #check by repeating once more if we have a -ve edge cycle or not
    for edge in graph.edge_list:
            u ,v ,wt = edge.src ,edge.dest ,edge.wt
            if currCost[u]!=float('inf') and (currCost[u] + wt) < currCost[v] :
                print('Graph has -Ve edge cycle')
                return
    
    # # Print shortest path
    # for j in range(1,len(parent)):
    #     print(f'{parent[j]}-->{j}  cost to reach : {currCost[j]}')

# Create a graph given in the above diagram
g = Graph(5)
g.addEdge(0, 1,6)
g.addEdge(0, 2,7)
g.addEdge(1,3,-4)
g.addEdge(1,4,5)
g.addEdge(1,2,8)
g.addEdge(2,3,9)
g.addEdge(2,4,-3)
g.addEdge(3,4,7)
g.addEdge(3,0,2)
g.addEdge(4,1,-2)

bellmanFord(g)

