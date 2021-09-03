#Write a function for convert age to days
num=str(input("Enter your age in DDMMYYYY format:"))
x=num.split('/')
print(x)
year=int(x[2])
print(year)
month=int(x[1])
date=int(x[0])
year1=2021
month1=3
date1=4
def leap():
    i=0
    year=int(x[2])
    while(year<year):
        if(year%4==0):
            i+=1
        year+=1
    return i


