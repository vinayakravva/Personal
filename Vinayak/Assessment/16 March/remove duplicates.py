#Program to remove all duplicates from a given string in Python
str1=str(input("Enter the word/sentence:"))
str1=str1.replace(" ","")
#str2=set(str1)
#str2="".join(str2)
t=""
for i in str1:
    if(i in t):
        pass
    else:
        t=t+i
print(t)
