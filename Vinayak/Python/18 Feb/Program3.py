#Python program to find the largest number amongst the three Numbers
a=int(input("Enter 1st Number :"))
b=int(input("Enter 2nd Number :"))
c=int(input("Enter 3rd Number :"))
if(a>b and a>c):
  print("1st Number is greater")
elif(b>a and b>c):
    print("2nd Number is greater")
else:
    print("3rd Number is greater")
    

