from zad3EK import edmonds_karp
from zad3tests import runtests
def floyd(G):
    n=len(G)
    S=[[float('inf') for _ in range(n)]for _ in range(n)]
    for u in range(n):
        S[u][u]=0
        for v in range(n):
            if G[u][v]:
                S[u][v]=G[u][v]

    for t in range(n):
        for x in range(n):
            for y in range(n):
                S[x][y]=min(S[x][y],S[x][t]+S[y][t])
    return S
def BlueAndGreen(G,K,d):
    n=len(G)
    S=floyd(G)
    G2=[[0 for _ in range(n+2)]for _ in range(n+2)]
    for u in range(n):
        for v in range(n):
            if K[u]!=K[v] and S[u][v]>=d:
                G2[u][v]=1
    for u in range(n):
        sum=1
        # for v in range(n):
        #     if G2[u][v]>0:
        #         sum+=G2[u][v]
        if K[u]=='B':
            G2[n][u]=sum
        else:
            G2[u][n+1]=sum
    #print(*G2,sep="\n")
    return edmonds_karp(G2,n,n+1)

G = [
      [0, 1, 1, 0, 1],
      [1, 0, 0, 1, 0],
      [1, 0, 0, 0, 1],
      [0, 1, 0, 0, 1],
      [1, 0, 1, 1, 0],
     ]
K = ['B', 'B', 'G', 'G', 'B']
D = 2

#print(BlueAndGreen(G,K,D))
runtests(BlueAndGreen)

