from collections import deque

def descent(G,s,k):
    def Visit(G,v,pk):

        vis[v]=True
        for u in range(n):
            if G[v][u] and G[v][u]<pk:
                par[u]=v
                Visit(G,u,G[v][u])
                if v==k:
                    return
    n=len(G)
    vis=[False for _ in range(n)]
    par=[None for _ in range(n)]
    vis[s]=True

    Visit(G,s,100)

    if not vis[k]:
        return None, -1
    
    T=deque()
    p=k
    cost=0

    while par[p]!=s:
        T.append(p)
        cost+=G[par[p]][p]
        p=par[p]
    T.append(p)
    cost+=G[par[p]][p]
    T.append(s)
    return reverse(T),cost


def reverse(T):
    n=len(T)
    for i in range(n//2):
        T[i],T[n-i-1]=T[n-1-i],T[i]
    return T

G=[[0,1,0,4,3,0,0],[1,0,1,0,0,0,0],[0,1,0,0,0,0,0],[4,0,0,0,0,2,3],[3,0,0,0,0,2,0],[0,0,0,2,2,0,1],[0,0,0,3,0,1,0]]
print(descent(G,0,6))