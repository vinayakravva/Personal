#Write a Python program to create the multiplication table of a number.
num=int(input("Enter the number:"))
i=1
while(i<=10):
    num1=num
    sum=num*i
    print(f"{num1}x{i}=",sum)
    i+=1