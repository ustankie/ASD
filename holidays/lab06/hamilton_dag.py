def hamilton(G):
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
    
    R=R[::-1]

    m=len(R)

    for u in range(m-1):
        if not R[u+1] in G[R[u]]:
            return False,[]
    return True,R

G=[[1,2],[3,5],[],[2,4],[2],[3,4]]
print(hamilton(G))
