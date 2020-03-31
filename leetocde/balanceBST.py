class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


vals_none = []
def inorder(root):
    if root!=None:
        inorder(root.left)
        vals_none.append(root.val)
        inorder(root.right)
    return vals_none


def maketree(vals,l,r):

    if(l<=r):
        middle_index = (l+r)//2
        #print(len(vals),vals,middle_index,l,r)
        middle_element = vals[middle_index]
        root = TreeNode(middle_element)
        root.left = maketree(vals,l,middle_index-1)
        root.right = maketree(vals,middle_index+1,r)
        return root

def balanceBST(root):
    """
    https://leetcode.com/problems/balance-a-binary-search-tree/
    """
    vals = inorder(root)
    tree = maketree(vals,0,len(vals)-1)
    return tree

tree = TreeNode(2)
tree.left = TreeNode(1)
tree.right = TreeNode(3)
tree.right.right = TreeNode(4)
balanceBST(tree)
#print(tree_traversal(tree))
