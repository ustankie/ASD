
def strong(G):
    def DFS(G,u,b,vis):
        nonlocal t
        for v in G[u]:
            if not vis[v]:
                vis[v]=True
                DFS(G,v,b,vis)
        t+=1
        time[u]=t
        T[b].append(u)

    n=len(G)
    t=1
    time=[None for _ in range(n)]
    vis=[False for _ in range(n)]
    T=[[]]
    b=0
    
    for u in range(n):
        if not vis[u]:
            vis[u]=True
            DFS(G,u,b,vis)

    G1=[[] for _ in range(n)]
    vis=[False for _ in range(n)]

    for u in range(n):
        for v in G[u]:
            G1[v].append(u)
    ind=[v for v in range(n)]
    
    for i in range(n):
        for j in range(i+1,n):
            if time[i]<time[j]:
                time[i],time[j]=time[j],time[i]
                ind[i],ind[j]=ind[j],ind[i]

    T=[]
    for u in ind:       
        if not vis[u]:
            T.append([])
            DFS(G1,u,b,vis)       
            b+=1
    return T
G=[[1],[2],[0,3,7],[5],[3],[6],[4,7],[10,8],[9],[7],[9]]
print(strong(G))

