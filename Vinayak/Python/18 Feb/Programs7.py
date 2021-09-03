#Program to input basic salary of an employee and calculate gross salary according to given conditions.
#Basic Salary <= 10000 : HRA = 20%, DA = 80%    
#Basic Salary is between 10001 to 20000 : HRA = 25%, DA = 90%
#Basic Salary >= 20001 : HRA = 30%, DA = 95%
b=int(input("Enter Basic Salary :"))
if(b<=10000):
    print("GROSS SALARY :",0.2*b+0.8*b+b)
elif(b>=10001 and b<=20000):
    print("Gross Salary :",0.25*b+0.9*b+b)
elif(b>=20001):
    print("Gross Salary :",0.3*b+0.95*b+b )
else:
    print("Nothing")