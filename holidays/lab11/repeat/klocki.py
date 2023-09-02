def bricks(A):
    n=len(A)
    F=[0 for _ in range(n)]
    F[0]=1

    for i in range(1,n):
        for j in range(i):
            if A[j][0]<=A[i][0] and A[i][1]<=A[j][1]:
                F[i]=max(F[i],F[j]+1)

    return n-F[n-1]

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

def lis(A,b):
    n=len(A)
    R=[]
    for i in range(n):
        a=binsearch(R,A[i][b],b)
        if a==len(R):
            R.append(A[i])
        else:
            R[a]=A[i]
    return R

def bricks2(A):
    R=lis(A,0)
    R=lis(R,1)
    return len(A)-len(R)-1,R


ranges = [
    [0, 5],
    [1, 4],
    [-3, 7],
    [2, 3],
    [2, 6],
    [4, 6],
    [2, 3]
]
ranges = [(0, 10), (1, 10), (2, 6), (6, 7), (11, 20), (11, 19), (12, 18), (13, 19), (14, 20)]
print(bricks2(ranges))
