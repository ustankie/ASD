from math import log10,e
from queue import PriorityQueue

def relax(d,par,u,v,c):
    #print(d[v],d[u],c)
    if d[v]>d[u]+c:
        d[v]=d[u]+c
        par[v]=u
        return True
    
    return False

def log_path(G,s,t):
    n=len(G)
    d=[float('inf') for _ in range(n)]
    par=[None for _ in range(n)]

    d[s]=0
    for i in range(n):
        b=False
        for u in range(n):
            for v,c in G[u]:
                b= relax(d,par,u,v,log10(c)) or b
            #print(d,u)
        if not b:                   
            #print(d)
            R=[]
            p=t
            while p!=None:
                R.append(p)
                p=par[p]
            return R[::-1],int(10**d[t]+0.5)
    if b:
        #print(d)
        R=[]
        p=t
        while p!=None:
            R.append(p)
            p=par[p]
        return R[::-1],int(10**d[t]+0.5)
    #print(d)
    return [],float('inf')



def undirected_weighted_graph_list(E):
    n = 0
    for e in E:
        n = max(n, e[0], e[1])
    n += 1
    G = [[] for _ in range(n)]
    for e in E:
        G[e[0]].append((e[1], e[2]))
        G[e[1]].append((e[0], e[2]))
    return G


             
E = [(0, 2, 1), (0, 1, 5), (0, 3, 8), (1, 3, 1), (2, 3, 8), (2, 6, 8), (6, 3, 1), (1, 5, 8),
     (3, 4, 5), (4, 5, 1), (6, 5, 5)]

G = undirected_weighted_graph_list(E)
print(G)
print(log_path(G,5,1))