S=input("Enter the string to perform operations: ")
Q=input("Enter length of list:")
X=[(input()) for _ in range(Q)]
Y=[(input()) for _ in range(Q)]
for i in range(len(Q)):
    S=list(map(str,S))
    S[X[i]-1]=Y[i]
    S=str("".join(S))
    print(S.count(Y))