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
    for u in range(n):
        for v in range(len(G[u])):
            G[u][v]=[G[u][v]+n,1,0]
    for i in range(m):
        G.append([[n+m+1,1,0]])
    G.append([[i,len(G[i]),0] for i in range(n)])
    G.append([])
    return G
def BFS2(G,s,t):
    n=len(G)

    vis=[False for _ in range(n)]
    par=[None for _ in range(n)]

    Q=deque()
    Q.append(s)
    vis[s]=True

    while len(Q)>0:
        u=Q.popleft()
        for v,c,f in G[u]:
            if c>0:
                cp=c-f
                
                if not vis[v] and cp>0:                    
                    vis[v]=True
                    par[v]=u

                    if v==t:
                        return True,par
                    Q.append(v)
    return False,par

def binworker2(M):
    G=convert2(M)
    n=len(G)
    max_flow=0
    s=n-2
    t=n-1

    augm,par=BFS2(G,s,t)
    while augm:
        p=t
        while p!=s:
            m=len(G[par[p]])
            for i in range(m):
                v,c,f = G[par[p]][i]
                if v==p:
                    G[par[p]][i][2]+=1
            p=par[p]
        max_flow+=1
        augm,par=BFS2(G,s,t)
    return max_flow
#{# def BFS2(G,F,s,t):
#     n=len(G)

#     vis=[False for _ in range(n)]
#     par=[None for _ in range(n)]
#     #min_cap=[float('inf') for _ in range(n)]

#     Q=deque()
#     Q.append(s)
#     vis[s]=True

#     while len(Q)>0:
#         u=Q.popleft()
#         for v in G[u]:
#             if c>0:
#                 cp=1-F[u][v]
#                 if not vis[v] and cp>0:                    
#                     vis[v]=True
#                     par[v]=u
#                     #min_cap[v]=min(min_cap[u],cp)
#                     if v==t:
#                         return True,par
#                     Q.append(v)
#     return False,par

# def binworker2(M):
#     G=convert2(M)
#     print(G)
#     n=len(G)
#     max_flow=0
    
#     F=[[0 for _ in range(n)]for _ in range(n)]

#     # for u in range(n):
#     #     for el in G[u]:            

#     s=n-2
#     t=n-1
#     augm,par=BFS2(G,F,s,t)
#     while augm:
#         p=t
#         while p!=s:
#             #m=len(G[par[p]])
#             F[par[p]][p]+=1
#             F[p][par[p]]=1
#             p=par[p]
#         max_flow+=1
#         augm,par=BFS2(G,F,s,t)
#     return max_flow
#}

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
#runtests( binworker2, all_tests = False )

M = [ [ 0, 1, 3], # 0
[ 2, 4], # 1
[ 0, 2], # 2
[ 3 ], # 3
[ 3, 2] ] # 4
M2=[[0, 1], [0, 1], [0]]
print(binworker(M))