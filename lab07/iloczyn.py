from math import inf,log

def relax(par,d,u,v,c):
    if d[v]>d[u]+c:
        d[v]=d[u]+c
        par[v]=u
        return True
    return False

def iloczyn(G,s):
    n=len(G)

    d=[inf for _ in range(n)]
    par=[None for _ in range(n)]

    par[s]=0

    for k in range(n):
        b=False
        for i in range(n):
            for j in range(n):
                if(G[i][j]!=None):
                    print(G[i][j])
                    b|=relax(par,d,i,j,log(G[i][j]))
        if not b:
            return True,par,d

    if b:
        return False,par,d
    return True,par,d

G=[[None,None,None,None,None,None,1   ,3  ,None],
   [None,None,1   ,None,None,None,None,None,None],
   [None,None,None,6   ,None,None,None,None,None],
   [None,None,None,None,None,4   ,None,None,None],
   [None,None,10  ,None,None,None,None,None,None],
   [None,None,None,None,1    ,None,1  ,None,None],
   [None,None,None,None,None,None,None,4   ,None],
   [None,None,None,None,None,None,None,None,None],
   [None,None,None,None,None,None,2   ,None,None],
]
d,par,is_cycle=iloczyn(G,1)
print(d,"\n",par)
print(is_cycle)
