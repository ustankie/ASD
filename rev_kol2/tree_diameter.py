

def undirected_graph_list(E: 'array of edges'):
    # Find a number of vertices in a graph
    n = 0
    for edge in E:
        n = max(n, edge[0], edge[1])
    n += 1
    
    G = [[] for _ in range(n)]
    for edge in E:
        G[edge[0]].append(edge[1])
        G[edge[1]].append(edge[0])
    return G


def tree_diameter(G):
    n=len(G)
    max_path=[0 for _ in range(n)]
    max_global=0
    vis=[False for _ in range(n)]

    def rec(G,s,max_path):
        nonlocal max_global
        max1=-1
        max2=-1
        for v in G[s]:
            if not vis[v]:
                vis[v]=True
                a=rec(G,v,max_path)
            else:
                a=max_path[v]
            if a>=max1:
                max2=max1
                max1=a
            elif a>max2:
                max2=a
        #print(max1,max2)
        if len(G[s])==1:
            max_path[s]=0
        else:
            max_path[s]=max(max_path[s],max(max1,max2)+1)
        if max1>=0 and max2>=0:
            max_global=max(max_global,max1+max2+2)
        else:
            max_global=max(max_global,max(max1,max2)+1)
        
        
        return max_path[s]
    rec(G,0,max_path)
    return max_global
def tree_diameter2(G):
    def Visit(G,u):
        for v in G[u]:
            if not vis[v]:
                d[v]=d[u]+1
                vis[v]=True
                Visit(G,v)

    n=len(G)
    vis=[False for _ in range(n)]
    d=[0 for _ in range(n)]
    time=0


    vis[0]=True
    Visit(G,0)
    max_ind=0
    max_num=0
    for i in range(n):
        if d[i]>max_num:
            max_num=d[i]
            max_ind=i
    
    vis=[False for _ in range(n)]
    d=[0 for _ in range(n)]
    vis[max_ind]=True
    Visit(G,max_ind)
    return max(d)


E = [(0, 1), (1, 2), (2, 3), (3, 4), (3, 5), (2, 6), (6, 7), (2, 8), (8, 9), (8, 10), (10, 17),
     (10, 16), (10, 15), (10, 11), (11, 12), (11, 13), (11, 14), (0, 18), (18, 21), (18, 19),
     (19, 20), (18, 22), (22, 23), (23, 24), (23, 25), (23, 26), (28, 27), (22, 27), (22, 29), (29, 30)]
E1 = [(0, 1)]
E3 = [(0, 1), (0, 2)]
G=undirected_graph_list(E3)
print(G)
print(tree_diameter2(G))