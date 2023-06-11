from collections import deque
from queue import PriorityQueue
def transform(G):
    n=len(G)
    neighbour=[(-1,-1),(0,-1),(1,-1),(-1,0),(1,0),(-1,1),(0,1),(1,1)]

    G2=[[] for _ in range(n*n)]
    for i in range(n):
        for j in range(n):
            for u,v in neighbour:
                u=u+i
                v=v+j
                if u>=0 and u<n and v>=0 and v<n:
                    a=i*n+j
                    c=u*n+v
                    if G[u][v]==1:
                        G2[a].append(c)
                    else:
                        b=len(G2)
                        for k in range(G[u][v]-1):
                            G2[a].append(b)
                            G2.append([])
                            a=b
                            b+=1
                        b-=1
                        G2[b].append(c)

    return G2


def king(G):
    n=len(G)
    G2=transform(G)
    m=len(G2)
    par=[None for _ in range(m)]
    vis=[False for _ in range(m)]
    d=[float('inf') for _ in range(m)]

    Q=deque()
    Q.append(0)
    t=n*n-1

    vis[0]=True
    d[0]=G[0][0]
    while len(Q)>0:
        u=Q.popleft()
        for v in G2[u]:
            if not vis[v]:
                vis[v]=True
                d[v]=d[u]+1
                par[v]=u
                if v==t:
                    T=[]
                    #print(d)
                    p=t
                    while p!=None:
                        if p//n<=n and p%n<=n:
                            T.append((p//n,p%n))
                        p=par[p]
                    return T[::-1],d[t]
                Q.append(v)
    # T=[]
    # if v==t:
        
    #     #print(d)
    #     p=t
    #     while p!=None:
    #         T.append((p//n,p%n))
    #         p=par[p]
    # return T[::-1],d[t]


G=[


[5, 1, 5, 5, 1, 3, 4, 5, 1, 4, 5, 3],
[4, 4, 4, 2, 1, 1, 4, 1, 5, 3, 3, 4],
[5, 5, 3, 5, 1, 5, 5, 2, 5, 4, 1, 1],
[1, 5, 3, 1, 5, 2, 1, 3, 3, 5, 2, 1],
[1, 2, 3, 2, 5, 3, 5, 1, 3, 3, 2, 4],
[2, 2, 3, 5, 1, 4, 4, 1, 5, 1, 3, 2],
[1, 4, 2, 3, 3, 1, 1, 2, 1, 5, 2, 5],
[2, 5, 3, 4, 1, 5, 2, 5, 3, 2, 2, 1],
[2, 4, 5, 5, 5, 1, 3, 3, 1, 5, 1, 2],
[2, 4, 4, 3, 1, 2, 1, 3, 1, 2, 2, 4],
[5, 4, 3, 5, 3, 5, 1, 5, 2, 3, 1, 3],
[5, 5, 1, 3, 5, 4, 2, 3, 5, 3, 2, 3],
]
print(king(G))