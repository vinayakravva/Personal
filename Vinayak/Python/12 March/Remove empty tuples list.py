#Program to remove empty tuples from a list
list1=[1,8,4,"a","t",(1,2)]
for i in list1:
    if(type(i)==tuple):
        if(len(i)==0):
            list1.remove(i)
print(list1)
