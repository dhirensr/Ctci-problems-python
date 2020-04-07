class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


def helper(sorted_vals,l,h):
    if(h<l):
        return None
    mid = int((l+h)//2)
    root = TreeNode(sorted_vals[mid])
    root.left = helper(sorted_vals,l,mid-1)
    root.right = helper(sorted_vals,mid+1,h)
    return root


def sortedListToBST(head):
    """
    https://leetcode.com/problems/convert-sorted-list-to-binary-search-tree/
    """
    sorted_vals = []
    while(head):
        sorted_vals.append(head.val)
        head = head.next
    root = helper(sorted_vals,0,len(sorted_vals)-1)




a= ListNode(1)
a.next= ListNode(2)
a.next.next= ListNode(3)
a.next.next.next= ListNode(4)
a.next.next.next.next = ListNode(5)
sortedListToBST(a)
