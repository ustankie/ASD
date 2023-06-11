from queue import PriorityQueue
def reverse(G):
    n=len(G)
    G2=[[]for _ in range(n)]

    for u in range(n):
        for v in G[u]:
            G2[v].append(u)
    return G2
    
def strong(G):
    def DFS(G,u):
        nonlocal t
        for v in G[u]:
            if not vis[v]:
                vis[v]=True
                DFS(G,v)
        time[u]=t+1
        t+=1

        T.append(u)

    n=len(G)
    t=0
    time=[0 for _ in range(n)]
    vis=[False for _ in range(n)]
    T=[]

    for u in range(n):
        if not vis[u]:
            vis[u]=True
            DFS(G,u)
    print(time)
    
    G2=reverse(G)
    vis=[False for _ in range(n)]
    
    Q=PriorityQueue()

    for u in range(n):
        m=n-time[u]
        Q.put((m,u))
    print(Q.queue)

    R=[]

    while not Q.empty():        
        t,u=Q.get()
        while not Q.empty() and vis[u]:
            t,u=Q.get()
        if not vis[u]:
            T=[]           
            vis[u]=True
            DFS(G2,u)
            R.append(T)
    return R
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
G=[[1],[2],[0,3,7],[5],[3],[6],[4,7],[10,8],[9],[7],[9]]
E = [(0, 1), (1, 2), (3, 2), (2, 4), (4, 1), (4, 5), (5, 6), (6, 7), (7, 8), (8, 9), (9, 6),
     (4, 7), (4, 6), (5, 9), (10, 0), (15, 14), (15, 11), (15, 11), (11, 13), (14, 13), (5, 13),
     (16, 8), (0, 12), (12, 3)]
E = [(0, 1), (1, 2), (3, 2), (2, 4), (4, 1), (4, 5), (6, 7), (7, 8), (8, 9), (9, 6)]

G=transform(E)
print(strong(G))




