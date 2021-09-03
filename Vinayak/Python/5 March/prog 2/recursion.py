#Write a Python program to get the factorial of a number using recursion
#Algorithm 
# define function
#contional statement if n==1 return 1
#else sum=n*recursion function(n-1)
#exit out of loop and return sum from the function
#print and call function by assigning value
def fact(n):
    if n==1:
        return 1
    else:
        sum=n*fact(n-1)
    return sum
print(fact(5))
