class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

    def __str__(self):
        return "Node "+str(self.val)

def compareLinkedList(ll1,ll2):
    number1=""
    number2=""
    number=0
    added_number=""
    head=ListNode(0)
    p=head
    ll1_copy=ll1
    ll2_copy=ll2


    while(ll1!=None):
        number1+=str(ll1.val)
        ll1=ll1.next

    while(ll2!=None):
        number2+=str(ll2.val)
        ll2=ll2.next


    added_number=str((int(number1[::-1])+int(number2[::-1])))
    for i in added_number:
        p.next=ListNode(int(i))
        p=p.next

    while(head!=None):
        head=head.next
    return head


if __name__ == "__main__":
    l1 = ListNode(2)
    l1.next = ListNode(4)
    l1.next.next = ListNode(3)
    l2 = ListNode(5)
    l2.next = ListNode(6)
    l2.next.next = ListNode(4)
    lsum = ListNode(7)
    lsum.next = ListNode(0)
    lsum.next.next = ListNode(8)
    compareLinkedList(l1, l2)
