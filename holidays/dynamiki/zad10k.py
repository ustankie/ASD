from zad10ktesty import runtests
from math import isqrt



def dywany ( n ):
    F=[float('inf') for _ in range(n+1)]
    par=[[None,None] for _ in range(n+1)]
    F[0]=0

    for i in range(1,n+1):
        a=isqrt(i)
        if a*a==i:
            F[i]=1
            par[i]=[i,None]
        else:
            for j in range(i//2):
                if F[i]>F[j]+F[i-j]:
                    par[i]=[j,i-j]
                F[i]=min(F[i],F[j]+F[i-j])

    R=[]
    def get_solution(i):
        if i==None:
            return
        if par[i][0]==i:
            R.append(isqrt(par[i][0]))
        else:
            get_solution(par[i][0])

        if par[i][1]==i:
            R.append(isqrt(par[i][1]))
        else:
            get_solution(par[i][1])
    
    get_solution(n)
    return R




runtests( dywany )
N=10
print(dywany(N))

