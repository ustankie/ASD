from queue import PriorityQueue
def reverse(G):
    n=len(G)
    G2=[[] for _ in range(n)]

    for u in range(n):
        for v in G[u]:
            G2[v].append(u)
    
    return G2

def strong_parts(G):
    n = len(G)
    t = 0
    time = [0 for _ in range(n)]
    vis = [False for _ in range(n)]
    T=[]

    def DFS(G,u):
        nonlocal t
        vis[u]=True

        for v in G[u]:
            if not vis[v]:    
                DFS(G,v)
        t+=1
        time[u]=t
        T.append(u)
    
    for u in range(n):
        if not vis[u]:
            DFS(G,u)

    G2=reverse(G)
    vis = [False for _ in range(n)]

    Q=PriorityQueue()

    for u in range(n):
        m=n-time[u]
        Q.put((m,u))
    
    R=[]

    while not Q.empty():
        t,u=Q.get()

        if not vis[u]:
            T=[]
            #vis[u]=True
            DFS(G2,u)
            R.append(T)
    return R

G=[[1],[2],[0,3,7],[5],[3],[6],[4,7],[10,8],[9],[7],[9]]
print(strong_parts(G))

