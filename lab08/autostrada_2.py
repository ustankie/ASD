def partition(T,p,r):
    x=T[r][2]
    i=p-1
    for j in range(p,r):
        if T[j][2]<x:
            i+=1
            T[i],T[j]=T[j],T[i]
    i+=1
    T[i],T[r]=T[r],T[i]
    return i

def quicksort(T,p,r):
    while p<r:
        q=partition(T,p,r)
        if (r-q)>(q-p):
            quicksort(T,p,q-1)
            p=q+1
        else:
            quicksort(T,q+1,r)
            r=q-1

def transform(G):
    n=len(G)
    E=[]
    for u in range(n):
        for v,c in G[u]:
            if u<v:
                E.append((u,v,c))
    return E

def transform2(E,n):
    m=len(E)
    G=[[]for _ in range(n)]

    for i in range(m):
        G[E[i][0]].append((E[i][1],E[i][2]))
        G[E[i][1]].append((E[i][0],E[i][2]))
    return G


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
def deunion(x,y):
    if x.rank>y.rank:
        y.par=y        
        if x.rank-1==y.rank:
            x.rank-=1
    else:
        x.par=x
        if x.rank==y.rank-1:
            y.rank-=1
def DFS(G):
    def Visit(G,s):
        vis[s]=True
        for v,c in G[s]:
            if not vis[v]:
                Visit(G,v)
    n=len(G)
    if n==0:
        return False
    vis=[False for _ in range(n)]

    for u in range(n):
        if not vis[u]:
            if u!=0:
                return False
            Visit(G,u)
    return True
def is_cons(V,n):
    for u in range(n):
        for v in range(n):
            if findset(V[u])!=findset(V[v]):
                return False
    return True
def highway(G):
    n=len(G)

    E=transform(G)

    m=len(E)
    quicksort(E,0,m-1)

    V=[Node(i) for i in range(n)]
    A=[]

    min_diff=float('inf')
    A1=A

    l=0

    while l<m:
        V=[Node(i) for i in range(n)]
        A=[]
        for r in range(l,m):
            e=E[r]
            u,v,c=e
            if findset(V[u])!=findset(V[v]):
                union(V[u],V[v])
                A.append(e)
        if is_cons(V,n):
            k=len(A)
            min_diff=min(A[k-1][2]-A[0][2],min_diff)
            A1=A
        l+=1

    return min_diff,A1



G2=[[(1,1),(2,3)],[(0,1),(4,8),(3,5)],[(0,3),(3,4),(5,6)],[(2,4),(1,5),(4,7),(5,2)],[(1,8),(3,7)],[(2,6),(3,2)]]
print(highway(G2))
