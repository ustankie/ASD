def topsort(G):
    n=len(G)
    vis=[False for _ in range(n)]
    R=[]

    def DFS(u):
        vis[u]=True
        for v in G[u]:
            if not vis[v]:
                DFS(v)
        R.append(u)

    for u in range(n):
        if not vis[u]:
            DFS(u)
    return R[::-1]

G=[[1,2],[2,4],[],[],[3,6],[4],[]]
G2=[[1],[],[0,3],[1,4],[5],[],[4,0]]
print(topsort(G))