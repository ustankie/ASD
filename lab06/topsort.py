def topsort(G):
    def DFS(G,u):
        vis[u]=True
        for v in G[u]:
            if not vis[v]:
                vis[v]=True
                DFS(G,v)
        T.append(u)
        #print(T)
    n=len(G)
    vis=[False for _ in range(n)]
    T=[]
    #vis[0]=True
    for u in range(n):
        if not vis[u]:
            DFS(G,u)
    #print(T)
    T.reverse()
    return T

G=[[1,2],[2,4],[],[],[3,6],[4],[]]
G2=[[1],[],[0,3],[1,4],[5],[],[4,0]]
print(topsort(G2))