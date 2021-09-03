#Write a Python program to print alphabet pattern 'A'. 
j=1
for i in range(7):
    if(i==0):
        print(" ",end=" ")
        print("*"*3)
    if(i==1 or i==4 or i==2 or i==5 or i==6):
        print("*",end="     ")
        print("*")
    if(i==3):
        print("*"*7)