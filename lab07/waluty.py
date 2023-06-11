from math import log10
def relax(par,d,u,v,c):
    if d[v]>d[u]+c:
        d[v]=d[u]+c
        par[v]=u
        return True
    return False

def bf(K,s):
    n=len(K)
    d=[float('inf') for _ in range(n)]
    par=[None for _ in range(n)]
    for u in range(n):
        for v in range(n):
            if K[u][v]>0:
                K[u][v]=log10(K[u][v])

    print(*K,sep="\n")
    print()
    d[s]=0
    for t in range(n):
        b=False
        for u in range(n):
            for v in range(n):
                if K[u][v]!=0:
                    b=b or relax(par,d,u,v,G[u][v])
                    #print(d,par,b)
        if not b:
            return False
    return True
def currency(K):
    n=len(K)
    for i in range(n):
        if bf(K,i):
            return i
    return None

def create(K,m):
    n=len(K)

    G=[[0 for _ in range(m)]for _ in range(m)]
    for i in range(n):

        G[K[i][0]][K[i][1]]=K[i][2]
    return G

PLN = 0; EUR = 1; USD = 2; YEN = 3

K = [(PLN, EUR, 4.51), (PLN, USD, 3.68), (PLN, YEN, 0.034),
     (EUR, PLN, 0.22), (EUR, USD, 0.82), (EUR, YEN, 0.0075),
     (USD, PLN, 0.27), (USD, EUR, 1.22), (USD, YEN, 0.0091),
     (YEN, PLN, 29.83), (YEN, EUR, 133,47), (YEN, USD, 109.62)]

G=create(K,4)
#print(G)
G2=[
    [ 0  ,0.5, 5 ],
    [0.5 , 0 ,1.5],
    [0.25, 1 ,0  ]
    ]
print(currency(G))