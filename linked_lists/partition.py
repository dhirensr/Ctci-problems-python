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
    def push(self,data):
        new_node = Node(new_data)
        new_node.next = self.head
        self.head = new_node #adding to the beginning

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

def partition(linked_list_obj,partition_value):
    ''' returns a new linked list with all values greater than partition_value'''
    temp=linked_list_obj.head
    data=[]
    new_linked_list=LinkedList()
    node_temp=None
    while(temp):
        if(temp.data > partition_value):
            previous_node=node_temp
            node_temp=Node(temp.data)
            if(new_linked_list.head==None):
                new_linked_list.head=node_temp
            elif (node_temp):
                previous_node.next=node_temp
        temp=temp.next
    return new_linked_list


new_partitoned_ll=partition(singly_linked_list,3)
temp=new_partitoned_ll.head
while(temp):
    print(temp.data)
    temp=temp.next
