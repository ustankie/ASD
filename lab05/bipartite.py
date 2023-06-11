from collections import deque

def bipartite(G):
    n=len(G)
    vis=[-1 for _ in range(n)]

    vis[0]=0
    Q=deque()
    Q.append(0)

    while (len(Q)>0):
        u=Q.popleft()
        for v in G[u]:
            if vis[v]==(-1):
                vis[v]=(vis[u]+1)%2
                Q.append(v)
            elif (vis[v]==vis[u]):
                return False
    return True


G=[[1,3,5],[0,2,4],[1,3,5],[0,2,4],[1,3,5],[4]]
print(bipartite(G))
