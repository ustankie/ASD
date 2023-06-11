from queue import PriorityQueue
def relax(d,par,u,v,c):
    if d[v]>d[u]+c:
        d[v]=d[u]+c
        par[v]=u
        return True
    return False
def dijkstra(G,s):
    n=len(G)
    d=[float('inf') for _ in range(n)]
    par=[None for _ in range(n)]

    d[s]=0
    Q=PriorityQueue()
    Q.put((0,s))

    while not Q.empty():
        c,u=Q.get()
        if c==d[u]:
            for v,k in G[u]:
                if relax(d,par,u,v,k):
                    Q.put((d[v],v))
    return d,par
def print_path(par,p):
    T=[]
    while p!=None:
        T.append(p)
        p=par[p]
    T=T[::-1]
    print(T)

def print_path_r(par,p):
    if p!=None:
        print_path_r(par,par[p])
        print(p)

G=[[(1,1),(6,2)],[(0,1),(2,3),(4,3)],[(1,3),(5,5)],[(4,3),(7,1),(8,8)],[(1,3),(5,2),(3,3),(6,1)],[(2,5),(4,2),(8,1)],[(0,2),(4,1),(7,7)],[(6,7),(3,1)],[(3,8),(5,1)]]
d,par=dijkstra(G,0)

print(d,"\n",par)
print_path_r(par,7)
