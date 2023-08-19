def is_directed(G):
    n=len(G)
    G1=[[0 for _ in range(n)]for _ in range(n)]
    edges=0

    for u in range(n):
        for v in G[u]:
            G1[u][v]+=1
            if  G1[v][u]>G1[u][v]:
                edges+=1
            else:
                edges-=1

    return edges!=0

def undirected_graph_list(E):
    n = 0
    for edge in E:
        n = max(n, edge[0], edge[1])
    n += 1
    G = [[] for _ in range(n)]
    for edge in E:
        G[edge[0]].append(edge[1])
        G[edge[1]].append(edge[0])
    return G

E = [(0, 1), (1, 2), (2, 5), (5, 6), (6, 8), (7, 8), (0, 7), (0, 3), (1, 3), (1, 4), (3, 4), (2, 4), 
     (4, 5), (7, 3), (3, 8), (8, 5)]
G = undirected_graph_list(E)

print(is_directed(G))

