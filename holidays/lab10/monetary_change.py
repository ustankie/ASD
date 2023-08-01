def filter(A,T):
    B=[]
    n=len(A)

    for i in range(n):
        if A[i]<=T:
            B.append(A[i])
    return B
def change(A,T):
    n=len(A)
    maxi=max(A)
    mini=min(A)

    A.sort()
    A=filter(A,T)
    n=len(A)
    inf=float('inf')
    F=[[inf for _ in range(T+1)]for _ in range(n)]
    if T<mini:
        return inf
    for i in range(n):
        F[i][A[i]]=1
    
    for i in range(n):

        for j in range(T+1):
            if i>0 and F[i-1][j]:
                F[i][j]=min(F[i][j],F[i-1][j])

            for k in range(j):
                if F[i][k] and F[i][j-k]<inf and F[i][k]<inf:
                    F[i][j]=min(F[i][j],F[i][k]+F[i][j-k])
                    #print(k,j-k)
                    #break
    return F[n-1][T]

def change2(A,T):
    n=len(A)
    inf=float('inf')
    F=[T+1 for _ in range(T+1)]
    par=[[None,None] for _ in range(T+1)]
    F[0]=0

    for i in range(1,T+1):
        for j in range(n):
            if A[j]<=i and F[i]>F[i-A[j]]+1:
                F[i]=min(F[i],F[i-A[j]]+1)
                par[i]=(i-A[j],A[j])
    if F[T]==T+1:
        F[T]=inf
    return F[T],get_solution2(F,par)

def get_solution2(F,par):
    T=len(F)-1
    if F[T]==float('inf'):
        return []
    
    R=[]
    p=T
    while p!=None:
        p,add=par[p]
        if p!=None:
            R.append(add)
    return R
    


A= [2, 5]
T=21

print(change2(A,T))
