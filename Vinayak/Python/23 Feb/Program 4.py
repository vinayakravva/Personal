#Write a Python program to count the number of even and odd numbers from a series of numbers.
i=0 
j=0
num=int(input("Enter number from where the series must start:"))
num1=int(input("series must end at:"))
while(num1>=num):
    if(num%2==0):
        i+=1
    else:
        j+=1
    num+=1

print(f'There are {i} even numbers and {j} odd numbers in Entered series')
   