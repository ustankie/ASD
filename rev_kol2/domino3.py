from collections import deque
class Node():
    def __init__(self,val):
        self.val=val
        self.rank=0
        self.par=self
def findset(x):
    if x!=x.par:
        x.par=findset(x.par)
    return x.par
def union(x,y):
    x=findset(x)
    y=findset(y)

def union(x,y):
    x=findset(x)
    y=findset(y)

    if x.rank>y.rank:
        y.par=x
    else:
        x.par=y
        if x.rank==y.rank:
            y.rank+=1
def transform(D):
    n=len(D)
    G=[]
    for i in range(n):
        a,b=D[i]
        while a>(len(G)-1):
            G.append([])
            #print(a)
        while b>(len(G)-1):
            G.append([])
            #print(b)
        G[a].append(b)
    return G

def reverse(G):
    n=len(G)
    G2=[[]for _ in range(n)]
    for u in range(n):
        for v in G[u]:
            G2[v].append(u)
    return G2

def domino(E):
    G=transform(E)
    n=len(G)
    V=[Node(i) for i in range(n)]

    for u in range(n):
        for v in G[u]:
            if findset(V[u])!=findset(V[u]):
                union(V[u],V[v])
    T=[[]for _ in range(n)]
    for u in range(n):        
        T[(V[u].par).val].append(u)   
    return T


E = [(0, 1), (1, 2), (3, 2), (2, 4), (4, 1), (4, 5), (5, 6), (6, 7), (7, 8), (8, 9), (9, 6),
     (4, 7), (4, 6), (5, 9), (10, 0), (15, 14), (15, 11), (15, 11), (11, 13), (14, 13), (5, 13),
     (16, 8), (0, 12), (12, 3)]
E1 = [(0, 1), (1, 2), (3, 2), (2, 4), (4, 1), (4, 5), (6, 7), (7, 8), (8, 9), (9, 6)]

print(domino(E1))

