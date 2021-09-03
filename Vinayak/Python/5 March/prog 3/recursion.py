#Write a Python program to solve the Fibonacci sequence using recursion.
#Algorithm
#define function fib
#assign n term and use for loop till range of n
#pass the for loop each value to function fib
#now in fib function write if n<=1 return n
#else return fib(n-1)+fib(n-2)


def fib(n):
    if(n<=1):
        return n
    else:
        return(fib(n-1)+fib(n-2))

n=10
for i in range(n):
    print(fib(i))