def build(T):
    m=len(T)
    n=0
    for i in range(m):
        n=max(n,T[i][1])
    G=[[]for _ in range(n+1)]
    #print(G)
    for i in range(m):
        G[T[i][0]].append(T[i][1])
    return G

def przedzialy(T,s,k):
    def Visit(G,u):
        if u==k: 
            return True
        vis[u]=True
        for v in G[u]:
            if v==k: 
                return True
            if not vis[v]:           
                par[v]=u
                Visit(G,v)

    G=build(T)
    #print(*G,sep="\n")
    n=len(G)
    vis=[False for _ in range(n)]
    par=[None for _ in range(n)]

    vis[s]=True
    for u in G[s]:
        if not vis[u]:
            if(Visit(G,u)): 
                return True

    return False
            


T=[(1,3),(2,5),(3,4),(1,2)]
print(przedzialy(T,1,4))