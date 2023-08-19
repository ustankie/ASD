from collections import deque

def comp(G):
    n = len(G)
    vis = [False for _ in range(n)]

    def DFS(G, u):
        vis[u] = True
        for v in G[u]:
            if not vis[v]:
                vis[v] = True
                DFS(G, v)

    count = 0

    for u in range(n):
        if not vis[u]:
            count += 1
            DFS(G, u)

    return count

def comp2(G):
    n=len(G)
    d=[None for _ in range(n)]
    
    def BFS(s):
        Q=deque()
        d[s]=0
        Q.append(s)
        while len(Q)>0:
            u=Q.popleft()
            for v in G[u]:
                if d[v]==None:
                    d[v]=d[u]+1
                    Q.append(v)

    count = 0
    for i in range(n):
        if d[i]==None:
            count+=1
            BFS(i)
    return count

G=[[],[2],[1,3],[2],[5,6],[4,6],[4,5],[8],[7],[]]
print(comp2(G))