from collections import defaultdict
class Graph:
    def __init__(self):
        self.graph = defaultdict(list)
    def addEdge(self, u, v):
        self.graph[u].append(v)


    def route_between_nodes(self,graph,node1,node2):

        visited = [False for i in range(len(list(graph.graph.keys())))]
        queue = [node1]
        counter = False
        while queue:
            if(counter == True):
                break
            val = queue.pop()
            for i in graph.graph[val]:
                if(visited[i]== False):
                    if(i == node2):
                        counter = True
                    else:
                        visited[val] = True
                        queue.append(i)
        if(counter== True):
            print('Yes')
        else:
            print('No')

g = Graph()
g.addEdge(0, 1)
g.addEdge(0, 2)
g.addEdge(1, 2)
g.addEdge(2, 0)
g.addEdge(2, 3)
g.addEdge(3, 3)
g.route_between_nodes(g,3,3)
