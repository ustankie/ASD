
def DFS(G):
    def Visit(G,u):
        nonlocal time
        visited[u]=True
        for v in G[u]:
            if not visited[v]:
                parent[v]=u
                Visit(G,v)
        time+=1

    n=len(G)
    visited=[False for _ in range(n)]
    parent=[None for _ in range(n)]
    time=0

    for u in range(n):
        if not visited[u]:
            Visit(G,u)
    
    return visited, parent

    
G=[[1],[0,5,6],[3,4,5],[6,5,2],[2],[1,2,3],[3,1]]

print(DFS(G))