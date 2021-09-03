#Accept number from user and calculate the sum of all number between 1 and given number
a=int(input("Enter Number:"))
sum=0
for x in range(1,a+1):
    sum=sum+x
print(sum)