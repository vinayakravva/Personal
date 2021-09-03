#Student Management System
class Student():
    def __init__(self,name,rollno,marks1,marks2):
        self.name=name
        self.rollno=rollno
        self.marks1=marks1
        self.marks2=marks2
    
    def accept(self,Name,Rollno,marks1,marks2):
        ob=Student(Name,Rollno,marks1,marks2)
        ls.append(ob) 
    def display(self,ob):
        print("Name   : ", ob.name)
        print("RollNo : ", ob.rollno)
        print("Marks1 : ", ob.marks1)
        print("Marks2 : ", ob.marks2)
        print("\n")
    def search(self,no):
        for i in ls:
            if i.rollno==no:
                return i


ls=[]
obj=Student('',0,0,0)
obj.accept("A", 1, 100, 100)
obj.accept("B", 2, 90, 90)
obj.accept("C", 3, 80, 80)
print(ls[0].name)
for i in range(len(ls)):    
    obj.display(ls[i])
print(obj.search(2))