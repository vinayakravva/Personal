#Check whether a given string is Heterogram or not
str1=str(input("Enter word to check:"))
k=0
for i in range(len(str1)):
    for j in range(len(str1)):
        if(i==j):
            continue
        if(str1[i]==str1[j]):
            k+=1
if(k>0):
    print("Not a Heterogram")
else:
    print("Its a Heterogram")
        
    
        
