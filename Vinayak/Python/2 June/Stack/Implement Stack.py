from collections import deque
class Stack:
    def __init__(self):
        self.items=deque()
 
    def is_empty(self):
        return self.items == []
 
    def push(self, data):
        self.items.append(data)
 
    def pop(self):
        return self.items.pop()
 
 
s = Stack()
while True:
    n=int(input("Enter what operation u want to perform:"))
    if n==1:
        s.push(int(input("Enter number to push1:")))
    if n==2:
        print(s.pop())
    if n==3:
        exit()