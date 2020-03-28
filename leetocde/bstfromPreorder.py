import queue

class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
def bstFromPreorder(preorder,inorder,start,end):
    if len(preorder)==0:
        return None
    elif (start > end):
        return None
    elif( start ==end):
        root = TreeNode(inorder[start])
        return root
    search_array = inorder[start:end]
    index= None
    #  print(start,end,action)
    for i in preorder:
        if(i in search_array):
            root = TreeNode(i)
            preorder.remove(i)
            index = inorder.index(i)
            #print(index,preorder)
            break
    if(index!=None):
        root.left = bstFromPreorder(preorder,inorder,start,index-1)
        root.right = bstFromPreorder(preorder,inorder,index+1,end)
        return root
    else:
        return None

root = bstFromPreorder([4,2],[2,4],0,1)
result = [root.val]
q = queue.Queue()
q.put(root)
while not q.empty():
    val = q.get()
    if val.left != None or val.right != None:
        if(val.left != None):
            q.put(val.left)
            result.append(val.left.val)
        else:
            result.append(None)
        if(val.right != None):
            q.put(val.right)
            result.append(val.right.val)
        else:
            result.append(None)
print(result)


def bstFromPreorder(preorder):
    inorder = sorted(preorder)
    if not preorder:
	return None
    root = TreeNode(preorder[0])
    idx = inorder.index(preorder[0])
    root.left = self.bstFromPreorder(preorder[1:idx + 1])
    root.right = self.bstFromPreorder(preorder[idx + 1:])
    return root
