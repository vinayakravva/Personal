#Program to accept the strings which contains all vowels
str1=str(input("Enter words with vowels:"))
list1=["a","e","i","o","u"]
sum=0
print(len(list1))
for j in str1:
    for i in list1:
        if(j==i):
            sum+=1

if(sum==len(str1)):
    print("String contains all vowels")
else:
    print("Not accepted")
