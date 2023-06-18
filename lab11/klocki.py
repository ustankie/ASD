#1)
# F[i]-wysokość najwyższej wieży zbudowanej z klocków ze zbioru od 0 do i
#F[0]=1
#F[i]=max(F[j])+1,j od 0 do i
#O(n^2)
#2)
#dwa razy algorytm na longest increasing subsequence O(nlogn)
def klocki(A):
    n=len(A)
    F=[0 for _ in range(n)]
    F[0]=1
    T=[]
    for i in range(1,n):
        for j in range(i):
            if A[i][0]>=A[j][0] and A[i][1]<=A[j][1]:
                F[i]=max(F[i],F[j])
        F[i]+=1
    return  n-max(F)

def binsearch(A,x,p):
    n=len(A)
    i=0
    j=n-1
    while i<=j:
        q=(i+j)//2
        if A[q][p]<=x:
            i=q+1
        else:
            j=q-1
    return i
        
def lis(A,p):
    n=len(A)
    F=[]
    for i in range(n):
        a=binsearch(F,A[i][p],p)
        if a==len(F):
            F.append(A[i])
        else:
            F[a]=A[i]
    return F

def klocki2(A):
    F=lis(A,0)
    F2=F[::-1]
    F3=lis(F2,1)

    return len(A)-len(F3)






A = [
    [0, 5],
    [1, 4],
    [-3, 7],
    [2, 3],
    [2, 6],
    [4, 6],
    [2, 3]
]
A=[(0, 10), (1, 10), (2, 6), (6, 7), (11, 20), (11, 19), (12, 18), (13, 19), (14, 20)]
print(klocki2(A))