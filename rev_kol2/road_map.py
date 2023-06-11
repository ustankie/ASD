from queue import PriorityQueue
def road_map(G,s,t):
    n=len(G)
    vis=[False for _ in range(n)]
    par=[None for _ in range(n)]
    d=[0 for _ in range(n)]

    Q=PriorityQueue()
    Q.put((0,s))

    while not Q.empty():
        c,u=Q.get()
        for v in range(n):
            if G[u][v]>=0 and not vis[v]:
                vis[v]=True
                par[v]=u
                d[v]=d[u]+G[u][v]
                Q.put((G[u][v],v))
            elif G[u][v]>=0 and d[u]+G[u][v]<d[v]:
                par[v]=u
                d[v]=d[u]+G[u][v]
                Q.put((G[u][v],v))
    T=[]
    p=t
    while p!=s:
        T.append(p)
        p=par[p]
    T.append(s)
    return T[::-1]


G=[[-1,1,-1,1,0,-1,1],[1,-1,1,-1,-1,-1,-1],[-1,1,-1,-1,-1,-1,-1],[1,-1,-1,-1,-1,0,1],[0,-1,-1,-1,-1,0,-1],[-1,-1,-1,0,0,-1,0],[1,-1,-1,1,-1,0,-1]]
print(road_map(G,0,6))