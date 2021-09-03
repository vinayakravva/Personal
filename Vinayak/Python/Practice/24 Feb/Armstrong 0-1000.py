i=0
while(i<=1000):
    num=i
    i+=1
    temp=str(num)
    temp1=int(temp)
    n=len(temp)
    y=0
    sum1=0
    while(y<n):
        sum=int(temp[y])**n+sum1
        y+=1
        sum1=sum
    if(sum==num):
        print(f"{num} is a Armstrong Number")