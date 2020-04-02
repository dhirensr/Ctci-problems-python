class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

# def helper(root):
#     counter = False
#     left_child  = root.left
#     right_child= root.right
#     if(root):
#         if(root.val!=1):
#             if(right_child and left_child):
#                 if(right_child.val!=1 and left_child.val!=1):
#                     counter = True
#             else:
#                 if(left_child and left_child.val!=1):
#                     counter = True
#                 if(right_child and right_child.val!=1):
#                     counter = True
#                 if(left_child==None and right_child==None):
#                     counter = True
#     if(counter == True):
#         root = None

#     if(left_child):
#         helper(left_child)
#     if(right_child):
#         helper(right_child)
#     return root

def pruneTree(root):
    """
    https://leetcode.com/problems/binary-tree-pruning/
    """
    if root:
        root.left = self.pruneTree(root.left)
        root.right = self.pruneTree(root.right)
        if not root.val and not root.left and not root.right:
            root = None
    return root


tree = TreeNode(1)
tree.left = TreeNode(0)
tree.left.left = TreeNode(0)
tree.left.right = TreeNode(0)
tree.right = TreeNode(0)
tree.right.left = TreeNode(0)
tree.right.right = TreeNode(1)

pruneTree(tree)
