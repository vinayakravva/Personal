num=int(input("Enter the Number ="))
if(num >= 100):
    if(num%2==0):
      print(f"{num} is even")
    else:  
          print(f"{num} is odd")
else:
    print(f"{num} is not accepted,Number should be greater than 100")
        