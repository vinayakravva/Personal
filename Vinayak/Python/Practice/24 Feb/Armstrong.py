num=input("Enter any number:")
temp=str(num)
temp1=int(temp)
n=len(temp)
i=0
sum1=0
while(i<n):
    sum=int(temp[i])**n+sum1
    i+=1
    sum1=sum
if(sum==temp1):
    print(f"{temp1} is a Armstrong Number")
else:
    print(f"{temp1} is not an Armstrong Number")


