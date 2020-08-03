from collections import defaultdict
class Graph:
    def __init__(self):
        self.graph = defaultdict(list)
    def addEdge(self, u, v):
        self.graph[u].append(v)


    def route_between_nodes(self,graph,node1,node2):
        print(graph.graph)

        visited = [False for i in range(len(list(graph.graph.keys())))]
        queue = [node1]
        while queue:
            val = queue.pop(0)
            if graph.graph[val]:
                for i in graph.graph[val]:
                    if(visited[i]== False):
                        if(i == node2):
                            return True
                        else:
                            visited[val] = True
                            queue.append(i)
        return False

g = Graph()
g.addEdge(0, 1)
g.addEdge(0, 2)
g.addEdge(1, 0)
g.addEdge(2, 0)
#g.addEdge(2, 3)
g.addEdge(3, 3)
print(g.route_between_nodes(g,0,3))
