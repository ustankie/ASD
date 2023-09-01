from math import sqrt,ceil

def make_edge_list(G):
    n=len(G)
    E=[]

    for i in range(n-1):
        for j in range(i+1,n):
            dist=sqrt((G[j][1]-G[i][1])*(G[j][1]-G[i][1])+(G[j][0]-G[i][0])*(G[j][0]-G[i][0]))
            E.append((i,j,dist))
    return E
def perform_DFS(G):
    n=len(G)
    vis=[False for _ in range(n)]
    R=[]
    count=0

    def DFS(u):
        nonlocal count
        count+=1
        vis[u]=True
        for v in G[u]:
            if not vis[v]:
                DFS(v)

    DFS(0)
    # for i in range(n):
    #     if not vis[i]:
    #         return False
    # return True
    return count==n

def edges_to_graph(E,n):
    m=len(E)
    G=[[]for _ in range(n)]
    for i in range(m):
        G[E[i][1]].append(E[i][0])
        G[E[i][0]].append(E[i][1])
    return G
def add_edge(G,e):
    G[e[0]].append(e[1]) 
    G[e[1]].append(e[0]) 

def remove_edge(G,e):
    u=e[0]
    v=e[1]
    
    
    for w in range(len(G[u])):
        # print(len(G[u]),w)
        if G[u][w]==v:
            G[u]=G[u][:w]+G[u][w+1:]
            break

    for w in range(len(G[v])):
        if G[v][w]==u:
            G[v]=G[v][:w]+G[v][w+1:]
            break

def highway(G):
    n=len(G)
    E=make_edge_list(G)
    E.sort(key=lambda x: x[2])
    m=len(E)
    # print(E)
    G2=edges_to_graph(E[:n-2],n)
    min_diff=float('inf')
    i=0
    j=n-1
    while j-i>=n-2 and j<m:
        # print(i,j,G2)
        if not perform_DFS(G2):
            j+=1
            if j<m:
                add_edge(G2,E[j])
        elif  perform_DFS(G2):
            min_diff=min(min_diff,E[j][2]-E[i][2])
            remove_edge(G2,E[i])
            i+=1
        
        
    return ceil(min_diff)



P = [(4, 4), (2, 3), (4.5, 0), (0, 0), (1, -1), (3, -2), (2, -4), (-1, 2), (-2, -2), (-4, 4), (-5, 0)]
P = [(5, 5), (3, -5), (0, 3), (-5, 0)]
print(highway(P))

