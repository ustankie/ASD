from collections import deque
from math import ceil
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
    if x.rank>y.rank:
        y.par=x
    else:
        x.par=y
        if x.rank==y.rank:
            y.rank+=1 
def partition(T,l,r):
    x=T[r][2]
    i=l-1
    for j in range(l,r):
        if T[j][2]>x:
            i+=1
            T[i],T[j]=T[j],T[i]
    i+=1
    T[i],T[r]=T[r],T[i]
    return i
def quicksort(T,l,r):
    while l<r:
        q=partition(T,l,r)
        if q-l>r-q:
            quicksort(T,q+1,r)
            r=q-1
        else:
            quicksort(T,l,q-1)
            l=q+1

def findbiggest(E):
    m=len(E)
    max_ind=0
    for u in range(m):
        max_ind=max(max_ind,E[u][0],E[u][1])
    return max_ind


def edges_to_list(E):
    n=findbiggest(E)
    G=[[] for _ in range(n+1)]
    for u,v,c in E:
        G[u].append((v,c))
        G[v].append((v,c))

    return G
def BFS(G,s,t):
    n=len(G)
    vis=[False for _ in range(n)]
    par=[(None,None) for _ in range(n)]

    vis[s]=True
    Q=deque()
    Q.append((s,0))

    while len(Q)>0:
        u,c=Q.popleft()
        for v,k in G[u]:
            if not vis[v]:
                vis[v]=True
                par[v]=(u,k)
                if v==t:
                    return par
                Q.append((v,k))
    return par
def guide(E,s,t,num):
    m=len(E)
    quicksort(E,0,m-1)
    n=findbiggest(E)
    V=[Node(i) for i in range(n+1)]
    A=[]

    for e in E:
        u,v,c=e
        if findset(V[u])!=findset(V[v]):
            union(V[u],V[v])
            A.append(e)
    G=edges_to_list(A)
    #print(*G,sep="\n")
    par=BFS(G,s,t)
    #print(par)
    T=[]
    p=t
    k=float('inf')
    min_c=float('inf')
    while p!=None:
        T.append(p)
        min_c=min(min_c,k)
        p,k=par[p]

    return T[::-1],ceil(num/min_c)
    
C = [(0, 1, 8), (0, 2, 15), (0, 5, 12), (0, 10, 10), (0, 12, 30), (1, 4, 15), (1, 2, 4), (2, 3, 7), (3, 1, 10), 
     (3, 4, 13), (4, 7, 14), (5, 6, 20), (5, 3, 18), (6, 4, 11), (6, 7, 8), (8, 7, 4), (9, 8, 12), (10, 5, 19),
     (10, 11, 25), (10, 7, 10), (11, 9, 60), (12, 11, 32), (9, 10, 25)]
#G3=[[(1,8),]]
num_tourists = 100
s = 0
t = 3
print(guide(C, s, t, num_tourists))