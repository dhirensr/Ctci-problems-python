class Node:
    def __init__(self,val):
        self.val = val
        self.left = None
        self.right = None


mini = -4294967296
maxi = 4294967296
def check_bst(node,mini,maxi):
    if node is None:
        return True

    if node.val < mini or node.val > maxi:
        return False
    return (check_bst(node.left,mini,node.val-1) and
            check_bst(node.right,node.val+1,maxi))

def validate_bst(tree):
    print(check_bst(tree,mini,maxi))


tree = Node(8)
tree.left = Node(4)
tree.right = Node(10)
tree.left.left = Node(2)
tree.left.right = Node(12)
tree.right.right = Node(20)
validate_bst(tree)
