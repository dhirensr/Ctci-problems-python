
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None



def delNodes(root, to_delete):
    if root == None:
        return None

    que = [root]
    output = []

    if root.val not in to_delete:
        output.append(root)

    while que:
        node = que.pop(0)

        if node.left:
            que.append(node.left)
            if node.left.val in to_delete:
                node.left = None

        if node.right:
            que.append(node.right)
            if node.right.val in to_delete:
                node.right = None

        if node.val in to_delete:
            if node.left:
                output.append(node.left)
            if node.right:
                output.append(node.right)

    return output


a= TreeNode(1)
a.left = TreeNode(2)
a.right = TreeNode(3)
a.left.left = TreeNode(4)
a.left.right = TreeNode(5)
a.right.left = TreeNode(6)
a.right.right = TreeNode(7)

delNodes(a,[3,5])
