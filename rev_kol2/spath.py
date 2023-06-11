from collections import deque
def BFS(G,s,k):
    n=len(G)
    vis=[False for _ in range(n)]
    par=[None for _ in range(n)]

    Q=deque()
    Q.append(s)
    vis[s]=True

    while len(Q)>0:
        u=Q.popleft()
        for v in G[u]:
            if not vis[v]:
                vis[v]=True
                par[v]=u
                if v==k:
                    return par
                Q.append(v)
    
def spath(G,s,k):
    par=BFS(G,s,k)
    if par==None:
        return None,float('inf')
    T=[]
    p=k
    while p!=None:
        T.append(p)
        p=par[p]
    return T[::-1],len(T)-1

G=[[1],[0,5,6],[3,4,5],[6,5,2],[2],[1,2,3],[3,1]]
G2=[[1],[0,2],[1,6,7],[7],[7],[7],[2],[3,4,5,2]]

print(spath(G,0,5))