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

    def k_reverse(self,k):
        current=self.head
        my_stack=[]
        prev=None
        while(current is not None):
            count=0
            while(current is not None and count < k):
                my_stack.append(current)
                current=current.next_node
                count+=1

            while(len(my_stack) > 0):
                if(prev==None):
                    prev=my_stack.pop()
                    self.head=prev
                else:
                    prev.next_node=my_stack.pop()
                    prev=prev.next_node
        prev.next_node=None


node=Node(1)
ll=LinkedList(node)
ll.add_node(3)
ll.add_node(2)
ll.add_node(5)
ll.k_reverse(2)
ll.traverse()
