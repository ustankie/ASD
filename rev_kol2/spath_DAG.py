from math import inf
def topsort(G):
    def DFS(G,s):
        for v,c in G[s]:
            if not vis[v]:
                vis[v]=True
                DFS(G,v)
        T.append(s)

    n=len(G)

    T=[]
    vis=[False for _ in range(n)]

    for u in range(n):
        if not vis[u]:
            vis[u]=True
            DFS(G,u)
    return T[::-1]

def relax(d,par,u,v,c):
    if d[v]>d[u]+c:
        d[v]=d[u]+c
        par[v]=u
        return True
    return False

def find_pos(T,s):
    for i in range(len(T)):
        if s==T[i]:
            return i
    
def DAG(G,s):
    n=len(G)
    T=topsort(G)
    ind=find_pos(T,s)
    d=[inf for _ in range(n)]   
    par=[None for _ in range(n)]

    d[s]=0
    for u in range(ind,n):
        for v,c in G[T[u]]:
            relax(d,par,T[u],v,c)
    return d,par



G=[[(1,1),(2,2)],[(2,3),(4,-5)],[],[],[(3,-1),(6,-8)],[(4,0)],[]]
G2=[[(1,-5)],[],[(0,-1),(3,4)],[(1,2),(4,-3)],[(5,7)],[],[(4,-2),(0,1)]]
print(DAG(G,0))
