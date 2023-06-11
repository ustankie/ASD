def floyd(G):
    n=len(G)
    S=[[float('inf') for j in range(n)]for i in range(n)]
    P=[[None for _ in range(n)]for _ in range(n)]

    for u in range(n):
        for v,c in G[u]:
            S[u][v]=c
            P[u][v]=u
    #print(S)
    for u in range(n):
        S[u][u]=0


    for t in range(n):
        for u in range(n):
            for v in range(n):
                if S[u][v]>(S[u][t]+S[t][v]):
                    S[u][v]=(S[u][t]+S[t][v])
                    P[u][v]=P[t][v] 
    # print(*S,sep="\n")
    # print()
    return S,P


                
G=[[(1,1),(6,2)],[(0,1),(2,3),(4,3)],[(1,3),(5,5)],[(4,3),(7,1),(8,8)],[(1,3),(5,2),(3,3),(6,1)],[(2,5),(4,2),(8,1)],[(0,2),(4,1),(7,7)],[(6,7),(3,1)],[(3,8),(5,1)]]
G2=[[(1,1),(2,3)],[(0,1),(4,8),(3,5)],[(0,3),(3,4),(5,6)],[(2,4),(1,5),(4,7),(5,2)],[(1,8),(3,7)],[(2,6),(3,2)]]

S,P=floyd(G2)

print(*S,sep="\n")