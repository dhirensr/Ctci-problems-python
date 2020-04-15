class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

moves = 0
def helper(root):
    global moves
    if root is None:
        return 0
    left = helper(root.left)
    right = helper(root.right)
    moves += abs(left) + abs(right)
    return root.val + left + right -1

a = TreeNode(3)
a.left  = TreeNode(0)
a.right  = TreeNode(0)

helper(a)
print(moves)
