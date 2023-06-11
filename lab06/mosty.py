
def bridges(G):
    def DFS(G,u,time,low,par):
        nonlocal t
        t+=1
        time[u]=t
        low[u]=time[u]
        for v in G[u]:        
            if low[v]==0:
                par[v]=u
                
                DFS(G,v,time,low,par)
                low[u]=min(low[u],low[v])
            elif v!=par[u]:
                low[u]=min(low[u],time[v])

    n=len(G)
    low=[0 for _ in range(n)]
    par=[None for _ in range(n)]
    time=[0 for _ in range(n)]
    time[0]=1
    low[0]=1
    t=1
    for u in range(n):
        if not low[u]:
            DFS(G,u,time,low,par)
    T=[]
    for u in range(1,n):
        if low[u]==(time[u]):
            T.append((par[u],u))

    return T

G=[[1,3],[0,2],[1,5,3],[0,2,4],[3],[2,7,6],[5,7],[6,5]]
print(bridges(G))
