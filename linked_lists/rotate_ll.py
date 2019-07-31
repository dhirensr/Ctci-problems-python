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

    def rotate(self,rotation_count):
        current=self.head
        temp_counter=1
        while (temp_counter!=rotation_count):
            temp_counter+=1
            current=current.next_node
        temp=current.next_node
        temp1=self.head
        self.head=temp
        current.next_node=None
        while(temp!=None):
            previous=temp
            temp=temp.next_node
        previous.next_node=temp1
        return self


node=Node(1)
ll=LinkedList(node)
ll.add_node(3)
ll.add_node(2)
ll.add_node(5)
ll.add_node(6)

ll.rotate(4)
ll.traverse()
