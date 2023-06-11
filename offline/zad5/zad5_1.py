from zad5testy import runtests
from collections import deque

def adjacent(E,S,T,n):
    G=[[]for _ in range(n)] 
    k=len(S)
    for i in range(k):
        T[S[i]]=1

    m=len(E)
    for i in range(m):
        G[E[i][0]].append((E[i][1],E[i][2]))
        G[E[i][1]].append((E[i][0],E[i][2]))
    return G

def find_min(cost,vis):
    n=len(cost)
    min_c=float('inf')
    ind=0
    
    for i in range(n):
        if not vis[i] and cost[i]<min_c:
            min_c=cost[i]
            ind=i
    return ind

def spacetravel( n, E, S, a, b ):
    T=[0 for _ in range(n)]
    G=adjacent(E,S,T,n)

    par=[None for _ in range(n)]
    vis=[False for _ in range(n)]
    vis2=[False for _ in range(n)]
    cost=[float('inf') for _ in range(n)]

    Q=deque()
    Q.append(a)
    vis[a]=True
    cost[a]=0

    u=a    
    while u!=b and len(Q)>0:
        p=Q.popleft()
        for i in G[p]:
            v=i[0]
            if not vis2[v]:
                vis2[v]=True
                Q.append(v)
        if T[p]:
            for v in S:
                if not vis2[v]:
                    vis2[v]=True
                    Q.append(v)
        vis[u]=True
        if T[u]:
            for v in S:
                if cost[u]<cost[v]:
                    cost[v]=cost[u]

        for i in G[u]: 
            #print(i)

            v=i[0]
            c=i[1]
            if cost[v]>(cost[u]+c):
                cost[v]=(cost[u]+c)
                par[v]=u
            
        u=find_min(cost,vis)
    for i in range(n):
        print((i,cost[i]),end="  ")
        
    if len(Q)==0 and u!=b:
        return None



    return cost[b]


    




# zmien all_tests na True zeby uruchomic wszystkie testy
runtests( spacetravel, all_tests = False )
E = [(0,1, 5),
(1,2,21),
(1,3, 1),
(2,4, 7),
(3,4,13),
(3,5,16),
(4,6, 4),
(5,6, 1)]
S = [ 0, 2, 3 ]
a = 1
b = 5
n = 7

print(spacetravel(n,E,S,a,b))