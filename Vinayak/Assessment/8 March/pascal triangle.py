#Program to print the pascal's  triangle using recursion
def triangle(n):
    for i in range(n):
        if(i==0):
          print(" "*(n-i-1),end="")
          print(1)
        else:
            result=11**(i)
            print(" "*(n-i-1),end="")
            print(result)
k=int(input("Enter no of rows:"))
triangle(k)


