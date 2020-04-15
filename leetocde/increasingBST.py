class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

vals= []
def traverse(root):
    if root:
        vals.append(root.val)
    if root.left:
        traverse(root.left)
    if root.right:
        traverse(root.right)

def increasingBST(root):
    """
    https://leetcode.com/problems/increasing-order-search-tree/
    """
    traverse(root)
    vals.sort()
    root = TreeNode(vals[0])
    for i in vals[1:]:
        temp = TreeNode(i)
        root.right = temp
        root = temp
    return root

a = TreeNode(5)
a.left = TreeNode(3)
a.right = TreeNode(6)
