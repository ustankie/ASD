from queue import PriorityQueue
def relax(par,d,u,v,k):
    if d[v]>k:
        d[v]=k
        par[v]=u
        return True
    return False
def prim(G,s):
    n=len(G)
    d=[float('inf') for _ in range(n)]
    par=[None for _ in range(n)]
    vis=[False for _ in range(n)]
    d[s]=0

    Q=PriorityQueue()

    Q.put((0,s))

    while not Q.empty():
        c,u=Q.get()
        if not vis[u]:
            vis[u]=True
            for v,k in G[u]:
                if not vis[v] and relax(par,d,u,v,k):
                    Q.put((d[v],v))
    A=[]
    for i in range(n):
        if par[i]!=None:
            A.append((i,par[i]))
    return A

G=[[(1,1),(2,3)],[(0,1),(4,8),(3,5)],[(0,3),(3,4),(5,6)],[(2,4),(1,5),(4,7),(5,2)],[(1,8),(3,7)],[(2,6),(3,2)]]
print(prim(G,1))