def descent(G,s,t):
    def DFS(u,c):
        for v in range(n):
            if G[u][v] and G[u][v]<c:              
                par[v]=u
                DFS(v,G[u][v])
                if v==t:
                    return
    n=len(G)
    par=[None for _ in range(n)]

    DFS(s,float('inf'))

    T=[]
    cost=0
    p=t
    while p!=s:
        T.append(p)
        cost+=G[par[p]][p]
        p=par[p]
    T.append(s)
    return T[::-1],cost

G=[
    [0,1,0,3,4,0,0],
    [1,0,1,0,0,0,0],
    [0,1,0,0,0,0,0],
    [3,0,0,0,0,2,2],
    [4,0,0,0,0,2,0],
    [0,0,0,2,2,0,1],
    [0,0,0,2,0,1,0]
    ]
print(descent(G,0,6))