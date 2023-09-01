def closure(G):
    n=len(G)
    S=[[False for _ in range(n)]for _ in range(n)]

    for u in range(n):
        S[u][u]=True
        for v in G[u]:
            S[u][v]=True
    
    for t in range(n):
        for u in range(n):
            for v in range(n):
                S[u][v]=S[u][v] or (S[u][t] and S[t][v])
    
    G2=[[]for _ in range(n)]
    for u in range(n):
        for v in range(u+1,n):
            if S[u][v]:
                G2[u].append(v)
                G2[v].append(u)
    return G2


G=[[1,2],[0,2,5],[0,4],[8],[2],[1,6],[5,7],[6],[3,9],[8]]
print(closure(G))