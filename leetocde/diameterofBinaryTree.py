class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None



def height(node):
    if node is None:
        return 0
    return 1+max(height(node.left),height(node.right))

def diameter(root):
    if root is None:
        return 0
    l_height = height(root.left)
    r_height = height(root.right)
    l_diameter = diameter(root.left)
    r_diameter = diameter(root.right)
    return max(l_height+r_height,max(l_diameter,r_diameter))

def diameterofBinaryTree(root):
    result = diameter(root)
    print(result)
    return result

a= TreeNode(1)
a.left = TreeNode(2)
a.left.left = TreeNode(4)
a.left.right = TreeNode(5)
a.right = TreeNode(3)

diameterofBinaryTree(a)
