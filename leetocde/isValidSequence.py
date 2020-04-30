class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

vals=[]
def helper(root,arr,index):
    if root.val !=arr[index]:
        return
    if root.left:
        if root.left.val == arr[index+1]:
            helper(root.left,arr,index+1)
    if root.right:
        if root.right.val == arr[index+1]:
            helper(root.right,arr,index+1)
    if index==len(arr)-1:
        if root.left ==None and root.right==None:
            vals.append(True)
            return
        else:
            return

def isValidSequence(root,arr):
    helper(root,arr,0)
    if True in vals:
        return True
    else:
        return False

root=TreeNode(0)
root.left = TreeNode(1)
root.right= TreeNode(0)
root.left.left = TreeNode(0)
root.left.left.right = TreeNode(1)
root.right.left= TreeNode(0)
print(isValidSequence(root,[0,1,0,1]))
