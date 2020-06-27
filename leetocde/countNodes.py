class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

count = 0
def helper(node):
    if not node or (node.left == None and node.right == None):
        return
    count +=1
    if node.left:
         helper(node.left,count+1)
    if node.right:
        helper(node.right,count+1)

def countNodes(root):
    helper(root)
    print(count)


a = TreeNode(1)
a.left = TreeNode(2)
a.right=  TreeNode(3)
a.right.left = TreeNode(6)
a.left.left = TreeNode(4)
a.left.right = TreeNode(5)

countNodes(a)
