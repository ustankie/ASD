from copy import deepcopy
def dag_list(E):
    n = max(u for edge in E for u in edge) + 1
    G = [[] for _ in range(n)]
    for u, v in E:
        G[u].append(v)
    return G

def getpaths(par,s,t,T,curr=[]):
    n=len(par)
    if t==s:
        T.append([t]+curr)
        return
    for v in par[t]:  
        getpaths(par,s,v,T,[t]+curr)
def paths(G,s,t):
    def DFS(u):
        vis[u]=True
        for v in G[u]:
            if not vis[v]:
                DFS(v)
            count[u]+=count[v]
            par[v].append(u)

                
    n=len(G)
    par=[[] for _ in range(n)]
    vis=[False for _ in range(n)]
    count=[0 for _ in range(n)]
    count[t]=1
    

    DFS(s)
    #print(*par,sep="\n")
    T=[]
    getpaths(par,s,t,T)


    return count[s],T





E = [(0, 1), (1, 2), (2, 3), (3, 4), (4, 5), (2, 6), (1, 6), (6, 3), (6, 9), (9, 10), (6, 7), (7, 10),
     (7, 8), (10, 11), (11, 8), (8, 4)]

G = dag_list(E)
print(paths(G,0,5))