from zad12ktesty import runtests 

def autostrada( T, k ):
    n=len(T)
    inf=float('inf')
    F=[[inf for _ in range(k+1)]for _ in range(n)]

    F[0][1]=T[0]
    for i in range(1,n):
        F[i][1]=F[i-1][1]+T[i]

    for i in range(1,n):
        for j in range(2,k+1):
            for m in range(j-1,i+1):
                F[i][j]=min(F[i][j],max(F[m][j-1],F[i][1]-F[m][1]))
    return F[n-1][k]


runtests ( autostrada,all_tests=True )

T = [5, 10, 30, 20, 15]
k = 3

print(autostrada(T,k))