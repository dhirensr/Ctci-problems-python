class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def levelOrderBottom(root):
    if not root:
        return []
    queue= [[root]]
    output= []
    while queue:
        nodes = queue.pop()
        if not nodes:
            break
        temp_outputs= []
        temp  = []
        for i in nodes:
            temp_outputs.append(i.val)
            if i.left!=None:
                temp.append(i.left)
            if i.right!=None:
                temp.append(i.right)
        queue.append(temp)
        #print(temp_outputs)
        output.append(temp_outputs)
    print(output)


a = TreeNode(3)
a.left = TreeNode(9)
a.right = TreeNode(20)
a.right.left = TreeNode(15)
a.right.right=  TreeNode(7)

levelOrderBottom(a)
