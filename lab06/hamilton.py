def hamilton(G):
    def DFS(G,u):
        for v in G[u]:
            if not vis[v]:
                vis[v]=True
                DFS(G,v)
        T.append(u)


    n=len(G)
    T=[]
    vis=[False for _ in range(n)]

    for u in range(n):
        if not vis[u]:
            vis[u]=True
            DFS(G,u)

    T.reverse()

    for u in range(n-1):
        if not T[u+1] in G[T[u]]:
            return None
    return T

G=[[1,2],[3,5],[],[2,4],[2],[3,4]]
print(hamilton(G))