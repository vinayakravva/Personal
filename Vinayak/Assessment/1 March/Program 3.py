# check given string is palindrome or not. *
num1=input("Enter the number:")
num3=str(num1)
num1=str(num1)
num2=num1[::-1]
print(num2)
if(num2==num3):
    print("It is a palindrome")
else:
    print("Its not a palindrome")