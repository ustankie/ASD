from collections import deque
def bipartite(G):
    n=len(G)
    colors=[ None for _ in range(n)]

    Q=deque()
    Q.append(0)
    colors[0]=0
    
    while len(Q)>0:
        u=Q.popleft()
        for v in G[u]:
            if colors[v]==None:
                colors[v]=1-colors[u]
                Q.append(v)
            elif colors[v]==colors[u]:
                return False
    return True



G=[[1,3,5],[0,2,4],[1,3,5],[0,2,4],[1,3,5],[4]]
print(bipartite(G))