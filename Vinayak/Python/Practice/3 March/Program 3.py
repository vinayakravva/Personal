#Python program to check whether the string is Symmetrical
var=str(input("Enter any word:"))
n=(len(var))//2
i=0
j=n
flag=0
while(i<n and j<(len(var))):
    if(var[i]==var[j]):
        i+=1
        j+=1
    else:
        flag=1
        print("Not symmetrical")
        break
if(flag==0):
    print("symmetrical")