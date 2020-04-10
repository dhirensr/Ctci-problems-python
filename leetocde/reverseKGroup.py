class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


def reverseKGroup(head,k):
    """
    https://leetcode.com/problems/reverse-nodes-in-k-group/
    """
    stack = []
    temp = head
    temp_node = None
    count =0
    if(k==1):
        return temp
    while head:
        stack.append(head)
        head = head.next
        if len(stack)==k:
            count += 1
            if(count == 1):
                temp = stack[-1]
            for i in range(len(stack)-1,-1,-1):
                if i==(k-1) and count!=1:
                    temp_node.next = stack[i]
                if i==0:
                    stack[i].next = head
                else:
                    temp_node = stack[i-1]
                    stack[i].next = stack[i-1]
            stack = []
    if stack:
        temp_node.next = stack[0]
    return temp


a= ListNode(1)
a.next = ListNode(2)
a.next.next = ListNode(3)
a.next.next.next = ListNode(4)
a.next.next.next.next = ListNode(5)

reverseKGroup(a,1)
