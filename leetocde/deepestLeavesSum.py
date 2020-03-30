class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


def deepestLeavesSum(root):
    """
    https://leetcode.com/problems/deepest-leaves-sum/
    """
    queue = [root]
    value = 0
    while queue:
        counter = False
        next_nodes = []
        for i in queue:
            val = i
            if (val.left!=None):
                counter = True
                next_nodes.append(val.left)
            if (val.right!=None):
                counter =True
                next_nodes.append(val.right)
        if counter == False:
            for i in queue:
                value+= i.val

        queue= next_nodes
    return value


a = TreeNode(1)
a.left = TreeNode(7)
a.right = TreeNode(0)
a.left.left = TreeNode(7)
a.left.right = TreeNode(8)
print(deepestLeavesSum(a))
