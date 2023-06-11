from queue import PriorityQueue
def relax(par,d,u,v,c):
    if d[v]>d[u]+c:
        d[v]=d[u]+c
        par[v]=u
        return True
    return False
    
def bf(G,s,t,a):
    n=len(G)

    par=[None for _ in range(n)]
    d=[float('inf') for _ in range(n)]

    Q=PriorityQueue()

    d[s]=0
    Q.put((d[s],s,a))


    while not Q.empty():
        c,u,os=Q.get()
        if d[u]==c:
            for v,k in G[u]:
                if os==0:
                    if relax(par,d,u,v,k):
                        Q.put((d[v],v,(os+1)%2))
                else:
                    d[v]=min(d[u],d[v])
                    Q.put((d[v],v,(os+1)%2))

                
    return d[t]

def bob(G,s,t):
    a=bf(G,s,t,0)
    b=bf(G,s,t,1)
    if a>b:
        return "B",b
    return "A",a

def directed_weighted_graph_list(E: 'array of edges'):
    # Find a number of vertices
    n = 0
    for e in E:
        n = max(n, e[0], e[1])
    n += 1
    # Create a graph
    G = [[] for _ in range(n)]
    for e in E:
        G[e[0]].append((e[1], e[2]))
    return G


G=[[(1,1),(5,3),(4,2)],[(2,5),(0,1),(4,8)],[(1,5),(4,10),(3,11)],[(2,11),(7,10)],[(1,8),(2,10),(0,2)],[(0,3),(6,15)],[(5,15),(7,9)],[(3,10),(6,7)]]
s=9
t=2
E = [(0, 1, 8), (0, 2, 15), (0, 5, 12), (0, 10, 10), (0, 12, 30), (1, 4, 15), (1, 2, 4), (2, 3, 7), (3, 1, 10), 
     (3, 4, 13), (4, 7, 14), (5, 6, 20), (5, 3, 18), (6, 4, 11), (6, 7, 8), (8, 7, 4), (9, 8, 12), (10, 5, 19),
     (10, 11, 25), (10, 7, 10), (11, 9, 60), (12, 11, 32), (9, 10, 25)]

G=directed_weighted_graph_list(E)
print(bob(G,s,t))
