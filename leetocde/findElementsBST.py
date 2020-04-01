class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class FindElements:

    def __init__(self, root):
        """
        https://leetcode.com/problems/find-elements-in-a-contaminated-binary-tree/
        """
        if root.val == None:
            return None
        root.val = 0
        node = [root]
        elements = []
        while node:
            val = node.pop()
            elements.append(val.val)
            if(val.left!=None):
                val.left.val = val.val *2 +1
                node.append(val.left)
            if(val.right!=None):
                val.right.val = val.val*2 + 2
                node.append(val.right)

        self.elements = elements

    def find(self,target):
        if(target in self.elements):
            return True
        else:
            return False

a = TreeNode(-1)
a.left = TreeNode(-1)
a.right = TreeNode(-1)

b= FindElements(a)
print(b.elements)
