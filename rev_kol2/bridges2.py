from collections import deque
def bridges(G):
    def DFS(u):
        nonlocal time    
        Q=deque()
        Q.append(u)   
        while len(Q)>0:
            u=Q.pop()
            if not vis[u]:
                vis[u]=True  
            
                d[u]=time
                low[u]=min(low[u],d[u])
                
                time+=1
                for v in G[u]:
                    if not vis[v]:                    
                        par[v]=u
                        Q.append(v)
                    elif v!=par[u]:
                        low[u]=min(low[u],d[v])
                if par[u]!=None:
                    p=u
                    while par[p]!=None and low[par[p]]>low[p]:
                        low[par[p]]=low[p]
                        p=par[p]
    n=len(G)
    time=0
    vis=[False for _ in range(n)]
    d=[0 for _ in range(n)]
    low=[float('inf') for _ in range(n)]
    par=[None for _ in range(n)]

    DFS(0)
    T=[]
    for u in range(1,n):
        if low[u]==d[u]:
            T.append((par[u],u))
    return T

G=[[1,3],[0,2],[1,5,3],[0,2,4],[3],[2,7,6],[5,7],[6,5]]
G2=[[1,2,3],[0,4,5],[0,3],[2,0],[1],[1,6,7],[5,7,8],[5,6,8],[7,6]]
print(bridges(G2))