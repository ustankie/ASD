
from egz1btesty import runtests

def dist(D,i,j):
    return D[j]-D[i]

def planets(D, C, T, E):
    n=len(D)
    F=[[float('inf')for _ in range(E+1)]for _ in range(n)]

    for i in range(E+1):
        F[0][i]=i*C[0]

    for i in range(n-1):
        distance=dist(D,i,i+1)
        for j in range(E+1):
            if j>0:
                F[i][j]=min(F[i][j],F[i][j-1]+C[i])
            if j==0:
                F[T[i][0]][0]=min(F[T[i][0]][0],F[i][0]+T[i][1])
            if distance<=j:
                F[i+1][j-distance]=min(F[i+1][j-distance],F[i][j])


    return min(F[n-1])

# zmien all_tests na True zeby uruchomic wszystkie testy
runtests(planets, all_tests=True)


D=  [0, 5, 10, 20]
C=  [2, 1, 3, 8]
T= [(2, 3), (3, 7), (2, 10), (3, 10)]
E= 10
print(planets(D,C,T,E))