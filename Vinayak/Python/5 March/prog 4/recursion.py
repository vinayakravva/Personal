#Python program to find the sum of sequence of all numbers upto the given number using recursive function
# enter the no from user
#  create a function
# conditional statements
# add recursive statement
# take if statement
# then call the functionn=10
def add(k):
    if(k>0):
        result=k+add(k-1)
    else:
        return 0
    return result
print (add(5))