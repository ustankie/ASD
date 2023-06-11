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
def floyd(G):
    n=len(G)
    S=[[float('inf')for _ in range(n)]for _ in range(n)]
    for u in range(n):
        for v in range(n):
            if G[u][v]:
                S[u][v]=1
        S[u][u]=0
    
    for t in range(n):
        for u in range(n):
            for v in range(n):
                S[u][v]=min(S[u][v],S[u][t]+S[t][v])
    return S

def merge(T1,T2):
    n1=len(T1)
    n2=len(T2)
    T=[0 for _ in range(n1+n2)]
    i=0
    j=0
    while i<n1 and j<n2:
        if T1[i][2]>T2[j][2]:
            T[i+j]=T2[j]
            j+=1
        else:
            T[i+j]=T1[i]
            i+=1
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
    T1=T[:n//2]
    T2=T[n//2:]
    return merge(merge_sort(T1),merge_sort(T2))

def kruskal(E,n):
    m=len(E)
    V=[Node(i) for i in range(n)]
    cost=0
    A=[]

    for e in E:
        u,v,c=e
        if findset(V[u])!=findset(V[v]):
            union(V[u],V[v])
            cost+=c
            A.append((u,v))
    return cost,A
def make_edges(S,K):
    n=len(K)
    E=[]
    for i in range(n-1):
        for j in range(i+1,n):
            E.append((K[i],K[j],S[K[i]][K[j]]))
    E=merge_sort(E)
    return E
def delivery(G,K):
    n=len(G)
    S=floyd(G)
    #print(*S,sep="\n")
    for i in range(n):
        for j in range(n):
            if G[i][j]:
    E=make_edges(S,K)
    #print(E)
    return kruskal(E,len(S))

def findbiggest(E):
    biggest=0
    for u,v in E:
        biggest=max(biggest,u,v)
    return biggest
def make_graph(E):
    n=findbiggest(E)+1
    G=[[0 for _ in range(n)]for _ in range(n)]
    for u,v in E:
        while (len(G)-1)<u or len(G)-1<v:
            G.append([])
        G[u][v]=1
        G[v][u]=1
    return G
E = [(0, 1), (1, 2), (1, 3), (3, 4), (4, 5), (5, 6), (4, 7), (7, 10), (10, 11), (11, 12), (11, 13), 
     (10, 14), (7, 8), (8, 9), (7, 15), (15, 16), (15, 18), (17, 18), (15, 19), (15, 20), (20, 21),
     (20, 22), (22, 23), (22, 24), (20, 25), (25, 26), (25, 27), (27, 28), (28, 29), (28, 30)]
C = [3, 5, 13, 14, 16, 15, 17, 23, 24, 25, 27, 30]
        
G=make_graph(E)
#print(*G,sep="\n")  
cost,A=delivery(G,C)
print(A)
print(cost)
