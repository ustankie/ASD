from   queue import PriorityQueue
def relax(par,d,u,v,c):
    if  d[v]>d[u]+c:
        d[v]=d[u]+c
        par[v]=u
        return True
    return False

def descent(G,s,t):
    n=len(G)
    d=[float('inf')for _ in range(n)]
    par=[None for _ in range(n)]

    Q=PriorityQueue()
    Q.put((0,float('inf'),s))
    d[s]=0

    while not Q.empty():
        c,p,u=Q.get()
        if c==d[u]:
            for v,k in G[u]:
                if k<p:
                    print(u,p,k,v)
                if (k<p or u==s) and relax(par,d,u,v,k):
                    print(d)
                    print(u,p,k,v)
                    Q.put((d[v],k,v))
    T=[]
    p=t
    while p!=None:
        T.append(p)
        p=par[p]
    if len(T)<2:
        T=[]
    return d[t],T[::-1]

def undirected_weighted_graph_list(E: 'array of edges'):
    # Find a number of vertices
    n = 0
    for e in E:
        n = max(n, e[0], e[1])
    n += 1
    # Create a graph
    G = [[] for _ in range(n)]
    for e in E:
        G[e[0]].append((e[1], e[2]))
        G[e[1]].append((e[0], e[2]))
    return G

E = [(0, 1, 1), (1, 2, 4), (2, 3, 3), (0, 5, 40), (5, 6, 38), (0, 7, 5), (6, 7, 8), (7, 1, 6),
     (7, 2, 16), (6, 2, 23), (6, 8, 35), (5, 4, 30), (8, 4, 20), (8, 3, 15), (4, 3, 80)]

G = undirected_weighted_graph_list(E)
print(*G,sep="\n")
print(descent(G, 0,3))
