#Python program to interchange first and last elements in a list 
list1=[12,35,9,56,5]
list2=list1[0]
list3=list1[len(list1)-1]
list1.pop(0)
list1.pop()
list1.insert(0,list3)
list1.append(list2)
print(list1)