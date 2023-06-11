from collections import deque
def tree_diameter(G,K):
    def Visit(G,u):
        for v in G[u]:
            if not vis[v]:
                d[v]=d[u]+1
                vis[v]=True
                Visit(G,v)

    n=len(G)
    m=len(K)
    vis=[False for _ in range(n)]
    d=[0 for _ in range(n)]
    time=0


    vis[K[0]]=True
    Visit(G,K[0])
    max_ind=0
    max_num=0
    for i in range(m):
        if d[K[i]]>max_num :
            max_num=d[K[i]]
            max_ind=K[i]
    
    vis=[False for _ in range(n)]
    d=[0 for _ in range(n)]
    vis[max_ind]=True
    Visit(G,max_ind)
    max_num=0
    max_ind2=0
    for i in range(m):
        if d[K[i]]>max_num :
            max_num=d[K[i]]
            max_ind2=K[i]
    
    return max_num,max_ind,max_ind2
def BFS(G,K):
    n=len(G)
    k=len(K)
    vis=[False for _ in range(n)]
    d=[0 for _ in range(n)]
    par=[None for _ in range(n)]

    Q=deque()
    Q.append(K[0])
    vis[K[0]]=True
    
    sum=0
    count=0

    while len(Q)>0:
        u=Q.popleft()
        for v in G[u]:
            if not vis[v]:
                par[v]=u
                vis[v]=True
                d[v]=d[u]+1
                Q.append(v)
    #vis=[False for _ in range(n)]
    G=[[]for _ in range(n)]
    for i in range(1,k):
        u=K[i]
        while par[u]!=None and not u in G[par[u]]:           
            G[par[u]].append(u)
            G[u].append(par[u])
            u=par[u]
    sum=0
    for u in range(n):
        sum+=len(G[u])
    return sum

def delivery(G,K):
    a=BFS(G,K)
    b,s,t=tree_diameter(G,K)

    return a-b,s,t


def undirected_graph_list(E: 'array of edges', n: 'number of vertices'):
    G = [[] for _ in range(n)]
    for edge in E:
        G[edge[0]].append(edge[1])
        G[edge[1]].append(edge[0])
    return G

E = [(0, 1), (1, 2), (1, 3), (3, 4), (4, 5), (5, 6), (4, 7), (7, 10), (10, 11), (11, 12), (11, 13), 
     (10, 14), (7, 8), (8, 9), (7, 15), (15, 16), (15, 18), (17, 18), (15, 19), (15, 20), (20, 21),
     (20, 22), (22, 23), (22, 24), (20, 25), (25, 26), (25, 27), (27, 28), (28, 29), (28, 30)]
C = [3, 5, 13, 14, 16, 15, 17, 23, 24, 25, 27, 30]
        
G=undirected_graph_list(E,31)
#print(*G,sep="\n")  
print(delivery(G,C))
# print(A)
# print(cost)

