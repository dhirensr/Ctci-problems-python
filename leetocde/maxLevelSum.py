class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


def maxLevelSum(root):
    """
    https://leetcode.com/problems/maximum-level-sum-of-a-binary-tree/
    """
    queue = [root]
    value = []
    k = 1
    while queue:
        next_nodes = []
        temp_val= 0
        for i in queue:
            val = i
            if (val.left!=None):
                next_nodes.append(val.left)
            if (val.right!=None):
                next_nodes.append(val.right)
            temp_val+= val.val
        queue= next_nodes
        value.append([k,temp_val])
        k+=1
    value.sort(key=lambda x: x[1],reverse=True)
    level,val = value[0] #maximum value
    return level


a = TreeNode(1)
a.left = TreeNode(7)
a.right = TreeNode(0)
a.left.left = TreeNode(7)
a.left.right = TreeNode(-8)
print(maxLevelSum(a))
