# Write a Python program to calculate the sum of a list of numbers using recursion.
#Algorithm
# First assign list
# define function
# assign sum variable to 0
# use for loop which iterates x in list
# conditional statement if type of x is == to type of list within the list
# use recusrion function
# else use sum=sum+x
# return sum 
# print or call function
list1=[8,5,[7,6],48,12]

def list_recursion(k):
    sum=0
    for x in k:
        if type(x)==type([]):
            sum=sum+list_recursion(x)
        else:
            sum=sum+x
    return sum
print(list_recursion(list1))
