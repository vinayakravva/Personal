class node:
    def __init__(self,id,name,batch):
        self.id = id
        self.name = name 
        self.batch = batch
        self.next = None
        self.prev = None


class double_linkedlist:
    def __init__(self):
        self.head = None

    def insert(self,newnode):
        if self.head == None:
            self.head = newnode
            self.head.prev = None
            self.head.next = None
        else:
            temp = self.head
            while(temp.next is not None):
                temp = temp.next
            temp.next = newnode
            newnode.prev = temp

    def display(self):
        temp = self.head
        print("Null <-----",end="")
        while(temp):
            print(f"[ID : {temp.id} , Name : {temp.name} , Batch : {temp.batch}] <---> ",end=" ")
            temp = temp.next
        print("null")


    def search(self,id):
        temp = self.head
        while(temp):
            if id == temp.id:
                print(f"[ID : {temp.id} , Name : {temp.name} , Batch : {temp.batch}]",end=" ")
                break
            temp = temp.next

        else:
            print("ID not found")
    def update(self,newnode):
        temp = self.head
        while(temp):
            if temp.id == newnode.id:
                temp.name = newnode.name
                temp.batch = newnode.batch
                break
            temp = temp.next
        else:
            print("ID not found")

        print("Your node : ")
        ob.display()

    def delete(self, id) :
        temp = self.head
        if temp is not None :
            if temp.id == id:
                self.head = temp.next
                temp.next.prev = None
                temp = None
                return
        while(temp is not None) :
            if temp.id == id :
                break
            temp = temp.next
        if temp == None :
            return -1
        temp.prev.next = temp.next
        temp.next.prev = temp.prev
        temp = None

ob = double_linkedlist()
# Driver code 
while(True):
    print("""
    1 -- ADD
    2 -- Display
    3 -- Search 
    4 -- Update
    5 -- Delete
    6 -- Exit
    """)

    ch = int(input("Enter your choice : "))

    if ch == 1:
        id = int(input("Enter your id : "))
        name = input("Enter your name : ")
        batch = input("Enter youe Batch name / no : ")
        newnode = node(id,name,batch)
        ob.insert(newnode)
    elif ch == 2:
        ob.display()

    elif ch == 3:
        id = int(input("Enter the ID : "))
        ob.search(id)

    elif ch == 4:
        id = int(input("Enter your id : "))
        name = input("Enter the new name : ")
        batch = input("Enter new batch name / no : ")
        newnode=node(id,name,batch)
        ob.update(newnode)

    elif ch == 5:
        id = int(input("Enter the ID : "))
        ob.delete(id)

    elif ch == 6:
        exit()

    else:
        print("")
        print("\t\t\tInvalid choice") 