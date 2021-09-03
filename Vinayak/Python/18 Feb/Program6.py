#Program to check  entered input is  alphabet digit or special character
var =(input("Enter any Number/Digit or Character :"))
d=ord(var)
if(d>=65 and d<=90)or(d>=97 and d<=122):
    print("Its a Alphabet")
elif(d>=48 and d<=57):
    print("Its a digit")
else:
    print("Its a Special Character")




    
