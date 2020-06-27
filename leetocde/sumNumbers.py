class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

output = []
def helper(node,result):
    if node:
        result+=str(node.val)
    if node and (node.left== None and node.right==None):
        output.append(int(result))
    if node and node.left:
        helper(node.left,result)
    if node and node.right:
        helper(node.right,result)

def sumNumbers(root):
    helper(root,"")
    result = 0
    for i in output:
        result +=i

    print(result)

a = TreeNode(4)
a.left = TreeNode(9)
a.right = TreeNode(0)
a.left.left = TreeNode(5)
a.left.right = TreeNode(1)

sumNumbers(a)
