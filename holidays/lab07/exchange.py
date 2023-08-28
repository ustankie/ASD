from math import log10
def relax(par,d,u,v,c):
    if d[v]>d[u]+c:
        d[v]=d[u]+c
        par[v]=u
        return True
    return False

def bf(G,s):
    n=len(G)
    
    d=[float('inf') for _ in range(n)]
    par=[None for _ in range(n)]

    d[s]=0
    
    for i in range(n):
        b=False
        for u in range(n):
            for v in range(n):
                if G[u][v]!=0:
                    b=relax(par,d,u,v,G[u][v]) or b
        if not b:
            return False
    #if b:
    return True
    #return False

def exchange(G):
    n=len(G)
    for i in range(n):
        for j in range(n):
            if G[i][j]>0:
                G[i][j]=log10(G[i][j])
    print(*G,sep="\n")
    
    for i in range(n):
        if bf(G,i):
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
print(exchange(G2))