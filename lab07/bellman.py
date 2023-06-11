from math import inf
def relax(d,par,u,v,c):
    if d[v]>(d[u]+c):
        par[v]=u
        d[v]=d[u]+c
        return True
    return False

def bf(G,s):
    n=len(G)

    d=[inf for _ in range(n)]
    par=[None for _ in range(n)]

    d[s]=0

    for k in range(n):
        b=False
        for i in range(n):
            for j in range(n):
                if G[i][j]!=None:
                    b|=relax(d,par,i,j,G[i][j])
        if not b:
            return d,par,False
    if b:
        return d,par,True
    return d,par,False

G=[[None,None,None,None,None,None,1   ,-3  ,None],
   [None,None,1   ,None,None,None,None,None,None],
   [None,None,None,6   ,None,None,None,None,None],
   [None,None,None,None,None,4   ,None,None,None],
   [None,None,-10 ,None,None,None,None,None,None],
   [None,None,None,None,0   ,None,-1  ,None,None],
   [None,None,None,None,None,None,None,-4  ,None],
   [None,None,None,None,None,None,None,None,None],
   [None,None,None,None,None,None,2   ,None,None],
]
d,par,is_cycle=bf(G,1)
print(d,"\n",par)
print(is_cycle)
