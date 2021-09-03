#BubbleSort
def bubbleSort(list1):
    for i in range(len(list1)-1,0,-1):
         for j in range(i):
             if list1[j]>list1[j+1]:
                 temp=list1[j]
                 list1[j]=list1[j+1]
                 list1[j+1]=temp
    return[list1]

#Selection Sort
def selectionSort(list1):
    for i in range(len(list1)):
        min=i
        for j in range(i,len(list1)):
            if list1[j]<list1[min]:
                min=j
        temp=list1[i]
        list1[i]=list1[min]
        list1[min]=temp
    return [list1]

#Merge Sort
def mergeSort(list1):
    if len(list1)<=1:
        return list1
    mid=len(list1)//2
    left=list1[:mid]
    right=list1[mid:]
    left=mergeSort(left)
    right=mergeSort(right)

    return merge_Sort(left,right)

def merge_Sort(a,b):
    sorted_list=[]
    len_a=len(a)
    len_b=len(b)
    i=j=0

    while i<len_a and j<len_b:
        if a[i]<=b[j]:
            sorted_list.append(a[i])
            i+=1
        else:
            sorted_list.append(b[j])
            j+=1
        
    while i<len_a:
        sorted_list.append(a[i])
        i+=1
    while j<len_b:
        sorted_list.append(b[j])
        j+=1
    
    return sorted_list

#InsertionSort
def insertionSort(list1):
    for i in range(len(list)):
        pass



#BinarySearch
def binarySearch(a,n):
    l=0
    u=len(a)-1
    while l<=u:
        mid=(l+u)//2
        if a[mid]==n:
            return mid
        else:
            if a[mid]<n:
                l=mid+1
                
            else:
                u=mid-1
    return -1

#LinearSearch
def linearSearch(list2,n):
    for i in range(len(list2)):
        if list2[i]==n:
            return i
        else:
            return -1

    
                


   
list1=[5,10,2,4,8,9]
list2=[2,4,5,8,9,10,4000,5054789]
n=41
print(bubbleSort(list1))
print(selectionSort(list1))
print(mergeSort(list1))
print(binarySearch(list2,n))
print(linearSearch(list2,n))