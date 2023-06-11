def filter(A,T):
    n=len(A)
    B=[]
    for i in range(n):
        if A[i]<=T and A[i]>0:
            B.append(A[i])
    return B

def subsum(A,T):
    if T<0:
        return False
    if T<=1:
        for el in A:
            if el==T:
                return True
        return False
    A=filter(A,T)
    n=len(A)
    F=[False for _ in range(T+1)]

    F[0]=True
    F[A[0]]=True

    for a in range(1,n):
        for t in range(T,A[a]-1,-1):
            F[t]=F[t] or F[t-A[a]]
            if F[T]:
                return F[T]
    return F[T]
def el_of_sum(A,T,F):
    n=len(A)
    i=n-1
    j=T
    B=[]
    while i>0 and j>0:
        #print(i,j,A[i])
        if j>=A[i] and F[i-1][j-A[i]]:
                B.append(A[i])
                j-=A[i]
                i-=1

        else:
            i-=1
    if i>=0 and j>=A[i]:
        B.append(A[i])
        
    return B[::-1]

def subsum2(A,T):
    if T<0:
        return False
    if T<=1:
        for el in A:
            if el==T:
                return True
        return False
    A=filter(A,T)
    n=len(A)
    F=[[False for _ in range(T+1)] for _ in range(n)]

    for i in range(n):
        F[i][0]=True
    F[0][A[0]]=True
    for a in range(1,n):
        for t in range(T,-1,-1):
            F[a][t]=F[a-1][t] 
            if t>=A[a]:
                F[a][t]=F[a][t] or F[a-1][t-A[a]]
            if F[a][T]:
                #print(*F,sep="\n")

                return F[a][T],el_of_sum(A,T,F)
    #print(*F,sep="\n")
    return F[n-1][T],el_of_sum(A,T,F)
A = [3, 5, 0, 0, 17, 3, 5, 2, 7, 8]
A = [4, 4, 1, 0, 7, 1]
T = 11

print(subsum2(A, T))