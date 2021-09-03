#Python Program to add two matrices using nested for loop.
X=[[6,3],[2,1]]
Y=[[8,5],[7,4]]
add=[[0,0],[0,0]]
for i in range(len(X)):
    for j in range(len(Y)):
        add[i][j]=X[i][j]+Y[i][j]
for x in add:
    print(x)