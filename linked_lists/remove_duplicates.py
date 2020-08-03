class Node:
    def __init__(self,data):
        self.next=None
        self.val=data
    def __str__(self):
        return "Node" + str(self.val)

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
fourth=Node(3)
fifth=Node(5)
singly_linked_list=LinkedList()

singly_linked_list.head=first
first.next=second
second.next=third
third.next=fourth
fourth.next=fifth

def remove_duplicates(linked_list_obj):
    node_count = {}
    while linked_list_obj:
        if linked_list_obj.val in node_count:
            node_count[linked_list_obj.val] +=1
            prev.next = linked_list_obj.next
        else:
            node_count[linked_list_obj.val] =1

        prev = linked_list_obj
        linked_list_obj = linked_list_obj.next
    return linked_list_obj


def traverse(head):
    data=[]
    temp=head
    while(temp):
        data.append(temp.val)
        temp=temp.next
    return data

# def remove_duplicates(linked_list_obj):
#     temp=linked_list_obj.head
#     data=[]
#     while(temp):
#         if temp.data not in data:
#             data.append(temp.data)
#             temp=temp.next
#         elif(temp.next!=None):
#             temp=temp.next
#         else:
#             temp=None
#     return data

ll = remove_duplicates(first)
print(traverse(first))
