from zad2testy import runtests
def binsearch(A,x,b):
    n=len(A)
    i=0
    j=n-1

    while i<=j:
        q=(i+j)//2
        if b:
            if x[1]>A[q][1]:
                j=q-1
            else:
                i=q+1
        else:

            if x[0]<A[q][0]:
                j=q-1
            else:
                i=q+1
    return i

def klocki(A):
    n=len(A)

    F=[0 for _ in range(n)]
    F[0]=1
    for i in range(1,n):
        for j in range(i):
            if A[j][0]<=A[i][0] and A[j][1]>=A[i][1] and F[i]<F[j]+1:
                F[i]=F[j]+1
    return max(F)+1

def lis(A,b):
    n=len(A)
    R=[]
    for i in range(n):
        a=binsearch(R,A[i],b)
        if a==len(R):
            R.append(A[i])
        else:
            R[a]=A[i]
        #print(R)
    return R

def klocki2(A):
    R=lis(A,0)
    #print(R)
    R=lis(R,1)
    #print(R)
    return len(R)


ranges = [
    [0, 5],
    [1, 4],
    [-3, 7],
    [2, 3],
    [2, 6],
    [4, 6],
    [2, 3]
]
print(klocki2(ranges))
runtests(klocki)