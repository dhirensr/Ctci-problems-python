class Node():
    def __init__(self,data,next_node=None):
        self.data=data
        self.next_node=next_node

    def getnext(self):
        return self.next_node

    def setnext(self,next_node):
        self.next_node=next_node
        return self

    def getdata(self):
        return self.data


class LinkedList():
    def __init__(self,head):
        self.head=head
        self.tail=None

    def add_node(self,data):
        new_node=Node(data)
        new_node.next_node=self.head
        self.head=new_node
        return self

    def traverse(self):
        current=self.head
        while(current!=None):
            print(current.data)
            current=current.next_node

    def middle_element(self):
        current=self.head
        second_pointer=self.head
        while (second_pointer.next_node !=None):
            if(second_pointer.next_node.next_node == None):
                second_pointer=second_pointer.next_node
            else:
                second_pointer=second_pointer.next_node.next_node
            current=current.next_node
        return current.data

node=Node(1)
ll=LinkedList(node)
ll.add_node(3)
ll.add_node(2)
ll.add_node(5)
ll.add_node(6)


#ll.traverse()
#ll.middle_element()
print(ll.middle_element())
