class Node:
    def __init__(self, val, isLeaf, topLeft, topRight, bottomLeft, bottomRight):
        self.val = val
        self.isLeaf = isLeaf
        self.topLeft = topLeft
        self.topRight = topRight
        self.bottomLeft = bottomLeft
        self.bottomRight = bottomRight

# def helper(grid,low_x,high_x,low_y,high_y):
#     topLeft = []
#     topRight = []
#     bottomLeft = []
#     bottomRight = []
#     all_elements = []
#     temp = len(grid)//2
#     for i in range(low_x,high_x):
#         for j in range(low_y,high_y):
#             all_elements.append(grid[i][j])

#     if set(all_elements) == 1:
#         if(all_elements[0] == 1):
#             return Node(True,True,None,None,None,None,None)
#         else:
#             return Node(False,True,None,None,None,None,None)
#     if(temp==0):
#         val = True
#         isLeaf= False
#         topLeft = Node(all_elements[0]==1,True,None,None,None,None)
#         topRight =  Node(all_elements[1]==1,True,None,None,None,None)
#         bottomLeft =  Node(all_elements[2]==1,True,None,None,None,None)
#         bottomRight =  Node(all_elements[3]==1,True,None,None,None,None)
#         return Node(val,isLeaf,topLeft,topRight,bottomLeft,bottomRight)

#     val = True
#     isLeaf= False
#     topLeft = helper(grid,low_x,temp+1,low_y,temp+1)
#     topRight = helper(grid,low_x,temp+1,temp+1,high_y)
#     bottomLeft = helper(grid,temp+1,high_x,low_x,temp+1)
#     bottomRight = helper(grid,temp+1,high_x,temp+1,high_y)
#     return Node(val,isLeaf,topLeft,topRight,bottomLeft,bottomRight)

def helper2(grid):
    if not grid:
        return None
    if all([grid[0][0] == g for row in grid for g in row]):
        return Node(grid[0][0] > 0, True, None, None, None, None)
    n = len(grid) // 2
    a = construct([r[:n] for r in grid[:n]])
    b = construct([r[n:] for r in grid[:n]])
    c = construct([r[:n] for r in grid[n:]])
    d = construct([r[n:] for r in grid[n:]])
    return Node(None, False, a, b, c, d)

def construct(grid):
    if not grid:
        return None
    if all([grid[0][0] == g for row in grid for g in row]):
        return Node(grid[0][0] > 0, True, None, None, None, None)
    n = len(grid) // 2
    a = construct([r[:n] for r in grid[:n]])
    b = construct([r[n:] for r in grid[:n]])
    c = construct([r[:n] for r in grid[n:]])
    d = construct([r[n:] for r in grid[n:]])
    return Node(None, False, a, b, c, d)


print(construct([[1,1,1,1,0,0,0,0],[1,1,1,1,0,0,0,0],[1,1,1,1,1,1,1,1],[1,1,1,1,1,1,1,1],[1,1,1,1,0,0,0,0],[1,1,1,1,0,0,0,0],[1,1,1,1,0,0,0,0],[1,1,1,1,0,0,0,0]]))
