class Node:
    # Contructor to create a new node
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

def helper(root):
    if root is None:
        return 0
    left = helper(root.left)
    right = helper(root.right)
    max_single= max(max(left,right)+root.data,root.data)
    max_top  = max(max_single,left+right+root.data)

    helper.res = max(helper.res,max_top)
    return max_single

def maxPathSum(root):
    helper.res = float("-inf")
    helper(root)
    return helper.res



root = Node(10)
root.left = Node(2)
root.right   = Node(10)
root.left.left  = Node(20)
root.left.right = Node(1)
root.right.right = Node(-25)
root.right.right.left   = Node(3)
root.right.right.right  = Node(4)

print(maxPathSum(root))
