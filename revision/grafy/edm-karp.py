from collections import deque
def BFS(G,F,s,t):
    n=len(G)
    min_cap=[float('inf') for i in range(n)]
    vis=[False for _ in range(n)]
    par=[None for _ in range(n)]
    
    Q=deque()
    Q.append(s)

    while len(Q)>0:
        u=Q.popleft()
        for v in range(n):
            if G[u][v]:
                c=G[u][v]-F[u][v]
                if c>0 and not vis[v]:
                    vis[v]=True
                    par[v]=u
                    min_cap[v]=min(c,min_cap[u])
                    if v==t:
                        return True,par,min_cap[t]
                    Q.append(v)
    return False,par,0

def flow(G,s,t):
    n=len(G)
    max_flow=0
    F=[[0 for _ in range(n)]for _ in range(n)]
    augm,par,min_cap=BFS(G,F,s,t)

    while augm:
        p=t
        while p!=s:
            F[p][par[p]]=min_cap
            F[par[p]][p]+=min_cap
            p=par[p]
        max_flow+=min_cap
        augm,par,min_cap=BFS(G,F,s,t)
    
    R=[]
    for u in range(n):
        for v in range(n):
            if G[u][v]:
                R.append(((u,v),F[u][v],G[u][v]))
    return max_flow,R

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
#print(flow(G,s,t))
M2=[[[5, 1, 0], [6, 1, 0], [8, 1, 0], [10, 0, 0]],
[[7, 1, 0], [9, 1, 0], [10, 0, 0]],
[[5, 1, 0], [7, 1, 0], [10, 0, 0]],
[[8, 1, 0], [10, 0, 0]],
[[7, 1, 0], [8, 1, 0], [10, 0, 0]],
[[0, 0, 0], [2, 0, 0], [11, 1, 0]],
[[0, 0, 0], [11, 1, 0]],
[[1, 0, 0], [2, 0, 0], [4, 0, 0], [11, 1, 0]],
[[0, 0, 0], [3, 0, 0], [4, 0, 0], [11, 1, 0]],
[[1, 0, 0], [11, 1, 0]],
[[0, 1, 0], [1, 1, 0], [2, 1, 0], [3, 1, 0], [4, 1, 0]],
[[5, 0, 0], [6, 0, 0], [7, 0, 0], [8, 0, 0], [9, 0, 0]]]
G2=[[[1,7],[3,3]],[[3,4],[4,6]],[[0,9],[5,9]],[[6,2],[4,9]],[],[[3,3],[6,6]],[[4,8]]]
#print(flow2(M2,10,11))
print(flow(M,10,11))