from collections import deque
from copy import deepcopy

def BFS(G,F,s,t):
    n=len(G)
    min_cap=[float('inf') for _ in range(n)]

    vis=[False for _ in range(n)]
    par=[None for _ in range(n)]

    vis[s]=True
    Q=deque()
    Q.append(s)

    while len(Q)>0:
        u=Q.popleft()
        for v in range(n):
            c=G[u][v]-F[u][v]
            if c>0 and not vis[v]:
                min_cap[v]=min(min_cap[u],c)
                vis[v]=True
                par[v]=u
                if v==t:
                    return True,par,min_cap[t]
                Q.append(v)
    return False,par,0


def flow(G,s,t):
    n=len(G)
    max_flow=0

    F=[[0 for _ in range(n)]for _ in range(n)]

    exists,par,min_cap=BFS(G,F,s,t)
    while exists:
        max_flow+=min_cap
        p=t
        while p!=s:
            F[par[p]][p]+=min_cap
            F[p][par[p]]=min_cap
            p=par[p]
        exists,par,min_cap=BFS(G,F,s,t)
    return max_flow

G=[[0,7,0,3,0,0,0],
   [7,0,0,4,6,0,0],
   [9,0,0,0,0,9,0],
   [3,4,0,0,9,0,2],
   [0,6,0,9,0,0,8],
   [0,0,9,3,0,0,6],
   [0,0,0,2,8,6,0]]

s=2
t=4

print(flow(G,s,t))