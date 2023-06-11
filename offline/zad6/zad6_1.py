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
def convert(M):
    n=len(M)
    m=findbiggest(M)+1
    G=[[0 for _ in range(m+n+2)]for _ in range(m+n+2)]
    for p in range(n):
        for q in M[p]:
            G[p][q+n]=1
    
    for i in range(n):
        G[m+n][i]=len(M[i])
        
    for i in range(m):
        G[i+n][m+n+1]=1
    return G
def convert2(G):
    m=findbiggest(G)+1
    n=len(G)
    F=[[]for _ in range(n+m)]
    for u in range(n):
        for v in range(len(G[u])):
            G[u][v]=G[u][v]+n
            F[u].append(0)
    for i in range(m):
        G.append([n+m+1])
        F[i+n].append(0)
    G.append([i for i in range(n)])
    F.append([0 for i in range(n)])
    G.append([])
    F.append([])
    return G,F
def BFS2(G,F,s,t):
    n=len(G)

    vis=[False for _ in range(n)]
    par=[None for _ in range(n)]

    Q=deque()
    Q.append(s)
    vis[s]=True

    while len(Q)>0:
        u=Q.popleft()
        for i in range(len(G[u])):
            v=G[u][i]
            if u==s:
                c=len(G[v])
            else:
                c=1              
            if not vis[v] and c-F[u][i]>0:                    
                vis[v]=True
                par[v]=u

                if v==t:
                    return True,par
                Q.append(v)
    return False,par

def binworker2(M):
    G,F=convert2(M)
    #print(*G,sep="\n")
    #print(F)
    n=len(G)
    max_flow=0
    s=n-2
    t=n-1

    augm,par=BFS2(G,F,s,t)
    while augm:
        p=t
        while p!=s:
            m=len(G[par[p]])
            for i in range(m):
                v = G[par[p]][i]
                if v==p:
                    F[par[p]][i]+=1
            p=par[p]
        max_flow+=1
        augm,par=BFS2(G,F,s,t)
    return max_flow

def BFS(G,F,s,t):
    n=len(G)

    vis=[False for _ in range(n)]
    par=[None for _ in range(n)]

    Q=deque()
    Q.append(s)
    vis[s]=True

    while len(Q)>0:
        u=Q.popleft()
        for v in range(n):
            if (G[u][v]-F[u][v])>0 and not vis[v]:
                vis[v]=True
                par[v]=u
                if v==t:
                    return True,par
                Q.append(v)
    return False,par

def binworker( M ):
    G=convert(M)
    #print(*G,sep="\n")
    n=len(G)
    F=[[0 for _ in range(n)]for _ in range(n)]
    max_flow=0

    s=n-2
    t=n-1
    is_path,par=BFS(G,F,s,t)
    
    while is_path:
        #print(par)
        p=t
        while p!=s:
            F[par[p]][p]+=1
            F[p][par[p]]=1
            p=par[p]
        max_flow+=1
        is_path,par=BFS(G,F,s,t)
    return max_flow


    

# zmien all_tests na True zeby uruchomic wszystkie testy
runtests( binworker2, all_tests = False )

M = [ [ 0, 1, 3], # 0
[ 2, 4], # 1
[ 0, 2], # 2
[ 3 ], # 3
[ 3, 2] ] # 4
M2=[[0, 1], [0, 1], [0]]
print(binworker2(M))