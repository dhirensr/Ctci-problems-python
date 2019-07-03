class Node:
    def __init__(self,data):
        self.next=None
        self.data=data
    def __str__(self):
        return "Node" + str(self.data)

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
fourth=Node(4)
fifth=Node(5)
singly_linked_list=LinkedList()

singly_linked_list.head=first
first.next=second
second.next=third
third.next=fourth
fourth.next=fifth

def remove_duplicates(linked_list_obj):
    temp=linked_list_obj.head
    data=[]
    while(temp):
        if temp.data not in data:
            data.append(temp.data)
            temp=temp.next
        elif(temp.next!=None):
            temp=temp.next
        else:
            temp=None
    return data

print(remove_duplicates(singly_linked_list))
