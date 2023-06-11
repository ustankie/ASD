from collections import deque
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
    pointer=0

    min_diff=float('inf')
    A1=A[:]

    l=0
    r=0

    while l<=r and r<m:
        r=l
        while r<m and not is_cons(V,n):   
            e=E[r]
            u,v,c=e
            if findset(V[u])!=findset(V[v]):
                union(V[u],V[v])
                A.append(e)
            #print(A)
            r+=1

        k=len(A)
        if r<m:
            #print("cons:",A)
            
            min_diff=min(A[k-1][2]-A[pointer][2],min_diff)
            A1=A[pointer:]

            while l<=r and is_cons(V,n):
                pointer+=1

                V=[Node(i) for i in range(n)]

                for i in range(pointer,k):
                    u,v,c=A[i]
                    union(V[u],V[v])

                l+=1

        if is_cons(V,n):
            k=len(A)
            min_diff=min(A[k-1][2]-A[pointer][2],min_diff)
            A1=A[pointer:]
    return min_diff,A1


G=[[(1,1),(6,2)],[(0,1),(2,3),(4,3)],[(1,3),(5,5)],[(4,3),(7,1),(8,8)],[(1,3),(5,2),(3,3),(6,1)],[(2,5),(4,2),(8,1)],[(0,2),(4,1),(7,7)],[(6,7),(3,1)],[(3,8),(5,1)]]

G2=[[(1,1),(2,3)],[(0,1),(4,8),(3,5)],[(0,3),(3,4),(5,6)],[(2,4),(1,5),(4,7),(5,2)],[(1,8),(3,7)],[(2,6),(3,2)]]
print(highway(G))
