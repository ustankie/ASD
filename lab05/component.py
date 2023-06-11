def component(G):
    def Visit(G,u):
        vis[u]=True
        for v in G[u]:
            if not vis[v]:
                Visit(G,v)


    n=len(G)
    l=0
    vis=[False for _ in range(n)]
    for u in range(n):
        if not vis[u]:
            l+=1
            Visit(G,u)
    return l

G=[[],[2],[1,3],[2],[5,6],[4,6],[4,5],[8],[7],[]]
print(component(G))