class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def mergeTwoLists(l1,l2):
    head = ListNode(-1)
    temp = head
    while l1 and l2:
        if l1.val <= l2.val:
            temp.next = l1
            l1 = l1.next
        else:
            temp.next =l2
            l2 = l2.next
        temp = temp.next

        temp.next = l1 or l2 # TO check if the longer list is pending
    return head.next

a = ListNode(1)
a.next = ListNode(2)
a.next.next = ListNode(3)

b = ListNode(1)
b.next = ListNode(3)
b.next.next = ListNode(4)

mergeTwoLists(a,b)
