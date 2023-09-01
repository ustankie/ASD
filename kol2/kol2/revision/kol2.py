from kol2testy import runtests
from queue import PriorityQueue

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
    return count==n
def graph_to_edges(G):
    n=len(G)
    edges=[]

    for u in range(n):
        for v,c in G[u]:
            if u<v:
                edges.append((u,v,c))
    edges.sort(key=lambda x:x[2])
    return edges

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
        if G[u][w]==v:
            G[u]=G[u][:w]+G[u][w+1:]
            break

    for w in range(len(G[v])):
        if G[v][w]==u:
            G[v]=G[v][:w]+G[v][w+1:]
            break
def beautree(G):
    n=len(G)
    E=graph_to_edges(G)
    
    m=len(E)
    G2=edges_to_graph(E[:n-1],n)
    min_diff=float('inf')
    prefix_sum=[0 for _ in range(m)]

    prefix_sum[0]=E[0][2]
    for i in range(1,m):
        prefix_sum[i]=prefix_sum[i-1]+E[i][2]
    

    for i in range(m-n+1):
        if perform_DFS(G2):
            
            if i==0:
                diff=prefix_sum[i+n-2]
            else:
                diff=prefix_sum[i+n-2]-prefix_sum[i-1]
            min_diff=min(min_diff,diff)
        if i<m-n:
            remove_edge(G2,E[i])
            add_edge(G2,E[i+n-1])
    if min_diff==float('inf'):
        min_diff=None
    return min_diff

G = [ [(1,3), (2,1), (4,2)],
[(0,3), (2,5) ],
[(1,5), (0,1), (3,6)],
[(2,6), (4,4) ],
[(3,4), (0,2) ] ]

# print(beautree(G))
        
        



    

G = [ [(1,3), (2,1), (4,2)],
[(0,3), (2,5) ],
[(1,5), (0,1), (3,6)],
[(2,6), (4,4) ],
[(3,4), (0,2) ] ]
Ge2 = [ [(1,2), (2,3)], # 0
        [(0,2), (2,1), (3,5), (4,6)], # 1
        [(0,3), (1,1), (3,9), (4,4)], # 2
        [(1,5), (2,9), (4,10), (5,8)], # 3
        [(2,4), (1,6), (3,10), (5,7)], # 4
        [(3,8), (4,7)] ] # 5
runtests( beautree, all_tests = True )
# print(beautree(Ge2))