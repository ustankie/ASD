from zad1testy import runtests
def zbigniew(A):
    n=len(A)
    F=[[float('inf') for _ in range(n)]for _ in range(n)]

    F[0][A[0]]=0
    for i in range(1,A[0]+1):
        F[i][A[0]-i]=1

    for i in range(1,n):
        for j in  range(n):
            for k in range(1,A[i]+j+1):
                if 0<=j+A[i]-k<n and i+k<n:
                    F[i+k][j+A[i]-k]=min(F[i][j]+1,F[i+k][j+A[i]-k])

    return min(F[n-1])

runtests(zbigniew)

A = [2, 2, 1, 0, 0, 0]


#A = [2, 3, 1, 1, 2, 0]
print(zbigniew(A))




