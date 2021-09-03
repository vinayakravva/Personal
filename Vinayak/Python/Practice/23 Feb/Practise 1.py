#Take 10 integers from keyboard using loop and print their average value on the screen.
sum = 0
i = 1
while(i<=10):
    num = int(input("Enter the Number"))
    sum = sum + num
    i+=1
print("Average is =",sum/10)