from collections import deque

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
    R=[]
    for u in range(n):
        for v in range(n):
            if G[u][v]:
                R.append(((u,v),G[u][v],F[u][v]))
    return max_flow,R

def multiple_ff(G,sources,sinks):
    n=len(G)
    G.append([0 for _ in range(n+2)])
    G.append([0 for _ in range(n+2)])

    for i in range(n):
        G[i].append(0)
        G[i].append(0)
    
    s1=len(sources)

    for i in range(s1):
        cap=0
        for j in range(n):
            cap+=G[sources[i]][j]
        G[n][sources[i]]=cap
    
    s2=len(sinks)

    for i in range(s2):
        cap=0
        for j in range(n):
            cap+=G[j][sinks[i]]
        G[sinks[i]][n+1]=cap
    
    return flow(G,n,n+1)

G=[[0,0,0,0,0,2,3,0,0,0,0,0],
   [0,0,0,0,0,3,0,0,0,0,0,0],
   [0,0,0,0,0,4,0,0,0,1,0,0],
   [0,0,0,0,0,0,0,0,0,5,0,0],
   [0,0,0,0,0,0,0,2,0,0,0,5],
   [0,0,0,0,2,0,7,0,0,0,0,0],
   [0,0,0,0,0,0,0,7,0,0,8,0],
   [0,0,0,0,0,8,0,0,0,0,0,0],
   [0,0,0,0,0,0,0,0,0,0,0,0],
   [0,0,0,0,3,0,0,0,4,0,0,0],
   [0,0,0,0,0,0,0,0,0,0,0,0],
   [0,0,0,0,0,0,0,0,0,0,0,0]

   ]

sources=[0,1,2,3]
sinks=[8,10,11]

print(multiple_ff(G,sources,sinks))