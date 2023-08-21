def good_beginning(G):
    
    def DFS(G,u):
        vis[u]=True
        for v in G[u]:
            if not vis[v]:
                vis[v]=True
                DFS(G,v)
        T.append(u)
        #print(T)
    n=len(G)
    vis=[False for _ in range(n)]
    T=[]
    #vis[0]=True
    for u in range(n):
        if not vis[u]:
            DFS(G,u)
    #print(T)
    a=T[len(T)-1]
    vis=[False for _ in range(n)]
    T=[]
    DFS(G,a)
    if len(T)==n:
        return a


    return None
G=[[1,2],[2,4],[],[],[3,6,5],[],[]]
G2=[[]]
print(good_beginning(G))