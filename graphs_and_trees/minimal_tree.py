class Node:
    def __init__(self,val):
        self.val= val
        self.left =None
        self.right = None

def minimal_tree(sorted_array,start,end):
    if(end < start):
        return None
    mid = (start+end )//2
    n = Node(sorted_array[mid])
    n.left = minimal_tree(sorted_array,start,mid-1)
    n.right = minimal_tree(sorted_array,mid+1,end)
    return n

minimal_tree([1,2,3,4,5],0,4)
