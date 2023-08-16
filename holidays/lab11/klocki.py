
def klocki(K):
    n = len(K)
    F=[0 for _ in range(n)]
    F[0]=1

    for i in range(1,n):
        for j in range(i):
            if K[j][0]<=K[i][0] and K[j][1]>=K[i][1]:
                F[i]=max(F[i],F[j]+1)

        
    return n-max(F)

def binsearch(A,x,p):
    n=len(A)
    i=0
    j=n-1

    while i<=j:
        q=(i+j)//2
        if A[q][p]==x:
            return q
        if p==0:
            if A[q][p]<x:
                i=q+1
            else:
                j=q-1
        else:
            if A[q][p]>=x:
                i=q+1
            else:
                j=q-1
    return i

def lis(K,p):
    n=len(K)
    F=[]

    for i in range(n):
        
        a=binsearch(F,K[i][p],p)
        if a==len(F):
            F.append(K[i])
        else:
            F[a]=K[i]
    return F

def klocki2(K):
    L=lis(K,0)
    R=lis(L,1)

    return len(K)-len(R)-1

A = [
    [0, 5],
    [1, 4],
    [-3, 7],
    [2, 3],
    [2, 6],
    [4, 6],
    [2, 3]
]
#A=[(0, 10), (1, 10), (2, 6), (6, 7), (11, 20), (11, 19), (12, 18), (13, 19), (14, 20)]
print(klocki2(A))