from kol3btesty import runtests
from queue import PriorityQueue

def relax(d,par,u,v,c):
    if d[v]>d[u]+c:
        d[v]=d[u]+c
        par[v]=u
        return True
    return False

def airports( G, A, s, t ):
    n=len(G)

    d=[float('inf') for _ in range(n)]
    par=[None for _ in range(n)]

    d[s]=0

    Q=PriorityQueue()
    Q.put((0,s))

    while not Q.empty():
        c,u=Q.get()
        if c==d[u]:
            for v,c in G[u]:
                if relax(d,par,u,v,c):
                    Q.put((d[v],v))
            for v in range(n):
                if v!=u and relax(d,par,u,v,A[u]+A[v]):
                    Q.put((d[v],v))
    return d[t]


# zmien all_tests na True zeby uruchomic wszystkie testy
runtests( airports, all_tests = False )