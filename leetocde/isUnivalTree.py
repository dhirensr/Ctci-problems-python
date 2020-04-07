class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


def helper(root):
    if root.left == None and root.right == None:
        return True
    l,r = True, True
    if root.left:
        l = root.left.val == root.val and helper(root.left)
    if root.right:
        r = root.right.val == root.val and helper(root.right)

def isUnivalTree(root):
    return helper(root)


a = TreeNode(1)

a.left = TreeNode(1)
a.right = TreeNode(2)
a.left.left = TreeNode(1)

print(isUnivalTree(a))
