class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

count = 0
def helper(root,L,R):
    global count
    if L <= root.val <= R:
        count += root.val
    if root.left:
        helper(root.left,L,R)
    if root.right:
        helper(root.right,L,R)
    return count

def rangeSumBST(root,L,R):
    global count
    helper(root,L,R)
    print(count)


a = TreeNode(10)
a.left = TreeNode(5)
a.right = TreeNode(15)

rangeSumBST(a,7,15)
