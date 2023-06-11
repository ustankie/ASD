from collections import deque
from copy import deepcopy

def BFS(G,s,t):
    n=len(G)

    vis=[False for _ in range(n)]
    par=[None for _ in range(n)]

    vis[s]=True
    Q=deque()
    Q.append(s)

    while len(Q)>0:
        u=Q.popleft()
        for v in range(n):
            if G[u][v] and not vis[v]:
                vis[v]=True
                par[v]=u
                if v==t:
                    T=[]
                    p=t
                    while p!=None:
                        T.append(p)
                        p=par[p]
                    return T[::-1]
                Q.append(v)
    T=[]
    p=t
    while p!=None:
        T.append(p)
        p=par[p]
    return T[::-1]

def cap(G,path):
    n=len(path)
    min_cap=G[path[0]][path[1]]
    for i in range(1,n-1):
        min_cap=min(min_cap,G[path[i]][path[i+1]])
    return min_cap

def modify(G,path,min_cap):
    n=len(path)
    for i in range(n-1):
        G[path[i]][path[i+1]]-=min_cap
        G[path[i+1]][path[i]]+=min_cap

def ff(G,s,t):
    n=len(G)
    flow=0

    G=deepcopy(G)
    path=BFS(G,s,t)
    if len(path)==0:
        return None
    
    while len(path)>1:
        min_cap=cap(G,path)
        flow+=min_cap
        modify(G,path,min_cap)
        path=BFS(G,s,t)

    return flow,G



G=[[0,7,0,3,0,0,0],
   [0,0,0,4,6,0,0],
   [9,0,0,0,0,9,0],
   [0,0,0,0,9,0,2],
   [0,0,0,0,0,0,0],
   [0,0,0,3,0,0,6],
   [0,0,0,0,8,0,0]]

s=2
t=4
M=[[0, 0, 0, 0, 0, 1, 1, 0, 1, 0, 0, 0],
[0, 0, 0, 0, 0, 0, 0, 1, 0, 1, 0, 0],
[0, 0, 0, 0, 0, 1, 0, 1, 0, 0, 0, 0],
[0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0],
[0, 0, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0],
[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
[1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0],
[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]]
print(ff(M,10,11))
