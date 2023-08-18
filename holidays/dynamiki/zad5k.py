from zad5ktesty import runtests

def garek ( A ):
    n=len(A)
    s=sum(A)

    G=[[[None,None] for _ in range(n)]for _ in range(n)]

    def rec(i,j):
        if i+1==j:
            G[i][j][0]=max(A[i],A[j])
            G[i][j][1]=min(A[i],A[j])
        if i==j:
            G[i][j][0]=A[i]
            G[i][j][1]=0
            return G[i][j]
        if i>j:
            return [0,0]
        if G[i][j][0]!=None:
            return G[i][j]
        o=rec(i+1,j)
        p=rec(i,j-1)
        G[i][j][0]=max(A[i]+o[1],A[j]+p[1])
        G[i][j][1]=min(o[0],p[0])

        return G[i][j]
    
    rec(0,n-1)

    #print(*G,sep="\n")
    return G[0][n-1][0]


runtests ( garek )
T = [8, 15, 3, 7]
print(garek(T))