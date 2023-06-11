from collections import deque
def stations(G):
    n=len(G)

    vis=[False for _ in range(n)]
    T=[]

    s=2
    Q=deque()
    Q.append(s)

    vis[s]=True
    while len(Q)>0:
        u=Q.popleft()
        for v in G[u]:
            if not vis[v]:
                vis[v]=True
                Q.append(v)
        T.append(u)
    return T[::-1]


G=[[1],[0,5,6],[3,4,5],[6,5,2],[2],[1,2,3],[3,1]]
G2=[[4,5],[2,3],[1,4,3],[1,2,4],[2,3,5,0],[0,4]]
print(stations(G2))