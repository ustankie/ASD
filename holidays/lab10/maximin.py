def maximin(T,k):
    n=len(T)

    F=[[0 for _ in range(k+1)]for _ in range(n)]
    par=[[[ None,None]for _ in range(k+1)]for _ in range(n)]

    F[0][1]=T[0]
    for i in range(n):
        F[i][1]=F[i-1][1]+T[i]
    
    for i in range(1,n):
        for j in range(2,k+1):
            for p in range(j,i):
                if min(F[p][j-1],F[i][1]-F[p][1])>F[i][j]:
                    par[i][j]=[p,j-1]
                F[i][j]=max(F[i][j],min(F[p][j-1],F[i][1]-F[p][1]))
    return F[n-1][k],get_solution(F,par,T)


def get_solution(F,par,G):
    n=len(par)
    k=len(par[0])-1
    T=[]

    i=n-1
    j=k
    while i!=None and i>0:
        T.append(i)
        i,j=par[i][j]
    
    T=T[::-1    ]
    print(T)
    R=[[]for _ in range(k)]
    #j=0
    a=0
    b=T[0]
    for p in range(k+1):
        for i in range(a,b+1):
            R[p].append(G[i])
        a=b+1
        if p<k-1:
            b=T[p+1]
    print(R)
    


A = [5, 2, 7, 1, 6, 3, 8, 4, 2, 7]
k = 3


# A = [5, 6, 1, 3, 12, 1, 6, 5, 8, 2, 7]
# #    [   15   ]  [  19  ]  [   22   ]
# k = 3
print(maximin(A,k))