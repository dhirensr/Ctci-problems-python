def helper(graph,node):
    print(graph,node)

    return graph


def build_order(projects,dependencies):
    graph = {}
    for i in projects:
        graph[i] = []
    for i,j in dependencies:
        graph[j].append(i)
    #print(graph)
    result = []
    #processed = []
    while len(result)!= len(projects):
        for i in graph.keys():
            if(len(graph[i]) == 0 and i not in result):
                result.append(i)
                for j in graph.keys():
                    if(result[-1] in graph[j]):
                        graph[j].remove(result[-1])
                        #graph.pop(result[-1],None)
    return result

print(build_order([1,2,3,4,5,6],[(1,4),(6,2),(2,4),(6,1),(4,3)]))
