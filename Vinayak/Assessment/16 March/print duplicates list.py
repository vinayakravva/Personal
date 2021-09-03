#Program to print duplicates from a list of integers 
list1=[-1,-1,1,8]
repeated=[]
for i in range(len(list1)):
    k=i+1
    for j in range(k,len(list1)):
        if list1[i]==list1[j] and list1[i] not in repeated:
            repeated.append(list1[i])
print(repeated)
