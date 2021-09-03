n=int(input('Enter a number: '))
 
b=int(bin(n)[2:])
rev=str(b)[::-1] 
if int(rev)==b:
    print(f"Binary representation of n={n} is {b} which is pallindrome ")
else:
    print(f"Binary representation of n={n} is {b} which is not a pallindrome ")
            
