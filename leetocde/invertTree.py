class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def helper(node):
    if not node:
        return None
    right = helper(node.right)
    left = helper(node.left)
    node.left =right
    node.right = left
    return node

def invertTree(root):
    if root:
        helper(root)
    return root

a = TreeNode(1)
a.left = TreeNode(2)
#a.right = TreeNode(7)
# a.left.left = TreeNode(1)
# a.left.right = TreeNode(3)
# a.right.left = TreeNode(3)
# a.right.right = TreeNode(1)

root1 = invertTree(a)
