import collections
def findCheapestPrice(n,flights,src,dst,K):
    flights_cost = {}
    for i in range(n):
        flights_cost[i] = []
    for node,neighbour,cost in flights:
        flights_cost[node].append([neighbour,cost])
    queue = collections.deque([(src,0,0)])
    minCost = float('inf')
    while queue:
        node,stops,cost = queue.popleft()
        if node == dst:
            minCost = min(minCost, cost)
        if stops > K or cost > minCost:
            continue
        for nei,nc in flights_cost[node]:
            queue.append([nei,stops+1,cost+nc])
    return minCost if minCost !=float('inf') else -1

#print(findCheapestPrice(5,[[1,2,10],[2,0,7],[1,3,8],[4,0,10],[3,4,2],[4,2,10],[0,3,3],[3,1,6],[2,4,5]],0,4,1))

#print(findCheapestPrice(3,[[0,1,100],[1,2,100],[0,2,500]],0,2,1))
print(findCheapestPrice(5,[[1,2,10],[2,0,7],[1,3,8],[4,0,10],[3,4,2],[4,2,10],[0,3,3],[3,1,6],[2,4,5]]
                        ,0
                        ,4
                        ,1))
