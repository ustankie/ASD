from queue import PriorityQueue
def create_graph(E):
    m=len(E)
    max_c=0
    n=0
    for i in range(m):
        n=max(n,E[i][0],E[i][1])
        max_c=max(max_c,E[i][2])
    
    G=[[] for _ in range(n+1)]
    for i in range(m):
        G[E[i][0]].append((E[i][1],E[i][2]))
    
    return G,max_c

def relax(d,par,v,u,c):
    if d[v]<c:
        d[v]=c
        par[v]=u
        return True
    return False

def guide(E,A,B,g):
    m=len(E)
    G,max_c=create_graph(E)
    n=len(G)
    inf=float('inf')

    d=[0 for _ in range(n)]
    par=[None for _ in range(n)]

    Q=PriorityQueue()
    d[A]=inf
    Q.put((max_c-d[A],A))

    while not Q.empty():
        c,u=Q.get()
        c=max_c-c
        if c==d[u]:
            for v,k in G[u]:
                if relax(d,par,v,u,min(d[u],k)):
                    Q.put((max_c-d[v],v))
    
    groups=g/d[B]
    if groups>g//d[B]:
        groups=g//d[B]+1
    else:
        groups=g//d[B]
    
    R=[]
    p=B
    while p!=None:
        R.append(p)
        p=par[p]
    
    return groups,R[::-1]




E=[(0,1,5),(0,2,3),(0,4,1),(1,3,5),(1,2,1),(2,6,3),(3,6,6),(4,6,8),(6,0,5)]   

#print(tourists(E,0,6,20))
C = [(0, 1, 8), (0, 2, 15), (0, 5, 12), (0, 10, 10), (0, 12, 30), (1, 4, 15), (1, 2, 4), (2, 3, 7), (3, 1, 10), 
     (3, 4, 13), (4, 7, 14), (5, 6, 20), (5, 3, 18), (6, 4, 11), (6, 7, 8), (8, 7, 4), (9, 8, 12), (10, 5, 19),
     (10, 11, 25), (10, 7, 10), (11, 9, 60), (12, 11, 32), (9, 10, 25)]

num_tourists = 100
s = 0
t = 3
print(guide(C, s, t, num_tourists))
    
