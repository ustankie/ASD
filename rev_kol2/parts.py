def parts(G):
    def DFS(u):
        vis[u]=True
        for v in G[u]:
            if not vis[v]:
                DFS(v)
    n=len(G)
    vis=[False for _ in range(n)]
    count=0

    for u in range(n):
        if not vis[u]:
            count+=1
            DFS(u)
    return count

G=[[],[2],[1,3],[2],[5,6],[4,6],[4,5],[8],[7],[]]
print(parts(G))