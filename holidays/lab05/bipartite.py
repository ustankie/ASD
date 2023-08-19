from collections import deque
def bipartite(G):
    n=len(G)
    d=[None for _ in range(n)]
    d[0]=0
    Q=deque()
    Q.append(0)
    while len(Q)>0:
        u=Q.popleft()
        for v in G[u]:
            if d[v]==None:
                d[v]=d[u]+1
                Q.append(v)
            elif d[v]%2==d[u]%2:
                return False
    return True
G=[[1,3,5],[0,2,4],[1,3,5],[0,2,4,5],[1,3,5],[4,2,0,3]]
print(bipartite(G))