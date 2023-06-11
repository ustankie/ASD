#Urszula Stankiewicz, nr albumu: 415668
# Algorytm traktuje listę M jako graf skierowany o krawędziach wagi 1, przy czym wierzchołkami są pracownicy oraz maszyny, a krawędzie są skierowane od pracowników
# do maszyn, które obsługują. Mamy więc do czynienia z problemem wielu źródeł i wielu ujść. Dodajemy zatem do grafu jedno wspólne źródło, które łączymy z pracownikami krawędziami o wadze 1
# oraz wspólne ujście, które łączymy z maszynami krawędziami o wadze 1. Na tak powstałym grafie puszczamy algorytm Edmondsa-Karpa.
# Algorytm jest poprawny, ponieważ każdy pracownik może pracować na jednej maszynie, oraz każda maszyna może być obsługiwana przez jednego pracownika, 
# co odpowiada opisanej reprezentacji grafowej. Wystarczy więc, że znajdziemy w tym grafie maksymalny przepływ.
# Algorytm ma złożoność O((P+m)*(P+m+E)^2) gdzie P - liczba pracowników, m - liczba maszyn, E - liczba krawędzi w liście M
from zad6testy import runtests
from collections import deque

def findbiggest(M):
    n=len(M)
    biggest=0
    for p in range(n):
        for m in M[p]:
            biggest=max(biggest,m)
    #print(biggest)
    return biggest
def merge(T1,T2):
    n1=len(T1)
    n2=len(T2)
    T=[0 for _ in range(n1+n2)]

    i=0
    j=0
    while i<n1 and j<n2:
        if T1[i][0]<T2[j][0]:
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
    T1=T[:n//2]
    T2=T[n//2:]
    return merge(merge_sort(T1),merge_sort(T2))
    
def convert(G):
    m=findbiggest(G)+1
    n=len(G)
    for i in range(m):
        G.append([[n+m+1,1]])    
    G.append([[i,1] for i in range(n)])
    G.append([[i,0]for i in range(n,m+n)])
    for u in range(n):
        for v in range(len(G[u])):
            G[G[u][v]+n].append([u,0])
            G[u][v]=[G[u][v]+n,1]
        G[u].append([n+m,0])      
    for u in range(n+m):
        G[u]=merge_sort(G[u])
    return G

def BFS(G,s,t):
    n=len(G)

    vis=[False for _ in range(n)]
    par=[None for _ in range(n)]

    Q=deque()
    Q.append(s)
    vis[s]=True

    while len(Q)>0:
        u=Q.popleft()
        for el in G[u]:
            v,c=el         
            if not vis[v] and c:                  
                vis[v]=True
                par[v]=u
                if v==t:
                    return True,par
                Q.append(v)
    return False,par
def binsearch(G,el):
    n=len(G)
    i=0
    j=n-1
    q=(i+j)//2
    while i<j:
        q=(i+j)//2
        if G[q][0]==el:
            return q
        if G[q][0]>el:
            j=q-1
        else:
            i=q+1
    return i
        
def binworker(M):
    G=convert(M)
    #print(*G,sep="\n")
    n=len(G)
    max_flow=0
    s=n-2
    t=n-1

    augm,par=BFS(G,s,t)
    
    while augm:
        p=t
        while p!=s:
            m=len(G[par[p]])
            i=binsearch(G[par[p]],p)
            G[par[p]][i][1]-=1
            j=binsearch(G[p],par[p])
            G[p][j][1]+=1          
            p=par[p]
        max_flow+=1
        augm,par=BFS(G,s,t)

    return max_flow

    

# zmien all_tests na True zeby uruchomic wszystkie testy
runtests( binworker, all_tests = False )

M = [ [ 0, 1, 3], # 0
[ 2, 4], # 1
[ 0, 2], # 2
[ 3 ], # 3
[ 3, 2] ] # 4
M2=[[0, 1], [0, 1], [0]]
#print(binworker(M))