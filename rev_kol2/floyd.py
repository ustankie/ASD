def fw(G):
    n=len(G)
    S=[[float('inf')for _ in range(n)]for _ in range(n)]
    P=[[None for _ in range(n)]for _ in range(n)]
    for i in range(n):
        for j in range(n):
            if G[i][j]:
                S[i][j]=G[i][j]
                P[i][j]=i
    for u in range(n):
        S[u][u]=0
    for t in range(n):
        for x in range(n):
            for y in range(n):
                if S[x][y]>(S[x][t]+S[t][y]):
                    S[x][y]=(S[x][t]+S[t][y])
                    P[x][y]=P[t][y]
    return S,P

def transform(G):
    n=len(G)
    G2=[[0 for _ in range(n)]for _ in range(n)]
    for u in range(n):
        for v,c in G[u]:
            G2[u][v]=c
    return G2

G=[[(1,1),(6,2)],[(0,1),(2,3),(4,3)],[(1,3),(5,5)],[(4,3),(7,1),(8,8)],[(1,3),(5,2),(3,3),(6,1)],[(2,5),(4,2),(8,1)],[(0,2),(4,1),(7,7)],[(6,7),(3,1)],[(3,8),(5,1)]]
G2=[[(1,1),(2,3)],[(0,1),(4,8),(3,5)],[(0,3),(3,4),(5,6)],[(2,4),(1,5),(4,7),(5,2)],[(1,8),(3,7)],[(2,6),(3,2)]]

G=transform(G)
G2=transform(G2)
#print(*G2,sep="\n")
S,P=fw(G2)
print(*S,sep="\n")
#print(P)