def middleNode(head):
    """
    return the second middle node of linked list
    """
    vals = []
    while head:
        vals.append(head)
        head = head.next
    mid = int(len(vals)/2)
    return vals[mid]
