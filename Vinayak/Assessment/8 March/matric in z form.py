## program to print the matric in z form 
n=3
a= [ [ 4, 5, 6],
    [ 1, 2, 3],
    [ 7, 8, 9 ] ]
for i in range(n):
    for j in range(n):
        if(i == 0):
            print(a[i][j], end = " ")
        elif(i == j):
            print(a[i][j], end = " ")
        elif(i == n - 1):
            print(a[i][j], end = " ")
print()