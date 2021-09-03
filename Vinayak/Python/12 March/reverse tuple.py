#Program to reverse a tuple
tuple1=("a",1,"t","d","p")
y=list(tuple1)
list1=[]
for i in range(-1,-(len(y)+1),-1):
    list1.append(y[i])
list1=tuple(list1)
print(list1)
