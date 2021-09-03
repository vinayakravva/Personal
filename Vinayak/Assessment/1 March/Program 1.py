#Print first 50 Fibonacci NUmbers
i=0
a=0
b=1
while(i<=50):
    if(i==0):
        print(i)
    if(i==1):
        print(i)
    if(i>1):
        fib=a+b
        print(fib)
        a=b
        b=fib
    i+=1
    
