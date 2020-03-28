class Node:
    def __init__(self,val):
        self.val = val
        self.left = None
        self.right = None

def list_of_depths(root):
    q = []
    result = []
    q.append([root])
    #print(q)
    while q :
        temp = []
        temp2 = []
        vals = q.pop()

        for val in vals:
            if(val.left!=None):
                temp2.append(val.left)
                temp.append(val.left.val)
            if(val.right!=None):
                temp2.append(val.right)
                temp.append(val.right.val)
        if temp2:
            q.append(temp2)
        result.append(temp)
    return result




a = Node(1)
a.left = Node(2)
a.right = Node(3)
a.left.left = Node(4)
a.right.right = Node(5)

print(list_of_depths(a))
