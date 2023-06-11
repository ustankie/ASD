def good_beginning(G):
    def DFS(G,u,time):
        vis[u]=time
        for v in G[u]:
            if not vis[v]:
                DFS(G,v,time)
    n=len(G)
    vis=[False for _ in range(n)]

    last=0
    time=1
    for u in range(n):
        if not vis[u]:
            DFS(G,u,time)
            time+=1
            last=u
    l=last
    vis=[False for _ in range(n)]
    DFS(G,last,time)

    for u in range(n):
        if not vis[u]:
            return False, None
    return True, l

G=[[1,2],[2,4],[],[],[3,6,5],[],[]]
G2=[[]]
print(good_beginning(G))