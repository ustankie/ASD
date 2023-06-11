from zad9testy import runtests
from collections import deque
from copy import deepcopy
from queue import PriorityQueue
def BFS(G,s,t):
    n=len(G)

    par=[None for _ in range(n)]
    vis=[False for _ in range(n)]

    vis[s]=True
    Q=deque()
    Q.append(s)

    while len(Q)>0:
        u=Q.popleft()
        for v in range(n):
            if G[u][v]>0 and not vis[v]:
                vis[v]=True
                par[v]=u
                Q.append(v)
    T=[]
    p=t
    while p!=None:
        T.append(p)
        p=par[p]
    
    return T[::-1]

def transform(E):
    m=len(E)
    n=0
    for i in range(m):
        n=max(n,E[i][0],E[i][1])
    n+=1
    G=[[0 for _ in range(n)]for _ in range(n)]
    for i in range(m):
        G[E[i][0]][E[i][1]]=E[i][2]
    return G

def cap(G,path):
    n=len(path)
    min_cap=G[path[0]][path[1]]
    for i in range(1,n-1):
        min_cap=min(min_cap,G[path[i]][path[i+1]])
    return min_cap

def update(G,path,min_cap):
    n=len(path)
    for i in range(n-1):
        G[path[i]][path[i+1]]-=min_cap
        G[path[i+1]][path[i]]+=min_cap

def ff(G,s,t):
    flow=0
    G=deepcopy(G)

    path=BFS(G,s,t)
    while len(path)>1:
        min_cap=cap(G,path)
        flow+=min_cap
        update(G,path,min_cap)
        path=BFS(G,s,t)

    return flow


def count(G):
    n=len(G)

    capacity=[0 for _ in range(n)]
    for u in range(n):
        for v in range(n):
            capacity[u]+=G[v][u]
    max_cap=0
    for u in range(n):
        max_cap=max(max_cap,capacity[u])
    return capacity,max_cap
def BFS2(G,F,s,t):
    n=len(G)

    min_cap=[float('inf') for _ in range(n)]
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

def ff2(G,s,t):
    n=len(G)
    max_flow=0
    F=[[0 for _ in range(n)] for _ in range(n)]

    augm,par,min_cap=BFS2(G,F,s,t)
    while augm:
        p=t
        while p!=s:
            F[p][par[p]]=min_cap
            F[par[p]][p]+=min_cap
            p=par[p]
      
        max_flow+=min_cap
        augm,par,min_cap=BFS2(G,F,s,t)

    # R=[]
    # for u in range(n):
    #     for v in range(n):
    #         if G[u][v]:
    #             R.append(((u,v),F[u][v],G[u][v]))

    

    return max_flow
def maxflow( G2,s ):
    G=transform(G2)
    n=len(G)
    capacity,max_cap=count(G)
    Q=PriorityQueue()
    for i in range(n):
        Q.put((max_cap-capacity[i],i))
    row=[0 for _ in range(n)]
    for i in range(n):
        c,row[i]=Q.get()
    
    #print(capacity)

    G.append([0 for _ in range(n+1)])
    for i in range(n):
        G[i].append(0)
    
    flow=0
    cities=(0,0)

    i=0
    j=1
    while j<n:
        u=row[i]
        v=row[j]
        while v<n and capacity[row[i]]+capacity[row[j]]>flow:         
            G[u][n]=capacity[u]
            G[v][n]=capacity[v]
            c_flow=ff2(G,s,n)

            if c_flow>flow:
                flow=c_flow
                cities=(u,v)
            G[u][n]=0
            G[v][n]=0
            v+=1
        i+=1
        j=u+1

    return flow#,cities
    



# zmien all_tests na True zeby uruchomic wszystkie testy
runtests( maxflow, all_tests = True )
G = [(0,1,7),(0,3,3),(1,3,4),(1,4,6),(2,0,9),(2,3,7),(2,5,9),
(3,4,9),(3,6,2),(5,3,3),(5,6,4),(6,4,8)]
s=2
print(maxflow(G,s))