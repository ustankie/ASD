#from topsort import topsort
def topsort(G):
    def DFS(u):
        for v in G[u]:
            if not vis[v]:
                vis[v]=True
                DFS(v)
        T.append(u)

    n=len(G)
    vis=[False for _ in range(n)]
    T=[]

    for u in range(n):
        if not vis[u]:
            vis[u]=True
            DFS(u)
    return T[::-1]
def hamilton(G):
    T=topsort(G)
    n=len(T)
    for i in range(n-1):
        u=T[i]
        v=T[i+1]
        if not v in G[u]:
            return None
    return T
G=[[1,2],[3,5],[],[2,4],[2],[3,4]]
print(hamilton(G))