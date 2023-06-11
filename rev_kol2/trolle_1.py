from collections import deque
def BFS(G,low,d):
    n=len(G)
    Q=deque()
    Q.append(0)
    I=[]
    vis=[False for _ in range(n)]
    cont=True
    while len(Q)>0 and cont:
        u=Q.popleft()
        for v in G[u]:
            if not vis[v]:
                vis[v]=True
                if d[v]==low[v] and v!=0:
                    I.append(v)
                    cont=False
                Q.append(v)
    return I
def trolle(G,C):
    def DFS(u):
        nonlocal time
        vis[u]=True
        d[u]=time
        low[u]=min(d[u],low[u])
        time+=1
        for v in G[u]:
            if not vis[v]:
                par[v]=u
                DFS(v)
                low[u]=min(low[u],low[v])
            elif v!=par[u]:
                low[u]=min(low[u],d[v])
    def DFS2(u,t):
        vis[u]=True
        for v in G[u]:
            if not vis[v]:
                t= DFS2(v,t+C[v])
        return t

    n=len(G)
    vis=[False for _ in range(n)]
    par=[None for _ in range(n)]
    d=[float('inf') for _ in range(n)]
    t=[0 for _ in range(n)]
    low=[float('inf') for _ in range(n)]
    time=0

    for u in range(n):
        if not vis[u]:
            DFS(u)
    print(low)
    print(d)
    I=BFS(G,low,d)
    print(I)
    e=None
    max_trol=0
    m=len(I)



    for j in range(m):
            i=I[j]
            vis=[False for _ in range(n)]
            vis[i]=True
            vis[par[i]]=True
            a=DFS2(i,C[i])

            if max_trol<a:
                max_trol=a
                e=(par[i],i)


    
    return e,max_trol

def transform(E):
    m=len(E)
    G=[[]]
    for u,v in E:
        while u>(len(G)-1):
            G.append([])
        while v>(len(G)-1):
            G.append([])
        G[u].append(v)
        G[v].append(u)
    return G
        
        




E = [(0, 1), (0, 2), (0, 3), (3, 4), (3, 5), (3, 6)]
C = [0, 5, 5, 4, 2, 2, 1]


E1 = [(0, 1), (1, 2), (2, 0), (3, 1), (3, 0), (4, 3), (5, 3), (5, 7), (5, 6), (6, 7), (0, 8), (8, 9),
     (9, 10), (8, 10), (10, 11), (11, 12), (12, 13), (11, 13)]
C1 = [0, 2, 8, 1, 7, 3, 5, 4, 3, 1, 2, 4, 5, 2]

E2 = [(0, 1), (1, 2), (1, 3), (3, 0), (3, 4), (4, 8), (8, 5), (4, 6), (6, 8), (7, 6)]
C2 = [0, 2, 7, 13, 5, 2, 3, 1, 5]


E3 = [(0, 1), (1, 2), (3, 0), (3, 2)]  # Brak mostów w tym grafie, więc nie opłaca się nic wysadzać
C3 = [0, 3, 10, 7]
G=transform(E2)
print(*G,sep="\n")
print(trolle(G,C2))
