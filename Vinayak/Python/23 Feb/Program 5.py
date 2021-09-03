#Write a Python program to get the Fibonacci series between 0 to 50.
#num=int(input("Enter number from where to start Fibonacci Sequence"))
#num1=int(input("Enter number from where to end Fibonacci Sequence"))
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
    

    
        
        


    

 
