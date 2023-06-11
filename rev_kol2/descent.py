from queue import PriorityQueue
def edges(G):
    E=[]
    n=len(G)

    for u in range(n):
        for v,c in G[u]:
            if u<v:
                E.append((c,(u,v)))

    return E
def partition(T,l,p):
    n=len(T)
    x=T[p][0]

    i=l-1

    for j in range(l,p):
        if T[j][0]>x:
            i+=1
            T[i],T[j]=T[j],T[i]
    i+=1
    T[i],T[p]=T[p],T[i]
    return i

def quicksort(T,l,p):
    while l<p:
        q=partition(T,l,p)
        if p-q>q-l:
            quicksort(T,l,q-1)
            l=q+1
        else:
            quicksort(T,q+1,p)
            p=q-1

def build_path(par,s,t):
    if len(par[t])==0:
        return []
    T=[t]
    p=par[t][-1][1]
    prev_d=par[t][-1][0]
    prev_c=par[t][-1][2]

    while p!=s:
        T.append(p)       
        q=p
        i=len(par[q])-1
        dc,p,c=par[q][i]
        while i>0 and dc+prev_c!=prev_d:
            i-=1
            dc,p,c=par[q][i]
        prev_d=dc
        prev_c=c
    T.append(p)    
    return T[::-1]

def descent(G,s,t):
    E=edges(G)
    m=len(E)
    quicksort(E,0,m-1)
    print(E)
    n=len(G)

    d=[float('inf') for _ in range(n)]  
    par=[[] for _ in range(n)]
    
    d[s]=0

    for i in range(m):
        u=E[i][1][0]
        v=E[i][1][1]
        c=E[i][0]
        if d[u]<d[v]:
            if d[v]>d[u]+c:
                d[v]=d[u]+c
                par[v].append((d[v],u,c))            
        elif d[v]<d[u]:
            if d[u]>d[v]+c:
                d[u]=d[v]+c
                par[u].append(((d[u],v,c)))
    
    return build_path(par,s,t),d[t]


    
def undirected_weighted_graph_list(E: 'array of edges'):
    # Find a number of vertices
    n = 0
    for e in E:
        n = max(n, e[0], e[1])
    n += 1
    # Create a graph
    G = [[] for _ in range(n)]
    for e in E:
        G[e[0]].append((e[1], e[2]))
        G[e[1]].append((e[0], e[2]))
    return G



E = [(0, 1, 1), (1, 2, 4), (2, 3, 3), (0, 5, 40), (5, 6, 38), (0, 7, 5), (6, 7, 8), (7, 1, 6),
     (7, 2, 16), (6, 2, 23), (6, 8, 35), (5, 4, 30), (8, 4, 20), (8, 3, 15), (4, 3, 80)]

G = undirected_weighted_graph_list(E)
s=2
t=0
print(descent(G,s,t))