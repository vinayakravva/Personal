#Program to remove all consecutive duplicates
str1=str(input("Enter Keyword:"))
t=""
for i in str1:
    if(i in t):
        pass
    else:
        t=t+i
print(t)
