from numpy import argmax
from time import time
def map_cars(A, L):
    total = 0
    for i in range(len(A)):
        A[i] = int(A[i] * 100 + .5)
        total += A[i]
        if total > 2 * L:
            return i 
    return len(A) 
def ferry(A,L):
    n=len(A)
    L=int(L*100+.5)
    n=map_cars(A,L)
    #print(A)
    F=[[[None for _ in range(L+1)]for _ in range(L+1)]for _ in range(n)]
    if A[0]<=L:
        F[0][L-A[0]][L]=1
        F[0][L][L-A[0]]=1
    else:
        return 0
    def rec(i,r,l):
        if i==0 and l-A[i]>=0 or r-A[i]>=0:
            return 1
        if F[i][r][l]==None:
            F[i][r][l]=0
            if r-A[i]>=0 and i>0:
                F[i][r][l]=rec(i-1,r-A[i],l)
            if l-A[i]>=0 and i>0:
                F[i][r][l]=F[i][r][l] or rec(i-1,r,l-A[i])
            
        return F[i][r][l]

    # print(*F,sep="\n")

    for i in range(n-1,-1,-1):
        if rec(i,L,L):
            return i+1
    
    return -1

def ferry2(A,L):
    n=len(A)
    L=int(L*100+.5)
    n=map_cars(A,L)
    #print(A)
    F=[[[0 for _ in range(L+1)]for _ in range(L+1)]for _ in range(n)]
    D=[0 for _ in range(n)]
    D[0]=1
    if A[0]<=L:
        F[0][L-A[0]][L]=1
        F[0][L][L-A[0]]=1
    else:
        return 0

    for i in range(1,n):
        for l in range(L,-1,-1):
            for r in range(L,-1,-1):
                if r+A[i]<=L:
                    F[i][l][r]=F[i-1][l][r+A[i]] or F[i][l][r]

                if l+A[i]<=L:
                    F[i][l][r]=F[i-1][l+A[i]][r] or F[i][l][r]

                D[i]=D[i] or F[i][l][r]

    for i in range(n-1,-1,-1):
        if D[i]:
            return i+1
    return 0


L = 18.24

cars = [15.16, 7.23, 4.98, 2.11, 3.08, 3.92, 6.34, 4.39, 2.63, 1234.88]
L = 18.24

cars = [3.16, 7.23, 4.98, 2.88, 6.34, 4.39, 2.63, 4.88]
# L=10
# cars=[3,5,6,6]
start=time()
print(ferry(cars,L))
end=time()
print(end-start)

        