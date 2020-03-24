def sumEvenGrandparent(root):
    """
    https://leetcode.com/problems/sum-of-nodes-with-even-valued-grandparent/
    """
    def dfs(node, grandparent, parent):
            s = 0
            if node is None:
                return 0
            if grandparent is not None and grandparent % 2 == 0:
                s += node.val
            s += dfs(node.left, parent, node.val)
            s += dfs(node.right, parent, node.val)
            return s

    return dfs(root, None, None)
