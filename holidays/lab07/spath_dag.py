def topsort(G):
    n=len(G)
    vis=[False for _ in range(n)]
    R=[]

    def DFS(u):
        vis[u]=True
        for v,c in G[u]:
            if not vis[v]:
                DFS(v)
        R.append(u)

    for u in range(n):
        if not vis[u]:
            DFS(u)
    return R[::-1]

def search(T,x):
    n=len(T)
    for i in range(n):
        if T[i]==x:
            return i
    return None

def relax(d,par,u,v,c):
    if d[v]>d[u]+c:
        par[v]=u
        d[v]=d[u]+c
        return True
    # print(d[u],d[v],c)
    return False


def spath_dag(G,s):
    n=len(G)
    T=topsort(G)
    #print(T)
    position=search(T,s)
    #print(position)

    
    inf=float('inf')
    d=[inf for _ in range(n)]
    par=[None for _ in range(n)]

    d[s]=0
    
    for u in range(position,n):
        #print(u,T[u])
        for v,c in G[T[u]]:
            relax(d,par,T[u],v,c)
    
    return par

G=[[(1,1),(2,2)],[(2,3),(4,-5)],[],[],[(3,-1),(6,-8)],[(4,0)],[]]
G2=[[(1,-5)],[],[(0,-1),(3,4)],[(1,2),(4,-3)],[(5,7)],[],[(4,-2),(0,1)]]
print(spath_dag(G,0))

    
