# Write a Python program to reverse the digits of a given number and add it to the original, If the sum is not a palindrome repeat this procedure
num=int(input("Enter to check:"))
while True:
    temp=str(num)
    temp=int(temp[::-1])
    if num==temp:
        print(f'{num} is a palindrome')
        break
    else:
        num += temp