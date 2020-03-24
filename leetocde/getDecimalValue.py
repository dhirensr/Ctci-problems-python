

class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

    def getDecimalValue(head):
        """
        https://leetcode.com/problems/convert-binary-number-in-a-linked-list-to-integer/
        """
        bin_result = ''
        while head:
            bin_result += str(head.val)
            head = head.next
        return int(bin_result,2)
