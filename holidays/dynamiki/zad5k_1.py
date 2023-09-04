from zad5ktesty import runtests

def garek ( A ):
    n=len(A)
    F=[[[None,None] for _ in range(n)]for _ in range(n)]

    def rec(i,j):
        if i>j:
            return [0,0]

        if F[i][j]!=[None,None]:
            return F[i][j]
        if i==j:
            F[i][j][0]=A[i]
            F[i][j][1]=0
            return F[i][j]
        
        a=rec(i+1,j)
        b=rec(i,j-1)
    
        F[i][j][0]=max(a[1]+A[i],b[1]+A[j])
        F[i][j][1]=min(a[0],b[0])

        return F[i][j]

    rec(0,n-1)
    print(*F,sep="\n")
    return F[0][n-1][0]
        


# runtests ( garek )
T = [8, 15, 3, 7]
print(garek(T))