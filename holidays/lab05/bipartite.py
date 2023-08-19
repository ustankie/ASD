from collections import deque
def bipartite(G):
    n=len(G)
    d=[None for _ in range(n)]
    d[0]=0
    Q=deque()
    Q.append(0)
    while len(Q)>0:
        u=Q.popleft()
        for v in G[u]:
            if d[v]==None:
                d[v]=d[u]+1
                Q.append(v)
            elif d[v]%2==d[u]%2:
                return False
    return True

def bipartite2(G):
    n = len(G)
    vis = [None for _ in range(n)]

    def DFS(G, u):
        for v in G[u]:
            if vis[v]==None:
                vis[v] = 1-vis[u]
                a=DFS(G, v)
                if not a:
                    return False
            elif vis[v]==vis[u]:
                return False
        return True

    for u in range(n):
        if vis[u]==None:
            vis[u]=0
            if not DFS(G, u):
                return False

    return True

G=[[1,3,5],[0,2,4],[1,3,5],[0,2,4],[1,3,5],[4,3]]

print(bipartite2(G))