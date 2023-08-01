from zad9testy import runtests
from collections import deque

def findmax(E):
    m=len(E)
    maxi=0
    max_weight=0
    for i in range(m):
        maxi=max(E[i][0],E[i][1],maxi)
        max_weight=max(max_weight,E[i][2])
    return maxi
def transform(E,s):
    m=len(E)
    maxi=findmax(E)
    max_cap=0
    
    n=maxi+2
    G=[[0 for _ in range(n)]for _ in range(n)]
    for i in range(m):
        #if E[i][1]!=s:
        G[E[i][0]][E[i][1]]=E[i][2]
        # if E[i][0]!=s:
        #     G[E[i][1]][E[i][0]]=E[i][2]
    capacity=[0 for _ in range(n)]
    for i in range(n):
        for j in range(n):
            capacity[j]+=G[i][j]
    max_cap=max(capacity)
    return G,max_cap,capacity
def BFS(G,F,s,t):
    n=len(G)
    min_cap=[float('inf')for _ in range(n)]
    par=[None for _ in range(n)]
    vis=[False for _ in range(n)]

    Q=deque()
    Q.append(s)
    vis[s]=True

    while len(Q)>0:
        u=Q.popleft()
        for v in range(n):
            c=G[u][v]-F[u][v]
            if c>0 and not vis[v]:
                par[v]=u
                vis[v]=True
                min_cap[v]=min(min_cap[u],c)
                if v==t:
                    return True,par,min_cap[t]
                Q.append(v)
    return False,par,0

def flow(G,s,t):
    n=len(G)
    max_flow=0
    F=[[0 for _ in range(n)]for _ in range(n)]

    augm,par,min_cap=BFS(G,F,s,t)
    while augm:
        p=t
        while p!=s:
            F[p][par[p]]=min_cap
            F[par[p]][p]+=min_cap
            p=par[p]
        max_flow+=min_cap
        augm,par,min_cap=BFS(G,F,s,t)
    return max_flow

def maxflow( E,s ):
    G,max_cap,capacity=transform(E,s)
    n=len(G)-1
    row=[(capacity[i],i) for i in range(n)]
    row.sort(key=lambda x: x[0],reverse=True)

    print(row)
    max_flow=0      

    i=0
    j=1
    while j<n:    
        u=row[i][1]
        v=row[j][1]
        while v<n and capacity[u]+capacity[v]>max_flow:
            #if s!=u and v!=s:
            G[u][n]=max_cap
            G[v][n]=max_cap
            max_flow=max(flow(G,s,n),max_flow)

            G[u][n]=0
            G[v][n]=0
            v+=1
        i+=1
        j=u+1
    return max_flow

    

# zmien all_tests na True zeby uruchomic wszystkie testy
runtests( maxflow, all_tests = True )
s=0
G =  [(0, 1, 10), (1, 2, 2), (1, 3, 5), (1, 4, 3)]
s=2
G=[(0, 1, 7),
(0, 3, 3),
(1, 3, 4),
(1, 4, 6),
(2, 0, 9),
(2, 3, 7),
(2, 5, 9),
(3, 4, 9),
(3, 6, 2),
(5, 3, 3),
(5, 6, 4),
(6, 4, 8)]

print(maxflow(G,s))