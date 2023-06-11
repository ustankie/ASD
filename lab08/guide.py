from math import ceil
from collections import deque

def merge(T1,T2):
    n1=len(T1)
    n2=len(T2)

    T=[0 for _ in range(n1+n2)]

    i=0
    j=0
    while i<n1 and j<n2:
        if T1[i][2]>T2[j][2]:
            T[i+j]=T1[i]
            i+=1
        else:
            T[i+j]=T2[j]
            j+=1
    while i<n1:
        T[i+j]=T1[i]
        i+=1
    while j<n2:
        T[i+j]=T2[j]
        j+=1  
    return T 
     
def merge_sort(T):
    n=len(T)
    if n==1:
        return T
    
    q=n//2
    T1=T[:q]
    T2=T[q:]

    return merge(merge_sort(T1),merge_sort(T2))

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
        self.par=self
        self.val=val
        self.rank=0

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
        
def transform2(E,n):
    G=[[] for _ in range(n)]

    for u,v,c in E:
        G[u].append((v,c))
        G[v].append((u,c))
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

def find_max(C):
    max_v=0
    for u,v,c in C:
        max_v=max(max_v,u,v)
    return max_v

def guide(G,x,y,t):
    #n=len(G)
    #E=transform(G)
    E=G
    n=find_max(G)+1
    E=merge_sort(E)

    V=[Node(i) for i in range(n)]
    A=[]

    for e in E:
        u,v,c=e
        #print(u,v)
        if findset(V[u])!=findset(V[v]):
            union(V[u],V[v])
            A.append(e)
    
    A=transform2(A,n)

    par=BFS(A,x,y)

    T=[]
    p=y
    k=float('inf')
    min_c=float('inf')
    while p!=None:
        T.append(p)
        min_c=min(min_c,k)
        p,k=par[p]
        
    
    T=T[::-1]
    return T,ceil(t/min_c)







G=[[(1,1),(6,2)],[(0,1),(2,3),(4,3)],[(1,3),(5,5)],[(4,3),(7,1),(8,8)],[(1,3),(5,2),(3,3),(6,1)],[(2,5),(4,2),(8,1)],[(0,2),(4,1),(7,7)],[(6,7),(3,1)],[(3,8),(5,1)]]
G2=[[(1,1),(2,3)],[(0,1),(4,8),(3,5)],[(0,3),(3,4),(5,6)],[(2,4),(1,5),(4,7),(5,2)],[(1,8),(3,7)],[(2,6),(3,2)]]

C = [(0, 1, 8), (0, 2, 15), (0, 5, 12), (0, 10, 10), (0, 12, 30), (1, 4, 15), (1, 2, 4), (2, 3, 7), (3, 1, 10), 
     (3, 4, 13), (4, 7, 14), (5, 6, 20), (5, 3, 18), (6, 4, 11), (6, 7, 8), (8, 7, 4), (9, 8, 12), (10, 5, 19),
     (10, 11, 25), (10, 7, 10), (11, 9, 60), (12, 11, 32), (9, 10, 25)]
#G3=[[(1,8),]]
num_tourists = 50
s = 0
t = 7
print(guide(C, s, t, num_tourists))

