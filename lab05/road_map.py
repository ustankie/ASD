from queue import PriorityQueue
from collections import deque

def map(G,s,k):
    n=len(G)
    vis=[False for _ in range(n)]
    par=[None for _ in range(n)]
    D=[0 for _ in range(n)]

    Q=PriorityQueue()
    Q.put((0,s))

    while not Q.empty():
        c,u=Q.get()
        print(Q.queue)

        for v in range(n):
            if G[u][v]>=0 and not vis[v]:
                vis[v]=True
                par[v]=u
                D[v]=D[u]+G[u][v]
                Q.put((G[u][v],v))
            
            elif G[u][v]>=0 and D[u]+G[u][v]<D[v]:
                par[v]=u
                D[v]=D[u]+G[u][v]
                Q.put((G[u][v],v))
        print(Q.queue)
        print()
    p=k
    T=deque()
    while par[p]!=s:
        T.append(p)
        p=par[p]
    T.append(p)
    T.append(s)
    return reverse(T),D[k]

def reverse(T):
    n=len(T)
    for i in range(n//2):
        T[i],T[n-i-1]=T[n-1-i],T[i]
    return T

G=[[-1,1,-1,1,0,-1,1],[1,-1,1,-1,-1,-1,-1],[-1,1,-1,-1,-1,-1,-1],[1,-1,-1,-1,-1,0,1],[0,-1,-1,-1,-1,0,-1],[-1,-1,-1,0,0,-1,0],[1,-1,-1,1,-1,0,-1]]
print(map(G,0,6))