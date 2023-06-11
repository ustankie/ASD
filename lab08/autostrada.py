from collections import deque
from queue import PriorityQueue
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
        return findset(x.par)
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

def highway(G):
    n=len(G)

    E=transform(G)

    m=len(E)
    quicksort(E,0,m-1)

    print(E)

    V=[Node(i) for i in range(n)]
    A=deque()

    min_diff=float('inf')

    l=0
    r=0
    #return rek(V,E,l,r,A)
    while l<=r and r<m:
        a=DFS(transform2(A,n))
        r=l
        while r<m and not a:
            e=E[r]
            u,v,c=e
            #W=V[:]
            if findset(V[u])!=findset(V[v]) and not e in A:
                union(V[u],V[v])
                A.append(e)
            print(A)
            r+=1
            a=DFS(transform2(A,n))
        
        if r<m:
            #print(E[r][2],E[l][2])
            min_diff=min(E[r-1][2]-E[l][2],min_diff)
        print(A,l,r,a,min_diff)

        u,v,c=A.popleft()

        deunion(V[u],V[v])
        
        #print(A)
        l+=1

        print(A,l,r)

        if r<m:
            min_diff=min(E[r][2]-E[l-1][2],min_diff)

    return min_diff

def rek(V1,E,l,r,A1):
    n=len(V1)
    m=len(E)
    if r==m-1:
        return E[r][2]-E[l][2]
    V=V1[:]
    A=A1[:]
    if not DFS(transform2(A,n)):
        u,v,c=E[l]
        #W=V[:]
        if findset(V[u])!=findset(V[v]):
            union(V[u],V[v])
            A.append((u,v,c))
            print(A)
        r+=1
        return min(E[r-1][2]-E[l][2],rek(V,E,l,r,A))
    else:
        u,v,c=E[l]
        #W=V[:]
        if findset(V[u])!=findset(V[v]):
            union(V[u],V[v])
            A.append((u,v,c))
            print(A)

        l+=1
        return min(E[r][2]-E[l-1][2],rek(V,E,l,r,A))



    





G2=[[(1,1),(2,3)],[(0,1),(4,8),(3,5)],[(0,3),(3,4),(5,6)],[(2,4),(1,5),(4,7),(5,2)],[(1,8),(3,7)],[(2,6),(3,2)]]
print(highway(G2))
