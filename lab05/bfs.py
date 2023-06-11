from collections import deque

def BFS(G,s):
    n=len(G)
    visited=[False for v in range(n)]
    parent=[None for v in range(n)]
    val=[None for v in range(n)]

    val[s]=0
    visited[s]=True

    Q=deque()
    Q.append(s)

    while (len(Q)>0):
        u=Q.popleft()
        for v in G[u]:
            if not visited[v]:
                visited[v]=True
                val[v]=val[u]+1
                parent[v]=u
                Q.append(v)
    return parent,visited,val

def BFS2(G,s):
    n=len(G)
    visited=[False for v in range(n)]
    parent=[None for v in range(n)]
    val=[None for v in range(n)]

    val[s]=0
    visited[s]=True

    Q=deque()
    Q.append(s)

    while (len(Q)>0):
        u=Q.popleft()
        for v in range(n):
            if G[u][v]:
                if not visited[v]:
                    visited[v]=True
                    val[v]=val[u]+1
                    parent[v]=u
                    Q.append(v)
    return parent,visited,val


G=[[1],[0,5,6],[3,4,5],[6,5,2],[2],[1,2,3],[3,1]]
print(BFS(G,0))

G2=[[0,1,0,0,0,0,0],[1,0,0,0,0,1,1],[0,0,0,1,1,1,0],[0,0,1,0,0,1,1],[0,0,1,0,0,0,0],[0,1,1,1,0,0,0],[0,1,0,1,0,0,0]]
G3=[[0,1,0,0,0,0,0],[1,0,1,0,0,0,0],[0,1,0,1,0,0,0],[0,0,1,0,0,0,1],[0,0,0,0,0,1,1],[0,0,0,0,1,0,1],[0,0,0,1,1,1,0]]

print(BFS2(G3,0))




