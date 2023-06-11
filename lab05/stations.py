from collections import deque

def consistent(G):
    n=len(G)
    vis=[False for i in range(n)]
    T=deque()

    Q=deque()
    Q.append(2)
    vis[2]=True

    while (len(Q)>0):
        u=Q.popleft()
        for v in G[u]:
            if not vis[v]:
                vis[v]=True
                Q.append(v)
        T.append(u)
    
    return T






G=[[1],[0,5,6],[3,4,5],[6,5,2],[2],[1,2,3],[3,1]]
G2=[[4,5],[2,3],[1,4,3],[1,2,4],[2,3,5,0],[0,4]]
print(consistent(G2))