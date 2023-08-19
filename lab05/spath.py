from collections import deque
def spath(G,s,k):
    n=len(G)
    vis=[False for _ in range(n)]
    val=[None for _ in range(n)]
    par=[None for _ in range(n)]

    Q=deque()
    Q.append(s)
    vis[s]=True
    val[s]=0

    while len(Q)>0:
        u=Q.popleft()
        for v in G[u]:
            if not vis[v]:
                val[v]=val[u]+1
                par[v]=u
                vis[v]=True
                Q.append(v)

                if v==k:
                    p=v
                    T=deque()
                    while par[p]!=s:
                        T.append(p)
                        p=par[p]
                    T.append(p)
                    T.append(s)
                    reverse(T)
                    return val[v],T
                
    return -1
def reverse(T):
    n=len(T)
    for i in range(n//2):
        T[i],T[n-i-1]=T[n-1-i],T[i]
G=[[1],[0,5,6],[3,4,5],[6,5,2],[2],[1,2,3],[3,1]]
G2=[[1],[0,2],[1,6,7],[7],[7],[7],[2],[3,4,5,2]]

print(spath(G2,0,5))