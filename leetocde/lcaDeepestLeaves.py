class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

def helper(root):
    if not root:
        return root,0
    l,l_depth= helper(root.left)
    r,r_depth = helper(root.right)
    if(l_depth==r_depth):
        return root,l_depth+1
    elif(l_depth > r_depth):
        return l,l_depth+1
    else:
        return r,r_depth+1


def lcaDeepestLeaves(root):
    """
    https://leetcode.com/problems/lowest-common-ancestor-of-deepest-leaves/
    """
    node,depth= helper(root)
    return node

a= TreeNode(1)
a.left = TreeNode(2)
a.right = TreeNode(3)
lcaDeepestLeaves(a)
