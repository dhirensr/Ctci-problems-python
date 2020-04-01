result = []
def helper(graph,node,val):
    last_node = node[-1]
    if(val in graph[last_node]):
        node.append(val)
        result.append(node)

    for i in graph[last_node]:
        temp = node.copy()
        #temp.pop()
        temp.append(i)
        helper(graph,temp,val)

def allPathsSourceTarget(graph):
    """
    https://leetcode.com/problems/all-paths-from-source-to-target/
    """
    last_node = len(graph)-1
    temp = list()
    temp.append(0)
    helper(graph,temp,last_node)
    temp_result = [list(set(i)) for i in result]
    final_result = []
    for j in temp_result:
        j.sort()
        final_result.append(j)
    return final_result

print(allPathsSourceTarget([[4,3,1],[3,2,4],[3],[4],[]]))
