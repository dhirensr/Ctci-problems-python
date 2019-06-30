class Node:
    def __init__(self,data):
        self.next=None
        self.data=data


class LinkedList:
    def __init__(self):
        self.head=None

    def traverse(self):
        data=[]
        temp=self.head
        while(temp):
            data.append(temp.data)
            temp=temp.next
        return data
first=Node(1)
second=Node(2)
third=Node(3)
singly_linked_list=LinkedList()

singly_linked_list.head=first
first.next=second
second.next=third
print(singly_linked_list.traverse())
