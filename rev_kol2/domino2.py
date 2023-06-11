from collections import deque
from queue import PriorityQueue
def transform(D):
    n=len(D)
    G=[]
    for i in range(n):
        a,b=D[i]
        while a>(len(G)-1):
            G.append([])
            #print(a)
        while b>(len(G)-1):
            G.append([])
            #print(b)
        G[a].append(b)
    return G

def reverse(G):
    n=len(G)
    G2=[[]for _ in range(n)]
    for u in range(n):
        for v in G[u]:
            G2[v].append(u)
    return G2
def domino(D):
    def DFS(G,u,T):
        nonlocal time
        nonlocal num
        for v in G[u]:
            if not vis[v]:
                vis[v]=True          
                DFS(G,v,T)                
        d[u]=time 
        time+=1
        T.append(u)
        comp[u]=num

    G=transform(D)
    time=0
    num=0
    n=len(G)
    vis=[False for _ in range(n)]
    comp=[-1 for _ in range(n)]
    d=[0 for i in range(n)]
    T=[]

    for u in range(n):
        if not vis[u]:
            vis[u]=True
            DFS(G,u,T)
    #print(d)
    G2=reverse(G)
    Q=PriorityQueue()

    for i in range(n):
        Q.put((n-d[i],i))
    #print(Q.queue)
    vis=[False for _ in range(n)]
    comp=[-1 for _ in range(n)]
    R=[]
    while not Q.empty():
        c,u=Q.get()
        if not vis[u]:
            T=[]
            vis[u]=True
            DFS(G2,u,T)
            #print(T)
            #print(R)
            R.append(T)
            num+=1
            
    count=0
    A=[]
    I=ingoing(G,comp)
    for i in range(len(R)):
        incoming=True
        for j in R[i]:
            if I[j]:
                incoming=False
                break
        if incoming:
            A.append(R[i][0])

    return A,len(A)
def ingoing(G,comp):
    n=len(G)
    I=[False for _ in range(n)]
    for u in range(n):
        for v in G[u]:
            if comp[u]!=comp[v]:
                I[v]=True

    return I
G=[[1],[2],[0,3,7],[5],[3],[6],[4,7],[10,8],[9],[7],[9]]


E = [(0, 1), (1, 2), (3, 2),  (4, 1), (4, 5), (5, 6), (6, 7), (7, 8), (8, 9), (9, 6),(2,4),
     (4, 7), (4, 6), (5, 9), (10, 0), (15, 14), (15, 11), (15, 11), (11, 13), (14, 13), (5, 13),
     (16, 8), (0, 12), (12, 3)]
E1 = [(0, 1), (1, 2), (3, 2), (2, 4), (4, 1), (4, 5), (5, 6), (6, 7), (7, 8), (8, 9), (9, 6)]

print(domino(E1))