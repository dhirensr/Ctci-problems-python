class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

output = 0
def searchBST(root, val):
    if not root or root.val == val:
        return root
    if val > root.val:
        searchBST(root.right,val)
    elif val < root.val:
        searchBST(root.left,val)


a = TreeNode(4)
a.left = TreeNode(2)
a.right = TreeNode(7)
a.left.left = TreeNode(1)
a.left.right = TreeNode(3)
print(searchBST(a,2))
print(output)
