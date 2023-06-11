from collections import deque

def cycle(G):
    n=len(G)
    vis=[False for _ in range(n)]
    parent=[None for _ in range(n)]

    Q=deque()
    Q.append(0)
    vis[0]=True

    while (len(Q)>0):
        u=Q.popleft()
        for v in G[u]:
            if not vis[v]:
                Q.append(v)
                vis[v]=True
                parent[v]=u
            #else: return True
            elif parent[u]!=v:
                return True
    return False

G=[[1],[0,5,6],[3,4,5],[6,5,2],[2],[1,2,3],[3,1]]
G2=[[1],[0,2],[1,6,7],[7],[7],[7],[2],[3,4,5,2]]
print(cycle(G2))