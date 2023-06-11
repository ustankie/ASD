def bridges(G):
    def DFS(G,u):
        nonlocal t
        time[u]=t
        t+=1
        low[u]=min(low[u],time[u])
        for v in G[u]:
            if not vis[v]:
                vis[v]=True
                par[v]=u                
                DFS(G,v)
                low[u]=min(low[u],low[v])
            elif v!=par[u]:
                low[u]=min(low[u],time[v])

    n=len(G)
    t=0
    time=[0 for _ in range(n)]
    vis=[False for _ in range(n)]
    low=[float('inf') for _ in range(n)]
    par=[None for _ in range(n)]

    for u in range(n):
        if not vis[u]:
            vis[u]=True
            DFS(G,u)
    print(low)
    print(time)
    E=[]
    for u in range(1,n):
        if low[u]==time[u]:
            E.append((par[u],u))
    return E

G=[[1,3],[0,2],[1,5,3],[0,2,4],[3],[2,7,6],[5,7],[6,5]]
print(bridges(G))