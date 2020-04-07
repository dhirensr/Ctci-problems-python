class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

def tree_traversal(root,values):
    if root.left == None and root.right == None:
        values.append(root.val)
    else:
        if(root.left):
            tree_traversal(root.left,values)
        if(root.right):
            tree_traversal(root.right,values)
    return values

def leafSimilar(root1, root2):
    """
    https://leetcode.com/problems/leaf-similar-trees/
    """
    leaf_values_root1 = tree_traversal(root1,[])
    leaf_values_root2 = tree_traversal(root2,[])
    return leaf_values_root2 == leaf_values_root1


a = TreeNode(3)
a.left = TreeNode(5)
a.right = TreeNode(1)
a.left.left = TreeNode(6)
a.left.right = TreeNode(2)
leafSimilar(a,a)
