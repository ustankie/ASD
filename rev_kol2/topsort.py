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

G=[[1,2],[2,4],[],[],[3,6],[4],[]]
G2=[[1],[],[0,3],[1,4],[5],[],[4,0]]
print(topsort(G2))
