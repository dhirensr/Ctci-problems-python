def possibleBipartition(N,dislikes):
    if not dislikes or N==1:
        return True
    adjacency_graph={}
    color = [0 for i in range(N+1)]
    for i in range(N+1):
        adjacency_graph[i] = []

    for u,v in dislikes:
        adjacency_graph[u].append(v)
        adjacency_graph[v].append(u)

    queue = []
    for i in range(1,N+1):
        if color[i] == 0:
            queue.append(i)
            color[i] = 1
            while queue:
                top = queue.pop()
                for j in adjacency_graph[top]:
                    if color[j] == color[top]:
                        return False
                    if color[j] == 0:
                        color[j] = -color[top]
                        queue.append(j)
    return True

print(possibleBipartition(10,
[[4,7],[4,8],[5,6],[1,6],[3,7],[2,5],[5,8],[1,2],[4,9],[6,10],[8,10],[3,6],[2,10],[9,10],[3,9],[2,3],[1,9],[4,6],[5,7],[3,8],[1,8],[1,7],[2,4]]))
