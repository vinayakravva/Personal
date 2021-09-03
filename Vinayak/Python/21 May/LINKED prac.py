class Node:
    def __init__(self,data):
        self.data=data
        self.next=None


class LinkedList:
    def _init_(self):
        self.head=None
    def insert_at_begining(self,data):
        node=Node(data)
        self.head=node
    def print(self):
        itr=self.head
        while itr is not None:
            print(itr.data,end=" --> ")
            itr=itr.next



    
ll=LinkedList()
ll.insert_at_begining(9)
ll.insert_at_begining(9)
ll.insert_at_begining(9)
ll.insert_at_begining(9)
ll.insert_at_begining(9)


