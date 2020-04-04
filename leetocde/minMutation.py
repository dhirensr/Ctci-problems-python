def minMutation(start,end,bank):
    """
    https://leetcode.com/problems/minimum-genetic-mutation/
    """
    chars = ["A", "C", "G", "T"]
    bank = set(bank)
    def bfs():
        q = [start]
        distance = {start:0}
        while q:
            cur = q.pop(0)
            if cur == end:
                return distance[cur]
            for i in range(len(cur)):
                for j in chars:
                    nw = cur[:i] + j + cur[i+1:]
                    if nw in bank and nw not in distance:
                        distance[nw] = distance[cur] + 1
                        q.append(nw)
        return -1
    return bfs()
print(minMutation("AACCGGTT",
                  "AAACGGTA",
                  ["AACCGATT","AACCGATA","AAACGATA","AAACGGTA"]))
