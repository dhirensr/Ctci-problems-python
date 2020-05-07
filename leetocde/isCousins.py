
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

visited={}
def helper_bfs(x,y,queue):
    k=1
    visited[queue[0].val]=[None,0]
    while queue:
        temp =[]
        for i in queue:
            if i.left:
                visited[i.left.val] =[i,k]
                temp.append(i.left)
            if i.right:
                visited[i.right.val] =[i,k]
                temp.append(i.right)
        k +=1
        queue = temp
    if visited[x][0]!= visited[y][0] and visited[x][1]==visited[y][1]:
        return True
    else:
        return False


def isCousins(root,x,y):
    queue=[root]
    print(helper_bfs(x,y,queue))

node=TreeNode(2,TreeNode(4),None)
root= TreeNode(1,node,TreeNode(3))
isCousins(root,4,3)
