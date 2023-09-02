def maximin(A,k):
    n=len(A)
    F=[[0 for _ in range(k+1)]for _ in range(n)]
    par=[[[None,None] for _ in range(k+1)]for _ in range(n)]


    F[0][1]=A[0]
    for i in range(1,n):
        F[i][1]=F[i-1][1]+A[i]

    for i in range(1,n):
        for j in range(2,k+1):
            for p in range(j,i):
                a=min(F[p][j-1],F[i][1]-F[p][1])
                if a>F[i][j]:
                    F[i][j]=max(a,F[i][j])
                    par[i][j]=[p,j-1]
    return F[n-1][k],get_solution(par,k,A)

def get_solution(par,k,A):
    n=len(par)

    i=n-1
    j=k

    R=[[]for _ in range(k)]
    while i!=-1:
        print(i,j,n,k)
        i1,j1=par[i][j]
        if i1==None:
            i1=-1
        for p in range(i1+1,i+1):
            R[j-1].append(A[p])
        i,j=i1,j1
        
    return R




A = [5, 2, 7, 1, 6, 3, 8, 4, 2, 7]
k = 3


A = [5, 6, 1, 3, 12, 1, 6, 5, 8, 2, 7]
#    [   15   ]  [  19  ]  [   22   ]
k = 3
print(maximin(A,k))

